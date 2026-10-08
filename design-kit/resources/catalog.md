# 웹프론트 디자인·UI/UX 자료 100선

> 자동 생성 파일 — `catalog.json` 을 고치고 `node scripts/build-catalog.mjs` 실행. 기준일 2026-10-08.
> stars 는 대략 구간. license 는 도입 전 저장소 LICENSE 파일로 재확인. pick: 3=기본 탑재 권장, 2=상황별 1순위, 1=참고·학습용

## 기본 탑재 권장 (★★★)

| # | 자료 | 분류 | 라이선스 | 쓰임 |
|---|---|---|---|---|
| 11 | [shadcn/ui](https://github.com/shadcn-ui/ui) | 컴포넌트 라이브러리·헤드리스 UI | MIT | 복사해서 소유하는 컴포넌트. React 프로젝트의 기본값 |
| 21 | [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | CSS 프레임워크·토큰·리셋 | MIT | 유틸리티 CSS 표준. 빌드 있는 프로젝트의 기본값 |
| 22 | [Open Props](https://github.com/argyleink/open-props) | CSS 프레임워크·토큰·리셋 | MIT | CSS 변수만으로 된 토큰(그림자·이징·간격·그라데이션). 빌드 없이 바로 |
| 26 | [modern-normalize](https://github.com/sindresorhus/modern-normalize) | CSS 프레임워크·토큰·리셋 | MIT | 브라우저 기본 스타일 정규화 — 모든 프로젝트 첫 줄 |
| 29 | [Pretendard](https://github.com/orioncactus/pretendard) | 타이포그래피·한글 폰트 | OFL-1.1 | 한국어 웹 본문 표준급. 다이나믹 서브셋으로 빠름 |
| 37 | [Lucide](https://github.com/lucide-icons/lucide) | 아이콘 | ISC | 1,500+ 선 아이콘. 키트 기본 아이콘 |
| 45 | [GSAP](https://github.com/greensock/GSAP) | 애니메이션·모션 | GSAP Standard (상업 무료, 조건 있음) | 타임라인·ScrollTrigger·SplitText. 게임 같은 연출의 표준 |
| 46 | [Motion](https://github.com/motiondivision/motion) | 애니메이션·모션 | MIT | 구 Framer Motion. 바닐라 JS·React 둘 다. 스프링 물리 |
| 48 | [AutoAnimate](https://github.com/formkit/auto-animate) | 애니메이션·모션 | MIT | 한 줄로 리스트 추가·삭제·정렬 애니메이션 |
| 55 | [Embla Carousel](https://github.com/davidjerleke/embla-carousel) | 인터랙션 부품 (캐러셀·오버레이·드래그) | MIT | 가볍고 터치 좋은 캐러셀. 플러그인 구조 |
| 57 | [Floating UI](https://github.com/floating-ui/floating-ui) | 인터랙션 부품 (캐러셀·오버레이·드래그) | MIT | 툴팁·팝오버·드롭다운 위치 계산의 표준 |
| 73 | [Apache ECharts](https://github.com/apache/echarts) | 데이터 시각화 | Apache-2.0 | 대용량·대시보드 차트. 한국어 로캘 |
| 79 | [axe-core](https://github.com/dequelabs/axe-core) | 접근성·품질 검사 | MPL-2.0 | 접근성 자동 검사 엔진 — CI·브라우저 확장 |
| 80 | [Lighthouse](https://github.com/GoogleChrome/lighthouse) | 접근성·품질 검사 | Apache-2.0 | 성능·접근성·SEO 점수. CI 로 회귀 감시 |
| 83 | [Front-End Checklist](https://github.com/thedaviddias/Front-End-Checklist) | 접근성·품질 검사 | MIT | 출시 전 프론트 점검표 |
| 87 | [Radix Colors](https://github.com/radix-ui/colors) | 색상·테마 도구 | MIT | 용도별 12단계 색 스케일(라이트·다크). 대비 보장 |

## 목차

- **A. 디자인 시스템 (학습·레퍼런스)** (10) — 상태·간격·접근성을 어떻게 정의하는지 배우는 교과서
- **B. 컴포넌트 라이브러리·헤드리스 UI** (10) — 검증된 동작·접근성을 가진 부품
- **C. CSS 프레임워크·토큰·리셋** (8) — 스타일 기반과 디자인 토큰
- **D. 타이포그래피·한글 폰트** (8) — 품질 체감이 가장 큰 영역
- **E. 아이콘** (8) — 일관된 시각 언어
- **F. 애니메이션·모션** (10) — 인터랙션의 손맛
- **G. 인터랙션 부품 (캐러셀·오버레이·드래그)** (10) — 직접 만들면 버그가 많은 부품
- **H. 표현형 스타일 (게임·레트로·손그림·배경)** (8) — 브랜드 개성
- **I. 데이터 시각화** (6) — 대시보드·통계 화면
- **J. 접근성·품질 검사** (8) — 출시 전 자동·수동 점검
- **K. 색상·테마 도구** (5) — 대비가 보장된 팔레트
- **L. 큐레이션 목록·영감** (6) — 더 찾아볼 때의 출발점
- **M. 스타터 템플릿** (3) — 새 프로젝트 뼈대

## A. 디자인 시스템 (학습·레퍼런스)

_상태·간격·접근성을 어떻게 정의하는지 배우는 교과서_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 1 | [Material Web (Material Design 3)](https://github.com/material-components/material-web) | Apache-2.0 | 1만+ | ★ | M3 컴포넌트의 상태 레이어·모션 토큰 정의 참고. 웹 컴포넌트라 프레임워크 무관 |
| 2 | [Primer CSS (GitHub)](https://github.com/primer/css) | MIT | 1만+ | ★ | 유틸리티+컴포넌트 CSS 의 모범. 버튼 상태(hover/active/disabled/focus) 정의가 꼼꼼 |
| 3 | [Carbon Design System (IBM)](https://github.com/carbon-design-system/carbon) | Apache-2.0 | 8천+ | ★ | 데이터 밀도 높은 화면, 그리드·간격 체계 학습 |
| 4 | [U.S. Web Design System (USWDS)](https://github.com/uswds/uswds) | CC0-1.0 (번들 폰트 OFL 등 개별) | 7천+ | ★ | 공공 수준 접근성·폼·에러 메시지 패턴, 컴포넌트별 사용 가이드 |
| 5 | [GOV.UK Frontend](https://github.com/alphagov/govuk-frontend) | MIT | 1천+ | ★★ | 접근성 최상급 폼·에러 메시지 패턴. 폼 설계할 때 1순위 참고 |
| 6 | [Radix Themes](https://github.com/radix-ui/themes) | MIT | 8천+ | ★★ | 색 12단계 스케일·라디우스·스케일링 토큰 설계 참고 |
| 7 | [Fluent UI (Microsoft)](https://github.com/microsoft/fluentui) | MIT | 2만+ | ★ | 디자인 토큰 계층(global→alias→component) 구조 학습 |
| 8 | [React Spectrum / React Aria (Adobe)](https://github.com/adobe/react-spectrum) | Apache-2.0 | 1.5만+ | ★★ | React Aria 훅: 접근성 완비 인터랙션의 업계 표준 |
| 9 | [Ant Design](https://github.com/ant-design/ant-design) | MIT | 9만+ | ★ | 관리자·B2B 화면 패턴 백과사전 |
| 10 | [Chakra UI](https://github.com/chakra-ui/chakra-ui) | MIT | 3.8만+ | ★ | 스타일 props·테마 토큰 설계, Ark UI 상태머신 기반 |

## B. 컴포넌트 라이브러리·헤드리스 UI

_검증된 동작·접근성을 가진 부품_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 11 | [shadcn/ui](https://github.com/shadcn-ui/ui) | MIT | 12만+ | ★★★ | 복사해서 소유하는 컴포넌트. React 프로젝트의 기본값 |
| 12 | [Radix Primitives](https://github.com/radix-ui/primitives) | MIT | 1.7만+ | ★★ | 스타일 없는 접근성 완비 부품(다이얼로그·드롭다운·탭) |
| 13 | [Headless UI](https://github.com/tailwindlabs/headlessui) | MIT | 2.6만+ | ★★ | React/Vue 용 무스타일 부품. Tailwind 와 궁합 |
| 14 | [Ariakit](https://github.com/ariakit/ariakit) | MIT | 8천+ | ★ | 콤보박스·메뉴 등 까다로운 접근성 패턴 |
| 15 | [Ark UI](https://github.com/chakra-ui/ark) | MIT | 5천+ | ★ | React/Vue/Solid/Svelte 공용 헤드리스 부품 (Zag 상태머신) |
| 16 | [daisyUI](https://github.com/saadeghi/daisyui) | MIT | 4만+ | ★★ | Tailwind 클래스 이름만으로 컴포넌트. 테마 전환이 쉬움 |
| 17 | [Flowbite](https://github.com/themesberg/flowbite) | MIT (Pro 별도) | 8천+ | ★★ | 바닐라 JS 로 동작 — 워드프레스·정적 사이트에 붙이기 쉬움 |
| 18 | [HyperUI](https://github.com/markmead/hyperui) | MIT | 1만+ | ★★ | 복사-붙여넣기 HTML 블록(랜딩·폼·카드·필터) |
| 19 | [Mantine](https://github.com/mantinedev/mantine) | MIT | 2.8만+ | ★★ | 100개+ 컴포넌트와 훅. 대시보드·폼 빠르게 |
| 20 | [Uiverse Galaxy](https://github.com/uiverse-io/galaxy) | MIT | 1.3만+ | ★★ | 커뮤니티 버튼·토글·로더 수천 개 — 아이디어 창고 |

## C. CSS 프레임워크·토큰·리셋

_스타일 기반과 디자인 토큰_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 21 | [Tailwind CSS](https://github.com/tailwindlabs/tailwindcss) | MIT | 9.5만+ | ★★★ | 유틸리티 CSS 표준. 빌드 있는 프로젝트의 기본값 |
| 22 | [Open Props](https://github.com/argyleink/open-props) | MIT | 5천+ | ★★★ | CSS 변수만으로 된 토큰(그림자·이징·간격·그라데이션). 빌드 없이 바로 |
| 23 | [Simple.css](https://github.com/kevquirk/simple.css) | MIT | 5천+ | ★★ | 클래스 없이 시맨틱 HTML 만으로 깔끔한 기본 스타일 — 문서·관리 페이지 |
| 24 | [UnoCSS](https://github.com/unocss/unocss) | MIT | 1.7만+ | ★ | 온디맨드 원자 CSS 엔진. Tailwind 대안 |
| 25 | [Bootstrap](https://github.com/twbs/bootstrap) | MIT | 17만+ | ★ | 레거시·관리자 화면. 그리드·유틸리티 문서가 탄탄 |
| 26 | [modern-normalize](https://github.com/sindresorhus/modern-normalize) | MIT | 7천+ | ★★★ | 브라우저 기본 스타일 정규화 — 모든 프로젝트 첫 줄 |
| 27 | [Utopia (유동 타이포·간격)](https://github.com/trys/utopia-core) | ISC | 100+ | ★★ | 화면 폭에 비례하는 clamp() 타이포·간격 스케일 생성 |
| 28 | [Style Dictionary](https://github.com/style-dictionary/style-dictionary) | Apache-2.0 | 5천+ | ★★ | 토큰 JSON → CSS/iOS/Android 변환. 디자인 시스템 확장 시 |

## D. 타이포그래피·한글 폰트

_품질 체감이 가장 큰 영역_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 29 | [Pretendard](https://github.com/orioncactus/pretendard) | OFL-1.1 | 3.5천+ | ★★★ | 한국어 웹 본문 표준급. 다이나믹 서브셋으로 빠름 |
| 30 | [SUIT](https://github.com/sun-typeface/SUIT) | OFL-1.1 | 300+ | ★★ | Pretendard 대안. 조금 더 둥글고 친근한 산세리프 |
| 31 | [Wanted Sans](https://github.com/wanteddev/wanted-sans) | OFL-1.1 | 300+ | ★★ | 원티드 서체. 숫자·영문 균형 좋아 대시보드에 |
| 32 | [IBM Plex Sans KR](https://github.com/IBM/plex) | OFL-1.1 | 1.1만+ | ★ | 기술·데이터 톤 한글 본문 폰트, Plex Mono 와 짝 맞추기 좋음 |
| 33 | [Noto CJK](https://github.com/notofonts/noto-cjk) | OFL-1.1 | 4천+ | ★ | 한중일 전부 커버. 다국어 서비스의 폴백 |
| 34 | [Inter](https://github.com/rsms/inter) | OFL-1.1 | 1.8만+ | ★★ | UI 영문 표준. 숫자 탭 정렬(tnum) 지원 |
| 35 | [Fontsource](https://github.com/fontsource/fontsource) | MIT (폰트는 각자) | 6천+ | ★★ | 구글·오픈 폰트를 npm 으로 자체 호스팅 |
| 36 | [Capsize](https://github.com/seek-oss/capsize) | MIT | 1.7천+ | ★ | 폰트 위아래 여백 제거 — 텍스트 정렬을 픽셀 단위로 (npm: @capsizecss/core) |

## E. 아이콘

_일관된 시각 언어_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 37 | [Lucide](https://github.com/lucide-icons/lucide) | ISC | 2.4만+ | ★★★ | 1,500+ 선 아이콘. 키트 기본 아이콘 |
| 38 | [Tabler Icons](https://github.com/tabler/tabler-icons) | MIT | 2.2만+ | ★★ | 5,000+ 아이콘. Lucide 에 없는 것 보충 |
| 39 | [Phosphor Icons](https://github.com/phosphor-icons/homepage) | MIT | 7천+ | ★★ | 굵기 6종(Thin~Fill·Duotone). 게임·캐주얼 UI 에 Fill 이 잘 어울림 (npm: @phosphor-icons/web) |
| 40 | [Heroicons](https://github.com/tailwindlabs/heroicons) | MIT | 2.2만+ | ★★ | Tailwind 팀 아이콘. Outline/Solid/Mini |
| 41 | [Remix Icon](https://github.com/Remix-Design/RemixIcon) | Remix Icon License v1.0 (사용·수정 허용, 아이콘 자체 재판매 금지) | 8천+ | ★ | 중국·아시아 서비스 아이콘 다수(결제·메신저류) |
| 42 | [Iconify](https://github.com/iconify/iconify) | MIT (아이콘 세트는 각자) | 5천+ | ★★ | 200개+ 아이콘 세트를 한 API 로 — 필요한 것만 번들 |
| 43 | [Simple Icons](https://github.com/simple-icons/simple-icons) | CC0-1.0 (상표는 각 회사) | 2.3만+ | ★★ | 브랜드 로고 아이콘(SNS 공유 버튼 등). 상표 가이드 준수 |
| 44 | [Material Symbols](https://github.com/google/material-design-icons) | Apache-2.0 | 5만+ | ★ | 가변 폰트 아이콘(굵기·채움·크기 축) |

## F. 애니메이션·모션

_인터랙션의 손맛_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 45 | [GSAP](https://github.com/greensock/GSAP) | GSAP Standard (상업 무료, 조건 있음) | 2.8만+ | ★★★ | 타임라인·ScrollTrigger·SplitText. 게임 같은 연출의 표준 |
| 46 | [Motion](https://github.com/motiondivision/motion) | MIT | 3.3만+ | ★★★ | 구 Framer Motion. 바닐라 JS·React 둘 다. 스프링 물리 |
| 47 | [Anime.js](https://github.com/juliangarnier/anime) | MIT | 7만+ | ★★ | 가볍고 문법 쉬움. v4 타임라인·스크롤 연동 |
| 48 | [AutoAnimate](https://github.com/formkit/auto-animate) | MIT | 1.3만+ | ★★★ | 한 줄로 리스트 추가·삭제·정렬 애니메이션 |
| 49 | [lottie-web](https://github.com/airbnb/lottie-web) | MIT | 3만+ | ★★ | After Effects 애니메이션 재생 — 축하·로딩·빈 상태 (신규는 LottieFiles/dotlottie-web 도 검토) |
| 50 | [Rive (웹 런타임)](https://github.com/rive-app/rive-wasm) | MIT | 1천+ | ★★ | 상태머신 있는 인터랙티브 애니메이션(캐릭터 반응) |
| 51 | [Lenis](https://github.com/darkroomengineering/lenis) | MIT | 1.6만+ | ★★ | 부드러운 스크롤. GSAP ScrollTrigger 와 조합 |
| 52 | [NumberFlow](https://github.com/barvian/number-flow) | MIT | 7.7천+ | ★★ | 숫자가 굴러가며 바뀌는 연출 — XP·가격·카운터 |
| 53 | [swup](https://github.com/swup/swup) | MIT | 5.2천+ | ★★ | 정적/멀티페이지 사이트의 페이지 전환 애니메이션 |
| 54 | [react-spring](https://github.com/pmndrs/react-spring) | MIT | 2.9만+ | ★ | 스프링 물리 기반 React 애니메이션 |

## G. 인터랙션 부품 (캐러셀·오버레이·드래그)

_직접 만들면 버그가 많은 부품_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 55 | [Embla Carousel](https://github.com/davidjerleke/embla-carousel) | MIT | 8천+ | ★★★ | 가볍고 터치 좋은 캐러셀. 플러그인 구조 |
| 56 | [Swiper](https://github.com/nolimits4web/swiper) | MIT | 4만+ | ★★ | 기능 많은 슬라이더(효과·썸네일·가상 슬라이드) |
| 57 | [Floating UI](https://github.com/floating-ui/floating-ui) | MIT | 3만+ | ★★★ | 툴팁·팝오버·드롭다운 위치 계산의 표준 |
| 58 | [Vaul](https://github.com/emilkowalski/vaul) | MIT | 7천+ | ★★ · 참고용 | 드래그로 닫는 바텀시트의 UX 레퍼런스. 저장소는 유지보수 종료 — 실사용은 react-modal-sheet 또는 <dialog>+Motion |
| 59 | [Sonner](https://github.com/emilkowalski/sonner) | MIT | 1.3만+ | ★★ | 쌓이고 스와이프로 닫히는 토스트 |
| 60 | [SortableJS](https://github.com/SortableJS/Sortable) | MIT | 3만+ | ★★ | 드래그 정렬(바닐라 JS). 칸반·순서 편집 |
| 61 | [dnd kit](https://github.com/clauderic/dnd-kit) | MIT | 1.7만+ | ★★ | React 드래그앤드롭, 키보드 접근성 포함 |
| 62 | [cmdk](https://github.com/dip/cmdk) | MIT | 1.3만+ | ★★ | ⌘K 커맨드 팔레트 — 검색 UX |
| 63 | [PhotoSwipe](https://github.com/dimsemenov/PhotoSwipe) | MIT | 2.4만+ | ★★ | 이미지 라이트박스(핀치 줌·스와이프) |
| 64 | [medium-zoom](https://github.com/francoischalifour/medium-zoom) | MIT | 4천 | ★ | 이미지 클릭 확대 한 줄 |

## H. 표현형 스타일 (게임·레트로·손그림·배경)

_브랜드 개성_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 65 | [Rough.js](https://github.com/rough-stuff/rough) | MIT | 2만+ | ★★ | 손그림 스타일 도형(Canvas/SVG). 업데이트는 뜸하지만 Excalidraw 가 쓰는 안정 버전 |
| 66 | [Rough Notation](https://github.com/rough-stuff/rough-notation) | MIT | 9천+ | ★★ · 참고용 | 텍스트 손그림 밑줄·동그라미 애니메이션. 2020년 이후 업데이트 없음 — 동작은 하지만 참고용 |
| 67 | [Excalidraw](https://github.com/excalidraw/excalidraw) | MIT | 13만+ | ★ | 손그림 톤 레퍼런스, 화이트보드 임베드·와이어프레임 |
| 68 | [NES.css](https://github.com/nostalgic-css/NES.css) | MIT | 2만+ | ★ · 참고용 | 8비트 게임 UI 프레임 — 유지보수 종료, 시각 레퍼런스로만 |
| 69 | [augmented-ui](https://github.com/propjockey/augmented-ui) | BSD-2-Clause | 1천+ | ★★ · 참고용 | 깎인 모서리·HUD 프레임. 2020년 이후 정체 — 아이디어만 가져와 clip-path 로 직접 구현 권장 |
| 70 | [Magic UI](https://github.com/magicuidesign/magicui) | MIT | 2.2만+ | ★ | shadcn CLI 로 가져오는 애니메이션 컴포넌트(마키·숫자·빛 효과) |
| 71 | [98.css](https://github.com/jdan/98.css) | MIT | 1만+ | ★ | 윈도우 98 UI — 레트로 무드 레퍼런스 |
| 72 | [tsParticles](https://github.com/tsparticles/tsparticles) | MIT | 8천+ | ★ | 파티클·컨페티 효과(레벨업·당첨 연출) |

## I. 데이터 시각화

_대시보드·통계 화면_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 73 | [Apache ECharts](https://github.com/apache/echarts) | Apache-2.0 | 6만+ | ★★★ | 대용량·대시보드 차트. 한국어 로캘 |
| 74 | [Chart.js](https://github.com/chartjs/Chart.js) | MIT | 6.5만+ | ★★ | 가벼운 기본 차트 8종 |
| 75 | [D3](https://github.com/d3/d3) | ISC | 11만+ | ★ | 맞춤형 시각화의 원천 — 학습 곡선 높음 |
| 76 | [ApexCharts](https://github.com/apexcharts/apexcharts.js) | ApexCharts Community License (연매출 200만 달러 미만 무료, 초과 시 유료) | 1.4만+ | ★★ | 인터랙티브 차트, 기본 디자인이 예쁨. v5 부터 라이선스 조건 있음 |
| 77 | [uPlot](https://github.com/leeoniya/uPlot) | MIT | 1만+ | ★ | 초경량·초고속 시계열 차트 |
| 78 | [visx (Airbnb)](https://github.com/airbnb/visx) | MIT | 1.9만+ | ★ | React + D3 저수준 시각화 부품 |

## J. 접근성·품질 검사

_출시 전 자동·수동 점검_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 79 | [axe-core](https://github.com/dequelabs/axe-core) | MPL-2.0 | 7.5천+ | ★★★ | 접근성 자동 검사 엔진 — CI·브라우저 확장 |
| 80 | [Lighthouse](https://github.com/GoogleChrome/lighthouse) | Apache-2.0 | 2.9만+ | ★★★ | 성능·접근성·SEO 점수. CI 로 회귀 감시 |
| 81 | [web-vitals](https://github.com/GoogleChrome/web-vitals) | Apache-2.0 | 8천+ | ★★ | 실사용자 LCP·INP·CLS 측정 |
| 82 | [Pa11y](https://github.com/pa11y/pa11y) | LGPL-3.0 | 4천+ | ★ | 명령줄 접근성 검사, 여러 페이지 일괄 |
| 83 | [Front-End Checklist](https://github.com/thedaviddias/Front-End-Checklist) | MIT | 7만+ | ★★★ | 출시 전 프론트 점검표 |
| 84 | [The A11Y Project](https://github.com/a11yproject/a11yproject.com) | Apache-2.0 | 3.9천+ | ★★ | 접근성 체크리스트·패턴 설명 |
| 85 | [focus-trap](https://github.com/focus-trap/focus-trap) | MIT | 1.5천+ | ★★ | 모달·시트 안에 키보드 포커스 가두기 |
| 86 | [Playwright](https://github.com/microsoft/playwright) | Apache-2.0 | 9.7만+ | ★★ | 화면 회귀 테스트·스크린샷 비교 |

## K. 색상·테마 도구

_대비가 보장된 팔레트_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 87 | [Radix Colors](https://github.com/radix-ui/colors) | MIT | 1.7천+ | ★★★ | 용도별 12단계 색 스케일(라이트·다크). 대비 보장 |
| 88 | [Leonardo (Adobe)](https://github.com/adobe/leonardo) | Apache-2.0 | 2천+ | ★★ | 목표 대비율로 팔레트 생성 |
| 89 | [chroma.js](https://github.com/gka/chroma.js) | BSD-3-Clause (ColorBrewer 팔레트는 Apache-2.0) | 1만+ | ★ | 색 보간·스케일·대비 계산 |
| 90 | [Culori](https://github.com/Evercoder/culori) | MIT | 1천+ | ★ | OKLCH 등 최신 색공간 변환 |
| 91 | [Color.js](https://github.com/color-js/color.js) | MIT | 2천+ | ★ | CSS Color 4 명세 작성자들이 만든 색 라이브러리, APCA 대비 |

## L. 큐레이션 목록·영감

_더 찾아볼 때의 출발점_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 92 | [Design Resources for Developers](https://github.com/bradtraversy/design-resources-for-developers) | MIT | 6만+ | ★★ | 무료 디자인 리소스 대형 목록 |
| 93 | [awesome-design-systems](https://github.com/alexpate/awesome-design-systems) | Unlicense | 2.6만+ | ★★ | 기업 디자인 시스템 모음 |
| 94 | [awesome-design](https://github.com/gztchan/awesome-design) | — | 1.5만+ | ★ · 참고용 | 디자인 도구·리소스 종합 (2024년 이후 갱신 정체) |
| 95 | [awesome-web-animation](https://github.com/sergey-pimenov/awesome-web-animation) | CC0-1.0 | 2천+ | ★ | 웹 애니메이션 라이브러리·글 목록 |
| 96 | [awesome-creative-coding](https://github.com/terkelg/awesome-creative-coding) | CC0-1.0 (미확인) | 1.4만+ | ★ | 제너러티브·인터랙티브 아트 자료 |
| 97 | [Codrops (tympanus) 데모 저장소](https://github.com/codrops) | MIT (데모별 확인) | — | ★★ | 실험적 인터랙션 데모 수백 개(GitHub org: codrops). 연출 아이디어 1순위 |

## M. 스타터 템플릿

_새 프로젝트 뼈대_

| # | 자료 | 라이선스 | ★ GitHub | 추천 | 쓰임 |
|---|---|---|---|---|---|
| 98 | [AstroWind](https://github.com/arthelokyo/astrowind) | MIT | 6천+ | ★★ | Astro + Tailwind 블로그·랜딩 스타터 |
| 99 | [Sage (Roots)](https://github.com/roots/sage) | MIT | 1.2만+ | ★★ | Vite + Tailwind + Blade 워드프레스 테마 스타터 |
| 100 | [Cruip Tailwind Landing Template](https://github.com/cruip/tailwind-landing-page-template) | GPL-3.0 | 4.5천+ | ★ | 랜딩 페이지 구성 참고 (GPL 이라 코드 재사용 시 주의) |

추천: ★★★ 기본 탑재 권장 · ★★ 상황별 1순위 · ★ 참고·학습용. "참고용"은 유지보수가 멈췄지만 구현 방식을 배울 가치가 있는 저장소.
