#!/usr/bin/env python3
"""Render the-claim METHOD PAGE from its markdown source of record → static HTML.

Source-and-render (per reading-SB + Essay-SB + PI): the prose lives in ONE markdown file
(field_ed/_persona_engine/the-claim.md, Essay-SB authors + reading-SB/PI gate), rendered
here into engine/the-claim.html in its existing house style. Build-time → STATIC HTML so
the reflexive gap-check can read the page (the old hand-authored <span class="tt"> prose
was unreadable to the gate). Re-run when the MD changes.

Usage: python3 gen_theclaim.py <the-claim.md> <out.html>
HOW PRODUCED: design-SB S158 2026-08-03.
"""
import sys, re, html

SRC = sys.argv[1]; OUT = sys.argv[2]
raw = open(SRC, encoding='utf-8').read()
raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S)           # strip the SOURCE-OF-RECORD comment

def esc(s): return html.escape(s, quote=False)
def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s

m_kick = re.search(r'^kicker:\s*(.+)$', raw, re.M)
KICKER = m_kick.group(1).strip() if m_kick else 'Grammar of Meaning'
m_h1 = re.search(r'^#\s+(.+)$', raw, re.M)
TITLE = m_h1.group(1).strip()
body = raw[m_h1.end():]

# split into blocks on blank lines
blocks = [b.strip() for b in re.split(r'\n\s*\n', body) if b.strip()]
out = []
for b in blocks:
    lines = [l.rstrip() for l in b.split('\n')]
    # bulleted list
    if all(l.lstrip().startswith('- ') or (i and not l.lstrip().startswith('- ') and l.startswith((' ', '\t')))
           for i, l in enumerate(lines)):
        items = []
        for l in lines:
            if l.lstrip().startswith('- '): items.append(l.lstrip()[2:])
            elif items: items[-1] += ' ' + l.strip()
        out.append('<ul class="recomp">' + ''.join('<li>' + inline(x) + '</li>' for x in items) + '</ul>')
        continue
    text = ' '.join(lines)
    hm = re.match(r'^#{1,3}\s+(.+)$', text)   # a secondary section heading (e.g. "The ah-ha's")
    if hm:
        out.append('<h2 class="section">' + inline(hm.group(1)) + '</h2>')
        continue
    # a whole-block single-* italic wrapper (lede OR footer links)
    if re.match(r'^\*(?!\*).*[^*]\*$', text):
        inner = text[1:-1]
        if '→' in inner or re.search(r'\]\(', inner):
            # footer nav block (arrow links) -> notes-link style; split on the → bullets
            parts = [p.strip() for p in re.split(r'\s*→\s*', inner) if p.strip()]
            out.append('<p class="notes-link">' + '<br>'.join('&rarr; ' + inline(p) for p in parts) + '</p>')
        else:
            out.append('<p class="lede"><em>' + inline(inner) + '</em></p>')
        continue
    out.append('<p>' + inline(text) + '</p>')

BODY = '\n'.join(out)

PAGE = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>The claim — Grammar of Meaning</title>
<!-- RENDERED from field_ed/_persona_engine/the-claim.md (source of record). Do not hand-edit; edit the MD + re-run gen_theclaim.py. -->
<style>
:root{--bg:#F6F1E4;--paper:#FFFDF6;--fg:#24302A;--muted:#6E7669;--line:#C9BE9F;--out:#C4602F;
 --serif:Iowan Old Style,Palatino,Georgia,serif;--sans:ui-sans-serif,-apple-system,Segoe UI,sans-serif}
@media(prefers-color-scheme:dark){:root{--bg:#1B211D;--paper:#232A25;--fg:#EDE7D8;--muted:#A6AEA3;
 --line:#3A423C;--out:#D9793F}}
:root[data-theme=dark]{--bg:#1B211D;--paper:#232A25;--fg:#EDE7D8;--muted:#A6AEA3;--line:#3A423C;--out:#D9793F}
:root[data-theme=light]{--bg:#F6F1E4;--paper:#FFFDF6;--fg:#24302A;--muted:#6E7669;--line:#C9BE9F;--out:#C4602F}
body{margin:0;background:var(--bg);color:var(--fg);font-family:var(--serif);font-size:17.5px;line-height:1.68}
main{max-width:34rem;margin:0 auto;padding:9vh 22px 12vh}
h1{font-size:30px;line-height:1.2;margin:0 0 10px;font-weight:600;text-wrap:balance}
h2.section{font-size:21px;line-height:1.25;margin:38px 0 4px;font-weight:600;color:var(--fg);padding-top:20px;border-top:1px solid var(--line)}
.kicker{font-family:var(--sans);font-size:11px;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);margin:0 0 14px}
p{margin:18px 0}
.lede{margin:6px 0 22px;padding:14px 20px 16px;border-left:3px solid var(--out);background:color-mix(in srgb,var(--out) 6%,transparent);border-radius:0 10px 10px 0;font-size:18.5px;line-height:1.55;color:var(--fg)}
.lede em{font-style:italic}
p strong,li strong{color:var(--fg)}
p strong:first-child{color:var(--out)}
.recomp{margin:16px 0;padding-left:0;list-style:none}
.recomp li{margin:12px 0;padding-left:18px;position:relative}
.recomp li::before{content:"—";position:absolute;left:0;color:var(--out)}
.recomp li strong{color:var(--out)}
.back{display:inline-block;margin-top:38px;font-family:var(--sans);font-size:13px;color:var(--out);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--out) 45%,transparent)}
.back:hover{background:color-mix(in srgb,var(--out) 12%,transparent)}
.notes-link{font-family:var(--sans);font-size:13.5px;margin:26px 0 0;line-height:2;padding-top:18px;border-top:1px solid var(--line)}
.notes-link a{color:var(--out);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--out) 45%,transparent)}
.themebtn{position:fixed;top:14px;right:14px;background:var(--paper);border:1px solid var(--line);border-radius:999px;padding:6px 14px;font-size:12px;cursor:pointer;color:var(--fg);font-family:var(--sans)}
</style>
</head>
<body>
<button class="themebtn" onclick="var r=document.documentElement;r.dataset.theme=r.dataset.theme==='dark'?'light':'dark'">theme</button>
<main>
<p class="kicker">__KICKER__</p>
<h1>__TITLE__</h1>
__BODY__
<p class="notes-link"><a href="rebuttals.html">The hard questions &mdash; objections &amp; answers &rarr;</a><br><a href="how-we-test.html">How we test this &rarr;</a><br><a href="reflexive.html">The full reflexive gloss &rarr;</a></p>
<a class="back" href="schema.html">&larr; the schema of the instrument</a>
</main>
</body>
</html>'''
PAGE = (PAGE.replace('__KICKER__', esc(KICKER))
            .replace('__TITLE__', inline(TITLE))
            .replace('__BODY__', BODY))

open(OUT, 'w', encoding='utf-8').write(PAGE)
print('wrote %s (%d bytes) · %d blocks' % (OUT, len(PAGE), len(blocks)))
