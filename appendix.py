#!/usr/bin/env python3
"""appendix.py — the TEMPORARY working appendix, at the very bottom of the SPA.

Six parts, headers exactly as reading-SB specified. Built with the IRR201 / Decision 186
generation corrections folded in rather than built-then-patched.

Spec voice throughout. No past tense. The ONLY node count is 157, explicitly labelled a
failure example in Part 6.
"""
import sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text()
assert 'id="x-working"' not in h, "already built"

SEC = '''
<!-- ══ TEMPORARY WORKING APPENDIX ══ -->
<section class="sec" id="x-working">
  <div class="sec-k"><span class="n">TMP</span><h2>The alternative-tree engine · working appendix</h2></div>

  <div class="flag" style="border-left-color:var(--terracotta);background:rgba(196,96,47,.05)"><span class="pin">Temporary — this section comes out</span>
    <b>This is a working artifact, not method.</b> It exists so the whole engine can be read top-to-bottom in one place while it is being got right. <b>It is removed once the fan runs clean.</b> Assembled <b>2026-07-19</b>; everything in it is a <i>specification</i> — the conformed engine has not been run, and nothing here is stated in the past tense.
    <br><br><b>The generation rule below is IRR201-locked</b> (Decision&nbsp;186), not house opinion. Three of the engine's four drifts happened because a gap in the spec got filled by whoever was implementing at the time; this round was fired <i>before</i> building, specifically to break that pattern.
  </div>

  <h3 class="xw-h">1 · The algorithm, in plain language</h3>
  <p class="xw-p">Already on the page and not repeated here: <a href="#c-engine"><b>§C6 — the alternative-tree engine, opened</b></a>. Input, the seven steps, the codeable kinds, the four gates, and the two piles outside the tree.</p>

  <h3 class="xw-h">2 · The schema</h3>

  <p class="xw-sub"><b>2a · the black box</b></p>
  <div class="xw-box">
    <div class="xw-flow">
      <span class="xw-n">1</span> declare the contract — what is <b>HELD</b>, what is <b>VARIED</b>
      <span class="xw-ar">↓</span>
      <span class="xw-n">2</span> hold the <b>song's own edge</b> at this position
      <span class="xw-ar">↓</span>
      <span class="xw-n">3</span> generate — <i>see the depth rule below; this is the part IRR201 changed</i>
      <span class="xw-ar">↓</span>
      <span class="xw-n">4</span> gate on four checks — <b>Sitz · paradigm · path-coherence · branch-state</b>
      <span class="xw-ar">↓</span>
      <span class="xw-n">5</span> measure distance, assign tier <span class="xw-note">(computed, never asked for)</span>
      <span class="xw-ar">↓</span>
      <span class="xw-n">6</span> grow, or <b>terminate</b>
      <span class="xw-ar">↓</span>
      <span class="xw-n">7</span> out → complete paths + <b>Pile A</b> (another world could hold it) + <b>Pile B</b> (doesn't follow)
    </div>
  </div>

  <div class="key" style="border-left-color:var(--terracotta)"><b>How generation works — and it differs by depth. <span class="st locked">IRR201 · 5/5</span></b>
    <br><br><b>At depth 1</b> — the substitution itself — the alternative-kinds apply. <span class="m">you hurt her</span> → <span class="m">you healed her</span> is a <b>CONTRARY</b>. That much is anchored in the real text.
    <br><br><b>At depth ≥ 2 they do not.</b> The taxonomy degrades once the thing you would be taking the contrary <i>of</i> is your own previous guess — <i>"the contrary of a guess is a double-guess."</i> Generation is instead by <b>explicit axis perturbation</b>, anchored to the <b>source's</b> structural slot at that position:
    <div class="eq">Generate the move where the <b>epistemic warrant shifts from testimony to speculation</b>,
holding <b>telos: harmony</b> — such that it satisfies the FEEDS edge from the previous move.</div>
    <b>Never</b> <i>"a move at distance 2"</i> — that scores the instruction rather than the move. <b>Distance is measured afterwards, never asked for.</b>
    <br><b>Never</b> <i>"the contrary of the previous move."</i> The anchor is the source's slot: a new M2′ is not the contrary of "healed" — it is <b>the structural equivalent of "suffer" in a healed world</b>. Envy, say: suffering from another's good rather than from direct harm.
    <br><br><b>The trunk anchors every branch; branches never anchor to each other.</b>
  </div>

  <p class="xw-sub"><b>2b · the control song, and the recursion</b> — the part that must stay visible</p>
  <div class="xw-box">
    <div class="xw-ctrl"><b>THE CONTROL</b> — every edge <span class="m">FEEDS</span>
      <div class="xw-chain"><b>M1</b> hurt <span class="xw-e">→</span> <b>M2</b> suffer <span class="xw-e">→</span> <b>M3</b> reappraise <span class="xw-e">→</span> <b>M4</b> loves <span class="xw-star">★</span> <span class="xw-e">→</span> <b>M5</b> fear <span class="xw-e">→</span> <b>M6</b> relay <span class="xw-e">→</span> <b>M7</b> be&nbsp;glad <span class="xw-e">→</span> <b>M8</b> apologise</div>
      <div class="xw-note">Frame coordinate — the four axes this song turns on: <span class="m">E testimony</span> · <span class="m">T harmony</span> · <span class="m">S1 charitable</span> · <span class="m">S2 reparative-integrative</span></div>
    </div>
    <div class="xw-sub2">the substitution &nbsp;·&nbsp; <b>M1 → M1′</b> <span class="m">you healed her</span> — a <b>CONTRARY</b>, everything else HELD</div>
    <div class="xw-fan">
      <div class="xw-depth"><span class="xw-dl">depth 1 → M2′</span> <span class="xw-held">holds the control's <b>M1→M2</b> edge (FEEDS)</span>
        <div class="xw-kids"><span class="xw-k">…</span><span class="xw-k">…</span><span class="xw-k">…</span></div></div>
      <div class="xw-depth"><span class="xw-dl">depth 2 → M3′</span> <span class="xw-held">holds the control's <b>M2→M3</b> edge (FEEDS)</span>
        <div class="xw-kids"><span class="xw-k">…</span><span class="xw-k">…</span><span class="xw-k">…</span><span class="xw-k">…</span><span class="xw-k">…</span></div></div>
    </div>
  </div>

  <div class="key"><b>The rule that must not drift again.</b>
    <div class="eq">The edge held at depth N is the <b>CONTROL's</b> edge between M(N) and M(N+1) —
the same for every branch at that depth, <b>never taken from the generated parent</b>.</div>
    At M3′ you hold the control's M2→M3 edge <i>regardless of which M2′ alternative you arrived through</i>. <b>The edge schedule is a property of the source song, not of the path.</b>
  </div>

  <div class="tbl"><table class="d">
    <tr><th style="width:30%">Also true of the fan</th><th>Why it matters</th></tr>
    <tr><td class="id"><b>Tier is per-node, never inherited</b></td><td>A branch can change tier between depths. The <b>kind</b> is <i>how it was generated</i>; the <b>tier</b> is <i>where it landed</i>, computed from that node's own coordinate.</td></tr>
    <tr><td class="id"><b>Only <span class="m">expected</span> + <span class="m">nuanced</span> fan</b></td><td><span class="m">far-in-frame</span> and <span class="m">doorway</span> are <b>leaves</b> — kept, tagged, not expanded.</td></tr>
    <tr><td class="id"><b>Two distances, not one</b></td><td><b>step</b> (from the parent — a small turn, or a jump?) and <b>cumulative</b> (from the song — where has this path ended up?). Static alone can't tell coherent evolution from a lurch; trajectory alone loses the no-longer-this-world signal.</td></tr>
    <tr><td class="id"><b>Each path rebuilds its own <span class="m">FILLS</span> and <span class="m">COMPOSES</span></b></td><td><i>You generate chains, not stories.</i> The model must close its own loops — which is also the strongest brake on free association available here.</td></tr>
    <tr><td class="id"><b>Termination is expected</b></td><td>Paths ending at M5′ or M7′ are normal. <b>The tree is ragged, and the raggedness is information</b> — it is not a run that failed to reach M8′.</td></tr>
    <tr><td class="id"><b>No expected tier spread</b></td><td>There is deliberately <b>no target distribution</b>. Forcing a uniform spread would be dishonest: if a source's frame is strong, distant candidates <i>ought</i> to be rare — and that rarity may itself be the finding.</td></tr>
  </table></div>

  <h3 class="xw-h">3 · The data shape</h3>
  <p class="xw-p">One row per generated move in <code>alt_tree_node</code>. The fields that carry the argument: <code>move</code> (the move as a <b>sentence</b>, not a code) · <code>alt_kind</code> · <code>edge_held</code> (the song's edge at this position) · <code>sitz</code> · <code>frame_band</code> · <code>branch_state</code> · <code>verdict</code> (expected / nuanced / far-in-frame / doorway / barred) · <code>interest</code> <span style="color:var(--terracotta)">(the model's opinion, <b>not</b> computed — and marked so by <code>metric_source</code>)</span> · plus the §2.4 provenance fields, never NULL.</p>
  <div class="flag"><span class="pin">Seven fields are missing, and writing the table out is what surfaced them</span>
    <b><code>dist</code></b> — the raw distance is computed and written to the CSV but <b>not to the table</b>, so the tier is stored without the number that produced it. That is the <i>declare-the-denominator</i> failure inside our own schema.<br>
    <b><code>coord_e coord_t coord_s1 coord_s2</code></b> — the branch's actual coordinate; without it a tier cannot be audited or recomputed without re-coding.<br>
    <b><code>axes_changed</code></b> · <b><code>frame_exit</code></b> · <b><code>governing_concept</code> + <code>concept_birth</code></b> · <b><code>retry_count</code></b> (the silent-truncation telemetry — currently printed, not stored).<br>
    <b><code>exits_to</code></b> — <b>which tradition's frame a doorway opens onto.</b> The entire bundling step depends on it, and it does not exist yet.
  </div>

  <h3 class="xw-h">4 · The script</h3>
  <p class="xw-p"><code>scripts/analysis/generate_alt_tree_v2_1963.py</code> runs the box: it holds <code>SOURCE_EDGES</code> position by position, calls generation at temperature&nbsp;0, applies the four gates, and imports the <b>computed frame gate</b> rather than scoring distance itself — so the tier and the generator cannot drift apart. Vocabulary is read from <code>v_exom_active_vocabulary</code>, never hardcoded; the morning the CLC landed is exactly when a hardcoded copy would have gone stale. <i>Described, not pasted — the file is the arbiter.</i></p>

  <h3 class="xw-h">5 · Pre-flight checklist</h3>
  <p class="xw-p">Checkable before or immediately after a run. <b>A "no" anywhere means don't trust the output.</b></p>
  <div class="tbl"><table class="d">
    <tr><th style="width:20%">Block</th><th>What it establishes</th></tr>
    <tr><td class="id"><b>A · before generating</b></td><td>Exactly the four kinds are asked for, with BEYOND-PARADIGM <b>flagged not coded</b> · temperature 0 · <b>the held edges match the control song position by position</b> (A4 — the drift that hid longest, and still has no automated check) · the source coordinate is in-vocabulary · vocabulary read from the canonical view.</td></tr>
    <tr><td class="id"><b>B · the gates bite</b></td><td>Sitz prunes a planted anachronism · branch-state catches the healed-then-wounded probe · <b>frame-coherence prunes nothing</b> (any barred row that passed Sitz and state is a bug) · <b>EDGE-BREAK is possible at all</b> — always 0 means the edge is being forced and the finding is being lost.</td></tr>
    <tr><td class="id"><b>C · the tree is COMPLETE</b><br><span class="xw-note">the block that caught us</span></td><td>No parent produced nothing · it reached <b>M8′</b> · the node count is in the thousands · every depth is populated · empty parses were <b>retried, not recorded as verdicts</b>.</td></tr>
    <tr><td class="id"><b>D · the tiers are meaningful</b></td><td>All four tiers present · doorways exist at all · distance is spread rather than holed · <b>reproducible</b> — two runs at temp 0 diff to nothing · <code>metric_source='computed'</code> on every row.</td></tr>
    <tr><td class="id"><b>E · before bundling</b></td><td>All of C passed · complete <b>paths</b> assembled, not just nodes · <b>Pile A and Pile B kept separate</b> · doorways carry <code>exits_to</code>.</td></tr>
  </table></div>

  <h3 class="xw-h">6 · Post-run bug check</h3>
  <p class="xw-p"><code>scripts/analysis/validate_alt_tree_run.py</code> is blocks B–E made runnable. Every check corresponds to a failure that actually occurred, and it degrades gracefully if the audit-field migration has not been applied — reporting the gap rather than crashing.</p>
  <div class="key" style="border-left-color:var(--fern)"><b>The test of the test.</b> Pointed at a known-bad run — <b>157 nodes, reported at the time as a success</b> — it <b>independently rediscovers every problem, without being told what to look for</b>:
    <div class="xw-res">
      <span class="xw-fail">C2 FAIL</span> depth 6, not 7 — never reached M8′<br>
      <span class="xw-fail">C3 FAIL</span> 157 nodes, far below the plausible floor — it truncated<br>
      <span class="xw-warn">B4 WARN</span> 0 EDGE-BREAK — the edge is being forced<br>
      <span class="xw-warn">D2 WARN</span> 1 doorway (0.6%) — the generator isn't reaching
    </div>
    That is the honest answer to <i>"how do we know it won't happen again."</i> <b>157 is quoted here as a failure example only</b> — it is the single node count on this page, and it is not a result.
  </div>

  <style>
  #x-working .xw-h{font-family:var(--serif);font-size:18px;color:var(--ink);margin:26px 0 4px;border-bottom:1px solid var(--rule);padding-bottom:4px}
  #x-working .xw-sub{font-size:13.5px;color:var(--ink-2);margin:14px 0 6px}
  #x-working .xw-p{font-size:13.5px;color:var(--ink-2);line-height:1.6;max-width:86ch;margin:6px 0 10px}
  #x-working .xw-note{font-size:11.5px;color:var(--ink-3);font-style:italic}
  #x-working .xw-box{border:1px solid var(--rule);border-radius:9px;background:var(--paper);padding:13px 15px;margin:8px 0 12px}
  #x-working .xw-flow{font-size:13px;color:var(--ink-2);line-height:1.9}
  #x-working .xw-n{font-family:var(--mono);font-size:10px;font-weight:700;color:var(--paper);background:var(--moss);border-radius:50%;padding:1px 6px;margin-right:5px}
  #x-working .xw-ar{color:var(--fern);margin:0 8px}
  #x-working .xw-ctrl{background:var(--paper-2);border-radius:7px;padding:10px 12px;font-size:12px;color:var(--ink-2)}
  #x-working .xw-chain{font-family:var(--mono);font-size:12.5px;color:var(--ink);line-height:1.9;margin:6px 0 4px}
  #x-working .xw-e{color:var(--fern);margin:0 2px}
  #x-working .xw-star{color:var(--honey)}
  #x-working .xw-sub2{text-align:center;font-size:12.5px;color:var(--ink-2);margin:10px 0;padding:6px;border-top:1px dashed var(--rule);border-bottom:1px dashed var(--rule)}
  #x-working .xw-depth{margin:8px 0}
  #x-working .xw-dl{font-family:var(--mono);font-size:11px;color:var(--moss);font-weight:700}
  #x-working .xw-held{font-size:11.5px;color:var(--ink-3);margin-left:8px}
  #x-working .xw-kids{display:flex;gap:6px;margin-top:5px;padding-left:14px}
  #x-working .xw-k{flex:1;height:16px;border:1px dashed var(--rule);border-radius:4px;background:var(--paper-2);text-align:center;font-size:10px;color:var(--ink-3);line-height:16px}
  #x-working .eq{font-family:var(--mono);font-size:11.5px;background:var(--paper-2);border-radius:6px;padding:9px 11px;margin:8px 0;white-space:pre-wrap;color:var(--ink-2);line-height:1.6}
  #x-working .xw-res{font-family:var(--mono);font-size:11.5px;background:var(--paper);border:1px solid var(--rule);border-radius:6px;padding:10px 12px;margin:8px 0;line-height:1.9}
  #x-working .xw-fail{color:var(--paper);background:var(--terracotta);border-radius:4px;padding:1px 7px;font-weight:700;margin-right:6px}
  #x-working .xw-warn{color:var(--paper);background:var(--honey);border-radius:4px;padding:1px 7px;font-weight:700;margin-right:6px}
  </style>
</section>
<!-- ══ /TEMPORARY WORKING APPENDIX ══ -->

'''

anchor = '\n\n</main>\n</div>\n</body></html>'
assert anchor in h, "page tail not found"
h = h.replace(anchor, '\n' + SEC + '</main>\n</div>\n</body></html>', 1)

# nav entry
nav = '  <a class="sub" href="#x-q">Open questions</a>\n'
assert nav in h
h = h.replace(nav, nav + '  <a class="sub" href="#x-working" style="color:var(--terracotta)">TMP · Engine working appendix</a>\n', 1)

p.write_text(h)
print("appendix inserted at the very bottom + nav entry")
