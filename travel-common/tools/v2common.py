"""v2 저장소 공통 규칙. 모든 도구가 이 정의를 함께 쓴다."""
import json, os

COUNTRIES = ('kr', 'jp', 'cn')
STORE = 'travel-common/v2/places'          # 장소 1곳 = 파일 1개 (travel-common/v2/places/{cc}/{id}.json)

# 가이드 필수 항목(VERIFICATION.md 6절). 운영시간과 휴무는 따로 관리한다.
CHECKLIST = ('location', 'access', 'duration', 'hours', 'closed_days', 'fees',
             'reservation', 'payment', 'language', 'caution')
CHECKLIST_KO = {'location': '위치', 'access': '접근·주차', 'duration': '소요시간', 'hours': '운영시간',
                'closed_days': '휴무', 'fees': '요금', 'reservation': '예약', 'payment': '결제',
                'language': '한국어 지원', 'caution': '주의사항'}
# claim.field → 체크리스트 항목 (description/highlight/tip 은 체크리스트 밖)
FIELD_TO_ITEM = {'location': 'location', 'access': 'access', 'parking': 'access', 'duration': 'duration',
                 'hours': 'hours', 'closed_days': 'closed_days', 'fees': 'fees', 'reservation': 'reservation',
                 'payment': 'payment', 'language': 'language', 'caution': 'caution'}
CONTENT_FIELDS = ('description', 'highlight', 'tip')

# 공개 가능한 판정. owner_verified 는 운영자가 직접 채운 값(사이트에 별도 표시).
PUBLISHABLE = {'verified', 'corrected', 'outdated', 'owner_verified'}
VERDICTS = PUBLISHABLE | {'unverifiable', 'rejected', 'pending', 'suggested', 'superseded'}
# superseded: 검증자가 '지금은 다르다(outdated)'고 했지만 새 문장을 주지 않은 경우. 옛 문장이므로 공개하지 않는다.
SOURCE_TYPES = {'official', 'government', 'national_tourism', 'operator', 'owner_input'}
GAP_REASONS = {'not_in_official_source', 'official_unreachable', 'conflicting_sources', 'not_collected'}


def path_of(root, cc, pid):
    return os.path.join(root, STORE, cc, f'{pid}.json')


def load(p):
    with open(p, encoding='utf-8') as fh:
        return json.load(fh)


def save(p, obj):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, 'w', encoding='utf-8') as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=1)
        fh.write('\n')


def iter_places(root, cc=None):
    for c in ([cc] if cc else COUNTRIES):
        d = os.path.join(root, STORE, c)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith('.json'):
                p = os.path.join(d, f)
                yield p, load(p)


def empty_checklist():
    return {k: {'status': 'gap', 'claims': [], 'gap': {'reason': 'not_collected', 'note': '아직 수집하지 않음'}}
            for k in CHECKLIST}


def recompute_checklist(place):
    """claims 판정으로 체크리스트 상태를 다시 계산한다. 수동 not_applicable·gap 메모는 유지한다."""
    cl = place['checklist']
    by_item = {k: [] for k in CHECKLIST}
    prev_partial = {k: cl[k].get('partial_gaps') for k in CHECKLIST}
    for c in place['claims']:
        item = FIELD_TO_ITEM.get(c['field'])
        if item and c['verdict'] in PUBLISHABLE:
            by_item[item].append(c['cid'])
    for k in CHECKLIST:
        if by_item[k]:
            cl[k] = {'status': 'filled', 'claims': by_item[k], 'gap': None}
            if prev_partial.get(k):
                cl[k]['partial_gaps'] = prev_partial[k]      # 채운 항목의 빠진 세부는 유지한다
        elif cl[k]['status'] == 'not_applicable':
            pass
        else:
            prev = cl[k].get('gap') or {}
            cl[k] = {'status': 'gap', 'claims': [], 'gap': prev or {'reason': 'not_collected', 'note': '아직 수집하지 않음'}}
    return place
