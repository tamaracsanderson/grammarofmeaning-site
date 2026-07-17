#!/usr/bin/env python3
"""VIZ-2 — the process flow: the row growing, step by step. Replaces the VIZ-2 vizslot (§E, #e-steps).

Her two asks, built as ONE thing: "a process diagram like engine.html" + "show step by step how this is
done in a data table, so we see how it expands, or what fields are added… it'll keep us more honest."
Each step lights up and writes its NAMED fields into a row you watch fill. The row IS the diagram.

Every datum from a §4 file (R1 — nothing invented):
  · steps · names · field names · statuses : the §E table in method-canonical.html (the arbiter)
  · M1's values          : field_ed/negative_space_pilot_8move_she_loves_you_2026-07-10.md (paraphrase only)
  · sitz · paradigm      : SPA §A7 (inherited down the scale — "a move's sitz = its nearest enclosing narrator's sitz")
  · the 2×2 cell         : SPA §B2
  · alternative_kind     : SPA §B5 (the CSV's "contrary of hurt" → CONTRARY)
  · M1' + gate + verdict : DATA_altworld_she_loves_you_1963.csv · DATA_full_fan_she_loves_you_1963.csv
Fields the pilot never recorded are marked NOT RECORDED — never invented. That is the honesty device §E asks for.
"""
import sys, re, json

UNREC = "— not recorded"

STEPS = [
 dict(s="S0", name="SEGMENT", does="the text → a sequence of moves", status="no rule exists", hole=True,
      hole_txt="<b>S0 has no rule.</b> We assert the song is 8 moves and the golden chain is 5, but no segmentation procedure is stated — so no second coder can reproduce the units, and <b>every reliability number downstream is conditional on units nobody specified</b>. This is why S4's unitizing κ≈0.20 while its cell-classification κ=1.0: coders agree what a gap <i>is</i> and disagree where one <i>ends</i>. S0 is the root, and the highest-value missing piece in the method.",
      fields=[("move_id","M1"),("move_index","1"),("paraphrase","you did something that hurt her")]),
 dict(s="S1", name="DECOMPOSE", does="each move → the CORE-7 grammar", status="IRR168v2 · ~92%",
      fields=[("operation","hurt (past)"),("type","narrate"),("voice",UNREC),("agent","you"),
              ("substrate","her"),("outcome","the wound"),("narrator","the friend")],
      note="The pilot's table has <b>no voice column</b> — S1 claims seven fields and recorded six. The row shows the hole rather than filling it."),
 dict(s="S2", name="SITUATE", does="attach the surround — inherited from the enclosing scale", status="IRR169v2 · ~97%",
      fields=[("sitz","a 1963 pop single; a friend brokering a reconciliation"),("paradigm","romantic-love-as-reconcilable")],
      note="Inherited, not re-declared: a move's sitz = its nearest enclosing narrator's sitz (§A7)."),
 dict(s="S3", name="CONNECT", does="moves → edges; the edges → the meta-move", status="IRR179 · not piloted",
      fields=[("edge_type","FEEDS"),("from_move","M1"),("to_move","M2"),("contact_status","n/a — within-text")],
      note="contact_status does the disqualifying work on <i>cross-text</i> pairs; on a within-text FEEDS edge there is nothing to disqualify."),
 dict(s="S4", name="DETECT", does="place every position on the 2×2; seer-tag the gaps", status="κ=1.0 cell / κ≈0.20 unit",
      fields=[("position","why-you-hurt-her"),("visibility","opaque"),("salience","in-focus"),("cell","★ THE GAP"),("seer","reader")]),
 dict(s="S5", name="CLASSIFY", does="the door, then the flavor", status="D160 · κ=1.0 door",
      fields=[("door","FILL"),("flavor","omitted")]),
 dict(s="S6", name="RESOLVE", does="who closes the gap — the text, or history?", status="field is mis-cut", hole=True,
      hole_txt="<b>S6's field is mis-cut</b> (your catch): <code>resolution</code> mixes <i>who closed it</i> with <i>what we could do about it</i>. “Generatable” is a capability, not a resolution. The pilot ran its three-way resolution on M4's gaps, not M1's — so this row is doubly empty: the field is wrong <i>and</i> unrecorded here.",
      fields=[("resolution",UNREC),("resolved_by",UNREC)]),
 dict(s="S7", name="GENERATE", does="run the engines: fills stay in the state, substitutes jump it", status="1 of 2 engines built",
      fields=[("candidate","you healed her"),("alternative_kind","CONTRARY"),("u_tier",UNREC),("citation",UNREC)],
      sub=True,
      note="The <b>fill engine is a spec, not code</b> — the one that makes the branches-not-taken that stay in the state. The built one is the substitute engine, which is what you see here."),
 dict(s="S8", name="GATE", does="prune by era-availability × path-coherence", status="IRR196 · gate 2 weak",
      fields=[("concept","contrary of hurt"),("concept_birth","perennial"),("era_gate","in-paradigm"),("path_coherence",UNREC)],
      note="Gate 1 (era) is real and computed. Gate 2 (path-coherence) is the weak one — the SPA says so."),
 dict(s="S9", name="CONVERGE", does="forward-fan ∩ backward-funnel", status="funnel not built", hole=True,
      hole_txt="<b>S9's second half doesn't exist.</b> The backward funnel is unbuilt, so the intersection is <b>eyeballed, not computed</b> — the 3-of-6 converging world-lines were read off by hand. The method doc says so itself: “the intersection should be COMPUTED (state-matching) once both directions run, not eyeballed.”",
      fields=[("world_line","1"),("terminal_verdict","CONVERGE")]),
]

# the S7 substitution — only `operation` is swapped; the other six are equally substitutable (her framing)
CORE7 = [("operation","hurt (past)","healed",True),("type","narrate",None,False),("voice",UNREC,None,False),
         ("agent","you",None,False),("substrate","her",None,False),("outcome","the wound",None,False),
         ("narrator","the friend",None,False)]

def build_block():
    chips = "".join(
        f'<button type="button" class="v2-step{" hole" if st.get("hole") else ""}" data-i="{i}">'
        f'<span class="sid">{st["s"]}</span><span class="snm">{st["name"]}</span>'
        f'{"<span class=chole>⚠</span>" if st.get("hole") else ""}</button>'
        for i, st in enumerate(STEPS))
    core7 = "".join(
        f'<div class="c7{" swapped" if sw else ""}"><div class="c7f">{f}</div>'
        f'<div class="c7v">{v}</div>'
        + (f'<div class="c7n">→ <b>{nv}</b></div>' if nv else '<div class="c7n subtle">equally substitutable — not run here</div>')
        + '</div>'
        for f, v, nv, sw in CORE7)
    data = json.dumps([{k: st.get(k) for k in ("s","name","does","status","fields","hole","hole_txt","note","sub")} for st in STEPS], ensure_ascii=False)
    return chips, core7, data

BLOCK = '''<div class="viz viz-2" id="viz-2">
<style>
/* VIZ-2 — scoped. Locked gom.css tokens only; palette never redefined. */
.viz-2{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-2 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-2 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-2 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-2 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-2 .chip-cand{color:var(--terracotta)}.viz-2 .chip-actual{color:var(--fern)}
.viz-2 .viz-lede{font-size:14.5px;color:var(--ink-2);margin:6px 0 12px;max-width:82ch;line-height:1.6}
/* stepper */
.viz-2 .v2-steps{display:flex;gap:5px;flex-wrap:wrap;margin:0 0 10px}
.viz-2 .v2-step{display:flex;flex-direction:column;align-items:flex-start;gap:1px;font-family:var(--sans);padding:5px 9px;border-radius:7px;border:1px solid var(--rule);background:var(--paper);cursor:pointer;position:relative;min-width:78px}
.viz-2 .v2-step .sid{font-family:var(--mono);font-size:9px;color:var(--ink-3)}
.viz-2 .v2-step .snm{font-size:10.5px;font-weight:600;color:var(--ink-2);letter-spacing:.02em}
.viz-2 .v2-step.hole{border-color:var(--terracotta);border-style:dashed}
.viz-2 .v2-step .chole{position:absolute;top:3px;right:5px;font-size:9px;color:var(--terracotta)}
.viz-2 .v2-step.on{background:var(--moss);border-color:var(--moss)}
.viz-2 .v2-step.on .sid,.viz-2 .v2-step.on .snm{color:var(--paper)}
.viz-2 .v2-step.on.hole{background:var(--terracotta);border-color:var(--terracotta);border-style:solid}
.viz-2 .v2-step.done{background:var(--paper-2)}
.viz-2 .v2-ctl{display:flex;gap:8px;align-items:center;flex-wrap:wrap;margin:0 0 12px}
.viz-2 .v2-btn{font-family:var(--sans);font-size:12.5px;font-weight:600;padding:6px 13px;border-radius:8px;border:1px solid var(--rule);background:var(--paper);color:var(--ink);cursor:pointer}
.viz-2 .v2-btn.primary{background:var(--moss);color:var(--paper);border-color:var(--moss)}
.viz-2 .v2-btn:disabled{opacity:.4;cursor:default}
.viz-2 .v2-count{font-family:var(--mono);font-size:11px;color:var(--ink-3);margin-left:auto}
/* the step readout */
.viz-2 .v2-now{border:1px solid var(--rule);border-left:3px solid var(--moss);border-radius:0 9px 9px 0;background:var(--paper);padding:10px 14px;margin:0 0 10px}
.viz-2 .v2-now.hole{border-left-color:var(--terracotta)}
.viz-2 .v2-now-h{display:flex;align-items:baseline;gap:8px;flex-wrap:wrap}
.viz-2 .v2-now-h b{font-family:var(--mono);font-size:12px;letter-spacing:.04em;color:var(--ink)}
.viz-2 .v2-now-h .does{font-size:12.5px;color:var(--ink-2)}
.viz-2 .v2-now-h .st{font-family:var(--mono);font-size:9.5px;margin-left:auto;padding:1px 7px;border-radius:20px;border:1px solid var(--sage);color:var(--ink-3);white-space:nowrap}
.viz-2 .v2-now-h .st.bad{border-color:var(--terracotta);color:var(--terracotta)}
.viz-2 .v2-note{font-size:12px;color:var(--ink-2);margin:7px 0 0;line-height:1.55}
.viz-2 .v2-hole{font-size:12.5px;color:var(--terracotta);background:var(--paper-2);border-radius:7px;padding:8px 11px;margin:7px 0 0;line-height:1.55}
/* THE ROW */
.viz-2 .v2-rowwrap{overflow-x:auto;border:1px solid var(--rule);border-radius:9px;background:var(--paper)}
.viz-2 .v2-row{display:flex;gap:0;min-width:min-content;padding:0}
.viz-2 .cellgrp{border-right:1px dashed var(--rule);padding:7px 8px;display:flex;gap:5px}
.viz-2 .cellgrp:last-child{border-right:0}
.viz-2 .cell{min-width:92px;max-width:150px;border:1px solid var(--rule-soft);border-radius:6px;padding:4px 6px;background:var(--paper-3)}
.viz-2 .cell .f{font-family:var(--mono);font-size:8px;color:var(--ink-3);letter-spacing:.03em;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.viz-2 .cell .v{font-size:11px;color:var(--ink);margin-top:2px;line-height:1.3}
.viz-2 .cell.fresh{border-color:var(--fern);background:var(--paper-2)}
.viz-2 .cell.unrec{border-style:dashed;border-color:var(--terracotta)}
.viz-2 .cell.unrec .v{color:var(--terracotta);font-family:var(--mono);font-size:9.5px}
.viz-2 .grplab{font-family:var(--mono);font-size:8px;color:var(--ink-3);writing-mode:vertical-rl;transform:rotate(180deg);align-self:center;letter-spacing:.06em}
.viz-2 .rowempty{padding:14px;font-size:12.5px;color:var(--ink-3);font-family:var(--mono)}
/* the S7 substitution panel */
.viz-2 .v2-sub{border:1px solid var(--honey);border-radius:9px;background:var(--paper);padding:10px 12px;margin:10px 0 0}
.viz-2 .v2-sub-h{font-size:12.5px;color:var(--ink-2);margin-bottom:8px}
.viz-2 .v2-sub-h b{color:var(--ink)}
.viz-2 .c7row{display:grid;grid-template-columns:repeat(7,1fr);gap:5px}
@media(max-width:820px){.viz-2 .c7row{grid-template-columns:repeat(3,1fr)}}
.viz-2 .c7{border:1px solid var(--rule-soft);border-radius:6px;padding:5px 6px;background:var(--paper-3)}
.viz-2 .c7.swapped{border-color:var(--honey);border-width:1.6px;background:var(--paper-2)}
.viz-2 .c7f{font-family:var(--mono);font-size:8px;color:var(--ink-3)}
.viz-2 .c7v{font-size:10.5px;color:var(--ink-2);margin-top:2px}
.viz-2 .c7n{font-size:9.5px;margin-top:3px;color:var(--honey)}
.viz-2 .c7n.subtle{color:var(--ink-3);font-style:italic}
.viz-2 .v2-layers{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:9px 0 0}
@media(max-width:680px){.viz-2 .v2-layers{grid-template-columns:1fr}}
.viz-2 .lyr{font-size:11.5px;line-height:1.5;border-radius:7px;padding:8px 10px}
.viz-2 .lyr b{font-family:var(--mono);font-size:10.5px}
.viz-2 .lyr-jump{background:var(--paper-2);border:1px solid var(--honey);color:var(--ink-2)}
.viz-2 .lyr-jump b{color:var(--honey)}
.viz-2 .lyr-wall{background:var(--paper-2);border:1px solid var(--terracotta);color:var(--ink-2)}
.viz-2 .lyr-wall b{color:var(--terracotta)}
.viz-2 .holes{margin:12px 0 0;border-left:3px solid var(--terracotta);background:var(--paper-2);border-radius:0 9px 9px 0;padding:10px 13px;font-size:12.5px;color:var(--ink-2)}
.viz-2 .holes b{color:var(--terracotta)}
.viz-2 .viz-src{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin:12px 0 0;line-height:1.65}
@media(prefers-reduced-motion:reduce){.viz-2 *{transition:none!important;animation:none!important}}
</style>
  <div class="viz-h">
    <span class="viz-id">VIZ-2</span>
    <span class="viz-t">The process flow — the row growing, step by step</span>
    <span class="chip chip-cand">candidate</span>
    <span class="chip chip-actual">ACTUAL — the move we really coded</span>
  </div>
  <p class="viz-lede">Your two notes, built as one thing: a walk through <b>S0→S9</b> where each step lights up and <b>writes its named fields into a row you watch fill</b>. The row <i>is</i> the diagram — a step that cannot name the field it writes is not a step. Run on the real move we coded (<b>M1</b>), not a made-up one. Three steps are <b class="holeword">broken</b>, and the row shows which: <b>the gaps are the finding</b>.</p>

  <div class="v2-steps" id="v2-steps">__CHIPS__</div>
  <div class="v2-ctl">
    <button type="button" class="v2-btn" id="v2-prev">◀ back</button>
    <button type="button" class="v2-btn primary" id="v2-next">write the next step ▶</button>
    <button type="button" class="v2-btn" id="v2-reset">reset</button>
    <span class="v2-count" id="v2-count"></span>
  </div>

  <div class="v2-now" id="v2-now"></div>
  <div class="v2-rowwrap"><div class="v2-row" id="v2-row"><div class="rowempty">the row is empty — press “write the next step” and watch it fill</div></div></div>
  <div id="v2-subwrap"></div>

  <div class="holes">
    <b>The three holes the table exposed</b> — all three were invisible in the prose version, and none is drawn as a clean pipeline.
    <b>S0</b> has no segmentation rule (so every κ downstream is conditional on units nobody specified) · <b>S6</b>'s field is mis-cut (resolution mixes <i>who closed it</i> with <i>what we could do about it</i>) · <b>S9</b>'s backward funnel is unbuilt (the intersection is eyeballed, not computed).
  </div>

  <p class="viz-src">Sources — steps, names, field names and statuses: the §E table above. M1's values: <code>negative_space_pilot_8move_she_loves_you_2026-07-10.md</code> (paraphrase only; no lyric). sitz · paradigm: §A7 (inherited). The 2×2 cell: §B2. alternative_kind: §B5. M1′, concept, era_gate, world_line, terminal_verdict: <code>DATA_altworld_she_loves_you_1963.csv</code> + <code>DATA_full_fan_she_loves_you_1963.csv</code> (485 nodes · 366 IN / 119 BARRED; 3 of 6 world-lines converge). Fields the pilot never recorded are marked <b>— not recorded</b>, never invented. Stage&nbsp;6&nbsp;=&nbsp;0.</p>
<script>
(function(){
  var S=__DATA__, CORE7HTML=__C7__;
  var steps=document.getElementById('v2-steps'), row=document.getElementById('v2-row'),
      now=document.getElementById('v2-now'), cnt=document.getElementById('v2-count'),
      subw=document.getElementById('v2-subwrap');
  var i=-1;
  function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  function render(){
    Array.prototype.forEach.call(steps.children,function(b,j){
      b.classList.toggle('on',j===i); b.classList.toggle('done',j<i);
    });
    // the row: every field written up to and including step i
    if(i<0){ row.innerHTML='<div class="rowempty">the row is empty — press “write the next step” and watch it fill</div>'; }
    else{
      var html='';
      for(var k=0;k<=i;k++){
        var st=S[k], cells='';
        st.fields.forEach(function(f){
          var unrec=f[1].indexOf('not recorded')>=0;
          cells+='<div class="cell'+(k===i?' fresh':'')+(unrec?' unrec':'')+'"><div class="f">'+esc(f[0])+'</div><div class="v">'+esc(f[1])+'</div></div>';
        });
        html+='<div class="cellgrp"><span class="grplab">'+st.s+'</span>'+cells+'</div>';
      }
      row.innerHTML=html;
      var fresh=row.querySelector('.cell.fresh'); if(fresh) fresh.scrollIntoView({block:'nearest',inline:'nearest'});
    }
    // the step readout
    if(i<0){ now.className='v2-now'; now.innerHTML='<div class="v2-now-h"><b>not started</b><span class="does">ten steps; each one writes named fields, or it isn’t a step</span></div>'; }
    else{
      var st=S[i];
      now.className='v2-now'+(st.hole?' hole':'');
      var h='<div class="v2-now-h"><b>'+st.s+' · '+st.name+'</b><span class="does">'+st.does+'</span>'
           +'<span class="st'+(st.hole?' bad':'')+'">'+esc(st.status)+'</span></div>';
      if(st.note) h+='<p class="v2-note">'+st.note+'</p>';
      if(st.hole) h+='<div class="v2-hole">⚠ '+st.hole_txt+'</div>';
      now.innerHTML=h;
    }
    subw.innerHTML = (i>=0 && S[i].sub) ? '<div class="v2-sub"><div class="v2-sub-h"><b>The substitution runs on one slot — but every slot could generate.</b> Here only <b>operation</b> is swapped (<i>hurt</i> → <i>healed</i>), which is the illustration, not a limit of the grammar. The other six are marked as equally substitutable so the picture cannot imply otherwise.</div><div class="c7row">'+CORE7HTML+'</div><div class="v2-layers"><span class="lyr lyr-jump"><b>state-jump</b> — a SUBSTITUTE moves to a neighbouring move <i>inside the same paradigm</i> (S7). It voids the premise, so it does not complete this state — it starts a different one.</span><span class="lyr lyr-wall"><b>beyond-paradigm</b> — a value the world of the text cannot hold at all is a <i>wall, not a jump</i>: flagged, not coded. The era-gate (S8) is what decides <b>in-paradigm</b> vs <b>barred</b>.</span></div></div>' : '';
    var total=0; for(var k=0;k<=i&&i>=0;k++) total+=S[k].fields.length;
    cnt.textContent = (i<0?'0':(i+1))+' / '+S.length+' steps · '+total+' fields written';
    document.getElementById('v2-prev').disabled=(i<0);
    document.getElementById('v2-next').disabled=(i>=S.length-1);
  }
  Array.prototype.forEach.call(steps.children,function(b,j){ b.onclick=function(){ i=j; render(); }; });
  document.getElementById('v2-next').onclick=function(){ if(i<S.length-1){i++;render();} };
  document.getElementById('v2-prev').onclick=function(){ if(i>=0){i--;render();} };
  document.getElementById('v2-reset').onclick=function(){ i=-1; render(); };
  render();
})();
</script>
</div>'''

def build(path):
    chips, core7, data = build_block()
    block = BLOCK.replace("__CHIPS__", chips).replace("__DATA__", data).replace("__C7__", json.dumps(core7))
    h = open(path, encoding="utf-8").read()
    slot = re.compile(r'<div class="vizslot"[^>]*>\s*<div class="vs-h"><span class="vs-id">VIZ-2</span>.*?</div>\s*</div>', re.S)
    built = re.compile(r'<div class="viz viz-2" id="viz-2">.*?</script>\s*</div>', re.S)
    if slot.search(h):
        h2 = slot.sub(lambda _: block, h, count=1)
    elif built.search(h):
        h2 = built.sub(lambda _: block, h, count=1)   # idempotent re-render of an already-built VIZ-2
    else:
        raise AssertionError("neither VIZ-2 vizslot nor built block matched")
    open(path, "w", encoding="utf-8").write(h2)
    nf = sum(len(s["fields"]) for s in STEPS)
    left = h2.count('class="vizslot"')
    holes = sum(1 for s in STEPS if s.get('hole'))
    print(f"VIZ-2 installed · {len(STEPS)} steps · {nf} fields · {holes} holes marked · slots left: {left}")

if __name__ == "__main__":
    build(sys.argv[1])
