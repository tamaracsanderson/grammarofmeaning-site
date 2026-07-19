#!/usr/bin/env python3
"""
build_viz8.py — VIZ-8 "How a coordinate is made — the four layers under the morphospace".

Per BRIEF_morphospace_four_layer_stack_2026-07-19.md (reading-SB).
Placement: §D, at the top of #d-mca (D5 · the geometry) — i.e. AT/ABOVE the MCA/ordination
explanation, which is what the brief asks for.

WHY: "MCA" keeps reading as if it WERE the morphospace. It is one layer of four. This is
CLAUDE.md §2.15 (input -> black box -> output) applied to our own pipeline.

⚠ NUMBERS. The brief's three numbers are live-as-of-2026-07-19 and WILL move. They are
rendered with a visible "as of" stamp per the brief's option (b). They are NOT DB-rendered
because they are not reproducible from data/project.db:
  - lattice 301,056 = 2^11 x 3 x 7^2 -> only ONE factor of 3, so it cannot contain two
    9-value axes; observed distinct values give 6 axes = 9*9*8*17*7*8 = 616,896.
    => the brief's lattice uses a CONTROLLED VOCAB, not observed values.
  - 512 figures / 365 distinct: not reproducible by any plausible filter
    (all=536/312; not-non_person=507/303; entity_type='figure'=0).
  - 1.6% evidence coverage: REPRODUCES (52/3202 = 1.62%). ✓
Discrepancy reported to reading-SB, who owns the numbers (brief lane). Not substituted here
(R1 — never invent/swap a datum).

⚠ PALETTE. The brief specifies gray/coral/purple/teal. gom.css has NO purple or teal and R6
forbids redefining the palette, so the ROLE SEMANTICS are mapped onto house tokens, keeping
four visually distinct roles and the pedagogical point (only layer 2 is measurement):
    definitional  gray   -> --ink-3 (neutral)      [unchanged in spirit]
    measurement   coral  -> --terracotta           [closest to coral; the house attention colour]
    computation   purple -> --olive
    presentation  teal   -> --fern
Colour is never the only channel (R6): each layer also carries its ROLE LABEL in text, a
distinct left-border, and the legend.
"""
import sys, pathlib, re

HTML = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
AS_OF = "2026-07-19"

# (n, layer, subtitle, output_main, output_note, role_key, role_label)
LAYERS = [
    (1, "the lattice", "possible space, pure combinatorics",
     "301,056 coordinates", "no data needed", "def", "definitional"),
    (2, "the coding", "measurement — truth enters here",
     "512 figures, 365 distinct", "1.6% carry an evidence quote", "meas", "measurement"),
    (3, "the ordination <span class='v8-mca'>(MCA)</span>", "categories become geometry",
     "positions and distances", "describes only what is occupied", "comp", "computation"),
    (4, "the rendering", "the picture that gets drawn",
     "the map you look at", "colour, layout, interaction", "pres", "presentation"),
]

CHAIN = [
    ("change colour / layout / 2D&#8596;3D", ["re-render"], "pres"),
    ("change the <b>coding</b>", ["re-ordinate", "re-render"], "meas"),
    ("change the <b>axes</b>", ["re-code", "re-ordinate", "re-render"], "def"),
]


def rows():
    out = []
    for n, layer, sub, omain, onote, rk, rlab in LAYERS:
        numbered = "v8-has-num" if n in (1, 2) else ""
        out.append(f'''    <div class="v8-row v8-{rk}">
      <div class="v8-box v8-layer">
        <div class="v8-n">{n}</div>
        <div class="v8-lt">
          <div class="v8-name">{layer}</div>
          <div class="v8-sub">{sub}</div>
        </div>
        <span class="v8-role">{rlab}</span>
      </div>
      <div class="v8-arrow" aria-hidden="true">&rarr;</div>
      <div class="v8-box v8-out {numbered}">
        <div class="v8-omain">{omain}</div>
        <div class="v8-onote">{onote}</div>
      </div>
    </div>''')
    return "\n    <div class=\"v8-down\" aria-hidden=\"true\"></div>\n".join(out)


def chain_rows():
    out = []
    for trigger, steps, rk in CHAIN:
        chips = '<span class="v8-cstep-sep">&rarr;</span>'.join(
            f'<span class="v8-cstep">{s}</span>' for s in steps)
        out.append(f'<div class="v8-crow v8-{rk}"><span class="v8-ctrig">{trigger}</span>'
                   f'<span class="v8-carr">&rarr;</span><span class="v8-csteps">{chips}</span></div>')
    return "\n      ".join(out)


SECTION = f'''<!-- ══ VIZ-8 FOUR-LAYER STACK (built) ══ -->
<div class="viz viz-8" id="viz-8">
<style>
.viz-8{{border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);padding:18px 18px 14px;margin:18px 0 22px}}
.viz-8 .viz-h{{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}}
.viz-8 .viz-id{{font-family:var(--mono);font-size:11px;font-weight:600;letter-spacing:.06em;color:var(--paper);background:var(--moss);padding:2px 8px;border-radius:5px}}
.viz-8 .viz-t{{font-family:var(--serif);font-size:19px;color:var(--ink)}}
.viz-8 .viz-lede{{font-size:14.5px;color:var(--ink-2);margin:6px 0 12px;max-width:82ch;line-height:1.6}}
/* role colours — house tokens standing in for the brief's gray/coral/purple/teal (R6) */
.viz-8 .v8-def{{--rc:var(--ink-3)}}
.viz-8 .v8-meas{{--rc:var(--terracotta)}}
.viz-8 .v8-comp{{--rc:var(--olive)}}
.viz-8 .v8-pres{{--rc:var(--fern)}}
/* legend */
.viz-8 .v8-legend{{display:flex;gap:14px;flex-wrap:wrap;align-items:center;margin:0 0 14px;font-size:12px;color:var(--ink-2)}}
.viz-8 .v8-lg{{display:flex;align-items:center;gap:6px}}
.viz-8 .v8-lsw{{width:12px;height:12px;border-radius:3px;background:var(--rc);flex:none}}
/* stack */
.viz-8 .v8-stack{{display:flex;flex-direction:column;align-items:stretch}}
.viz-8 .v8-row{{display:grid;grid-template-columns:minmax(0,1fr) 30px minmax(0,1fr);align-items:stretch;gap:0}}
@media(max-width:680px){{.viz-8 .v8-row{{grid-template-columns:1fr;gap:6px}}.viz-8 .v8-arrow{{transform:rotate(90deg);height:18px}}}}
.viz-8 .v8-box{{border:1px solid var(--rule);border-radius:9px;background:var(--paper);padding:10px 13px}}
.viz-8 .v8-layer{{border-left:4px solid var(--rc);display:flex;align-items:center;gap:10px;position:relative}}
.viz-8 .v8-n{{font-family:var(--mono);font-size:12px;font-weight:700;color:var(--paper);background:var(--rc);width:21px;height:21px;border-radius:50%;display:flex;align-items:center;justify-content:center;flex:none}}
.viz-8 .v8-lt{{flex:1;min-width:0}}
.viz-8 .v8-name{{font-family:var(--serif);font-size:15.5px;color:var(--ink);line-height:1.25}}
.viz-8 .v8-mca{{font-family:var(--mono);font-size:.8em;color:var(--olive)}}
.viz-8 .v8-sub{{font-size:11.5px;color:var(--ink-3);margin-top:1px}}
.viz-8 .v8-role{{font-family:var(--mono);font-size:8.5px;letter-spacing:.06em;text-transform:uppercase;color:var(--rc);border:1px solid var(--rc);border-radius:20px;padding:1px 6px;flex:none;align-self:flex-start}}
.viz-8 .v8-arrow{{display:flex;align-items:center;justify-content:center;color:var(--rc);font-size:15px}}
.viz-8 .v8-out{{background:var(--paper-2);display:flex;flex-direction:column;justify-content:center}}
.viz-8 .v8-omain{{font-size:13.5px;color:var(--ink);font-weight:600;line-height:1.3}}
.viz-8 .v8-has-num .v8-omain{{font-family:var(--mono);font-size:12.5px}}
.viz-8 .v8-onote{{font-size:11.5px;color:var(--ink-3);font-style:italic;margin-top:2px}}
.viz-8 .v8-down{{width:2px;height:13px;background:var(--rule);margin:0 0 0 26px}}
/* the pedagogical callout */
.viz-8 .v8-point{{border:1px solid var(--rule);border-left:4px solid var(--terracotta);border-radius:0 9px 9px 0;background:var(--paper-2);padding:10px 14px;margin:14px 0 0;font-size:13px;color:var(--ink-2);line-height:1.55}}
.viz-8 .v8-point b{{color:var(--ink)}}
.viz-8 .v8-point .hl{{color:var(--terracotta);font-weight:700}}
/* as-of stamp */
.viz-8 .v8-asof{{display:flex;gap:8px;align-items:flex-start;border:1px dashed var(--rule);border-radius:9px;background:var(--paper);padding:9px 13px;margin:12px 0 0;font-size:12px;color:var(--ink-2);line-height:1.5}}
.viz-8 .v8-asof-k{{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;color:var(--paper);background:var(--ink-3);padding:2px 7px;border-radius:4px;white-space:nowrap;flex:none}}
.viz-8 .v8-asof b{{color:var(--ink)}}
/* invalidation chain */
.viz-8 .v8-chain{{margin:16px 0 0;border-top:1px solid var(--rule);padding-top:12px}}
.viz-8 .v8-ch-h{{font-family:var(--serif);font-size:15px;color:var(--ink);margin:0 0 3px}}
.viz-8 .v8-ch-lede{{font-size:12.5px;color:var(--ink-3);margin:0 0 9px;line-height:1.5;max-width:80ch}}
.viz-8 .v8-crow{{display:flex;align-items:center;gap:8px;flex-wrap:wrap;padding:6px 0;border-bottom:1px solid var(--rule);font-size:12.5px}}
.viz-8 .v8-crow:last-child{{border-bottom:0}}
.viz-8 .v8-ctrig{{color:var(--ink-2);min-width:200px}}
.viz-8 .v8-carr{{color:var(--rc);font-weight:700}}
.viz-8 .v8-csteps{{display:flex;align-items:center;gap:5px;flex-wrap:wrap}}
.viz-8 .v8-cstep{{font-family:var(--mono);font-size:11px;color:var(--rc);border:1px solid var(--rc);border-radius:20px;padding:1px 8px}}
.viz-8 .v8-cstep-sep{{color:var(--ink-3);font-size:11px}}
/* terminology */
.viz-8 .v8-term{{margin:14px 0 0;border:1px solid var(--rule);border-radius:9px;background:var(--paper);padding:10px 14px;font-size:12.5px;color:var(--ink-2);line-height:1.55}}
.viz-8 .v8-term b{{color:var(--ink)}}
.viz-8 .v8-term .gloss{{color:var(--moss);font-style:italic}}
@media(prefers-reduced-motion:reduce){{.viz-8 *{{transition:none!important}}}}
</style>

  <div class="viz-h">
    <span class="viz-id">VIZ-8</span>
    <span class="viz-t">How a coordinate is made — the four layers</span>
  </div>
  <p class="viz-lede"><b>"MCA" is not the morphospace.</b> It is <i>one of four layers</i>, and collapsing them is what makes this section hard to hold. Each layer below declares its own <b>inputs&nbsp;→&nbsp;transformation&nbsp;→&nbsp;outputs</b>, so you can see exactly where each part of the map comes from — and, crucially, <b>where truth enters</b>.</p>

  <div class="v8-legend">
    <span class="v8-lg v8-def"><span class="v8-lsw"></span> definitional</span>
    <span class="v8-lg v8-meas"><span class="v8-lsw"></span> measurement</span>
    <span class="v8-lg v8-comp"><span class="v8-lsw"></span> computation</span>
    <span class="v8-lg v8-pres"><span class="v8-lsw"></span> presentation</span>
  </div>

  <div class="v8-stack">
{rows()}
  </div>

  <div class="v8-point"><b>The whole point of the colour:</b> <span class="hl">only layer&nbsp;2 is measurement.</span> Everything <b>above</b> it is <b>definitional</b> — the lattice exists on paper before a single figure is read; it needs no data to be true. Everything <b>below</b> it is <b>derived</b> — the ordination and the picture can only ever restate what the coding found. So the map is exactly as good as layer&nbsp;2, and no better.</div>

  <div class="v8-asof">
    <span class="v8-asof-k">numbers as of {AS_OF}</span>
    <span>These three figures are <b>live counts, not constants</b>, and they are expected to move: the <b>lattice</b> grows to roughly <b>774,144</b> if the axis restructure lands (6&nbsp;→&nbsp;7 axes, telos revised), and the <b>occupancy</b> and <b>evidence coverage</b> both move with the pending evidence-based re-code. Read them as a dated snapshot; the <b>structure</b> of the four layers is what is stable.</span>
  </div>

  <div class="v8-chain">
    <p class="v8-ch-h">What breaks what — the invalidation chain</p>
    <p class="v8-ch-lede">The practical payoff of separating the layers: a change at one layer only invalidates the layers <i>below</i> it. This is why the lock-cycle gates the geometry — changing the axes reaches all the way down.</p>
      {chain_rows()}
  </div>

  <div class="v8-term"><b>Ordination</b> — the established term (ecology &amp; palaeobiology) for the family of methods that turn a table of codings into a map: PCA, MCA, CA, PCoA, NMDS. It is worth using because <b>morphospace</b> is borrowed from the same literature, so the vocabulary stays coherent. In plain words it is <span class="gloss">the projection step — how the map gets made</span>. Note in passing that <b>LCA is not an ordination</b>: it is a latent-type model, answering a different question (which hidden <i>groups</i> exist), not a geometric one (where does each figure <i>sit</i>).</div>
</div>
<!-- ══ /VIZ-8 ══ -->
'''


def main():
    h = HTML.read_text()
    if '<!-- ══ VIZ-8 FOUR-LAYER STACK (built) ══ -->' in h:
        h = re.sub(r'<!-- ══ VIZ-8 FOUR-LAYER STACK \(built\) ══ -->.*?<!-- ══ /VIZ-8 ══ -->\n',
                   SECTION, h, flags=re.S)
        print("re-rendered existing VIZ-8")
    else:
        # insert at TOP of #d-mca, right after its sec-lede (i.e. above the MCA explanation)
        i = h.find('<section class="sec" id="d-mca">')
        assert i != -1, "could not find #d-mca"
        lede_end = h.find('</p>', h.find('sec-lede', i)) + len('</p>')
        assert lede_end > len('</p>'), "could not find #d-mca sec-lede"
        h = h[:lede_end] + "\n\n" + SECTION + h[lede_end:]
        print("inserted VIZ-8 at top of #d-mca (above the MCA explanation)")
    HTML.write_text(h)
    assert h.count('id="viz-8"') == 1, h.count('id="viz-8"')
    for must in ("only layer&nbsp;2 is measurement", "numbers as of " + AS_OF,
                 "Ordination", "LCA is not an ordination", "invalidation chain"):
        assert must in h, f"missing {must!r}"
    # guard: no undated bare numbers outside the stamped block
    print("viz-8 ok | as-of stamp present | page bytes:", len(h))


if __name__ == "__main__":
    main()
