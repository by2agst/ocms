import json,re,sys
from pathlib import Path
A=Path('docs/archify'); ep=sys.argv[1]
ids=sorted([p.name for p in A.glob(f'OCMS{ep}.*') if p.is_dir()]+[p.stem.replace('.trace','') for p in []],key=lambda s:int(s.split('.')[1]))
ids=sorted({p.parent.name for p in A.glob(f'OCMS{ep}.*/*.trace.json')},key=lambda s:int(s.split('.')[1]))
for s in ids:
    t=json.loads((A/s/f'{s}.trace.json').read_text()); p=json.loads((A/'plain'/f'{s}.plain.json').read_text()); e=json.loads((A/'en'/f'{s}.en.json').read_text())
    st=t['steps']; f=[x['fit'] for x in st]; pct=(f.count('Sesuai')+.5*f.count('Sebagian'))/len(st)*100
    bad=[]
    for x in st:
        for fl,a,b in re.findall(r'([\w./\-]+\.\w+):(\d+)(?:-(\d+))?',x.get('code_ref') or ''):
            if fl.startswith('ocmsadminprivateapi/cronservice/'): bad.append(('STALE-COPY',fl)); continue
            fp=Path(fl)
            if not fp.exists(): bad.append(('missing',fl)); continue
            L=sum(1 for _ in open(fp,errors='ignore'))
            if int(a)>L or (b and int(b)>L): bad.append(('range',fl,a,b,L))
    fl_bad=[x['flow_file'] for x in st if x['flow_file']!='User story (tidak ada di flow deck)']
    lang=[i for i,x in enumerate(p['steps']) if re.search(r'\b(yang|dan|untuk|tidak|dengan)\b',x['en'].lower()) or re.search(r'\b(the|and|with|of)\b',x['id'].lower())]
    cw=[i for i,x in enumerate(p['steps']) if re.search(r'\.(java|ts|tsx)\b|\b(server|endpoint|payload|API|cron|table|SFTP|JWT)\b',x['en']+' '+x['id'])]
    pctnote=re.findall(r'(\d+(?:[.,]\d+)?)\s*%',t.get('note',''))
    html=[(A/s/f'{s}.html').exists(),(A/s/f'{s}.id.html').exists()]
    print(s,len(st),len(p['steps']),len(e['steps']),f'{pct:.1f}%',dict((k,f.count(k)) for k in set(f)),'bad',bad[:3],'flow',len(fl_bad),'lang',lang,'codewords',cw,'notepct',pctnote[:2],'html',html)
