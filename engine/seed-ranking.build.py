#!/usr/bin/env python3
"""build_scatter.py — the 1.C Seed-Ranking scatterplot (She Loves You).

Generated FROM the data pack's CSV (DATA_seed_ranking_scatterplot_SLY_2026-07-26.md),
not transcribed — the pack's store-of-record is the seed_ranking DB table (§2.13); this
reads the pack's paste-ready CSV so the points are the real coordinates.

Spec (reading-SB / PI, S155): x=dependency 0→17, y=salience 6→30, all 23 moves; three
annotated callouts (M4 structural, M14 salience, M1 human-pick); quadrant labels; the point
is ranking ≠ choosing; y-axis labelled a COMPUTED PROXY for rhetorical centrality (pack footer).
Green, self-contained.
"""
import re, csv, io, html, pathlib

pack = pathlib.Path("dataA.md").read_text()
csv_block = re.search(r"```csv\n(.*?)```", pack, re.S).group(1)
rows = list(csv.DictReader(io.StringIO(csv_block)))
pts = [dict(move=r["move"], x=int(r["x_dependency"]), y=int(r["y_salience"]),
            callout=r["callout"], label=r["label"]) for r in rows]
assert len(pts) == 23, f"expected 23 moves, got {len(pts)}"

# ── geometry ──
W, H = 760, 620
ML, MR, MT, MB = 92, 40, 70, 78          # margins
PW, PH = W-ML-MR, H-MT-MB
XMIN, XMAX = 0, 17
YMIN, YMAX = 6, 30
def sx(x): return ML + (x-XMIN)/(XMAX-XMIN)*PW
def sy(y): return MT + (1-(y-YMIN)/(YMAX-YMIN))*PH
XMID, YMID = 8.5, 18                      # quadrant split (mid of each range)

e = html.escape
svg = []
svg.append(f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" '
           f'aria-label="Seed-ranking scatterplot: dependency (structural centrality) on x, salience (rhetorical centrality, a computed proxy) on y, for 23 moves of She Loves You.">')

# quadrant shading (top-right = the near-empty "obvious anchors" corner)
svg.append(f'<rect x="{sx(XMID):.0f}" y="{MT}" width="{ML+PW-sx(XMID):.0f}" height="{sy(YMID)-MT:.0f}" class="q-empty"/>')
# quadrant divider lines
svg.append(f'<line x1="{sx(XMID):.1f}" y1="{MT}" x2="{sx(XMID):.1f}" y2="{MT+PH}" class="qline"/>')
svg.append(f'<line x1="{ML}" y1="{sy(YMID):.1f}" x2="{ML+PW}" y2="{sy(YMID):.1f}" class="qline"/>')

# axes
svg.append(f'<line x1="{ML}" y1="{MT+PH}" x2="{ML+PW}" y2="{MT+PH}" class="axis"/>')
svg.append(f'<line x1="{ML}" y1="{MT}" x2="{ML}" y2="{MT+PH}" class="axis"/>')
# ticks
for xv in range(0,18,3):
    svg.append(f'<line x1="{sx(xv):.1f}" y1="{MT+PH}" x2="{sx(xv):.1f}" y2="{MT+PH+5}" class="tick"/>')
    svg.append(f'<text x="{sx(xv):.1f}" y="{MT+PH+18}" class="tk" text-anchor="middle">{xv}</text>')
for yv in range(6,31,6):
    svg.append(f'<line x1="{ML-5}" y1="{sy(yv):.1f}" x2="{ML}" y2="{sy(yv):.1f}" class="tick"/>')
    svg.append(f'<text x="{ML-9}" y="{sy(yv)+3.5:.1f}" class="tk" text-anchor="end">{yv}</text>')

# quadrant corner labels
svg.append(f'<text x="{ML+PW-6}" y="{MT+13}" class="ql" text-anchor="end">obvious anchors — nearly empty</text>')
svg.append(f'<text x="{ML+PW-6}" y="{MT+PH-8}" class="ql" text-anchor="end">structural, not felt</text>')
svg.append(f'<text x="{ML+6}" y="{MT+13}" class="ql" text-anchor="start">felt, not structural</text>')
svg.append(f'<text x="{ML+6}" y="{MT+PH-8}" class="ql" text-anchor="start">connective tissue</text>')

CALL = {"HUMAN-PICK":"pt-human", "STRUCTURAL":"pt-struct", "SALIENCE":"pt-sal"}
# ordinary points first, highlighted last (draw on top)
for p in sorted(pts, key=lambda p: p["callout"]!=""):
    cx, cy = sx(p["x"]), sy(p["y"])
    cls = CALL.get(p["callout"], "pt")
    r = 8 if p["callout"] else 5
    svg.append(f'<g class="{cls}"><title>{e(p["move"])} — dep {p["x"]}, sal {p["y"]}: {e(p["label"])}</title>'
               f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}"/>'
               f'<text x="{cx:.1f}" y="{cy-(r+4):.1f}" class="mlab" text-anchor="middle">{e(p["move"])}</text></g>')

# ── callout annotations (leader line + boxed note) ──
def callout(px, py, tx, ty, w, lines, cls):
    s=[f'<line x1="{px:.1f}" y1="{py:.1f}" x2="{tx:.1f}" y2="{ty:.1f}" class="lead"/>',
       f'<rect x="{tx:.1f}" y="{ty:.1f}" width="{w}" height="{14+len(lines)*15}" rx="6" class="note {cls}"/>']
    for i,ln in enumerate(lines):
        b='note-h' if i==0 else 'note-b'
        s.append(f'<text x="{tx+9:.1f}" y="{ty+16+i*15:.1f}" class="{b}">{ln}</text>')
    return "".join(s)

m4=next(p for p in pts if p["move"]=="M4"); m14=next(p for p in pts if p["move"]=="M14"); m1=next(p for p in pts if p["move"]=="M1")
svg.append(callout(sx(m4["x"]), sy(m4["y"]), sx(m4["x"])-238, sy(m4["y"])+8, 232,
    ["M4 · structural anchor","everything leans on it —","but nobody would call it the song."], "n-struct"))
svg.append(callout(sx(m14["x"]), sy(m14["y"]), sx(m14["x"])+18, sy(m14["y"])-2, 226,
    ["M14 · the felt center","reads as the heart —","but little depends on it."], "n-sal"))
svg.append(callout(sx(m1["x"]), sy(m1["y"]), sx(m1["x"])+20, sy(m1["y"])+16, 214,
    ["M1 · the human's pick","top of no column —","the call no ranking makes."], "n-human"))

# axis titles
svg.append(f'<text x="{ML+PW/2:.0f}" y="{H-24}" class="axt" text-anchor="middle">dependency &#8594; structural centrality  <tspan class="axt-sub">(computed: how many moves build on it)</tspan></text>')
svg.append(f'<text x="26" y="{MT+PH/2:.0f}" class="axt" text-anchor="middle" transform="rotate(-90 26 {MT+PH/2:.0f})">salience &#8594; rhetorical centrality  <tspan class="axt-sub">(a computed proxy)</tspan></text>')
svg.append('</svg>')
SVG="".join(svg)

DOC=f'''<div class="seedscatter" id="seed-scatter">
<style>
.seedscatter{{font-family:var(--sans,Inter,system-ui,sans-serif);color:var(--ink,#24302A);max-width:820px}}
.seedscatter h3{{font-family:var(--serif,Newsreader,Georgia,serif);font-size:21px;color:var(--ink,#24302A);margin:0 0 4px}}
.seedscatter .lede{{font-size:14px;color:var(--ink-2,#4A5952);line-height:1.6;margin:0 0 6px;max-width:76ch}}
.seedscatter .lede b{{color:var(--moss,#2C4A38)}}
.seedscatter .scroll{{overflow-x:auto}}
.seedscatter svg{{display:block;max-width:100%;height:auto;background:var(--paper,#FCFBF7);border:1px solid var(--rule,#C9BE9F);border-radius:12px}}
.seedscatter .q-empty{{fill:rgba(63,125,87,.05)}}
.seedscatter .qline{{stroke:var(--rule,#C9BE9F);stroke-width:1;stroke-dasharray:3 4;opacity:.7}}
.seedscatter .axis{{stroke:var(--ink-3,#7C8478);stroke-width:1.2}}
.seedscatter .tick{{stroke:var(--ink-3,#7C8478);stroke-width:1}}
.seedscatter .tk{{font-family:var(--mono,IBM Plex Mono,monospace);font-size:10px;fill:var(--ink-3,#7C8478)}}
.seedscatter .ql{{font-family:var(--sans,Inter,sans-serif);font-size:9.5px;fill:var(--ink-3,#7C8478);font-style:italic;letter-spacing:.02em}}
.seedscatter .axt{{font-family:var(--sans,Inter,sans-serif);font-size:12.5px;fill:var(--ink-2,#4A5952);font-weight:600}}
.seedscatter .axt-sub{{font-weight:400;font-size:10.5px;fill:var(--ink-3,#7C8478);font-style:italic}}
.seedscatter .pt circle{{fill:var(--sage,#8BA888);opacity:.62}}
.seedscatter .mlab{{font-family:var(--mono,monospace);font-size:8.5px;fill:var(--ink-3,#7C8478)}}
.seedscatter .pt-struct circle{{fill:var(--moss,#2C4A38)}}
.seedscatter .pt-sal circle{{fill:var(--olive,#6E7B3A)}}
.seedscatter .pt-human circle{{fill:var(--terracotta,#C4602F);stroke:var(--paper,#FCFBF7);stroke-width:2}}
.seedscatter .pt-struct .mlab,.seedscatter .pt-sal .mlab,.seedscatter .pt-human .mlab{{fill:var(--ink,#24302A);font-weight:700;font-size:10px}}
.seedscatter .lead{{stroke:var(--ink-3,#7C8478);stroke-width:1;stroke-dasharray:2 2;opacity:.8}}
.seedscatter .note{{fill:var(--paper-3,#FFFFFF);stroke:var(--rule,#C9BE9F);stroke-width:1}}
.seedscatter .n-struct{{stroke:var(--moss,#2C4A38)}}
.seedscatter .n-sal{{stroke:var(--olive,#6E7B3A)}}
.seedscatter .n-human{{stroke:var(--terracotta,#C4602F);stroke-width:1.6}}
.seedscatter .note-h{{font-family:var(--sans,sans-serif);font-size:11px;font-weight:700;fill:var(--ink,#24302A)}}
.seedscatter .note-b{{font-family:var(--sans,sans-serif);font-size:10.5px;fill:var(--ink-2,#4A5952)}}
.seedscatter .insight{{font-size:13.5px;line-height:1.6;color:var(--ink-2,#4A5952);background:var(--paper-2,#EFE7D3);border-left:3px solid var(--moss,#2C4A38);border-radius:0 8px 8px 0;padding:11px 14px;margin:12px 0 0;max-width:80ch}}
.seedscatter .insight b{{color:var(--ink,#24302A)}}
.seedscatter .foot{{font-size:11.5px;color:var(--ink-3,#7C8478);line-height:1.55;margin:10px 0 0;max-width:82ch}}
</style>
  <h3>1.C · Seed ranking — the instrument ranks, the human chooses</h3>
  <p class="lede">Every move of <i>She Loves You</i> on the two seed-criteria that most <b>disagree</b>: how much of the song structurally <b>depends</b> on it (x), and how much it reads as the emotional <b>heart</b> (y). The human's actual seed — <b>M1</b> — tops neither column.</p>
  <div class="scroll">{SVG}</div>
  <div class="insight"><b>Ranking &#8800; choosing.</b> The instrument ranks on four objective columns; <b>M4</b> wins structural dependency, <b>M14</b> wins salience, and the move the researcher actually seeded — <b>M1</b> — is #1 on none of them. The tool informs the human; it does not replace the call. That empty top-right corner — high on both — is itself the finding: the obvious anchor the song never has.</p>
  <p class="foot"><b>Honesty:</b> the y-axis (salience) is a <b>computed proxy</b> for rhetorical centrality — more interpretive than dependency, which is a direct count. Source: the <code>seed_ranking</code> table (SLY-1963), 23 of 24 labelled moves scored (M23 absent, not an error). Coordinates read from <code>DATA_seed_ranking_scatterplot_SLY_2026-07-26.md</code>.</p>
</div>'''

pathlib.Path("seed_scatter_fragment.html").write_text(DOC)
# also a standalone reviewable page
head=('<!doctype html><html lang="en"><head><meta charset="utf-8">'
      '<meta name="viewport" content="width=device-width,initial-scale=1">'
      '<title>1.C · Seed-Ranking scatterplot — Grammar of Meaning</title>'
      '<link rel="preconnect" href="https://fonts.googleapis.com">'
      '<link href="https://fonts.googleapis.com/css2?family=Newsreader:opsz,wght@6..72,400;6..72,600&family=Inter:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;600&display=swap" rel="stylesheet">'
      '<style>:root{--paper:#FCFBF7;--paper-2:#EFE7D3;--paper-3:#FFFFFF;--rule:#C9BE9F;--ink:#24302A;--ink-2:#4A5952;--ink-3:#7C8478;--fern:#3F7D57;--moss:#2C4A38;--sage:#8BA888;--olive:#6E7B3A;--terracotta:#C4602F}'
      'body{background:var(--paper);margin:0;padding:40px 24px}main{max-width:860px;margin:0 auto}</style></head><body><main>')
pathlib.Path("seed_scatter_page.html").write_text(head+DOC+"</main></body></html>")
print("built:", len(DOC), "bytes fragment |", len(pts), "points | M1/M4/M14 callouts placed")
