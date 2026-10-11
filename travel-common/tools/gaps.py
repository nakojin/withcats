#!/usr/bin/env python3
"""'보완 필요' 작업표를 내보내고, 채운 값을 다시 들여온다.

  gaps.py export <repo_root> [--tier A] [--all]  → travel-common/v2/worksheets/gaps.csv (엑셀용 UTF-8 BOM)
                                              기본은 수집·검증 뒤에도 남은 빈칸만. --all 은 미수집 항목 포함
  gaps.py import <repo_root> <filled.csv>    → 채운 행을 owner_verified claim 으로 반영

작업표 채우는 법: value 에 사실 한 가지를 쓴다. source_url(공식 페이지) 또는 source_type=owner_input(전화·현장 확인 등,
memo 에 방법 기재) 중 하나와 checked_at(YYYY-MM-DD)이 반드시 있어야 한다. 해당 사항이 없으면 value 에 '해당 없음'.
"""
import csv, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2common import CHECKLIST, CHECKLIST_KO, iter_places, save, recompute_checklist

COLS = ['place_id', 'country', 'tier', 'name_ko', 'item', 'item_ko', 'kind', 'reason', 'note',
        'value', 'source_url', 'source_type', 'checked_at', 'memo']
OUT = 'travel-common/v2/worksheets/gaps.csv'


def export(root, tier=None, include_uncollected=False):
    rows = []
    for _, pl in iter_places(root):
        if tier and pl['tier'] != tier:
            continue
        for k in CHECKLIST:
            it = pl['checklist'][k]
            base = {'place_id': pl['id'], 'country': pl['country'], 'tier': pl['tier'], 'name_ko': pl['names']['ko'],
                    'item': k, 'item_ko': CHECKLIST_KO[k]}
            if it['status'] == 'gap' and (include_uncollected or it['gap']['reason'] != 'not_collected'):
                rows.append(dict(base, kind='gap', reason=it['gap']['reason'], note=it['gap'].get('note', '')))
            for g in it.get('partial_gaps', []) or []:
                rows.append(dict(base, kind='partial', reason=g['reason'], note=f"{g.get('detail', '')}: {g['note']}"))
    os.makedirs(os.path.dirname(os.path.join(root, OUT)), exist_ok=True)
    with open(os.path.join(root, OUT), 'w', encoding='utf-8-sig', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, '') for c in COLS})
    print(f'exported {len(rows)} rows -> {OUT}')


def import_(root, path):
    places = {pl['id']: (p, pl) for p, pl in iter_places(root)}
    errors, done = [], 0
    with open(path, encoding='utf-8-sig', newline='') as fh:
        rows = [r for r in csv.DictReader(fh) if (r.get('value') or '').strip()]
    for n, r in enumerate(rows, 2):
        pid, item, value = r['place_id'], r['item'], r['value'].strip()
        if pid not in places or item not in CHECKLIST:
            errors.append(f'row {n}: unknown place/item {pid}/{item}'); continue
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', r.get('checked_at', '').strip()):
            errors.append(f'row {n}: checked_at YYYY-MM-DD required'); continue
        url, stype = r.get('source_url', '').strip(), (r.get('source_type') or '').strip() or 'official'
        if not url and not (stype == 'owner_input' and r.get('memo', '').strip()):
            errors.append(f'row {n}: source_url, or source_type=owner_input with memo, required'); continue
        p, pl = places[pid]
        if value == '해당 없음':
            pl['checklist'][item] = {'status': 'not_applicable', 'claims': [], 'gap': None,
                                     'note': r.get('memo', ''), 'checked_at': r['checked_at']}
        else:
            cid = f"owner-{r['checked_at']}-{item}-{sum(1 for c in pl['claims'] if c['cid'].startswith('owner-')) + 1}"
            pl['claims'].append({'cid': cid, 'field': item, 'text': value, 'original_text': None, 'value': None,
                                 'verdict': 'owner_verified', 'verify_note': r.get('memo') or None,
                                 'sources': [{'url': url or None, 'type': stype, 'page_updated': None, 'checked_at': r['checked_at']}],
                                 'collector': 'owner', 'verifier': None, 'run': 'owner'})
            if r.get('kind') == 'partial':
                pl['checklist'][item]['partial_gaps'] = [g for g in pl['checklist'][item].get('partial_gaps', [])
                                                         if g.get('detail', '') not in r.get('note', '')]
        recompute_checklist(pl)
        save(p, pl)
        done += 1
    for e in errors:
        print('ERROR', e)
    print(f'imported {done}, rejected {len(errors)}')
    return 1 if errors else 0


if __name__ == '__main__':
    mode, root = sys.argv[1], sys.argv[2]
    if mode == 'export':
        export(root, sys.argv[sys.argv.index('--tier') + 1] if '--tier' in sys.argv else None, '--all' in sys.argv)
    else:
        sys.exit(import_(root, sys.argv[3]))
