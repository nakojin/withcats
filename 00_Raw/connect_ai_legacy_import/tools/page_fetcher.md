# 📄 페이지 수집 — URL 본문 추출 + 요약 저장

URL 목록에서 웹페이지 본문을 추출하고, 로컬 LLM이 핵심 내용을 요약해 두뇌 폴더에 저장합니다.
**API 키 불필요** — requests + BeautifulSoup으로 직접 파싱.

## 무엇을 해주나요?
- 🌐 URL 목록에서 본문 자동 추출 (광고·nav 제거)
- 🧠 로컬 LLM으로 핵심 요약 + 주요 포인트 추출
- 💾 두뇌 폴더(`00_Raw/YYYY-MM-DD/`)에 마크다운으로 자동 저장
- 📋 `page_fetcher_report.md`에 모든 수집 결과 누적

## 설정 (page_fetcher.json)

| 필드 | 설명 | 예시 |
|------|------|------|
| `URLS` | 수집할 URL 배열 | `["https://example.com/article"]` |
| `LLM_URL` | LM Studio/Ollama URL | `http://127.0.0.1:1234` |
| `MODEL` | 모델명 (빈 값 = 자동) | `""` |
| `EXTRACT_MODE` | 추출 방식 | `summary` / `keywords` / `full` |
| `BRAIN_PATH` | 두뇌 폴더 절대경로 | `~/Downloads/지식메모리` |
| `SAVE_TO_BRAIN` | 두뇌 자동 저장 여부 | `true` |

## 시작하기

```bash
pip install requests beautifulsoup4
python page_fetcher.py
```

## 출력
- `page_fetcher_report.md` — 누적 수집 보고서
- `{BRAIN_PATH}/00_Raw/YYYY-MM-DD/page_{제목}_{타임스탬프}.md`
