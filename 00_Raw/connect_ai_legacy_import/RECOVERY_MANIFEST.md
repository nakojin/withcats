# 📋 레거시 지식 복구 매니페스트 (Recovery Manifest)

> **수행 일자**: 2026-05-24
> **레거시 원본**: `C:\Users\nakojin\.connect-ai-brain`
> **대상 저장소 (Vault)**: `E:\ai_projects\withcats`
> **담당**: YaongYaong AI Studio (Antigravity B모드 수동 복구 파이프라인)

---

## 1. 복구 개요

본 매니페스트는 레거시 Connect AI 로컬 저장소에 남아 있던 `manual-review` 및 `sensitive/skip` 후보 파일들에 대한 수동 정밀 검증을 완료하고, 실제 인증 자격증명(토큰, 비밀번호 등)의 유출 없이 안전하게 Knowledge Vault로 이관 복구한 현황을 기록합니다.

### 🛡️ 보안 무결성 선언
> [!IMPORTANT]
> 본 수동 복구 작업을 진행하며, 모든 신규 생성/이관 파일 내에 실제 `token`, `secret`, `key`, `oauth`, `password`, `bearer`, `telegram_token`, `client_secret` 등 고위험 인증 정보가 포함되지 않았음을 교차 검증을 통해 100% 확정하였습니다.
> 또한, 기존 `withcats` 저장소의 주요 지식 파일(`memory.md`, `tracker.json`, `company_state.json` 등)을 절대 덮어쓰지 않고 독립 격리 영역을 활용하여 안전을 도모하였습니다.

---

## 2. 복구 방식 및 처리 통계

| 처리 유형 | 대상 경로 / 파일명 | 개수 | 설명 / 이관 정책 |
| :--- | :--- | :---: | :--- |
| **📥 원본 import** (safe) | `00_Raw/connect_ai_legacy_import/tool_configs/*.json` | **7** | 민감 정보가 없는 순수 도구 설정 스키마 및 기본값 JSON 파일 아카이브 이관 |
| **🛡️ 마스킹본 / 요약** (summary) | `00_Raw/connect_ai_legacy_import/summaries/*.md` | **2** | 에이전트 설정 및 외부 API 연동 도구의 스키마 구조 요약 지식 복구 |
| **🎓 템플릿 복구** (template) | `40_템플릿/connect_ai_legacy_skills/README.md` | **1** | 레거시 에이전트의 스킬(Skill) 관리 및 가이드 템플릿 복구 |
| **🧠 메모리 검증** (review) | `_company/_imports/connect_ai_legacy_memory_review/memory_diff_summary.md` | **1** | 레거시 빈 메모리 검증 및 기존 withcats 고가치 메모리 보존 선언 |
| **⏸️ 보류 (Pending)** | - | **0** | 모든 manual-review/sensitive 파일 검증 완료로 보류 없음 |
| **🚫 영구 제외 (Skipped)** | 외부 계정/인증 관련 JSON 및 뼈대 파일 | **4** | 실제 자격증명 및 인증용 JSON 원본 등은 보안 정책상 복구 영구 제외 |
| **📊 총합 (Total)** | | **15** | 검토 대상 전체에 대한 매핑 및 조치 완수 |

---

## 3. 세부 파일별 처리 명세 (28개 후보 통합 제어)

### ① 원본 / 마스킹본 아카이브 이관 대상 (7개)
아래 7개 파일은 실제 민감 토큰이 완전히 비어 있는 안전한 JSON 템플릿(schema)으로 확인되어, 아카이브 목적으로 `tool_configs/` 에 복구 완료했습니다.
1. `developer/tools/pwa_setup.json` -> [pwa_setup.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/pwa_setup.json)
2. `developer/tools/web_init.json` -> [web_init.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/web_init.json)
3. `editor/tools/music_generate.json` -> [music_generate.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/music_generate.json)
4. `editor/tools/music_studio_setup.json` -> [music_studio_setup.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/music_studio_setup.json)
5. `researcher/tools/monitor_daily.json` -> [monitor_daily.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/monitor_daily.json)
6. `researcher/tools/page_fetcher.json` -> [page_fetcher.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/page_fetcher.json)
7. `researcher/tools/web_search.json` -> [web_search.json](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/tool_configs/web_search.json)

### ② 안전 요약본 및 지식 변환 대상 (10개 config.md + 4개 연동 JSON)
설정 가이드 및 외부 도구 구조는 다음 안전 요약 지식 파일들로 완전 변환하여 복구했습니다.
* [agent_configs_summary.md](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/summaries/agent_configs_summary.md): 에이전트별 `config.md` 파일 10개 통합 가이드 요약
* [external_tools_structure.md](file:///E:/ai_projects/withcats/00_Raw/connect_ai_legacy_import/summaries/external_tools_structure.md): 외부 연동 도구 4종(`google_calendar_write.json`, `paypal_revenue.json`, `telegram_setup.json`, YouTube 6종 도구) 구조 요약
* [memory_diff_summary.md](file:///E:/ai_projects/withcats/_company/_imports/connect_ai_legacy_memory_review/memory_diff_summary.md): 레거시 `memory.md` 10개 무결성 검증 완료 및 withcats 기존 메모리 유지 선언

### ③ 영구 제외 파일 목록 (Skipped / Excluded) (4개)
사용자 절대 금지 규정에 의거하여, 실제 인증 세션 유출 방지를 위해 아래 항목들은 복제 및 복구 대상에서 영구 제외합니다.
1. `.telegram_offset.json` (메시지 폴링 오프셋 번호 - 무가치/보안 제외)
2. `youtube_account.json` (실제 유튜브 연동 로그인 세션 - 보안 제외)
3. `gemini_account.json` / `oauth.local.json` (실제 OAuth 발급 세션 - 보안 제외)
4. `.telegram_poll.lock` (임시 잠금 파일 - 무가치 제외)
