import json, re, sys
T='/tmp/claude-0/-home-user/8dd0b81a-179c-57e0-a83d-a5b3adbd13ea/tasks'
def last(agent, test, pat):
    best=None
    for line in open(f'{T}/{agent}.output',encoding='utf-8'):
        try: ev=json.loads(line)
        except: continue
        st=[ev]
        while st:
            o=st.pop()
            if isinstance(o,str):
                if test(o): best=o
            elif isinstance(o,dict): st+=o.values()
            elif isinstance(o,list): st+=o
    return json.loads(re.search(pat,best,re.S).group(0))
mode=sys.argv[1]
if mode=='collected':   # pipe.py collected <agent> <n>
    d=last(sys.argv[2], lambda s:'"claims"' in s and '"unconfirmed"' in s and '"key"' in s, r'\[\s*\{.*\}\s*\]')
    n=sys.argv[3]; json.dump(d,open(f'r1/collected{n}.json','w'),ensure_ascii=False,indent=1)
    out=[{'key':p['key'],'name_ko':p['name_ko'],'name_local':p['name_local'],'admin_region':p.get('admin_region'),'address':p.get('address'),
          'description':p.get('description',''),'highlights':p.get('highlights',[]),
          'claims':[{k:c[k] for k in ('cid','field','text','value')}|{'urls':[s['url'] for s in c['sources']]} for c in p['claims']],
          'collector_unconfirmed':[u['field'] for u in p['unconfirmed']]} for p in d if p['claims']]
    json.dump(out,open(f'r1/verify_in{n}.json','w'),ensure_ascii=False,indent=1)
    print(n,[(p['key'],len(p['claims'])) for p in d])
elif mode=='verified':  # pipe.py verified <agent> <n>
    d=last(sys.argv[2], lambda s:'"places"' in s and '"verdicts"' in s, r'\{\s*"places".*\}')
    json.dump(d,open(f'r1/verified{sys.argv[3]}.json','w'),ensure_ascii=False,indent=1)
    print(sys.argv[3], d.get('summary',{}))
