#!/usr/bin/env python3
"""VIZ-1 — the edge legend + the song's edges re-drawn. Replaces the VIZ-1 vizslot in method-canonical.html.

Every datum from a §4 file (R1 — nothing invented):
  · moves + edges + residuals: field_ed/negative_space_pilot_8move_she_loves_you_2026-07-10.md (paraphrase only, no lyric)
  · edge families/names/definitions: the §A6 v2 taxonomy table in method-canonical.html (the arbiter) = edge_taxonomy_v2_2026-07-11.md
  · IRR177 corrections: the pilot's own cold-cohort section + the SPA's IRR ledger (row 177)
Gen-3 names canonical (FEEDS/FILLS/RESIDUAL), gen-2 kept as alias (THEN/ANSWERS/BEQUEST), gen-1 retired (production/completion/reception).
R2 ink rule: ACTUAL / ATTESTED / GENERATED never share ink. R6: colour never the only channel — every family also has a dash + arrowhead + label.

Usage: build_viz1.py <method-canonical.html> (edits in place)
"""
import sys, re

# ── the 8 moves — verbatim operations from the pilot (paraphrase, never lyric) ──
MOVES = [
    dict(id="M1", op="hurt (past)",    who="you → her",           typ="narrate",   x=90),
    dict(id="M2", op="suffer",          who="she → (self)",        typ="narrate",   x=222),
    dict(id="M3", op="reappraise",      who="she → you (char.)",   typ="narrate",   x=354),
    dict(id="M4", op="loves",           who="she → you",           typ="report",    x=486, star=True),
    dict(id="M5", op="fear / believe",  who="you → (the loss)",    typ="assert",    x=618),
    dict(id="M6", op="relay / witness", who="I (friend) → you",    typ="report",    x=750),
    dict(id="M7", op="exhort-feel",     who="→ you (be glad)",     typ="directive", x=882),
    dict(id="M8", op="exhort-act",      who="→ you (apologize)",   typ="directive", x=1014),
]
# ── FILLS that SURVIVE IRR177 (backward onto the money-move M4) ──
FILLS = [
    dict(frm="M2", to="M4", role="DEGREE",  why="how much she suffered → she cares a lot"),
    dict(frm="M6", to="M4", role="WARRANT", why="how the friend knows — he carries her word"),
    dict(frm="M7", to="M4", role="OUTCOME", why="what the love produces — be glad"),
    dict(frm="M8", to="M4", role="OUTCOME", why="…and reconcile"),
]
# ── FILLS the author drew that 5 COLD CODERS REMOVED (IRR177) — the mechanism, shown ──
CORRECTED = [
    dict(frm="M1", to="M4", role="REASON",      became="why she loves you — the positive ground"),
    dict(frm="M3", to="M4", role="REASON",      became="reappraisal removes an obstacle; it does not supply the ground"),
    dict(frm="M5", to="M4", role="RECIPROCITY", became="the addressee's foreclosed reciprocity"),
]
# ── the two RESIDUALS per the SPA's canonical sentence (§C-1) ──
RESIDUALS = [
    dict(frm="M4", label="the addressee's foreclosed reciprocity", sub="does HE love her back? — never stated · 5/5 touch, 3/5 name", x=486),
    dict(frm="META", label="the friend's motive", sub="why does the friend care? — the mediator's stake · 5/5 cold", x=750),
]
# ── the four families, from the §A6 v2 table. present=coded on this song ──
FAMILIES = [
    dict(key="A", name="COHERENCE", scope="within a text: how its moves build", cls="fam-a",
         edges=[("FEEDS","THEN","move N → N+1","7 on this song",True),
                ("FILLS","ANSWERS","a later move → an earlier gap","4 — and they run backward",True),
                ("COMPOSES","NESTS","a move → the meta-move holding it","8 — all of them",True),
                ("ELABORATES","—","N+1 → a finished claim N","none coded",False),
                ("SCAFFOLDS","—","N → N+1","none coded",False)]),
    dict(key="B", name="RECEPTION", scope="text → later reader", cls="fam-b",
         edges=[("RESIDUAL","BEQUEST","an unresolvable gap → reception","2 — pointing out of the song",True),
                ("REINTERPRETS","—","a later reader → a residual","none — no reception coded",False),
                ("FORKS","FORK","a later reader → a residual","none — the song has no interpretive fork",False)]),
    dict(key="C", name="CONVERGENCE", scope="cross-text: sameness", cls="fam-c",
         edges=[("EXACT-STRUCTURAL-MATCH","RHYME","a move here :: a move there","none — no cross-text pair coded",False),
                ("CLOSE-MATCH","COUSIN","a near-rhyme","none",False),
                ("GENERALIZES","—","a pair → the pattern P both instantiate","none",False),
                ("BROADER / NARROWER","—","across texts","none",False),
                ("CITE / ECHO","—","a borrower → a source","none",False)]),
    dict(key="D", name="DIVERGENCE", scope="cross-text: difference", cls="fam-d",
         edges=[("SURFACE-MATCH","FALSE-FRIEND","same words, different move","none — no cross-text pair coded",False),
                ("OPPOSES","COUNTER","a deliberate opposite","none",False),
                ("INVERTS","INVERT","a reversal","none",False),
                ("IRONIC","—","a move → itself","none",False)]),
]

def mx(mid):
    if mid == "META": return 552
    return next(m["x"] for m in MOVES if m["id"] == mid)

def build_svg():
    W, H = 1130, 524
    NY, NW, NH = 250, 116, 62      # move-node row
    s = []
    # meta-move box (COMPOSES/NESTS holds all eight)
    s.append(f'<rect class="metabox" x="40" y="{NY-58}" width="{W-80}" height="{NH+96}" rx="14"/>')
    s.append(f'<text class="metalab" x="52" y="{NY-38}">META-MOVE · the friend PERSUADES you to reconcile (because she loves you)</text>')
    s.append(f'<text class="metasub" x="52" y="{NY-24}">COMPOSES <tspan class="alias">/ NESTS</tspan> — it contains all eight; the edges below are its internal structure</text>')

    # FEEDS chain (solid, forward)
    for a, b in zip(MOVES, MOVES[1:]):
        x1, x2 = a["x"] + NW/2, b["x"] - NW/2
        s.append(f'<line class="e-feeds" x1="{x1}" y1="{NY+NH/2}" x2="{x2-7}" y2="{NY+NH/2}" marker-end="url(#ah-feeds)"/>')
    s.append(f'<text class="elab lab-a" x="34" y="{NY-8}">FEEDS <tspan class="alias">/ THEN</tspan> → forward, move to move</text>')

    # FILLS arcs — BACKWARD onto M4 (drawn beneath, arrowhead into M4)
    tx = mx("M4")
    for i, f in enumerate(FILLS):
        fx = mx(f["frm"]); depth = 74 + i*26
        x2 = tx + (26 if fx > tx else -26)
        s.append(f'<path class="e-fills" d="M {fx} {NY+NH} C {fx} {NY+NH+depth}, {x2} {NY+NH+depth}, {x2} {NY+NH+8}" marker-end="url(#ah-fills)"/>')
        midx = (fx + x2)/2
        s.append(f'<text class="rolelab" x="{midx}" y="{NY+NH+depth+11}">{f["role"]}</text>')
    s.append(f'<text class="elab lab-a2" x="60" y="{NY+NH+182}">← FILLS <tspan class="alias">/ ANSWERS</tspan> — later moves answering the money-move, running <tspan class="bk">backward</tspan></text>')

    # IRR177-corrected edges (toggleable ghost layer)
    s.append('<g id="v1-corrected" class="corrected-layer" hidden>')
    for i, c in enumerate(CORRECTED):
        fx = mx(c["frm"]); depth = 46 + i*18
        x2 = tx + (20 if fx > tx else -20)
        s.append(f'<path class="e-corrected" d="M {fx} {NY} C {fx} {NY-depth}, {x2} {NY-depth}, {x2} {NY-6}"/>')
        s.append(f'<text class="corrlab" x="{(fx+x2)/2}" y="{NY-depth-3}">{c["role"]} ✕</text>')
    s.append('</g>')

    # move nodes
    for m in MOVES:
        star = ' star' if m.get("star") else ''
        s.append(f'<g class="node{star}"><rect x="{m["x"]-NW/2}" y="{NY}" width="{NW}" height="{NH}" rx="9"/>'
                 f'<text class="nid" x="{m["x"]-NW/2+9}" y="{NY+15}">{m["id"]}{" ★" if m.get("star") else ""}</text>'
                 f'<text class="nop" x="{m["x"]}" y="{NY+34}" text-anchor="middle">{m["op"]}</text>'
                 f'<text class="nwho" x="{m["x"]}" y="{NY+48}" text-anchor="middle">{m["who"]}</text>'
                 f'<text class="ntyp" x="{m["x"]+NW/2-9}" y="{NY+15}" text-anchor="end">{m["typ"]}</text></g>')

    s.append(f'<text class="moneylab" x="{mx("M4")}" y="{NY-8}" text-anchor="middle">★ the money-move — every FILLS arrow lands here</text>')

    # RESIDUAL edges — pointing OUT of the text, up to an un-coded reception band
    s.append(f'<line class="recline" x1="40" y1="86" x2="{W-40}" y2="86"/>')
    s.append(f'<text class="recband" x="52" y="80">RECEPTION — where history would step in · <tspan class="none">none coded on this song</tspan></text>')
    for ri, r in enumerate(RESIDUALS):
        x = r["x"]; y0 = NY-58 if r["frm"] == "META" else NY
        ylab = 116 if ri == 0 else 152
        s.append(f'<path class="e-res" d="M {x} {y0} C {x} {y0-60}, {x+58} {150}, {x+58} {96}" marker-end="url(#ah-res)"/>')
        s.append(f'<text class="reslab" x="{x+66}" y="{ylab}">{r["label"]}</text>')
        s.append(f'<text class="ressub" x="{x+66}" y="{ylab+13}">{r["sub"]}</text>')
    s.append(f'<text class="elab lab-b" x="60" y="{178}">RESIDUAL <tspan class="alias">/ BEQUEST</tspan> ↑ — the two gaps the song cannot fill from inside</text>')

    defs = ('<defs>'
      '<marker id="ah-feeds" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 Z" class="mk-a"/></marker>'
      '<marker id="ah-fills" markerWidth="9" markerHeight="9" refX="7" refY="3.2" orient="auto"><path d="M0,0 L7,3.2 L0,6.4 Z" class="mk-a"/></marker>'
      '<marker id="ah-res" markerWidth="10" markerHeight="10" refX="7" refY="3.4" orient="auto"><path d="M0,0 L7,3.4 L0,6.8" fill="none" class="mk-b"/></marker>'
      '</defs>')
    return f'<svg class="v1-svg" viewBox="0 0 {W} {H}" role="img" aria-label="The 8 moves of She Loves You with every coded edge drawn in its family treatment">{defs}{"".join(s)}</svg>'

def build_legend():
    out = []
    for f in FAMILIES:
        rows = []
        for op, alias, connects, count, present in f["edges"]:
            cls = "edge on" if present else "edge off"
            al = '<span class="alias">/ ' + alias + '</span>' if alias != "—" else ''
            ct = '<span class="ct ' + ('yes' if present else 'no') + '">' + count + '</span>'
            rows.append('<div class="' + cls + '"><div class="e-top"><b>' + op + '</b>' + al + ct + '</div>'
                        '<div class="e-cn">' + connects + '</div></div>')
        out.append(f'''<div class="fam {f["cls"]}">
  <div class="fam-h"><span class="swatch"></span><b>FAMILY {f["key"]} · {f["name"]}</b><span class="scope">{f["scope"]}</span></div>
  <div class="fam-t">{"".join(rows)}</div>
</div>''')
    return "".join(out)

BLOCK = '''<div class="viz viz-1" id="viz-1">
<style>
/* VIZ-1 — scoped. Uses only locked gom.css tokens; palette is NOT redefined. */
.viz-1{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:22px 0}
.viz-1 .viz-h{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}
.viz-1 .viz-id{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}
.viz-1 .viz-t{font-family:var(--serif);font-size:19px;color:var(--ink)}
.viz-1 .chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor}
.viz-1 .chip-cand{color:var(--terracotta)}
.viz-1 .chip-actual{color:var(--fern)}
.viz-1 .viz-lede{font-size:14.5px;color:var(--ink-2);margin:6px 0 14px;max-width:82ch;line-height:1.6}
.viz-1 .retired{font-family:var(--mono);font-size:12.5px;text-decoration:line-through;color:var(--ink-3)}
.viz-1 .alias{font-family:var(--mono);font-size:.86em;color:var(--ink-3);font-weight:400}
/* legend */
.viz-1 .v1-legend{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:0 0 14px}
@media(max-width:760px){.viz-1 .v1-legend{grid-template-columns:1fr}}
.viz-1 .fam{border:1px solid var(--rule);border-radius:9px;padding:9px 11px;background:var(--paper)}
.viz-1 .fam-h{display:flex;align-items:center;gap:8px;flex-wrap:wrap;font-size:12.5px;margin-bottom:5px}
.viz-1 .fam-h b{font-family:var(--mono);font-size:11px;letter-spacing:.04em}
.viz-1 .scope{font-size:11px;color:var(--ink-3)}
.viz-1 .swatch{width:34px;height:0;flex:none;border-top-width:3px;border-top-style:solid}
.viz-1 .fam-a .swatch{border-top-color:var(--moss);border-top-style:solid}
.viz-1 .fam-b .swatch{border-top-color:var(--honey);border-top-style:dashed}
.viz-1 .fam-c .swatch{border-top-color:var(--olive);border-top-style:dotted}
.viz-1 .fam-d .swatch{border-top-color:var(--terracotta);border-top-style:double;border-top-width:4px}
.viz-1 .fam-a .fam-h b{color:var(--moss)}.viz-1 .fam-b .fam-h b{color:var(--honey)}
.viz-1 .fam-c .fam-h b{color:var(--olive)}.viz-1 .fam-d .fam-h b{color:var(--terracotta)}
.viz-1 .fam-t{display:flex;flex-direction:column}
.viz-1 .edge{padding:5px 0;border-top:1px solid var(--rule-soft)}
.viz-1 .e-top{display:flex;align-items:baseline;gap:6px;flex-wrap:wrap}
.viz-1 .e-top b{font-family:var(--mono);font-size:10.5px;letter-spacing:.02em;color:var(--ink)}
.viz-1 .e-cn{font-size:10.5px;color:var(--ink-3);margin-top:1px;line-height:1.4}
.viz-1 .ct{margin-left:auto;font-family:var(--mono);font-size:9.5px;text-align:right}
.viz-1 .ct.yes{color:var(--fern);font-weight:600}
.viz-1 .ct.no{color:var(--ink-3)}
.viz-1 .edge.off{opacity:.55}
.viz-1 .edge.off .e-top b{font-weight:400;color:var(--ink-2)}
/* svg */
.viz-1 .v1-scroll{overflow-x:auto;border:1px solid var(--rule-soft);border-radius:9px;background:var(--paper)}
.viz-1 .v1-svg{display:block;width:100%;min-width:1000px;height:auto}
.viz-1 .metabox{fill:none;stroke:var(--sage);stroke-width:1.4;stroke-dasharray:2 4}
.viz-1 .metalab{font-family:var(--mono);font-size:10px;font-weight:600;fill:var(--moss);letter-spacing:.03em}
.viz-1 .metasub{font-family:var(--sans);font-size:9.5px;fill:var(--ink-3)}
.viz-1 .node rect{fill:var(--paper-3);stroke:var(--rule);stroke-width:1.3}
.viz-1 .node.star rect{stroke:var(--fern);stroke-width:2.2;fill:var(--paper-2)}
.viz-1 .nid{font-family:var(--mono);font-size:8.5px;fill:var(--ink-3);letter-spacing:.03em}
.viz-1 .node.star .nid{fill:var(--fern);font-weight:600}
.viz-1 .nop{font-family:var(--serif);font-size:13px;fill:var(--ink)}
.viz-1 .nwho{font-family:var(--sans);font-size:9px;fill:var(--ink-3)}
.viz-1 .ntyp{font-family:var(--mono);font-size:8px;fill:var(--ink-3)}
/* FAMILY A — solid, filled arrowhead */
.viz-1 .e-feeds{stroke:var(--moss);stroke-width:2.4;fill:none}
.viz-1 .e-fills{stroke:var(--moss);stroke-width:2;fill:none;stroke-dasharray:9 3}
.viz-1 .mk-a{fill:var(--moss)}
/* FAMILY B — dashed, open chevron */
.viz-1 .e-res{stroke:var(--honey);stroke-width:2.2;fill:none;stroke-dasharray:7 4}
.viz-1 .mk-b{stroke:var(--honey);stroke-width:1.6}
.viz-1 .recline{stroke:var(--rule);stroke-width:1;stroke-dasharray:3 5}
.viz-1 .recband{font-family:var(--mono);font-size:9.5px;fill:var(--ink-3);letter-spacing:.04em}
.viz-1 .recband .none{color:var(--ink-3);fill:var(--terracotta)}
.viz-1 .elab{font-family:var(--mono);font-size:10px;letter-spacing:.03em}
.viz-1 .lab-a,.viz-1 .lab-a2{fill:var(--moss)}
.viz-1 .lab-b{fill:var(--honey)}
.viz-1 .bk{fill:var(--terracotta);font-weight:600}
.viz-1 .moneylab{font-family:var(--mono);font-size:9px;fill:var(--fern);font-weight:600}
.viz-1 .rolelab{font-family:var(--mono);font-size:8.5px;fill:var(--ink-3);text-anchor:middle}
.viz-1 .reslab{font-family:var(--serif);font-size:12px;fill:var(--ink);font-weight:600}
.viz-1 .ressub{font-family:var(--sans);font-size:9px;fill:var(--ink-3)}
/* the IRR177-removed layer */
.viz-1 .corrected-layer[hidden]{display:none}
.viz-1 .e-corrected{stroke:var(--ink-3);stroke-width:1.4;fill:none;stroke-dasharray:2 3;opacity:.75}
.viz-1 .corrlab{font-family:var(--mono);font-size:8px;fill:var(--ink-3);text-anchor:middle;text-decoration:line-through}
/* controls + none-of */
.viz-1 .v1-ctl{display:flex;gap:10px;align-items:flex-start;flex-wrap:wrap;margin:10px 0 0}
.viz-1 .v1-btn{font-family:var(--sans);font-size:12.5px;font-weight:600;padding:6px 13px;border-radius:8px;border:1px solid var(--rule);background:var(--paper);color:var(--ink);cursor:pointer}
.viz-1 .v1-btn[aria-pressed=true]{background:var(--moss);color:var(--paper);border-color:var(--moss)}
.viz-1 .v1-ctl-note{font-size:11.5px;color:var(--ink-3);flex:1;min-width:240px;line-height:1.5}
.viz-1 .v1-none{margin:14px 0 0;border-left:3px solid var(--terracotta);background:var(--paper-2);border-radius:0 9px 9px 0;padding:11px 14px;font-size:13px;color:var(--ink-2)}
.viz-1 .v1-none ul{margin:6px 0 0;padding-left:18px}
.viz-1 .v1-none li{margin:4px 0}
.viz-1 .viz-src{font-family:var(--mono);font-size:10.5px;color:var(--ink-3);margin:12px 0 0;line-height:1.65}
@media(prefers-reduced-motion:reduce){.viz-1 *{transition:none!important;animation:none!important}}
</style>
  <div class="viz-h">
    <span class="viz-id">VIZ-1</span>
    <span class="viz-t">The edge legend, and the song's edges re-drawn</span>
    <span class="chip chip-cand">candidate</span>
    <span class="chip chip-actual">all edges ACTUAL — coded from the text</span>
  </div>
  <p class="viz-lede">Every edge the instrument found in "She Loves You", drawn in its family's treatment and named twice — the <b>operational</b> name a coder checks, and the <b>alias</b> a reader reads. The old diagram's labels (<span class="retired">production · completion · reception</span>) were the <b>retired gen-1 names</b>; these are gen-3, post-IRR179. <b>Colour is never the only signal</b> — each family also carries its own dash and arrowhead.</p>

  <div class="v1-legend">__LEGEND__</div>

  <div class="v1-scroll">__SVG__</div>

  <div class="v1-ctl">
    <button type="button" class="v1-btn" id="v1-toggle" aria-pressed="false">Show what IRR177 removed</button>
    <span class="v1-ctl-note">Five cold coders read the same 8 moves and <b>deleted three arrows the author had drawn</b> — each became a residual. The measurement correcting the reference is the mechanism, so it ships visible.</span>
  </div>

  <div class="v1-none">
    <b>What the song has none of</b> — the question the old diagram couldn't answer.
    <ul>
      <li><b>No interpretive fork.</b> FORKS and REINTERPRETS are empty: no later reader has been coded closing either residual, so nothing has diverged yet.</li>
      <li><b>No cross-text edges at all.</b> Families C and D need a <i>pair</i> — a move here and a move there. The song has no cross-text pair coded, so CONVERGENCE and DIVERGENCE are available-and-unused, not absent-from-the-world. This is where the comparative claim would live, and it is not yet made.</li>
      <li><b>No ELABORATES, no SCAFFOLDS.</b> Both are Family A edges the pilot did not code on this text.</li>
    </ul>
  </div>

  <p class="viz-src">Sources — moves, edges and residuals: <code>field_ed/negative_space_pilot_8move_she_loves_you_2026-07-10.md</code> (paraphrase only; no lyric is reproduced). Families, names and coding definitions: the §A6 v2 table above (<code>edge_taxonomy_v2_2026-07-11.md</code>, IRR179). Corrections: IRR177 cold-cohort run. Nothing here is invented; Stage&nbsp;6&nbsp;=&nbsp;0.</p>
<script>
(function(){
  var b=document.getElementById('v1-toggle'), g=document.getElementById('v1-corrected');
  if(!b||!g) return;
  b.addEventListener('click',function(){
    var on=b.getAttribute('aria-pressed')==='true';
    b.setAttribute('aria-pressed', String(!on));
    if(on){ g.setAttribute('hidden',''); b.textContent='Show what IRR177 removed'; }
    else  { g.removeAttribute('hidden');  b.textContent='Hide what IRR177 removed'; }
  });
})();
</script>
</div>'''

def build(path):
    h = open(path, encoding="utf-8").read()
    block = BLOCK.replace("__LEGEND__", build_legend()).replace("__SVG__", build_svg())
    pat = re.compile(r'<div class="vizslot"[^>]*>\s*<div class="vs-h"><span class="vs-id">VIZ-1</span>.*?</div>\s*</div>', re.S)
    assert pat.search(h), "VIZ-1 vizslot not matched"
    h2 = pat.sub(lambda _: block, h, count=1)
    assert 'class="vizslot"' in h2, "other slots must survive"
    open(path, "w", encoding="utf-8").write(h2)
    left = h2.count('class="vizslot"')
    print(f"VIZ-1 installed · {len(MOVES)} moves · {len(FILLS)} FILLS · {len(CORRECTED)} corrected · {len(RESIDUALS)} residuals · slots left: {left}")

if __name__ == "__main__":
    build(sys.argv[1])
