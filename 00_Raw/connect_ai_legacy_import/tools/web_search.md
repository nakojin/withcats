# 🔍 웹 검색 — 자동 수집 + 두뇌 저장

DuckDuckGo로 검색하고, 로컬 LLM이 결과를 요약·분석해 두뇌 폴더에 자동 저장합니다.
**API 키 불필요** — 외부 계정 없이 즉시 사용.

## 무엇을 해주나요?
- 🔍 DuckDuckGo HTML 검색 (광고 없는 결과)
- 📄 제목·URL·스니펫 수집
- 🧠 로컬 LLM으로 핵심 요약 + 인사이트 추출
- 💾 두뇌 폴더(`00_Raw/YYYY-MM-DD/`)에 마크다운으로 자동 저장
- 📋 `web_search_report.md`에 누적 기록

## 설정 (web_search.json)

| 필드 | 설명 | 예시 |
|------|------|------|
| `SEARCH_QUERIES` | 검색어 배열 | `["AI 최신 트렌드", "로컬 LLM 사용법"]` |
| `LLM_URL` | LM Studio/Ollama URL | `http://127.0.0.1:1234` |
| `MODEL` | 모델명 (빈 값 = 자동) | `""` |
| `MAX_RESULTS` | 검색 결과 수 | `8` |
| `BRAIN_PATH` | 두뇌 폴더 절대경로 | `~/Downloads/지식메모리` |
| `SAVE_TO_BRAIN` | 두뇌 자동 저장 여부 | `true` |

## 시작하기

```bash
pip install requests beautifulsoup4
python web_search.py
```

## 출력
- `web_search_report.md` — 모든 검색 보고서 누적
- `{BRAIN_PATH}/00_Raw/YYYY-MM-DD/search_{쿼리}_{타임스탬프}.md` — 두뇌 저장본
