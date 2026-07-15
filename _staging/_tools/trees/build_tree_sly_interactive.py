#!/usr/bin/env python3
"""Add the FILLED/POSSIBLE/PRUNED gap-state layer to reading-SB's She-Loves-You trace-tree.

Item A (part 2) of the S150 design-SB batch. The song tree is already node-interactive
(click a node → detail); this adds the gap explorer that mirrors the golden-chain's — the
song's gaps as an expand-on-click accordion, each fill tagged FILLED / POSSIBLE / PRUNED with
why. Content lifted from the source's own move-table + residuals + review box; nothing invented.
The song's real prunings: the her-voice lens demoted per IRR177 (1/5 cold → reader-lens, not a
form gap), and the deeper roots deliberately omitted as too speculative.

Usage: build_tree_sly_interactive.py <src_tree_she_loves_you.html> <OUTPUT.html>
"""
import sys, json

GAPS = [
  dict(slot="the song fills itself", q="~80% self-completing (the 8 moves)", gap=None, fills=[
    dict(label="M1–M3 · hurt → suffer → reappraise (narrate)", state="FILLED", tier="self", why="the backstory the song reports on — it answers its own setup."),
    dict(label="M4 · loves — the core (report)", state="FILLED", tier="self", why="the third-person love-report; the song’s money move."),
    dict(label="M6 · relay / witness (report)", state="FILLED", tier="self", why="the friend-as-messenger — the meta-move made explicit."),
    dict(label="M7 · “be glad” (directive)", state="FILLED", tier="self", why="the call-and-response exhortation (“yeah yeah yeah”)."),
    dict(label="M8 · “apologize” (directive)", state="FILLED", tier="self", why="the resolution the song presses toward."),
  ]),
  dict(slot="reciprocity", q="does HE love her back?", gap="5/5 cold", fills=[
    dict(label="a cover from his POV · a sequel", state="POSSIBLE", tier="reception-target", why="never stated — a gap the FORM produces (all five cold cohorts touch it, IRR177). Only an external voice fills it."),
  ]),
  dict(slot="the messenger’s motive", q="why does the friend care?", gap="5/5 cold", fills=[
    dict(label="a jealous-friend / triangulation reading", state="POSSIBLE", tier="reception-target", why="the witness’s stake is never given — confirmed 5/5 cold. The meta-move’s own money-cell gap."),
  ]),
  dict(slot="her voice", q="the un-voiced woman", gap="1/5 cold", fills=[
    dict(label="a reader-supplied lens · a woman’s-POV cover", state="POSSIBLE", tier="reader-lens", why="a real reader-lens — she is talked about for 8 moves, never speaks."),
    dict(label="…as a FORM-produced gap", state="PRUNED", tier="1/5 cold", why="demoted per the IRR177 cold correction: only 1/5 cohorts surfaced it cold, so it is a reader-lens, NOT a gap the form foregrounds. Pruned from primary, kept as secondary — the pruning shown, not hidden."),
  ]),
  dict(slot="deeper roots (below the pivot)", q="the pop equivalent of the NT’s pagan/Jewish grafts", gap="omitted", fills=[
    dict(label="African-American gospel structure (under R3)", state="PRUNED", tier="too-speculative", why="deliberately omitted as too speculative (review #5) — a deeper graft-tier candidate, held pending the backward-admissibility IRR."),
    dict(label="Tin-Pan-Alley craft as itself a graft of earlier song-forms (under R4)", state="PRUNED", tier="too-speculative", why="omitted for the same reason — held for a deeper root tier rather than asserted."),
  ]),
]

def build(src, out):
    h = open(src).read()
    h = h.replace('<title>Bidirectional trace-tree — "She Loves You" (candidate pilot)</title>',
                  '<title>Interactive trace-tree — "She Loves You" (candidate pilot)</title>\n<meta name="robots" content="noindex,nofollow">')

    css = """
  /* ---- gap-state layer (design-SB, Item A part 2) — mirrors the golden-chain grammar ---- */
  .gapsec{margin:2rem 0}
  .statekey{display:flex;gap:14px;flex-wrap:wrap;font-family:var(--mono);font-size:11.5px;color:var(--muted);margin:.2rem 0 .9rem}
  .st{font-family:var(--mono);font-size:9.5px;font-weight:700;letter-spacing:.04em;text-transform:uppercase;
    padding:2px 8px;border-radius:20px;white-space:nowrap}
  .st.FILLED{background:var(--root-soft);color:var(--root);border:1px solid var(--root)}
  .st.POSSIBLE{background:var(--accent-soft);color:var(--accent);border:1px solid var(--accent)}
  .st.PRUNED{background:var(--paper);color:var(--muted);border:1px solid var(--hair)}
  .gaprow{border:1px solid var(--hair);border-radius:11px;margin:9px 0;overflow:hidden;background:var(--surface)}
  .gaphead{display:flex;align-items:center;gap:10px;padding:12px 15px;cursor:pointer;font-family:var(--sans)}
  .gaphead:hover{background:var(--paper)}
  .gaphead .slot{font-family:var(--serif);font-weight:600;font-size:15px;color:var(--ink)}
  .gaphead .q{font-size:12.5px;color:var(--muted)}
  .gaphead .gid{margin-left:auto;font-family:var(--mono);font-size:10.5px;font-weight:700;color:var(--recept);
    border:1px solid var(--recept);border-radius:20px;padding:2px 9px;white-space:nowrap}
  .gaphead .caret{color:var(--muted);transition:transform .18s}
  .gaprow.open .caret{transform:rotate(90deg)}
  .gapfills{display:none;padding:2px 15px 13px}
  .gaprow.open .gapfills{display:block}
  .fill{display:flex;gap:10px;align-items:flex-start;padding:9px 0;border-top:1px solid var(--hair)}
  .fill .ftxt{font-size:13.5px}
  .fill.pruned .flabel{text-decoration:line-through;color:var(--muted)}
  .fill .flabel{font-weight:600}
  .fill .fwhy{color:var(--muted);font-size:12.5px;margin-top:2px}
  .fill .ftier{font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-left:6px}
  .backlink{display:inline-block;margin:1.4rem 0 0;font-family:var(--sans);font-size:13.5px}
</style>"""
    h = h.replace("</style>", css, 1)

    # gap-explorer section, inserted right before the review box
    gj = json.dumps(GAPS, ensure_ascii=False)
    section = '''    <div class="gapsec">
      <h2>The gap explorer — filled · possible · pruned</h2>
      <p>The same lens as the golden-chain tree, on the song. Expand a gap to see its fills tagged by state — what the song <b>fills</b> itself (~80%), what stays <b>possible</b> (a reception target only an outside voice completes), and what was <b>pruned</b> (shown, not hidden — the her-voice lens demoted per the IRR177 cold correction, and the deeper roots held as too speculative).</p>
      <div class="statekey">
        <span><span class="st FILLED">filled</span> the song fills it</span>
        <span><span class="st POSSIBLE">possible</span> a reception target / reader-lens</span>
        <span><span class="st PRUNED">pruned</span> ruled out or demoted — shown</span>
      </div>
      <div id="gapexplorer"></div>
    </div>
'''
    h = h.replace('    <div class="review">', section + '    <div class="review">', 1)

    # backlink after the foot
    h = h.replace('    </div>\n  </div>\n\n<script>',
                  '    </div>\n    <a class="backlink" href="coding-lab.html">← back to the coding lab</a>\n  </div>\n\n<script>', 1)

    # JS to render the accordion (appended inside the existing <script>, before </script>)
    js = "\n// ---- gap explorer (design-SB, Item A part 2) ----\nvar GAPS=" + gj + r""";
(function(){
  var host=document.getElementById('gapexplorer'); if(!host) return;
  var html='';
  GAPS.forEach(function(g){
    html+='<div class="gaprow"><div class="gaphead" onclick="this.parentNode.classList.toggle(\'open\')">'
      +'<span class="caret">▸</span><span class="slot">'+g.slot+'</span><span class="q">'+g.q+'</span>'
      +(g.gap?'<span class="gid">'+g.gap+'</span>':'')+'</div><div class="gapfills">';
    g.fills.forEach(function(f){
      html+='<div class="fill'+(f.state==='PRUNED'?' pruned':'')+'"><span class="st '+f.state+'">'+f.state.toLowerCase()+'</span>'
        +'<div class="ftxt"><span class="flabel">'+f.label+'</span><span class="ftier">'+f.tier+'</span>'
        +'<div class="fwhy">'+f.why+'</div></div></div>';
    });
    html+='</div></div>';
  });
  host.innerHTML=html;
})();
"""
    h = h.replace("</script>", js + "\n</script>", 1)
    open(out, "w").write(h)
    print(f"wrote {out} — {len(GAPS)} gap slots, {sum(len(g['fills']) for g in GAPS)} fills")

if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2])
