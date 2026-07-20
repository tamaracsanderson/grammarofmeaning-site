#!/usr/bin/env python3
"""axisdefs.py — render the axis definitions into §D2 FROM THE STORE.

Not transcribed: queried from exom_axis_vocabulary (definition · term_source ·
definition_status) at build time, so the page cannot become a second store that drifts.

The asymmetry is rendered, not smoothed:
  the AXIS names are mostly inherited (Plantinga · Quine · Aristotle · Ricoeur · Sedgwick)
  the VALUE names are mostly ours, minted by earlier coding runs
Anything with definition_status='project' renders visibly as OURS. Pending renders as a
visible gap — presenting a minted definition as inherited would be a §13 citation-veracity
failure, and hiding the gap would be the same failure by omission.
"""
import sqlite3, sys, pathlib, html as H

DB = "/Users/tamarasanderson/Documents/twelve-laws/data/project.db"
SEVEN = ['epistemic-warrant','ontological-commitment','inferential-operation','telos',
         'evaluative-stance','hermeneutic-posture','ground-world-relation']
LABEL = {'epistemic-warrant':'E','ontological-commitment':'M','inferential-operation':'O',
         'telos':'T','evaluative-stance':'S1','hermeneutic-posture':'S2',
         'ground-world-relation':'G'}

con = sqlite3.connect(DB); con.row_factory = sqlite3.Row
q = lambda s, a=(): con.execute(s, a).fetchall()

axes = {r['axis_name']: r for r in q(
    "SELECT axis_name, definition, term_source, definition_status FROM exom_axis_vocabulary "
    "WHERE sub_level='_axis'")}
# NOTE: the axis-set restriction is REQUIRED. Without it `temporal` (2 pending values)
# leaks in and the pending total reads 30 instead of 28 — the same undeclared-rule bug
# that made the view return 550,368. Declared here so it cannot go silent again.
_ph = ','.join('?'*len(SEVEN))
vals = q("SELECT axis_name, axis_value, definition, term_source, COALESCE(definition_status,'pending') st "
         "FROM exom_axis_vocabulary WHERE (sub_level IS NULL OR sub_level<>'_axis') "
         "AND status NOT IN ('retired','held') AND axis_name IN (" + _ph + ") "
         "ORDER BY axis_name, axis_value", SEVEN)

e = lambda s: H.escape(s or "")
tot = {'sourced': 0, 'project': 0, 'pending': 0}
for r in vals:
    tot[r['st'] if r['st'] in tot else 'pending'] += 1
for a in SEVEN:
    st = (axes.get(a) or {})['definition_status'] if axes.get(a) else 'pending'
    tot[st if st in tot else 'pending'] += 1

CHIP = {'sourced': '<span class="ad-c ad-src">inherited</span>',
        'project': '<span class="ad-c ad-prj">ours</span>',
        'pending': '<span class="ad-c ad-pen">pending</span>'}

rows = []
for a in SEVEN:
    r = axes.get(a)
    st = (r['definition_status'] if r else None) or 'pending'
    src = (r['term_source'] if r else None) or ''
    dfn = (r['definition'] if r else None) or '—'
    rows.append(
        f'<tr class="ad-axrow"><td class="id"><b>{LABEL[a]}</b> · {e(a)}</td>'
        f'<td>{CHIP[st]}</td>'
        f'<td>{e(dfn)}'
        + (f'<div class="ad-src-l"><b>Source:</b> {e(src)}</div>' if src else
           '<div class="ad-src-l ad-ours">Minted here — no external anchor.</div>')
        + '</td></tr>')
    mine = [v for v in vals if v['axis_name'] == a]
    if mine:
        by = {}
        for v in mine:
            by.setdefault(v['st'], []).append(v['axis_value'])
        bits = []
        for k in ('sourced', 'project', 'pending'):
            if by.get(k):
                bits.append(f'{CHIP[k]} ' + ' · '.join(f'<span class="m">{e(x)}</span>' for x in sorted(by[k])))
        rows.append(f'<tr class="ad-valrow"><td class="ad-vl">its values</td><td colspan="2">'
                    + '<br>'.join(bits) + '</td></tr>')

BLOCK = f'''<!-- ══ AXIS DEFINITIONS (rendered from exom_axis_vocabulary) ══ -->
  <h3 class="ad-h">What each axis and value actually means</h3>
  <p class="ad-lede">Rendered <b>from <code>exom_axis_vocabulary</code></b> at build time — the columns <code>definition</code> · <code>term_source</code> · <code>definition_status</code>. Not transcribed, because a transcribed definition is a second store, and a second store drifts.</p>

  <div class="key" style="border-left-color:var(--terracotta)"><b>The asymmetry is the interesting part, so it is shown rather than smoothed.</b>
    <div class="ad-tot"><span class="ad-c ad-src">inherited</span> {tot['sourced']} &nbsp; <span class="ad-c ad-prj">ours</span> {tot['project']} &nbsp; <span class="ad-c ad-pen">pending</span> {tot['pending']}</div>
    <b>The axis names are mostly inherited</b> — warrant from <b>Plantinga</b> (1993), ontological-commitment from <b>Quine</b> (1948), telos from <b>Aristotle</b>, and the S1/S2 split from <b>Ricoeur</b> + <b>Sedgwick</b>. <b>The value names are mostly ours</b>, minted by earlier coding runs without an external anchor.
    <br><br>Everything marked <span class="ad-c ad-prj">ours</span> is <b>our coinage, not a citation</b>. Presenting a minted term as inherited would be a citation-veracity failure; hiding the <span class="ad-c ad-pen">pending</span> gaps would be the same failure by omission. <b>M, O and G's values are undefined</b> — that is a real gap, and it is shown as one.
  </div>

  <div class="tbl"><table class="d ad-t">
    <tr><th style="width:22%">Axis</th><th style="width:10%">Definition</th><th>What it means</th></tr>
    {chr(10).join(rows)}
  </table></div>
  <style>
  #d-axes .ad-h{{font-family:var(--serif);font-size:17px;color:var(--ink);margin:26px 0 3px}}
  #d-axes .ad-lede{{font-size:13px;color:var(--ink-3);margin:2px 0 10px;max-width:86ch;line-height:1.55}}
  #d-axes .ad-tot{{font-family:var(--mono);font-size:12px;margin:6px 0 9px}}
  #d-axes .ad-c{{font-family:var(--mono);font-size:9.5px;letter-spacing:.04em;text-transform:uppercase;padding:1px 7px;border-radius:20px;white-space:nowrap}}
  #d-axes .ad-src{{color:var(--moss);background:rgba(63,125,87,.14)}}
  #d-axes .ad-prj{{color:var(--paper);background:var(--olive)}}
  #d-axes .ad-pen{{color:var(--terracotta);background:rgba(196,96,47,.12)}}
  #d-axes .ad-t td{{vertical-align:top}}
  #d-axes .ad-axrow td{{padding-top:10px}}
  #d-axes .ad-src-l{{font-size:11.5px;color:var(--ink-3);margin-top:5px;line-height:1.45;font-style:italic}}
  #d-axes .ad-ours{{color:var(--olive)}}
  #d-axes .ad-valrow td{{border-top:0;padding-top:2px;font-size:12px;line-height:1.8}}
  #d-axes .ad-vl{{font-size:11px;color:var(--ink-3);font-style:italic}}
  </style>
<!-- ══ /AXIS DEFINITIONS ══ -->

'''

p = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else "method-canonical.html")
h = p.read_text()
import re
if '<!-- ══ AXIS DEFINITIONS' in h:
    h = re.sub(r'<!-- ══ AXIS DEFINITIONS.*?<!-- ══ /AXIS DEFINITIONS ══ -->\n', BLOCK, h, flags=re.S)
    print("re-rendered")
else:
    anchor = '<details class="dd"'
    i = h.find('id="d-axes"'); j = h.find(anchor, i)
    assert j != -1, "insertion point (the details block in D2) not found"
    h = h[:j] + BLOCK + '  ' + h[j:]
    print("inserted into §D2")
p.write_text(h)
print(f"totals rendered: inherited {tot['sourced']} · ours {tot['project']} · pending {tot['pending']}")
