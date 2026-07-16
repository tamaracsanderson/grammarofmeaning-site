#!/usr/bin/env python3
"""coordinate-space.html v2 — the reframe: a coordinate ANSWERS one question.

Per reading-SB's BATCH_to_designSB_coordinate_space_reframe_2026-07-15 (PR #2473):
fix the question ("Why is there suffering?") → spin a coordinate → it answers → the reader
watches the 6 axes develop into a stance → an "axes doing the work" line teaches what a
coordinate IS. Occupied → name the real thinkers (from the occupied-tuple data). Gap →
the generated answer, tagged GENERATED.

⚠️ ACQUISITION PANEL IS HELD (reading-SB's caveat, 2026-07-15): the first acquisition list was
generated WITHOUT a DB check and 2/6 were already in the corpus; at ~31% coded, an "empty"
coordinate is usually a CODING gap, not an acquisition gap. A CODE-IT vs ACQUIRE triage engine
is being built — the panel ships as a visible [pending] placeholder until then, and must never
assert "we don't have this".

Occupancy is VERIFIED per-stance against DATA_occupied_tuples (not asserted from the payload).

Usage: build_coordspace_v2.py <occupied_tuples.json> <OUTPUT.html>
"""
import sys, json

AX=[("epistemic-warrant","E","how it knows"),("ontological-commitment","O","what it takes to be real"),
    ("inferential-operation","M","how it moves"),("telos","T","what it is for"),
    ("stance","S","its posture"),("ground-world-relation","G","world-relation")]

QUESTION="Why is there suffering?"

# Payload A — reading-SB's generated stance-answers ($0 Sonnet, temp 0). Verbatim.
STANCES=[
 dict(key="augustinian", name="The Augustinian",
      coord=["revelation","personal-agentive","exegesis","salvation","reverent","creation"],
      work=["epistemic-warrant","inferential-operation"],
      workline="epistemic-warrant (revelation) + inferential-operation (exegesis)",
      answer="Suffering entered a good creation through the free turning of created wills away from God — Adam’s disobedience read in Genesis 3 and unfolded in Romans 5, not a metaphysical necessity but a personal-agentive rupture in a personal-agentive cosmos. What Scripture discloses (and reason cannot deduce) is that suffering is neither God’s design nor the world’s ground, but the wound the salvation-story is written to heal."),
 dict(key="buddhist", name="The Buddhist / contemplative",
      coord=["embodied-practice","dependent-arising","analogical-mapping","liberation","reparative","dependent-arising"],
      work=["ontological-commitment","epistemic-warrant"],
      workline="ontological-commitment (dependent-arising, doubled as ground) + epistemic-warrant (embodied-practice)",
      answer="Sit long enough and you watch it happen: a sensation arises, the mind grasps or pushes, and <i>dukkha</i> is the shape that grasping takes — the second and third noble truths are not doctrines but observations any practitioner can re-run. There is no substrate “suffering” behind the arising; it is the same knot the whole conditioned world is — which is exactly why loosening the knot is possible.",
      flag="design-SB flag for reading-SB: <b>dependent-arising</b> sits here in the <b>ontological-commitment</b> slot, but it is not among the 12 occupied O-values (it <i>is</i> an occupied <i>ground</i> value). The O menu holds 13 values and 12 are occupied — is this the legitimate 13th, or should O be <i>void</i> / <i>process-becoming</i> with dependent-arising as the ground? Not guessed here."),
 dict(key="materialist", name="The secular-materialist",
      coord=["observation","material","causal-explanation","knowledge-understanding","reductive","emergence"],
      work=["inferential-operation","stance"],
      workline="inferential-operation (causal-explanation) + stance (reductive)",
      answer="Suffering is what nociceptive signaling, limbic valuation, and predictive-error minimization <i>feel like from the inside</i> in a nervous system complex enough to model itself — an emergent property of evolved tissue, selected because organisms that could be hurt outlived ones that couldn’t. The “why” decomposes into proximate (neurochemistry) and ultimate (fitness gradients) causes; there is no residual “why” once those are given."),
 dict(key="apophatic", name="The apophatic mystic",
      coord=["mystical-union","apophatic","dialectical-negation","contemplation","reverent","manifestation"],
      work=["ontological-commitment","inferential-operation"],
      workline="ontological-commitment (apophatic) + inferential-operation (dialectical-negation)",
      answer="To say “there <i>is</i> suffering, and it has a <i>cause</i>” is already to have said too much — both terms belong to the naming-mind that the dark cloud undoes. In the manifestation, what appears as suffering is neither other than the One nor the same as it; the question is not answered but un-said, and the un-saying is itself the contemplative work."),
 dict(key="gap", name="★ The gap — no one holds this seat", star=True,
      coord=["embodied-practice","material","induction","liberation","reparative","unspecified"],
      work=["epistemic-warrant","ontological-commitment"],
      workline="epistemic-warrant (embodied-practice) + ontological-commitment (material)",
      answer="Suffering is what accumulates in a body — held tension, trauma imprint, dysregulated nervous system — and what you learn, from working with enough bodies including your own, is that it is <i>material all the way down</i> and yet responsive to practice. No cosmology is required and none is offered; the induction from ten thousand somatic sessions is simply that these patterns can be released, and release is the whole of liberation on offer.",
      rub="The rub: embodied-practice + liberation + reparative usually co-travel with dependent-arising or manifestation grounds; pairing them with <b>material</b> + <b>unspecified</b> names a live but <b>under-inhabited seat</b>."),
]

def build(data_path,out):
    d=json.load(open(data_path))
    keys=[a for a,_,_ in AX]
    occ={tuple(t["coord"][a] for a in keys):t for t in d["occupied_tuples"]}
    # VERIFY occupancy per stance against the real data (never assert from the payload)
    for s in STANCES:
        t=occ.get(tuple(s["coord"]))
        s["occupied"]= t is not None
        s["n"]= t["n"] if t else 0
        s["figs"]= t["figures"] if t else []
    JS=json.dumps({"AX":[{"k":k,"s":sh,"g":g} for k,sh,g in AX],"STANCES":STANCES,
                   "NOCC":d["n_distinct_occupied_tuples"],"POSSIBLE":d["possible_full_menu"],
                   "NFIG":d["n_figures"],"PCT":d["occupancy_pct_of_full_menu"],"Q":QUESTION}, ensure_ascii=False)

    HTML="""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>Why is there suffering? — the coordinate space</title>
<style>
  :root{--paper:#f7f2e7;--paper2:#fffdf7;--card:#fffefa;--ink:#26221a;--ink2:#5b5346;--ink3:#8a8172;--line:#e4dcc9;--line2:#d0c6ae;--moss:#4b6b46;--moss-d:#33502f;--gold:#b8892f;--gold-bg:#f6ecd4;--myst:#5b53a6;--myst-bg:#eae7f6;--terra:#9c3f37;--terra-bg:#f7e7e4;--mono:ui-monospace,"SF Mono",Menlo,Consolas,monospace;--sans:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,sans-serif;--serif:"Iowan Old Style","Palatino Linotype",Palatino,Georgia,serif;}
  @media (prefers-color-scheme:dark){:root{--paper:#14130f;--paper2:#1a1813;--card:#1e1b15;--ink:#ece7dc;--ink2:#b3aa98;--ink3:#847c6c;--line:#332f27;--line2:#423d31;--moss:#8fb884;--moss-d:#6c9a62;--gold:#e0b45f;--gold-bg:#2c2410;--myst:#a99ee6;--myst-bg:#221d38;--terra:#d98b80;--terra-bg:#301b18;}}
  *{box-sizing:border-box} body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);font-size:15.5px;line-height:1.62}
  .wrap{max-width:880px;margin:0 auto;padding:0 22px 80px}
  a{color:var(--moss-d)}
  header{padding:40px 0 10px}
  .banner{display:inline-block;font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;color:#fff;background:var(--myst);padding:4px 10px;border-radius:5px;margin-bottom:14px}
  .eyebrow{font-family:var(--mono);font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--gold);margin:0 0 10px}
  /* the fixed question */
  .q{font-family:var(--serif);font-weight:500;font-size:38px;line-height:1.1;margin:0 0 10px;letter-spacing:-.015em}
  .qsub{color:var(--ink2);font-size:16.5px;max-width:66ch;margin:0 0 6px}
  .qbar{display:flex;align-items:center;gap:12px;flex-wrap:wrap;background:var(--card);border:1px solid var(--line2);border-left:3px solid var(--gold);border-radius:0 12px 12px 0;padding:12px 16px;margin:16px 0 4px}
  .qbar .ql{font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink3)}
  .qbar .qv{font-family:var(--serif);font-size:17px;font-weight:600;color:var(--ink)}
  .qbar .qnote{font-family:var(--mono);font-size:10.5px;color:var(--ink3);margin-left:auto}
  .spin{font-family:var(--sans);font-size:15px;font-weight:600;padding:11px 26px;border-radius:12px;border:0;cursor:pointer;background:var(--moss);color:#fff}
  .spin:hover{filter:brightness(1.07)}
  .spinrow{display:flex;gap:10px;align-items:center;flex-wrap:wrap;margin:14px 0 4px}
  .dots{display:flex;gap:6px;margin-left:auto}.dot{width:9px;height:9px;border-radius:50%;background:var(--line2);cursor:pointer}.dot.on{background:var(--moss)}.dot.star{background:var(--myst)}
  /* coordinate chips */
  .coord{display:grid;grid-template-columns:repeat(6,1fr);gap:7px;margin:16px 0 2px}
  @media(max-width:660px){.coord{grid-template-columns:repeat(3,1fr)}}
  .cx{background:var(--paper2);border:1px solid var(--line2);border-radius:9px;padding:8px 9px;min-height:70px;transition:.2s}
  .cx .ax{font-family:var(--mono);font-size:8.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--ink3)}
  .cx .val{font-family:var(--serif);font-size:13px;color:var(--ink);margin-top:3px;line-height:1.2;word-break:break-word}
  .cx.work{border-color:var(--gold);background:var(--gold-bg);box-shadow:0 0 0 2px var(--gold-bg)}
  .cx.work .val{color:var(--gold);font-weight:700}
  .cx.work .ax{color:var(--gold)}
  /* the answer */
  .ansbox{background:var(--card);border:1px solid var(--line2);border-radius:14px;padding:0;overflow:hidden;margin:14px 0 0}
  .anshead{display:flex;align-items:center;gap:10px;padding:12px 18px;border-bottom:1px solid var(--line2);background:var(--paper2);flex-wrap:wrap}
  .anshead .nm{font-family:var(--serif);font-weight:600;font-size:18px}
  .tag{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.05em;text-transform:uppercase;padding:3px 9px;border-radius:20px;white-space:nowrap}
  .tag.occ{background:#e8efe2;color:var(--moss-d);border:1px solid var(--moss)}
  @media(prefers-color-scheme:dark){.tag.occ{background:#1c2a18;color:var(--moss)}}
  .tag.gen{background:var(--myst-bg);color:var(--myst);border:1px solid var(--myst)}
  .ans{padding:16px 20px;font-family:var(--serif);font-size:17px;line-height:1.55;color:var(--ink)}
  .work-line{margin:0;padding:11px 20px;background:var(--gold-bg);border-top:1px solid var(--line2);font-size:13.5px;color:var(--gold)}
  .work-line b{color:var(--gold);font-weight:700}
  .who{padding:13px 20px;border-top:1px solid var(--line2);font-size:14px;color:var(--ink2)}
  .who .f{display:inline-block;background:var(--paper2);border:1px solid var(--line2);border-radius:20px;padding:2px 9px;margin:3px 3px 0 0;font-size:12px}
  .rub{padding:12px 20px;border-top:1px solid var(--line2);background:var(--myst-bg);font-size:13.5px;color:var(--myst)}
  .flagbox{padding:12px 20px;border-top:1px solid var(--line2);background:var(--terra-bg);font-size:13px;color:var(--terra)}
  /* held acquisition panel */
  .held{margin:14px 0 0;border:1.5px dashed var(--line2);border-radius:12px;padding:14px 18px;background:var(--paper2);color:var(--ink3);font-size:13.5px}
  .held b{color:var(--ink2)}
  .held .hl{font-family:var(--mono);font-size:10px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--terra);border:1px solid var(--terra);border-radius:20px;padding:2px 8px;margin-right:8px}
  .foot{margin-top:36px;padding-top:16px;border-top:1px solid var(--line);font-family:var(--mono);font-size:11.5px;color:var(--ink3);line-height:1.7}
  .backlink{display:inline-block;margin:24px 0 0;font-family:var(--mono);font-size:12px}
  .ctx{font-size:13.5px;color:var(--ink2);margin:16px 0 0}
</style>
</head>
<body>
<div class="wrap">
<header>
  <span class="banner">candidate · Stage 6 = 0 · not a finding</span>
  <p class="eyebrow">the coding lab · the coordinate space</p>
  <h1 class="q" id="qtext">Why is there suffering?</h1>
  <p class="qsub">Every stance has an answer. Spin a coordinate — six axes: how it knows, what it takes to be real, how it moves, what it’s for, its posture, its world-relation — and watch them develop into one. The line at the bottom of each answer names <b>which axes did the work</b>. That’s what a coordinate <i>is</i>.</p>
  <div class="qbar"><span class="ql">the question</span><span class="qv" id="qv">Why is there suffering?</span><span class="qnote">fixed for now · a question-picker comes later</span></div>
</header>

<div class="spinrow">
  <button class="spin" id="spin">spin a coordinate →</button>
  <span style="font-family:var(--mono);font-size:11.5px;color:var(--ink3)">or click a dot</span>
  <span class="dots" id="dots"></span>
</div>

<div class="coord" id="coord"></div>
<div class="ansbox">
  <div class="anshead"><span class="nm" id="nm"></span><span id="tg"></span></div>
  <div class="ans" id="ans"></div>
  <p class="work-line" id="wl"></p>
  <div id="who"></div>
  <div id="rub"></div>
  <div id="flag"></div>
</div>
<div id="held"></div>

<p class="ctx" id="ctx"></p>

<a class="backlink" href="coding-lab.html">← back to the coding lab</a>
<p class="foot">HOW PRODUCED · design-SB, build_coordspace_v2.py — the reframe per reading-SB’s BATCH_to_designSB_coordinate_space_reframe_2026-07-15 (researcher: “shouldn’t they all answer a single question — see how the 6 coordinates develop into something”). Stance-answers are reading-SB’s payload (generated $0 Sonnet temp 0), reproduced verbatim. <b>Occupancy is verified per-stance against DATA_occupied_tuples — not asserted from the payload.</b> WHAT NEEDS VERIFICATION · (1) the real-stance answers are the model’s reconstruction — validate vs primary before any claim. (2) The <b>acquisition panel is HELD</b> per reading-SB’s caveat: the first list was generated without a DB check (2/6 were already in the corpus), and at ~31% coded an empty coordinate is usually a <b>coding</b> gap, not an acquisition gap — it ships only after the CODE-IT vs ACQUIRE triage engine + a DB check. (3) The gap answer is generated, never a finding. (4) One coordinate-value query is flagged inline for reading-SB. Stage 6 = 0; nothing written to the DB.</p>
</div>
<script>
var D=__DATA__;
(function(){
  var AX=D.AX,S=D.STANCES,i=0;
  var coord=document.getElementById('coord'),nm=document.getElementById('nm'),tg=document.getElementById('tg'),
      ans=document.getElementById('ans'),wl=document.getElementById('wl'),who=document.getElementById('who'),
      rub=document.getElementById('rub'),flag=document.getElementById('flag'),held=document.getElementById('held'),
      dots=document.getElementById('dots'),ctx=document.getElementById('ctx');
  function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  S.forEach(function(s,k){var d=document.createElement('span');d.className='dot'+(s.star?' star':'');d.onclick=function(){go(k);};dots.appendChild(d);});
  ctx.innerHTML='Of <b>'+D.POSSIBLE.toLocaleString()+'</b> coherent coordinates, <b>'+D.NOCC+'</b> are occupied by a real figure ('+D.PCT.toFixed(2)+'%). These five are a demonstrator set — the gap was chosen one axis off an occupied region, so it sits next to real minds rather than floating in incoherent space.';
  function go(k){
    i=k; var s=S[i];
    coord.innerHTML=AX.map(function(a,j){
      var isWork=s.work.indexOf(a.k)>=0;
      return '<div class="cx'+(isWork?' work':'')+'"><div class="ax">'+a.s+' · '+esc(a.k)+'</div><div class="val">'+esc(s.coord[j])+'</div></div>';
    }).join('');
    nm.textContent=s.name;
    if(s.occupied){ tg.innerHTML='<span class="tag occ">occupied · '+s.n+(s.n>1?' figures sit here':' figure sits here')+'</span>'; }
    else { tg.innerHTML='<span class="tag gen">generated · no figure at this coordinate</span>'; }
    ans.innerHTML=s.answer;
    wl.innerHTML='<b>The axes doing the work:</b> '+s.workline+' — the highlighted chips above. Change one and the answer changes shape.';
    if(s.occupied){
      var f=s.figs.slice(0,14).map(function(x){return '<span class="f">'+esc(x)+'</span>';}).join('');
      who.innerHTML='<div class="who"><b>Who sits here:</b> '+f+(s.figs.length>14?' <span style="color:var(--ink3)">+'+(s.figs.length-14)+' more</span>':'')+'</div>';
    } else {
      who.innerHTML='<div class="who"><b>No figure sits at this exact coordinate.</b> That does not mean the stance is absent from the world — only ~31% of the corpus is coded, so an empty seat is usually a <b>coding</b> gap, not a missing thinker.</div>';
    }
    rub.innerHTML = s.rub ? '<div class="rub">'+s.rub+'</div>' : '';
    flag.innerHTML = s.flag ? '<div class="flagbox">⚑ '+s.flag+'</div>' : '';
    // acquisition panel — HELD per reading-SB's caveat
    held.innerHTML = s.star ? '<div class="held"><span class="hl">acquisition panel · held</span><b>Who might sit here, and what to acquire</b> — deliberately not shipped yet. The first candidate list was generated from model knowledge <i>without checking the database</i>, and 2 of 6 names were already in the corpus. At ~31% coded, an empty coordinate is usually a <b>coding</b> gap, not an acquisition gap — so a panel asserting “we don’t have this” would be wrong. It ships once reading-SB’s <b>CODE-IT vs ACQUIRE</b> triage engine lands and each candidate is DB-checked.</div>' : '';
    dots.querySelectorAll('.dot').forEach(function(d,j){d.classList.toggle('on',j===i);});
  }
  document.getElementById('spin').onclick=function(){ var k; do{ k=Math.floor(Math.random()*S.length);}while(k===i&&S.length>1); go(k); };
  go(0);
})();
</script>
</body>
</html>"""
    HTML=HTML.replace("__DATA__",JS)
    open(out,"w").write(HTML)
    nocc=sum(1 for s in STANCES if s["occupied"])
    print(f"wrote {out} — {len(STANCES)} stances ({nocc} verified-occupied, {len(STANCES)-nocc} generated); acquisition panel HELD")

if __name__=="__main__":
    build(sys.argv[1],sys.argv[2])
