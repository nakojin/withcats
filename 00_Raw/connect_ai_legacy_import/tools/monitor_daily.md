# 📡 일일 모니터 — 자동 뉴스 수집 + CEO 브리핑

매일 지정한 키워드를 자동 검색해 요약 브리핑을 두뇌 폴더에 저장하고, 텔레그램으로 발송합니다.
**API 키 불필요** (텔레그램은 선택 사항).

## 무엇을 해주나요?
- 📡 DuckDuckGo로 키워드별 최신 뉴스·정보 수집
- 🧠 로컬 LLM으로 CEO 브리핑 형식으로 요약
- 💾 두뇌 폴더(`00_Raw/YYYY-MM-DD/daily_brief_*.md`)에 자동 저장
- 📱 텔레그램으로 브리핑 자동 발송 (TELEGRAM_TOKEN 설정 시)
- 🔁 N시간 간격으로 자동 반복 (24시간 자율 사이클 지원)

## 설정 (monitor_daily.json)

| 필드 | 설명 | 예시 |
|------|------|------|
| `KEYWORDS` | 모니터링 키워드 배열 | `["AI 트렌드", "로컬 LLM", "1인기업"]` |
| `LLM_URL` | LM Studio/Ollama URL | `http://127.0.0.1:1234` |
| `MODEL` | 모델명 (빈 값 = 자동) | `""` |
| `MAX_RESULTS_PER_KW` | 키워드당 수집 결과 수 | `5` |
| `INTERVAL_HOURS` | 실행 간격 (시간) | `24` |
| `TOTAL_RUN_HOURS` | 총 실행 시간 (0 = 무한) | `0` |
| `BRAIN_PATH` | 두뇌 폴더 절대경로 | `~/Downloads/지식메모리` |
| `SAVE_TO_BRAIN` | 두뇌 자동 저장 여부 | `true` |
| `TELEGRAM_TOKEN` | 텔레그램 봇 토큰 (선택) | `""` |
| `TELEGRAM_CHAT_ID` | 텔레그램 채팅 ID (선택) | `""` |

## 시작하기

```bash
pip install requests beautifulsoup4
python monitor_daily.py
```

**백그라운드 실행 (24시간 자율 권장):**
```bash
# 맥/리눅스
nohup python3 monitor_daily.py > monitor.log 2>&1 &

# 윈도우
start /b python monitor_daily.py > monitor.log 2>&1
```

## 출력
- `monitor_daily_log.md` — 모든 브리핑 누적 로그
- `{BRAIN_PATH}/00_Raw/YYYY-MM-DD/daily_brief_YYYY-MM-DD.md`
