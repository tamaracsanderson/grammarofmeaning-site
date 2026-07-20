#!/usr/bin/env python3
"""c6fix.py — bring §C6 into line with Decision 186 (the crit blocker), plus items A + B.

§C6 and the working appendix were saying two different things about the single most
important mechanism, ~1,300 lines apart. This makes §C6 current and marks the superseded
approach AS superseded rather than deleting it — the fact that it changed, and why, is
itself method content.

Also folds in the addendum:
  A · "gate on four checks" -> the four checks do FOUR DIFFERENT JOBS (two prune, one
      shapes, one only measures) + the self-report weakness on Sitz/branch-state
  B · "the contract" -> "what's held / what's varied", declared once per RUN, above the loop
  1b · step 3 over-claims: the engine holds the forward spine only; backward FILLS and
      whole-text COMPOSES are a declared narrowing
"""
import sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text(); done = []
def sub(l, o, n):
    global h
    assert o in h, f"NOT FOUND: {l}\n  {o[:150]}"
    h = h.replace(o, n, 1); done.append(l)

# ── B: step 1 is a declaration, not a loop step ──
sub("step 1 · held/varied",
 '<tr><td class="id"><b>1</b></td><td><b>Declare the contract</b></td><td>State what is <b>HELD</b> and what is <b>VARIED</b>. Everything downstream is only interpretable against this declaration.</td></tr>',
 '<tr class="c6-decl"><td class="id"><b>0</b></td><td><b>Declare what\'s held and what\'s varied</b><br><span class="c6-once">once per run — not a loop step</span></td><td><b>VARIED (run&nbsp;A):</b> four axes — <span class="m">E</span> · <span class="m">T</span> · <span class="m">S1</span> · <span class="m">S2</span>, one axis at a time, one step, from the parent\'s value.<br><b>HELD:</b> the other three axes (<span class="m">M</span> · <span class="m">O</span> · <span class="m">G</span>) · the song\'s edge at each position · the source\'s structural slot at each depth · the Sitz ceiling (≤1963) · the tier cuts · the vocabulary.<br><span class="c6-note-i">Run&nbsp;B varies all seven — that difference <i>is</i> the A/B test. The held set is much larger and differently shaped than the varied set, which is why this is a <b>declaration</b> rather than a step: it sits above the loop and is not re-negotiated at each fork.</span></td></tr>')

# ── 1b: step 3 over-claims ──
sub("step 3 · edge narrowing",
 '<tr><td class="id"><b>3</b></td><td><b>Ask what the song\'s own edge demands</b></td><td>Not "what could come next?" but "what does <i>this</i> edge require?" The source\'s structure sets the question; the engine does not invent one.</td></tr>',
 '<tr><td class="id"><b>3</b></td><td><b>Ask what the song\'s own edge demands</b></td><td>Not "what could come next?" but "what does <i>this</i> edge require?" The source\'s structure sets the question; the engine does not invent one.<br><span class="c6-warn"><b>A declared narrowing:</b> the engine holds <b>the forward spine only</b> — one <span class="m">FEEDS</span> edge per position. The song actually carries three families at once (<a href="#viz-1">VIZ-1</a>): <span class="m">FEEDS</span> forward, <span class="m">FILLS</span> running <i>backward</i>, and <span class="m">COMPOSES</span> from every move to the whole. So no generated world can contain a move that <i>answers an earlier gap</i> — a capability the source demonstrably has. <b>The alt tree is edge-poorer than the song by construction.</b> Acceptable for run&nbsp;A; recorded here because it is a narrowing, not a neutral simplification.</span></td></tr>')

# ── THE CRIT BLOCKER: step 4 -> Decision 186 ──
sub("step 4 · generation (D186)",
 '<tr><td class="id"><b>4</b></td><td><b>Generate the codeable kinds</b></td><td>The three below — contrary, between, privation — plus anything that lands <i>beyond</i> the paradigm, which is flagged rather than coded.</td></tr>',
 '<tr><td class="id"><b>4</b></td><td><b>Generate</b> — and it differs by depth <span class="st locked">IRR201 · D186</span></td><td><b>At depth&nbsp;1</b> (the substitution itself) the alternative-kinds below apply: <span class="m">you hurt her</span> → <span class="m">you healed her</span> is a <b>CONTRARY</b>, anchored in the real text.<br><b>At depth&nbsp;≥2 they do not.</b> Generation is by <b>explicit axis perturbation</b> anchored to the <b>source\'s</b> slot at that position — <i>"the epistemic warrant shifts from testimony to speculation, holding telos: harmony, satisfying the FEEDS edge."</i><br><b>Never</b> "a move at distance&nbsp;2" (that scores the instruction, not the move — distance is measured <i>afterwards</i>) and <b>never</b> "the contrary of the previous move": beyond depth&nbsp;1 the thing you would take the contrary <i>of</i> is your own previous guess. <b>The trunk anchors every branch; branches never anchor to each other.</b></td></tr>')

# ── A: step 5 -> four different jobs ──
sub("step 5 · four jobs not four gates",
 '<tr><td class="id"><b>5</b></td><td><b>Gate on four checks</b></td><td>Era (Sitz) · paradigm · path-coherence · state. A failure does not always mean discard — <i>which</i> check failed decides which pile it lands in.</td></tr>',
 '<tr><td class="id"><b>5</b></td><td><b>Run the four checks</b><br><span class="c6-once">two prune · one shapes · one only measures</span></td><td><b>"Gate" is the wrong word for all four</b> — they do different jobs, and the difference is the part most easily misread:<br>· <b>Sitz</b> — <i>prevents and prunes.</i> The barred lexicon is in the prompt, so the model is told upfront; anything returned <span class="m">BARRED</span> is dropped anyway.<br>· <b>branch-state</b> — <i>prunes.</i> A <span class="m">contradiction</span> is dropped.<br>· <b>path-coherence</b> — <i>shapes, prunes nothing.</i> It is the anchoring to the source\'s slot, so it changes what gets generated and leaves less to throw away.<br>· <b>frame / paradigm</b> — <i>prunes nothing at all.</i> It only assigns the tier. <b>It is a ruler, not a filter</b> (IRR199&nbsp;U4).</td></tr>')

# ── the self-report weakness ──
sub("self-report weakness",
 '<h3 class="c6-h">The three codeable kinds — and their geometry</h3>',
 '<div class="flag" style="border-left-color:var(--terracotta)"><span class="pin">A known weakness in two of the four checks</span>\n'
 '    <b>Sitz and branch-state prune on the model\'s own self-report</b> — it answers <span class="m">sitz:IN|BARRED</span> and <span class="m">state:ok|contradiction</span> about its own output. That is the same failure IRR201 named for distance: <b>asking a model to report a property of its answer scores its compliance with the instruction, not the property.</b> The frame check does <i>not</i> have this problem, because the coordinate is computed from the text afterwards. <b>Flagged, fix pending</b> — the honest version, and the more interesting one.\n'
 '  </div>\n\n'
 '  <h3 class="c6-h">The three codeable kinds — and their geometry <span class="c6-sup">depth&nbsp;1 only</span></h3>')

sub("kinds note · superseded",
 'These are the <a href="#b-alt">§B5</a> alternative kinds, with the shape each one has relative to the move it replaces. The geometry column is the part worth holding: they are not three flavours of "different," they differ along <i>different dimensions</i>.',
 'These are the <a href="#b-alt">§B5</a> alternative kinds, with the shape each one has relative to the move it replaces. The geometry column is the part worth holding: they are not three flavours of "different," they differ along <i>different dimensions</i>.<br><br><b class="c6-supx">Superseded beyond depth&nbsp;1 — kept because the change is itself method content.</b> This taxonomy was the generation rule <i>at every fork</i> until IRR201 (Decision&nbsp;186) found unanimously that it degrades from depth&nbsp;2 onward — the thing you would take the contrary of is your own previous guess, and <i>"the contrary of a guess is a double-guess."</i> It still governs <b>depth&nbsp;1</b>, where the anchor is the real text. Beyond that, see step&nbsp;4.')

# styles
sub("c6 styles",
 '#c-engine .c6-h{',
 '#c-engine .c6-decl{background:rgba(224,169,59,.09)}\n'
 '  #c-engine .c6-once{font-family:var(--mono);font-size:10px;color:var(--ink-3);letter-spacing:.03em}\n'
 '  #c-engine .c6-note-i{font-size:11.5px;color:var(--ink-3);display:block;margin-top:5px;line-height:1.5}\n'
 '  #c-engine .c6-warn{display:block;margin-top:6px;font-size:12px;color:var(--ink-2);background:rgba(196,96,47,.07);border-left:2px solid var(--terracotta);padding:6px 9px;border-radius:0 5px 5px 0;line-height:1.5}\n'
 '  #c-engine .c6-sup{font-family:var(--mono);font-size:10px;color:var(--paper);background:var(--terracotta);border-radius:20px;padding:2px 8px;vertical-align:middle}\n'
 '  #c-engine .c6-supx{color:var(--terracotta)}\n'
 '  #c-engine .c6-h{')

p.write_text(h)
print("APPLIED:"); [print("  ✓", d) for d in done]
