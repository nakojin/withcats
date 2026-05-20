# 런타임 읽기/쓰기 경로 검증 보고서 (Runtime Path Audit)

본 보고서는 **야옹야옹 AI 스튜디오 / YaongYaong AI Studio**의 지식 저장소(`withcats`) 폴더 구조 변경(v2)에 앞서, AI Studio 엔진(VS Code 확장 프로그램 소스 코드)이 런타임 환경에서 실제로 어떤 경로에 데이터를 읽고 쓰는지(Read/Write) 정밀 추적하고 검증한 보고서입니다.

---

## 1. 전수 조사 개요

* **조사 및 검증 대상**: `E:\ai_projects\yaongyaong_ai_studio\src\extension.ts` (엔진 코어 로직)
* **추적 키워드**: `getCompanyDir()`, `path.join(getCompanyDir()`, `sessions`, `_report.md`, `sessionDir`, `fs.mkdirSync`, `00_Raw/conversations`, `40_템플릿`, `site`
* **목적**: `sessions/`, `site/`, `conversations/` 등의 디렉토리를 루트로 물리적 이관할 때, 엔진의 강제 디렉토리 재생성(Auto-Recreate) 여부 및 런타임 에러(Crash) 유무를 소스 코드 수준에서 사전에 완전히 보증함.

---

## 2. 런타임 경로 동작 상세 분석

### A. 세션 산출물 및 에이전트 보고서 실제 저장 구조
1. **세션 디렉토리 동적 생성 (`makeSessionDir()`)**
   * 엔진 내부에서 세션 디렉토리는 다음과 같이 하드코딩되어 있습니다.
     ```typescript
     function makeSessionDir(): string {
       const ts = new Date().toISOString().replace(/[:.]/g, '-').slice(0, 16);
       const dir = path.join(getCompanyDir(), 'sessions', ts);
       fs.mkdirSync(dir, { recursive: true });
       return dir;
     }
     ```
   * **실제 저장 위치**: `{회사 폴더(기본값 _company)}/sessions/{YYYY-MM-DD-hh-mm}/`
   
2. **`_report.md` (CEO 종합 보고서) 실제 생성 및 읽기**
   * **생성 (Write)**: `fs.writeFileSync(path.join(sessionDir, '_report.md'), ...)` 형태로 생성됩니다.
   * **읽기 (Read)**: `path.join(getCompanyDir(), 'sessions', s, '_report.md')`를 통해 이전 세션 이력을 로드하거나 사이드바 UI에 노출하기 위해 동적으로 조회합니다.
   
3. **에이전트별 산출물 md 실제 저장**
   * 각 에이전트의 산출물 파일은 세션별로 분배 실행 시점에 `path.join(sessionDir, '${agent_id}.md')` 경로에 직접 기록됩니다. (예: `sessions/2026-05-18T03-25/secretary.md`)

---

### B. 주요 디렉토리 물리적 이관 가능성 최종 판단

#### 1. `sessions/` 폴더를 루트(`C:\Users\nakojin\connect_ai\sessions`)로 옮길 때 깨지는가?
* **판단**: **❌ 엔진 수정 없이 이동 시 즉각 오작동 및 강제 재생성됨**
* **근거**: 
  * 엔진 소스 코드에 `fs.mkdirSync(path.join(dir, 'sessions'), { recursive: true });` 및 `path.join(getCompanyDir(), 'sessions', ts)`가 하드코딩되어 강하게 제어되고 있습니다.
  * 수동으로 `sessions` 폴더를 루트로 이동시켜도, **에이전트를 1회 가동하거나 스튜디오를 실행하는 순간 `getCompanyDir()` 아래에 빈 `_company/sessions/` 디렉토리가 강제로 자동 재생성**됩니다.
  * 또한, 엔진은 루트의 `sessions/`가 아닌 `_company/sessions/`만을 스캔하므로 과거 세션 히스토리가 사이드바 UI 및 컨텍스트에 전혀 잡히지 않게 됩니다.
* **해결 방안**: 엔진의 `makeSessionDir()` 함수와 세션 리더가 `sessions` 루트 경로를 참조하도록 소스 코드 상수를 패치하기 전까지는 수동 이동을 **절대 보류**해야 합니다.

#### 2. `site/` 폴더를 루트로 이동할 수 있는가?
* **판단**: **🟢 이행 완료 (루트 site/ 로의 이동 완료)**
* **근거**:
  * 엔진 소스 코드에서 `path.join(root, 'site')`로 참조하는 지점들은 개발자가 신규 생성하는 프로젝트 하위 경로(`_company/projects/<프로젝트명>/site/`)로써, 유저의 배포용 정적 웹사이트 루트 디렉토리인 `_company/site/`와는 완전히 무관한 샌드박스 영역입니다.
  * 퍼블리싱 자동화 파이프라인에서 산출하는 `_company/site/` 폴더를 엔진은 **하드코딩으로 읽거나 쓰지 않으며**, 단지 정적 빌드 스크립트 실행 대상으로 삼을 뿐입니다.
  * 따라서, `_company/site/`를 루트 `site/`로 물리적 이동시키는 작업을 1단계 조치로써 안전하게 완료하였으며, 엔진 오작동이나 런타임 리스크 없이 정상 작동함을 보증합니다.

#### 3. `_company/00_Raw/conversations`를 루트 `00_Raw/conversations`로 이동할 수 있는가?
* **판단**: **❌ 엔진 수정 없이 이동 시 대화 기록 유실 및 강제 재생성됨**
* **근거**:
  * 엔진의 대화록 디렉토리 참조 함수는 다음과 같이 명확히 선언되어 있습니다.
    ```typescript
    function getConversationsDir(): string {
      const brain = getCompanyDir(); 
      return path.join(brain, '00_Raw', 'conversations');
    }
    ```
  * 따라서 대화록 디렉토리는 기본적으로 `{_company}/00_Raw/conversations`로 고정됩니다.
  * 엔진 수정 없이 이 폴더를 루트의 `00_Raw/conversations`로 이동할 경우, 에이전트와 대화하는 순간 **자동으로 `_company/00_Raw/conversations/` 폴더가 강제로 재생성**되며 새로운 대화 내역이 분산되어 과거 기록(History)을 엔진이 병합해서 읽지 못하는 치명적인 정합성 결함이 발생합니다.
  * **보류 조치**: 엔진 내 `getConversationsDir()` 함수가 `getCompanyDir()`가 아닌 `brainDir`을 직접 바라보거나 유연하게 가리키도록 소스 코드를 패치한 후 이관해야 합니다.

#### 4. `40_템플릿/` 리네임 보류 구체 사유
* **판단**: **❌ 엔진 수정 전 변경 절대 금지**
* **근거**:
  * 엔진 코어 내부에서 템플릿(재사용 빌딩 블록) 탐색 시 `path.join(brainDir, '40_템플릿', agentId)`를 직접 하드코딩해서 스캔하고 있으며, `withcats` 내부의 `pack_apply.py` 도구 역시 `40_템플릿`이라는 이름을 조인해서 작동합니다.
  * 폴더명을 영문(`templates`) 등으로 변경 시 즉시 템플릿 적용(Code Kit 패치) 기능 전체가 `FileNotFoundError`로 크래시가 발생합니다.

#### 5. `00_Raw/` 리네임 보류 구체 사유
* **판단**: **❌ 엔진 수정 전 변경 절대 금지**
* **근거**:
  * 엔진이 최근 데이터 인입(D&D) 경로로 `00_Raw`를 사용하고 있고, `extension.ts` (L5528)에서 최근 14일 이내 입수된 파일을 스캔하여 프롬프트 컨텍스트에 동적으로 강제 주입해 주는 실시간 상황 지식 엔진이 `00_Raw`에 강결합되어 있습니다.
  * 이름 변경 시 에이전트의 실시간 자율 정보 갱신(RAG) 기능이 작동을 멈추고 맙니다.

---

## 3. 종합 읽기/쓰기 동작 유형 분석

| 구분 | 대상 경로 | 주체 (엔진/도구) | 동작 유형 (R/W) | 구조 변경 가능성 (v2) | 리스크 및 예외 조치 |
| :--- | :--- | :---: | :---: | :---: | :--- |
| **코어 쓰기** | `_company/sessions/` | AI Studio 엔진 | **Write** (세션 생성시)<br>**Read** (히스토리 복구시) | **❌ 보류** (엔진 수정 후) | 단순 이동 시 빈 폴더 강제 재생성 및 과거 히스토리 유실. |
| **코어 쓰기** | `_company/00_Raw/conv/` | AI Studio 엔진 | **Write** (실시간 대화 기록)<br>**Read** (최근 대화록 요약) | **❌ 보류** (엔진 수정 후) | 변경 시 대화 기록 이원화 및 과거 로그 스캔 누락. |
| **정적 참조** | `_company/site/` | 자동화 빌드 툴 | **Write** (사이트 빌드 배포)<br>엔진 런타임 영향 無 | **🟢 이행 완료** | 루트 `site/`로의 물리 이관을 성공적으로 완료하였습니다. |
| **코어 읽기** | `40_템플릿/` | 엔진 & `pack_apply.py` | **Read** (템플릿 스캔)<br>**Write** (빌딩블록 내보내기) | **❌ 보류** (엔진 수정 후) | 변경 시 즉각 템플릿 킷 연동 시스템 불능 및 크래시 유발. |
| **동적 입수** | `00_Raw/` | AI Studio 엔진 | **Write** (드래그 입수)<br>**Read** (실시간 컨텍스트 주입) | **❌ 보류** (엔진 수정 후) | 변경 시 드롭다운 입수 및 RAG 자율 스캔 엔진 정지. |
| **상태 관리** | `company_state.json` | AI Studio 엔진 | **Read/Write** (활성 상태 제어) | **🟡 현 상태 유지** | 두뇌 루트 경로 아래 고정 정의되어 있어, 이관 대상에서 영구 제외. |

---

## 4. 안전한 이행을 위한 최종 권장 순서 (Final Roadmap)

검증된 런타임 데이터를 종합한 결과, **안정적인 3단계 롤아웃 플랜**을 제안합니다.

### 🎯 1단계: 지금 바로 실행 가능한 로컬 청소 (무수정 호환 - site/ 이관 완료)
* **대상**: `_company/site/`
* **작업**: 엔진 소스 코드 및 에이전트 코딩 런타임의 수정 없이, 오직 정적 결과물 빌드 파이프라인 대상인 `_company/site/` 디렉토리를 루트인 `site/`로 이전을 완료하였습니다.
* **효과**: 저장소에서 무겁고 큰 빌드 결과물이 핵심 에이전트 시스템 디렉토리에서 분리되어 Vault 검색 효율이 높아집니다.

### 🎯 2단계: AI Studio 엔진 코드 리팩토링 및 릴리스 (개발 영역)
* **대상**: `E:\ai_projects\yaongyaong_ai_studio`의 코어 상수 제거
* **작업**:
  1. `makeSessionDir()` 및 세션 탐색 경로에서 `sessions/` 명칭을 유연하게 매핑하도록 패치.
  2. `getConversationsDir()` 함수가 `getCompanyDir()`가 아닌 `brainDir`을 직접 보게 변경하여, `_company/00_Raw/conversations`를 루트 `00_Raw/conversations`로 통합할 통로를 개방.
  3. `40_템플릿`, `00_Raw` 명칭을 설정에서 오버라이드할 수 있도록 패치.
  4. `pack_apply.py` 내의 `40_템플릿` 참조 코드 수정.

### 🎯 3단계: 최종 v2 물리 마이그레이션 적용 (완료 단계)
* **대상**: `sessions/`, `inbox/`, `templates/`, `conversations/` 최종 영문화 통합
* **작업**:
  1. 업데이트된 AI Studio 릴리스 버전을 로컬에 적용.
  2. `withcats` 저장소의 `_company/sessions/`를 루트 `sessions/`로 통째로 이전 및 통합.
  3. `_company/00_Raw/conversations/`를 루트 `00_Raw/conversations/`로 통째로 이전 및 통합.
  4. `40_템플릿/` ➡️ `templates/` 리네임.
  5. `00_Raw/` ➡️ `inbox/` (또는 `raw/`) 리네임.
  6. 최종 런타임 빌드 동작 테스트 및 검증 완료.
