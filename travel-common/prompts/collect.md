# 수집 프롬프트 (Sonnet 5.5)

입력 파일: 장소 목록 `[{key, status, country, name_ko, name_local, region}]`. 규칙: `travel-common/VERIFICATION.md` 2·3·6절.

1. 공식·1차 출처만 근거로 쓴다: 운영자 공식 사이트, 관리 기관(지자체·국가유산청 등), 국가·도시 공식 관광기관. 블로그·여행사·OTA는 공식 페이지를 찾는 단서로만 쓴다.
2. WebFetch 가 실패하면(503, JS 렌더링) `curl -sL` 로 다시 연다. JS 사이트는 사이트가 쓰는 공개 API URL 을 인용해도 된다.
3. 체크리스트 10항목(위치·접근·소요시간·운영시간·휴무·요금·예약·결제·한국어 지원·주의)과 설명·하이라이트용 사실을 claim 1개 = 사실 1개로 뽑는다. **공식 페이지에 있는 운영 정보는 빠짐없이** 뽑는다.
4. 페이지 번호가 바뀌는 목록(FAQ ?pageIndex= 등)보다 고정 URL 을 인용한다. 인용한 문장이 그 URL 에 실제로 있는지 다시 확인한다.
5. 찾지 못한 항목은 `unconfirmed` 에 이유와 함께 쓴다. 추정·기억으로 채우지 않는다. 공식 출처끼리 값이 다르면 `unconfirmed` 에 `<항목>.conflict` 로 두 값과 URL 을 적는다.
6. 한국어, 우리 문장. 원문 인용은 `evidence` 에 15단어 이하.
7. `description`(300~500자)과 `highlights`(4~6개)는 claim 에 있는 사실로만 쓴다. 요약문은 쓰지 않는다.

출력: `[{key, name_ko, name_local, admin_region, address, description, highlights, claims:[{cid, field, text, value, evidence, sources:[{url, type, page_updated}]}], unconfirmed:[{field, reason}]}]`
