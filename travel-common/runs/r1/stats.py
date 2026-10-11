import json,glob,sys,collections
sys.path.insert(0,'wt4/travel-common/tools')
from v2common import CHECKLIST, PUBLISHABLE
for cc in ('kr','jp','cn'):
    P=[json.load(open(f)) for f in sorted(glob.glob(f'wt4/travel-common/v2/places/{cc}/*.json'))]
    P=[p for p in P if any(r['run'].startswith('r1-') for r in p['meta']['runs'])]
    cl=[c for p in P for c in p['claims'] if c['run'].startswith('r1-') and c['verdict']!='suggested']
    v=collections.Counter(c['verdict'] for c in cl)
    fill=[sum(p['checklist'][k]['status']=='filled' for k in CHECKLIST) for p in P]
    gaps=collections.Counter(p['checklist'][k]['gap']['reason'] for p in P for k in CHECKLIST if p['checklist'][k]['status']=='gap')
    item=collections.Counter(k for p in P for k in CHECKLIST if p['checklist'][k]['status']=='filled')
    sug=sum(c['verdict']=='suggested' for p in P for c in p['claims'] if c['run'].startswith('r1-'))
    n=len(cl)
    print(cc, 'places',len(P),'verified',sum(p['status']=='verified' for p in P),'claims',n,dict(v),
          'corr%%=%.1f'%(100*(v['corrected']+v['outdated'])/n),'nonpub%%=%.1f'%(100*(n-sum(v[k] for k in PUBLISHABLE))/n),
          'fill=%.1f'%(sum(fill)/len(P)),'suggested',sug, dict(gaps))
    print('  items',{k:item[k] for k in CHECKLIST})
    print('  weak',sorted([(f,p['id']) for f,p in zip(fill,P) if f<=3]))
    print('  draft',[p['id'] for p in P if p['status']!='verified'])
