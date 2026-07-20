#!/usr/bin/env python3
"""sweep2.py — remaining prose + VIZ-8 + the notes this sweep obsoletes.

RULE APPLIED THROUGHOUT: statements about the VOCABULARY become seven-axis.
Statements about the COMPLETED CODING RUN keep their figures and are marked as the
earlier six-axis basis — the run happened on six axes and saying otherwise would
falsify it. Same principle as leaving VIZ-5's coordinates alone.
"""
import sys, pathlib
p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text(); done = []

def sub(label, old, new, count=1):
    global h
    assert old in h, f"NOT FOUND: {label}\n  {old[:150]}"
    h = h.replace(old, new, count); done.append(label)

# ── nav ──
sub("nav D2", '<a class="sub" href="#d-axes">D2 · The six axes</a>',
              '<a class="sub" href="#d-axes">D2 · The seven axes</a>')

# ── §insights: vocabulary statement -> seven ──
sub("insights figure-coding",
    'place a <i>figure</i> at a coordinate on the six axes (E·O·M·T·S·G) — the atlas',
    'place a <i>figure</i> at a coordinate on the seven axes (E·O·M·T·S1·S2·G) — the atlas')

# ── §insights: this one describes the COMPLETED RUN -> mark the basis, keep the figure ──
sub("insights 6-coordinate (run)",
    'the 6-coordinate figure-coding you guessed is the one that\'s <i>partly</i> done (31%)',
    'the figure-coding you guessed is the one that\'s <i>partly</i> done (31%) — run on the earlier <b>six</b>-axis set, before the CLC split stance')

# ── §A2 / §03 definitions -> seven ──
sub("a-frame def", 'a coordinate on the six axes — a possible mind',
                   'a coordinate on the seven axes — a possible mind')
sub("d-frame def", 'one point on six categorical axes',
                   'one point on seven categorical axes')

# ── §D3 roster/frame/atlas ──
sub("d-rfa frame row",
    '<i>A coordinate</i> — one point in the 6 axes. A <b>seat</b>. Exists with or without an occupant.</td><td class="id">(axis combinations)</td><td class="n">275,184</td><td class="id">9·13·7·7·6·8 ✓</td>',
    '<i>A coordinate</i> — one point in the 7 axes. A <b>seat</b>. Exists with or without an occupant.</td><td class="id">(axis combinations)</td><td class="n">707,616</td><td class="id">9·13·7·9·4·3·8 ✓</td>')

sub("d-rfa nesting (run)",
    '└ 483   FULLY coded       (all 6 axes; insufficient-context dropped; re-run 2026-07-17 post-dedup)\n              └ 342   distinct coordinates occupied   ( = 0.124% of 275,184 )',
    '└ 483   FULLY coded       (all 6 axes of the EARLIER set; insufficient-context dropped; 2026-07-17)\n              └ 342   distinct coordinates occupied   ( = 0.124% of the then-current 275,184 )')

sub("d-rfa 483 line",
    '<b>483 is the subset of 536 that has all six axes coded cleanly.</b> They are not two independent counts. And 275,184 has nothing to do with how many thinkers exist — it is the size of the grid those 483 are scattered across.',
    '<b>483 is the subset of 536 that has all six axes coded cleanly</b> — six, because the run predates the CLC split; a re-code on the locked seven-axis set has not run. They are not two independent counts. And the lattice figure has nothing to do with how many thinkers exist — it is the size of the grid those 483 are scattered across.')

# ── FAQ ──
sub("faq axes",
    '<b>Is it 6 axes, and are the values "coordinates"?</b></td><td>Six <b>axes</b>; each axis has <b>values</b>; a <b>coordinate</b> is one value chosen per axis — a 6-tuple, which is one <b>frame</b> (a possible mind). A value is not a coordinate.',
    '<b>Is it 6 axes, and are the values "coordinates"?</b></td><td><b>Seven</b> axes since the CLC split stance into S1/S2 (it was six); each axis has <b>values</b>; a <b>coordinate</b> is one value chosen per axis — a 7-tuple, which is one <b>frame</b> (a possible mind). A value is not a coordinate.')

# ── VIZ-8 ──
sub("viz8 lattice", '<div class="v8-omain">275,184 coordinates</div>',
                    '<div class="v8-omain">707,616 coordinates</div>')
sub("viz8 stamp basis",
    'The lattice is the product of the <b>active controlled vocabulary</b> on the six axes (9&#183;13&#183;7&#183;7&#183;6&#183;8), not of the values observed in the codings.',
    'The lattice is the product of the <b>active controlled vocabulary</b> on the seven axes (9&#183;13&#183;7&#183;9&#183;4&#183;3&#183;8), read through <code>v_exom_active_vocabulary</code> — not of the values observed in the codings. It was 275,184 on the earlier six-axis set; the authoritative store has not yet propagated the change.')

# ── VIZ-6 ──
sub("viz6 six-axis space", 'A <b>frame</b> is a location in a six-axis space — not a name.',
                           'A <b>frame</b> is a location in a seven-axis space — not a name.')

# ── the two notes this sweep obsoletes ──
sub("C3 dated note",
    'The <b>S1/S2 stance split above is the current axis set</b> (a different split from the frame/path-coherence one above). <a href="#morphospace">§02</a> and <a href="#d-axes">§D2</a> still describe the <b>earlier six-axis set</b>, because the restructured vocabulary is applied to the working store but <b>not yet to the authoritative one</b> — so the lattice count that follows from it is deliberately not quoted anywhere on this page.',
    'The <b>S1/S2 stance split above is the current axis set</b> (a different split from the frame/path-coherence one above), and <a href="#morphospace">§02</a> and <a href="#d-axes">§D2</a> now describe it too — the page was swept to the locked vocabulary. What has <i>not</i> happened is propagation to the <b>authoritative store</b>, which still carries the earlier six-axis basis; the lattice figure therefore travels with that status wherever it appears.')

sub("FIN disclosure",
    '<br><br><b>What is already current:</b> <a href="#c-gates">§C3</a>\'s account of the gate — including the evaluative/hermeneutic split, which is why the song activates four axes rather than three.\n    <br><b>What still shows the earlier set:</b> <a href="#morphospace">§02</a> and <a href="#d-axes">§D2</a>\'s axis count and value tables, and the lattice figure in <a href="#viz-8">VIZ-8</a>. The <b>post-restructure lattice is not quoted anywhere on this page</b> until the authoritative store agrees with it.',
    '<br><br><b>The page has been swept</b> to the locked seven-axis vocabulary — axis counts, value lists, the tier vocabulary and the lattice all now describe the post-CLC set.\n    <br><b>What has not happened:</b> propagation to the <b>authoritative store</b>, which still carries the earlier six-axis basis. The lattice figure therefore appears with that status attached wherever it is quoted, rather than being withheld.\n    <br><b>What deliberately keeps the earlier figures:</b> anything describing the <i>completed coding run</i> — the 483 fully-coded figures, the 342 occupied coordinates, and the coordinates drawn in <a href="#viz-5">VIZ-5</a>. That run happened on six axes; restating it on seven would falsify it. A re-code has not run.')

p.write_text(h)
print("APPLIED:"); [print("  ✓", d) for d in done]
