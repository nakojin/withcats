#!/usr/bin/env python3
"""v1 catalog 3개를 v2 장소 파일로 옮긴다.

- v1 의 본문(하이라이트·설명·운영정보)은 검증 전 자료라 `legacy` 에만 보존하고 공개하지 않는다.
- 좌표는 coordinates/{cc}.json 에서 confidence high/medium 만 넣는다.
- Tier 는 tiers/tier_a_draft.json 의 기존 레코드면 A, 나머지 C.
- 이미 claim 이 들어간 파일은 건드리지 않는다(재실행 안전).
사용: convert_v1.py <repo_root>
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from v2common import COUNTRIES, path_of, load, save, empty_checklist

TODAY = '2026-10-11'


def v1_rows(root):
    k = load(f'{root}/korea-travel/catalog.json')['records']
    for r in k:
        yield 'kr', r['id'], {'ko': r['name_ko'], 'local': r['name_ko']}, r['admin_region'], r.get('locality') or '', r, 'korea-travel/catalog.json'
    for r in load(f'{root}/japan-travel/catalog.json')['items']:
        yield 'jp', r['id'], {'ko': r['name_ko'], 'local': r['name_ja']}, r['prefecture'], r['city'], r, 'japan-travel/catalog.json'
    for r in load(f'{root}/china-travel/catalog.json')['items']:
        yield 'cn', r['id'], {'ko': r['name_ko'], 'local': r['name_local']}, r['province'], r['city'], r, 'china-travel/catalog.json'


def main(root):
    coords = {}
    for cc in COUNTRIES:
        for x in load(f'{root}/travel-common/coordinates/{cc}.json')['items']:
            coords[x['id']] = x
    tier_a = {i for e in load(f'{root}/travel-common/tiers/tier_a_draft.json') for i in e['existing_ids']}
    made = kept = 0
    for cc, pid, names, region, city, raw, src in v1_rows(root):
        p = path_of(root, cc, pid)
        if os.path.exists(p) and load(p).get('claims'):
            kept += 1
            continue
        g = coords.get(pid) or {}
        coord = None
        if g.get('confidence') in ('high', 'medium'):
            coord = {k: g[k] for k in ('lat', 'lng', 'geo_type', 'precision', 'geo_source', 'confidence', 'osm')}
        save(p, {
            'id': pid, 'country': cc, 'tier': 'A' if pid in tier_a else 'C', 'status': 'draft',
            'names': names, 'admin_region': region, 'former_region': None, 'city': city, 'address': None,
            'coord': coord, 'coord_note': None if coord else f"좌표 검증 대기 (geocode confidence: {g.get('confidence', 'none')})",
            'summary': None, 'description': None, 'highlights': [],
            'checklist': empty_checklist(), 'claims': [], 'conflicts': [],
            'legacy': {'source': src, 'note': 'v1 자료. 검증 전이므로 공개하지 않는다.', 'record': raw},
            'meta': {'created': TODAY, 'updated': TODAY, 'runs': []},
        })
        made += 1
    print(f'created {made}, kept (already has claims) {kept}')


if __name__ == '__main__':
    main(sys.argv[1])
