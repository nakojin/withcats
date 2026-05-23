# 🏢 에이전트별 환경 설정 구조 요약 (Agent Configs Summary)

> [!NOTE]
> 본 문서는 레거시 Connect AI 로컬 저장소(`C:\Users\nakojin\.connect-ai-brain`)의 에이전트별 `config.md` 10개 파일을 분석하여, 실제 민감 인증값(토큰, 키)은 제외하고 에이전트 구동 및 도구 구성을 위해 요구되는 환경변수 규격과 설명 구조만을 안전하게 통합 복구한 지식 문서입니다.
> 모든 원본 파일의 실제 인증값은 비어 있는 템플릿 상태였으며, 본 문서에도 어떠한 실제 비밀키가 포함되어 있지 않습니다.

---

## 1. 개요 및 저장소 정책

Connect AI 및 야옹야옹 AI 스튜디오의 에이전트들은 개별적인 개인화 비서 설정 및 외부 API 연결을 위해 각 에이전트 폴더 내부에 `config.md`를 구성하고 있었습니다. 
* **보안 필터**: 로컬에서는 자유롭게 편집하되, 원격 저장소 노출을 차단하기 위해 `.gitignore`에 기본 설정되어 있습니다.
* **지식 가치**: 에이전트 확장 및 리브랜딩 과정에서 각 캐릭터가 어떤 도구와 외부 연동 사양을 기본적으로 지원하고 설계되었는지 보여주는 중요한 시스템 아키텍처 정보입니다.

---

## 2. 에이전트별 요구 변수 일람

| 에이전트 | 역할 (Role) | 요구 환경 변수 / 설정 사양 | 주요 목적 |
| :--- | :--- | :--- | :--- |
| **냐장님 (CEO)** | 총괄 / 디렉터 | 없음 (공통 가이드 파일만 존재) | 전체 오케스트레이션 및 조율 |
| **코냥 (Developer)** | 개발 / 엔지니어 | 없음 (공통 가이드 파일만 존재) | PWA, 웹팩, Lint 자동화 실행 |
| **디냥 (Designer)** | 디자인 / 그래픽 | `FIGMA_TOKEN`<br>`STITCH_API_KEY` | 피그마 컴포넌트 데이터 추출 및 스타일 연동 |
| **비냥 (Secretary)** | 비서 / 운영지원 | `TELEGRAM_BOT_TOKEN`<br>`TELEGRAM_CHAT_ID` | 텔레그램 메신저 자율 가동 및 모니터링 알림 발송 |
| **기획냥 (Planner/PM)** | 유튜브 기획 | `YOUTUBE_API_KEY`<br>`YOUTUBE_CHANNEL_ID` | YouTube Data API를 통한 트렌드 분석 및 채널 기획 |
| **마켓냥 (Marketing)** | 마케팅 / SNS | `META_ACCESS_TOKEN`<br>`INSTAGRAM_BUSINESS_ID` | Meta Graph API를 통한 인스타그램 피드 자동 발행 및 분석 |
| **재무냥 (Finance)** | 비즈니스 / 재무 | `CLIENT_ID` (PayPal)<br>`CLIENT_SECRET` (PayPal) | PayPal 매출 및 실적 데이터 수집 자동화 |
| **리서냥 (Researcher)** | 분석 / 웹 리서치 | 없음 (웹 리서치 도구 템플릿 사용) | 웹 문서 크롤링 및 트렌드 요약 |
| **작가냥 (Writer)** | 카피라이팅 / 글쓰기 | 없음 (공통 가이드 파일만 존재) | 블로그, 원고, 소셜 콘텐츠 기고 |
| **편집냥 (Editor)** | 영상 편집 / 음악 | 없음 (MusicGen, ACE-Step 로컬 모델 연동) | 오디오 생성 및 영상 렌더링 파이프라인 |

---

## 3. 핵심 변수 발급 및 설정 가이드

### 📱 텔레그램 연동 (`TELEGRAM_BOT_TOKEN`, `TELEGRAM_CHAT_ID`)
* **발급처**: Telegram `@BotFather`를 통해 신규 봇을 생성하고 고유 토큰을 발급받습니다.
* **채팅 ID 확인**: 텔레그램 `@userinfobot` 채널에 아무 메시지나 전송하여 본인의 고유한 숫자형 Chat ID를 확인한 뒤 기재합니다.
* **활용도**: `monitor_daily.json` 도구 가동 시 주기적 브리핑 결과를 텔레그램 메시지로 자동 전송받을 수 있습니다.

### 📺 YouTube 연동 (`YOUTUBE_API_KEY`, `YOUTUBE_CHANNEL_ID`)
* **발급처**: Google Cloud Console에서 YouTube Data API v3를 활성화한 후 API 키를 생성합니다.
* **채널 ID 확인**: 유튜브 채널 고급 설정에서 `UC`로 시작하는 고유 채널 ID를 추출하여 기재합니다.
* **주의**: YouTube API의 일일 기본 할당량(Quota)인 **10,000 unit** 한도를 넘지 않도록 도구 호출 주기를 제어(권장 6시간 간격)해야 합니다.

### 📷 Meta Graph / Instagram 연동 (`META_ACCESS_TOKEN`, `INSTAGRAM_BUSINESS_ID`)
* **발급처**: Meta for Developers 대시보드에서 앱을 생성하고, Graph API 탐색기를 통해 페이지 및 Instagram Graph API 권한이 포함된 장기 액세스 토큰을 발급받습니다.
* **비즈니스 ID**: Meta 비즈니스 설정 페이지 혹은 Graph API 호출을 통해 인스타그램 비즈니스 계정 ID를 조회하여 기재합니다.

### 🎨 디자인 연동 (`FIGMA_TOKEN`)
* **발급처**: Figma 계정 설정 -> Personal access tokens 세션에서 새 토큰을 생성합니다.
* **용도**: 에이전트가 Figma 파일의 레이아웃 및 픽셀 정렬 상태를 분석하여 스크랩할 수 있도록 돕습니다.
