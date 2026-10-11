#!/usr/bin/env python3
"""v2 장소 파일에서 사이트용 공개 데이터와 현황표를 만든다.

  build.py <repo_root>
  → travel-common/v2/published/{kr,jp,cn}.json : 공개 가능한 값만(판정 verified/corrected/outdated/owner_verified)
  → travel-common/v2/STATUS.md                 : 나라·항목별 채움률과 보완 필요 수
v1 의 legacy 본문, pending·suggested·unverifiable claim, 검증자 작업 메모(conflicts)는 공개 데이터에 들어가지 않는다.
"""
import collections, json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2common import COUNTRIES, CHECKLIST, CHECKLIST_KO, FIELD_TO_ITEM, PUBLISHABLE, iter_places

NAME = {'kr': '한국', 'jp': '일본', 'cn': '중국'}


def public_place(pl):
    facts = collections.defaultdict(list)
    for c in pl['claims']:
        if c['verdict'] in PUBLISHABLE:
            facts[c['field']].append({'text': c['text'], 'verdict': c['verdict'],
                                      'owner_input': c['verdict'] == 'owner_verified',
                                      'sources': [{'url': s.get('url'), 'type': s.get('type'), 'checked_at': s.get('checked_at')} for s in c['sources']]})
    guide = {}
    for k in CHECKLIST:
        it = pl['checklist'][k]
        fields = [f for f, item in FIELD_TO_ITEM.items() if item == k]
        guide[k] = {'status': it['status'], 'facts': [x for f in fields for x in facts.get(f, [])],
                    'gap': it.get('gap'), 'partial_gaps': [g['note'] for g in it.get('partial_gaps') or []]}
    content_ok = (pl.get('content_review') or {}).get('status') == 'ok'
    dates = [s.get('checked_at') for c in pl['claims'] if c['verdict'] in PUBLISHABLE for s in c['sources'] if s.get('checked_at')]
    return {'id': pl['id'], 'tier': pl['tier'], 'status': pl['status'], 'names': pl['names'],
            'admin_region': pl['admin_region'], 'city': pl['city'], 'address': pl['address'], 'coord': pl['coord'],
            'summary': pl['summary'] if content_ok else None, 'description': pl['description'] if content_ok else None,
            'highlights': pl['highlights'] if content_ok else [],
            'details': {f: facts[f] for f in ('description', 'highlight', 'tip') if facts.get(f)},
            'guide': guide,
            'last_verified': max(dates) if dates else None}


def main(root):
    out_dir = os.path.join(root, 'travel-common/v2/published')
    os.makedirs(out_dir, exist_ok=True)
    stat = {}
    for cc in COUNTRIES:
        places = [pl for _, pl in iter_places(root, cc)]
        pub = [public_place(pl) for pl in places]
        with open(os.path.join(out_dir, f'{cc}.json'), 'w', encoding='utf-8') as fh:
            json.dump({'country': cc, 'generated_from': 'travel-common/v2/places', 'places': pub}, fh, ensure_ascii=False, indent=1)
            fh.write('\n')
        s = {'places': len(places), 'tier_a': sum(p['tier'] == 'A' for p in places),
             'verified': sum(p['status'] == 'verified' for p in places),
             'with_claims': sum(bool(p['claims']) for p in places), 'coord': sum(bool(p['coord']) for p in places),
             'items': {k: collections.Counter(p['checklist'][k]['status'] for p in places if p['claims']) for k in CHECKLIST},
             'processed': sum(bool(p['meta']['runs']) for p in places),
             'gap_reasons': collections.Counter(p['checklist'][k]['gap']['reason'] for p in places if p['meta']['runs']
                                                for k in CHECKLIST if p['checklist'][k]['status'] == 'gap')}
        stat[cc] = s
    L = ['# v2 자료 현황', '', '`build.py` 가 자동 생성한다. 손으로 고치지 않는다.', '',
         '| 나라 | 장소 | Tier A | 수집 회차 거침 | 사실(claim) 보유 | 검증 완료(공개 가능) | 좌표 |', '|---|---|---|---|---|---|---|']
    for cc, s in stat.items():
        L.append(f"| {NAME[cc]} | {s['places']} | {s['tier_a']} | {s['processed']} | {s['with_claims']} | {s['verified']} | {s['coord']} |")
    L += ['', '## 가이드 필수 항목 채움 (수집·검증을 거친 장소 기준)', '',
          '| 항목 | ' + ' | '.join(NAME[c] for c in COUNTRIES) + ' |', '|---|' + '---|' * len(COUNTRIES)]
    for k in CHECKLIST:
        cells = []
        for cc in COUNTRIES:
            c, n = stat[cc]['items'][k], stat[cc]['with_claims']
            cells.append(f"{c.get('filled', 0)}/{n}" + (f" (해당없음 {c['not_applicable']})" if c.get('not_applicable') else '') if n else '-')
        L.append(f'| {CHECKLIST_KO[k]} | ' + ' | '.join(cells) + ' |')
    L += ['', '## 보완 필요 사유 (수집 회차를 거친 장소의 빈 항목 수)', '', '| 사유 | ' + ' | '.join(NAME[c] for c in COUNTRIES) + ' |', '|---|' + '---|' * len(COUNTRIES)]
    for r in ('not_in_official_source', 'official_unreachable', 'conflicting_sources', 'not_collected'):
        L.append(f'| {r} | ' + ' | '.join(str(stat[cc]['gap_reasons'].get(r, 0)) for cc in COUNTRIES) + ' |')
    with open(os.path.join(root, 'travel-common/v2/STATUS.md'), 'w', encoding='utf-8') as fh:
        fh.write('\n'.join(L) + '\n')
    print(json.dumps({cc: {k: v for k, v in s.items() if k in ('places', 'with_claims', 'verified', 'coord')} for cc, s in stat.items()}, ensure_ascii=False))


if __name__ == '__main__':
    main(sys.argv[1])
