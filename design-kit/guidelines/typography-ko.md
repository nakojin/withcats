# 한국어 타이포그래피

## 폰트 조합

| 역할 | 기본 | 대안 | 토큰 |
|---|---|---|---|
| 본문·UI | Pretendard Variable | IBM Plex Sans KR (기술 톤), Noto Sans KR (구글 생태계), SUIT | `--font` |
| 디스플레이 | 본문과 동일 (차분한 서비스) | Black Han Sans (게임·스트리트), Gmarket Sans (커머스), Do Hyeon | `--font-display` |
| 숫자·코드 | `font-variant-numeric: tabular-nums` (`.tnum`) | JetBrains Mono, D2Coding | `--font-mono` |

- 디스플레이 폰트는 **제목·숫자·로고에만**. 본문에 쓰지 않는다.
- Black Han Sans 는 굵기가 400 하나뿐 → `font-weight: 400` 로 지정해야 가짜 볼드가 생기지 않는다.
- 폰트는 2종(+모노)까지. 3종이 넘으면 화면이 산만해진다.

## 불러오기

키트 기본은 **로컬 파일**(`starter/fonts/`)이라 오프라인에서도 동작한다.

```html
<link rel="stylesheet" href="css/fonts.css">   <!-- Pretendard 다이나믹 서브셋 + Black Han Sans -->
```

다이나믹 서브셋은 화면에 쓰인 글자 묶음의 woff2 만 받는다(전체 3MB 중 보통 수백 KB). 사이트 용량을 줄이고 싶고 인터넷 연결이 보장되면 CDN 으로 바꿔도 된다:

```html
<!-- 본문: 다이나믹 서브셋 — 화면에 쓰인 글자 묶음만 받는다 -->
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/variable/pretendardvariable-dynamic-subset.min.css">
<!-- 디스플레이 (필요할 때만) -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap">
```

- 버전은 고정(`@v1.3.9`). `@latest` 는 캐시 안 되고 깨질 수 있다.
- 폰트 스택 마지막에 `system-ui, 'Apple SD Gothic Neo', 'Malgun Gothic'` — 로드 전에도 한글이 고르게 보인다.

## 줄바꿈·행간

| 규칙 | 값 | 이유 |
|---|---|---|
| 단어 단위 줄바꿈 | `word-break: keep-all` | "피규\|어" 처럼 단어 중간에서 끊기는 것 방지 (base.css 적용됨) |
| 긴 URL·영문 | `overflow-wrap: anywhere` | keep-all 과 함께 써야 넘침 방지 |
| 제목 | `text-wrap: balance` | 두 줄 제목의 길이를 맞춤 |
| 본문 | `text-wrap: pretty` | 마지막 줄에 한 글자만 남는 것 방지 |
| 본문 행간 | 1.6 (`--lh`) | 한글은 영문보다 글자 면이 꽉 차서 1.5~1.7 |
| 제목 행간 | 1.25 (`--lh-tight`) | 큰 글자는 좁게 |
| 한 줄 길이 | 최대 35~40자 (`max-width: 40em` 정도) | 한글 기준 읽기 편한 길이 |

## 크기

- 유동 스케일 `--fs-xs … --fs-2xl` 은 `clamp()` 로 360px → 1280px 사이에서 자연스럽게 커진다. 브레이크포인트마다 크기를 다시 정하지 않는다.
- 모바일 본문 최소 16px — iOS 는 입력칸 글자가 16px 미만이면 확대해 버린다.
- 자간: 한글 본문은 기본값(0) 또는 -0.01em. 큰 제목만 -0.02em. 넓히지 않는다.
- 굵기: 본문 400, 강조 600, 제목 700. 800 이상은 디스플레이용.

## 쓰기 (UX 라이팅)

- 해요체로 통일: "저장했어요", "다시 시도해 주세요".
- 버튼은 동사로 끝: "담기", "구매하러 가기" — "확인" 대신 무엇을 확인하는지.
- 오류는 사용자 탓 하지 않기: "잘못 입력하셨습니다" → "이메일 형식이 아니에요".
- 숫자: 천 단위 쉼표, 단위 붙여 쓰기(`12,900원`, `3일 전`), 표·랭킹은 `.tnum` 으로 자리 맞춤.
