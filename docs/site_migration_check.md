# site 폴더 이관 사전점검 보고서 (Site Migration Check)

본 보고서는 **야옹야옹 AI 스튜디오 / YaongYaong AI Studio** 지식 저장소(`withcats`) 폴더 구조 개선(v2) 1단계 작업으로 분류된 **`_company/site/` ➡️ 루트 `site/`로의 물리적 이전**의 실현 가능성과 런타임 안정성을 최종 점검한 보고서입니다.

---

## 1. 사전 점검 결과 요약

| 항목 | 점검 내용 | 결과 및 상태 |
| :--- | :--- | :--- |
| **디렉토리 존재 여부** | `_company/site/` 실제 존재 여부 | **🟢 존재함** |
| **내부 리소스 정보** | 하위 디렉토리 수 / 파일 수 / 총 용량 | 2개 폴더 / 1개 파일 / **약 12 Bytes** |
| **엔진 소스 코드 참조** | `yaongyaong_ai_studio` 내 하드코딩 여부 | **❌ 없음 (완전 안전)** |
| **지식 저장소 내부 참조** | `withcats` 내 스크립트/설정 참조 여부 | **❌ 없음 (완전 안전)** |
| **Git 제외 필터 영향** | 루트 및 하위 `.gitignore` 배제 규칙 여부 | **❌ 없음** |
| **이동 가능 여부 판단** | **지금 바로 즉시 이동 가능 여부** | **🟢 즉시 이동 가능 (최종 승인)** |

---

## 2. 세부 조사 및 분석 내용

### A. 디렉토리 구조 및 리소스 규모
* **물리 경로**: `C:\Users\nakojin\connect_ai\_company\site`
* **내부 구조**:
  ```
  _company/site/
  └── blog/
      └── posts/
          └── example_post.md (12 Bytes)
  ```
* **총 파일 용량**: 12 Bytes (`example_post.md` 파일 1개만 존재)
* **평가**: 보관된 정적 웹 포스트 및 리소스의 물리적 크기가 극도로 미미하여 디스크 I/O나 깃 인덱싱 지연 없이 즉각적인 물리 이관이 가능합니다.

### B. 소스 코드 및 저장소 내부 참조 검증
1. **AI Studio 엔진 저장소 (`yaongyaong_ai_studio`)**
   * `'site'` 문자열이 검색되는 유일한 구문들은 `path.join(root, 'site')`로써, 이는 개발자 에이전트가 신규 생성하는 개별 웹 프로젝트 디렉토리(`_company/projects/<프로젝트명>/site/`) 관련 샌드박스 로직입니다.
   * 엔진 핵심 코드 수준에서 정적 퍼블리싱 사이트 루트인 `_company/site/` 경로를 하드코딩으로 강제 조회하거나 런타임에 직접 제어하는 부분은 **존재하지 않습니다.**
   
2. **withcats 지식 저장소 (`connect_ai`)**
   * 과거 `2026-05-13` 에이전트 대화 히스토리 및 세션 리포트 내에 에이전트가 `<list_files path="site/blog"/>`와 같은 상대 경로로 조회를 시도했다가 `site` 폴더가 `_company` 외부에 있어 실패한 trace 기록만 다수 보존되어 있습니다.
   * active 상태로 동작하는 핵심 파이썬 스크립트 코드나 에이전트 런타임 내부에 `_company/site` 경로를 참조하는 정적 코드는 **존재하지 않습니다.**

### C. Git 제외 필터 (`.gitignore`) 영향 분석
* **루트 `.gitignore`**: `node_modules/`, `.cache/` 등 임시 파일만 제외할 뿐, `site` 또는 `_company/site` 관련 제외 규칙은 포함되어 있지 않습니다.
* **회사 `.gitignore` (`_company/.gitignore`)**: API 키 정보 파일 배제용으로 세팅되어 있으며 `site` 관련 예외 룰은 전혀 없습니다.
* **평가**: `site/` 디렉토리를 루트로 이전하여도 Git 추적(Tracking) 및 GitHub 원격 저장소 백업에 아무런 악영향이 없습니다.

---

## 3. 이관 시 예상 리스크 및 대책

* **이동 시 리스크**: **없음 (Zero Risk)**
  * 엔진 소스코드 결합도가 0%에 가까우므로 런타임 오작동을 유발하지 않으며, 이관 시 엔진에 의해 빈 폴더가 강제로 재생성되지 않습니다.
  * 단, 향후 정적 퍼블리싱 자동화 스크립트가 구동될 경우 해당 스크립트 내 빌드 결과물 아웃풋 타깃 경로를 `_company/site`가 아닌 루트 `site`로 자동 맵핑되도록 설정값 1곳만 동기화해주면 완전히 종료됩니다.

---

## 4. 이관 절차 및 가이드라인 (명령어)

추후 실제 1단계 폴더 이행 작업을 수행할 때 사용할 수 있는 구체적인 실행 명령어 가이드라인입니다.

### 📋 1. 폴더 물리적 이전 명령어 (PowerShell / Windows Cmd)
```powershell
# withcats 저장소 루트(C:\Users\nakojin\connect_ai)에 위치한 상태에서 실행

# 1. _company/site 폴더를 루트 디렉토리로 이동
Move-Item -Path _company/site -Destination ./site
```

### 📋 2. 이전 완료 후 검증 명령어
```powershell
# 1. 기존 _company 하위에 site 폴더가 완전히 삭제되고 없는지 확인
Get-ChildItem -Path _company

# 2. 루트 레벨로 이동된 site 폴더 구조가 올바르게 전송되었는지 확인
Get-ChildItem -Path site/blog/posts

# 3. 예시 파일의 정합성 최종 검사
Get-Content -Path site/blog/posts/example_post.md
```
* **기대 결과**: `Get-ChildItem -Path _company` 목록에 `site`가 나타나지 않고, 루트의 `site/blog/posts` 하위에 `example_post.md` 파일이 존재해야 합니다.
