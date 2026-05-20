# 경로 참조 전수 조사 보고서 (Path Reference Audit)

본 문서는 **야옹야옹 AI 스튜디오 / YaongYaong AI Studio** 지식 저장소인 `withcats` (`connect_ai`)의 폴더 구조를 v2로 안전하게 업그레이드하기 위해, AI Studio 엔진 저장소와 `withcats` 내부에서 기존 경로를 하드코딩하여 참조하는 모든 지점을 전수 조사하고 리스크를 분석한 보고서입니다.

---

## 1. 조사 개요

* **조사 대상 저장소 (2개)**:
  1. **AI Studio 엔진 저장소**: `E:\ai_projects\yaongyaong_ai_studio` (VS Code 확장 프로그램 및 웹 백엔드 코어)
  2. **withcats 지식 저장소 (Vault)**: `C:\Users\nakojin\connect_ai` (에이전트 지식, 세션 데이터 및 커스텀 툴 런타임)
* **검색 키워드**: `_company`, `00_Raw`, `40_템플릿`, `company_state.json`, `connect_ai`, `withcats`
* **조사 목적**: 실제 파일 이동 및 이름 변경 작업 전에 하드코딩된 경로 참조를 파악하여, 구조 변경 시 발생할 수 있는 런타임 오작동 및 데이터 누락 사고를 사전 차단하고 안전한 이행 전략을 수립함.

---

## 2. 저장소별 발견된 참조 경로 및 파일 목록

### A. AI Studio 엔진 저장소 (`yaongyaong_ai_studio`)

AI Studio 엔진 코드 내부에는 **P-Reinforce 규격 파일명 및 폴더명이 다수 하드코딩**되어 시스템 코어 로직과 결합해 있습니다.

1. **`_company` 관련 참조**
   * `src/paths.ts` (L16): `export const COMPANY_SUBDIR = '_company';`
     * 회사 폴더의 기본 디렉토리 상수로 정의되어 있어, 이 값을 변경하지 않는 한 엔진은 항상 `_company/` 디렉토리를 기준으로 런타임 데이터를 스캔합니다.
   * `src/extension.ts` (L5519, L5584): 지식 스캔 시 시스템 영역을 제외하기 위한 무시(ignore) 목록에 `_company`, `_shared`, `_agents`, `sessions`, `approvals` 등이 하드코딩되어 있습니다.
   * `src/extension.ts` (L1032~L1067): 하위 호환성을 위해 구버전 루트 파일을 `_company/` 내부로 투명하게 마이그레이션하는 동적 로직이 내장되어 있습니다.
   * `assets/tool-seeds/developer/pack_apply.py` (L68): `business_tools = os.path.join(brain_root, "_company", "_agents", "business", "tools")` 와 같이 특정 에이전트 도구의 실행 경로를 하드코딩하여 조인하고 있습니다.

2. **`00_Raw` 관련 참조**
   * `src/extension.ts` (L5528, L5588): `const rawDir = path.join(brain, '00_Raw');`
     * 최근 14일 이내 입수된 파일을 스캔하여 에이전트의 상황 인지 프롬프트(Prompt)에 동적으로 인입(`inject`)하는 시스템 아키텍처가 `00_Raw` 폴더명을 기준으로 작동합니다.
   * `src/extension.ts` (L7586~L7591): `return path.join(brain, '00_Raw', 'conversations');`
     * 에이전트와의 데일리 대화 기록 및 회의 로그 저장 경로가 `00_Raw/conversations/`로 고정되어 있습니다.
   * `assets/tool-seeds/researcher/monitor_daily.py` (L117), `page_fetcher.py` (L99), `web_search.py` (L113): 리서치 에이전트 도구들이 수집한 원시 마크다운 데이터를 저장할 때 `00_Raw/YYYY-MM-DD/` 경로를 하드코딩하여 조인합니다.
   * `web/src/app/api/brain/save/route.ts` (L12): 웹 프론트엔드 API 레이어에서도 `00_Raw` 경로를 사용하여 저장 처리를 수행합니다.

3. **`40_템플릿` 관련 참조**
   * `src/extension.ts` (L5902): `const standardDir = path.join(brainDir, '40_템플릿', agentId);`
     * AI 에이전트의 재사용 템플릿 빌딩 블록을 스캔하고 읽어오는 로직의 탐색 경로가 `40_템플릿` 한글 명칭으로 하드코딩되어 있습니다.
   * `src/extension.ts` (L8747): 템플릿 파일 생성 및 내보내기 시 `path.join(brainDir, '40_템플릿', agentId, safeName)`을 타깃으로 지정합니다.
   * `assets/tool-seeds/developer/pack_apply.py` (L249, L413): 개발자 에이전트의 핵심 스크립트 내부에서 코드 템플릿(Landing Kit 등)을 탐색하기 위해 `os.path.join(brain_root, "40_템플릿", "developer")` 경로를 참조합니다.

4. **`company_state.json` 관련 참조**
   * `src/extension.ts` (L1173, L1206): `path.join(brain, 'company_state.json')`
     * 전체 AI 에이전트들의 활성화 상태 및 시스템 상태 정보를 저장하고 파싱하기 위해 두뇌 루트 경로 아래의 특정 파일명을 직접 가리킵니다.

5. **`connect_ai` & `withcats` 관련 참조**
   * `.gitignore`, `docs/GITHUB_WORKFLOW.md`, `docs/WEB_MVP_PLAN.md` 등 프로젝트 명세서 및 깃 가이드라인 문서 내 로컬 환경 설명 텍스트로만 존재하며, 엔진 실행 파일 내부에 하드코딩된 핵심 동적 로직은 확인되지 않았습니다.

---

### B. withcats 지식 저장소 (`connect_ai`)

지식 저장소 내부에서는 과거 생성된 에이전트 런타임 로그와 일부 동적 실행 스크립트에서 참조가 발견되었습니다.

1. **`_company/_agents/developer/tools/pack_apply.py` (핵심 커스텀 툴)**
   * **[심각]** 6행, 249행, 413행에서 두뇌 루트 하위의 `"40_템플릿"` 한글 경로명을 직접 조인하여 코드 템플릿을 읽고 프로젝트에 패치합니다.
   * 이 스크립트가 실행되는 도중 `40_템플릿/` 경로명이 존재하지 않으면 즉각 에러가 나며 개발자 에이전트의 빌드 자동화가 중단됩니다.

2. **세션 히스토리 및 과거 로그 문서 (`_company/sessions/`)**
   * 과거 실행되었던 100개 이상의 세션 실행 리포트(`_report.md`) 및 에이전트 실행 기록 파일 내에 당시 실행 명령어 세트(`cd "c:\Users\nakojin\connect_ai\_company\_agents\..." && py -3 ...`)가 절대 경로 형태로 대량 보존되어 있습니다.
   * 단, 이는 과거 실행 히스토리 로그이므로 현재 활성 런타임 시스템 작동에는 직접적인 문제를 일으키지 않는 정적 텍스트 데이터입니다.

3. **기타 마크다운 데이터 (`_company/_shared/tracker.json` 등)**
   * 시스템 공유 디렉토리 내 일부 인덱스 및 자가 의사결정 트래커 문서 내에서 `withcats`, `connect_ai` 명칭이 간접 참조로 포함되어 있습니다.

---

## 3. 구조 변경 시 안정성 평가 및 영향 분석

### ⚠️ 구조 변경 시 깨질 가능성이 매우 높은 핵심 위험 참조 (3대 리스크)

1. **`40_템플릿/` 한글 폴더명 리네임 리스크**
   * **영향**: AI Studio 엔진 내부 템플릿 스캐너(`extension.ts`)와 `withcats` 내 개발자 에이전트의 패치 도구(`pack_apply.py`) 두 곳에 `"40_템플릿"` 명칭이 강하게 결합되어 있습니다.
   * **결과**: 엔진 수정 없이 `40_템플릿` 폴더명을 리네임할 경우, 스튜디오의 재사용 템플릿 로딩 기능이 마비되며, `pack_apply` 실행 시 `FileNotFoundError`가 발생합니다.

2. **`00_Raw/` 폴더명 리네임 리스크**
   * **영향**: 최근 인입 데이터 스캔 시스템(`extension.ts`)이 `00_Raw` 명칭을 가리킵니다.
   * **결과**: `00_Raw` 폴더명을 임의로 `inbox/` 등으로 변경하면, 유저가 드래그 앤 드롭한 파일이 올바르게 인입 처리되더라도 에이전트가 최근 정보를 자율 스캔하여 메모리에 연동하는 핵심 기능이 마비됩니다.

3. **`_company/` 시스템 루트 폴더명 리네임 리스크**
   * **영향**: 엔진 핵심 경로 정의 `COMPANY_SUBDIR = '_company'`와 무시 필터(`ignoreList`) 배열이 연동되어 있습니다.
   * **결과**: 이 폴더명을 임의로 변경하면 AI Studio 엔진이 회사 폴더로 인식하지 못해 시스템 락이 풀리거나, 지식 검색 스캔 대상에 개인 세션 정보가 무방비로 흘러들어가 프롬프트 오류를 유발하고, 엔진이 임의로 새로운 빈 `_company/` 폴더를 루트에 자동 재성성해 버립니다.

---

### 🟢 안전하게 리네임 또는 물리적 이동이 가능한 항목

다음 항목들은 엔진 소스 코드 레벨에서 명시적으로 하드코딩되지 않았거나, 정적 성격이 강하여 상대 경로 또는 루트 레벨 독립이 가능합니다.

1. **`_company/site/` ➡️ 루트 `site/`로 분리**
   * **분석**: 정적 웹 사이트 생성 산출물 영역으로, 엔진이나 에이전트 런타임에서 해당 경로를 하드코딩하여 조회하는 부분이 없습니다. 루트로 이동시키더라도 자동 빌드 파이프라인의 대상 경로 변수 1곳만 수정하면 되므로 매우 안전합니다.
2. **`_company/sessions/` ➡️ 루트 `sessions/`로 분리**
   * **분석**: 엔진의 무시 필터 배열(`ignoreList`)에 이미 `'sessions'` 문자열이 하드코딩되어 있습니다. 따라서 루트 레벨의 `sessions/` 폴더로 통째로 이동시키더라도 엔진 스캐너에 의해 안전하게 제외 처리되며, 지식 검색 성능에 영향을 주지 않습니다.
3. **`_company/00_Raw/conversations/` ➡️ 루트 `00_Raw/conversations/`로 통합**
   * **분석**: 엔진 코드에서는 대화 로그 저장 위치로 `path.join(brain, '00_Raw', 'conversations')`를 지정하고 있습니다. 기존 구조에서는 `_company` 내부와 루트에 이중으로 꼬여 있던 `00_Raw` 구조를 루트의 단일 `00_Raw/conversations/`로 물리적 이전하여 정비하면, 엔진의 수정 없이도 즉시 호환 및 단일 진실 소스(SSOT)가 구축됩니다.

---

## 4. 리네임 가능성 종합 요약

| 원본 경로/파일명 | 권장 변경 대상 v2 | 리네임 가능성 | 위험 요인 및 예외 처리 |
| :--- | :--- | :---: | :--- |
| `_company/site/` | `site/` | **🟢 안전** | 엔진 영향 없음. 빌드 타깃 설정만 수정하면 즉시 분리 가능. |
| `_company/sessions/` | `sessions/` | **🟢 안전** | 엔진 `ignoreList`에 `sessions`가 이미 등록되어 있어 스캔 회피 가능. |
| `_company/00_Raw/conv/` | `00_Raw/conversations/` | **🟢 안전** | 엔진이 이미 `brain/00_Raw/conversations`를 가리키고 있어 자연스럽게 연동됨. |
| `company_state.json` | `company_state.json` | **🟡 현 유지** | 두뇌 루트 디렉토리 고정 파일로 엔진 하드코딩됨. 유지 필요. |
| `40_템플릿/` | `templates/` | **❌ 당장 불가** | 엔진 소스 및 `pack_apply.py` 런타임 코드 수정과 동시 배포 필수. |
| `00_Raw/` | `inbox/` 또는 `raw/` | **❌ 당장 불가** | 엔진 입수(D&D) 로직 및 최근 파일 동적 인입(L5528)이 정지됨. |
| `_company/` | `core/` 또는 `runtime/` | **❌ 당장 불가** | 엔진 `COMPANY_SUBDIR` 상수 및 ignore 필터와 결합되어 변경 시 시스템 마비. |

---

## 5. 안전한 구조 개편을 위한 3단계 제안 (Next Steps)

참조 전수 조사 결과를 기반으로, 한 번에 모든 폴더명을 리네임하여 시스템이 깨지는 것을 예방하기 위해 아래와 같은 단계적 이행 시나리오를 제안합니다.

### 📌 1단계: 엔진 무수정 상태에서의 안전한 물리적 이사 (즉시 실행 가능)
* **목표**: 엔진 코드를 한 줄도 수정하지 않고, `withcats` 저장소 자체 구조만 정비하여 검색 노이즈와 결합도를 낮춤.
* **작업 내용**:
  1. `_company/site/` 디렉토리를 루트인 `site/`로 물리적 이동.
  2. `_company/sessions/` 디렉토리를 루트인 `sessions/`로 물리적 이동.
  3. `_company/00_Raw/conversations/` 하위의 대화 로그를 루트 `00_Raw/conversations/`로 이전하고 하나로 통합.

### 📌 2단계: 엔진 소스 코드 리팩토링 및 동시 패치 (동일 시점 반영)
* **목표**: 하드코딩된 한글 폴더명(`40_템플릿`, `00_Raw`) 및 시스템 폴더명(`_company`)을 제거하고 유연성을 확보.
* **작업 내용**:
  1. **엔진 저장소 (`yaongyaong_ai_studio`)**:
     * `src/paths.ts` 및 `src/extension.ts` 내부의 `"40_템플릿"`, `"00_Raw"` 경로 참조 부분을 설정 변수나 유연한 영문 상수로 변경.
  2. **withcats 저장소**:
     * `_company/_agents/developer/tools/pack_apply.py` 스크립트 내 `"40_템플릿"` 문자열을 신규 영문 폴더명과 매핑되도록 업데이트.
  3. 두 패치 사항을 깃 브랜치에 동시 정합성 확인 후 커밋.

### 📌 3단계: 최종 v2 폴더 구조 마이그레이션 완성
* **목표**: 완전히 영문화되고 직관적인 최적의 폴더 구조로 전환을 완료.
* **작업 내용**:
  1. 패치된 AI Studio 엔진 업데이트 적용.
  2. `withcats` 저장소의 `40_템플릿/` ➡️ `templates/`로 최종 변경.
  3. `00_Raw/` ➡️ `inbox/` (또는 `raw/`)로 최종 변경.
  4. 최종 빌드 및 에이전트 도구 실행 검증.
