#!/usr/bin/env python3
"""
build_treedraw.py — VIZ-7 "The fan, drawn — and the six world-lines to M8".

Milestones (d) + (c) of the tree-revamp brief, from ONE shared substrate:
  (d) the radial/DAG draw of the substitution fan — the Saquib money shot (§4).
  (c) the six world-lines read as full-sentence chains to M8, predecessors inline (§2c).

Self-contained SVG radial layout computed in-page (NO cytoscape / D3 / CDN — R7 / CSP).
Inserted into §C5 (#c-trees), after VIZ-4, before #d-frame.

DATA (arbiter): substrate_treedraw.json, built from the two canonical CSVs
  (DATA_full_fan_she_loves_you_1963.csv · DATA_altworld_she_loves_you_1963.csv).

RULES: R1 — the fan is drawn to its REAL depth (M6'/depth-5); the M7'-M8' fan (~2000
nodes) is shown as an explicit NOT-YET-GENERATED hole, never fabricated. The 6 world-lines
reach M8 because that data is real (48 rows). R2/R4 — all GENERATED ink, tagged GENERATED
on its face; barred branches in a distinct treatment, never mixed with in-paradigm. R6 —
gom tokens only, colour never the only channel (fill+shape+dash+text), scrolls in its own
container, prefers-reduced-motion respected. R7 — self-contained, $0.
"""
import json, sys, pathlib, re

HERE = pathlib.Path(__file__).resolve().parent
SUB = json.loads((HERE / "substrate_treedraw.json").read_text())
HTML = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")

DATA_JSON = json.dumps(SUB, ensure_ascii=False, separators=(",", ":"))
M = SUB["meta"]

SECTION = '''<!-- ══ VIZ-7 TREE-DRAW (built) ══ -->
<div class="viz viz-7" id="viz-7">
<style>
.viz-7{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-7 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-7 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-7 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-7 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-7 .chip-gen{color:var(--olive)}
.viz-7 .viz-lede{font-size:14.5px;color:var(--ink-2);margin:6px 0 12px;max-width:82ch;line-height:1.6}
/* TL;DR card (brief §3) */
.viz-7 .v7-tldr{border:1px solid var(--rule);border-left:4px solid var(--olive);border-radius:0 10px 10px 0;background:var(--paper);padding:12px 15px;margin:2px 0 16px}
.viz-7 .v7-tldr-h{display:flex;align-items:baseline;gap:9px;margin-bottom:6px}
.viz-7 .v7-tldr-k{font-family:var(--mono);font-size:10.5px;font-weight:700;letter-spacing:.08em;color:var(--paper);background:var(--olive);padding:2px 9px;border-radius:5px}
.viz-7 .v7-tldr-sub{font-size:12px;color:var(--ink-3);font-style:italic}
.viz-7 .v7-beats{margin:0;padding-left:18px;display:grid;gap:6px}
.viz-7 .v7-beats li{font-size:13.5px;color:var(--ink-2);line-height:1.5}
.viz-7 .v7-box{font-family:var(--mono);font-size:.85em;background:var(--paper-2);padding:1px 6px;border-radius:4px;color:var(--moss)}
/* tabs */
.viz-7 .v7-tabs{display:flex;gap:4px;border-bottom:2px solid var(--rule);margin:0 0 12px}
.viz-7 .v7-tab{font-family:var(--sans);font-size:13px;font-weight:600;padding:8px 14px;border:0;background:transparent;color:var(--ink-3);cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-2px}
.viz-7 .v7-tab.on{color:var(--ink);border-bottom-color:var(--moss)}
.viz-7 .v7-pane{display:none}.viz-7 .v7-pane.on{display:block}
/* radial */
.viz-7 .v7-legend{display:flex;gap:16px;flex-wrap:wrap;align-items:center;font-size:12px;color:var(--ink-2);margin:0 0 8px}
.viz-7 .v7-lg{display:flex;align-items:center;gap:6px}
.viz-7 .v7-sw{width:13px;height:13px;flex:none;border-radius:50%}
.viz-7 .v7-sw-in{background:var(--fern)}
.viz-7 .v7-sw-bar{background:transparent;border:1.5px dashed var(--terracotta)}
.viz-7 .v7-sw-root{background:var(--honey)}
.viz-7 .v7-stage{position:relative;overflow:auto;border:1px solid var(--rule);border-radius:9px;background:var(--paper);max-width:100%}
.viz-7 svg.v7-svg{display:block;margin:0 auto;max-width:100%;height:auto;touch-action:pan-y}
.viz-7 .v7-edge-in{stroke:var(--sage);stroke-width:.6;fill:none;opacity:.55}
.viz-7 .v7-edge-bar{stroke:var(--terracotta);stroke-width:.5;fill:none;opacity:.32;stroke-dasharray:2 2}
.viz-7 .v7-node{cursor:pointer}
.viz-7 .v7-hi{stroke:var(--ink);stroke-width:1.4;fill:none;opacity:.9}
.viz-7 .v7-ring{stroke:var(--rule);stroke-width:.5;fill:none;opacity:.5;stroke-dasharray:2 3}
.viz-7 .v7-ringlab{font-family:var(--mono);font-size:8.5px;fill:var(--ink-3)}
.viz-7 .v7-tip{font-size:13px;color:var(--ink-2);line-height:1.5;min-height:64px;border:1px solid var(--rule);border-radius:9px;background:var(--paper-2);padding:10px 13px;margin:10px 0 0}
.viz-7 .v7-tip .tp-pos{font-family:var(--mono);font-weight:700;color:var(--ink)}
.viz-7 .v7-tip .tp-move{font-weight:600;color:var(--ink)}
.viz-7 .v7-tip .tp-chain{font-size:12px;color:var(--ink-3);margin-top:4px;font-style:italic}
.viz-7 .v7-tip .tp-gate-in{color:var(--moss);font-family:var(--mono);font-size:11px}
.viz-7 .v7-tip .tp-gate-bar{color:var(--terracotta);font-family:var(--mono);font-size:11px}
.viz-7 .v7-hole{border:1px dashed var(--terracotta);border-radius:9px;background:rgba(196,96,47,.05);padding:9px 13px;margin:10px 0 0;font-size:12.5px;color:var(--ink-2);line-height:1.5}
.viz-7 .v7-hole b{color:var(--terracotta)}
/* world-lines */
.viz-7 .v7-wl-note{font-size:13px;color:var(--ink-3);margin:0 0 12px;max-width:84ch;line-height:1.55}
.viz-7 .v7-wl{border:1px solid var(--rule);border-radius:10px;background:var(--paper);padding:12px 14px;margin:0 0 11px}
.viz-7 .v7-wl-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:9px}
.viz-7 .v7-wl-n{font-family:var(--mono);font-size:11px;font-weight:700;color:var(--paper);padding:2px 8px;border-radius:5px}
.viz-7 .v7-wl-conv .v7-wl-n{background:var(--moss)}
.viz-7 .v7-wl-div .v7-wl-n{background:var(--terracotta)}
.viz-7 .v7-verdict{font-family:var(--mono);font-size:10px;letter-spacing:.05em;padding:2px 8px;border-radius:20px}
.viz-7 .v7-wl-conv .v7-verdict{color:var(--moss);border:1px solid var(--moss)}
.viz-7 .v7-wl-div .v7-verdict{color:var(--terracotta);border:1px solid var(--terracotta)}
.viz-7 .v7-wl-tag{font-size:11.5px;color:var(--ink-3)}
.viz-7 .v7-strand{overflow-x:auto;padding:2px 0 4px}
.viz-7 .v7-beads{display:flex;align-items:flex-start;gap:0;min-width:640px}
.viz-7 .v7-bead{flex:1;display:flex;flex-direction:column;align-items:center;position:relative;padding:0 3px;min-width:74px}
.viz-7 .v7-bead:not(:last-child)::after{content:"";position:absolute;top:8px;left:50%;width:100%;height:2px;background:var(--rule)}
.viz-7 .v7-wl-conv .v7-bead:not(:last-child)::after{background:rgba(44,74,56,.35)}
.viz-7 .v7-wl-div .v7-bead:not(:last-child)::after{background:rgba(196,96,47,.3)}
.viz-7 .v7-dot{width:18px;height:18px;border-radius:50%;background:var(--paper);border:2px solid var(--moss);z-index:1;display:flex;align-items:center;justify-content:center;font-family:var(--mono);font-size:8px;color:var(--ink-3)}
.viz-7 .v7-wl-div .v7-dot{border-color:var(--terracotta)}
.viz-7 .v7-bead.fork .v7-dot{box-shadow:0 0 0 3px var(--honey)}
.viz-7 .v7-bead.term .v7-dot{background:var(--honey);border-color:var(--honey)}
.viz-7 .v7-bl-pos{font-family:var(--mono);font-size:9px;color:var(--ink-3);margin-top:4px}
.viz-7 .v7-bl-move{font-size:10.5px;color:var(--ink-2);text-align:center;line-height:1.25;margin-top:2px;max-width:80px}
.viz-7 .v7-bl-birth{font-family:var(--mono);font-size:8px;color:var(--ink-3);margin-top:2px;text-align:center}
.viz-7 .v7-sentence{font-size:13px;color:var(--ink);line-height:1.55;margin:9px 0 0;padding:8px 11px;background:var(--paper-2);border-radius:7px;border-left:3px solid var(--rule)}
.viz-7 .v7-wl-conv .v7-sentence{border-left-color:var(--moss)}
.viz-7 .v7-wl-div .v7-sentence{border-left-color:var(--terracotta)}
.viz-7 .v7-sentence b{color:var(--moss)}
.viz-7 .v7-conv-key{font-size:12.5px;color:var(--ink-2);background:var(--paper-2);border:1px solid var(--rule);border-radius:9px;padding:10px 13px;margin:4px 0 12px;line-height:1.55}
.viz-7 .v7-conv-key b{color:var(--ink)}
.viz-7 .v7-fork-key{font-family:var(--mono);font-size:10px;color:var(--ink-3);margin:6px 0 0}
.viz-7 .v7-fork-key .k-honey{color:#9a7407}
@media(prefers-reduced-motion:reduce){.viz-7 *{transition:none!important}}
</style>

  <div class="viz-h">
    <span class="viz-id">VIZ-7</span>
    <span class="viz-t">The fan, drawn — and the six world&#8209;lines to M8</span>
    <span class="chip chip-gen">GENERATED</span>
  </div>
  <p class="viz-lede">Two lenses on <b>Path&nbsp;A</b> generation from a single substitution (<i>you hurt her → you healed her</i>): the whole admissible <b>fan</b>, drawn as a radial graph, and six committed <b>world&#8209;lines</b> followed all the way to&nbsp;M8. Every branch here is <b>generated, never taken</b> — flagged as such.</p>

  <div class="v7-tldr">
    <div class="v7-tldr-h"><span class="v7-tldr-k">TL;DR</span><span class="v7-tldr-sub">what this is, in four beats</span></div>
    <ol class="v7-beats">
      <li><b>Why.</b> To <i>see</i> what one changed move opens up — the shape of "all the worlds still inside the paradigm," and which ones the era&#8209;gate bars.</li>
      <li><b>What you'd miss otherwise.</b> That the possibility space has <b>structure</b>: it fans out ~3× per move, the gate prunes a growing fraction, and only some paths <b>re&#8209;converge</b> on the song's sung ending. You can't see a shape by reading a list.</li>
      <li><b>Inputs → <span class="v7-box">substitute + fork + gate</span> → outputs.</b> In: one substitution. Black box: split at every fork (~3 admissible children) × the Sitz/era gate. Out: the ''' + str(M["fan"]["nodes"]) + '''&#8209;node fan (''' + str(M["fan"]["in_paradigm"]) + ''' in&#8209;paradigm + ''' + str(M["fan"]["barred"]) + ''' barred) and ''' + str(M["world_lines"]["count"]) + ''' world&#8209;lines.</li>
      <li><b>How it connects.</b> This is the <b>GENERATE</b> half (Decision&nbsp;175), Path&nbsp;A. The morphospace (§D) is the infrastructure a path draws on to stay coherent; §A9 is the ACTUAL song these all branch off.</li>
    </ol>
  </div>

  <div class="v7-tabs">
    <button class="v7-tab on" data-pane="fan">The fan · radial</button>
    <button class="v7-tab" data-pane="wl">The six world&#8209;lines · to M8</button>
  </div>

  <!-- ── PANE: radial fan ── -->
  <div class="v7-pane on" data-pane="fan">
    <div class="v7-legend">
      <span class="v7-lg"><span class="v7-sw v7-sw-root"></span> the substitution (M1′)</span>
      <span class="v7-lg"><span class="v7-sw v7-sw-in"></span> in&#8209;paradigm (''' + str(M["fan"]["in_paradigm"]) + ''')</span>
      <span class="v7-lg"><span class="v7-sw v7-sw-bar"></span> barred by the era&#8209;gate (''' + str(M["fan"]["barred"]) + ''')</span>
    </div>
    <div class="v7-stage"><svg class="v7-svg" id="v7svg" viewBox="0 0 680 680" width="680" height="680" role="img" aria-label="Radial draw of the 485-node substitution fan; rings are moves M1prime to M6prime; in-paradigm nodes filled, barred nodes hollow and dashed."></svg></div>
    <div class="v7-tip" id="v7tip"><b>Hover or tap a node.</b> Each dot is a generated move&#8209;state; its ring is the move number; the spoke back to the centre is its full chain from the substitution.</div>
    <div class="v7-hole">Note — the fan is drawn to its real depth: <b>M6′ (the 6th move)</b>, the outer ring. The <b>M7′–M8′ expansion (~2,000 nodes) is not yet generated</b> — that is reading-SB's to produce, and it is shown here as absent rather than invented. The six world&#8209;lines (next tab) reach M8 because that smaller dataset is real.</div>
  </div>

  <!-- ── PANE: world-lines ── -->
  <div class="v7-pane" data-pane="wl">
    <p class="v7-wl-note">A <b>world&#8209;line</b> (a physics term — one object's path through spacetime) is <b>one committed path</b>: already chosen at every fork. Here are six, each read as a chain — <b>every move carries the ones before it</b>, so no move is an orphan — all the way to <b>M8</b>. The governing concept and its birth year are shown under each bead; a ⬤ honey ring marks a <b>deciding fork</b>, a filled honey bead the <b>terminal</b>.</p>
    <div class="v7-conv-key"><b>''' + str(M["world_lines"]["converge"]) + ''' of ''' + str(M["world_lines"]["count"]) + ''' converge</b> back onto the song's sung ending (apologize / reconcile); <b>''' + str(M["world_lines"]["diverge"]) + ''' diverge</b> to a different terminal. That split is the finding: substituting <i>healed</i> for <i>hurt</i> removes the injury, so a path can only re&#8209;land on the apology if it <i>re&#8209;introduces</i> a hurt — which is why every convergent one shares a shape (<i>healed → the healer withdraws → a new hurt → apology for the withdrawal</i>).</div>
    <div class="v7-fork-key"><span class="k-honey">⬤</span> deciding fork &nbsp;·&nbsp; ⬤ terminal</div>
    <div id="v7wl"></div>
  </div>

  <p class="cap" style="font-family:var(--sans);font-size:11px;color:var(--ink-3);margin-top:12px">Source: <code>DATA_full_fan_she_loves_you_1963.csv</code> (''' + str(M["fan"]["nodes"]) + ''' nodes) + <code>DATA_altworld_she_loves_you_1963.csv</code> (''' + str(M["world_lines"]["count"]) + ''' world&#8209;lines × 8). <b>Candidate · GENERATED</b> — the engine is hand-authored + static, not yet live. Radial layout computed in&#8209;page; no external libraries.</p>

<script>
(function(){
  var D=''' + DATA_JSON + ''';
  var root=document.getElementById("viz-7"); if(!root) return;

  // ---------- radial fan ----------
  var svg=root.querySelector("#v7svg"), tip=root.querySelector("#v7tip");
  var W=680, cx=W/2, cy=W/2, maxD=D.meta.fan.max_depth, ring=(W/2-40)/maxD;
  var nodes=D.fan_nodes, byid={}; nodes.forEach(function(n){byid[n.id]=n;});
  var kids={}; nodes.forEach(function(n){ if(n.parent>=0){(kids[n.parent]=kids[n.parent]||[]).push(n.id);} });
  // leaf order via DFS from root (id 0)
  var order=[], seen={};
  (function dfs(id){ var ch=kids[id]; if(!ch||!ch.length){order.push(id);return;} ch.forEach(dfs); })(0);
  var nLeaf=order.length, ang={}, li=0;
  order.forEach(function(id){ ang[id]=(li/nLeaf)*Math.PI*2 - Math.PI/2; li++; });
  // internal node angle = mean of children (post-order)
  function setAng(id){ var ch=kids[id]; if(!ch||!ch.length) return ang[id];
    var s=0; ch.forEach(function(c){s+=setAng(c);}); return ang[id]=s/ch.length; }
  setAng(0);
  function pos(id){ var n=byid[id], r=n.depth*ring; return [cx+r*Math.cos(ang[id]), cy+r*Math.sin(ang[id])]; }

  var NS="http://www.w3.org/2000/svg", parts=[];
  // rings + labels
  for(var d=1; d<=maxD; d++){
    parts.push('<circle class="v7-ring" cx="'+cx+'" cy="'+cy+'" r="'+(d*ring).toFixed(1)+'"/>');
    parts.push('<text class="v7-ringlab" x="'+cx+'" y="'+(cy - d*ring - 2).toFixed(1)+'" text-anchor="middle">M'+(d+1)+'&#8242;</text>');
  }
  // edges
  nodes.forEach(function(n){ if(n.parent<0) return;
    var a=pos(n.parent), b=pos(n.id);
    parts.push('<path class="v7-edge-'+(n.gate==="barred"?"bar":"in")+'" d="M'+a[0].toFixed(1)+' '+a[1].toFixed(1)+' L'+b[0].toFixed(1)+' '+b[1].toFixed(1)+'"/>');
  });
  // nodes
  nodes.forEach(function(n){ var p=pos(n.id);
    var isRoot=n.parent<0, r=isRoot?6:(n.depth>=5?2:2.6);
    var fill=isRoot?"var(--honey)":(n.gate==="in"?"var(--fern)":"var(--paper)");
    var stroke=n.gate==="barred"?"var(--terracotta)":"none";
    var dash=n.gate==="barred"?' stroke-dasharray="1.5 1.5" stroke-width="1"':'';
    parts.push('<circle class="v7-node" data-id="'+n.id+'" cx="'+p[0].toFixed(1)+'" cy="'+p[1].toFixed(1)+'" r="'+r+'" fill="'+fill+'" stroke="'+stroke+'"'+dash+'/>');
  });
  parts.push('<path class="v7-hi" id="v7hi" d=""/>');
  svg.innerHTML=parts.join("");

  var hi=svg.querySelector("#v7hi");
  function esc(s){return (s||"").replace(/&/g,"&amp;").replace(/</g,"&lt;");}
  function show(n){
    var chain=n.chain.map(esc).join(" &rarr; ");
    var g=n.gate==="in"
      ? '<span class="tp-gate-in">in-paradigm</span>'
      : '<span class="tp-gate-bar">barred &mdash; concept postdates 1963</span>';
    tip.innerHTML='<span class="tp-pos">M'+n.m+'&#8242;</span> &middot; '+g+
      '<br><span class="tp-move">'+esc(n.move)+'</span> <span style="color:var(--ink-3)">&mdash; '+esc(n.concept)+'</span>'+
      '<div class="tp-chain">'+chain+'</div>';
    // spoke: root -> node
    var p=pos(n.id), d="M"+cx+" "+cy+" L"+p[0].toFixed(1)+" "+p[1].toFixed(1);
    hi.setAttribute("d", d);
  }
  svg.addEventListener("mouseover", function(e){ var t=e.target.closest(".v7-node"); if(t) show(byid[+t.getAttribute("data-id")]); });
  svg.addEventListener("click", function(e){ var t=e.target.closest(".v7-node"); if(t) show(byid[+t.getAttribute("data-id")]); });

  // ---------- world-lines ----------
  var wlWrap=root.querySelector("#v7wl"), whtml=[];
  D.world_lines.forEach(function(w){
    var conv=w.verdict==="CONVERGE";
    var beads=w.positions.map(function(p){
      var cls="v7-bead"+(p.fork?" fork":"")+(p.terminal?" term":"");
      return '<div class="'+cls+'"><div class="v7-dot">'+p.i+'</div>'+
        '<div class="v7-bl-pos">'+esc(p.pos)+'</div>'+
        '<div class="v7-bl-move">'+esc(p.move)+'</div>'+
        '<div class="v7-bl-birth">'+esc(p.birth)+'</div></div>';
    }).join("");
    whtml.push('<div class="v7-wl '+(conv?"v7-wl-conv":"v7-wl-div")+'">'+
      '<div class="v7-wl-h"><span class="v7-wl-n">WL'+w.wl+'</span>'+
      '<span class="v7-verdict">'+w.verdict+'</span>'+
      '<span class="v7-wl-tag">'+(conv?"re-lands on the sung ending":"ends elsewhere")+'</span></div>'+
      '<div class="v7-strand"><div class="v7-beads">'+beads+'</div></div>'+
      '<div class="v7-sentence"><b>Read as one sentence:</b> '+esc(w.sentence)+'.</div></div>');
  });
  wlWrap.innerHTML=whtml.join("");

  // ---------- tabs ----------
  root.querySelectorAll(".v7-tab").forEach(function(b){
    b.addEventListener("click", function(){
      var p=b.getAttribute("data-pane");
      root.querySelectorAll(".v7-tab").forEach(function(x){x.classList.toggle("on", x===b);});
      root.querySelectorAll(".v7-pane").forEach(function(x){x.classList.toggle("on", x.getAttribute("data-pane")===p);});
    });
  });
})();
</script>
</div>
<!-- ══ /VIZ-7 ══ -->
'''

def main():
    h = HTML.read_text()
    wrapped = SECTION
    if '<!-- ══ VIZ-7 TREE-DRAW (built) ══ -->' in h:
        h = re.sub(r'<!-- ══ VIZ-7 TREE-DRAW \(built\) ══ -->.*?<!-- ══ /VIZ-7 ══ -->\n',
                   wrapped, h, flags=re.S)
        print("re-rendered existing VIZ-7")
    else:
        anchor = h.find('<section class="sec" id="d-frame">')
        assert anchor != -1, "could not find #d-frame insertion point"
        # place just before the D section (end of C5)
        h = h[:anchor] + wrapped + "\n" + h[anchor:]
        print("inserted VIZ-7 at end of §C5 (before #d-frame)")
    HTML.write_text(h)
    assert h.count('id="viz-7"') == 1, h.count('id="viz-7"')
    for must in ("The fan, drawn", "GENERATE", "not yet generated"):
        assert must in h, f"missing {must!r}"
    for banned in ("IN-FRAME", "convergence everywhere", "never met"):
        assert banned not in SECTION, f"banned {banned!r}"
    print("viz-7 present:", h.count('id="viz-7"'), "| page bytes:", len(h))

if __name__ == "__main__":
    main()
