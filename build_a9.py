#!/usr/bin/env python3
"""
build_a9.py — insert (idempotently) the A9 "See the full move" section into
method-canonical.html.

Milestone (b) of the tree-revamp brief (BRIEF_to_designSB_tree_revamp_2026-07-18.md §2b):
the sidebar has promised "A9 · Worked: She Loves You" (#a-ex) for a while, but NO section
with id="a-ex" exists — a dangling nav link. That gap IS the thing she keeps asking for and
that bit her in the Saquib call: "there's nowhere I can actually see the fully-diagrammed
'She Loves You' song anymore, with the moves, the edges."

This builds that section: the ACTUAL song, coded end-to-end — the 8 moves, the edges drawn,
the 3-way gap resolution, and the meta-move. All ACTUAL/ATTESTED ink (no GENERATED content;
the tree/fan Path-A generation is separate). Carries the 4-beat TL;DR card (brief §3) as the
first instance of that pattern.

DATA SOURCE (arbiter): field_ed/negative_space_pilot_8move_she_loves_you_2026-07-10.md
  + IRR177 cold-cohort correction (research/00_irr/irr177_*_reconciliation_2026-07-10.md).
Numbers/status are the pilot's; the un-voiced-woman reading is flagged as a reader-lens
(cold 1/5), NOT a form-produced gap — per R4 (status on its face) + R1 (don't invent a datum).

RULES honored: R1 (no invented datum — the depth-6/7 fan is NOT here; residuals carry their
cold vote-counts), R2 (ACTUAL vs ATTESTED never share ink with GENERATED — this view is all
ACTUAL/ATTESTED), R4 (every claim carries status), R5 (show the mechanism), R6 (gom.css tokens
only, both themes, colour never the only channel), R7 (self-contained, $0).
"""
import re, sys, pathlib

HTML = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")

# ── the 8 moves (ACTUAL coding, from the pilot) ──────────────────────────────
# (num, operation, agent→substrate, SAID type, [ (gap, seer, fill|sub, flavor), ... ])
MOVES = [
    ("M1", "hurt (past)",   "you → her",           "narrate",
      [("why you hurt her", "reader", "FILL", "omitted"),
       ("how badly",        "reader", "FILL", "underdetermined"),
       ("reparable?",       "reader", "FILL", "omitted")]),
    ("M2", "suffer",        "she → (self)",         "narrate",
      [("how much she suffered", "reader", "FILL", "underdetermined")]),
    ("M3", "reappraise",    "she → you (char.)",    "narrate",
      [("on what basis she turned", "reader", "FILL", "omitted")]),
    ("M4", "loves",         "she → you",            "report",
      [("her warrant / how known", "reader · narrator", "FILL", "omitted"),
       ("outcome / what it produces", "—", "FILL", "omitted"),
       ("reciprocity", "—", "FILL", "omitted"),
       ("her own interior / voice", "narrator + reader", "— (foreclosed)", "foreclosed")]),
    ("M5", "fear / believe","you → (the loss)",     "assert",
      [("why you believe it's gone", "reader", "FILL", "omitted")]),
    ("M6", "relay / witness","I (friend) → you",    "report",
      [("is the relay accurate", "reader", "— (foreclosed)", "foreclosed"),
       ("the friend's motive", "reader", "FILL", "omitted")]),
    ("M7", "exhort-feel",   "→ you (be glad)",      "directive",
      [("presupposes you're not already glad", "—", "FILL", "presupposed")]),
    ("M8", "exhort-act",    "→ you (apologize)",    "directive",
      [("to whom / how", "reader", "FILL", "omitted"),
       ("presupposes you have pride", "—", "—", "presupposed")]),
]

# ── the completion edges (FILLS, backward onto M4) ───────────────────────────
FILLS = [
    ("M1 + M3", "REASON (negative)", "the backstory removes the obstacle — 'you're not cruel'"),
    ("M2",      "DEGREE",            "'nearly broke her' = she cares a lot"),
    ("M5 + M8", "RECIPROCITY",       "your fear + your urged return = you love her too"),
    ("M6",      "WARRANT",           "'how does the friend know?' — 'I met her, I carry her word'"),
    ("M7 + M8", "OUTCOME",           "what the love produces = be glad + reconcile"),
]

# ── the 3-way gap resolution, IRR177-corrected (the headline) ────────────────
# each: (gap, disposition, mechanism, status-class, status-label)
RESO = [
    ("DEGREE",        "filled internally", "M2 supplies it",                          "fill",  "filled"),
    ("WARRANT",       "filled internally", "M6 supplies it",                          "fill",  "filled"),
    ("OUTCOME",       "filled internally", "M7 + M8 supply it",                        "fill",  "filled"),
    ("REASON (obstacle)", "filled internally", "M1 + M3 remove the obstacle to love", "fill",  "filled"),
    ("why she loves — the positive ground", "RESIDUAL",
        "reappraisal removes an obstacle; it never supplies the positive ground (IRR177 corrected the reference here)",
        "res", "residual · 2/5 explicit, +3 adjacent"),
    ("the addressee's reciprocity — does HE love her back?", "RESIDUAL",
        "never stated; the reliable second residual the FORM produces",
        "res", "residual · 5/5 touch, 3/5 name"),
    ("the friend's motive", "RESIDUAL",
        "the mediator's stake is never given — confirmed cold, every stranger named it",
        "res", "residual · 5/5"),
]

def moves_rows():
    out = []
    for num, op, agent, typ, gaps in MOVES:
        star = ' <span class="a9-star" title="the pivot — everything completes onto it">★</span>' if num == "M4" else ""
        # gap cell: each gap on its own line with seer·fill·flavor
        glines = []
        for g, seer, fill, flav in gaps:
            fore = ' a9-fore' if 'foreclosed' in flav else ''
            glines.append(
                f'<span class="a9-gap{fore}"><b>{g}</b>'
                f'<span class="a9-meta">{seer} · {fill} · {flav}</span></span>')
        gcell = ''.join(glines)
        rowcls = ' class="a9-m4"' if num == "M4" else ""
        out.append(
            f'<tr{rowcls}><td class="a9-mn"><b>{num}</b>{star}</td>'
            f'<td class="a9-op">{op}</td><td class="a9-ag">{agent}</td>'
            f'<td><span class="a9-typ a9-typ-{typ.split("-")[0].split(" ")[0]}">{typ}</span></td>'
            f'<td class="a9-gaps">{gcell}</td></tr>')
    return '\n'.join(out)

def fills_rows():
    return '\n'.join(
        f'<tr><td class="a9-from"><b>{frm}</b></td><td class="a9-to">{to}</td>'
        f'<td class="a9-mech">{mech}</td></tr>'
        for frm, to, mech in FILLS)

def reso_rows():
    out = []
    for gap, disp, mech, cls, lab in RESO:
        out.append(
            f'<tr class="a9-r-{cls}"><td class="a9-rg">{gap}</td>'
            f'<td><span class="a9-pill a9-pill-{cls}">{lab}</span></td>'
            f'<td class="a9-mech">{mech}</td></tr>')
    return '\n'.join(out)

SECTION = f'''<section class="sec" id="a-ex">
  <div class="sec-k"><span class="n">A9</span><h2>Worked end&#8209;to&#8209;end — "She Loves You"</h2></div>
  <p class="sec-lede">The one place to <b>see the full move</b>: the real song, coded in full — the eight moves, the edges that connect them, and the two gaps it cannot fill from inside. This is the <b>ACTUAL</b> text every generated tree (§C5) branches off. <span class="a9-jump"><a href="#viz-1">the edge legend is VIZ&#8209;1&nbsp;↑</a></span></p>

  <!-- ══ TL;DR card (the 4-beat header — brief §3 · Saquib's "one slide on what it is") ══ -->
  <div class="a9-tldr">
    <div class="a9-tldr-h"><span class="a9-tldr-k">TL;DR</span><span class="a9-tldr-sub">what this is, in four beats</span></div>
    <ol class="a9-beats">
      <li><b>Why.</b> Before any generation, you have to be able to <i>read the coded song</i> — the ground truth the whole method stands on. This view is that artifact, stable and linkable.</li>
      <li><b>What it shows you that you'd miss otherwise.</b> That the song is an <b>almost self-completing</b> object — seven of its moves quietly answer questions a later move raised — and that the few gaps it <i>can't</i> close from inside are exactly where later readers step in. You only see this once the whole thing is coded.</li>
      <li><b>Inputs → <span class="a9-box">the grammar + the gap detector</span> → outputs.</b> In: the lyric (ACTUAL text). Black box: CORE&#8209;7 per move (§A3) + the edge taxonomy (§A6) + the gap grid (§B). Out: 8 coded moves, the edge graph, and the residual set below.</li>
      <li><b>How it connects.</b> This is the <b>ANALYZE</b> half of the two&#8209;move method (Decision&nbsp;175): <span class="a9-ag2">analyze → generate</span>. Romans&nbsp;8 is this same run on scripture; the tree family (§C5) is what <i>generation</i> does with it.</li>
    </ol>
  </div>

  <!-- ══ 1 · the 8-move spine (ACTUAL coding) ══ -->
  <h3 class="a9-h">The eight moves <span class="a9-chip a9-chip-actual">ACTUAL · coded</span></h3>
  <p class="a9-note">Each move: its <b>operation</b>, who acts on what, its <b>SAID type</b>, and — the money column — the <b>gap</b> it leaves (with <i>who could see it · how it could close · its flavour</i>). <span class="a9-fore-key">Shaded gaps are <b>foreclosed</b></span> — the form structurally forbids the fill.</p>
  <div class="a9-scroll"><table class="a9-t a9-moves">
    <tr><th>Move</th><th>Operation</th><th>Agent → substrate</th><th>Type</th><th>The gap — <span class="a9-meta-h">seer · fill|sub · flavour</span></th></tr>
    {moves_rows()}
  </table></div>

  <!-- ══ 2 · the edges drawn ══ -->
  <h3 class="a9-h">The song as a graph <span class="a9-chip a9-chip-actual">ACTUAL</span></h3>
  <div class="a9-edges">
    <div class="a9-edge-card a9-feeds">
      <div class="a9-ec-h"><span class="m">FEEDS</span> — the production chain, forward</div>
      <div class="a9-chain">M1<span class="a9-arr">→</span>M2<span class="a9-arr">→</span>M3<span class="a9-arr">→</span><b class="a9-piv">M4</b><span class="a9-arr">→</span>M5<span class="a9-arr">→</span>M6<span class="a9-arr">→</span>M7<span class="a9-arr">→</span>M8</div>
      <p class="a9-ec-cap">Each move's output becomes the next move's input. The wound is felt, the feeling is reappraised, the reappraisal grounds the love, and so on.</p>
    </div>
    <div class="a9-edge-card a9-compose">
      <div class="a9-ec-h"><span class="m">COMPOSES</span> — the meta-move holds them all</div>
      <p class="a9-ec-cap"><b>The friend persuades you to reconcile with her</b> (because she loves you). Read as one move, the whole song's agent is <b>the friend</b>; it <b>contains</b> M1–M8, and the edges below are its internal wiring. Its <i>own</i> gaps — the friend's motive, and whether the friend is reliable — no component fills.</p>
    </div>
  </div>
  <h4 class="a9-h4"><span class="m">FILLS</span> — the completion edges, mostly <b>backward onto M4</b></h4>
  <p class="a9-note">This is the surprise: later and other moves quietly supply values M4 left open. The song answers its own questions.</p>
  <div class="a9-scroll"><table class="a9-t a9-fills">
    <tr><th>These moves…</th><th>…fill M4's</th><th>The mechanism</th></tr>
    {fills_rows()}
  </table></div>

  <!-- ══ 3 · the 3-way resolution (the headline, IRR177-corrected) ══ -->
  <h3 class="a9-h">The headline — run every M4 gap through <span class="a9-mono">{{ filled · residual }}</span></h3>
  <div class="a9-flag">
    <span class="a9-flag-k">Read this before the table</span>
    The <b>reference</b> coding (by the method author) called five of M4's gaps self-filled and named the <i>un-voiced woman</i> as the deepest residual. <b>IRR177 ran the same eight moves past five cold cohorts</b> and corrected two things — the honest, load-bearing part. (a) The reliable second residual is the <b>addressee's reciprocity</b> (does <i>he</i> love her back? — 5/5 touched it), <b>not</b> her voice (only 1/5 found that cold; it is a real but <b>reader-supplied lens</b>, not a gap the form produces). (b) "Why she loves you" is a <b>third residual</b>, not filled — reappraisal removes an obstacle, it doesn't supply the ground. This correction is itself a specimen: the primed author saw a gap the cold coders didn't. <span class="a9-cite">ATTESTED · IRR177, 5 cold cohorts</span>
  </div>
  <div class="a9-scroll"><table class="a9-t a9-reso">
    <tr><th>M4's gap</th><th>Disposition</th><th>Mechanism</th></tr>
    {reso_rows()}
  </table></div>
  <p class="a9-verdict"><b>≈ 80% self-completing.</b> Four of M4's gaps close from inside the song; three stay <b>residual</b> and are <span class="m">BEQUEATHS</span>'d forward — to reception (§A6 Family&nbsp;B). Those three residuals are where history (Augustine on Romans; a woman's-POV cover of the song) steps in. <span class="a9-chip a9-chip-attest">ATTESTED · DeepSeek: ~6 unfilled of ~29</span></p>

  <div class="postit"><span class="pin">Why this view exists — the thing that went missing</span>
    You've said more than once that there was <i>nowhere</i> to see the fully-diagrammed song — "with the moves, the edges" — and that it bit you in the Saquib call. The sidebar had promised <b>A9 · Worked: She Loves You</b> but the anchor was never built; that's fixed now. This is the stable artifact: send it as a link, and it introduces itself (the TL;DR card) before it shows the work. The <b>Romans 8</b> run will live beside it as the second worked example, same shape. <b>Everything here is ACTUAL or ATTESTED</b> — no generated ink; the invented worlds start at §C5.
  </div>
</section>

'''

STYLE = '''<style>
/* A9 "see the full move" — scoped; gom.css tokens only, palette NOT redefined; both themes */
#a-ex .a9-jump{font-size:12.5px;margin-left:6px}
#a-ex .a9-jump a{color:var(--fern)}
#a-ex .a9-tldr{border:1px solid var(--rule);border-left:4px solid var(--fern);border-radius:10px;background:var(--paper-3);padding:14px 16px;margin:16px 0 22px}
#a-ex .a9-tldr-h{display:flex;align-items:baseline;gap:9px;margin-bottom:8px}
#a-ex .a9-tldr-k{font-family:var(--mono);font-size:11px;font-weight:700;letter-spacing:.08em;color:var(--paper);background:var(--fern);padding:2px 9px;border-radius:5px}
#a-ex .a9-tldr-sub{font-size:12px;color:var(--ink-3);font-style:italic}
#a-ex .a9-beats{margin:0;padding-left:20px;display:grid;gap:7px}
#a-ex .a9-beats li{font-size:14px;color:var(--ink-2);line-height:1.55}
#a-ex .a9-box{font-family:var(--mono);font-size:.86em;background:var(--paper-2);padding:1px 6px;border-radius:4px;color:var(--moss)}
#a-ex .a9-ag2,#a-ex .a9-mono{font-family:var(--mono);font-size:.9em;color:var(--moss)}
#a-ex .a9-h{font-family:var(--serif);font-size:18px;color:var(--ink);margin:26px 0 4px;display:flex;align-items:center;gap:10px;flex-wrap:wrap}
#a-ex .a9-h4{font-family:var(--serif);font-size:15px;color:var(--ink);margin:18px 0 2px}
#a-ex .a9-note{font-size:13px;color:var(--ink-3);margin:2px 0 10px;max-width:84ch;line-height:1.55}
#a-ex .a9-fore-key b{color:var(--terracotta)}
#a-ex .a9-chip{font-family:var(--mono);font-size:9.5px;letter-spacing:.05em;text-transform:uppercase;padding:2px 8px;border-radius:20px;border:1px solid currentColor;white-space:nowrap}
#a-ex .a9-chip-actual{color:var(--fern)}
#a-ex .a9-chip-attest{color:var(--olive)}
/* tables scroll in their own container (R6) */
#a-ex .a9-scroll{overflow-x:auto;margin:8px 0 4px;border:1px solid var(--rule);border-radius:9px}
#a-ex .a9-t{border-collapse:collapse;width:100%;min-width:560px;font-size:13px}
#a-ex .a9-t th{background:var(--paper-2);text-align:left;padding:7px 10px;font-family:var(--sans);font-size:10.5px;letter-spacing:.04em;text-transform:uppercase;color:var(--ink-2);font-weight:700;border-bottom:1px solid var(--rule)}
#a-ex .a9-t td{padding:8px 10px;border-bottom:1px solid var(--rule);vertical-align:top;color:var(--ink-2)}
#a-ex .a9-t tr:last-child td{border-bottom:0}
#a-ex .a9-meta-h{font-family:var(--mono);font-size:9px;text-transform:none;letter-spacing:0;color:var(--ink-3);font-weight:400}
#a-ex .a9-mn{white-space:nowrap;font-family:var(--mono);color:var(--ink)}
#a-ex .a9-star{color:var(--honey);font-size:1.1em}
#a-ex .a9-op{font-weight:600;color:var(--ink)}
#a-ex .a9-ag{font-size:12px;color:var(--ink-3)}
#a-ex tr.a9-m4{background:rgba(224,169,59,.09)}
#a-ex .a9-typ{font-family:var(--mono);font-size:10px;padding:1px 7px;border-radius:20px;letter-spacing:.03em;border:1px solid var(--rule);color:var(--ink-2)}
#a-ex .a9-typ-narrate{background:rgba(63,125,87,.10)}
#a-ex .a9-typ-report{background:rgba(224,169,59,.13)}
#a-ex .a9-typ-assert{background:rgba(110,123,58,.13)}
#a-ex .a9-typ-directive{background:rgba(196,96,47,.11)}
#a-ex .a9-gaps{display:flex;flex-direction:column;gap:5px}
#a-ex .a9-gap{display:flex;flex-direction:column;line-height:1.3}
#a-ex .a9-gap b{font-weight:600;color:var(--ink)}
#a-ex .a9-meta{font-family:var(--mono);font-size:10px;color:var(--ink-3)}
#a-ex .a9-fore{background:rgba(196,96,47,.10);border-left:2px solid var(--terracotta);padding:3px 7px;border-radius:0 5px 5px 0}
#a-ex .a9-fore b{color:var(--terracotta)}
/* edges */
#a-ex .a9-edges{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0 2px}
@media(max-width:720px){#a-ex .a9-edges{grid-template-columns:1fr}}
#a-ex .a9-edge-card{border:1px solid var(--rule);border-radius:9px;padding:11px 13px;background:var(--paper)}
#a-ex .a9-ec-h{font-size:13px;color:var(--ink);margin-bottom:7px}
#a-ex .m{font-family:var(--mono);font-size:.92em;font-weight:600;color:var(--moss);letter-spacing:.02em}
#a-ex .a9-chain{font-family:var(--mono);font-size:15px;color:var(--ink-2);letter-spacing:.04em;padding:4px 0}
#a-ex .a9-arr{color:var(--fern);margin:0 3px}
#a-ex .a9-piv{color:var(--paper);background:var(--honey);padding:0 5px;border-radius:4px}
#a-ex .a9-ec-cap{font-size:12px;color:var(--ink-3);line-height:1.5;margin:6px 0 0}
#a-ex .a9-from{white-space:nowrap;font-family:var(--mono);color:var(--ink);font-size:12px}
#a-ex .a9-to{white-space:nowrap;font-weight:700;color:var(--moss);font-size:12px}
#a-ex .a9-mech{font-size:12px;color:var(--ink-3);line-height:1.45}
/* resolution */
#a-ex .a9-flag{border:1px solid var(--rule);border-left:4px solid var(--honey);border-radius:0 9px 9px 0;background:var(--paper-2);padding:11px 14px;margin:10px 0;font-size:13px;color:var(--ink-2);line-height:1.55}
#a-ex .a9-flag-k{display:block;font-family:var(--sans);font-size:10px;letter-spacing:.06em;text-transform:uppercase;font-weight:700;color:var(--olive);margin-bottom:5px}
#a-ex .a9-cite,#a-ex .a9-chip-attest{font-family:var(--mono);font-size:9.5px;color:var(--olive)}
#a-ex .a9-rg{color:var(--ink);font-weight:600;font-size:12.5px}
#a-ex tr.a9-r-fill{background:rgba(63,125,87,.06)}
#a-ex tr.a9-r-res{background:rgba(196,96,47,.07)}
#a-ex .a9-pill{font-family:var(--mono);font-size:10px;padding:2px 8px;border-radius:20px;white-space:nowrap;font-weight:600}
#a-ex .a9-pill-fill{background:rgba(63,125,87,.15);color:var(--moss)}
#a-ex .a9-pill-res{background:rgba(196,96,47,.14);color:var(--terracotta)}
#a-ex .a9-verdict{font-size:13.5px;color:var(--ink-2);line-height:1.6;margin:12px 0 2px;max-width:86ch}
</style>
'''

def main():
    h = HTML.read_text()
    block = STYLE + SECTION
    marker = '<!-- ══ A9 SEE-THE-FULL-MOVE (built) ══ -->\n'
    wrapped = marker + block + '<!-- ══ /A9 ══ -->\n'

    if '<!-- ══ A9 SEE-THE-FULL-MOVE (built) ══ -->' in h:
        # idempotent re-render: replace the whole built block
        h = re.sub(r'<!-- ══ A9 SEE-THE-FULL-MOVE \(built\) ══ -->.*?<!-- ══ /A9 ══ -->\n',
                   wrapped, h, flags=re.S)
        print("re-rendered existing A9 block")
    else:
        # first build: insert before the B · GAP DETECTOR comment / #b-triad section
        anchor = h.find('<!-- ═══════════════ B · GAP DETECTOR')
        if anchor == -1:
            anchor = h.find('<section class="sec" id="b-triad">')
        assert anchor != -1, "could not find insertion point (B section)"
        h = h[:anchor] + wrapped + h[anchor:]
        print("inserted new A9 block before B · GAP DETECTOR")

    HTML.write_text(h)
    # sanity
    assert h.count('id="a-ex"') == 1, f'expected 1 a-ex, got {h.count(chr(34)+"a-ex"+chr(34))}'
    for must in ("FEEDS", "COMPOSES", "BEQUEATHS", "IRR177", "addressee's reciprocity", "ANALYZE"):
        assert must in h, f'missing {must!r}'
    for banned in ("frame-jump", "IN-FRAME", "RESIDUAL /", "convergence everywhere"):
        assert banned not in SECTION, f'banned token present: {banned!r}'
    print("a-ex sections:", h.count('id="a-ex"'), "| bytes now:", len(h))

if __name__ == "__main__":
    main()
