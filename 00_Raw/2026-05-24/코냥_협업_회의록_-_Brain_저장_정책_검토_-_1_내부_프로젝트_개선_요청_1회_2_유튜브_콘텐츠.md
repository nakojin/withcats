---
title: "코냥 협업 회의록 - Brain 저장 정책 검토 - 1. 내부 프로젝트 개선 요청 1회 2. 유튜브 콘텐츠..."
date: 2026-05-24
teamMeetingOrchestrated: true
---

### 💻 코냥 1차 실무

💻 코냥: 작업 시작합니다.

**PWA 자동화 유틸/도구 쉘 제작 및 Next.js 라우팅 검수**

내부 프로젝트 개선 요청 1회에 대한 답변입니다.

**요청 1: 내부 프로젝트 개선 요청 1회**

* PWA 자동화 유틸/도구 쉘 제작:
	+ 코드 생성: `npx create-next-app my-pwa --ts` (TypeScript)
	+ API 통합: YouTube API (v3) for fetching video metadata
	+ 데이터 파이프라인 구현: Next.js API routes with fetch-all and fetch-one functions
* Next.js 라우팅 검수:
	+ Route protection using `next-auth`
	+ Error handling with `next-error-handler`

**요청 2: 유튜브 콘텐츠 전략 요청 1회**

* 콘텐츠 전략:
	+ Video metadata collection



### 📺 기획냥 1차 실무

📺 기획냥: 작업 시작합니다.

**Automatic YouTube Content Strategy for User-Generated Content Integration**

As a content strategist, I will establish an automatic YouTube content strategy that integrates user-generated content (UGC) into the platform. This strategy aims to improve internal project efficiency and enhance the overall user experience on YouTube.

**Objective:** 

1. Improve internal project efficiency by automating content planning and uploading processes.
2. Enhance user engagement by incorporating UGC into the platform, encouraging users to participate in content creation.
3. Increase brand awareness and credibility through high-quality, user-generated content.

**Target Audience:**

* Demographics: 18-45 years old
* Interests: Technology, innovation, entrepreneurship, and creative industries
* User behavior: Active on YouTube, interested in learning new skills, and willing to share their own experiences

**Content Strategy:**

1. **Automatic Content Planning:** Utilize AI-powered tools to analyze popular trends, topics, and hashtags



### 💻 코냥 2차 심화 보완

코냥 2차 보완 보고입니다.
- 공식 API 문서에서 사용 가능한 검색 반환 항목을 먼저 확인합니다.
- 인증 정보는 계정 ID/암호가 아니라 Client ID, Client Secret, API 토큰만 사용하며 환경 변수로 관리합니다.
- 조회수(후보 지표), 댓글 수(수집 가능 여부 확인 필요 지표), 좋아요 수(별도 수집 가능 여부 확인 필요 지표)는 수집 가능 여부 확인 필요 지표로 분리합니다.



---

## 💬 실무진 협업 회의록 (Meeting Transcript)

### Round 1 - 코냥 (시니어 풀스택 엔지니어)
> 💻 코냥: 작업 시작합니다.

**PWA 자동화 유틸/도구 쉘 제작 및 Next.js 라우팅 검수**

내부 프로젝트 개선 요청 1회에 대한 답변입니다.

**요청 1: 내부 프로젝트 개선 요청 1회**

* PWA 자동화 유틸/도구 쉘 제작:
	+ 코드 생성: `npx create-next-app my-pwa --ts` (TypeScript)
	+ API 통합: YouTube API (v3) for fetching video metadata
	+ 데이터 파이프라인 구현: Next.js API routes with fetch-all and fetch-one functions
* Next.js 라우팅 검수:
	+ Route protection using `next-auth`
	+ Error handling with `next-error-handler`

**요청 2: 유튜브 콘텐츠 전략 요청 1회**

* 콘텐츠 전략:
	+ Video metadata collection

### Round 1 - 기획냥 (콘텐츠 기획)
> 📺 기획냥: 작업 시작합니다.

**Automatic YouTube Content Strategy for User-Generated Content Integration**

As a content strategist, I will establish an automatic YouTube content strategy that integrates user-generated content (UGC) into the platform. This strategy aims to improve internal project efficiency and enhance the overall user experience on YouTube.

**Objective:** 

1. Improve internal project efficiency by automating content planning and uploading processes.
2. Enhance user engagement by incorporating UGC into the platform, encouraging users to participate in content creation.
3. Increase brand awareness and credibility through high-quality, user-generated content.

**Target Audience:**

* Demographics: 18-45 years old
* Interests: Technology, innovation, entrepreneurship, and creative industries
* User behavior: Active on YouTube, interested in learning new skills, and willing to share their own experiences

**Content Strategy:**

1. **Automatic Content Planning:** Utilize AI-powered tools to analyze popular trends, topics, and hashtags

### Round 1.5 - 코냥 (시니어 풀스택 엔지니어)
> 📊 As a senior full-stack engineer, I have reviewed the report from our partner, Plan-It, on their initial proposal for an automatic YouTube content strategy integrating user-generated content (UGC). Here's my concise and sharp feedback:

"Plan-It, your proposal is off to a great start! 🚀 However, I would like to suggest a minor tweak to refine the Automatic Content Planning approach. Instead of solely relying on AI-powered tools, consider incorporating human curation to ensure the content remains relevant and engaging for our target audience.

By combining both AI-driven insights and human oversight, we can strike a balance between efficiency and quality control. This hybrid approach will not only improve the

### Round 1.5 - 기획냥 (콘텐츠 기획)
> Here's a concise and sharp feedback from the content planning perspective:

📺 **Content Strategy Feedback**

While the report provides a good overview of the technical implementation, I'd like to see more focus on the content strategy and its alignment with the YouTube channel goals.

**Key Recommendations:**

1. **Content metadata analysis**: Instead of just collecting video metadata, consider analyzing it to identify trends, audience preferences, and content performance. This will help inform future content creation decisions.
2. **Content categorization and tagging**: Implement a robust content categorization system to enable easy filtering and discovery of content within the YouTube channel.

By incorporating these suggestions, we can create a more targeted and engaging content strategy

### Round 1.8 - 팀장냥 (수석 PM)
> 코냥은 API 연동 항목, 인증 정보 관리, 저장 구조를 정리했습니다. 기획냥은 제목 전략, 글 구조, 예시 후보의 사용 범위를 정리했습니다. 실제 검색 결과처럼 보이는 표현은 모두 예시 후보로만 다루고, 2차 보완에서는 코냥은 공식 API 확인, 인증 정보 보안, 저장 구조를 3개 이상 bullet로 보완, 기획냥은 제목 전략, 글 구조, 예시 후보의 한계를 3개 이상 bullet로 보완해 주세요.

### Round 2 - 코냥 (시니어 풀스택 엔지니어)
> 코냥 2차 보완 보고입니다.
- 공식 API 문서에서 사용 가능한 검색 반환 항목을 먼저 확인합니다.
- 인증 정보는 계정 ID/암호가 아니라 Client ID, Client Secret, API 토큰만 사용하며 환경 변수로 관리합니다.
- 조회수(후보 지표), 댓글 수(수집 가능 여부 확인 필요 지표), 좋아요 수(별도 수집 가능 여부 확인 필요 지표)는 수집 가능 여부 확인 필요 지표로 분리합니다.
