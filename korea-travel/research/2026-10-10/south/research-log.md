# 조사 기록
## 결과
70개 독립 장소 레코드. 전북 9, 광주 6, 전남 9, 대구 5, 경북 10, 부산 5, 울산 6, 경남 10, 제주 10. 모든 레코드에 실제 열람한 공식 페이지 URL, 제목, 확인일, 근거와 불확실성 포함. 각 장소에 2개 이상의 현장 팁을 작성했다.
## 방법
한국관광공사 VISITKOREA 및 운영기관 공식 페이지를 일반 웹 검색으로 찾고 원문 HTML을 열어 소개·주소·관련 시설 내용을 확인했다. 검색 결과만으로 레코드를 확정하지 않았다. 관광 API, 관광 MCP, 자동 수집 스크립트는 사용하지 않았다. 로컬 Python은 조사 결과의 JSON/MD 편집·검증에만 사용했다.
본문의 변동 정보나 오래된 가격·상충하는 운영일은 데이터에 고정하지 않았다. 최상급, 약효, 확정되지 않은 역사 전승·연대, 동물 관찰·개화 보장 문구를 제외했다.
## 중복 처리
original-inventory.json의 기존 56개 제목과 대조했다. 기존 도시·섬 복합 레코드인 목포·여수·담양·거제·남해·통영 등의 하위 명소는 신규 수 확보 수단으로 사용하지 않았다. 순천 새 장소는 순천만 습지·정원과 별도인 선암사·낙안읍성이다. 박물관·사찰·공원 내부 건물과 보조 박물관은 부모 장소에 통합했다. 군산근대역사박물관과 근대건축관은 별도 건물·전시 장소로 각각 기록했다.
## 유보·오류·충돌
광주·전남 일부 공식 주소에서 전남광주통합특별시 표기를 확인했다. 이를 근거로 법적 행정변경을 단정하지 않고 기존 17권역은 호환 분류임을 표시했다. 통합 책임자에게 별도 확인을 요청했다.
거창항노화힐링랜드의 상세 페이지와 과거 기사 사이 휴무 요일 차이, 국립나주박물관의 KTO와 운영기관 주말 종료시간 차이를 발견해 운영값을 보류했다.
운주사 창건 연대의 모순 문장, 다산초당 설명의 황사영백서 작성자 및 거주기간 오류 우려는 채택하지 않았다.
내장사 등 일부 KTO 페이지는 본문 로드 실패로 제외했다. 화엄사 소개는 구체 볼거리 근거가 부족했고 운영기관 홈페이지 요청이 타임아웃으로 끝나 추가하지 않았다. 우회 접속·접근 제한 해제는 하지 않았다.
## 편집 기준
계절 추천과 관람 순서는 일반적 편집 판단으로 명시했다. 실제 거리·지형·하위 구역의 관계는 읽은 공식 설명에 기반한다. 어린이관·체험·탑승·암자·야간조명은 운영을 보장하지 않는다. 호랑이 관람 불확실성, 해안 물때·파도, 주민 생활 공간·문화재 보호를 구별했다.
## 출처 색인
### kr-jeonbuk-wanggung-ri / 익산 왕궁리유적
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=73417 | VISITKOREA — Archaeological Site in Wanggung-ri | official_page_read | 2026-10-10 | 백제 왕궁터에서 사찰로 바뀐 공간의 흔적; 낮은 구릉에 펼쳐진 발굴 유적
### kr-jeonbuk-gunsan-modern-history / 군산근대역사박물관
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=77116 | VISITKOREA — Gunsan Modern History Museum | official_page_read | 2026-10-10 | 해양물류역사관의 군산항 전시; 독립영웅관; 1930년대 군산 거리를 다룬 근대생활관
- https://museum.gunsan.go.kr/index_Archive.jsp | 군산근대역사박물관 — 전시 및 아카이브 | official_page_read | 2026-10-10 | 해양물류역사관·독립영웅관·근대생활관의 전시 주제를 본문에서 확인.
### kr-jeonbuk-gunsan-modern-architecture / 군산근대건축관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=1580843 | VISITKOREA — Gunsan Modern Architecture Exhibition Hall | official_page_read | 2026-10-10 | 옛 조선은행 군산지점의 붉은 벽돌과 높은 지붕; 군산 근대건축·화폐·역사자료 전시
### kr-jeonbuk-seonunsa / 고창 선운사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111739 | VISITKOREA — Gochang Seonunsa Temple | official_page_read | 2026-10-10 | 선운사 사찰 경관; 천연기념물 동백나무숲
### kr-gwangju-yangnim-history / 양림역사문화마을
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=193806 | VISITKOREA — MUST-HAVE ITEMS IN GWANGJU | official_page_read | 2026-10-10 | 근대 선교 관련 건축과 한옥이 함께 있는 마을; 이장우 가옥·오웬기념각 등 역사 공간; 재활용 재료를 활용한 펭귄마을 예술
### kr-gwangju-mudeungsan / 무등산국립공원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=193806 | VISITKOREA — MUST-HAVE ITEMS IN GWANGJU | official_page_read | 2026-10-10 | 입석대·서석대 암석 경관; 장불재와 백마능선의 억새
### kr-jeonbuk-chaeseokgang / 부안 채석강
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110874 | VISITKOREA — Chaeseokgang Cliff | official_page_read | 2026-10-10 | 책을 겹친 듯한 해안 퇴적층; 절벽과 바다가 만나는 경관
### kr-jeonbuk-jeokbyeokgang / 부안 적벽강
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=82266 | VISITKOREA — Jeokbyeokgang Cliffs | official_page_read | 2026-10-10 | 화산암과 퇴적물이 만난 암석 경관; 후박나무 군락 주변 생태
### kr-jeonbuk-naesosa / 부안 내소사
- https://english.visitkorea.or.kr/svc/sp/HallyuNew/contentsView.do?dataSetId=70&vcontsId=198507 | VISITKOREA — Embark on a Heart-fluttering Romance Tour of See You in My 19th Life | official_page_read | 2026-10-10 | 전나무 진입 숲길; 대웅전의 정교한 꽃무늬 나무 창살
### kr-jeonbuk-hagwon-farm / 고창 학원농장
- https://english.visitkorea.or.kr/svc/sp/HallyuNew/contentsView.do?dataSetId=70&vcontsId=198507 | VISITKOREA — Embark on a Heart-fluttering Romance Tour of See You in My 19th Life | official_page_read | 2026-10-10 | 청보리 재배 경관으로 알려진 농장; 메밀·해바라기·코스모스 등 경관 작물
### kr-gwangju-uijae-museum / 의재미술관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=215986 | VISITKOREA — Uijae Museum of Korean Art | official_page_read | 2026-10-10 | 허백련을 기리는 미술관; 완만한 길의 곡선을 반영한 건축과 전시 공간
### kr-gwangju-sajik-park / 광주 사직공원
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=81415 | VISITKOREA — Gwangju Sajik Park | official_page_read | 2026-10-10 | 사직단의 역사와 복원된 공간; 양파정·팔각정 등 도심 전망 공간
### kr-gwangju-national-museum / 국립광주박물관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=111459 | VISITKOREA — Gwangju National Museum | official_page_read | 2026-10-10 | 광주·전남 지역 역사문화 자료 전시; 어린이·교육 체험 공간
### kr-gwangju-asia-culture-center / 국립아시아문화전당
- https://www.acc.go.kr/main/contents.do?PID=050801 | 국립아시아문화전당 — 박물관 소개 | official_page_read | 2026-10-10 | 아시아문화박물관 상설·기획 전시; 아시아 문화자료 아카이브와 특별열람 공간
### kr-jeonbuk-gochang-dolmen / 고창 고인돌 유적
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=94408 | VISITKOREA — Gochang Dolmen Site | official_page_read | 2026-10-10 | 야외 고인돌 유적 경관; 청동기 생활과 무덤 문화를 설명하는 박물관
### kr-daegu-arboretum / 대구수목원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=81562 | VISITKOREA — Daegu Arboretum | official_page_read | 2026-10-10 | 쓰레기매립지를 복원한 식물원; 선인장·약용식물 등을 나눈 주제원
### kr-daegu-dodong-seowon / 도동서원
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=88740 | VISITKOREA — Dodongseowon Confucian Academy | official_page_read | 2026-10-10 | 유학 교육 공간인 도동서원의 건물군; 전란 이후 현재 위치로 옮겨 세운 서원 역사
### kr-daegu-art-museum / 대구미술관
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=78255 | VISITKOREA — Daegu Art Museum | official_page_read | 2026-10-10 | 대구 미술의 역사와 국내외 동시대 미술 기획전; 미술정보센터의 자료 열람·휴게 공간
### kr-daegu-apsan-observatory / 앞산 전망대·케이블카
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=68080 | VISITKOREA — Apsan Cable Car (Apsan Observatory) | official_page_read | 2026-10-10 | 대구 도심 파노라마; 도시와 산을 연결하는 전망대 건축
### kr-daegu-national-science-museum / 국립대구과학관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=65612 | VISITKOREA — Daegu National Science Museum | official_page_read | 2026-10-10 | 어린이 참여형 과학 전시; 천체투영관과 4D 영상 시설
### kr-ulsan-jangsaengpo-whale-museum / 장생포 고래박물관
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=85947 | VISITKOREA — Jangsaengpo Whale Museum | official_page_read | 2026-10-10 | 대형 고래 골격; 고래의 진화·생태와 포경 도구 전시
### kr-ulsan-bangudae-petroglyphs / 울주 대곡리 반구대 암각화
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=90261 | VISITKOREA — Petroglyphs of Bangudae Terrace in Daegok-ri | official_page_read | 2026-10-10 | 바위면의 바다·육지 동물과 사냥 장면; 반구천 주변 절벽 경관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=75310 | VISITKOREA — Ulsan Petroglyph Museum | official_page_read | 2026-10-10 | 암각화 모형과 영상 전시를 확인. 실제 암각화 관찰의 보조 공간으로만 사용.
### kr-ulsan-taehwagang-garden / 태화강 국가정원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=80718 | VISITKOREA — Taehwagang National Garden | official_page_read | 2026-10-10 | 태화강을 끼고 조성한 주제정원; 십리대숲과 강변 산책 경관
### kr-ulsan-ganjeolgot / 간절곶
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=199595 | VISITKOREA — Ganjeolgot Cape | official_page_read | 2026-10-10 | 바다 앞 잔디 공원과 등대; 대형 소망우체통과 간절곶 표석
### kr-ulsan-ulsan-museum / 울산박물관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=80706 | VISITKOREA — Ulsan Museum | official_page_read | 2026-10-10 | 선사에서 근현대로 이어지는 역사관; 산업도시 울산을 설명하는 산업사관; 어린이 체험 공간
### kr-ulsan-oegosan-onggi / 외고산옹기마을
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=86347 | VISITKOREA — Oegosan Onggi Village | official_page_read | 2026-10-10 | 마을의 다양한 옹기와 공방 경관; 울산옹기박물관의 대형 옹기; 옹기아카데미·문화공원
### kr-busan-haedong-yonggungsa / 해동용궁사
- https://english.visitkorea.or.kr/svc/contents/infoBscView.do?menuSn=508&vcontsId=177329 | VISITKOREA — My Name Filming Location Tour | official_page_read | 2026-10-10 | 바다 절벽 위 사찰 경관; 입구의 십이지상; 대나무 사이로 이어지는 계단
### kr-busan-f1963 / F1963
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=187060 | VISITKOREA — F1963 | official_page_read | 2026-10-10 | 옛 와이어 공장 골조를 살린 재생 건축; 전시장·공연장·예술도서관; 외부 산책 공간
### kr-busan-ahopsan-forest / 아홉산숲
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=112679 | VISITKOREA — Ahopsan Forest | official_page_read | 2026-10-10 | 맹종죽 대나무숲; 소나무·편백·삼나무 등이 섞인 숲길
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?dataSetId=68&menuSn=862&vcontsId=215227 | VISITKOREA — Busan travel article | official_page_read | 2026-10-10 | 아홉산숲의 맹종죽 숲과 입구 소나무를 본문에서 확인.
### kr-busan-huinnyeoul-village / 흰여울문화마을
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=182513 | VISITKOREA — Huinnyeoul Culture Street, Busan | official_page_read | 2026-10-10 | 바다 절벽 위 주택과 골목; 절영해안산책로로 내려가는 계단; 흰여울해안터널
### kr-busan-kangkangee-village / 깡깡이예술마을
- https://english.visitkorea.or.kr/svc/contents/infoBscView.do?menuSn=508&vcontsId=177329 | VISITKOREA — My Name Filming Location Tour | official_page_read | 2026-10-10 | 수리조선소와 항구 작업 풍경; 배 표면을 두드리던 작업 소리에서 이어진 마을 이야기
### kr-jeju-stone-park / 제주돌문화공원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=76736 | VISITKOREA — Jeju Stone Park | official_page_read | 2026-10-10 | 설문대할망·오백장군 설화를 풀어낸 돌 전시; 제주돌박물관과 야외 돌문화 전시; 전통 제주 주거 공간
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?dataSetId=249&menuSn=923&vcontsId=247515 | VISITKOREA — Jeju Stone Park | official_page_read | 2026-10-10 | 돌박물관과 초가 전통마을 구역을 본문에서 확인.
### kr-jeju-seongeup-village / 성읍민속마을
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110748 | VISITKOREA — Seongeup Folk Village | official_page_read | 2026-10-10 | 제주의 옛 민가가 남은 생활 마을; 민요·공예·음식·방언으로 이어지는 생활문화
### kr-jeju-haenyeo-museum / 제주해녀박물관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=103315 | VISITKOREA — Jeju Haenyeo Museum | official_page_read | 2026-10-10 | 해녀가 기증한 생활·작업 자료; 해녀 집을 재현한 전시; 반농반어 생활과 영등굿 등 공동체 문화
### kr-jeju-sanbangsan / 산방산
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=94909 | VISITKOREA — Sanbangsan Mountain (Jeju) | official_page_read | 2026-10-10 | 남서부 해안 위로 솟은 산방산 암체; 산방굴사와 불상; 봄 들판을 배경으로 한 산 경관
### kr-jeju-yongmeori-coast / 용머리해안
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110862 | VISITKOREA — Yongmeorihaean Coast | official_page_read | 2026-10-10 | 파도와 침식이 만든 층상 해안 절벽; 해안을 따라 걷는 암반 길; 진입로의 하멜 기념물
### kr-jeju-bijarim / 비자림
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111245 | VISITKOREA — Bijarim Forest | official_page_read | 2026-10-10 | 오래된 비자나무 군락; 굵은 줄기와 넓게 펼쳐진 수관의 숲 경관
### kr-jeju-43-peace-park / 제주4·3평화공원·평화기념관
- https://jeju43peace.or.kr/ | 제주4·3평화재단 — 공원·기념관 안내 | official_page_read | 2026-10-10 | 4·3 희생자를 기억하는 추모 공원; 사건의 원인·전개·결과와 진상규명 과정을 다루는 기념관
### kr-jeju-geum-oreum / 금오름
- https://english.visitkorea.or.kr/svc/contents/bbsHtmlView.do?dataSetId=70&menuSn=862&vcontsId=200970 | VISITKOREA — Into the mysterious volcanic island of Jeju | official_page_read | 2026-10-10 | 정상 분화구의 형태와 물이 고이는 지형; 주변 오름·바다·한라산 방향 조망
### kr-jeju-hwansang-forest / 환상숲곶자왈공원
- https://english.visitkorea.or.kr/svc/contents/bbsHtmlView.do?dataSetId=70&menuSn=862&vcontsId=200970 | VISITKOREA — Into the mysterious volcanic island of Jeju | official_page_read | 2026-10-10 | 용암 지형에 자리 잡은 숲; 양치식물과 큰 나무 뿌리가 얽힌 생태 경관
### kr-jeju-eco-land / 에코랜드 테마파크
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?dataSetId=249&menuSn=923&vcontsId=247515 | VISITKOREA — Gyorae Natural Recreation Forest, Nearby Attractions | official_page_read | 2026-10-10 | 곶자왈을 지나는 증기기관차 형태의 전기열차; 호숫가·목초지 등 역별 주제 공간
### kr-gyeongbuk-dosan-seowon / 도산서원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111174 | VISITKOREA — Dosanseowon Confucian Academy | official_page_read | 2026-10-10 | 이황이 가르치던 도산서당; 사후에 조성한 도산서원 공간; 전교당 등 강학 건축
### kr-gyeongbuk-sosu-seowon / 영주 소수서원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111103 | VISITKOREA — Sosuseowon Confucian Academy | official_page_read | 2026-10-10 | 소백산 아래 자리한 사액서원; 직방재·일신재의 학습 공간
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=172555 | VISITKOREA — Cultural Heritage Sites | official_page_read | 2026-10-10 | 소수서원의 직방재·일신재, 병산서원의 배치와 강변 환경을 본문에서 확인.
### kr-gyeongbuk-byeongsan-seowon / 병산서원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=107434 | VISITKOREA — Byeongsanseowon Confucian Academy | official_page_read | 2026-10-10 | 강학당·사당·기숙 공간을 갖춘 서원; 낙동강과 뒷산이 어우러진 배치
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=172555 | VISITKOREA — Cultural Heritage Sites | official_page_read | 2026-10-10 | 소수서원의 직방재·일신재, 병산서원의 배치와 강변 환경을 본문에서 확인.
### kr-gyeongbuk-baekdudaegan-arboretum / 국립백두대간수목원
- https://koagi.or.kr/bdna/index.do | 국립백두대간수목원 — 공식 누리집 | official_page_read | 2026-10-10 | 백두대간·고산 식물을 다루는 주제 전시원; 호랑이숲
- https://english.visitkorea.or.kr/svc/contents/infoHtmlView.do?menuSn=177&vcontsId=145437 | VISITKOREA — 100 Must-Visit Tourist Spots | official_page_read | 2026-10-10 | 봉화 위치와 주제정원 구성 확인. 호랑이 관찰 제한은 운영기관 원문을 우선.
### kr-gyeongbuk-mungyeongsaejae / 문경새재도립공원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111158 | VISITKOREA — Mungyeongsaejae Provincial Park | official_page_read | 2026-10-10 | 주흘관·조곡관·조령관의 세 관문; 관문 사이로 이어지는 역사 옛길
### kr-gyeongbuk-gyeongju-national-museum / 국립경주박물관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=111324 | VISITKOREA — Gyeongju National Museum | official_page_read | 2026-10-10 | 신라역사관의 유물 전시; 신라미술관의 불교·미술 자료; 어린이 교육 공간
### kr-gyeongbuk-jisan-tombs / 고령 지산동 고분군
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=81842 | VISITKOREA — Jisandong Ancient Tombs | official_page_read | 2026-10-10 | 주산 능선·비탈에 분포한 대가야 고분; 크기와 위치가 다른 봉분 경관
### kr-gyeongbuk-juwangsan / 주왕산국립공원
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=111050 | VISITKOREA — Juwangsan National Park | official_page_read | 2026-10-10 | 높은 암벽과 깊은 계곡; 계곡을 따라 만나는 폭포; 대전사 주변 산악 경관
### kr-gyeongbuk-bongjeongsa / 안동 봉정사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111148 | VISITKOREA — Bongjeongsa Temple | official_page_read | 2026-10-10 | 오래된 목조건축 극락전; 극락전 중수 기록이 전하는 사찰 건축사
### kr-gyeongbuk-seongnyugul / 울진 성류굴
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=90549 | VISITKOREA — Seongnyugul Cave | official_page_read | 2026-10-10 | 종유석·석순·석주; 휘어진 석주와 물에 잠긴 석순의 지질 흔적
### kr-gyeongnam-jinjuseong / 진주성
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=75199 | VISITKOREA — Jinjuseong Fortress | official_page_read | 2026-10-10 | 남강을 내려다보는 성곽; 촉석루와 승전 기념물; 성 안 국립진주박물관
### kr-gyeongnam-haeinsa / 합천 해인사
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=111156 | VISITKOREA — Hapcheon Haeinsa Temple | official_page_read | 2026-10-10 | 팔만대장경을 보관하는 장경판전; 산사 건축과 불교 문화유산
### kr-gyeongnam-tongdosa / 양산 통도사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110668 | VISITKOREA — Tongdosa Temple | official_page_read | 2026-10-10 | 대웅전과 불교 유산; 성보박물관의 불교 문화 전시
### kr-gyeongnam-upo-wetland / 창녕 우포늪
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=110738 | VISITKOREA — Changnyeong Upo Wetland | official_page_read | 2026-10-10 | 자연 습지의 물·식생 경관; 생태관의 우포 사계절·생물 전시
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=96983 | VISITKOREA — Upo Wetland Eco Center | official_page_read | 2026-10-10 | 우포의 사계절·생물 등을 모형과 영상으로 설명하는 전시를 확인.
### kr-gyeongnam-hwangmaesan / 황매산군립공원
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=79930 | VISITKOREA — Hwangmaesan County Park | official_page_read | 2026-10-10 | 바위산과 소나무·철쭉 경관; 맑은 날의 합천호·주변 산 조망
### kr-gyeongnam-gimhae-national-museum / 국립김해박물관
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=95722 | VISITKOREA — Gimhae National Museum | official_page_read | 2026-10-10 | 변한과 가야의 문화유산 전시; 철광석·숯을 상징하는 검은 벽돌 외관; 구지봉 아래 위치
### kr-gyeongnam-sangjogam / 고성 상족암군립공원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=104806 | VISITKOREA — Sangjogam County Park | official_page_read | 2026-10-10 | 해안 암반의 공룡 발자국; 층을 이룬 절벽과 상다리 모양 해식 지형; 고성공룡박물관의 화석·공룡 모형
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=93691 | VISITKOREA — Goseong Dinosaur Museum | official_page_read | 2026-10-10 | 박물관 화석·모형 전시와 상족암 해안 연결을 확인.
### kr-gyeongnam-marisan-tombs / 함안 말이산 고분군
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=177241 | VISITKOREA — Ancient Tombs in Marisan Mountain, Haman | official_page_read | 2026-10-10 | 아라가야의 고분 경관; 산 위와 비탈에 분포한 크기 다른 봉분
### kr-gyeongnam-ssanggyesa-hadong / 하동 쌍계사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=111834 | VISITKOREA — Hadong Ssanggyesa Temple | official_page_read | 2026-10-10 | 지리산 남쪽 기슭의 사찰 공간; 봄 벚꽃길과 주변 차 재배 경관; 불일폭포 연계 탐방
### kr-gyeongnam-geochang-healing-land / 거창 항노화힐링랜드
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=217128 | VISITKOREA — Geochang Anti-aging Healing Land | official_page_read | 2026-10-10 | 우두산의 Y자형 출렁다리; 무장애 데크 산책로; 견암폭포 주변 자생식물원
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?dataSetId=249&menuSn=923&vcontsId=176245 | VISITKOREA — Geochang Anti-aging Healing Land travel article | official_page_read | 2026-10-10 | Y자 출렁다리 접근과 무장애 데크가 다르며 견암폭포 주변 식물원이 있음을 확인. 과거 운영 정보는 채택하지 않음.
### kr-jeonnam-unjusa / 화순 운주사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110763 | VISITKOREA — Unjusa Temple | official_page_read | 2026-10-10 | 구층석탑; 석조불감; 원형다층석탑
### kr-jeonnam-seonamsa / 순천 선암사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=110583 | VISITKOREA — Seonamsa Temple | official_page_read | 2026-10-10 | 승선교의 아치와 자연 암반; 대웅전 앞 두 삼층석탑; 오래된 나무가 있는 진입 숲길
### kr-jeonnam-naganeupseong / 순천 낙안읍성
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=80266 | VISITKOREA — Naganeupseong Walled Town | official_page_read | 2026-10-10 | 돌 성곽 위에서 보는 초가 지붕; 생활 공간이 남은 마을 골목; 전통공예·음악 체험
### kr-jeonnam-dasan-chodang / 강진 다산초당
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=94338 | VISITKOREA — Dasan Chodang | official_page_read | 2026-10-10 | 정약용의 유배·저술 관련 초당; 천일각에서 보는 강진만; 인근 다산박물관 연계
### kr-jeonnam-wando-arboretum / 완도수목원
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=78533 | VISITKOREA — Wando Arboretum | official_page_read | 2026-10-10 | 상록활엽수 난대림; 종류별 전문소원과 온실; 전망대의 다도해 조망
### kr-jeonnam-seomjingang-train-village / 곡성 섬진강기차마을
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=94313 | VISITKOREA — Seomjingang Train Village | official_page_read | 2026-10-10 | 옛 곡성역 공간; 옛 선로를 달리는 증기기관차형 관광열차; 가정역 방향의 철도 경관
### kr-jeonnam-daeheungsa / 해남 대흥사
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=104832 | VISITKOREA — Daeheungsa Temple | official_page_read | 2026-10-10 | 금당천 양쪽으로 나뉜 사찰 배치; 서산대사 관련 표충사; 초의선사·일지암의 차문화 맥락
### kr-jeonnam-naju-national-museum / 국립나주박물관
- https://english.visitkorea.or.kr/svc/contents/contentsView.do?vcontsId=65851 | VISITKOREA — Naju National Museum | official_page_read | 2026-10-10 | 영산강 유역 출토 유물; 개방형 수장고; 문화재 보존·수장 관련 체험 공간
- https://naju.museum.go.kr/eng/ | Naju National Museum — official home | official_page_read | 2026-10-10 | 박물관 위치와 현재 운영 안내를 확인. KTO와 주말 시간 상충으로 운영값 보류.
### kr-jeonnam-haenam-dinosaur-museum / 해남공룡박물관
- https://english.visitkorea.or.kr/svc/whereToGo/locIntrdn/rgnContentsView.do?vcontsId=76188 | VISITKOREA — Haenam Uhangri Dinosaur Museum | official_page_read | 2026-10-10 | 우항리 화석산지 관련 공룡 전시; 다이노가든; 조류생태관과 어린이 구역
