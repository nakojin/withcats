# 🏢 withcats Knowledge Vault 구조 분석 및 업그레이드 제안서 (v2)

본 문서는 `withcats` 저장소의 현재 폴더 구조를 심층적으로 분석하고, 시스템 안정성 및 유지보수성을 극대화하기 위한 구조 개선(v2) 계획을 다룹니다. **현재 파일의 물리적 이동이나 삭제는 진행하지 않으며**, 본 제안서에 기반하여 다음 단계의 작업 계획을 수립합니다.

---

## 1. 🔍 현재 루트 구조 요약
저장소의 최상위(Root) 구조는 다음과 같이 구성되어 있습니다.

```text
C:\Users\nakojin\connect_ai\
├── .git/                     # Git 형상관리 메타데이터
├── .gitignore                # 제외 패턴 정의
├── .gitkeep                  # 빈 디렉토리 유지를 위한 파일
├── 00_Raw/                   # 날짜별 수집 정보 및 외부 원본 원고
├── 40_템플릿/                 # 리액트/HTML 구조 템플릿 (landing-kit 등)
├── _company/                 # 핵심 에이전트 시스템 및 런타임 데이터 영역
├── company_state.json        # 시스템 전역 메트릭 정보 (Founding Date, Task 수 등)
└── README.md                 # 프로젝트 개요
```

---

## 2. 🗂 _company 하위 구조 요약
`_company` 디렉토리는 야옹야옹 AI 스튜디오 에이전트들의 지식 베이스와 실행 흔적이 집약된 **핵심 영역**입니다.

```text
_company/
├── 00_Raw/                   # 일자별 채팅 로그 (conversations/)
├── _agents/                  # 10개 에이전트 캐릭터별 설정/프롬프트/메모리/도구 코드
│   ├── business/, ceo/, designer/, developer/, editor/, 
│   │   instagram/, researcher/, secretary/, writer/, youtube/
│   │   ├── config.md         # 에이전트 기본 정보/메타데이터
│   │   ├── prompt.md         # 페르소나 시스템 프롬프트
│   │   ├── memory.md         # 자가학습으로 누적된 메모리 데이터
│   │   ├── goal.md           # 에이전트 주간/상시 목표
│   │   ├── tools.md          # 사용 가능 도구 목록 문서
│   │   └── tools/            # [주의] 에이전트 전용 Python 실행 스크립트 (.py, .json)
├── _shared/                  # 전역 연동 설정 및 의사결정 기록 장부
│   ├── active.json           # 활성화된 세션/에이전트 목록
│   ├── agent_models.json     # 에이전트별 매핑 LLM (Gemma-4, Qwen2.5, GPT-OSS 등)
│   ├── decisions.md          # 자동 누적된 회사 의사결정 로그 (핵심)
│   ├── goals.md              # 회사 전역 목표 목록
│   ├── identity.md           # 회사 정체성 (withcats 브랜드 가이드, 타깃층, 금기사항)
│   ├── tracker.json          # 500개 이상의 수행 태스크 증적(Evidence) 히스토리 장부
│   ├── schedule.md           # 작업 일정 가이드
│   └── _system.md            # 시스템 프롬프트 보조 파일
├── sessions/                 # 일자/시간별 에이전트 실행 및 CEO 종합 리포트
│   └── YYYY-MM-DDTHH-MM/     # 각 실행 주기 세션 폴더
│       ├── _brief.md         # 세션 요약 브리핑
│       ├── _report.md        # CEO 종합 평가 리포트
│       └── [agent_name].md   # 개별 에이전트가 제출한 업무 결과 보고서
├── src/                      # [주의] 데이터 프로세서 및 퍼블리시 서비스 (.py)
├── utils/                    # [주의] SEO 인핸서 등 런타임 헬퍼 유틸리티 (.py)
└── 임시 디버깅 파일들         # api_test.py, api_test_result.md, thumbnail_concept.png 등
```

---

## 3. 🎯 00_Raw, 40_템플릿, company_state.json 역할 추정

### 💡 `00_Raw` (Root)
* **추정 역할**: **외부 원본 자료/기획 소스 공급처 (External Input Ingestion)**
* **상세**: 날짜별 폴더(`2026-05-12`, `2026-05-13`) 하위에 `AI_1인_기업_자동화_챕터_1.md`, `MrBeast_유튜브_전략.md` 등과 같이 사용자가 주입한 외부 정보 원고가 보관되어 있습니다. 리서치 에이전트(`researcher`)나 비즈니스 에이전트(`business`)가 지식 검색(RAG)을 위해 이 폴더의 파일을 소스로 삼는 역할을 합니다.

### 💡 `40_템플릿` (Root)
* **추정 역할**: **코드 제너레이터용 원본 골격 저장소 (Asset Boilerplate templates)**
* **상세**: 개발 에이전트(`developer`)가 프론트엔드 작업이나 랜딩 페이지(landing-kit 등)를 코딩할 때 참조·복사해서 쓸 수 있는 원본 React 컴포넌트(`Hero.tsx`, `Features.tsx`, `CTA.tsx`)와 매니페스트 템플릿입니다. 즉, AI가 코드를 생산하기 위한 '설계 골격' 역할을 합니다.

### 💡 `company_state.json` (Root)
* **추정 역할**: **전역 시스템 생명주기 및 대시보드 상태 기록 (Dashboard & Growth Metrics)**
* **상세**:
  ```json
  { "tasksCompleted": 509, "knowledgeInjected": 9, "lastSessionDate": "", "foundedAt": "2026-05-10" }
  ```
  전체 수행한 작업 카운트(509회), 지식 주입 카운트(9회), 설립일자 등을 보관합니다. 메인 UI 대시보드에서 회사 성장 지표나 통계를 시각화하여 유저에게 보여주기 위한 상태값 세팅용 파일입니다.

---

## 4. ⚠️ 운영 메모리/세션/자동화 코드/템플릿/원본자료가 섞여 있는 지점

현재 `withcats` 저장소는 **'순수한 데이터/지식(Vault)'**과 **'런타임 실행 코드(Engine/Script)'**가 한데 어우러져 있는 구조적 혼선 상태입니다.

1. **중복된 `00_Raw` 디렉토리**:
   - 루트의 `00_Raw` (유저 주입 원본)와 `_company/00_Raw` (에이전트-유저 간 일일 대화 히스토리 로그)가 이름이 동일하여 에이전트가 상대 경로 탐색 시 오작동하거나 경로를 혼동할 여지가 큽니다.
2. **에이전트 데이터와 실행 코드의 혼재**:
   - `_company/_agents/[agent_id]/tools/` 디렉토리 내에 Python 코드(`.py`)와 설명 파일(`.md`), 규격 파일(`.json`)이 에이전트 프롬프트(`prompt.md`), 기억(`memory.md`)과 한 곳에 묶여 있습니다.
3. **소스 소유권 분산**:
   - `_company/src/` 및 `_company/utils/` 하위에 자동화 로직 소스 코드(`publish_service.py`, `seo_enhancer.py` 등)가 저장되어 있습니다. 소스 코드는 엔진 저장소(`yaongyaong_ai_studio`)에 집중되어야 하며, Vault는 지식과 설정 정보에 집중하는 것이 본래 깃 저장소 분리 목적에 부합합니다.
4. **임시 테스트 파일의 난립**:
   - `_company/` 루트 경로에 `api_test.py`, `api_test_result.md`, `thumbnail_concept_1.png` 등 테스트 과정에서 발생한 잔해 및 디버깅 스크립트들이 여과 없이 누적되고 있습니다.

---

## 5. 👍 현재 구조의 장점
* **독립적인 에이전트 관리**: 각 에이전트 폴더별로 `config`, `prompt`, `memory`, `goal`이 확실히 캡슐화되어 있어, 새로운 성격의 냥 에이전트를 추가하거나 개별 기억을 관리하기에 극도로 편리합니다.
* **시간대별 세션 이력의 완전성**: `sessions/` 하위에 날짜-시간 포맷으로 완벽히 아카이빙이 수행되므로 언제든 과거 에이전트들의 활동 증적(`_brief.md`, `_report.md`)을 영구히 감사(Audit)할 수 있습니다.
* **강력한 전역 공유 장부**: `_shared/decisions.md` 및 `tracker.json`에 비즈니스 관련 의사결정과 태스크 진행 사항이 자동으로 차곡차곡 자가 학습 형태로 누적되어 비즈니스 흐름을 읽기에 직관적입니다.

---

## 6. 🛑 현재 구조의 위험 요소
* **한글 폴더명 잠재적 에러**: 최상위 `40_템플릿` 폴더는 한글로 되어 있어, Git 작업이나 시스템 OS 환경(Linux 컨테이너 구동, 또는 OS 로케일 차이)에 따라 파일 경로 깨짐이나 모듈 임포트 실패를 유발할 수 있습니다.
* **보안 노출 위협**: 에이전트 실행 툴(`tools/`) 디렉토리 혹은 자동화 소스 내부에 API 키나 토큰 정보가 부주의하게 코딩되거나 캐싱되어 원격 깃허브에 통째로 Push될 위험이 있습니다.
* **코드 이원화로 인한 빌드 혼선**: 실행 스크립트가 `yaongyaong_ai_studio` 저장소와 `withcats` 저장소 양쪽에 이원화되어 존재하므로, 코드 업데이트 시 양쪽 싱크를 맞추어야 하는 오버헤드가 큽니다.
* **의사결정 및 트래커 파일 비대화**: `decisions.md` (2,200줄 돌파), `tracker.json` (36,000줄 돌파) 파일의 크기가 시스템이 24시간 가동되면서 기하급수적으로 커지고 있습니다. 이를 주기적으로 압축하거나 분할하지 않으면 메모리 부족 및 파일 IO 지연을 초래합니다.

---

## 7. 🚀 추천 폴더 구조 v2

데이터의 흐름과 Concerns의 명확한 분리를 반영한 **Upgrade 구조**안입니다. (폴더명 영문화 및 역할군 명확화)

```text
C:\Users\nakojin\connect_ai\ (withcats Vault v2)
├── config/                   # [신설] 전역 메트릭 및 시스템 메타데이터 보관
│   └── company_state.json    # (기존 company_state.json 이동)
├── inputs/                   # (기존 00_Raw 에서 변경) 유저가 주입하는 원본 외부 기획 문서
│   └── YYYY-MM-DD/
├── logs/                     # [신설] 시스템 구동 및 히스토리 로그 분리
│   └── conversations/        # (기존 _company/00_Raw/conversations 에서 이동)
├── templates/                # (기존 40_템플릿 에서 변경) 한글 깨짐 방지를 위한 영문화 템플릿
│   └── developer/landing-kit/
├── _company/                 # 핵심 지식 및 런타임 정보 코어
│   ├── _agents/              # (유지) 에이전트 개별 지식 캡슐
│   │   └── [agent_id]/
│   │       ├── config.md, prompt.md, memory.md, goal.md
│   │       └── tool_manifest.json  # 코드 제거, 실행 매니페스트 규격만 유지
│   ├── _shared/              # (유지) 전역 의사결정 장부
│   │   ├── active.json, decisions.md, goals.md, identity.md, tracker.json
│   │   └── schedule.md
│   └── sessions/             # (유지) 시간대별 증적 히스토리 기록
│       └── YYYY-MM-DDTHH-MM/
├── site/                     # (기존 _company/site 에서 이동) 정적 사이트 포스트 산출물 독립
│   └── blog/posts/
└── .scratch/                 # 임시 테스트 스크립트 및 개념도 썸네일 전용 격리 공간
```

---

## 8. 📝 실제 이동 전 체크리스트
- [ ] **경로 참조 전수 검사**: `yaongyaong_ai_studio` 엔진 소스 코드 전체에서 `_company/00_Raw`, `40_템플릿`, `company_state.json` 등을 하드코딩으로 읽어오는 구문이 있는지 확인.
- [ ] **Git History 보존 검토**: 중요도가 높은 `company_state.json` 및 `decisions.md` 등의 파일 이동 시, git 커밋 히스토리가 끊기지 않도록 `git mv` 명령어를 사용해 안전하게 이동할 수 있도록 시나리오 작성.
- [ ] **한글 인코딩 변환 예외**: 윈도우 환경과 타 타깃 OS 환경 호환성을 위해 `40_템플릿` 내 React 컴포넌트의 한글 유실 방지 인코딩 백업 수행.
- [ ] **보안 정보 누출 점검**: `src/`나 에이전트 `tools/` 코드 내부에 은밀하게 기재된 API 토큰 등이 있는지 점검 후 환경 변수로 이관 준비.

---

## 9. 🟢 다음 단계에서 수정해도 되는 파일 목록
* **새로운 구조 정의 문서 및 설정 매핑**:
  - `docs/architecture_review.md` (본 구조 리뷰 문서)
  - `_company/_shared/active.json`, `agent_models.json` 등 (에이전트 동작 활성화용 설정 매핑)
  - 에이전트 `memory.md` 및 `goal.md` (단순 가이드 보강용 텍스트 파일)

## 🔴 다음 단계에서 절대 건드리면 안 되는 파일 목록 (동작 보존 필수)
* **시스템 전역 핵심 실행 로직 파일**:
  - `_company/src/*.py` 및 `_company/utils/*.py` (실제 자동화 엔진 파이프라인)
  - 에이전트 전용 Custom Tools 소스: `_company/_agents/*/tools/*.py`, `*.json`
* **누적 히스토리 및 영구 메타데이터 파일**:
  - `_company/_shared/tracker.json` (500회 이상의 증적 레코드 유실 금지)
  - `_company/_shared/decisions.md` (자가 학습 의사결정 정보 유실 금지)
  - `company_state.json` (Founding 및 완료 수치 유실 금지)
  - `_company/sessions/` 하위의 과거 모든 날짜별 레포트 서류들
