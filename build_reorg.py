#!/usr/bin/env python3
"""
build_reorg.py — §D reorg: morphospace concept before the grammar.

Per BRIEF_spa_section_d_reorg_morphospace_first_2026-07-19.md (reading-SB).

LOAD-BEARING REQUIREMENT (the only one the brief makes binding):
    the morphospace concept must precede the first use of `coordinate` / `frame-coherence`.

LETTERING DECISION (the brief explicitly leaves this to design-SB):
    We do NOT re-letter A->B->C->D. Measured hazard: 172 inline prose cross-references
    (28 bare "§X", 35 "§Xn", 109 "A-n"/"D-n" def-ids). A full re-letter means rewriting all
    of them, and every miss is a silent wrong-pointer -- the same failure class the brief is
    trying to avoid with anchors, just in prose.
    Instead we use the page's EXISTING front-matter convention, which is numeric:
        00 Thesis-grade insights · 01 Project principles  ->  02 (new) · 03 (moved d-frame)
    then §A..§E continue untouched. Result: precedence achieved, zero re-lettering.

ANCHORS:
    Anchor ids on this page are SEMANTIC SLUGS (d-frame, c-gates), not positional. Moving a
    section carries its id with it, so every existing anchor keeps resolving with no alias
    needed. We rename NO ids and delete NO ids. (Renaming d-frame -> a-frame would also have
    collided with the existing #a-frame.)

WHAT MOVES (concept)              WHAT STAYS (apparatus)
  #d-frame  (D-1 frame def)         #d-axes (D2 value tables)
  #viz-8    (four-layer stack)      #d-rfa  (D3 roster/frame/atlas + counts)
  + new #morphospace intro          #d-cloud (D4) #d-mca (D5) #d-diag (D6) #d-occ (D7)

NUMBERS: the new front section carries NO counts. The page currently disagrees with itself
(§D3 says lattice 275,184 / 536 rows / 483 coded / 342 occupied; VIZ-8 per reading-SB's brief
says 301,056 / 512 / 365). That contradiction is reported to reading-SB, who owns the numbers;
this reorg deliberately does not propagate either set into new copy (R1).
"""
import re, sys, pathlib

HTML = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")


def extract_section(h, sid):
    """Cut out <section ... id="sid"> ... </section> and return (html_without, section_html)."""
    start = h.find(f'<section class="sec" id="{sid}">')
    assert start != -1, f"section {sid} not found"
    end = h.find('</section>', start) + len('</section>')
    # include trailing newline(s)
    while end < len(h) and h[end] == '\n':
        end += 1
    return h[:start] + h[end:], h[start:end]


def extract_block(h, start_marker, end_marker):
    s = h.find(start_marker)
    assert s != -1, f"marker not found: {start_marker}"
    e = h.find(end_marker, s) + len(end_marker)
    while e < len(h) and h[e] == '\n':
        e += 1
    return h[:s] + h[e:], h[s:e]


NEW_SECTION = '''<section class="sec" id="morphospace">
  <div class="sec-k"><span class="n">02</span><h2>The morphospace — the space of possible minds</h2></div>
  <p class="sec-lede">This comes first because everything after it borrows from it. §A–§C use the word <b>coordinate</b> long before the apparatus that computes one — so here is the idea, plainly, up front. <b>The full axis tables, the geometry and the diagnostics stay where they are, in §D</b>; this is orientation, not the apparatus.</p>

  <div class="key"><b>What a morphospace is.</b> The term is borrowed from <b>theoretical morphology</b> (Raup), where it names the space of all shapes an organism <i>could</i> take — not just the ones that exist. Its power is that it treats the <b>empty regions as real</b>: a shape nothing has ever grown is still a location on the map, and asking why nothing is there is a research question rather than a gap in the data.
  <br><br>We use it for <b>minds</b> instead of shells. A <b>frame</b> is one possible mind — described by its <i>commitments</i>, not by its owner's name — and the morphospace is the space of all of them. That is what lets us say a thinker <i>occupies</i> a position, that two thinkers are <i>near</i> each other, and that some coherent positions have <b>no occupant at all</b>.</div>

  <div class="def">
    <div class="def-h"><span class="def-id">02-a</span><h3 class="def-t">axis · value · coordinate</h3><span class="st locked">plain-language, promoted from the FAQ</span></div>
    <p class="def-q">Q: What exactly is a "coordinate," and is a value one?</p>
    <div class="def-b"><dl>
      <dt>The three words</dt><dd class="op">There are six <b>axes</b>. Each axis offers a set of <b>values</b> — the ways a mind can answer that axis. A <b>coordinate</b> is <b>one value chosen per axis</b> — a 6&#8209;tuple. That coordinate <i>is</i> a <b>frame</b>: one possible mind.</dd>
      <dt>The distinction that keeps slipping</dt><dd class="warn"><b>A value is not a coordinate.</b> "Revelation" is a <i>value</i> on one axis; a coordinate is the whole six-part answer — <i>knows by revelation, holds a personal-agentive ground, reasons by exegesis,</i> and so on.</dd>
      <dt>Why it has to be a tuple</dt><dd>Because that is what makes <b>distance</b> possible. Two coordinates can be near or far, and that distance is what later sections spend as a currency — most sharply in <b>§C3</b>, where <span class="m">frame-coherence</span> asks whether a generated alternative has drifted out of the source's worldview. <b>Frame-coherence is a coordinate distance.</b> That is the one forward-reference worth carrying with you.</dd>
    </dl></div>
  </div>

  <div class="key"><b>The three things, and how they feed each other — library · morphospace · flywheel.</b>
    <div class="tbl"><table class="d">
      <tr><th style="width:18%">The thing</th><th>What it is</th><th>What it gives the others</th></tr>
      <tr><td class="id"><b>the library</b></td><td>The <b>corpus we actually hold</b> — the texts and the named voices collected so far. Real, finite, and uneven.</td><td>It supplies the <b>occupants</b>. Nothing lands on the map that was not read out of the library first.</td></tr>
      <tr><td class="id"><b>the morphospace</b></td><td>The <b>space those occupants sit in</b> — every coherent position a mind could hold, whether or not anyone holds it.</td><td>It turns a pile of voices into a <b>geography</b>: near, far, clustered, and — the interesting part — <b>empty</b>.</td></tr>
      <tr><td class="id"><b>the flywheel</b></td><td>The <b>loop between them</b>: an empty region prompts a search, the search brings texts into the library, the new codings re-shape the map, which exposes the next empty region.</td><td>It is what makes the project <b>compound</b> rather than merely accumulate.</td></tr>
    </table>
    <p class="cap">The catch that keeps the loop honest: an <b>empty</b> position may mean nobody ever held that view — or may only mean we have not coded the person who did. Those look identical from the map, which is why the flywheel needs a gate rather than an accelerator. The mechanism is in <b>§D7</b>.</p></div>
  </div>

  <div class="postit"><span class="pin">Where the rest of it lives</span>
    This section is deliberately short. The <b>apparatus</b> — every value on every axis (<b>§D2</b>), who is on the roster and how the counts nest (<b>§D3</b>), thinkers as point-clouds (<b>§D4</b>), how categories are turned into a map (<b>§D5</b>), the results and their diagnostics (<b>§D6</b>), and occupied-vs-coherent plus the flywheel (<b>§D7</b>) — all stay in <b>§D</b>, after the grammar that supplies their vocabulary. You are meant to arrive there already knowing what a coordinate is.
  </div>
</section>

'''


def main():
    h = HTML.read_text()
    before = len(h)

    # ── idempotency: if already reorganised, rebuild from a clean state is not attempted;
    #    just report and exit.
    if 'id="morphospace"' in h:
        print("already reorganised (#morphospace present) — no-op")
        return

    # 1. cut the concept section (#d-frame) and the four-layer viz (#viz-8) out of §D
    h, d_frame = extract_section(h, 'd-frame')
    h, viz8 = extract_block(h,
                            '<!-- ══ VIZ-8 FOUR-LAYER STACK (built) ══ -->',
                            '<!-- ══ /VIZ-8 ══ -->')

    # 2. re-badge the moved concept section: "D" -> "03"; keep id + def-id D-1 (109 prose refs)
    d_frame = d_frame.replace('<span class="n">D</span><h2>The morphospace of frames</h2>',
                              '<span class="n">03</span><h2>A frame is a coordinate — the morphospace of minds</h2>', 1)
    assert '<span class="n">03</span>' in d_frame, "re-badge of d-frame failed"

    # 3. insert: new #morphospace + moved #d-frame + moved VIZ-8, before the grammar (#a-move)
    anchor = h.find('<section class="sec" id="a-move">')
    assert anchor != -1, "#a-move not found"
    # place VIZ-8 inside the new intro (after it), then the frame definition section
    payload = NEW_SECTION + viz8 + "\n" + d_frame
    h = h[:anchor] + payload + h[anchor:]

    # 4. nav rail — add the two new entries above "A · Grammar", drop the stale D1 entry,
    #    and relabel the D group as the apparatus.
    nav_old = '  <h4>A · Grammar</h4>'
    nav_new = ('  <h4>Start here</h4>\n'
               '  <a class="sub" href="#morphospace">02 · The morphospace</a>\n'
               '  <a class="sub" href="#d-frame">03 · A frame is a coordinate</a>\n'
               '  <a class="sub" href="#viz-8">VIZ-8 · How a coordinate is made</a>\n'
               '  <h4>A · Grammar</h4>')
    assert nav_old in h, "nav anchor 'A · Grammar' not found"
    h = h.replace(nav_old, nav_new, 1)

    # drop the now-moved D1 nav entry from the D group
    h = h.replace('  <a class="sub" href="#d-frame">D1 · A frame is a coordinate</a>\n', '', 1)
    # relabel the D nav group
    h = h.replace('<h4>D · Morphospace</h4>', '<h4>D · Morphospace — the apparatus</h4>', 1)

    # 5. back-pointer at the top of what is now §D's first section (#d-axes)
    da = h.find('<section class="sec" id="d-axes">')
    assert da != -1
    lede_end = h.find('</p>', h.find('sec-lede', da)) + len('</p>')
    backptr = ('\n  <p class="cap" style="font-family:var(--sans);font-size:12px;color:var(--ink-3);'
               'margin:6px 0 0">The <b>concept</b> — what a morphospace is, and what a coordinate is — '
               'is introduced up front in <a href="#morphospace" style="color:var(--fern)">§02</a>. '
               'This is the apparatus.</p>')
    h = h[:lede_end] + backptr + h[lede_end:]

    # 6. front-matter courtesy pointer at the first prose use of "coordinate" (in #insights)
    ins = h.find('<section class="sec" id="insights">')
    first_coord = h.find('place a', ins)
    if first_coord != -1:
        seg_end = h.find('</td>', first_coord)
        if seg_end != -1 and 'morphospace' not in h[first_coord:seg_end]:
            h = (h[:seg_end] + ' <a href="#morphospace" style="color:var(--fern);font-size:11px">'
                 '(what a coordinate is &rarr; §02)</a>' + h[seg_end:])

    # 7. the single inline "§D1" reference now points at a front section — retarget the label
    h = h.replace('§D1', '§03', 1)

    HTML.write_text(h)

    # ── verification ────────────────────────────────────────────────────────────────
    ids = set(re.findall(r'id="([a-z0-9-]+)"', h))
    hrefs = set(re.findall(r'href="#([a-z0-9-]+)"', h))
    missing = sorted(hrefs - ids)
    print(f"bytes {before} -> {len(h)}")
    print("ids:", len(ids), "| href targets:", len(hrefs), "| BROKEN:", missing or "none ✓")
    assert not missing, f"broken anchors: {missing}"
    for sid in ('d-frame', 'd-axes', 'd-rfa', 'd-cloud', 'd-mca', 'd-diag', 'd-occ',
                'a-move', 'c-gates', 'morphospace', 'viz-8'):
        assert f'id="{sid}"' in h, f"lost id {sid}"
    # precedence check
    pos_ms = h.find('id="morphospace"')
    pos_a = h.find('id="a-move"')
    assert pos_ms < pos_a, "morphospace must precede the grammar"
    print("precedence: #morphospace before #a-move ✓")


if __name__ == "__main__":
    main()
