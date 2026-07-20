#!/usr/bin/env python3
"""c6sub.py — substitute the current engine spec into §C6 and delete the TMP appendix.

Closes a unanimous crit finding. HDS: "the only report of the engine's current behaviour is
inside the section marked for deletion." Lamberth: "shipping it inside the canonical document
means the canonical document is not currently canonical."

One §C6 carries the spec. The appendix goes. Superseded material lives in a COLLAPSED
drawer (Saquib #3, Lamberth #2) — not inline, not a redirect.
"""
import re, sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text()

NEW = '''<section class="sec" id="c-engine">
  <div class="sec-k"><span class="n">C6</span><h2>The engine — what it does, and what it does not yet see</h2></div>
  <p class="sec-lede">§C3 gives the <b>aspects</b> a branch is judged on; <a href="#c-trees">§C5</a> names the <b>objects</b>. This is the <b>engine itself</b>: one substitution at the root, a walk forward through the eight positions, and one generative act repeated at every fork.</p>

  <div class="flag" style="border-left-color:var(--terracotta)"><span class="pin">Status — a specification, not a report</span>
    This is the engine <b>as specified</b>. The FILLS-obligation revision below is <b>approved but not yet validated</b> — mini-test&nbsp;A2 is its first test, with a retrospective-check fallback if it does not hold. Nothing here is stated in the past tense, and the only run-figures quoted are from the Run&nbsp;A mini-test, labelled as such.
  </div>

  <h3 class="c6-h">What stays the same</h3>
  <div class="key"><b>One substitution at the root</b> — <span class="m">you hurt her</span> → <span class="m">you healed her</span> — then walk forward through the eight positions.
    <br><br><b>Axis perturbation is the only generative act.</b> Everything else either constrains what may be generated or measures what was. At each fork: <b>five candidates</b> — one holding all four axes, plus one per axis. <b>The axis is systematic; only the value is the model's choice.</b> Distance is measured afterwards, <b>never asked for</b>.
  </div>

  <h3 class="c6-h">What changes — and it is larger than it looks</h3>
  <p class="c6-note">The engine believes the song is a <b>chain</b>: M1 feeds M2 feeds M3, through to M8. <b>The song's own coding says otherwise.</b></p>
  <div class="key" style="border-left-color:var(--honey)"><b>There is the forward chain — and also five <i>backward</i> edges, nearly all landing on one move</b>, each carrying a <b>slot label</b>, several with multiple sources:
    <div class="eq">M1 + M3  →  M4   <b>reason</b>        why she loves you despite the hurt
M2       →  M4   <b>degree</b>        how much
M5 + M8  →  M4   <b>reciprocity</b>   whether you love her back
M6       →  M4   <b>warrant</b>       how the friend knows
M7 + M8  →  M4 / META  <b>outcome</b>  what it produces</div>
    M4 is <b>"she loves you."</b> <b>Five other moves exist partly in order to answer it.</b> That is what makes M4 the money-move — <i>not the middle of a chain, but the thing the structure converges on</i>.
    <br><br><b>The engine cannot see any of it.</b> So in every alternative world generated so far, <b>M4′ is merely "whatever comes after M3′"</b> — it loses the one structural fact that makes M4 matter.
  </div>

  <div class="key" style="border-left-color:var(--fern)"><b>The revision: a backward edge becomes a forward obligation.</b>
    <br><br>Generating M5′ no longer asks only <i>"what does M5's slot do here?"</i> but <i>"what does M5's slot do here, <b>such that it answers M4′'s reciprocity gap</b>?"</i>
    <br><br>And where the obligation <b>cannot be met</b> — where the substitution dissolved the gap, so there is nothing left to answer — that is an <b>edge-break on a FILLS edge</b>, flagged as a <b>structural-consequence finding</b> rather than forced. A new kind of output: not <i>"this move doesn't follow"</i> but <b>"in this world, nobody needs to say why she loves you."</b>
  </div>

  <h3 class="c6-h">Two things that stop being silent</h3>
  <div class="tbl"><table class="d">
    <tr><th style="width:26%">What</th><th>Why it matters</th></tr>
    <tr><td class="id"><b>the metric, with its denominator</b></td><td>Distance is a <b>Hamming count</b> — how many axes differ; no magnitudes, no weighting — and its <b>denominator (4)</b> is recorded on every row. <span style="color:var(--terracotta)">Currently <code>NULL</code> on all 111 rows of Run&nbsp;A</span>, so a stored <code>d=3</code> does not carry the basis that makes it a number.</td></tr>
    <tr><td class="id"><b><code>exits_to</code> on a doorway</b></td><td>Which world the doorway opens onto. <span style="color:var(--terracotta)">Currently <code>NULL</code> on all three of Run&nbsp;A's doorways</span> — and <b>a doorway that doesn't say which world it opens onto is half a finding</b>. Bundling by target frame cannot run without it.</td></tr>
  </table></div>

  <div class="flag"><span class="pin">Declared, not silent — what the engine still does not carry</span>
    The engine holds <b>the forward spine plus these FILLS obligations</b>. <span class="m">COMPOSES</span> — all eight moves to the whole — is <b>still not carried</b>. That remains a narrowing, and it is recorded as one rather than left to be discovered.
  </div>

  <div class="flag" style="border-left-color:var(--honey)"><span class="pin">An open question, not a decision</span>
    <b>Should the gate use the Hamming count, or the MCA metric that <a href="#d-mca">§D</a> justifies?</b> §D argues for MCA on the grounds of its behaviour on rare categories — co-occurrence geometry rather than a flat count. The gate currently runs <b>Hamming</b>. <b>The page does not yet reconcile the two</b>, and naming the metric sharpens the contradiction rather than resolving it. <b>Unsettled, and recorded as unsettled</b> — likely an IRR.
  </div>

  <details class="dd"><summary>Superseded — the alternative-kinds taxonomy as the generation rule (pre-Decision&nbsp;186)</summary>
    <div class="dd-b">
      <p>Until IRR201 (Decision&nbsp;186) the generation rule at <i>every</i> fork was the <a href="#b-alt">§B5</a> alternative-kinds — <b>CONTRARY</b> (the far pole; geometry <i>sign</i>) · <b>[BETWEEN]</b> (the nameable middle, where most real alternatives live; <i>magnitude</i>) · <b>PRIVATION</b> (the relation withdrawn; <i>origin</i>) — plus <b>BEYOND-PARADIGM</b> (<i>orthogonal</i>), flagged rather than coded.</p>
      <p><b>Why it was replaced:</b> all five cohorts found unanimously that the taxonomy <b>degrades from depth&nbsp;2 onward</b>, because the thing you would take the contrary <i>of</i> is your own previous guess — <i>"the contrary of a guess is a double-guess."</i></p>
      <p><b>It still governs depth&nbsp;1</b>, where the anchor is the real text: <span class="m">you hurt her</span> → <span class="m">you healed her</span> is a CONTRARY. Beyond depth&nbsp;1, generation is axis perturbation anchored to the <b>source's</b> slot — the trunk anchors every branch; branches never anchor to each other.</p>
      <p class="cap">Kept because the change, and its reason, are method content. This drawer is the record, not a redirect.</p>
    </div>
  </details>

  <style>
  #c-engine .c6-h{font-family:var(--serif);font-size:17px;color:var(--ink);margin:24px 0 4px}
  #c-engine .c6-note{font-size:13.5px;color:var(--ink-2);margin:2px 0 10px;max-width:86ch;line-height:1.6}
  #c-engine .eq{font-family:var(--mono);font-size:11.5px;background:var(--paper-2);border-radius:6px;padding:10px 12px;margin:9px 0;white-space:pre-wrap;color:var(--ink-2);line-height:1.7}
  </style>
</section>'''

i = h.find('<section class="sec" id="c-engine">')
j = h.find('<section', i + 10)
assert i != -1 and j > i, "C6 bounds not found"
h = h[:i] + NEW + '\n\n' + h[j:]

# delete the TMP appendix + its nav entry
a = h.find('<!-- ══ TEMPORARY WORKING APPENDIX ══ -->')
b = h.find('<!-- ══ /TEMPORARY WORKING APPENDIX ══ -->') + len('<!-- ══ /TEMPORARY WORKING APPENDIX ══ -->')
assert a != -1 and b > a, "appendix bounds not found"
h = h[:a] + h[b:]
h = re.sub(r'\s*<a class="sub" href="#x-working"[^>]*>[^<]*</a>\n?', '\n', h, count=1)

# nav label for C6
h = h.replace('<a class="sub" href="#c-engine">C6 · The engine, opened</a>',
              '<a class="sub" href="#c-engine">C6 · The engine</a>', 1)

p.write_text(h)
ids = set(re.findall(r'id="([a-z0-9-]+)"', h)); hrefs = set(re.findall(r'href="#([a-z0-9-]+)"', h))
print("appendix removed:", 'x-working' not in h)
print("broken anchors:", sorted(hrefs - ids) or "NONE")
print("sections:", h.count('<section'))
