# 검증 프롬프트 (Opus 5.5)

입력: 수집자의 claim 문장·값·출처 URL(수집자의 근거 문구는 주지 않는다), 설명·하이라이트, 수집자가 못 찾은 항목.

1. claim 마다 인용 URL 을 직접 연다(WebFetch, 실패 시 `curl -sL`). 자기 지식으로 판정하지 않는다.
2. 판정: `verified`(그대로 맞음) · `corrected`(일부 틀림, 고친 문장 제시) · `outdated`(새 값 존재) · `unverifiable`(페이지에 없음/열리지 않음) · `rejected`(1차 출처 아님).
3. 설명·하이라이트에서 판정을 통과한 claim 으로 뒷받침되지 않는 문장을 모두 적는다.
4. 수집자가 못 찾은 항목은 공식 페이지에서 2회까지 찾아보고, 찾으면 `suggested_claims` 로 제시한다(직접 확정하지 않는다).
5. 공식 출처끼리 다른 점, 오래된 출처(12개월 이상)를 `conflicts` 에 적는다.

출력: `{places:[{key, verdicts:[{cid, verdict, corrected_text, note}], unsupported_in_description, unsupported_in_highlights, suggested_claims:[{field, text, url}], conflicts}], summary}`
