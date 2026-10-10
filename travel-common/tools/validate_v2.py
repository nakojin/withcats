#!/usr/bin/env python3
"""공통 스키마 v2 검증기 (표준 라이브러리만 사용).

사용:
  validate_v2.py coords  <repo_root>            # coordinates/*.json 이 catalog 와 맞는지
  validate_v2.py places  <places.json> [--today YYYY-MM-DD]   # v2 장소 레코드 배열 검사
종료 코드: 오류가 있으면 1, 경고만 있으면 0.
"""
import json, sys, datetime, collections

BBOX = {'kr': (32.5, 39.5, 123.5, 132.5), 'jp': (24.0, 46.0, 122.0, 146.5), 'cn': (17.5, 54.0, 73.0, 135.5)}
OPS_KEYS = ('hours', 'fees', 'reservation', 'closed_days', 'payment')
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


def ops_item(path, o, sources, err):
    if not isinstance(o, dict) or o.get('status') not in STATUS:
        err.append(f'{path}: status must be one of {sorted(STATUS)}')
        return
    st, val = o['status'], o.get('value')
    if st == 'confirmed':
        if not val:
            err.append(f'{path}: confirmed requires a value')
        key = path.split('.')[-1]
        if not any(key in (s.get('supports') or []) for s in sources):
            err.append(f'{path}: confirmed but no source lists "{key}" in supports')
        if not o.get('checked_at'):
            err.append(f'{path}: confirmed requires checked_at')
    elif st == 'unconfirmed':
        if val is not None:
            err.append(f'{path}: unconfirmed must have value null')
        if not o.get('note'):
            err.append(f'{path}: unconfirmed requires a note explaining why')


def places(path, today):
    err, warn = [], []
    with open(path, encoding='utf-8') as fh:
        d = json.load(fh)
    d = d if isinstance(d, list) else d.get('places', [])
    ids = [p.get('id') for p in d]
    if len(ids) != len(set(ids)):
        err.append('duplicate ids')
    for p in d:
        pid = p.get('id', '?')
        for k in ('id', 'country', 'admin_region', 'city', 'names', 'category', 'coord', 'summary', 'description',
                  'highlights', 'ops', 'sources', 'quality'):
            if p.get(k) in (None, '', [], {}):
                err.append(f'{pid}: missing {k}')
        if p.get('country') not in BBOX:
            err.append(f'{pid}: country must be kr/jp/cn')
        c = p.get('coord') or {}
        if c:
            lat0, lat1, lng0, lng1 = BBOX.get(p.get('country'), (-90, 90, -180, 180))
            if not (lat0 <= c.get('lat', -999) <= lat1 and lng0 <= c.get('lng', -999) <= lng1):
                err.append(f'{pid}: coord outside country bounding box')
            if c.get('confidence') not in CONF - {'none'}:
                err.append(f'{pid}: coord.confidence must be high/medium/low')
        src = p.get('sources') or []
        for s in src:
            if not s.get('url') or not s.get('checked_at'):
                err.append(f'{pid}: source needs url and checked_at')
        for k in OPS_KEYS:
            ops_item(f'{pid}.ops.{k}', (p.get('ops') or {}).get(k), src, err)
        if p.get('recommended_duration_min') is None and not p.get('duration_note'):
            warn.append(f'{pid}: recommended_duration_min null without duration_note')
        tier = (p.get('quality') or {}).get('depth_tier')
        if tier == 'A':
            if len(p.get('description') or '') < 300:
                err.append(f'{pid}: tier A needs description >= 300 chars')
            if len(p.get('highlights') or []) < 4:
                err.append(f'{pid}: tier A needs >= 4 highlights')
            if p.get('recommended_duration_min') is None or not p.get('how_to_get_there'):
                err.append(f'{pid}: tier A needs duration and how_to_get_there')
            if c.get('confidence') not in ('high', 'medium'):
                err.append(f'{pid}: tier A needs coord confidence high/medium')
            for k in ('hours', 'fees'):
                if ((p.get('ops') or {}).get(k) or {}).get('status') == 'unconfirmed':
                    err.append(f'{pid}: tier A needs ops.{k} confirmed or not_applicable')
        lv = (p.get('quality') or {}).get('last_verified')
        if lv and today:
            age = (datetime.date.fromisoformat(today) - datetime.date.fromisoformat(lv)).days
            if age > 90:
                warn.append(f'{pid}: last_verified {age} days ago (> 90)')
    return err, warn


if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'coords':
        e, w, s = coords(sys.argv[2])
        print('coordinate confidence by country:', s)
    elif mode == 'places':
        today = sys.argv[sys.argv.index('--today') + 1] if '--today' in sys.argv else None
        e, w = places(sys.argv[2], today)
    else:
        sys.exit(__doc__)
    for m in w:
        print('WARN ', m)
    for m in e:
        print('ERROR', m)
    print(f'{len(e)} errors, {len(w)} warnings')
    sys.exit(1 if e else 0)
