#!/usr/bin/env python3
"""VIZ-6 — "Why do we suffer?" the coordinate machine, end to end. Replaces the VIZ-6 vizslot (§D7, #d-occ).

Her most ambitious ask: one thing carrying seven parts (A–G). A guided walk anchored on one fixed
question. Every datum real (R1) and from a §4/arbiter source:
  · the pastiche + its fix (B)     : §D1 pastiche drawer (verbatim)
  · the Augustinian answer (C)     : coordinate-space payload / generate_stance_answers — revelation·personal-agentive·exegesis (34 figures)
  · the morphospace (D)            : LINK to VIZ-3, not rebuilt
  · the flywheel + triage gate (E) : §D7 (coding-gap / acquisition-gap / real-absence)
  · top-down/bottom-up (F)         : §F post-it — IRR183 → 186 → 187; 42% O-disagreement forced the 6th axis
  · open questions (G)             : §D4 point-cloud, §D4b voice_provenance, §F telos/stance-still-candidate
★ The honesty is the point: 275,184 coords · 365 occupied (0.13%) · 31% coded → an empty seat is
almost always a coding gap wearing a real-absence costume; the flywheel is a diagram, not a machine yet.
D172: "frame" here = a coordinate (the surviving sense). telos + stance marked candidate (never promoted).
"""
import sys, re, json

QUESTION = "Why do we suffer?"
# the Augustinian coordinate (real, coded — 34 figures sit here)
COORD = [
    ("E", "epistemic-warrant", "revelation", False, "how it knows"),
    ("O", "ontological-commitment", "personal-agentive", False, "what it takes to be real"),
    ("M", "inferential-operation", "exegesis", False, "how it moves"),
    ("T", "telos", "salvation", True, "what it is for"),
    ("S", "stance", "reverent", True, "its posture"),
    ("G", "ground-world-relation", "creation", False, "world-relation"),
]
WORK = ["epistemic-warrant", "inferential-operation"]  # the axes doing the work in the answer
ANSWER = ("Suffering entered a good creation through the free turning of created wills away from God — Adam's disobedience "
          "read in Genesis 3 and unfolded in Romans 5, not a metaphysical necessity but a personal-agentive rupture in a "
          "personal-agentive cosmos. What Scripture discloses (and reason cannot deduce) is that suffering is neither God's "
          "design nor the world's ground, but the wound the salvation-story is written to heal.")
PASTICHE = ("Augustine reads the conspicuous silence as itself a datum: <i>superbia</i> is precisely the disposition that "
            "occludes one's own loves from oneself. The addressee's uncertainty is therefore not exculpatory but symptomatic — "
            "pride hides the heart from itself. The <i>ordo amoris</i> does not ask 'do you feel love?' but 'is your love "
            "ordered rightly toward the good?'")
TRIAGE = [
    ("coding gap", "we hold the text; nobody has coded it", "CODE IT — free, we own it", "none — it's just work", "most of them", "code"),
    ("acquisition gap", "we don't hold the text; it exists", "SHOP — or a substitute if copyright bars the primary", "none — a purchase order", "some", "shop"),
    ("real absence", "coherent, but nobody has ever stood there", "GENERATE — and ask: why has no one thought this?", "the whole point", "the interesting one", "generate"),
]
CHAIN = [
    ("1 · top-down origin", "The base E/O/M reels are marked in the code, verbatim, as “the known values (researcher's list, S138).” Authored, not induced."),
    ("2 · IRR183 — taxonomy round", "Still top-down: five models reasoning about what axes should exist. Lock-with-changes — added telos, flagged stance, added E/O/M values unanimously."),
    ("3 · IRR186 — the bottom-up turn", "Triggered by real coding failures — an O-axis split-rate diagnostic on actual coded text. 5/5 PROCEED WITH RESTRUCTURING; no cohort endorsed the 8-value set. Root cause: O conflated what-is-real with how-it-relates-to-the-world."),
    ("4 · IRR187 — harder", "A bigger diagnostic: n=43, <b>42% O-disagreement</b>. Decompose O into substance-only + wire ground-world-relation as a 6th coordinate → Decision 168. <b>The 6th axis was forced by a measured failure, not designed.</b>"),
]
OPEN = [
    ("Copyright", "An in-copyright thinker (Merleau-Ponty) is seated from <b>attributed</b> quotes in secondary sources — included and tagged <code>voice_provenance = attributed</code>, never excluded."),
    ("A mind that changed", "A thinker who holds two things, or changed, is a <b>point-cloud</b>, not a point — Augustine legitimately occupies ≥3 (394 conditional → 396 → 426 unconditional). Multiplicity is the feature; the discipline is to distinguish it from coder error."),
    ("A frame that is two Es", "Some minds know two ways at once. Whether a coordinate can carry two epistemic-warrants, or must split into two frames, is open."),
    ("telos + stance are still candidate", "T and S were never promoted to locked. IRR183 added telos (unanimous) and flagged stance (4/5) pending a mini-round that never ran — yet both are used in the geometry. Marked candidate here, not settled."),
]

def build(page_path):
    DATA = json.dumps({
        "q": QUESTION,
        "coord": [{"k": k, "ax": ax, "v": v, "cand": cand, "gloss": g} for k, ax, v, cand, g in COORD],
        "work": WORK, "answer": ANSWER, "pastiche": PASTICHE,
        "triage": [{"kind": a, "means": b, "route": c, "value": d, "share": e, "cls": f} for a, b, c, d, e, f in TRIAGE],
        "chain": [{"h": a, "b": b} for a, b in CHAIN],
        "open": [{"q": a, "a": b} for a, b in OPEN],
        "possible": 275184, "occupied": 365, "coded_pct": 31,
    }, ensure_ascii=False)

    BLOCK = '''<div class="viz viz-6" id="viz-6">
<style>
.viz-6{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-6 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-6 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-6 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-6 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-6 .chip-cand{color:var(--terracotta)}
.viz-6 .qbar{display:flex;align-items:center;gap:10px;flex-wrap:wrap;border-left:3px solid var(--honey);background:var(--paper-2);border-radius:0 9px 9px 0;padding:9px 14px;margin:8px 0 12px}
.viz-6 .qbar .ql{font-family:var(--mono);font-size:9.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--ink-3)}
.viz-6 .qbar .qv{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-6 .honesty{border:1.5px solid var(--terracotta);border-radius:9px;background:var(--paper-2);padding:10px 13px;margin:0 0 14px;font-size:12.5px;color:var(--ink-2);line-height:1.55}
.viz-6 .honesty b{color:var(--terracotta)}
.viz-6 .stat{font-family:var(--serif);font-size:15px;color:var(--ink)}
.viz-6 .v6-tabs{display:flex;gap:3px;flex-wrap:wrap;border-bottom:2px solid var(--rule);margin:0 0 14px}
.viz-6 .v6-tab{font-family:var(--sans);font-size:12.5px;font-weight:600;padding:7px 11px;border:0;background:transparent;color:var(--ink-3);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px}
.viz-6 .v6-tab.on{color:var(--ink);border-bottom-color:var(--moss)}
.viz-6 .v6-tab .l{font-family:var(--mono);font-size:10px;color:var(--olive);margin-right:4px}
.viz-6 .v6-pane{display:none;animation:none}.viz-6 .v6-pane.on{display:block}
.viz-6 .pane-h{font-family:var(--serif);font-size:16px;color:var(--ink);margin:0 0 4px}
.viz-6 .pane-s{font-size:13px;color:var(--ink-2);margin:0 0 12px;max-width:80ch;line-height:1.55}
/* A — coordinate chips */
.viz-6 .coordrow{display:grid;grid-template-columns:repeat(6,1fr);gap:7px}
@media(max-width:660px){.viz-6 .coordrow{grid-template-columns:repeat(3,1fr)}}
.viz-6 .cx{background:var(--paper);border:1px solid var(--rule);border-radius:9px;padding:8px 9px;min-height:78px;position:relative}
.viz-6 .cx .ck{font-family:var(--mono);font-size:8.5px;color:var(--ink-3)}
.viz-6 .cx .cv{font-family:var(--serif);font-size:14px;color:var(--ink);margin-top:3px;line-height:1.2}
.viz-6 .cx .cg{font-size:9px;color:var(--ink-3);margin-top:4px}
.viz-6 .cx.work{border-color:var(--honey);background:var(--paper-2)}
.viz-6 .cx.work .cv{color:var(--honey);font-weight:700}
.viz-6 .cx .cand{position:absolute;top:5px;right:6px;font-family:var(--mono);font-size:7.5px;color:var(--terracotta);border:1px solid var(--terracotta);border-radius:20px;padding:0 5px}
.viz-6 .finding{border-left:3px solid var(--moss);background:var(--paper-2);border-radius:0 9px 9px 0;padding:10px 13px;margin:12px 0 0;font-size:12.5px;color:var(--ink-2);line-height:1.55}
.viz-6 .finding b{color:var(--ink)}
/* B — side by side */
.viz-6 .sbs{display:grid;grid-template-columns:1fr 1fr;gap:12px}
@media(max-width:720px){.viz-6 .sbs{grid-template-columns:1fr}}
.viz-6 .card{border:1px solid var(--rule);border-radius:10px;padding:12px 14px;background:var(--paper)}
.viz-6 .card.persona{border-color:var(--rule)}
.viz-6 .card.frame{border-color:var(--fern)}
.viz-6 .card .ct{font-family:var(--mono);font-size:10px;letter-spacing:.05em;text-transform:uppercase;margin-bottom:6px}
.viz-6 .card.persona .ct{color:var(--ink-3)}.viz-6 .card.frame .ct{color:var(--fern)}
.viz-6 .card .quote{font-family:var(--serif);font-size:13.5px;line-height:1.5;color:var(--ink);font-style:italic}
.viz-6 .card .verdict{font-size:11.5px;color:var(--ink-2);margin-top:9px;padding-top:8px;border-top:1px solid var(--rule-soft);line-height:1.5}
.viz-6 .card .verdict b{color:var(--ink)}
.viz-6 .card.persona .verdict b{color:var(--terracotta)}
.viz-6 .card.frame .verdict b{color:var(--fern)}
/* C — answer */
.viz-6 .answer{border:1px solid var(--fern);border-radius:10px;padding:14px 16px;background:var(--paper);font-family:var(--serif);font-size:16px;line-height:1.55;color:var(--ink)}
.viz-6 .workline{margin:10px 0 0;font-size:12.5px;color:var(--honey);font-family:var(--mono)}
.viz-6 .workline b{color:var(--honey)}
/* D — link */
.viz-6 .linkcard{border:1px dashed var(--rule);border-radius:10px;padding:14px 16px;background:var(--paper);text-align:center}
.viz-6 .linkcard a{font-family:var(--sans);font-size:14px;font-weight:600;color:var(--fern);text-decoration:none;border-bottom:1px solid var(--fern)}
/* E — flywheel */
.viz-6 .fly{display:flex;flex-direction:column;gap:0}
.viz-6 .fly-step{display:flex;align-items:center;gap:10px;padding:7px 0}
.viz-6 .fly-node{font-family:var(--mono);font-size:11px;padding:6px 11px;border-radius:7px;border:1px solid var(--rule);background:var(--paper);white-space:nowrap}
.viz-6 .fly-node.gate{border-color:var(--honey);background:var(--paper-2);color:var(--honey);font-weight:600}
.viz-6 .triage{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:6px 0}
@media(max-width:680px){.viz-6 .triage{grid-template-columns:1fr}}
.viz-6 .tri{border:1px solid var(--rule);border-radius:9px;padding:9px 11px;background:var(--paper)}
.viz-6 .tri.code{border-left:3px solid var(--fern)}.viz-6 .tri.shop{border-left:3px solid var(--honey)}.viz-6 .tri.generate{border-left:3px solid var(--terracotta)}
.viz-6 .tri .tk{font-family:var(--mono);font-size:10px;font-weight:600}
.viz-6 .tri.code .tk{color:var(--fern)}.viz-6 .tri.shop .tk{color:var(--honey)}.viz-6 .tri.generate .tk{color:var(--terracotta)}
.viz-6 .tri .tm{font-size:11px;color:var(--ink-2);margin-top:3px;line-height:1.4}
.viz-6 .tri .tr{font-family:var(--mono);font-size:9.5px;color:var(--ink);margin-top:5px}
.viz-6 .tri .tv{font-size:9.5px;color:var(--ink-3);margin-top:3px;font-style:italic}
.viz-6 .brake{border-left:3px solid var(--terracotta);background:var(--paper-2);border-radius:0 9px 9px 0;padding:10px 13px;margin:10px 0 0;font-size:12.5px;color:var(--ink-2);line-height:1.55}
.viz-6 .brake b{color:var(--terracotta)}
/* F — chain */
.viz-6 .chain{position:relative;margin:4px 0 0;padding-left:16px;border-left:2px solid var(--rule)}
.viz-6 .clink{margin:0 0 12px;position:relative}
.viz-6 .clink::before{content:"";position:absolute;left:-21px;top:4px;width:8px;height:8px;border-radius:50%;background:var(--olive)}
.viz-6 .clink.forced::before{background:var(--terracotta)}
.viz-6 .clink .ch{font-family:var(--mono);font-size:11px;font-weight:600;color:var(--ink)}
.viz-6 .clink .cb{font-size:12px;color:var(--ink-2);margin-top:3px;line-height:1.5}
/* G — open */
.viz-6 .opens{display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(max-width:720px){.viz-6 .opens{grid-template-columns:1fr}}
.viz-6 .open{border:1px solid var(--rule-soft);border-radius:8px;padding:9px 11px;background:var(--paper)}
.viz-6 .open .ok{font-family:var(--mono);font-size:10.5px;color:var(--olive);font-weight:600}
.viz-6 .open .oa{font-size:12px;color:var(--ink-2);margin-top:3px;line-height:1.5}
.viz-6 .viz-src{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin:14px 0 0;line-height:1.65}
@media(prefers-reduced-motion:reduce){.viz-6 *{transition:none!important;animation:none!important}}
</style>
  <div class="viz-h">
    <span class="viz-id">VIZ-6</span>
    <span class="viz-t">The coordinate machine, end to end</span>
    <span class="chip chip-cand">candidate</span>
  </div>
  <div class="qbar"><span class="ql">the fixed question</span><span class="qv">Why do we suffer?</span></div>
  <div class="honesty"><b>The honesty is the point.</b> Of <span class="stat">275,184</span> coherent coordinates, <span class="stat">365</span> are occupied by a coded figure (0.13%). But only <b>31% of the roster is coded</b> — so an empty seat is almost always a <b>coding gap wearing a real-absence costume</b>. The thesis-grade finding (unoccupied-but-coherent) is <b>not available yet</b>, and the flywheel below is a diagram, not a machine — its triage engine is spec'd but the coding-vs-acquisition ratio has not come back.</div>

  <div class="v6-tabs" role="tablist" id="v6-tabs">
    <button type="button" class="v6-tab on" data-p="a"><span class="l">A</span>six → a frame</button>
    <button type="button" class="v6-tab" data-p="b"><span class="l">B</span>frame vs persona</button>
    <button type="button" class="v6-tab" data-p="c"><span class="l">C</span>it answers</button>
    <button type="button" class="v6-tab" data-p="d"><span class="l">D</span>where it sits</button>
    <button type="button" class="v6-tab" data-p="e"><span class="l">E</span>the flywheel</button>
    <button type="button" class="v6-tab" data-p="f"><span class="l">F</span>found, not designed</button>
    <button type="button" class="v6-tab" data-p="g"><span class="l">G</span>open questions</button>
  </div>

  <div class="v6-pane on" id="q-a">
    <div class="pane-h">A · Six coordinates become a frame</div>
    <div class="pane-s">A <b>frame</b> is a location in a six-axis space — not a name. Here is the coordinate the Augustinian answer is generated <i>from</i>. The two axes that will do the visible work in the answer are lit.</div>
    <div class="coordrow" id="v6-coord"></div>
    <div class="finding"><b>Two axes are still candidate.</b> <code>telos</code> and <code>stance</code> were never promoted to locked (IRR183 flagged stance for a mini-round that never ran) — they are marked candidate above, and used in the geometry with that caveat.</div>
  </div>

  <div class="v6-pane" id="q-b">
    <div class="pane-h">B · How a frame differs from a persona</div>
    <div class="pane-s">This is the whole reason the coordinate exists. Ask the model “what would Augustine say” and it returns a <b>persona</b> — good, but unfalsifiable and untraceable. Ask a <b>frame</b> — a mind that knows by revelation, holds a personal-agentive ground, reasons by exegesis — and the answer is traceable to stated commitments. Same figure, two objects.</div>
    <div class="sbs">
      <div class="card persona"><div class="ct">persona — “what would Augustine say?”</div><div class="quote" id="v6-pastiche"></div><div class="verdict">It is <b>good</b>. It is also <b>unfalsifiable</b>, and it is what the model already believes “Augustine” sounds like — nothing in it is traceable to a coded commitment, and nothing could come out differently.</div></div>
      <div class="card frame"><div class="ct">frame — the coordinate answers</div><div class="quote" id="v6-frameans"></div><div class="verdict"><b>Traceable.</b> Change the epistemic-warrant from revelation to observation and the answer must change shape. Augustine is a <b>location</b> in the space, not a voice to imitate.</div></div>
    </div>
  </div>

  <div class="v6-pane" id="q-c">
    <div class="pane-h">C · The frame answers the gap</div>
    <div class="pane-s">The Augustinian coordinate — <code>revelation · personal-agentive · exegesis · salvation · reverent · creation</code>, where <b>34 real figures sit</b> — answering the fixed question.</div>
    <div class="answer" id="v6-answer"></div>
    <div class="workline" id="v6-workline"></div>
  </div>

  <div class="v6-pane" id="q-d">
    <div class="pane-h">D · Where the frame sits in the morphospace</div>
    <div class="pane-s">A frame is a point you can locate among all the others. This coordinate lives in the space rendered above — the Augustinian seat is in the dense religious region (dim-1 low).</div>
    <div class="linkcard"><a href="#viz-3">↑ See it in VIZ-3 — the 3D morphospace, 483 points</a><div style="font-size:11px;color:var(--ink-3);margin-top:6px">Not rebuilt here; the same geometry, one section up.</div></div>
  </div>

  <div class="v6-pane" id="q-e">
    <div class="pane-h">E · The acquisition flywheel — with its triage gate</div>
    <div class="pane-s">The loop you described — gaps → acquire → fill → find more gaps — is real, but it has <b>no brake</b>. An uncoded figure and an absent figure look identical from the map, so without a gate the flywheel <b>always says “go shopping.”</b> The gate is the fix.</div>
    <div class="fly">
      <div class="fly-step"><span class="fly-node">read the empty seats</span><span style="color:var(--ink-3)">→</span><span class="fly-node gate">◆ triage each seat</span></div>
    </div>
    <div class="triage" id="v6-triage"></div>
    <div class="brake"><b>Status, honestly:</b> the triage engine is spec'd and was spawned, but the coding-gap-vs-acquisition ratio it was meant to report <b>has not come back</b>. Until it does, this is a diagram, not a machine — and it is why coding is prioritised over acquisition (TG-4 reverses the shopping priority).</div>
  </div>

  <div class="v6-pane" id="q-f">
    <div class="pane-h">F · Top-down origin, bottom-up re-cutting</div>
    <div class="pane-s">Are the axes designed or discovered? <b>Both, in sequence</b> — and the honest label is “top-down origin, bottom-up re-cutting.” The chain is citable, and the strongest evidence the frame measures something real is that the <b>6th axis was forced by a measured failure, not designed</b>.</div>
    <div class="chain" id="v6-chain"></div>
  </div>

  <div class="v6-pane" id="q-g">
    <div class="pane-h">G · The open questions</div>
    <div class="pane-s">Four the coordinate frame raises and has not closed.</div>
    <div class="opens" id="v6-open"></div>
  </div>

  <p class="viz-src">Sources — the pastiche + its fix: §D1 (verbatim). The Augustinian answer: the coordinate-space payload (generated $0 Sonnet, temp 0) at <code>revelation·personal-agentive·exegesis·salvation·reverent·creation</code> (34 figures). The flywheel + triage: §D7. The IRR183→186→187 chain: §F. Open questions: §D4, §D4b, §F. Morphospace: VIZ-3 (not rebuilt). Occupancy: 365 / 275,184; 31% coded. Stage&nbsp;6&nbsp;=&nbsp;0.</p>
<script>
(function(){
  var D=__DATA__;
  function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  // A — coordinate
  document.getElementById('v6-coord').innerHTML=D.coord.map(function(c){
    var work=D.work.indexOf(c.ax)>=0;
    return '<div class="cx'+(work?' work':'')+'">'+(c.cand?'<span class="cand">candidate</span>':'')
      +'<div class="ck">'+c.k+' · '+esc(c.ax)+'</div><div class="cv">'+esc(c.v)+'</div><div class="cg">'+esc(c.gloss)+'</div></div>';
  }).join('');
  // B
  document.getElementById('v6-pastiche').innerHTML='“'+D.pastiche+'”';
  document.getElementById('v6-frameans').innerHTML='“'+D.answer+'”';
  // C
  document.getElementById('v6-answer').textContent=D.answer;
  document.getElementById('v6-workline').innerHTML='<b>The axes doing the work:</b> '+D.work.join(' + ')+' — revelation discloses what reason cannot deduce, and exegesis reads it out of Genesis 3 / Romans 5. Change either and the answer changes shape.';
  // E
  document.getElementById('v6-triage').innerHTML=D.triage.map(function(t){
    return '<div class="tri '+t.cls+'"><div class="tk">'+esc(t.kind)+' · '+t.share+'</div><div class="tm">'+esc(t.means)+'</div><div class="tr">→ '+esc(t.route)+'</div><div class="tv">thesis value: '+esc(t.value)+'</div></div>';
  }).join('');
  // F
  document.getElementById('v6-chain').innerHTML=D.chain.map(function(c,i){
    return '<div class="clink'+(i===3?' forced':'')+'"><div class="ch">'+c.h+'</div><div class="cb">'+c.b+'</div></div>';
  }).join('');
  // G
  document.getElementById('v6-open').innerHTML=D.open.map(function(o){
    return '<div class="open"><div class="ok">'+esc(o.q)+'</div><div class="oa">'+o.a+'</div></div>';
  }).join('');
  // tabs
  document.querySelectorAll('#v6-tabs .v6-tab').forEach(function(t){ t.onclick=function(){
    document.querySelectorAll('#v6-tabs .v6-tab').forEach(function(x){x.classList.toggle('on',x===t);});
    var p=t.getAttribute('data-p');
    document.querySelectorAll('.viz-6 .v6-pane').forEach(function(pane){pane.classList.toggle('on',pane.id==='q-'+p);});
  };});
})();
</script>
</div>'''
    block = BLOCK.replace("__DATA__", DATA)
    h = open(page_path, encoding="utf-8").read()
    slot = re.compile(r'<div class="vizslot"[^>]*>\s*<div class="vs-h"><span class="vs-id">VIZ-6</span>.*?</div>\s*</div>', re.S)
    built = re.compile(r'<div class="viz viz-6" id="viz-6">.*?</script>\s*</div>', re.S)
    if slot.search(h):
        h2 = slot.sub(lambda _: block, h, count=1)
    elif built.search(h):
        h2 = built.sub(lambda _: block, h, count=1)
    else:
        raise AssertionError("neither VIZ-6 vizslot nor built block matched")
    open(page_path, "w", encoding="utf-8").write(h2)
    left = h2.count('class="vizslot"')
    print(f"VIZ-6 installed · 7 panels (A-G) · triage {len(TRIAGE)} · chain {len(CHAIN)} · open {len(OPEN)} · slots left: {left}")

if __name__ == "__main__":
    build(sys.argv[1])
