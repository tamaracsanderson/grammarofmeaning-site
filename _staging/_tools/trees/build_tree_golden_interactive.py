#!/usr/bin/env python3
"""Add a non-destructive interactive layer to reading-SB's static golden-chain trace-tree.

Item A of the S150 design-SB batch (BATCH_to_designSB_trees_and_perennial_2026-07-14):
clickable nodes → a detail panel (the move it codes, the pericope/line, its edges' provenance
class); the election move → a FILLED/POSSIBLE/PRUNED gap explorer with expand-on-click; the
IRR182 provenance rendering (solid=attested, dashed-grey=reconstructed) is preserved verbatim
from the source SVG. Content (nodes, gaps, prunings) is reading-SB's, lifted from the source
tree's own tables + review box; nothing invented.

Usage: build_tree_golden_interactive.py <src_tree_golden_chain.html> <OUTPUT.html>
"""
import sys, re, json

# --- node model: overlay a transparent clickable rect at each node's known coords ---
# coords lifted verbatim from the source SVG node groups.
NODES = {
  "dort":       dict(x=112,y=150,w=240,h=70, t="doctrine", title="Canons of Dort (1619)",
                     d="<b>Doctrine · reception branch (forward).</b> Unconditional Election · Perseverance. The Reformed terminus of the left fork — reads <i>proginōskō</i> as fore-love. Edge to Calvin is <b>attested</b> (Dort codifies the Calvinist reading).", prov="attested"),
  "westminster":dict(x=368,y=150,w=196,h=70, t="doctrine", title="Westminster III (1646)",
                     d="<b>Doctrine · reception branch (forward).</b> “Of God’s Eternal Decree.” Sits beside Dort on the Reformed fork. Edge <b>attested</b>.", prov="attested"),
  "methodism":  dict(x=980,y=150,w=220,h=70, t="doctrine", title="Wesleyan-Methodist",
                     d="<b>Doctrine · reception branch (forward).</b> Resistible, losable grace. The terminus of the right fork — reads <i>proginōskō</i> as fore-seen faith. Edge to Wesley <b>attested</b>.", prov="attested"),
  "remonstrance":dict(x=1216,y=150,w=240,h=70,t="doctrine", title="Remonstrance (1610)",
                     d="<b>Doctrine · reception branch (forward).</b> Conditional Election. The Arminian terminus; the doctrine Dort was convened to reject. Edge <b>attested</b>.", prov="attested"),
  "augustine":  dict(x=240,y=430,w=190,h=66, t="interpreter", title="Augustine (354–430)",
                     d="<b>Interpreter (mediating reader).</b> Late anti-Pelagian — unconditional election. Edge to the pivot is <b>attested</b>: Augustine explicitly comments on Rom 8:28–30 (<i>De praedestinatione sanctorum</i>). Note: “attested that he read it” is not “attested that his reading is the verse’s sense.”", prov="attested"),
  "calvin":     dict(x=228,y=300,w=190,h=66, t="interpreter", title="Calvin (1509–64)",
                     d="<b>Interpreter.</b> <i>Institutes</i> III · the <i>ordo salutis</i>. Carries Augustine’s reading into the Reformed formulae. Edge <b>attested</b>.", prov="attested"),
  "arminius":   dict(x=1078,y=430,w=196,h=66,t="interpreter", title="Arminius (1560–1609)",
                     d="<b>Interpreter.</b> foreknew = foreseen faith. The hinge of the right fork — it is his reading of <i>proginōskō</i> (candidate <b>G4</b>) that the whole left/right split rides on. Edge <b>attested</b>.", prov="attested"),
  "wesley":     dict(x=1092,y=300,w=196,h=66,t="interpreter", title="Wesley (1703–91)",
                     d="<b>Interpreter.</b> Prevenient grace · can fall away — fills candidate <b>G5</b> (modality of “glorified”: losable). Edge <b>attested</b>.", prov="attested"),
  # roots
  "yada":       dict(x=356,y=1048,w=228,h=78,t="jewish-root", title="Hebrew יָדַע yāda‘ — covenant “knowing”",
                     d="<b>Backward · jewish-root.</b> Amos 3:2 · Jer 1:5 — election, not cognition. Grafts under <b>foreknew</b> (προέγνω). Edge marked <b>attested</b> on lexical-semantic grounds (LXX renders <i>yāda‘</i> with <i>ginōskō</i>) — but review item 4 asks: a root the verb grafts, or just semantic background?", prov="attested"),
  "deut":       dict(x=626,y=1048,w=250,h=78,t="jewish-root", title="Deuteronomic election-not-by-merit",
                     d="<b>Backward · jewish-root.</b> Deut 7:7–8 · 9:4–6 — God set his love, not for their righteousness (the <b>warrant</b>, candidate G1). Edge <b>attested</b>.", prov="attested"),
  "qumran":     dict(x=918,y=1048,w=248,h=78,t="jewish-root", title="Qumran — 1QS “Two Spirits”",
                     d="<b>Backward · jewish-root · RECONSTRUCTED.</b> Community Rule III–IV · a real Second-Temple predestinarian <b>parallel</b> — but Paul never quotes Qumran. Drawn <b>dashed-grey</b>: parallel, not citation. Genealogy or shared <i>Zeitgeist</i>? (Review item 3.)", prov="reconstructed"),
  "stoic":      dict(x=470,y=1300,w=260,h=82,t="pagan-root", title="Stoic pronoia (providence)",
                     d="<b>Backward · pagan-root · RECONSTRUCTED — most fragile edge in the tree.</b> cosmic <i>sympatheia</i> ≈ “all things work together” (Rom 8:28, πάντα συνεργεῖ). No citation exists. Is Paul grafting Stoic providence, or just using shared Hellenistic vocabulary? Drawn <b>dashed-grey</b>. Should it appear at all? (Review item 1.)", prov="reconstructed"),
  "philo":      dict(x=792,y=1300,w=238,h=82,t="pagan-root", title="Philo / Middle-Platonic mediation",
                     d="<b>Backward · pagan-root · RECONSTRUCTED.</b> A possible Hellenistic-Jewish conduit between Greek concepts and Paul. Entirely inferential; no textual link. Drawn <b>dashed-grey</b>. Keep, demote, or cut? (Review item 2.)", prov="reconstructed"),
  # non-election pivot moves (open a node panel, not the gap explorer)
  "called":     dict(x=670,y=742,w=126,h=118,t="move", title="called — ἐκάλεσεν (move 3, v.30)",
                     d="<b>Pivot move 3.</b> The chain’s effectual call. Not an election move — no starred gap attaches here; it inherits the warrant/scope gaps from foreknew.", prov="attested"),
  "justified":  dict(x=806,y=742,w=126,h=118,t="move", title="justified — ἐδικαίωσεν (move 4, v.30)",
                     d="<b>Pivot move 4.</b> Forensic justification. Links backward to the <i>warrant</i> gap (justified on what basis?).", prov="attested"),
  "glorified":  dict(x=942,y=742,w=172,h=118,t="move", title="glorified — ἐδόξασεν (move 5, v.30)",
                     d="<b>Pivot move 5 · proleptic aorist (candidate G5).</b> A completed past tense for a future reality — the grammatical seat of the <i>modality</i> gap: is glory certain, or losable? Wesley fills it “losable.”", prov="attested"),
}
# the two election moves open the gap explorer
ELECTION = {
  "foreknew":   dict(x=386,y=742,w=132,h=118, title="foreknew — προέγνω (move 1, v.29)"),
  "predestined":dict(x=528,y=742,w=132,h=118, title="predestined — προώρισεν (move 2, v.29–30)"),
}

# --- gap explorer: the 5 slots at the election move, fills tagged FILLED / POSSIBLE / PRUNED ---
# lifted from the source's U0-U4 universe table + G1-G7 candidates + review box.
GAPS = [
  dict(slot="agent", q="who elects?", gap=None, fills=[
    dict(label="God", state="FILLED", tier="U0", why="the passage’s own filler — the implied subject of every verb."),
    dict(label="Christ (“his Son,” 8:29)", state="POSSIBLE", tier="U1", why="raised in the immediate context, not the chain’s subject."),
    dict(label="the Spirit (8:26–27)", state="POSSIBLE", tier="U1", why="intercedes nearby; a candidate agent the passage doesn’t select."),
    dict(label="the human response (Rom 10:9–13)", state="POSSIBLE", tier="U2", why="Pauline-corpus tier; the synergist reading pulls here."),
    dict(label="corporate Israel (Rom 9–11)", state="POSSIBLE", tier="U3", why="the NPP / corporate-election reading; wider-context tier."),
  ]),
  dict(slot="warrant", q="on what basis these?", gap="G1", fills=[
    dict(label="God’s own purpose/grace, not works", state="POSSIBLE", tier="U2", why="Rom 9:11–12; 11:5–6; Eph 1:11 fill it — but the passage itself fills NONE. That silence IS gap G1."),
    dict(label="covenant-love, not righteousness", state="POSSIBLE", tier="U3", why="Deut 7:7–8; 9:4–6 — the jewish-root warrant."),
    dict(label="foreseen faith", state="POSSIBLE", tier="U4", why="later-reception tier; Arminius’ fill (candidate G4)."),
    dict(label="foreseen merit", state="PRUNED", tier="U4", why="condemned as Pelagian (Council of Carthage, 418). A fill the tradition explicitly ruled out — shown so the pruning is visible, not hidden."),
  ]),
  dict(slot="scope", q="which set?", gap="G2", fills=[
    dict(label="“those whom” — a bounded set", state="FILLED", tier="U0", why="the passage’s own language."),
    dict(label="“the called…according to his purpose”", state="FILLED", tier="U0", why="the passage names the in-group."),
    dict(label="all-who-love-God", state="FILLED", tier="U0", why="v.28’s own qualifier."),
    dict(label="the not-chosen / reprobate", state="POSSIBLE", tier="U1", why="raised at Rom 9:18–22, NOT here — the chain names only the saved. That un-named half IS gap G2."),
    dict(label="Israel-and-Gentiles corporately", state="POSSIBLE", tier="U3", why="wider-context corporate reading."),
  ]),
  dict(slot="modality", q="how certain?", gap="G5", fills=[
    dict(label="certain / necessary — “glorified” as completed past", state="FILLED", tier="U0", why="the proleptic aorist: a done deal grammatically."),
    dict(label="contingent / losable", state="POSSIBLE", tier="U4", why="the perseverance debate; Wesley’s “can fall away.”"),
    dict(label="conditional-on-perseverance", state="POSSIBLE", tier="U2", why="Rom 11:22 “if you continue” pulls back toward condition."),
  ]),
  dict(slot="sequence", q="link-to-link?", gap="G7", fills=[
    dict(label="temporal · logical · causal · unbreakable-chain", state="FILLED", tier="U0", why="the golden chain’s own force: each link entails the next."),
    dict(label="separable-with-possible-failure", state="POSSIBLE", tier="U4", why="the losable-grace reading; can a link fail?"),
  ]),
]
CANDIDATES = [  # the G1-G7 output, for the “all candidate gaps” accordion tail
  dict(g="G1", txt="the <b>warrant</b> of election is unfilled (on what basis these?)", kind="bounded-contrast-set", status="recovered = basis"),
  dict(g="G2", txt="the <b>reprobate</b> / not-chosen are unnamed", kind="scope-boundary", status="recovered = reprobation"),
  dict(g="G3", txt="the <b>agency-boundary</b> (where God’s act ends, the human’s begins)", kind="sequence + warrant", status="recovered = agency"),
  dict(g="G4", txt="<b>proginōskō</b> under-defined — foresaw vs fore-loved?", kind="definition-probe", status="NEW — the translation-fork (= the left/right split)"),
  dict(g="G5", txt="<b>modality</b> of “glorified” — certain or losable?", kind="modality", status="NEW — Wesley fills it"),
  dict(g="G6", txt="the elect as <b>individuals vs corporate</b>", kind="presupposition", status="NEW — the corporate/individual crux"),
  dict(g="G7", txt="<b>sequence-mode</b> — temporal, logical, causal; can a link fail?", kind="sequence/dependency", status="NEW — the unbreakable-chain question"),
]

def build(src_path, out_path):
    h = open(src_path).read()
    h = h.replace("<title>Bidirectional Trace-Tree — the Golden Chain (Romans 8:28–30) · CANDIDATE PILOT</title>",
                  '<title>Interactive Trace-Tree — the Golden Chain (Romans 8:28–30) · CANDIDATE PILOT</title>\n<meta name="robots" content="noindex,nofollow">')

    # 1) CSS for the interactive layer (append inside <style>)
    css = """
  /* ---- interactive layer (design-SB, Item A) ---- */
  .hit{fill:transparent;cursor:pointer}
  .hit:hover{fill:var(--indigo);fill-opacity:.07;stroke:var(--indigo);stroke-width:2;rx:8}
  .hit.sel{fill:var(--indigo);fill-opacity:.10;stroke:var(--indigo);stroke-width:2.4}
  .hint{font-family:ui-sans-serif,-apple-system,sans-serif;font-size:12.5px;color:var(--slate);margin:10px 2px 14px}
  .hint b{color:var(--indigo)}
  #treepanel{position:sticky;bottom:0;margin-top:14px;background:var(--card);border:1px solid var(--border);
    border-radius:12px;padding:0;overflow:hidden;box-shadow:0 -2px 14px rgba(0,0,0,.06)}
  #tp-head{display:flex;align-items:center;gap:10px;padding:13px 18px;background:var(--pivot-bg);
    border-bottom:1px solid var(--border)}
  #tp-kind{font-family:ui-sans-serif,sans-serif;font-size:10px;font-weight:700;letter-spacing:.08em;
    text-transform:uppercase;color:#fff;background:var(--indigo);padding:3px 9px;border-radius:20px;white-space:nowrap}
  #tp-title{font-family:Georgia,serif;font-weight:700;font-size:16px;color:var(--ink)}
  #tp-body{padding:16px 20px;font-size:14.5px;line-height:1.55}
  #tp-body .prov{font-family:ui-sans-serif,sans-serif;font-size:12px;color:var(--slate);margin-top:10px}
  .prov .dashkey{color:var(--recon);font-style:italic}
  /* gap explorer */
  .gaprow{border:1px solid var(--border);border-radius:9px;margin:9px 0;overflow:hidden;background:var(--node-bg)}
  .gaphead{display:flex;align-items:center;gap:10px;padding:11px 14px;cursor:pointer;font-family:ui-sans-serif,sans-serif}
  .gaphead:hover{background:var(--chip-bg)}
  .gaphead .slot{font-weight:700;font-size:14px;color:var(--ink)}
  .gaphead .q{font-size:12.5px;color:var(--slate)}
  .gaphead .gid{margin-left:auto;font-size:10.5px;font-weight:700;color:var(--indigo);
    border:1px solid var(--indigo);border-radius:20px;padding:2px 9px;white-space:nowrap}
  .gaphead .caret{color:var(--slate);transition:transform .18s}
  .gaprow.open .caret{transform:rotate(90deg)}
  .gapfills{display:none;padding:4px 14px 14px}
  .gaprow.open .gapfills{display:block}
  .fill{display:flex;gap:10px;align-items:flex-start;padding:9px 0;border-top:1px solid var(--rule)}
  .fill .st{font-family:ui-sans-serif,sans-serif;font-size:9.5px;font-weight:700;letter-spacing:.04em;
    text-transform:uppercase;padding:2px 8px;border-radius:20px;white-space:nowrap;flex:none;margin-top:1px}
  .st.FILLED{background:#e7efdf;color:#33502f;border:1px solid #6c9a62}
  .st.POSSIBLE{background:var(--pivot-bg);color:var(--indigo);border:1px solid var(--indigo-soft)}
  .st.PRUNED{background:var(--chip-bg);color:var(--slate);border:1px solid var(--border)}
  @media (prefers-color-scheme:dark){.st.FILLED{background:#1c2a18;color:#8fb884}}
  .fill .ftxt{font-size:13.5px}
  .fill.pruned .flabel{text-decoration:line-through;color:var(--slate)}
  .fill .flabel{font-weight:600}
  .fill .fwhy{color:var(--slate);font-size:12.5px;margin-top:2px}
  .fill .ftier{font-family:ui-monospace,monospace;font-size:10.5px;color:var(--slate);margin-left:6px}
  .statekey{display:flex;gap:14px;flex-wrap:wrap;font-family:ui-sans-serif,sans-serif;font-size:11.5px;
    color:var(--slate);margin:2px 0 10px}
  .statekey .st{cursor:default}
  .backlink{display:inline-block;margin:22px 0 0;font-family:ui-sans-serif,sans-serif;font-size:13px}
</style>"""
    h = h.replace("</style>", css, 1)

    # 2) overlay hit-rects (added just before </svg> so they sit on top)
    overlays = ['<!-- interactive overlay (design-SB) -->']
    for nid, n in NODES.items():
        overlays.append(f'<rect class="hit" data-node="{nid}" x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="8"><title>{n["title"]}</title></rect>')
    for nid, n in ELECTION.items():
        overlays.append(f'<rect class="hit" data-gap="1" data-node="{nid}" x="{n["x"]}" y="{n["y"]}" width="{n["w"]}" height="{n["h"]}" rx="8"><title>{n["title"]} — click for the gap explorer</title></rect>')
    h = h.replace("</svg>", "\n        " + "\n        ".join(overlays) + "\n      </svg>", 1)

    # 3) hint above the diagram + panel below it
    h = h.replace('<div class="diagram-scroll">',
                  '<p class="hint">▸ <b>Interactive.</b> Click any node for its provenance class + the move it touches. Click a starred <b>election move</b> (foreknew / predestined) to open the gap explorer — each slot’s fills tagged <b>filled · possible · pruned</b>, expand to see why.</p>\n    <div class="diagram-scroll">', 1)
    panel = '''    <div id="treepanel">
      <div id="tp-head"><span id="tp-kind">start</span><span id="tp-title">Click a node</span></div>
      <div id="tp-body">Click any node in the tree above. Reconstructed (dashed-grey) edges are hypotheses, never settled genealogy (IRR182). Start with the starred <b>election move</b> for the gap explorer.</div>
    </div>
    <a class="backlink" href="coding-lab.html">← back to the coding lab</a>'''
    # insert panel after the diagram-scroll block's closing + its lede paragraph
    h = h.replace('    <p class="lede" style="margin-top:14px">',
                  panel + '\n    <p class="lede" style="margin-top:14px">', 1)

    # 4) JS data + handlers before </body>
    js = "<script>\n"
    js += "var NODES=" + json.dumps({k: {"t": v["t"], "title": v["title"], "d": v["d"], "prov": v["prov"]} for k, v in NODES.items()}, ensure_ascii=False) + ";\n"
    js += "var ELECTION=" + json.dumps({k: {"title": v["title"]} for k, v in ELECTION.items()}, ensure_ascii=False) + ";\n"
    js += "var GAPS=" + json.dumps(GAPS, ensure_ascii=False) + ";\n"
    js += "var CANDS=" + json.dumps(CANDIDATES, ensure_ascii=False) + ";\n"
    js += r"""
var kind=document.getElementById('tp-kind'), title=document.getElementById('tp-title'), body=document.getElementById('tp-body');
function sel(el){ document.querySelectorAll('.hit.sel').forEach(function(h){h.classList.remove('sel');}); if(el) el.classList.add('sel'); }
function showNode(id){
  var n=NODES[id]; if(!n) return;
  kind.textContent=n.t; title.innerHTML=n.title;
  var pk = n.prov==='reconstructed'
    ? '<span class="dashkey">reconstructed — drawn dashed-grey; a hypothesis, not settled genealogy (IRR182).</span>'
    : 'attested — the citation/link is real (which is not the same as the reading being correct).';
  body.innerHTML = n.d + '<div class="prov">Edge provenance: '+pk+'</div>';
}
function showGap(id){
  var e=ELECTION[id];
  kind.textContent='election move · gap explorer'; title.innerHTML=e.title;
  var html='<div class="statekey">'
    +'<span><span class="st FILLED">filled</span> the passage takes this</span>'
    +'<span><span class="st POSSIBLE">possible</span> coherent, raised elsewhere / higher tier</span>'
    +'<span><span class="st PRUNED">pruned</span> ruled out — shown, not hidden</span></div>';
  GAPS.forEach(function(g,i){
    html+='<div class="gaprow" data-i="'+i+'"><div class="gaphead" onclick="this.parentNode.classList.toggle(\'open\')">'
      +'<span class="caret">▸</span><span class="slot">'+g.slot+'</span><span class="q">'+g.q+'</span>'
      +(g.gap?'<span class="gid">gap '+g.gap+'</span>':'')+'</div><div class="gapfills">';
    g.fills.forEach(function(f){
      html+='<div class="fill'+(f.state==='PRUNED'?' pruned':'')+'"><span class="st '+f.state+'">'+f.state.toLowerCase()+'</span>'
        +'<div class="ftxt"><span class="flabel">'+f.label+'</span><span class="ftier">'+f.tier+'</span>'
        +'<div class="fwhy">'+f.why+'</div></div></div>';
    });
    html+='</div></div>';
  });
  html+='<div class="gaprow" data-i="cands"><div class="gaphead" onclick="this.parentNode.classList.toggle(\'open\')">'
    +'<span class="caret">▸</span><span class="slot">all seven candidate gaps</span><span class="q">G1–G7, the generator’s output</span></div><div class="gapfills">';
  CANDS.forEach(function(c){
    html+='<div class="fill"><span class="st POSSIBLE">'+c.g+'</span><div class="ftxt"><span class="flabel">'+c.txt+'</span>'
      +'<div class="fwhy">'+c.kind+' · '+c.status+'</div></div></div>';
  });
  html+='</div></div>';
  body.innerHTML=html;
}
document.querySelectorAll('.hit').forEach(function(h){
  h.addEventListener('click',function(){ sel(h); var id=h.getAttribute('data-node');
    if(h.getAttribute('data-gap')) showGap(id); else showNode(id);
    document.getElementById('treepanel').scrollIntoView({behavior:'smooth',block:'nearest'}); });
});
</script>
"""
    h = h.replace("</body>", js + "</body>", 1)
    open(out_path, "w").write(h)
    print(f"wrote {out_path} — {len(NODES)+len(ELECTION)} clickable nodes, {len(GAPS)} gap slots, {len(CANDIDATES)} candidates")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
