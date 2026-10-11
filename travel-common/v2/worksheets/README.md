# 보완 필요 작업표

`gaps.csv` 는 수집·검증을 거친 뒤에도 공식 출처로 채우지 못한 항목 목록이다(`tools/gaps.py export` 가 생성). 엑셀에서 열어 채운 뒤 `tools/gaps.py import <repo_root> <파일>` 로 들여온다.

| 열 | 내용 |
|---|---|
| `kind` | `gap`(항목 전체가 빔) / `partial`(일부는 채웠고 세부가 빔) |
| `reason` | `not_in_official_source` · `official_unreachable` · `conflicting_sources` |
| `note` | 무엇이 빠졌는지, 충돌이면 두 값과 출처 |
| **`value`** | 채울 사실 1가지(한국어). 해당 사항이 없으면 `해당 없음` |
| **`source_url`** | 근거 공식 페이지. 없으면 비우고 아래 `owner_input` 사용 |
| **`source_type`** | 기본 `official`. 전화·현장·메일 확인이면 `owner_input` |
| **`checked_at`** | 확인한 날짜 `YYYY-MM-DD` (필수) |
| **`memo`** | `owner_input` 이면 확인 방법(예: "관리소 전화 02-…, 담당자 확인") 필수 |

들여온 값은 `owner_verified` 로 기록되고 사이트에는 "운영자 확인"으로 따로 표시된다. 출처나 날짜가 빠진 행은 거부된다.
