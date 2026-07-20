#!/usr/bin/env python3
"""
sweep.py — the post-CLC vocabulary sweep, in ONE pass.

Per reading-SB (2026-07-19): the SPA never reads Neon, so only the lattice NUMBER was ever
parity-gated. Everything else is page content and can land now.

VOCABULARY SOURCED FROM THE RESTRUCTURED STORE (data/project.db), not from the brief:
  7 axes · E 9 · M 13 · O 7 · T 9 · S1 4 · S2 3 · G 8  ->  9*13*7*9*4*3*8 = 707,616
  telos (9): agency-mastery communion fidelity-service flourishing harmony
             justice-world-transformation knowledge-understanding liberation salvation
  S1 evaluative-stance (4): charitable neutral-descriptive reverent suspicious
  S2 hermeneutic-posture (3): literal reductive-deconstructive reparative-integrative
  retired: contemplation (telos), paranoid (stance) · renamed: power-mastery -> agency-mastery

⚠ DATA IS NOT REWRITTEN. `contemplation` x49 and `power-mastery` x10 live inside VIZ-5's
embedded figure coordinates — what those figures were ACTUALLY CODED AS under the earlier
vocabulary. Rewriting them would falsify a coding run. They are LABELLED instead.
"""
import re, sys, pathlib

p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text()
applied = []


def sub(label, old, new, count=1):
    global h
    assert old in h, f"NOT FOUND: {label}\n  {old[:160]}"
    n = h.count(old)
    h = h.replace(old, new, count)
    applied.append(f"{label}  (matched {n}, replaced {count})")


# ─────────── 1. §D2 header + lede ───────────
sub("D2 sec-k",
    '<div class="sec-k"><span class="n">D2</span><h2>The six axes — and every value on them</h2></div>',
    '<div class="sec-k"><span class="n">D2</span><h2>The seven axes — and every value on them</h2></div>')

sub("D2 lede",
    'You asked for four things here: what each axis is, how we got to six, what the values are, and how each value is defined. This is all six, with live counts from the coded corpus.',
    'What each axis is, how the set arrived at <b>seven</b>, what the values are, and how each value is defined. The vocabulary below is the <b>locked post-CLC set</b> (Decisions&nbsp;181/183/184); the figure counts beside each value are from the <b>earlier coding run</b> and are marked where that matters.')

# ─────────── 2. summary table: telos 7->9, stance -> S1 + S2 ───────────
sub("T row",
    '<tr><td class="id"><b>T</b> · telos</td><td>What is it for?</td><td class="n">7</td><td><span class="st cand">all candidate</span></td></tr>',
    '<tr><td class="id"><b>T</b> · telos</td><td>What is it for?</td><td class="n">9</td><td><span class="st locked">locked · CLC</span></td></tr>')

sub("S row -> S1 + S2",
    '<tr><td class="id"><b>S</b> · stance</td><td>What posture does it take toward its object?</td><td class="n">6</td><td><span class="st cand">all candidate</span></td></tr>',
    '<tr><td class="id"><b>S1</b> · evaluative-stance</td><td>What posture does it take toward its <i>object</i>?</td><td class="n">4</td><td><span class="st locked">locked · CLC</span></td></tr>\n'
    '    <tr><td class="id"><b>S2</b> · hermeneutic-posture</td><td>How does it <i>read</i> — what does it do with a text?</td><td class="n">3</td><td><span class="st locked">locked · CLC</span></td></tr>')

# ─────────── 3. the lattice line ───────────
sub("lattice",
    '<p class="cap">9 × 13 × 7 × 7 × 6 × 8 = <b>275,184</b> theoretical coordinates. Values live in the DB table <code>exom_axis_vocabulary</code>, never hardcoded — a genuinely novel value proposed by a coder auto-registers as <span class="m">candidate</span> (that is fit-or-extend, P-2, implemented).</p>',
    '<p class="cap">9 × 13 × 7 × 9 × 4 × 3 × 8 = <b>707,616</b> theoretical coordinates on the locked seven-axis vocabulary. '
    '<span style="color:var(--terracotta)"><b>Status:</b> the restructured vocabulary is applied to the working store but <b>not yet to the authoritative one</b>, which still carries the earlier six-axis basis (275,184). The figure above is the one the locked vocabulary implies; it becomes the stored figure when propagation completes.</span> '
    'Values live in the DB table <code>exom_axis_vocabulary</code> and are read through <code>v_exom_active_vocabulary</code> — the canonical query, which drops the per-axis sentinel rows, excludes retired and held values, and names the seven axes explicitly rather than inferring them. Never hardcoded: a genuinely novel value proposed by a coder auto-registers as <span class="m">candidate</span> (fit-or-extend, P-2, implemented).</p>')

# ─────────── 4. honesty flag 1 — now stale ───────────
sub("honesty flag 1",
    '<b>1. Telos and stance are still <span class="m">candidate</span> in the live vocabulary — they were never promoted.</b> IRR183 added telos (unanimous) and flagged stance as the strongest new-axis candidate (4/5), and explicitly called for a <b>stance mini-round before stance→green</b>. That round never ran. <b>But both axes are being used as though locked</b> — they are in the 275,184 denominator and in the geometry. E/O/M/G went through empirical MECE-diagnostics; T and S did not.',
    '<b>1. Telos and stance were the open question, and the CLC closed it.</b> IRR183 added telos (unanimous) and flagged stance as the strongest new-axis candidate (4/5), calling for a <b>stance mini-round before stance→green</b>. IRR200 then found that <i>neither promoted as-is</i>: telos mixed levels, and stance was doing two jobs at once. Both were walked in the lock-cycle and settled (Decisions&nbsp;181/183/184) — <b>telos re-cut to nine values, and stance split into an evaluative half (S1) and a hermeneutic half (S2)</b>, which is why the axis count moved from six to seven. <b>The honest residue:</b> E/O/M/G went through empirical MECE-diagnostics and T/S1/S2 did not — they were settled by researcher judgement in the CLC, which is a weaker warrant and is recorded as such.')

# ─────────── 5. telos + stance value lists ───────────
sub("telos values",
    '<b>T · telos</b> (all candidate) — <span class="m">salvation</span> 145 · <span class="m">liberation</span> 128 (Gutiérrez) · <span class="m">flourishing</span> 108 · <span class="m">knowledge-understanding</span> 66 · <span class="m">contemplation</span> 42 (Aquinas) · <span class="m">harmony</span> 14 · <span class="m">power-mastery</span> 9 (Bacon).',
    '<b>T · telos</b> (locked, 9) — <span class="m">salvation</span> 145 · <span class="m">liberation</span> 128 (Gutiérrez) · <span class="m">flourishing</span> 108 · <span class="m">knowledge-understanding</span> 66 · <span class="m">harmony</span> 14 · <span class="m">agency-mastery</span> 9 (Bacon; <i>was</i> <span class="m">power-mastery</span>) · and three added by the CLC with <b>no figures coded to them yet</b>: <span class="m">communion</span> · <span class="m">justice-world-transformation</span> · <span class="m">fidelity-service</span>. <span style="color:var(--terracotta)"><span class="m">contemplation</span> (42, Aquinas) is <b>retired</b> — its cases redistribute on a re-code.</span>')

sub("stance values",
    '<b>S · stance</b> (all candidate; parents = <b>Ricoeur</b> suspicion/restoration + <b>Sedgwick</b> paranoid/reparative) — <span class="m">reverent</span> 211 · <span class="m">reparative</span> 179 · <span class="m">suspicious</span> 60 · <span class="m">charitable</span> 57 · <span class="m">reductive</span> 3 · <span class="m">paranoid</span> 2.',
    '<b>S1 · evaluative-stance</b> (locked, 4 — the posture toward the <i>object</i>) — <span class="m">reverent</span> 211 · <span class="m">suspicious</span> 60 · <span class="m">charitable</span> 57 · <span class="m">neutral-descriptive</span> (new, uncoded).<br>'
    '<b>S2 · hermeneutic-posture</b> (locked, 3 — what it does with a <i>text</i>; parents = <b>Ricoeur</b> suspicion/restoration + <b>Sedgwick</b> paranoid/reparative) — <span class="m">reparative-integrative</span> 179 (<i>was</i> <span class="m">reparative</span>) · <span class="m">reductive-deconstructive</span> 3 (<i>was</i> <span class="m">reductive</span>) · <span class="m">literal</span> (new, uncoded). <span style="color:var(--terracotta)"><span class="m">paranoid</span> (2) is <b>retired</b>.</span><br>'
    '<span style="font-size:11.5px;color:var(--ink-3)">The split is why a source can now be coded <i>suspicious</i> on S1 and <i>reparative-integrative</i> on S2 at once — a suspicious reading of a text one is charitable toward. That combination was unsayable while stance was a single axis.</span>')

# ─────────── 6. honesty flag 2 — "the 6th axis" is now the 7th ───────────
sub("honesty flag 2",
    '<b>2. The master lexicon names the 6th axis "derivation." That is wrong.</b> The 6th axis is <span class="m">ground-world-relation</span>.',
    '<b>2. The master lexicon names the last axis "derivation." That is wrong.</b> The seventh axis is <span class="m">ground-world-relation</span>.')

sub("flag 2 stale-count line",
    'The lexicon also still states "~40K possible," which is the <b>5-axis</b> count (34,398) from before G existed. Both are stale; the data is the arbiter.',
    'The lexicon also still states "~40K possible," which is the <b>5-axis</b> count (34,398) from before G existed — two restructures out of date now. Both are stale; the data is the arbiter, read through <code>v_exom_active_vocabulary</code>.')

# ─────────── 7. the six-axis statements elsewhere ───────────
for old, new, lbl in [
    ('There are six <b>axes</b>', 'There are seven <b>axes</b>', '§02 axis count'),
    ('a <b>6&#8209;tuple</b>', 'a <b>7&#8209;tuple</b>', '§02 tuple'),
    ('one value chosen per axis</b> — a 6&#8209;tuple', 'one value chosen per axis</b> — a 7&#8209;tuple', '§02 tuple b'),
]:
    if old in h: sub(lbl, old, new)

p.write_text(h)
print("APPLIED:")
for a in applied:
    print("  ✓", a)
