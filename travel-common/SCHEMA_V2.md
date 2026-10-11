# 여행 자료 스키마 v2

장소 1곳 = 파일 1개: `v2/places/{kr|jp|cn}/{id}.json`. 규칙의 정의는 `tools/v2common.py`, 검사는 `tools/validate_v2.py store` 가 한다.

## 원칙

1. **공개는 판정을 통과한 사실(claim)만.** `verified`·`corrected`·`outdated`(독립 검증 통과)와 `owner_verified`(운영자가 출처와 함께 직접 입력)만 사이트에 나간다.
2. **모르면 빈칸이 아니라 '보완 필요'.** 체크리스트 항목마다 값이 없으면 사유(`gap.reason`)를 둔다.
3. **v1 자료는 `legacy` 에 보존하고 공개하지 않는다.** 검증 전 자료이기 때문이다.
4. **복제 금지.** 공식 사이트·리뷰는 사실·수치만 수집해 우리 문장으로 쓴다.

## 장소 파일

| 필드 | 내용 |
|---|---|
| `id`, `country`, `tier`(A/B/C), `status` | `status`: `draft` 또는 `verified`(공개 가능) |
| `names` | `{ko, local}` |
| `admin_region`, `former_region`, `city`, `address` | 행정구역은 최신 공식 명칭, 이전 명칭은 `former_region` |
| `coord`, `coord_note` | `{lat, lng, geo_type, precision, geo_source, confidence, osm}`. high·medium 만 넣고 나머지는 `coord_note` |
| `summary`, `description`, `highlights` | 수집 claim 으로만 쓴 본문. `content_review.status` 가 `ok` 일 때만 공개. 요약은 설명문 첫 문장 |
| `checklist` | 아래 10개 항목, 각 `{status: filled|gap|not_applicable, claims[], gap{reason, note}, partial_gaps[]}` |
| `claims[]` | 사실 1개씩. 아래 형식 |
| `conflicts[]` | 공식 출처끼리 다른 점과 채택 근거 |
| `open_questions[]` | 체크리스트 밖의 미확인 사항(면적, 혼잡 시기 등) |
| `content_review` | 본문 검토 결과(`ok`/`needs_fix`, 근거 없는 문장 목록) |
| `legacy` | v1 원자료(비공개) |
| `meta.runs[]` | 수집·검증 회차 기록(모델, 날짜, 판정 수) |

### 체크리스트 10항목

`location`(위치) · `access`(접근·주차) · `duration`(소요시간) · `hours`(운영시간) · `closed_days`(휴무) · `fees`(요금, 무료면 "무료" 명시) · `reservation`(예약, 중국은 실명·여권) · `payment`(결제) · `language`(한국어 지원) · `caution`(주의사항)

`gap.reason`: `not_in_official_source`(공식 출처에 없음) · `official_unreachable`(공식 사이트 접속 불가) · `conflicting_sources`(공식 출처끼리 충돌) · `not_collected`(아직 수집 전)

### claim

```
{ "cid": "run-c1", "field": "fees", "text": "우리 문장으로 쓴 사실 1개", "original_text": "검증 전 문장(수정됐을 때)",
  "value": "정규화 값", "verdict": "verified|corrected|outdated|owner_verified|unverifiable|rejected|pending|suggested",
  "verify_note": "...", "sources": [{"url": "...", "type": "official|government|national_tourism|operator|owner_input",
  "page_updated": "YYYY-MM-DD|null", "checked_at": "YYYY-MM-DD"}], "collector": "sonnet-5.5|owner", "verifier": "opus-5.5|null", "run": "..." }
```

`suggested` 는 검증자가 새로 찾은 사실로, 다음 회차에서 독립 수집·검증을 거쳐야 공개된다.

## 공개 데이터

`tools/build.py` 가 `v2/published/{cc}.json` 과 `v2/STATUS.md` 를 만든다. 공개 데이터에는 판정을 통과한 사실과 그 출처·확인일, 체크리스트별 보완 필요 사유만 들어간다.
