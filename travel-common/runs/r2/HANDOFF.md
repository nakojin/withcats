# r2 인수인계 (2026-10-11): 2차 감사·수집 보충

v2.0 1회차(81곳)를 마친 뒤, 다음 작업을 다른 작업자가 이어받기 위한 문서다. 먼저 읽을 것: `travel-common/VERIFICATION.md`, `travel-common/SCHEMA_V2.md`, `travel-common/prompts/collect.md`, `travel-common/prompts/verify.md`, `docs/travel_v2_plan.md` 10절.

## 원칙 (모든 작업 공통)

- **근거는 공식·1차 출처뿐이다.** 운영자 공식 사이트, 관리 기관(지자체·국가유산청 등), 국가·도시 공식 관광기관만 쓴다. 블로그·여행사·OTA 는 공식 페이지를 찾는 단서로만 쓴다. 기억이나 추정으로 채우지 않는다.
- **보이는 본문만 근거다.** `display:none`, `<script>` 안 JSON, HTML 주석, 메타데이터에만 있는 값은 쓰지 않는다. 단, 페이지가 화면에 그리는 데 쓰는 공개 API 응답은 쓸 수 있다.
- **12개월이 지난 출처의 운영 규칙**(시간·요금·예약)은 문장에 출처 시점을 적는다. 예: "2025년 1월 안내 기준". 게시 연도를 알 수 없는 기사형 페이지는 운영 규칙의 근거로 쓰지 않는다.
- **복제 금지.** 사실과 수치만 가져와 우리 한국어 문장으로 쓴다. 원문 인용은 `evidence` 에 15단어 이하로만 둔다.
- **실시간 정보, 프로모션, 행정 할인 대상 목록**(군인·소방관·기자 등)은 수집하지 않는다.
- **장소 파일과 공개 파일은 고치지 않는다.** `travel-common/v2/places/`, `v2/published/` 가 그 대상이다. 결과는 아래 출력 위치에만 쓴다. 병합은 결과를 교차 검토한 뒤에 한다.
- **자기가 수집한 것을 자기가 검증하지 않는다.** 수집 결과의 검증은 다른 모델이 한다.

## 작업 1 (최우선): 시급 2건 독립 확인

`suggested_queue.json` 에서 `priority: 1` 인 2건이다. 공식 페이지에서 직접 확인해 수집 형식(작업 4)으로 `suggested_output/urgent.json` 에 쓴다.
- `east-qd-01` 칭다오 잔교: 회란각과 주변이 2026-10-13 22:00부터 12월 중순까지 보수 공사로 폐쇄된다. 원 공고나 시 정부 게시물로 확인한다.
- `east-qd-06` 라오산: 타이칭 케이블카가 2026-04-24부터 운행 중단 중이다. 현재도 중단 상태인지 최신 공지로 확인한다.

## 작업 2: 2차 감사 (공개 claim 1,783건)

배경: 10% 표본 재검증 오류율이 5.1%로, 기준(2% 이하)을 넘었다. 공개 중인 claim 전부를 다시 본다.
- 입력: `audit_input/part01.json` ~ `part30.json` (파트당 약 60건). 각 항목은 `{place, name, cid, field, text, sources[]}` 이다.
- 항목마다 인용 URL 을 직접 열고, 문장이 페이지(오늘 기준)에 그대로 뒷받침되는지 판정한다.
  - `ok`: 그대로 맞음. 번역·의역은 괜찮다.
  - `error`: 숫자·시간·날짜·가격·조건·이름 중 하나라도 다르거나, 페이지에 없거나, 과장됐다. 가능하면 고친 문장을 `corrected_text` 에 쓴다.
  - `cannot_open`: 2번 시도해도 열리지 않는다. 오류로 세지 않는다.
- 1회차에서 놓친 유형을 특히 엄격하게 본다.
  - 과장·경계 오류: "기본적으로 휴무 없음"→"연중무휴", "면제·감면 대상"→"전액 면제", "1.2m(含) 이하 무료"→"1.2m 이상 할인", "350m"→"350층"
  - 숨은 마크업에만 있는 값
  - 인용 페이지에 없는 날짜·회차·요금표
- 출력: `audit_output/partNN.json` (입력 파트 번호와 같게)
  ```json
  {"auditor": "codex", "date": "YYYY-MM-DD",
   "results": [{"place": "", "cid": "", "judgement": "ok|error|cannot_open", "note": "근거 문구나 다른 점", "corrected_text": null}],
   "summary": {"checked": 0, "ok": 0, "error": 0, "cannot_open": 0}}
  ```
- 진행 순서: part01부터 차례로 한다. 파트 하나를 끝낼 때마다 커밋한다.

## 작업 3: Tier A 수집 (52곳)

- 입력: `collect_queue.json`. 우선순위 순으로 정렬돼 있다(strong·medium → 기존 → weak).
- `key` 가 있으면 그대로 쓴다. `null` 이면 `new:<cc>-<지역>-<영문슬러그>` 형식으로 정한다. 예: `new:jp-tokyo-tokyo-tower`. 기존 키는 `travel-common/v2/places/*/` 의 파일명과 같다.
- 방법은 `travel-common/prompts/collect.md` 를 그대로 따른다.
  - 체크리스트 10항목: 위치·접근(주차 포함)·소요시간·운영시간·휴무·요금·예약·결제·한국어 지원·주의사항
  - claim 1개 = 사실 1개
  - 못 찾은 항목은 `unconfirmed` 에 이유와 함께 적는다. 10항목 가운데 claim 도 unconfirmed 도 없는 항목이 있으면 안 된다.
  - 공식 출처끼리 값이 다르면 `<항목>.conflict` 로 두 값과 URL 을 적는다.
  - `description`(300~500자)과 `highlights`(4~6개)는 claim 에 있는 사실로만 쓴다. 조사 과정은 쓰지 않는다.
- 출력: `collected/batchNN.json`. 3곳씩 묶고 NN 은 01부터 매긴다. 형식은 collect.md 의 출력 형식 그대로이고, 최상위에 `"collector": "codex"` 를 둔다.
  ```json
  {"collector": "codex", "date": "YYYY-MM-DD", "places": [{"key": "", "name_ko": "", "name_local": "", "admin_region": "", "address": "", "description": "", "highlights": [], "claims": [{"cid": "c1", "field": "hours", "text": "", "value": "", "evidence": "", "sources": [{"url": "", "type": "official|government|national_tourism|operator", "page_updated": null}]}], "unconfirmed": [{"field": "", "reason": ""}]}]}
  ```
  - `field` 값: `location, access, parking, duration, hours, closed_days, fees, reservation, payment, language, caution, description, highlight, tip`

## 작업 4 (시간이 남으면): 검증자 제안 사실 독립 수집

- 입력: `suggested_queue.json` (226건). 1회차 검증자가 공식 페이지에서 발견했지만, 아직 독립 수집을 거치지 않아 공개하지 않은 사실이다.
- `hint_url`·`hint_text` 는 단서일 뿐이다. 페이지를 직접 열어 확인하고 우리 문장으로 다시 쓴다. 페이지에 없거나 다르면 그렇게 적는다.
- 출력: `suggested_output/partNN.json` (50건씩)
  ```json
  {"collector": "codex", "results": [{"place": "", "sid": "", "status": "found|not_found|different", "claim": {"field": "", "text": "", "evidence": "", "sources": [{"url": "", "type": "", "page_updated": null}]}, "note": ""}]}
  ```

## 작업 방법

- 브랜치: `claude/new-git-repository-bzoc4t` 에서 새 브랜치(예: `ari/r2`)를 만들어 작업하고 푸시한다. 원 브랜치에는 직접 푸시하지 않는다.
- 진행 기록: `LEDGER.tsv` 에 `작업\t파트/배치\t상태\t날짜` 를 한 줄씩 덧붙인다. 상태는 `done` 또는 `partial`.
- 파일은 UTF-8, `ensure_ascii=False` 로 쓴다. JSON 이 깨지지 않았는지 `python3 -m json.tool` 로 확인한다.
- 커밋 메시지에는 무슨 작업을 했는지(예: `r2 audit part01-05`)만 적는다.

## 이후 처리 (인수 후)

- 감사 결과에서 `error` 는 교차 확인한 뒤 판정을 바꾸고, 설명문도 같이 고친다.
- 새 수집분은 다른 모델이 독립 검증한 뒤 `merge_run.py` 로 병합한다.
- 감사 반영 뒤 새 10% 표본의 오류가 2% 이하이면 v2.0 태그를 단다.
