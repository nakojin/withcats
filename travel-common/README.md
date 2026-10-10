# travel-common

한국·일본·중국 여행 자료(`korea-travel/`, `japan-travel/`, `china-travel/`)를 하나의 구조로 묶어 v2 로 올리기 위한 공통 폴더다.
전체 계획은 [docs/travel_v2_plan.md](../docs/travel_v2_plan.md) 를 따른다.

| 경로 | 내용 |
|---|---|
| `SCHEMA_V2.md` | 공통 스키마 v2 명세 |
| `tools/validate_v2.py` | 좌표 파일·v2 레코드 검증기 (표준 라이브러리만 사용) |
| `tools/geocode.py` | 장소 좌표 수집(OSM Nominatim, 초당 1회 이하, 캐시) |
| `tests/` | 검증기 단위 테스트 (`python3 tests/test_validate_v2.py`) |
| `coordinates/` | 장소별 좌표 중간 산출물. catalog 는 아직 수정하지 않는다 |
| `research/` | Tier A 후보 조사 근거(웹검색, 출처 URL·확인일) |
| `tiers/` | Tier A 선정 결과 |

검증:

```
python3 tools/validate_v2.py coords <repo_root>
python3 tools/validate_v2.py places <places.json> --today 2026-10-10
```
