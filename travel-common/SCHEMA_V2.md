# 여행 자료 공통 스키마 v2 (초안)

3개국(korea / japan / china) 장소 레코드를 하나의 구조로 맞추기 위한 명세다. 검증은 `tools/validate_v2.py` 가 한다.
v1 의 필드명은 나라마다 다르므로(`records`/`items`, `operational`/`hours_and_fees`/`operations`) v2 에서 통일한다.

## 원칙

1. **확인한 값만 `confirmed`.** 공식 출처를 직접 읽은 값에만 쓰고, 출처 URL 을 연결한다.
2. **모르면 null + 이유.** 추정·기억으로 채우지 않는다. `status: unconfirmed`, `value: null`, `note` 에 이유를 쓴다.
3. **복제 금지.** 공식 사이트·리뷰는 사실과 수치를 수집해 우리 문장으로 요약한다. 문장을 그대로 옮기지 않는다.
4. **원자료 보존.** v1 의 `region` 같은 원표기는 지우지 않고 v2 에서도 `source_region` 으로 남긴다.

## 레코드 구조 (place)

| 필드 | 형식 | 비고 |
|---|---|---|
| `id` | string | v1 id 유지 |
| `country` | `kr` / `jp` / `cn` | |
| `admin_region` | string | 표준 시도·도도부현·성 이름 |
| `source_region` | string | v1 원표기 |
| `city` | string | |
| `names` | `{ko, local, en?}` | |
| `category` | string[] | 1개 이상 |
| `coord` | `{lat, lng, geo_type, precision, geo_source, confidence}` | `geo_type`: point/area, `precision`: poi/centroid/place, `confidence`: high/medium/low |
| `summary` | string | 1~2문장 |
| `description` | string | A 등급은 300자 이상 |
| `highlights` | string[] | A 등급은 4개 이상 |
| `recommended_duration_min` | int / null | null 이면 `duration_note` 에 이유 |
| `best_time` | string | |
| `how_to_get_there` | string / null | 공식 접근 안내 요약 |
| `ops` | `{hours, fees, reservation, closed_days, payment}` | 각 항목은 아래 `opsItem` |
| `sources` | `[{url, checked_at, supports[]}]` | `supports` 는 hours/fees/reservation/closed_days/payment/location/description |
| `quality` | `{depth_tier, last_verified}` | `depth_tier`: A/B/C |
| `nearby` | `[{poi_id, type, distance_m}]` | 선택. P5 이후 |

### opsItem

```
{ "status": "confirmed | unconfirmed | not_applicable",
  "value": "string | null",
  "note": "string | null",         // unconfirmed 이면 이유 필수
  "checked_at": "YYYY-MM-DD" }
```

## 깊이 등급 (depth_tier)

| 등급 | 조건 |
|---|---|
| A | 설명 300자 이상, 하이라이트 4개 이상, 소요시간·접근 확인, 좌표 confidence high/medium, `hours`·`fees` 가 confirmed 또는 not_applicable |
| B | 설명 150자 이상, 하이라이트 3개 이상, 좌표 확인 |
| C | 그 외(현재 v1 대부분) |

## 좌표 파일 (`coordinates/{kr,jp,cn}.json`)

catalog 를 바꾸지 않는 중간 산출물이다. 각 행은 `{id, lat, lng, geo_type, precision, geo_source, osm, matched_display, confidence, flags}`.
`confidence` 가 `low`/`none` 이거나 `flags` 에 `locality_mismatch` 가 있으면 사람이 검토해야 하며, 검토 전에는 v2 레코드에 쓰지 않는다.
OSM 데이터는 ODbL 이라 사이트에 "© OpenStreetMap contributors" 표기를 해야 한다.
