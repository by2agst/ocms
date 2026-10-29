import json,glob,subprocess,collections,sys
from pathlib import Path
A=Path('docs/archify'); I=A/'_inputs'
sid={}
for f in sorted(glob.glob(str(I/'story_id'/'*.json'))): sid.update(json.load(open(f)))
old=json.load(open(A/'story_id.json')); old.update(sid)
(A/'story_id.json').write_text(json.dumps(old,ensure_ascii=False,indent=1))
TYPE_EN={'Removed tapi mirip':'Removed but similar','Kode tanpa story':'Code without story','Code tanpa story (cek)':'Code without story (to check)','Code tanpa story (belum dipastikan)':'Code without story (unconfirmed)','Code tanpa story':'Code without story','Tanpa story':'Without story'}

def en_type(t):
    if t in TYPE_EN: return TYPE_EN[t]
    r=t
    for a,b in (('Kode ada tanpa story','Code exists without story'),('Kode tanpa story','Code without story'),('Code tanpa story','Code without story'),('Tidak ada story','No story'),('tanpa story','without story'),('belum dipastikan','unconfirmed'),('di chunk ini','in this chunk'),('di chunk','in this chunk'),('(cek)','(to check)')):
        r=r.replace(a,b)
    return r
key=lambda p:[int(x) for x in Path(p).stem[4:].split('.')]
oid,oen,seen=[],[],set()
for f in sorted(glob.glob(str(I/'orphans'/'*.json')),key=key):
    for o in json.load(open(f)):
        k=(o['feature'],o['source'][:80])
        if k in seen: continue
        seen.add(k)
        base={x:o[x] for x in ('feature','source','story','type','verified','note')}
        oid.append(base); e=dict(base); e['type']=en_type(o['type']); e['note']=o.get('note_en') or o['note']; oen.append(e)
(A/'meta.json').write_text(json.dumps({'prelim':{},'orphans':oid},ensure_ascii=False,indent=1))
(A/'en'/'meta.en.json').write_text(json.dumps({'prelim':{},'orphans':oen},ensure_ascii=False,indent=1))
print('story_id',len(old),'orphans',len(oid),dict(collections.Counter(o['type'] for o in oid)))
sk=str(Path.home()/'.claude/skills/story-evidence-report/scripts')
for s in ('build.py','build_index.py'):
    r=subprocess.run(['python3','-I',f'{sk}/{s}'],capture_output=True,text=True); print((r.stdout+r.stderr).strip().splitlines()[-2:])
