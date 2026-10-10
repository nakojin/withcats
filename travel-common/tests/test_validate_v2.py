import copy, json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
import validate_v2 as v

OK = {
 'id': 'kr-test', 'country': 'kr', 'admin_region': '서울특별시', 'source_region': '서울', 'city': '종로구',
 'names': {'ko': '테스트궁', 'local': '테스트궁'}, 'category': ['궁궐'],
 'coord': {'lat': 37.58, 'lng': 126.98, 'geo_type': 'point', 'precision': 'poi', 'geo_source': 'osm_nominatim', 'confidence': 'high'},
 'summary': '요약 문장.', 'description': '가' * 320, 'highlights': ['a', 'b', 'c', 'd'], 'recommended_duration_min': 90,
 'best_time': '봄', 'how_to_get_there': '지하철 3호선',
 'ops': {k: {'status': 'confirmed', 'value': 'x', 'note': None, 'checked_at': '2026-10-10'} for k in v.OPS_KEYS},
 'sources': [{'url': 'https://example.go.kr', 'checked_at': '2026-10-10', 'supports': list(v.OPS_KEYS)}],
 'quality': {'depth_tier': 'A', 'last_verified': '2026-10-10'},
}

def run(p, today='2026-10-10'):
    f = tempfile.NamedTemporaryFile('w', suffix='.json', delete=False, encoding='utf-8')
    json.dump([p], f, ensure_ascii=False); f.close()
    try: return v.places(f.name, today)
    finally: os.unlink(f.name)

class T(unittest.TestCase):
    def test_valid(self):
        e, w = run(OK); self.assertEqual(e, [])
    def test_confirmed_without_source_support(self):
        p = copy.deepcopy(OK); p['sources'][0]['supports'] = ['hours']
        e, _ = run(p); self.assertTrue(any('fees' in m and 'no source' in m for m in e))
    def test_unconfirmed_needs_null_and_note(self):
        p = copy.deepcopy(OK); p['ops']['payment'] = {'status': 'unconfirmed', 'value': '현금', 'note': None}
        e, _ = run(p); self.assertTrue(any('value null' in m for m in e)); self.assertTrue(any('note' in m for m in e))
    def test_tier_a_requires_depth(self):
        p = copy.deepcopy(OK); p['description'] = '짧다'; p['highlights'] = ['a']
        e, _ = run(p); self.assertTrue(any('300' in m for m in e)); self.assertTrue(any('highlights' in m for m in e))
    def test_tier_a_requires_hours_fees_known(self):
        p = copy.deepcopy(OK); p['ops']['fees'] = {'status': 'unconfirmed', 'value': None, 'note': '공식 미기재'}
        e, _ = run(p); self.assertTrue(any('tier A needs ops.fees' in m for m in e))
    def test_coord_outside_country(self):
        p = copy.deepcopy(OK); p['coord']['lat'] = 10
        e, _ = run(p); self.assertTrue(any('bounding box' in m for m in e))
    def test_stale_verification_warns(self):
        p = copy.deepcopy(OK); p['quality']['last_verified'] = '2026-01-01'
        _, w = run(p); self.assertTrue(any('> 90' in m for m in w))
    def test_tier_b_can_have_unconfirmed(self):
        p = copy.deepcopy(OK); p['quality']['depth_tier'] = 'B'
        p['ops']['fees'] = {'status': 'unconfirmed', 'value': None, 'note': '공식 미기재'}
        e, _ = run(p); self.assertEqual(e, [])

if __name__ == '__main__':
    unittest.main(verbosity=2)
