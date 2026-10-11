#!/usr/bin/env python3
"""공통 스키마 v2 검증기 (표준 라이브러리만 사용).

사용:
  validate_v2.py coords  <repo_root>            # coordinates/*.json 이 catalog 와 맞는지
  validate_v2.py store   <repo_root> [--today YYYY-MM-DD]     # v2 장소 파일 전체 검사
종료 코드: 오류가 있으면 1, 경고만 있으면 0.
"""
import json, os, sys, datetime, collections

BBOX = {'kr': (32.5, 39.5, 123.5, 132.5), 'jp': (24.0, 46.0, 122.0, 146.5), 'cn': (17.5, 54.0, 73.0, 135.5)}
STATUS = {'confirmed', 'unconfirmed', 'not_applicable'}
CONF = {'high', 'medium', 'low', 'none'}


def coords(root):
    err, warn = [], []
    def jload(p):
        with open(p, encoding='utf-8') as fh:
            return json.load(fh)
    cat_ids = {
        'kr': [r['id'] for r in jload(f'{root}/korea-travel/catalog.json')['records']],
        'jp': [r['id'] for r in jload(f'{root}/japan-travel/catalog.json')['items']],
        'cn': [r['id'] for r in jload(f'{root}/china-travel/catalog.json')['items']],
    }
    summary = {}
    for cc, ids in cat_ids.items():
        try:
            d = jload(f'{root}/travel-common/coordinates/{cc}.json')['items']
        except FileNotFoundError:
            err.append(f'{cc}: coordinates file missing')
            continue
        got = [x['id'] for x in d]
        if len(got) != len(set(got)):
            err.append(f'{cc}: duplicate ids')
        miss, extra = set(ids) - set(got), set(got) - set(ids)
        if miss:
            err.append(f'{cc}: {len(miss)} catalog ids without coordinates, e.g. {sorted(miss)[:3]}')
        if extra:
            err.append(f'{cc}: {len(extra)} ids not in catalog')
        lat0, lat1, lng0, lng1 = BBOX[cc]
        for x in d:
            c = x.get('confidence')
            if c not in CONF:
                err.append(f"{x['id']}: bad confidence {c!r}")
            if c != 'none':
                if not (lat0 <= x.get('lat', -999) <= lat1 and lng0 <= x.get('lng', -999) <= lng1):
                    err.append(f"{x['id']}: coordinate outside {cc} bounding box")
                if not x.get('geo_source'):
                    err.append(f"{x['id']}: missing geo_source")
        # 같은 좌표를 공유하는 서로 다른 장소는 오매칭 가능성
        pos = collections.defaultdict(list)
        for x in d:
            if x.get('lat') is not None:
                pos[(round(x['lat'], 4), round(x['lng'], 4))].append(x['id'])
        dup = [v for v in pos.values() if len(v) > 1]
        if dup:
            warn.append(f'{cc}: {len(dup)} coordinate collisions, e.g. {dup[:2]}')
        summary[cc] = dict(collections.Counter(x.get('confidence') for x in d))
    return err, warn, summary


def store(root, today=None):
    """v2 장소 파일 전체를 검사한다."""
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from v2common import (CHECKLIST, FIELD_TO_ITEM, PUBLISHABLE, VERDICTS, SOURCE_TYPES, GAP_REASONS, iter_places)
    err, warn = [], []
    seen = set()
    for path, p in iter_places(root):
        pid = p.get('id', path)
        if pid in seen:
            err.append(f'{pid}: duplicate id')
        seen.add(pid)
        for k in ('id', 'country', 'tier', 'status', 'names', 'admin_region', 'checklist', 'claims', 'meta'):
            if k not in p:
                err.append(f'{pid}: missing {k}')
        if p.get('country') not in BBOX:
            err.append(f'{pid}: bad country')
            continue
        c = p.get('coord')
        if c:
            lat0, lat1, lng0, lng1 = BBOX[p['country']]
            if not (lat0 <= c.get('lat', -999) <= lat1 and lng0 <= c.get('lng', -999) <= lng1):
                err.append(f'{pid}: coord outside country bounding box')
        cids = [x['cid'] for x in p['claims']]
        if len(cids) != len(set(cids)):
            err.append(f'{pid}: duplicate claim ids')
        pub = {}
        for x in p['claims']:
            if x.get('verdict') not in VERDICTS:
                err.append(f"{pid}.{x['cid']}: bad verdict {x.get('verdict')!r}")
            if x['verdict'] in PUBLISHABLE:
                pub[x['cid']] = x
                if not x.get('text'):
                    err.append(f"{pid}.{x['cid']}: publishable claim without text")
                if not x.get('sources'):
                    err.append(f"{pid}.{x['cid']}: publishable claim without source")
                for s_ in x.get('sources', []):
                    if s_.get('type') not in SOURCE_TYPES:
                        err.append(f"{pid}.{x['cid']}: source type {s_.get('type')!r} not allowed")
                    if not s_.get('checked_at'):
                        err.append(f"{pid}.{x['cid']}: source without checked_at")
                    if not s_.get('url') and s_.get('type') != 'owner_input':
                        err.append(f"{pid}.{x['cid']}: source without url")
                    if today and s_.get('checked_at'):
                        age = (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(s_['checked_at'])).days
                        if age > 90:
                            warn.append(f"{pid}.{x['cid']}: checked {age} days ago (> 90)")
        cl = p['checklist']
        for k in CHECKLIST:
            it = cl.get(k)
            if not it:
                err.append(f'{pid}: checklist missing {k}')
                continue
            if it['status'] == 'filled':
                bad = [c_ for c_ in it['claims'] if c_ not in pub or FIELD_TO_ITEM.get(pub[c_]['field']) != k]
                if not it['claims'] or bad:
                    err.append(f'{pid}: checklist {k} filled but claims invalid {bad}')
            elif it['status'] == 'gap':
                if (it.get('gap') or {}).get('reason') not in GAP_REASONS:
                    err.append(f'{pid}: checklist {k} gap without valid reason')
            elif it['status'] != 'not_applicable':
                err.append(f"{pid}: checklist {k} bad status {it['status']!r}")
        if p['status'] == 'verified':
            if (p.get('content_review') or {}).get('status') != 'ok':
                err.append(f'{pid}: verified but content_review not ok')
            if any(x['verdict'] == 'pending' for x in p['claims']):
                err.append(f'{pid}: verified but has pending claims')
            if any(cl[k]['status'] == 'gap' and cl[k]['gap']['reason'] == 'not_collected' for k in CHECKLIST):
                err.append(f'{pid}: verified but checklist has not_collected items')
    return err, warn


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'coords':
        e, w, s = coords(sys.argv[2])
        print('coordinate confidence by country:', s)
    elif mode == 'store':
        today = sys.argv[sys.argv.index('--today') + 1] if '--today' in sys.argv else None
        e, w = store(sys.argv[2], today)
    else:
        sys.exit(__doc__)
    for m in w:
        print('WARN ', m)
    for m in e:
        print('ERROR', m)
    print(f'{len(e)} errors, {len(w)} warnings')
    sys.exit(1 if e else 0)
