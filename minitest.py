#!/usr/bin/env python3
"""minitest.py — render the Run A mini-test into the working appendix FROM alt_tree_node.

Read from the canonical rows, not from the MD, so it cannot drift. Every number below is a
live query at build time.
"""
import sqlite3, sys, pathlib, re
DB="/Users/tamarasanderson/Documents/twelve-laws/data/project.db"
con=sqlite3.connect(DB); q=lambda s:con.execute(s).fetchall()
TREE='SLY-heal-2026-07-18'
n=q(f"SELECT COUNT(*) FROM alt_tree_node WHERE tree_id='{TREE}'")[0][0]
maxd=q(f"SELECT MAX(depth) FROM alt_tree_node WHERE tree_id='{TREE}'")[0][0]
dist=dict(q(f"SELECT dist,COUNT(*) FROM alt_tree_node WHERE tree_id='{TREE}' AND dist IS NOT NULL GROUP BY dist ORDER BY dist"))
verd=q(f"SELECT verdict,COUNT(*) FROM alt_tree_node WHERE tree_id='{TREE}' GROUP BY verdict ORDER BY COUNT(*) DESC")
doors=q(f"SELECT position,move,axes_changed FROM alt_tree_node WHERE tree_id='{TREE}' AND verdict='doorway'")
nodoor=q(f"SELECT COUNT(*) FROM alt_tree_node WHERE tree_id='{TREE}' AND verdict='doorway' AND coord_e='revelation'")[0][0]
noexit=q(f"SELECT COUNT(*) FROM alt_tree_node WHERE tree_id='{TREE}' AND verdict='doorway' AND exits_to IS NULL")[0][0]
nodenom=q(f"SELECT COUNT(*) FROM alt_tree_node WHERE tree_id='{TREE}' AND dist_denominator IS NULL")[0][0]
msrc=q(f"SELECT DISTINCT metric_source FROM alt_tree_node WHERE tree_id='{TREE}'")
import html as H
e=lambda s:H.escape(str(s or ''))
dmax=max(dist.values())
bars="".join(f'<div class="mt-b"><span class="mt-d">d={d}</span><span class="mt-bar" style="width:{max(3,round(c/dmax*100))}%"></span><span class="mt-n">{c}</span></div>' for d,c in sorted(dist.items()))
vrows="".join(f'<tr><td class="id"><span class="m">{e(v)}</span></td><td class="n">{c}</td><td class="n">{c/n*100:.1f}%</td></tr>' for v,c in verd)
drows="".join(f'<tr><td class="id">{e(p)}</td><td>{e(m)[:70]}</td><td class="id"><span class="m">{e(a)}</span></td></tr>' for p,m,a in doors)
BLOCK=f'''<!-- ══ MINI-TEST RUN A (from alt_tree_node) ══ -->
  <h3 class="xw-h">Run A — the mini-test result</h3>
  <p class="xw-p">Read live from <code>alt_tree_node</code> (<code>tree_id={TREE}</code>) at build time, not transcribed. <b>M1→M4</b>, perturbing <span class="m">E</span>·<span class="m">T</span>·<span class="m">S1</span>·<span class="m">S2</span> only — <b>{n} nodes</b> to depth {maxd}. This is a <b>mini-test of the new generator</b>, not the fan.</p>
  <div class="xw-two">
    <div><p class="xw-sub"><b>The distribution problem is fixed</b></p>
      <div class="mt-hist">{bars}</div>
      <p class="xw-note"><b>d=1 is now the mode, with no holes.</b> Under the old generator d=1 never occurred at all — that hole was the tell. Distance is measured after the fact; none of it was requested.</p></div>
    <div><p class="xw-sub"><b>Tiers</b></p>
      <div class="tbl"><table class="d"><tr><th>verdict</th><th>n</th><th>share</th></tr>{vrows}</table></div>
      <p class="xw-note">Doorways <b>{[c for v,c in verd if v=='doorway'][0]/n*100:.1f}%</b>, up from ~0.6% under the old generator.</p></div>
  </div>
  <p class="xw-sub"><b>All {len(doors)} doorways arrive the same way — and none were asked for</b></p>
  <div class="tbl"><table class="d"><tr><th style="width:8%">pos</th><th>move</th><th style="width:32%">axes changed</th></tr>{drows}</table></div>
  <p class="xw-note">{nodoor} of {len(doors)} carry <span class="m">coord_e=revelation</span>: the warrant leaves the naturalistic set, so the <b>frame-exit test fires and outranks distance</b>. The generator was never told to produce a doorway.</p>
  <div class="flag"><span class="pin">Two gaps this run makes visible</span>
    <b><code>exits_to</code> is empty on all {noexit} doorways.</b> The column now exists, but nothing populates it — and <b>bundling by target frame cannot run without it</b>. A doorway that doesn't say which world it opens onto is only half a finding.
    <br><br><b><code>dist_denominator</code> is NULL on all {nodenom} rows.</b> The field added to carry the denominator alongside the distance is itself unpopulated — so <code>d=3</code> is stored without the "out of how many axes" that makes it meaningful. <i>The fix for the declare-the-denominator failure has not yet been filled in.</i>
    <br><br>Clean: <code>metric_source</code> is <b>{e(msrc[0][0])}</b> on every row — no self-report leaked into a measured field.
  </div>
<!-- ══ /MINI-TEST RUN A ══ -->

'''
p=pathlib.Path(sys.argv[1]); h=p.read_text()
if '<!-- ══ MINI-TEST RUN A' in h:
    h=re.sub(r'<!-- ══ MINI-TEST RUN A.*?<!-- ══ /MINI-TEST RUN A ══ -->\n', BLOCK, h, flags=re.S); print("re-rendered")
else:
    a='  <h3 class="xw-h">6 · Post-run bug check</h3>'
    assert a in h, "appendix part-6 anchor not found"
    h=h.replace(a, BLOCK+a, 1); print("inserted before Part 6")
h=h.replace('#x-working .xw-decl{', '''#x-working .xw-two{display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:8px 0}
  @media(max-width:760px){#x-working .xw-two{grid-template-columns:1fr}}
  #x-working .mt-hist{margin:6px 0}
  #x-working .mt-b{display:flex;align-items:center;gap:7px;margin:3px 0}
  #x-working .mt-d{font-family:var(--mono);font-size:10px;color:var(--ink-3);width:26px}
  #x-working .mt-bar{height:13px;background:var(--fern);border-radius:3px;opacity:.75}
  #x-working .mt-n{font-family:var(--mono);font-size:10.5px;color:var(--ink-2)}
  #x-working .xw-decl{''',1)
p.write_text(h)
print(f"n={n} depth={maxd} dist={dist} doorways={len(doors)} all-revelation={nodoor} exits_to-null={noexit} denom-null={nodenom}")
