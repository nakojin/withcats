#!/usr/bin/env python3
"""3개국 여행 catalog 의 장소에 대표 좌표를 붙이는 스크립트 (OSM Nominatim).

- 입력: korea-travel/catalog.json, japan-travel/catalog.json, china-travel/catalog.json
- 출력: travel-common/coordinates/{kr,jp,cn}.json  (catalog 는 수정하지 않는다)
- Nominatim 사용 정책: 초당 1회 이하, 식별 가능한 User-Agent, 응답 캐시로 재요청 방지
- 좌표는 후보 점수화 후 선택하며 confidence(high/medium/low/none)와 flags 를 남긴다.
  low/none 은 사람이 검토해야 한다. OSM 데이터는 ODbL 이므로 출처를 표시해야 한다.
"""
import argparse, json, os, re, sys, time, urllib.parse, urllib.request

UA = 'withcats-travel-data/1.0 (data-quality pass; contact via repository owner)'
BAD_CLASS_TYPE = {('highway', 'bus_stop'), ('railway', 'station'), ('railway', 'halt'), ('railway', 'tram_stop'),
                  ('public_transport', 'platform'), ('public_transport', 'stop_position'), ('public_transport', 'station'),
                  ('amenity', 'parking'), ('amenity', 'bus_station'), ('highway', 'platform')}
GOOD_CLASS = {'tourism', 'historic', 'leisure', 'natural', 'boundary', 'man_made', 'amenity', 'building', 'waterway', 'place', 'landuse'}
AREA_CLASS = {'boundary', 'natural', 'landuse', 'leisure'}


def core(name):
    """행정구역명에서 접미사를 떼어 부분일치 비교용 핵심어를 만든다."""
    n = re.sub(r'\(.*?\)', '', name or '').strip()
    for suf in ('특별자치도', '특별자치시', '특별시', '광역시', '자치구', '자치주', '특별행정구'):
        if n.endswith(suf):
            n = n[: -len(suf)]
            break
    else:
        n = re.sub(r'(도|부|현|성|시|군|구)$', '', n) if len(n) > 2 else n
    return n


def load(root):
    out = []
    k = json.load(open(f'{root}/korea-travel/catalog.json', encoding='utf-8'))['records']
    for r in k:
        out.append({'id': r['id'], 'cc': 'kr', 'q': r['name_ko'], 'q2': f"{r['name_ko']} {(r.get('locality') or '').split(';')[0]}",
                    'region': r['admin_region'], 'city': '',
                    'sgg': re.findall(r'[가-힣]{1,6}(?:시|군|구)', (r.get('locality') or '').split(';')[0])})
    j = json.load(open(f'{root}/japan-travel/catalog.json', encoding='utf-8'))['items']
    for r in j:
        out.append({'id': r['id'], 'cc': 'jp', 'q': r['name_ja'], 'q2': f"{r['name_ja']} {r['city']}", 'region': r['prefecture'], 'city': r['city']})
    c = json.load(open(f'{root}/china-travel/catalog.json', encoding='utf-8'))['items']
    for r in c:
        out.append({'id': r['id'], 'cc': 'cn', 'q': r['name_local'], 'q2': f"{r['name_local']} {r['city']}", 'region': r['province'], 'city': r['city']})
    return out


def search(q, cc, cache, path, delay):
    key = f'{cc}|{q}'
    if key in cache:
        return cache[key]
    params = urllib.parse.urlencode({'q': q, 'format': 'jsonv2', 'limit': 5, 'accept-language': 'ko',
                                     'countrycodes': cc, 'addressdetails': 0})
    req = urllib.request.Request('https://nominatim.openstreetmap.org/search?' + params, headers={'User-Agent': UA})
    for attempt in range(3):
        try:
            data = json.load(urllib.request.urlopen(req, timeout=40))
            break
        except Exception as e:  # 429/네트워크 오류는 대기 후 재시도
            time.sleep(8 * (attempt + 1))
            data = None
    cache[key] = data if data is not None else []
    if data is None:
        cache[key + '|error'] = True
    json.dump(cache, open(path, 'w', encoding='utf-8'), ensure_ascii=False)
    time.sleep(delay)
    return cache[key]


# 관광지 본체가 아닌 부속 시설(상점·식당·안내소·숙박)은 감점한다.
NON_POI_CLASS = {'highway', 'railway', 'route', 'power', 'barrier'}      # 관광지가 될 수 없는 시설
SOFT_BAD_CLASS = {'shop', 'office', 'craft', 'information'} | NON_POI_CLASS
SOFT_BAD_TYPE = {'restaurant', 'cafe', 'fast_food', 'bar', 'pub', 'toilets', 'information', 'hotel', 'hostel',
                 'guest_house', 'motel', 'apartment', 'ticket', 'gift', 'checkpoint'}
# OSM 이 행정구역 개편 후 이름(전남광주통합특별시 등)으로 표기하는 경우를 인정하는 별칭
ALIAS = {'전라남도': ['전남', '전남광주'], '광주광역시': ['광주', '전남광주'], '전북특별자치도': ['전북', '전라북'],
         '경상북도': ['경북'], '경상남도': ['경남'], '충청남도': ['충남'], '충청북도': ['충북']}


def region_hits(region, disp):
    names = [core(region), region] + ALIAS.get(region, [])
    return any(n and n in disp for n in names)


def norm(t):
    return re.sub(r'[\s·・\-\(\)（）]', '', t or '')


def score(c, rec):
    cls, typ = c.get('category'), c.get('type')
    if (cls, typ) in BAD_CLASS_TYPE:
        return -10, 'transport_or_parking'
    s = 0
    if cls in GOOD_CLASS:
        s += 2
    if cls in SOFT_BAD_CLASS or typ in SOFT_BAD_TYPE:
        s -= 4
    disp = c.get('display_name', '')
    if region_hits(rec['region'], disp):
        s += 4
    city = core(rec['city']) if rec['city'] else ''
    if city and city in disp:
        s += 2
    first = norm((c.get('name') or disp.split(',')[0]))
    q = norm(rec['q'])
    if q and first == q:
        s += 4
    elif q and (q in first or first in q) and len(first) >= 2:
        s += 2
    s += min(float(c.get('importance') or 0), 1.0)
    return s, ''


def pick(rec, cache, path, delay):
    flags = []
    # 질의 후보: 이름 → 이름+지역 → 복합 이름의 첫 구성요소 → 첫 구성요소+지역 (최대 4회 요청)
    parts = [p for p in re.split(r'[·/／・]|\(|（', rec['q']) if p.strip()]
    first = re.sub(r'[\)）].*$', '', parts[0]).strip() if parts else rec['q']
    queries = [rec['q'], rec['q2']]
    if first and first != rec['q']:
        queries += [first, f"{first} {rec['q2'][len(rec['q']):].strip()}".strip()]
    toks = rec['q'].split()
    if len(toks) > 1:                                   # '추암 촛대바위' → '추암촛대바위', '촛대바위'
        queries += [''.join(toks), toks[-1]]
    cands, chosen = [], None
    for n, qq in enumerate(queries):
        cands = search(qq, rec['cc'], cache, path, delay)
        scored = sorted(((score(c, rec), c) for c in cands), key=lambda t: -t[0][0])
        if scored and scored[0][0][0] > 2:
            chosen = scored[0]
            if n:
                flags.append(f'query_variant_{n}')
            break
    if not chosen:
        if cands:                      # 후보는 있지만 교통시설뿐 등
            sc, c = sorted(((score(c, rec), c) for c in cands), key=lambda t: -t[0][0])[0]
            chosen = (sc, c)
            flags.append('only_poor_candidates')
        else:
            return {'id': rec['id'], 'confidence': 'none', 'flags': flags + ['no_result']}
    (sc, why), c = chosen
    disp = c.get('display_name', '')
    region_ok = region_hits(rec['region'], disp)
    cls, typ = c.get('category'), c.get('type')
    geo_type = 'area' if (cls in AREA_CLASS and c.get('osm_type') == 'relation') or cls in {'boundary', 'natural', 'landuse'} else 'point'
    precision = 'centroid' if geo_type == 'area' else ('place' if cls == 'place' else 'poi')
    if not region_ok:
        flags.append('region_not_in_display')
    sgg = rec.get('sgg') or []
    local_ok = True
    if sgg and not any(t in disp for t in sgg):             # 같은 이름의 다른 지역 장소를 잡은 경우
        local_ok = False
        flags.append('locality_mismatch')
    if rec['city'] and core(rec['city']) not in disp:
        flags.append('city_not_in_display')
    if why:
        flags.append(why)
    if cls == 'place':
        flags.append('matched_a_place_not_a_poi')
    anc = cls in SOFT_BAD_CLASS or typ in SOFT_BAD_TYPE
    if anc:
        flags.append('ancillary_facility')
    if 'only_poor_candidates' in flags or cls in NON_POI_CLASS or not local_ok:
        conf = 'low'
    elif anc and region_ok:
        conf = 'medium'
    elif 'city_not_in_display' in flags:
        conf = 'medium' if region_ok else 'low'
    elif sc >= 6 and region_ok and not why and cls != 'place':
        conf = 'high'
    elif region_ok and not why:
        conf = 'medium'
    else:
        conf = 'low'
    return {'id': rec['id'], 'lat': round(float(c['lat']), 6), 'lng': round(float(c['lon']), 6), 'geo_type': geo_type,
            'precision': precision, 'geo_source': 'osm_nominatim', 'osm': f"{c.get('osm_type')}/{c.get('osm_id')}",
            'osm_class': cls, 'osm_type': typ, 'matched_name': (c.get('name') or '')[:80], 'matched_display': disp[:140],
            'confidence': conf, 'flags': flags}


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--cache', required=True)
    ap.add_argument('--delay', type=float, default=1.1)
    ap.add_argument('--only', help='kr|jp|cn')
    ap.add_argument('--limit', type=int, default=0)
    a = ap.parse_args()
    cache = json.load(open(a.cache, encoding='utf-8')) if os.path.exists(a.cache) else {}
    recs = [r for r in load(a.root) if not a.only or r['cc'] == a.only]
    if a.limit:
        recs = recs[: a.limit]
    out = {'kr': [], 'jp': [], 'cn': []}
    for i, r in enumerate(recs, 1):
        out[r['cc']].append(pick(r, cache, a.cache, a.delay))
        if i % 25 == 0:
            print(f'{i}/{len(recs)}', flush=True)
    os.makedirs(f'{a.root}/travel-common/coordinates', exist_ok=True)
    for cc, rows in out.items():
        if rows:
            json.dump({'country': cc, 'source': 'OpenStreetMap contributors (ODbL) via Nominatim', 'generated': '2026-10-10',
                       'items': rows}, open(f'{a.root}/travel-common/coordinates/{cc}.json', 'w', encoding='utf-8'),
                      ensure_ascii=False, indent=1)
    print('done', {k: len(v) for k, v in out.items()}, flush=True)
