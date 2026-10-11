#!/usr/bin/env python3
"""수집(collected) + 독립 검증(verified) 결과를 v2 장소 파일에 병합한다.

사용: merge_run.py <repo_root> <run_id> <date> <collected.json> <verified.json> [content_fix.json]
- 판정이 corrected/outdated 면 검증자 문장으로 바꾸고 원문은 original_text 에 남긴다.
- 판정이 없는 claim 은 pending(비공개). 검증자가 새로 찾은 사실은 suggested(비공개, 다음 회차에서 수집·검증).
- 수집자의 unconfirmed 는 체크리스트 gap(또는 이미 채운 항목의 partial_gaps)으로 옮긴다.
- 설명·하이라이트에 근거 없는 내용이 지적되면 content_review=needs_fix 로 두고 공개하지 않는다.
  content_fix.json({key: [[old, new], ...]}) 로 고친 뒤에만 ok 가 된다.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2common import (COUNTRIES, CHECKLIST, path_of, load, save, empty_checklist, recompute_checklist)

UNREACH = re.compile(r'\b(503|403)\b|\(000|000/503|접속 불가|열리지 않|열 수 없|연결 실패|unreachable', re.I)
CONFLICT = re.compile(r'conflict|충돌|서로 다르|와 다름|과 다름', re.I)
COORD_HANDLED = {'location.coordinates'}      # 좌표는 지오코딩 단계에서 따로 처리


def find_place(root, key):
    if key.startswith('new:'):
        pid = key[4:]
        return pid.split('-')[0], pid, True
    for cc in COUNTRIES:
        if os.path.exists(path_of(root, cc, key)):
            return cc, key, False
    raise SystemExit(f'unknown key {key}')


def skeleton(cc, pid, col, date):
    return {'id': pid, 'country': cc, 'tier': 'A', 'status': 'draft',
            'names': {'ko': col['name_ko'], 'local': col['name_local']}, 'admin_region': col.get('admin_region'),
            'former_region': None, 'city': None, 'address': None, 'coord': None, 'coord_note': '좌표 수집 대기',
            'summary': None, 'description': None, 'highlights': [], 'checklist': empty_checklist(),
            'claims': [], 'conflicts': [], 'legacy': None, 'meta': {'created': date, 'updated': date, 'runs': []}}


def main(root, run, date, col_path, ver_path, fix_path=None):
    cols = load(col_path)
    vers = {p['key']: p for p in load(ver_path)['places']}
    fixes = load(fix_path) if fix_path else {}
    for col in cols:
        cc, pid, is_new = find_place(root, col['key'])
        p = path_of(root, cc, pid)
        place = load(p) if os.path.exists(p) else skeleton(cc, pid, col, date)
        ver = vers.get(col['key'])
        verdicts = {v['cid']: v for v in (ver or {}).get('verdicts', [])}
        place['claims'] = [c for c in place['claims'] if not c['cid'].startswith(run + '-')]   # 같은 회차 재병합 대비
        place['coord_candidates'] = [x for x in place.get('coord_candidates', []) if x.get('run') != run]
        for c in col['claims']:
            v = verdicts.get(c['cid'])
            verdict = v['verdict'] if v else 'pending'
            text = c['text']
            orig = None
            if v and verdict in ('corrected', 'outdated') and v.get('corrected_text'):
                orig, text = text, v['corrected_text']
            elif verdict in ('corrected', 'outdated'):
                verdict = 'superseded'                      # 고친 문장이 없으면 옛 문장을 공개하지 않는다
            # 좌표는 claim 이 아니라 좌표 후보로 따로 보관(지도 대조 후 coord 에 반영)
            if c['field'] == 'location' and re.fullmatch(r'\s*-?\d+\.\d+\s*,\s*-?\d+\.\d+\s*', str(c.get('value') or '')):
                lat, lng = [float(x) for x in c['value'].split(',')]
                place['coord_candidates'].append({'lat': lat, 'lng': lng, 'source': c['sources'][0]['url'] if c['sources'] else None,
                                                  'verify_note': (v or {}).get('note'), 'run': run})
                continue
            place['claims'].append({
                'cid': f"{run}-{c['cid']}", 'field': c['field'], 'text': text, 'original_text': orig,
                'value': c.get('value'), 'verdict': verdict, 'verify_note': (v or {}).get('note'),
                'sources': [dict(s, checked_at=date) for s in c['sources']],
                'collector': 'sonnet-5.5', 'verifier': 'opus-5.5' if v else None, 'run': run})
        for i, s in enumerate((ver or {}).get('suggested_claims', []), 1):
            place['claims'].append({
                'cid': f'{run}-s{i}', 'field': s['field'], 'text': s['text'], 'original_text': None, 'value': None,
                'verdict': 'suggested', 'verify_note': '검증자가 공식 페이지에서 발견. 다음 회차에서 독립 수집·검증 필요',
                'sources': [{'url': s['url'], 'type': 'official', 'page_updated': None, 'checked_at': date}],
                'collector': None, 'verifier': 'opus-5.5', 'run': run})
        place['conflicts'] = [x for x in place['conflicts'] if x.get('run') != run] + \
                             [{'run': run, 'text': t} for t in (ver or {}).get('conflicts', [])]
        # unconfirmed → gap
        place['open_questions'] = [q for q in place.get('open_questions', []) if q.get('run') != run]
        pending_gaps = {}
        for u in col.get('unconfirmed', []):
            if u['field'] in COORD_HANDLED:
                continue
            item = u['field'].split('.')[0]
            if CONFLICT.search(u['field'] + ' ' + u['reason']):
                reason = 'conflicting_sources'
            elif UNREACH.search(u['reason']):
                reason = 'official_unreachable'
            else:
                reason = 'not_in_official_source'
            if item == 'all':
                for k in CHECKLIST:
                    pending_gaps.setdefault(k, []).append({'reason': reason, 'note': u['reason'], 'run': run})
            elif item in CHECKLIST:
                pending_gaps.setdefault(item, []).append({'reason': reason, 'note': u['reason'], 'detail': u['field'], 'run': run})
            else:
                place['open_questions'].append({'topic': u['field'], 'note': u['reason'], 'run': run})
        recompute_checklist(place)
        for k, gaps in pending_gaps.items():
            item = place['checklist'][k]
            if item['status'] == 'filled':
                item['partial_gaps'] = gaps            # 일부는 채웠지만 빠진 세부가 있음
            else:
                item['gap'] = {'reason': gaps[0]['reason'], 'note': ' / '.join(g['note'] for g in gaps)}
        # 본문
        if col.get('description'):
            unsupported = (ver or {}).get('unsupported_in_description', []) + (ver or {}).get('unsupported_in_highlights', [])
            desc, hl = col['description'], list(col['highlights'])
            for old, new in fixes.get(col['key'], []):
                desc = desc.replace(old, new)
                hl = [h.replace(old, new) for h in hl]
            # 수정·비공개된 claim 의 옛 표현(숫자+뒤 6글자)이 본문에 그대로 남아 있으면 공개를 막는다
            body = re.sub(r'\s', '', desc + ' '.join(hl))
            for c in place['claims']:
                if c['run'] != run or c['verdict'] not in ('corrected', 'outdated', 'superseded', 'unverifiable', 'rejected'):
                    continue
                old = re.sub(r'\s', '', c.get('original_text') or c['text'])
                new_t = re.sub(r'\s', '', c['text']) if c['verdict'] in ('corrected', 'outdated') else ''
                stale = sorted({old[m.start():m.end() + 6] for m in re.finditer(r'\d[\d,.:~]*', old)
                                if old[m.start():m.end() + 6] in body and old[m.start():m.end() + 6] not in new_t
                                and len(old[m.start():m.end() + 6]) >= 5})
                if stale:
                    unsupported.append(f"{c['cid']} 판정({c['verdict']}) 전 수치 {stale} 가 본문에 남음")
            fixed = col['key'] in fixes
            # 요약문은 검증자가 보지 않으므로 쓰지 않고, 검토된 설명문의 첫 문장을 요약으로 쓴다.
            first = re.split(r'(?<=다\.)\s', desc, maxsplit=1)[0]
            place['summary'], place['description'], place['highlights'] = first, desc, hl
            stale_left = [u for u in unsupported if '수치' in u and '본문에 남음' in u]
            place['content_review'] = {'status': 'ok' if ((not unsupported or fixed) and not stale_left) else 'needs_fix',
                                       'unsupported': unsupported, 'fixed_by': 'content_fix' if fixed else None,
                                       'basis': '수집 claim 으로만 작성, 검증자 검토', 'run': run}
        if col.get('address'):
            place['address'] = col['address']
        place['meta']['updated'] = date
        place['meta']['runs'] = [r for r in place['meta']['runs'] if r['run'] != run] + [{
            'run': run, 'date': date, 'collector': 'sonnet-5.5', 'verifier': 'opus-5.5' if ver else None,
            'claims': len(col['claims']), 'verdicts': {k: sum(1 for c in place['claims'] if c['run'] == run and c['verdict'] == k)
                                                       for k in ('verified', 'corrected', 'outdated', 'unverifiable', 'rejected', 'pending', 'suggested')}}]
        settled = all(place['checklist'][k]['status'] != 'gap' or place['checklist'][k]['gap']['reason'] != 'not_collected' for k in CHECKLIST)
        no_pending = not any(c['verdict'] == 'pending' for c in place['claims'])
        content_ok = (place.get('content_review') or {}).get('status') == 'ok'
        place['status'] = 'verified' if (settled and no_pending and content_ok) else 'draft'
        save(p, place)
        filled = sum(1 for k in CHECKLIST if place['checklist'][k]['status'] == 'filled')
        print(f"{cc}/{pid}: {'new' if is_new else 'existing'} status={place['status']} checklist {filled}/{len(CHECKLIST)}")


if __name__ == '__main__':
    main(*sys.argv[1:])
