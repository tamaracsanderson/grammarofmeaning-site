#!/usr/bin/env python3
"""Trail-map interaction concept for the golden-chain trace-tree (bakeoff entry #2).

"Paths in the woods, which are taken" — Saquib's grammar: time runs left→right (roots → the
letter → reception → today); SOLID trails = what we know (attested), DASHED = what could have
been (reconstructed); paths are named and traceable; every signpost carries plain words. Fixes
the "squished / not enough words" feel with an orientation frame, few landmarks, and
click-a-signpost-to-learn (progressive disclosure). Self-contained; content is reading-SB's,
from the golden-chain source. Candidate pilot.

Usage: build_trailmap.py <OUTPUT.html>
"""
import sys, json

# landmarks along the trail (x = time, left→right)
NODES = {
 "philo":   dict(x=120, y=110, kind="root", prov="recon", label="Philo", sub="Middle-Platonic conduit",
                 d="<b>A root we can only reconstruct.</b> A possible Hellenistic-Jewish conduit between Greek ideas and Paul — entirely inferential, no textual link. Drawn as a faded trail: it <i>could have</i> fed the chain; we cannot show that it did."),
 "stoic":   dict(x=95, y=300, kind="root", prov="recon", label="Stoic pronoia", sub="“all things work together”",
                 d="<b>The faintest trail on the map.</b> Stoic cosmic providence echoes Romans 8:28 (“all things work together for good”), but no citation exists. Is Paul borrowing, or just sharing the vocabulary of his age? The most fragile could-have-been edge."),
 "qumran":  dict(x=150, y=470, kind="root", prov="recon", label="Qumran · 1QS", sub="the “Two Spirits”",
                 d="<b>A parallel, not a source.</b> The Dead Sea “Two Spirits” text is a real predestinarian cousin — but Paul never quotes it. Shared water, not a proven stream. Dashed."),
 "yada":    dict(x=320, y=175, kind="root", prov="attested", label="Hebrew yāda‘", sub="covenant “knowing”",
                 d="<b>A documented root.</b> The Hebrew <i>yāda‘</i> (Amos 3:2; Jer 1:5) means covenant election, not cognition — and the Greek Old Testament renders it with the very verb behind “foreknew.” A solid trail: the lexical bridge is attested."),
 "deut":    dict(x=320, y=405, kind="root", prov="attested", label="Deuteronomy", sub="chosen by love, not merit",
                 d="<b>A documented root.</b> Deut 7:7–8 / 9:4–6 — God set his love on Israel, not for their righteousness. This is the <i>warrant</i> the chain leaves unspoken. Solid."),
 "pivot":   dict(x=595, y=290, kind="pivot", prov="attested", label="Romans 8:28–30", sub="the golden chain",
                 d="<b>Where you’re standing.</b> The five links — foreknew · predestined · called · justified · glorified — that Paul chains into one unbroken sweep. Every trail on this map runs into it or out of it. The roads back (the roots it grew from) and the roads forward (the doctrines it became) were traced <i>separately</i> and meet only here."),
 "fork":    dict(x=760, y=290, kind="fork", prov="attested", label="“foreknew” — προέγνω", sub="the trail splits",
                 d="<b>The fork in the woods.</b> One word decides the whole map. Read <i>proginōskō</i> as fore-<b>love</b> (God chose them) and you take the upper trail; read it as fore-<b>see</b> (God saw their faith coming) and you take the lower. Two readings of one verse — this is the road that diverged."),
 "augustine":dict(x=855, y=150, kind="interp", prov="attested", label="Augustine", sub="unconditional",
                 d="<b>Upper trail · documented.</b> Augustine reads election as unconditional and comments directly on this passage. Attested that he walked here — not proof his reading is the verse’s only sense."),
 "calvin":  dict(x=985, y=115, kind="interp", prov="attested", label="Calvin", sub="the ordo salutis",
                 d="<b>Upper trail · documented.</b> Calvin carries Augustine’s reading into a system — the chain becomes the order of salvation. Solid."),
 "dort":    dict(x=1110, y=120, kind="doctrine", prov="attested", label="Canons of Dort", sub="unconditional election",
                 d="<b>Where the upper trail comes out today.</b> The Reformed formula — unconditional election, perseverance. The end of the fore-love path."),
 "arminius":dict(x=855, y=430, kind="interp", prov="attested", label="Arminius", sub="foreseen faith",
                 d="<b>Lower trail · documented.</b> Arminius reads “foreknew” as God foreseeing who would believe — election becomes conditional. It is <i>his</i> reading of one verb that opens this whole trail."),
 "wesley":  dict(x=985, y=465, kind="interp", prov="attested", label="Wesley", sub="grace you can lose",
                 d="<b>Lower trail · documented.</b> Wesley adds prevenient grace and a grace that can be fallen from — the chain’s links become losable. Solid."),
 "remon":   dict(x=1110, y=460, kind="doctrine", prov="attested", label="Remonstrance", sub="conditional election",
                 d="<b>Where the lower trail comes out today.</b> The Arminian formula — conditional election, resistible grace. The end of the fore-see path."),
 "today":   dict(x=1185, y=290, kind="today", prov="attested", label="Today", sub="",
                 d="<b>Today.</b> Both trails are still walked — the same five verses, two live readings, four centuries on."),
}
# trail segments: (from, to, trail-membership, prov)
EDGES = [
 ("yada","pivot","roots","attested"),
 ("deut","pivot","roots","attested"),
 ("qumran","pivot","couldhavebeen","recon"),
 ("stoic","pivot","couldhavebeen","recon"),
 ("philo","pivot","couldhavebeen","recon"),
 ("pivot","fork","both","attested"),
 ("fork","augustine","reformed","attested"),
 ("augustine","calvin","reformed","attested"),
 ("calvin","dort","reformed","attested"),
 ("dort","today","reformed","attested"),
 ("fork","arminius","arminian","attested"),
 ("arminius","wesley","arminian","attested"),
 ("wesley","remon","arminian","attested"),
 ("remon","today","arminian","attested"),
]
# the named trails a walker can pick
TRAILS = {
 "roots":    dict(label="The roots it grew from", desc="back to what the chain was built on — two documented (yāda‘, Deuteronomy), three we can only reconstruct (Stoic, Philo, Qumran).", members_edges=["roots","couldhavebeen"], color="var(--myst)"),
 "reformed": dict(label="The fore-LOVE trail → Dort", desc="read “foreknew” as God choosing, and the trail runs Augustine → Calvin → the Canons of Dort: unconditional election.", members_edges=["reformed","both"], color="var(--moss)"),
 "arminian": dict(label="The fore-SEE trail → Remonstrance", desc="read “foreknew” as God foreseeing faith, and the trail runs Arminius → Wesley → the Remonstrance: conditional election.", members_edges=["arminian","both"], color="var(--gold)"),
}

def trail_path(x1,y1,x2,y2):
    dx=x2-x1
    return f"M {x1} {y1} C {x1+dx*0.42} {y1}, {x2-dx*0.42} {y2}, {x2} {y2}"

def build(out):
    W,H=1240,600
    # edges svg
    edge_svg=[]
    for i,(a,b,trail,prov) in enumerate(EDGES):
        n1,n2=NODES[a],NODES[b]
        d=trail_path(n1["x"],n1["y"],n2["x"],n2["y"])
        dash='stroke-dasharray="2 9"' if prov=="recon" else ''
        cls=f"seg {prov} t-{trail}"
        edge_svg.append(f'<path class="{cls}" data-trail="{trail}" d="{d}" fill="none" {dash} stroke-linecap="round"/>')
    # node svg (signposts)
    node_svg=[]
    for nid,n in NODES.items():
        k=n["kind"]
        if k=="today":
            node_svg.append(f'<g class="mk today" data-node="{nid}"><line x1="{n["x"]}" y1="60" x2="{n["x"]}" y2="530" stroke="var(--line2)" stroke-width="1.5" stroke-dasharray="3 5"/><text x="{n["x"]}" y="50" text-anchor="middle" class="todaylab">TODAY</text></g>')
            continue
        w = 150 if k in("pivot",) else 128
        node_svg.append(
          f'<g class="mk k-{k} p-{n["prov"]}" data-node="{nid}" tabindex="0" transform="translate({n["x"]-w//2},{n["y"]-22})">'
          f'<rect class="box" width="{w}" height="44" rx="10"/>'
          f'<text class="lab" x="{w//2}" y="19" text-anchor="middle">{n["label"]}</text>'
          f'<text class="sub" x="{w//2}" y="34" text-anchor="middle">{n["sub"]}</text>'
          f'</g>')

    DATA=json.dumps({nid:{"label":n["label"],"kind":n["kind"],"prov":n["prov"],"d":n["d"]} for nid,n in NODES.items()}, ensure_ascii=False)
    TRAILJSON=json.dumps(TRAILS, ensure_ascii=False)

    HTML=f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>The golden chain, as a trail — Grammar of Meaning</title>
<style>
  :root{{--paper:#f7f2e7;--paper2:#fffdf7;--card:#fffefa;--ink:#26221a;--ink2:#5b5346;--ink3:#8a8172;--line:#e4dcc9;--line2:#d0c6ae;--moss:#4b6b46;--moss-d:#33502f;--gold:#b8892f;--gold-bg:#f6ecd4;--myst:#5b53a6;--myst-bg:#eae7f6;--terra:#9c3f37;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,sans-serif;--serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;}}
  @media (prefers-color-scheme:dark){{:root{{--paper:#14130f;--paper2:#1a1813;--card:#1e1b15;--ink:#ece7dc;--ink2:#b3aa98;--ink3:#847c6c;--line:#332f27;--line2:#423d31;--moss:#8fb884;--moss-d:#6c9a62;--gold:#e0b45f;--gold-bg:#2c2410;--myst:#a99ee6;--myst-bg:#221d38;--terra:#d98b80;}}}}
  *{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15.5px;line-height:1.6}}
  .wrap{{max-width:1180px;margin:0 auto;padding:0 22px 80px}}
  a{{color:var(--moss-d)}}@media(prefers-color-scheme:dark){{a{{color:var(--moss)}}}}
  header{{padding:40px 0 14px}}
  .banner{{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#fff;background:var(--terra);padding:4px 10px;border-radius:5px;margin-bottom:14px}}
  .eyebrow{{font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}}
  h1{{font-family:var(--serif);font-weight:500;font-size:31px;line-height:1.12;margin:0 0 10px}}
  .orient{{background:var(--card);border:1px solid var(--line2);border-left:3px solid var(--moss);border-radius:0 12px 12px 0;padding:15px 19px;margin:8px 0 20px;font-size:15.5px;color:var(--ink2);max-width:80ch}}
  .orient b{{color:var(--ink)}}
  /* trail picker */
  .pick{{display:flex;gap:9px;flex-wrap:wrap;margin:0 0 6px}}
  .pbtn{{font-family:var(--sans);font-size:13.5px;padding:8px 14px;border-radius:99px;border:1.5px solid var(--line2);background:var(--paper2);color:var(--ink2);cursor:pointer;transition:.16s}}
  .pbtn:hover{{border-color:var(--ink3)}}
  .pbtn.on{{border-color:var(--ink);background:var(--ink);color:var(--paper);font-weight:600}}
  .pdesc{{font-size:13.5px;color:var(--ink2);min-height:2.6em;margin:8px 2px 6px;max-width:82ch}}
  /* map */
  .mapwrap{{overflow-x:auto;border:1px solid var(--line2);border-radius:14px;background:var(--paper2)}}
  svg.trail{{display:block;width:100%;min-width:1040px;height:auto}}
  .era{{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;fill:var(--ink3)}}
  .baseline{{stroke:var(--line2);stroke-width:1.5}}
  .seg{{stroke:var(--ink3);stroke-width:3;opacity:.5;transition:opacity .18s,stroke .18s,stroke-width .18s}}
  .seg.recon{{stroke:var(--myst);opacity:.4}}
  .seg.lit{{opacity:1;stroke-width:5}}
  .seg.dim{{opacity:.12}}
  .mk{{cursor:pointer}}
  .mk .box{{fill:var(--card);stroke:var(--line2);stroke-width:1.6;transition:.16s}}
  .mk .lab{{font-family:var(--serif);font-size:14px;font-weight:600;fill:var(--ink)}}
  .mk .sub{{font-family:var(--sans);font-size:10.5px;fill:var(--ink3)}}
  .mk.p-recon .box{{stroke:var(--myst);stroke-dasharray:3 4}}
  .mk.k-pivot .box{{fill:var(--gold-bg);stroke:var(--gold);stroke-width:2.4}}
  .mk.k-fork .box{{fill:#fbeee9;stroke:var(--terra);stroke-width:2}}
  @media(prefers-color-scheme:dark){{.mk.k-fork .box{{fill:#2a1a17}}}}
  .mk:hover .box,.mk.sel .box{{stroke-width:3;filter:drop-shadow(0 2px 6px rgba(0,0,0,.14))}}
  .mk.dim{{opacity:.22}}
  .todaylab{{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.1em;fill:var(--ink3)}}
  .legend{{display:flex;gap:20px;flex-wrap:wrap;font-family:var(--mono);font-size:11.5px;color:var(--ink3);margin:12px 2px 0;align-items:center}}
  .legend .sw{{display:inline-block;width:26px;height:0;border-top:3px solid var(--ink3);vertical-align:middle;margin-right:7px}}
  .legend .sw.re{{border-top:3px dashed var(--myst)}}
  /* learn panel */
  #panel{{margin-top:16px;background:var(--card);border:1px solid var(--line2);border-radius:12px;overflow:hidden}}
  #ph{{display:flex;align-items:center;gap:10px;padding:12px 18px;background:var(--pivot-bg,var(--gold-bg));border-bottom:1px solid var(--line2)}}
  #pk{{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:#fff;background:var(--moss);padding:3px 9px;border-radius:20px}}
  #pt{{font-family:var(--serif);font-weight:600;font-size:17px}}
  #pb{{padding:15px 20px;font-size:15px;line-height:1.6;color:var(--ink2)}}
  #pb b{{color:var(--ink)}}
  .backlink{{display:inline-block;margin:24px 0 0;font-family:var(--mono);font-size:12px}}
  .foot{{margin-top:36px;padding-top:16px;border-top:1px solid var(--line);font-family:var(--mono);font-size:12px;color:var(--ink3);line-height:1.7}}
</style>
</head>
<body>
<div class="wrap">
<header>
  <span class="banner">candidate · interaction bakeoff · entry #2 · trail-map</span>
  <p class="eyebrow">the coding lab · reading a passage as a trail</p>
  <h1>The golden chain, as a trail through the woods</h1>
  <div class="orient"><b>What you’re looking at.</b> One passage — Romans 8:28–30 — with time running left to right. To the <b>left</b>, the roots it grew from; in the <b>middle</b>, the passage itself; to the <b>right</b>, the doctrines it became, all the way to <b>today</b>. A <b>solid</b> trail is a path we can document. A <b>dashed</b> trail is one we can only reconstruct — a road that <i>might</i> have been walked. <b>Pick a trail below</b> to light it up, or <b>click any signpost</b> to learn what stands there.</div>
</header>

<div class="pick" id="pick">
  <button class="pbtn on" data-t="all">Show the whole map</button>
  <button class="pbtn" data-t="roots">The roots it grew from</button>
  <button class="pbtn" data-t="reformed">The fore-LOVE trail → Dort</button>
  <button class="pbtn" data-t="arminian">The fore-SEE trail → Remonstrance</button>
</div>
<div class="pdesc" id="pdesc">The whole map. Two documented roots feed the passage from the left; from the fork on one word — “foreknew” — two reception trails climb to today. The three faded roots are the ones we can only reconstruct.</div>

<div class="mapwrap">
  <svg class="trail" viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="The golden chain as a trail map">
    <line class="baseline" x1="40" y1="545" x2="{W-30}" y2="545"/>
    <text class="era" x="150" y="568">deep roots · pre-Christian</text>
    <text class="era" x="560" y="568">the letter · c. 57 AD</text>
    <text class="era" x="900" y="568">reception · 400–1700</text>
    <text class="era" x="1150" y="568" text-anchor="end">today</text>
    <g id="edges">{''.join(edge_svg)}</g>
    <g id="nodes">{''.join(node_svg)}</g>
  </svg>
</div>
<div class="legend">
  <span><span class="sw"></span>solid — a path we can document (attested)</span>
  <span><span class="sw re"></span>dashed — a path we can only reconstruct (what could have been)</span>
  <span style="color:var(--gold)">◆ the passage</span>
  <span style="color:var(--terra)">✳ the fork — one word, two readings</span>
</div>

<div id="panel">
  <div id="ph"><span id="pk">start here</span><span id="pt">Click a signpost to learn what stands there</span></div>
  <div id="pb">Every marker on the trail opens a plain-language note — what it is, whether the path to it is documented or reconstructed, and why it matters. Start at the golden landmark in the middle: <b>Romans 8:28–30</b>, where every trail meets.</div>
</div>

<a class="backlink" href="coding-lab.html">← back to the coding lab</a>
<p class="foot">HOW PRODUCED · design-SB, {sys.argv[0].split('/')[-1]} — bakeoff entry #2 (trail-map) for the golden-chain trace-tree interaction, per the researcher’s S150 direction (intuitive · paths-in-the-woods · orientation + context + click-to-learn) + Saquib’s schemas (time left→right; solid=what-we-know / dashed=what-could-have-been; named traced paths). Content is reading-SB’s golden-chain (Rom 8:28–30). SCHOLARLY SOURCES · the golden-chain trace-tree; Saquib’s situation-calculus + diffusion-network schemas; Poemage (linked-path highlighting). WHAT NEEDS VERIFICATION · candidate interaction concept for review; Saquib-schema-match still to confirm with him; Stage 6 = 0; nothing written to the DB.</p>
</div>
<script>
var NODES=__DATA__, TRAILS=__TRAILS__;
(function(){{
  var segs=[].slice.call(document.querySelectorAll('.seg'));
  var mks=[].slice.call(document.querySelectorAll('.mk[data-node]'));
  var pk=document.getElementById('pk'),pt=document.getElementById('pt'),pb=document.getElementById('pb');
  function esc(s){{return String(s).replace(/[&<>]/g,function(c){{return{{'&':'&amp;','<':'&lt;','>':'&gt;'}}[c];}});}}
  function showNode(id){{ var n=NODES[id]; if(!n) return;
    mks.forEach(function(m){{m.classList.toggle('sel',m.getAttribute('data-node')===id);}});
    pk.textContent={{root:'a root',pivot:'the passage',fork:'the fork',interp:'a reader',doctrine:'a doctrine',today:'today'}}[n.kind]||n.kind;
    pt.textContent=n.label; pb.innerHTML=n.d;
    document.getElementById('panel').scrollIntoView({{behavior:'smooth',block:'nearest'}});
  }}
  mks.forEach(function(m){{ var id=m.getAttribute('data-node');
    m.addEventListener('click',function(){{showNode(id);}});
    m.addEventListener('keydown',function(e){{if(e.key==='Enter'||e.key===' '){{e.preventDefault();showNode(id);}}}});
  }});
  // trail picker
  var pdesc=document.getElementById('pdesc');
  var descAll='The whole map. Two documented roots feed the passage from the left; from the fork on one word — “foreknew” — two reception trails climb to today. The three faded roots are the ones we can only reconstruct.';
  function pickTrail(t){{
    document.querySelectorAll('#pick .pbtn').forEach(function(b){{b.classList.toggle('on',b.getAttribute('data-t')===t);}});
    if(t==='all'){{ segs.forEach(function(s){{s.classList.remove('lit','dim');}}); mks.forEach(function(m){{m.classList.remove('dim');}}); pdesc.textContent=descAll; return; }}
    var mem=TRAILS[t].members_edges;
    segs.forEach(function(s){{ var on=mem.indexOf(s.getAttribute('data-trail'))>=0; s.classList.toggle('lit',on); s.classList.toggle('dim',!on); }});
    // dim nodes not touched by a lit segment
    var live={{}};
    __EDGEMAP__.forEach(function(e){{ if(mem.indexOf(e[2])>=0){{live[e[0]]=1;live[e[1]]=1;}} }});
    mks.forEach(function(m){{ var id=m.getAttribute('data-node'); m.classList.toggle('dim', id!=='today' && !live[id]); }});
    pdesc.textContent=TRAILS[t].label+' — '+TRAILS[t].desc;
  }}
  document.querySelectorAll('#pick .pbtn').forEach(function(b){{ b.onclick=function(){{pickTrail(b.getAttribute('data-t'));}}; }});
  showNode('pivot');
}})();
</script>
</body>
</html>"""
    HTML=HTML.replace("__DATA__",DATA).replace("__TRAILS__",TRAILJSON).replace("__EDGEMAP__",json.dumps([[a,b,t] for a,b,t,p in EDGES]))
    open(out,"w").write(HTML)
    print(f"wrote {out} — {len(NODES)} signposts, {len(EDGES)} trail segments, {len(TRAILS)} named trails")

if __name__=="__main__":
    build(sys.argv[1])
