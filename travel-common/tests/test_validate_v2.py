import copy, os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tools'))
import validate_v2 as v
from v2common import CHECKLIST, path_of, save, empty_checklist, recompute_checklist


def claim(cid, field, verdict='verified', url='https://example.go.kr', stype='official', checked='2026-10-11'):
    return {'cid': cid, 'field': field, 'text': f'{field} 사실', 'original_text': None, 'value': None, 'verdict': verdict,
            'sources': [{'url': url, 'type': stype, 'page_updated': None, 'checked_at': checked}], 'run': 't'}


def place():
    p = {'id': 'kr-test', 'country': 'kr', 'tier': 'A', 'status': 'verified', 'names': {'ko': '테스트', 'local': '테스트'},
         'admin_region': '서울특별시', 'city': '', 'address': None,
         'coord': {'lat': 37.58, 'lng': 126.98, 'geo_type': 'point', 'precision': 'poi', 'geo_source': 'osm_nominatim', 'confidence': 'high', 'osm': 'n/1'},
         'checklist': empty_checklist(), 'claims': [claim(f'c{i}', k) for i, k in enumerate(CHECKLIST)],
         'conflicts': [], 'content_review': {'status': 'ok'}, 'meta': {'runs': []}}
    return recompute_checklist(p)


def run(p, today='2026-10-11'):
    d = tempfile.mkdtemp()
    save(path_of(d, p['country'], p['id']), p)
    return v.store(d, today)


class T(unittest.TestCase):
    def test_recompute_keeps_partial_gaps(self):
        p = place(); p['checklist']['hours']['partial_gaps'] = [{'reason': 'not_in_official_source', 'note': 'x', 'run': 't'}]
        recompute_checklist(p); self.assertEqual(len(p['checklist']['hours']['partial_gaps']), 1)

    def test_valid(self):
        e, w = run(place()); self.assertEqual(e, []); self.assertEqual(w, [])

    def test_publishable_claim_needs_url(self):
        p = place(); p['claims'][0]['sources'][0]['url'] = None
        e, _ = run(p); self.assertTrue(any('without url' in m for m in e))

    def test_owner_input_without_url_is_allowed(self):
        p = place(); p['claims'][0].update(verdict='owner_verified', sources=[{'url': None, 'type': 'owner_input', 'checked_at': '2026-10-11'}])
        e, _ = run(p); self.assertEqual(e, [])

    def test_blog_source_type_rejected(self):
        p = place(); p['claims'][1]['sources'][0]['type'] = 'blog'
        e, _ = run(p); self.assertTrue(any("'blog' not allowed" in m for m in e))

    def test_filled_item_must_point_to_publishable_claim(self):
        p = place(); p['claims'][2]['verdict'] = 'unverifiable'      # duration
        e, _ = run(p); self.assertTrue(any('checklist duration filled but claims invalid' in m for m in e))
        recompute_checklist(p)                                          # 재계산하면 gap 으로 바뀐다
        p['checklist']['duration']['gap'] = {'reason': 'not_in_official_source', 'note': 'x'}
        e, _ = run(p); self.assertEqual(e, [])

    def test_gap_needs_known_reason(self):
        p = place(); p['claims'] = p['claims'][1:]; recompute_checklist(p)
        p['checklist']['location']['gap'] = {'reason': 'blog_said_so'}
        e, _ = run(p); self.assertTrue(any('gap without valid reason' in m for m in e))

    def test_verified_requires_content_review_and_no_pending(self):
        p = place(); p['content_review'] = {'status': 'needs_fix'}; p['claims'].append(claim('cx', 'description', verdict='pending'))
        e, _ = run(p)
        self.assertTrue(any('content_review not ok' in m for m in e)); self.assertTrue(any('pending' in m for m in e))

    def test_verified_cannot_have_uncollected_items(self):
        p = place(); p['claims'] = p['claims'][1:]; recompute_checklist(p)   # location → not_collected
        e, _ = run(p); self.assertTrue(any('not_collected' in m for m in e))

    def test_coord_outside_country(self):
        p = place(); p['coord']['lat'] = 10
        e, _ = run(p); self.assertTrue(any('bounding box' in m for m in e))

    def test_stale_check_warns(self):
        p = place(); p['claims'][0]['sources'][0]['checked_at'] = '2026-01-01'
        _, w = run(p); self.assertTrue(any('> 90' in m for m in w))


if __name__ == '__main__':
    unittest.main(verbosity=1)
