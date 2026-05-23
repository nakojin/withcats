# 🔌 외부 연동 도구(API) 구조 및 스키마 분석 (External Tools Structure)

> [!NOTE]
> 본 문서는 레거시 Connect AI 로컬 저장소에서 외부 플랫폼 연동을 담당하던 9개 도구(`sensitive/skip` 및 보류 후보군)의 내부 구조 스키마와 사양을 통합 분석하여 복구한 안전 지식 문서입니다.
> 원본에 존재하던 설정 변수의 최상위 구조, 매개변수 종류, 기본값 사양을 문서화하였으며, 실제 인증키나 토큰 값은 완전히 배제되어 있으므로 안전하게 활용할 수 있습니다.

---

## 1. Google Calendar 연동 도구 (`google_calendar_write.json`)

에이전트가 구글 캘린더 API에 직접 접근하여 일정을 조회 및 추가하기 위한 구조 명세입니다.

### ⚙️ JSON 스키마 사양
```json
{
  "CLIENT_ID": "",
  "CLIENT_SECRET": "[REDACTED_CLIENT_SECRET]",
  "REFRESH_TOKEN": "[REDACTED_REFRESH_TOKEN]",
  "CALENDAR_ID": "primary",
  "DEFAULT_DURATION_MINUTES": 60
}
```

* **매개변수 설명**:
  * `CLIENT_ID` / `CLIENT_SECRET`: Google Cloud Console OAuth 2.0 클라이언트 자격증명 정보.
  * `REFRESH_TOKEN`: 구글 인증 서버로부터 얻은 무기한 리프레시 토큰.
  * `CALENDAR_ID`: 기본값은 `"primary"`로 설정되어 있으며, 특정 공유 캘린더 ID로 덮어쓰기 가능.
  * `DEFAULT_DURATION_MINUTES`: 일정을 등록할 때의 기본 소요 시간 단위 (분, 기본 60분).

---

## 2. PayPal 매출 수집 도구 (`paypal_revenue.json`)

에이전트가 PayPal 개발자 계정을 통해 특정 기간 동안의 실제 매출 및 환불 이력, 비즈니스 KPI 통계를 정산하기 위한 도구 명세입니다.

### ⚙️ JSON 스키마 사양
```json
{
  "MODE": "sandbox",
  "CLIENT_ID": "",
  "CLIENT_SECRET": "[REDACTED_CLIENT_SECRET]",
  "LOOKBACK_DAYS": 30,
  "CURRENCY": ""
}
```

* **매개변수 설명**:
  * `MODE`: `"sandbox"` (테스트 환경) 또는 `"live"` (실서비스 환경) 중 선택.
  * `CLIENT_ID` / `CLIENT_SECRET`: PayPal Developer Dashboard에서 발급받는 인증키.
  * `LOOKBACK_DAYS`: 분석 대상이 되는 과거 일수 범위 (기본값: 30일).
  * `CURRENCY`: 통화 필터 (예: `"USD"`, `"KRW"` 등). 비워두면 수집된 모든 통화의 총합을 보고서로 작성함.

---

## 3. YouTube 분석 및 자율 최적화 도구 세트

YouTube API 및 웹 크롤링 파이프라인을 결합하여, 기획냥과 마켓냥이 동영상 콘텐츠 제작 전략을 수립하는 데 활용하는 도구 구성 명세입니다.

### ① 자율 기획 스케줄러 (`auto_planner.json`)
에이전트가 자율적으로 기획 및 트렌드 조사를 실행하는 가동 간격을 관리하는 스키마입니다.
* **INTERVAL_HOURS**: 실행 간격 시간. (1, 2, 3, 6, 12, 24 중 선택 가능. YouTube API 일일 쿼터 제한을 방지하기 위해 **6시간** 이상 설정을 강력 권장함)
* **TOTAL_RUN_HOURS**: 전체 가동 모드 지정. `0`인 경우 제한이 없는 무한 자율 모드로 돌고, 양수인 경우 그 시간 만큼 동작 후 종료됩니다.

### ② 채널 정밀 분석기 (`channel_full_analysis.json`)
* **구조**: `{}` (빈 객체)
* **목적**: 기본 채널의 전체 프로필, 총 구독자 수, 누적 조회수 추이 및 전체 동영상 목록 메타데이터를 일괄적으로 로딩하는 초기화 엔드포인트입니다.

### ③ 댓글 수집기 (`comment_harvester.json`)
인기 동영상 및 업로드 영상의 시청자 피드백을 모니터링하여 공통 키워드와 감정을 분석하는 도구입니다.
```json
{
  "VIDEOS_PER_CHANNEL": 5,
  "COMMENTS_PER_VIDEO": 20,
  "LOOKBACK_DAYS": 14
}
```
* `VIDEOS_PER_CHANNEL`: 채널별 수집 대상 동영상 수 (최신 5개).
* `COMMENTS_PER_VIDEO`: 동영상 하나당 크롤링할 시청자 댓글 수 (최대 20개).
* `LOOKBACK_DAYS`: 분석할 동영상의 업로드 기한 범위 (최근 14일 이내).

### ④ 경쟁사 벤치마킹 분석기 (`competitor_brief.json`)
```json
{
  "TOP_N_PER_CHANNEL": 5,
  "LOOKBACK_DAYS": 30
}
```
* 동종 카테고리 내 경쟁 채널들의 최신 30일 데이터 중 성과(조회수 대비 인터랙션 비율 등)가 가장 높은 상위 `TOP_N_PER_CHANNEL`개 동영상을 추출하여 기획 브리핑을 생성합니다.

### ⑤ 자사 채널 자가진단 (`my_videos_check.json`)
```json
{
  "LOOKBACK_DAYS": 30,
  "TOP_N": 15,
  "COMMENT_SAMPLES": 5
}
```
* 본인 채널의 최근 30일 실적을 진단하고, 대표 동영상 15개의 시청자 댓글 중 5개씩 샘플링하여 부정 피드백 및 요구사항을 자동 요약합니다.

### ⑥ 트렌드 모니터링 (`trend_sniper.json`)
```json
{
  "TARGET_KEYWORDS": [
    "유튜브 자동화",
    "AI 비즈니스",
    "마케팅 트렌드",
    "생산성 툴"
  ]
}
```
* 특정 핵심 타겟 키워드 군을 상시 관측하여 해당 검색어 범주 내 급상승 중인 신규 채널 및 바이럴 동영상을 신속히 발견합니다.

---

## 4. 텔레그램 연동 인프라 (`telegram_setup.json`)

비냥(Secretary)이 사내 공지 및 개별 알림을 텔레그램 메신저로 중계할 때 사용되는 최소 명세입니다.

### ⚙️ JSON 스키마 사양
```json
{
  "TELEGRAM_BOT_TOKEN": "[REDACTED_TELEGRAM_TOKEN]",
  "TELEGRAM_CHAT_ID": "[REDACTED_TELEGRAM_CHAT_ID]"
}
```
* **동작 원리**: 에이전트 시스템이 완료된 모닝 브리핑이나 비정상 상태 에러 로그를 발견하면, Telegram Bot API `sendMessage` 엔드포인트를 타겟 챗 ID에 포스트하여 관리자에게 실시간 알림을 보냅니다.
* **보안 조치**: 봇 토큰이나 챗 ID는 노출 시 악용 가능성이 매우 크므로 본 저장소 복구 단계에서는 완전히 차단하였으며, 개별 로컬 환경에서 로딩 시에만 빈 칸에 입력하여 사용합니다.
