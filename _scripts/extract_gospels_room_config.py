#!/usr/bin/env python3
"""Extract the Gospels reading-room image config from the Lovable gospel-depths mock.
render-from-data (§2.16). Preserves EXACT img URLs + crops (curation, per IMAGE-CREDITS.md
'never swap/regenerate'). Re-run if the mock updates. Credits per IMAGE-CREDITS.md (CC0)."""
import re, json, sys

GDE = sys.argv[1] if len(sys.argv) > 1 else "."
def match_close(s, i):
    open_c=s[i]; depth=0; instr=None
    while i < len(s):
        c=s[i]
        if instr:
            if c=='\\': i+=2; continue
            if c==instr: instr=None
        elif c in '"\'`': instr=c
        elif c in '[{': depth+=1
        elif c in ']}':
            depth-=1
            if depth==0: return i
        i+=1
    return -1
def objs(body):
    i=0
    while i < len(body):
        if body[i]=='{':
            j=match_close(body,i); yield body[i:j+1]; i=j+1
        else: i+=1
def field(o,k):
    m=re.search(k+r'\s*:\s*"((?:[^"\\]|\\.)*)"', o); return m.group(1).replace('\\"','"') if m else None

def sections_from(path, imgkey='img'):
    src=open(path).read()
    si=src.index('SECTIONS' if 'plates' in path else 'MOVEMENTS')
    eq=src.index('=', si); lb=src.index('[', eq)          # <-- the array '[', AFTER '=' (skips Section[])
    arr=src[lb:match_close(src,lb)+1]
    out=[]
    for sec in objs(arr[1:-1]):
        rec={"n":field(sec,'n'),"title":field(sec,'title'),"latin":field(sec,'latin')}
        rec["brief"]=field(sec,'brief') or field(sec,'line')
        # candidate arrays (plates) OR single img (contents)
        if 'cands' in sec:
            ci=sec.index('cands'); clb=sec.index('[',ci); cbody=sec[clb:match_close(sec,clb)+1]
            cands=[]
            for c in objs(cbody[1:-1]):
                img=field(c,'img')
                if not img: continue
                t=field(c,'t'); d=field(c,'d'); a=field(c,'a'); note=field(c,'note')
                cm=re.search(r'crop\s*:\s*\[([^\]]+)\]', c)
                crop=[float(x) for x in cm.group(1).split(',')] if cm else None
                cands.append({"img":img,"title":t,"date":d,"artist":a,"crop":crop,
                              "current":bool(re.search(r'current\s*:\s*true',c)),
                              "credit":" · ".join(x for x in [t,a,d,"The Met"] if x),
                              **({"note":note} if note else {})})
            rec["candidates"]=cands
        out.append(rec)
    return out

plates=sections_from(GDE+"/src/routes/plates.tsx")
config={"_note":"Gospels reading-room image config — extracted from the Lovable gospel-depths mock (plates.tsx) via _scripts/extract_gospels_room_config.py. render-from-data (§2.16). Images MET Open Access (CC0); provenance authoritative in the mock's IMAGE-CREDITS.md. RULES: never swap/regenerate images; crop = curation, tune don't reset; on 404 look up SAME object via Met API. 'credit' = museum caption + PD-source record (§2.4).",
 "source":"gospel-depths-explorer mock · plates.tsx + IMAGE-CREDITS.md",
 "license":"The Metropolitan Museum of Art — Open Access (CC0)",
 "movements":plates}
open("reading-room-preview/data/gospels_room_config.json","w").write(json.dumps(config,indent=2,ensure_ascii=False))
print("movements:",len(plates),"| total candidates:",sum(len(s['candidates']) for s in plates))
for s in plates: print(f"  {s['n']} {s['title']:13s} {len(s['candidates'])} cands · current: {[c['title'][:30] for c in s['candidates'] if c['current']]}")
