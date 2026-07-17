#!/usr/bin/env python3
"""VIZ-4 — the schema, then the table. Replaces the VIZ-4 vizslot (§C5, #c-trees).

Her structural insight: "a data table would be a lot easier, maybe with a pivot table?" +
"clear ID and field names, and a tab that has definitions". Three tabs: Schema · Data · Definitions.

Every datum real (R1):
  · 485 fan nodes : DATA_full_fan_she_loves_you_1963.csv (id·parent·depth·position·move·concept·gate)
  · 48 world-line rows : DATA_altworld_she_loves_you_1963.csv
  · fan family + widths + fan-vs-worldline finding : SPA §C5 (the arbiter)
D172: the CSV gate value "IN" is rendered as "in-paradigm"; 485 = 366 in-paradigm + 119 barred.
Definitions tab carries in-paradigm + beyond-paradigm.
Ink rule: the entire fan + world-lines are GENERATED (what-could-have-been, gated). One ink;
within it, in-paradigm (kept) vs barred (pruned) by treatment. No ACTUAL/ATTESTED present to mix.

Usage: build_viz4.py <fan.csv> <alt.csv> <method-canonical.html>
"""
import sys, re, csv, json

def build(fan_path, alt_path, page_path):
    fan = list(csv.DictReader(open(fan_path, encoding="utf-8")))
    alt = list(csv.DictReader(open(alt_path, encoding="utf-8")))
    # fan rows, typed
    F = [{"id": int(r["id"]), "parent": int(r["parent"]), "depth": int(r["depth"]),
          "pos": r["position"], "move": r["move"], "concept": r["concept"],
          "gate": "in-paradigm" if r["gate"] == "IN" else "barred"} for r in fan]
    nin = sum(1 for r in F if r["gate"] == "in-paradigm")
    nbar = len(F) - nin
    from collections import Counter
    by_depth = dict(sorted(Counter(r["depth"] for r in F).items()))
    widths = [by_depth.get(i, 0) for i in range(max(by_depth) + 1)]
    # world-lines
    from collections import defaultdict
    wls = defaultdict(list)
    for r in alt:
        wls[r["world_line"]].append(r)
    WL = []
    for k in sorted(wls, key=int):
        rs = sorted(wls[k], key=lambda x: int(x["position_index"]))
        WL.append({"wl": k, "verdict": rs[0]["terminal_verdict"],
                   "moves": [{"pos": r["position"], "move": r["move"], "concept": r["governing_concept"],
                              "birth": r["concept_birth"], "gate": ("in-paradigm" if r["era_gate"]=="IN-FRAME" else ("barred" if r["era_gate"]=="BARRED" else r["era_gate"])),
                              "fork": r["is_deciding_fork"]} for r in rs]})
    nconv = sum(1 for w in WL if w["verdict"] == "CONVERGE")
    DATA = json.dumps({"F": F, "WL": WL, "nin": nin, "nbar": nbar, "widths": widths,
                       "nconv": nconv, "ntotal": len(F)}, ensure_ascii=False)

    BLOCK = '''<div class="viz viz-4" id="viz-4">
<style>
.viz-4{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-4 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-4 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-4 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-4 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-4 .chip-cand{color:var(--terracotta)}.viz-4 .chip-gen{color:var(--olive)}
.viz-4 .viz-lede{font-size:14.5px;color:var(--ink-2);margin:6px 0 12px;max-width:82ch;line-height:1.6}
.viz-4 .v4-tabs{display:flex;gap:4px;border-bottom:2px solid var(--rule);margin:0 0 14px}
.viz-4 .v4-tab{font-family:var(--sans);font-size:13px;font-weight:600;padding:8px 14px;border:0;background:transparent;color:var(--ink-3);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px}
.viz-4 .v4-tab.on{color:var(--ink);border-bottom-color:var(--moss)}
.viz-4 .v4-pane{display:none}.viz-4 .v4-pane.on{display:block}
/* schema pane */
.viz-4 .ladder{display:flex;align-items:flex-end;gap:10px;margin:6px 0 4px;overflow-x:auto;padding-bottom:4px}
.viz-4 .rung{display:flex;flex-direction:column;align-items:center;gap:5px;min-width:64px}
.viz-4 .rung .bar{width:100%;background:var(--olive);border-radius:4px 4px 0 0;min-height:6px;opacity:.8}
.viz-4 .rung .rl{font-family:var(--mono);font-size:9px;color:var(--ink-3)}
.viz-4 .rung .rn{font-family:var(--mono);font-size:12px;color:var(--ink);font-weight:600}
.viz-4 .rung.wall{position:relative}
.viz-4 .wallnote{font-family:var(--mono);font-size:10px;color:var(--terracotta);border-left:2px dashed var(--terracotta);padding-left:8px;margin:8px 0 0}
.viz-4 .finding{border-left:3px solid var(--moss);background:var(--paper-2);border-radius:0 9px 9px 0;padding:10px 13px;margin:12px 0;font-size:13px;color:var(--ink-2);line-height:1.55}
.viz-4 .finding b{color:var(--ink)}
.viz-4 .schemas{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0 0}
@media(max-width:720px){.viz-4 .schemas{grid-template-columns:1fr}}
.viz-4 .schema{border:1px solid var(--rule);border-radius:9px;padding:11px 13px;background:var(--paper)}
.viz-4 .schema h4{font-family:var(--serif);font-size:14.5px;margin:0 0 3px;color:var(--ink)}
.viz-4 .schema .sn{font-size:11.5px;color:var(--ink-3);margin:0 0 8px}
.viz-4 .fld{display:flex;gap:8px;font-size:11.5px;padding:3px 0;border-top:1px solid var(--rule-soft)}
.viz-4 .fld .fk{font-family:var(--mono);font-size:10.5px;color:var(--olive);white-space:nowrap;min-width:96px}
.viz-4 .fld .fd{color:var(--ink-2)}
/* data pane */
.viz-4 .v4-filters{display:flex;gap:6px;flex-wrap:wrap;align-items:center;margin:0 0 10px}
.viz-4 .fchip{font-family:var(--mono);font-size:10.5px;padding:4px 10px;border-radius:20px;border:1px solid var(--rule);background:var(--paper);color:var(--ink-2);cursor:pointer}
.viz-4 .fchip.on{background:var(--moss);border-color:var(--moss);color:var(--paper)}
.viz-4 .fchip.bar.on{background:var(--terracotta);border-color:var(--terracotta)}
.viz-4 .fcount{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin-left:auto}
.viz-4 .v4-tablewrap{max-height:420px;overflow:auto;border:1px solid var(--rule);border-radius:9px}
.viz-4 table.v4-t{width:100%;border-collapse:collapse;font-size:11.5px}
.viz-4 table.v4-t th{position:sticky;top:0;background:var(--paper-2);font-family:var(--mono);font-size:9px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-3);text-align:left;padding:6px 8px;border-bottom:1px solid var(--rule);z-index:1}
.viz-4 table.v4-t td{padding:5px 8px;border-bottom:1px solid var(--rule-soft);vertical-align:top}
.viz-4 table.v4-t td.mono{font-family:var(--mono);font-size:10.5px;color:var(--ink-3)}
.viz-4 table.v4-t tr.barred{background:repeating-linear-gradient(45deg,transparent,transparent 6px,var(--paper-2) 6px,var(--paper-2) 7px)}
.viz-4 table.v4-t tr.barred td{color:var(--ink-3)}
.viz-4 .gtag{font-family:var(--mono);font-size:9px;padding:1px 6px;border-radius:20px;white-space:nowrap}
.viz-4 .gtag.in{color:var(--fern);border:1px solid var(--fern)}
.viz-4 .gtag.bar{color:var(--terracotta);border:1px dashed var(--terracotta)}
.viz-4 .why{font-style:italic;color:var(--terracotta);font-size:10.5px}
/* world-lines */
.viz-4 .wl-h{font-family:var(--serif);font-size:15px;margin:16px 0 4px;color:var(--ink)}
.viz-4 .wl{border:1px solid var(--rule);border-radius:9px;padding:9px 11px;margin:7px 0;background:var(--paper)}
.viz-4 .wl.conv{border-left:3px solid var(--fern)}.viz-4 .wl.div{border-left:3px solid var(--rule)}
.viz-4 .wl-top{display:flex;align-items:baseline;gap:8px;font-size:12px}
.viz-4 .wl-v{font-family:var(--mono);font-size:9.5px;padding:1px 7px;border-radius:20px}
.viz-4 .wl-v.conv{color:var(--fern);border:1px solid var(--fern)}.viz-4 .wl-v.div{color:var(--ink-3);border:1px solid var(--rule)}
.viz-4 .wl-path{font-size:11.5px;color:var(--ink-2);margin-top:5px;line-height:1.5}
.viz-4 .wl-path .fork{color:var(--terracotta);font-weight:600}
.viz-4 .shape{border:1px solid var(--fern);border-radius:9px;background:var(--paper-2);padding:10px 13px;margin:10px 0 0;font-size:12.5px;color:var(--ink-2)}
.viz-4 .shape b{color:var(--fern)}
/* definitions pane */
.viz-4 .defs{display:grid;grid-template-columns:1fr 1fr;gap:10px}
@media(max-width:720px){.viz-4 .defs{grid-template-columns:1fr}}
.viz-4 .def{border:1px solid var(--rule-soft);border-radius:8px;padding:9px 11px;background:var(--paper)}
.viz-4 .def .dk{font-family:var(--mono);font-size:10.5px;color:var(--olive);font-weight:600}
.viz-4 .def .dd{font-size:12px;color:var(--ink-2);margin-top:3px;line-height:1.5}
.viz-4 .def.para{border-color:var(--terracotta)}
.viz-4 .def.para .dk{color:var(--terracotta)}
.viz-4 .viz-src{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin:12px 0 0;line-height:1.65}
@media(prefers-reduced-motion:reduce){.viz-4 *{transition:none!important}}
</style>
  <div class="viz-h">
    <span class="viz-id">VIZ-4</span>
    <span class="viz-t">The schema, then the table — 485 nodes you can actually read</span>
    <span class="chip chip-cand">candidate</span>
    <span class="chip chip-gen">GENERATED · the fan is what-could-have-been, gated</span>
  </div>
  <p class="viz-lede">You asked for a table, not another tree — and you were right about <i>why</i>: the fan doubles at every level (<b id="v4-widths"></b>), so past ~5 levels it stops being drawable. <b>The fan is a dataset; only a world-line is a drawing.</b> Three tabs: the <b>schema</b> (the fields and how they relate), the <b>data</b> (all 485 rows, filterable — <b id="v4-split"></b>), and <b>definitions</b> (every field and every value, traceable).</p>

  <div class="v4-tabs" role="tablist">
    <button type="button" class="v4-tab on" data-p="schema">Schema</button>
    <button type="button" class="v4-tab" data-p="data">Data</button>
    <button type="button" class="v4-tab" data-p="defs">Definitions</button>
  </div>

  <div class="v4-pane on" id="p-schema">
    <div class="ladder" id="v4-ladder"></div>
    <div class="wallnote" id="v4-wallnote"></div>
    <div class="finding"><b>Why this is a table, not a tree.</b> The full fan is the whole admissible space — split at every fork, ~3 children each. A <b>world-line</b> is one coherent path through it. Same object, two views — and that is the distinction that unblocked the problem: “we can’t draw 2,000 leaves” stops mattering once the fan is held as data and only a single world-line is drawn.</div>
    <div class="schemas">
      <div class="schema">
        <h4>substitution fan <span style="font-family:var(--mono);font-size:10px;color:var(--olive)">GENERATED</span></h4>
        <div class="sn">one row per generated move-state · <code>DATA_full_fan_she_loves_you_1963.csv</code> · 485 rows</div>
        <div class="fld"><span class="fk">id</span><span class="fd">the node’s own number</span></div>
        <div class="fld"><span class="fk">parent</span><span class="fd">the id it forked from (−1 = the root) — this is the tree edge</span></div>
        <div class="fld"><span class="fk">depth</span><span class="fd">how many forks deep (0…5)</span></div>
        <div class="fld"><span class="fk">position</span><span class="fd">which move-slot it fills (M1′…M6′)</span></div>
        <div class="fld"><span class="fk">move</span><span class="fd">the generated move, in words (paraphrase)</span></div>
        <div class="fld"><span class="fk">concept</span><span class="fd">the governing concept + its birth-era — this is what the gate checks</span></div>
        <div class="fld"><span class="fk">gate</span><span class="fd"><b>in-paradigm</b> (kept) or <b>barred</b> (pruned)</span></div>
      </div>
      <div class="schema">
        <h4>world-line <span style="font-family:var(--mono);font-size:10px;color:var(--olive)">GENERATED</span></h4>
        <div class="sn">one committed state per position — a single path through the fan · <code>DATA_altworld_she_loves_you_1963.csv</code> · 48 rows = 6 × 8</div>
        <div class="fld"><span class="fk">world_line</span><span class="fd">which of the 6 paths</span></div>
        <div class="fld"><span class="fk">position</span><span class="fd">M1′…M8′ along the path</span></div>
        <div class="fld"><span class="fk">move</span><span class="fd">the committed move at that position</span></div>
        <div class="fld"><span class="fk">governing_concept</span><span class="fd">the concept driving that move</span></div>
        <div class="fld"><span class="fk">concept_birth</span><span class="fd">when the concept became available</span></div>
        <div class="fld"><span class="fk">era_gate</span><span class="fd">in-paradigm / barred for this path</span></div>
        <div class="fld"><span class="fk">is_deciding_fork</span><span class="fd">the fork that sends it to CONVERGE or DIVERGE</span></div>
        <div class="fld"><span class="fk">terminal_verdict</span><span class="fd">does it land on the sung ending? CONVERGE / DIVERGE</span></div>
      </div>
    </div>
  </div>

  <div class="v4-pane" id="p-data">
    <div class="v4-filters">
      <span style="font-family:var(--mono);font-size:10px;color:var(--ink-3)">gate:</span>
      <button type="button" class="fchip gate on" data-g="all">all</button>
      <button type="button" class="fchip gate" data-g="in-paradigm">in-paradigm</button>
      <button type="button" class="fchip gate bar" data-g="barred">barred</button>
      <span style="font-family:var(--mono);font-size:10px;color:var(--ink-3);margin-left:8px">depth:</span>
      <span id="v4-depths"></span>
      <span class="fcount" id="v4-fcount"></span>
    </div>
    <div class="v4-tablewrap">
      <table class="v4-t"><thead><tr><th>id</th><th>parent</th><th>depth</th><th>position</th><th>move</th><th>concept</th><th>gate</th></tr></thead><tbody id="v4-tbody"></tbody></table>
    </div>
    <div class="finding" style="margin-top:12px"><b>The 119 barred rows are the gate working, not failures.</b> Every one is barred because its governing concept was <b>born after 1963</b> — a concept the song’s world could not hold (the <b>era gate</b>). “codependency (1980s)”, “online-validation (2000s)”, “Maslow flourishing (late 1960s)”. The era of a fill is data; the gate reads it and prunes what is <i>beyond-paradigm</i>.</div>

    <div class="wl-h">The 6 world-lines — <span id="v4-conv"></span> converge on the sung ending</div>
    <div id="v4-wls"></div>
    <div class="shape"><b>The shape the convergent ones share</b> — and it is not a coincidence: substituting “healed” for “hurt” removes the injury at the mouth of the fan, so any path that lands on the apology must re-introduce it. Every convergent world-line runs <b>healed → the healer withdraws → a new hurt → apology for the withdrawal</b>.</div>
  </div>

  <div class="v4-pane" id="p-defs">
    <div class="defs">
      <div class="def para"><span class="dk">in-paradigm</span><div class="dd">A generated value the text’s world <i>can</i> hold — its governing concept was available in the text’s era. Kept in the fan. (The gate’s pass state; renders as “IN” in the raw CSV.)</div></div>
      <div class="def para"><span class="dk">beyond-paradigm</span><div class="dd">A value the text’s world <i>cannot</i> hold at all — anachronistic to the era, or outside its conceptual universe. A wall, not a jump: flagged, not coded. Every barred row here is beyond-paradigm on the era gate.</div></div>
      <div class="def"><span class="dk">gate</span><div class="dd">The prune step (S8): era-availability × path-coherence. This CSV records the net outcome (in-paradigm / barred); the era component is legible in each concept’s birth-year.</div></div>
      <div class="def"><span class="dk">substitution fan</span><div class="dd">GENERATED. The whole admissible space of forks from one substitution — a dataset, not a drawing. 485 nodes = 366 in-paradigm + 119 barred.</div></div>
      <div class="def"><span class="dk">world-line</span><div class="dd">GENERATED. One committed path through the fan — the only member of the family that is a <i>drawing</i>. 6 × 8 = 48 rows.</div></div>
      <div class="def"><span class="dk">CONVERGE / DIVERGE</span><div class="dd">A world-line’s terminal verdict: does it re-land on the song’s sung ending (CONVERGE) or end elsewhere (DIVERGE)? Computed as forward-fan ∩ backward-funnel — currently eyeballed, per §E S9.</div></div>
      <div class="def"><span class="dk">depth · parent · id</span><div class="dd">The tree structure: <code>parent</code> points to the id a node forked from; <code>depth</code> is how many forks deep. Per level the fan is 1 → 4 → 12 → 36 → 108 → 324.</div></div>
      <div class="def"><span class="dk">position</span><div class="dd">Which move-slot a node fills — M1′…M8′ (the prime marks a generated, not-actual, move).</div></div>
    </div>
  </div>

  <p class="viz-src">Sources — 485 fan nodes: <code>DATA_full_fan_she_loves_you_1963.csv</code> (366 in-paradigm / 119 barred; per-level 1→4→12→36→108→324). 48 world-line rows: <code>DATA_altworld_she_loves_you_1963.csv</code> (6 × 8; 3 CONVERGE). Family names + the fan-vs-world-line finding: §C5. D172: the CSV gate value “IN” renders as “in-paradigm.” Only era-barring is separable in this file (see report). Paraphrase only; no lyric. Stage&nbsp;6&nbsp;=&nbsp;0.</p>
<script>
(function(){
  var D=__DATA__;
  document.getElementById('v4-widths').textContent=D.widths.join(' → ');
  document.getElementById('v4-split').textContent=D.nin+' in-paradigm · '+D.nbar+' barred';
  document.getElementById('v4-conv').textContent=D.nconv+' of '+D.WL.length;
  function esc(s){return String(s).replace(/[&<>]/g,function(c){return{'&':'&amp;','<':'&lt;','>':'&gt;'}[c];});}
  // ladder
  var maxw=Math.max.apply(null,D.widths);
  document.getElementById('v4-ladder').innerHTML=D.widths.map(function(w,i){
    var h=Math.round(10+ (w/maxw)*120);
    return '<div class="rung'+(i>=5?' wall':'')+'"><div class="rn">'+w+'</div><div class="bar" style="height:'+h+'px"></div><div class="rl">depth '+i+'</div></div>';
  }).join('');
  document.getElementById('v4-wallnote').innerHTML='⟶ at depth 5 the level already holds <b>'+D.widths[5]+'</b> nodes; depth 6 would be ~972. Past here the tree is unreadable — which is the whole point: it is <b>held as a dataset</b>, and only a single world-line is ever drawn.';
  // tabs
  document.querySelectorAll('.v4-tab').forEach(function(t){ t.onclick=function(){
    document.querySelectorAll('.v4-tab').forEach(function(x){x.classList.toggle('on',x===t);});
    var p=t.getAttribute('data-p');
    document.querySelectorAll('.v4-pane').forEach(function(pane){pane.classList.toggle('on',pane.id==='p-'+p);});
  };});
  // depth filter chips
  var depths=[]; D.F.forEach(function(r){if(depths.indexOf(r.depth)<0)depths.push(r.depth);}); depths.sort();
  var gate='all', depth='all';
  document.getElementById('v4-depths').innerHTML='<button type="button" class="fchip depth on" data-d="all">all</button>'+depths.map(function(d){return '<button type="button" class="fchip depth" data-d="'+d+'">'+d+'</button>';}).join('');
  function whyBar(concept){ var m=concept.match(/\\(([^)]+)\\)/); return m?('born '+m[1]+' — after 1963'):'anachronistic to 1963'; }
  function renderTable(){
    var rows=D.F.filter(function(r){ return (gate==='all'||r.gate===gate) && (depth==='all'||r.depth==(depth|0)); });
    var cap=rows.slice(0,600);
    document.getElementById('v4-tbody').innerHTML=cap.map(function(r){
      var g=r.gate==='in-paradigm'?'<span class="gtag in">in-paradigm</span>':'<span class="gtag bar">barred</span>';
      var concept=esc(r.concept)+(r.gate==='barred'?' <span class="why">'+whyBar(r.concept)+'</span>':'');
      return '<tr class="'+(r.gate==='barred'?'barred':'')+'"><td class="mono">'+r.id+'</td><td class="mono">'+(r.parent<0?'root':r.parent)+'</td><td class="mono">'+r.depth+'</td><td class="mono">'+esc(r.pos)+'</td><td>'+esc(r.move)+'</td><td>'+concept+'</td><td>'+g+'</td></tr>';
    }).join('');
    document.getElementById('v4-fcount').textContent='showing '+rows.length+' of '+D.ntotal+(rows.length>600?' (first 600 drawn)':'');
  }
  document.querySelectorAll('.fchip.gate').forEach(function(b){ b.onclick=function(){ gate=b.getAttribute('data-g'); document.querySelectorAll('.fchip.gate').forEach(function(x){x.classList.toggle('on',x===b);}); renderTable(); };});
  document.getElementById('v4-depths').querySelectorAll('.fchip.depth').forEach(function(b){ b.onclick=function(){ depth=b.getAttribute('data-d'); document.querySelectorAll('.fchip.depth').forEach(function(x){x.classList.toggle('on',x===b);}); renderTable(); };});
  renderTable();
  // world-lines
  document.getElementById('v4-wls').innerHTML=D.WL.map(function(w){
    var conv=w.verdict==='CONVERGE';
    var path=w.moves.map(function(m){ return (m.fork==='yes'?'<span class="fork">':'<span>')+esc(m.move)+'</span>'; }).join(' <span style="color:var(--ink-3)">→</span> ');
    return '<div class="wl '+(conv?'conv':'div')+'"><div class="wl-top"><b>world-line '+w.wl+'</b><span class="wl-v '+(conv?'conv':'div')+'">'+w.verdict+'</span></div><div class="wl-path">'+path+'</div></div>';
  }).join('');
})();
</script>
</div>'''
    block = BLOCK.replace("__DATA__", DATA)
    h = open(page_path, encoding="utf-8").read()
    slot = re.compile(r'<div class="vizslot"[^>]*>\s*<div class="vs-h"><span class="vs-id">VIZ-4</span>.*?</div>\s*</div>', re.S)
    built = re.compile(r'<div class="viz viz-4" id="viz-4">.*?</script>\s*</div>', re.S)
    if slot.search(h):
        h2 = slot.sub(lambda _: block, h, count=1)
    elif built.search(h):
        h2 = built.sub(lambda _: block, h, count=1)
    else:
        raise AssertionError("neither VIZ-4 vizslot nor built block matched")
    open(page_path, "w", encoding="utf-8").write(h2)
    left = h2.count('class="vizslot"')
    print(f"VIZ-4 installed · {len(F)} fan rows ({nin} in-paradigm / {nbar} barred) · {len(WL)} world-lines ({nconv} converge) · slots left: {left}")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], sys.argv[3])
