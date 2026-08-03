#!/usr/bin/env python3
"""Generate a reading-room FIELD-GUIDE page (artfieldguide aesthetic) from a Situate reading MD.

Reusable per room: the six-part frame (Preface · Frontispiece · Sitz · Paradigm · Frame · Lineage ·
"Where did this come from") is the instrument's fixed SITUATE layers, so any future room swaps the MD
and re-runs this. Renders in the Lovable "Victorian Botanical" design language as a self-contained
static page (no build step / no runtime markdown dep), two-column with a sticky scroll-spy rail.

Usage: python3 gen_situate_fieldguide.py <reading.md> <out.html>
HOW PRODUCED: design-SB S158 2026-08-03, per the FOR-DESIGN-SB render spec embedded in
  situate_reading_gospels_PRIMARY_s158; aesthetic ported from the PI's artful-journey-guide Lovable export.
"""
import sys, re, html, json

SRC = sys.argv[1] if len(sys.argv) > 1 else 'situate_gospels.md'
OUT = sys.argv[2] if len(sys.argv) > 2 else 'situate.html'
VIZ_PATH = sys.argv[3] if len(sys.argv) > 3 else None
VIZ = json.load(open(VIZ_PATH, encoding='utf-8')) if VIZ_PATH else {}

raw = open(SRC, encoding='utf-8').read()

# ── strip internal matter: the top blockquote note, and the two HTML comments ──
raw = re.sub(r'<!--.*?-->', '', raw, flags=re.S)                       # design-SB note + methodology footer
# top: keep the # title + first ### subtitle; drop the > blockquote before "## How to read this"
m_title = re.search(r'^#\s+(.+)$', raw, re.M)
TITLE = m_title.group(1).strip()
m_sub = re.search(r'^###\s+(.+)$', raw, re.M)
SUBTITLE = m_sub.group(1).strip()
# body starts at the first "## " section
body = raw[raw.index('## '):]

# ── split into ## sections ──
parts = re.split(r'(?m)^##\s+', body)
sections = []  # (heading, content)
for p in parts:
    if not p.strip():
        continue
    lines = p.split('\n', 1)
    head = lines[0].strip()
    content = lines[1] if len(lines) > 1 else ''
    sections.append((head, content.strip()))

# ── inline markdown → HTML ──
def esc(s): return html.escape(s, quote=False)
def inline(s):
    s = esc(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)', r'<em>\1</em>', s)
    s = re.sub(r'`(.+?)`', r'<code>\1</code>', s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', s)
    return s

def level_class(tag):
    """Fuzzy-map any lens-tag to a colour class (handles 'John on its own', future 'Mark on its own', etc.)."""
    t = tag.lower()
    if 'braid' in t: return 'lv-braid'
    if 'on its own' in t: return 'lv-each'
    return 'lv-whole'

# ── viz renderers: static SVG/HTML from the coded viz-data JSON (engine-backed) ──
EMBLEM = {'Matthew': '\U0001F477'.replace('\U0001F477', '✦'), 'Mark': '\U0001F981',
          'Luke': '\U0001F402', 'John': '\U0001F985'}
EMBLEM = {'Matthew': '\U0001F464', 'Mark': '\U0001F981', 'Luke': '\U0001F402', 'John': '\U0001F985'}
GOSPELS = ['Matthew', 'Mark', 'Luke', 'John']
ABBR = {'Matthew': 'Mt', 'Mark': 'Mk', 'Luke': 'Lk', 'John': 'Jn'}

def viz_paradigm(v):
    sd = v.get('shared_dominant', ''); ps = v.get('per_source', {})
    cards = []
    for g in GOSPELS:
        d = ps.get(g, {}); dom = d.get('dominant', '')
        secs = sorted([s for s in d.get('scripts', []) if not s.get('is_dominant') and s.get('name') != dom],
                      key=lambda s: -s.get('salience', 0))[:2]
        sec = ''.join('<li>' + inline(s['name']) + '</li>' for s in secs)
        cards.append('<div class="pdg-card"><div class="pdg-emblem">' + EMBLEM.get(g, '') + '</div>'
                     '<div class="pdg-g">' + g + '</div><div class="pdg-dom">' + inline(dom) + '</div>'
                     + (('<ul class="pdg-sec">' + sec + '</ul>') if sec else '') + '</div>')
    return ('<figure class="viz-real viz-paradigm"><div class="pdg-shared">All four share one dominant script — '
            '<b>' + inline(sd) + '</b> — and inflect it differently:</div><div class="pdg-grid">'
            + ''.join(cards) + '</div><figcaption>' + esc(v.get('provenance', '')) + '</figcaption></figure>')

def viz_frame(v):
    ps = v.get('per_source', {}); axes = v.get('axes', [])
    val = {}
    for g in GOSPELS:
        for a in ps.get(g, []):
            val[(a['axis'], g)] = a['value']
    shared, diverge = [], []
    for ax in axes:
        vals = [val.get((ax, g), '') for g in GOSPELS]
        if len(set(vals)) == 1 and vals[0]:
            shared.append((ax, vals[0]))
        else:
            diverge.append((ax, list(zip(GOSPELS, vals))))
    body = ('<div class="fr-legend"><span class="fr-chip shared">shared</span> the common ground'
            '&nbsp;&nbsp; <span class="fr-chip div">split</span> where they diverge</div>')
    for ax, v0 in shared:
        body += ('<div class="fr-row"><div class="fr-ax">' + inline(ax) + '</div><div class="fr-val">'
                 '<span class="fr-chip shared">' + inline(v0) + '</span> <span class="fr-note">all four agree</span></div></div>')
    for ax, pairs in diverge:
        chips = ''.join('<span class="fr-chip div"><b>' + ABBR.get(g, g[:2]) + '</b>&nbsp;' + inline(v0) + '</span>' for g, v0 in pairs)
        body += '<div class="fr-row"><div class="fr-ax">' + inline(ax) + '</div><div class="fr-val">' + chips + '</div></div>'
    return '<figure class="viz-real viz-frame">' + body + '<figcaption>' + esc(v.get('provenance', '')) + '</figcaption></figure>'

def _svg_wrap(text, x, y, cls, up, maxc=17, lh=13):
    words = text.split(); lines = []; cur = ''
    for w in words:
        if cur and len(cur + ' ' + w) > maxc: lines.append(cur); cur = w
        else: cur = (cur + ' ' + w).strip()
    if cur: lines.append(cur)
    lines = lines[:3]
    out = '<text class="%s" text-anchor="middle">' % cls
    for k, ln in enumerate(lines):
        yy = y - (len(lines) - 1 - k) * lh if up else y + k * lh
        out += '<tspan x="%.0f" y="%.0f">%s</tspan>' % (x, yy, esc(ln))
    return out + '</text>'

def viz_timeline(v):
    ev = sorted(v.get('events', []), key=lambda e: e.get('sort', 0))
    if not ev: return ''
    xs = [e.get('sort', 0) for e in ev]; lo, hi = min(xs), max(xs)
    W, H, padx = 920, 260, 74
    X = lambda s: padx + (s - lo) / (hi - lo) * (W - 2 * padx) if hi > lo else W / 2
    ay = H / 2
    p = ['<svg viewBox="0 0 %d %d" class="vz-svg" role="img" aria-label="timeline of the gospels and their world">' % (W, H)]
    p.append('<line x1="%d" y1="%.0f" x2="%d" y2="%.0f" class="vz-axis"/>' % (padx, ay, W - padx, ay))
    tx = X(70)
    p.append('<line x1="%.0f" y1="28" x2="%.0f" y2="%d" class="vz-hinge"/>' % (tx, tx, H - 28))
    p.append('<text x="%.0f" y="20" class="vz-hinge-lab" text-anchor="middle">Temple falls · 70 CE</text>' % tx)
    up = True
    for idx, e in enumerate(ev):
        x = X(e.get('sort', 0)); gsp = e.get('kind') == 'gospel'
        p.append('<circle cx="%.0f" cy="%.0f" r="%d" class="vz-dot%s"/>' % (x, ay, 5 if gsp else 3, ' vz-gospel' if gsp else ''))
        if gsp or idx <= 1:   # label the 4 gospels + the two early anchors (Jesus, Paul); the 70-CE cluster stays context dots (Temple = the hinge)
            ly = ay - 62 if up else ay + 62
            p.append('<line x1="%.0f" y1="%.0f" x2="%.0f" y2="%.0f" class="vz-conn"/>' % (x, ay, x, ly + (14 if up else -14)))
            p.append('<text x="%.0f" y="%.0f" class="vz-yr" text-anchor="middle">%s</text>' % (x, ay + (20 if up else -12), esc(e.get('year', ''))))
            p.append(_svg_wrap(e.get('label', ''), x, ly, 'vz-ev-lab' + (' vz-gospel-lab' if gsp else ''), up))
            up = not up
    p.append('</svg>')
    return '<figure class="viz-real viz-timeline">' + ''.join(p) + '<figcaption>' + esc(v.get('provenance', '')) + '</figcaption></figure>'

def viz_map(v):
    homes = v.get('homes', [])
    pts = [h for h in homes if h.get('lat') is not None]
    unc = [h for h in homes if h.get('lat') is None]
    if not pts: return ''
    W, H, pad = 680, 300, 58
    lons = [h['lon'] for h in pts]; lats = [h['lat'] for h in pts]
    lo_x, hi_x = min(lons), max(lons); lo_y, hi_y = min(lats), max(lats)
    dx = (hi_x - lo_x) or 1; dy = (hi_y - lo_y) or 1
    lo_x -= dx * 0.28; hi_x += dx * 0.28; lo_y -= dy * 0.55; hi_y += dy * 0.55
    PX = lambda lon: pad + (lon - lo_x) / (hi_x - lo_x) * (W - 2 * pad)
    PY = lambda lat: H - pad - (lat - lo_y) / (hi_y - lo_y) * (H - 2 * pad)
    p = ['<svg viewBox="0 0 %d %d" class="vz-svg vz-map-svg" role="img" aria-label="the four gospel homes across the Mediterranean">' % (W, H)]
    p.append('<rect x="0" y="0" width="%d" height="%d" class="vz-sea"/>' % (W, H))
    g0 = int(lo_x) // 5 * 5
    for gl in range(g0, int(hi_x) + 6, 5):
        gx = PX(gl)
        if pad < gx < W - pad:
            p.append('<line x1="%.0f" y1="%d" x2="%.0f" y2="%d" class="vz-grat"/>' % (gx, pad, gx, H - pad))
    p.append('<text x="%d" y="%d" class="vz-map-dir" text-anchor="start">← west</text>' % (pad, H - 12))
    p.append('<text x="%d" y="%d" class="vz-map-dir" text-anchor="end">east →</text>' % (W - pad, H - 12))
    for h in pts:
        x = PX(h['lon']); y = PY(h['lat'])
        p.append('<circle cx="%.0f" cy="%.0f" r="6" class="vz-home"/>' % (x, y))
        p.append('<text x="%.0f" y="%.0f" class="vz-home-em" text-anchor="middle">%s</text>' % (x, y - 15, EMBLEM.get(h['gospel'], '')))
        p.append('<text x="%.0f" y="%.0f" class="vz-home-lab" text-anchor="middle">%s</text>' % (x, y + 21, esc(h['gospel'] + ' · ' + h['place'].split('(')[0].strip())))
    p.append('</svg>')
    uh = ''
    if unc:
        u = unc[0]
        uh = ('<div class="vz-map-unc">' + EMBLEM.get(u['gospel'], '') + ' <b>' + esc(u['gospel']) + '</b> — '
              + esc(u['place']) + ' <span class="fr-note">(' + esc(u.get('certainty', '')) + ')</span></div>')
    return '<figure class="viz-real viz-map">' + ''.join(p) + uh + '<figcaption>' + esc(v.get('provenance', '')) + '</figcaption></figure>'

def render_blocks(md):
    """Render a section body (paragraphs, lists, tables, ### subsections, [SLOT], gloss)."""
    out = []
    lines = md.split('\n')
    i = 0
    while i < len(lines):
        ln = lines[i]
        s = ln.strip()
        if not s:
            i += 1; continue
        if re.match(r'^-{3,}$', s):           # horizontal-rule separator — drop (chapters already framed)
            i += 1; continue
        # ### subsection with optional level-tag
        m = re.match(r'^###\s+(.+)$', s)
        if m:
            htxt = m.group(1)
            lvl = ''
            tm = re.search(r'\s+—\s+\*(.+?)\*\s*$', htxt)
            if tm:
                tag = tm.group(1).strip()
                lvl = level_class(tag)
                htxt = htxt[:tm.start()].strip()
                lab = f'<span class="lvl {lvl}">{esc(tag)}</span>'
            else:
                lab = ''
            aid = 'x-' + re.sub(r'[^a-z0-9]+', '-', htxt.lower()).strip('-')[:40]
            out.append(f'<h3 id="{aid}">{inline(htxt)} {lab}</h3>')
            i += 1; continue
        # [SLOT: ...] -> bind the real engine-backed viz if data present, else honest placeholder
        m = re.match(r'^\[SLOT:\s*(.+?)\]$', s)
        if m:
            low = m.group(1).lower(); viz = ''
            if 'timeline' in low and VIZ.get('timeline'): viz = viz_timeline(VIZ['timeline'])
            elif ' map' in (' ' + low) and VIZ.get('map'): viz = viz_map(VIZ['map'])
            elif 'paradigm' in low and VIZ.get('paradigm'): viz = viz_paradigm(VIZ['paradigm'])
            elif ('radar' in low or 'frame' in low) and VIZ.get('frame'): viz = viz_frame(VIZ['frame'])
            out.append(viz if viz else (f'<figure class="viz-slot"><span class="vs-mark">◈</span>'
                       f'<figcaption>{inline(m.group(1))}</figcaption></figure>'))
            i += 1; continue
        # table
        if s.startswith('|'):
            tbl = []
            while i < len(lines) and lines[i].strip().startswith('|'):
                tbl.append(lines[i].strip()); i += 1
            rows = [[c.strip() for c in r.strip('|').split('|')] for r in tbl]
            rows = [r for r in rows if not all(re.match(r'^:?-+:?$', c or '-') for c in r)]  # drop --- sep
            thtml = '<div class="tbl-wrap"><table class="fg-tbl">'
            if rows:
                thtml += '<thead><tr>' + ''.join(f'<th>{inline(c)}</th>' for c in rows[0]) + '</tr></thead>'
                thtml += '<tbody>' + ''.join('<tr>' + ''.join(f'<td>{inline(c)}</td>' for c in r) + '</tr>'
                                             for r in rows[1:]) + '</tbody>'
            out.append(thtml + '</table></div>'); continue
        # bulleted list (bullets may wrap across lines)
        if s.startswith('- '):
            items = []
            while i < len(lines):
                cur = lines[i]
                if cur.strip().startswith('- '):
                    items.append(cur.strip()[2:]); i += 1
                elif cur.strip() and not cur.strip().startswith(('- ', '#', '|', '[SLOT')) and cur.startswith((' ', '\t')):
                    items[-1] += ' ' + cur.strip(); i += 1          # continuation line
                else:
                    break
            out.append('<ul>' + ''.join(f'<li>{inline(it)}</li>' for it in items) + '</ul>')
            continue
        # "In this chapter:" mini-nav line -> styled
        if s.startswith('**In this chapter:**'):
            out.append(f'<p class="in-chapter">{inline(s)}</p>'); i += 1; continue
        # paragraph (gather until blank)
        para = [s]; i += 1
        while i < len(lines) and lines[i].strip() and not re.match(r'^(###|\||\[SLOT|-\s|##)', lines[i].strip()):
            para.append(lines[i].strip()); i += 1
        out.append(f'<p>{inline(" ".join(para))}</p>')
    return '\n'.join(out)

# ── classify sections ──
preface = frontis = provenance = None
chapters = []   # (num, name, gloss, body)
for head, content in sections:
    if head.startswith('How to read this'):
        preface = content
    elif head.startswith('Frontispiece'):
        frontis = ('Frontispiece', head.split('—', 1)[1].strip() if '—' in head else '', content)
    elif head.startswith('Where did this come from'):
        provenance = content
    else:
        cm = re.match(r'Chapter\s+(\d+)\s*·\s*(.+?)\s+—\s+(.+)$', head)
        if cm:
            num, name, gloss = cm.group(1), cm.group(2).strip(), cm.group(3).strip()
            # pull the leading *italic gloss* line if present (secondary gloss under the ##)
            chapters.append((num, name, gloss, content))

ROMAN = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV'}

# ── build the reading column ──
read_html = []
# Frontispiece card
if frontis:
    read_html.append('<section id="frontispiece" class="frontis"><div class="ch-strip"><span class="ch-num">✦</span>'
                     f'<div><h2>{inline(frontis[0])}</h2><p class="ch-gloss">{inline(frontis[1])}</p></div></div>'
                     f'{render_blocks(frontis[2])}</section>')
# Chapters
TOC = [('frontispiece', 'Frontispiece')]
for num, name, gloss, content in chapters:
    aid = f'ch-{name.lower()}'
    TOC.append((aid, f'{ROMAN.get(num, num)} · {name}'))
    # strip a leading *gloss* paragraph (already captured as `gloss` from the heading)
    body_md = content
    read_html.append(
        f'<section id="{aid}" class="chapter"><div class="ch-strip"><span class="ch-num">{ROMAN.get(num, num)}</span>'
        f'<div><h2>{inline(name)}</h2><p class="ch-gloss">{inline(gloss)}</p></div></div>'
        f'{render_blocks(body_md)}</section>')
# read-deeper
read_html.append('''<section id="read-deeper" class="read-deeper">
  <div class="ch-strip"><span class="ch-num">→</span><div><h2>Read deeper</h2>
  <p class="ch-gloss">The coded outputs this situating opens onto.</p></div></div>
  <div class="deeper-grid">
    <a href="resurrection.html">The braided reading <span>— the four resurrection accounts, move by move</span></a>
    <a href="spine.html">The convergence map <span>— where the four braid and part</span></a>
    <a href="reception.html">Reception <span>— how the end-silence was received</span></a>
    <a href="fan.html">The fan <span>— Mark's abrupt ending and its alternative worlds</span></a>
  </div>
</section>''')
# provenance closing band
if provenance:
    TOC.append(('provenance', 'Where did this come from'))
    read_html.append(f'<section id="provenance" class="provenance"><div class="ch-strip"><span class="ch-num">❧</span>'
                     f'<div><h2>Where did this come from</h2><p class="ch-gloss">The process, the coded data, and the sources behind everything above.</p></div></div>'
                     f'{render_blocks(provenance)}</section>')

toc_html = ''.join(f'<li><a href="#{aid}" data-sec="{aid}">{esc(lab)}</a></li>' for aid, lab in TOC)

PAGE = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(TITLE)} · a field guide</title>
<meta name="robots" content="noindex,nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=EB+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Lora:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
:root{{
  --paper:#f6f4ec; --ink:#1c2b1e; --ink-soft:#2f4532; --ink-mute:#5a6a54; --rule:#c2ccb8;
  --accent:#8a2a2a; --accent-soft:#5a1a1a; --marker:#c4a484; --card:#e6ebdd;
  --serif:"EB Garamond",Georgia,serif; --sans:"Lora",Georgia,serif; --mono:"JetBrains Mono",ui-monospace,monospace;
  --lv-whole:#5a6a54; --lv-each:#8a2a2a; --lv-braid:#6a5a2a;
}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{
  --paper:#181c17; --ink:#e7ebde; --ink-soft:#cdd6c4; --ink-mute:#94a08c; --rule:#33402f;
  --accent:#d98a6a; --accent-soft:#e0a084; --marker:#6a5a3a; --card:#20261c;
  --lv-whole:#94a08c; --lv-each:#d98a6a; --lv-braid:#c2a86a;
}}}}
*{{box-sizing:border-box}}
html{{scroll-behavior:smooth}}@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:var(--serif);font-size:18px;line-height:1.7;
  -webkit-font-smoothing:antialiased;font-feature-settings:"ss01","ss02","cv11";
  background-image:radial-gradient(circle at 1px 1px, rgba(90,106,84,.06) 1px, transparent 0);background-size:22px 22px;}}
::selection{{background:var(--marker);color:var(--ink)}}
a{{color:var(--accent);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}}
.bar{{position:sticky;top:0;z-index:30;display:flex;justify-content:space-between;align-items:center;gap:12px;
  padding:10px 20px;background:color-mix(in srgb,var(--paper) 92%,transparent);backdrop-filter:blur(6px);border-bottom:1px solid var(--rule)}}
.bar a{{font-family:var(--sans);font-size:13px;color:var(--accent);text-decoration:none;border-bottom:1px solid color-mix(in srgb,var(--accent) 35%,transparent)}}
.bar .rm{{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-mute)}}
/* header / frontispiece */
header.pg{{max-width:52rem;margin:0 auto;padding:8vh 24px 2vh;text-align:center}}
.kick{{font-family:var(--mono);font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:var(--ink-mute);margin:0 0 14px}}
h1.title{{font-family:var(--serif);font-weight:500;font-size:clamp(34px,6vw,58px);line-height:1.04;letter-spacing:-.02em;color:var(--ink);margin:0 0 10px;font-variation-settings:"opsz" 144}}
.subtitle{{font-family:var(--serif);font-style:italic;font-size:19px;color:var(--ink-mute);max-width:34rem;margin:0 auto}}
.orn{{color:var(--accent);font-size:22px;margin:16px 0 0;letter-spacing:.4em}}
/* preface */
.preface{{max-width:44rem;margin:2vh auto 0;padding:0 24px}}
.preface .pf-card{{background:var(--card);border:1px solid var(--rule);border-radius:4px;padding:22px 26px}}
.preface .pf-h{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--accent);margin:0 0 10px}}
.preface p{{margin:.7rem 0}}
/* layout: reading + sticky rail */
.layout{{display:grid;grid-template-columns:1fr 15rem;gap:clamp(24px,4vw,64px);max-width:66rem;margin:5vh auto 0;padding:0 24px 16vh;align-items:start}}
@media(max-width:820px){{.layout{{grid-template-columns:1fr}} .rail{{display:none}}}}
.reading{{min-width:0;max-width:44rem}}
.rail{{position:sticky;top:70px;font-family:var(--sans);font-size:13px}}
.rail .rh{{font-family:var(--mono);font-size:10px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-mute);margin:0 0 12px}}
.rail ul{{list-style:none;margin:0;padding:0;border-left:1px solid var(--rule)}}
.rail li a{{display:block;padding:5px 0 5px 14px;margin-left:-1px;color:var(--ink-mute);text-decoration:none;border-left:2px solid transparent;line-height:1.35}}
.rail li a:hover{{color:var(--ink)}}
.rail li a.on{{color:var(--accent);border-left-color:var(--accent);font-weight:500}}
/* chapter title strips */
.ch-strip{{display:flex;align-items:baseline;gap:16px;margin:0 0 8px;padding-top:8px;border-top:1px solid var(--rule)}}
.ch-strip .ch-num{{font-family:var(--serif);font-size:30px;color:var(--accent);line-height:1;flex:0 0 auto;font-style:italic}}
.ch-strip h2{{font-family:var(--serif);font-weight:500;font-size:29px;line-height:1.1;letter-spacing:-.01em;color:var(--ink);margin:0}}
.ch-gloss{{font-family:var(--serif);font-style:italic;font-size:16px;color:var(--ink-mute);margin:3px 0 0;line-height:1.4}}
section.chapter,section.frontis,section.read-deeper,section.provenance{{margin-top:3.5rem;scroll-margin-top:70px}}
section.frontis{{margin-top:2.5rem}}
/* prose */
.reading h3{{font-family:var(--serif);font-weight:600;font-size:20px;line-height:1.3;margin:2.2rem 0 .5rem;scroll-margin-top:70px;color:var(--ink);display:flex;flex-wrap:wrap;align-items:baseline;gap:10px}}
.reading p{{margin:.85rem 0}}
.reading p:first-of-type::first-letter{{}}
.reading strong{{color:var(--ink);font-weight:600}}
.reading ul{{margin:.8rem 0;padding-left:1.3rem}} .reading li{{margin:.35rem 0}}
.in-chapter{{font-family:var(--sans);font-size:14px;color:var(--ink-mute);background:color-mix(in srgb,var(--card) 60%,transparent);border-left:2px solid var(--rule);padding:8px 14px;border-radius:0 4px 4px 0}}
.lvl{{font-family:var(--mono);font-size:9px;letter-spacing:.08em;text-transform:uppercase;padding:2px 7px;border-radius:3px;font-weight:500;white-space:nowrap;
  color:#fff;background:var(--ink-mute)}}
.lvl.lv-whole{{background:var(--lv-whole)}} .lvl.lv-each{{background:var(--lv-each)}} .lvl.lv-braid{{background:var(--lv-braid)}}
/* tables */
.tbl-wrap{{overflow-x:auto;margin:1.2rem 0}}
.fg-tbl{{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:14px;line-height:1.5}}
.fg-tbl th{{text-align:left;font-family:var(--mono);font-size:10px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-mute);border-bottom:1.5px solid var(--rule);padding:7px 10px;vertical-align:bottom}}
.fg-tbl td{{border-bottom:1px solid var(--rule);padding:9px 10px;vertical-align:top;color:var(--ink-soft)}}
.fg-tbl tr:last-child td{{border-bottom:none}}
/* viz slot placeholder */
.viz-slot{{margin:1.6rem 0;padding:20px 22px;border:1px dashed color-mix(in srgb,var(--accent) 40%,var(--rule));border-radius:4px;background:color-mix(in srgb,var(--card) 50%,transparent);display:flex;gap:12px;align-items:flex-start}}
.viz-slot .vs-mark{{color:var(--accent);font-size:16px;flex:0 0 auto;line-height:1.4}}
.viz-slot figcaption{{font-family:var(--sans);font-style:italic;font-size:14px;color:var(--ink-mute);line-height:1.5}}
/* real (engine-backed) viz */
.viz-real{{margin:1.8rem 0}}
.viz-real .vz-svg{{width:100%;height:auto;display:block}}
.viz-real figcaption{{font-family:var(--mono);font-size:9.5px;letter-spacing:.02em;color:var(--ink-mute);margin-top:8px;line-height:1.5}}
.vz-axis{{stroke:var(--ink-mute);stroke-width:1.4}}
.vz-hinge{{stroke:var(--accent);stroke-width:1;stroke-dasharray:3 4;opacity:.7}}
.vz-hinge-lab{{font-family:var(--mono);font-size:9px;letter-spacing:.06em;text-transform:uppercase;fill:var(--accent)}}
.vz-conn{{stroke:var(--rule);stroke-width:1}}
.vz-dot{{fill:var(--ink-mute)}} .vz-dot.vz-gospel{{fill:var(--accent)}}
.vz-yr{{font-family:var(--mono);font-size:10px;fill:var(--ink-mute)}}
.vz-ev-lab{{font-family:var(--sans);font-size:11px;fill:var(--ink-soft)}}
.vz-ev-lab.vz-gospel-lab{{fill:var(--accent);font-weight:600}}
.vz-map-svg{{border:1px solid var(--rule);border-radius:4px}}
.vz-sea{{fill:color-mix(in srgb,#7fa8b8 15%,var(--paper))}}
.vz-grat{{stroke:var(--rule);stroke-width:.6;opacity:.5}}
.vz-map-dir{{font-family:var(--mono);font-size:10px;fill:var(--ink-mute)}}
.vz-home{{fill:var(--accent);stroke:var(--paper);stroke-width:1.5}}
.vz-home-em{{font-size:16px}}
.vz-home-lab{{font-family:var(--sans);font-size:12px;fill:var(--ink-soft);font-weight:500}}
.vz-map-unc{{font-family:var(--sans);font-size:13px;color:var(--ink-mute);margin-top:10px;padding:8px 12px;border:1px dashed var(--rule);border-radius:4px;background:color-mix(in srgb,var(--card) 50%,transparent)}}
.pdg-shared{{font-family:var(--serif);font-size:16px;color:var(--ink-soft);margin-bottom:14px;line-height:1.5}}
.pdg-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px}}
@media(max-width:560px){{.pdg-grid{{grid-template-columns:1fr}}}}
.pdg-card{{border:1px solid var(--rule);border-radius:4px;background:var(--card);padding:14px 16px}}
.pdg-emblem{{font-size:22px;line-height:1}}
.pdg-g{{font-family:var(--serif);font-weight:600;font-size:18px;color:var(--ink);margin:4px 0 2px}}
.pdg-dom{{font-family:var(--serif);font-style:italic;font-size:14px;color:var(--accent);line-height:1.35}}
.pdg-sec{{list-style:none;margin:8px 0 0;padding:0}}
.pdg-sec li{{font-family:var(--sans);font-size:12.5px;color:var(--ink-mute);padding:2px 0 2px 12px;position:relative}}
.pdg-sec li::before{{content:"·";position:absolute;left:2px;color:var(--accent)}}
.viz-frame{{border:1px solid var(--rule);border-radius:4px;padding:16px 18px;background:color-mix(in srgb,var(--card) 40%,transparent)}}
.fr-legend{{font-family:var(--sans);font-size:12px;color:var(--ink-mute);margin-bottom:12px}}
.fr-row{{display:grid;grid-template-columns:11rem 1fr;gap:12px;align-items:baseline;padding:7px 0;border-top:1px solid var(--rule)}}
.fr-row:first-of-type{{border-top:none}}
.fr-ax{{font-family:var(--mono);font-size:11px;color:var(--ink-soft)}}
.fr-val{{display:flex;flex-wrap:wrap;gap:6px;align-items:baseline}}
.fr-chip{{font-family:var(--sans);font-size:12px;padding:2px 9px;border-radius:3px;white-space:nowrap}}
.fr-chip.shared{{background:color-mix(in srgb,var(--lv-whole) 22%,transparent);color:var(--ink-soft);border:1px solid color-mix(in srgb,var(--lv-whole) 45%,transparent)}}
.fr-chip.div{{background:color-mix(in srgb,var(--accent) 12%,transparent);color:var(--accent-soft);border:1px solid color-mix(in srgb,var(--accent) 30%,transparent)}}
.fr-chip.div b{{color:var(--accent);font-weight:600}}
.fr-note{{font-family:var(--sans);font-size:11px;color:var(--ink-mute);font-style:italic}}
@media(max-width:560px){{.fr-row{{grid-template-columns:1fr}}}}
/* read-deeper */
.deeper-grid{{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:1.2rem}}
@media(max-width:560px){{.deeper-grid{{grid-template-columns:1fr}}}}
.deeper-grid a{{display:block;font-family:var(--sans);text-decoration:none;border:1px solid var(--rule);border-radius:4px;padding:12px 15px;background:var(--card);color:var(--accent);font-weight:600;font-size:15px;transition:border-color .15s}}
.deeper-grid a:hover{{border-color:var(--accent)}}
.deeper-grid a span{{display:block;font-family:var(--serif);font-weight:400;font-style:italic;color:var(--ink-mute);font-size:13.5px;margin-top:2px}}
/* provenance band */
.provenance{{background:var(--card);border:1px solid var(--rule);border-radius:4px;padding:24px 28px;margin-top:4rem}}
.provenance .fg-tbl,.provenance p{{font-size:16px}}
footer.foot{{max-width:52rem;margin:0 auto;padding:0 24px 12vh;font-family:var(--sans);font-size:12px;line-height:1.6;color:var(--ink-mute);text-align:center;border-top:1px solid var(--rule);padding-top:18px}}
footer.foot a{{color:var(--accent)}}
</style>
<script>(function(){{try{{var t=localStorage.getItem("gom-theme");if(t)document.documentElement.dataset.theme=t;}}catch(e){{}}}})();</script>
</head>
<body>
<div class="bar">
  <a href="index.html#toc">&larr; the contents</a>
  <span class="rm">Situate · a field guide to the four gospels</span>
  <a href="resurrection.html">the braided reading &rarr;</a>
</div>
<header class="pg">
  <p class="kick">The reading room · Situate</p>
  <h1 class="title">{inline(TITLE)}</h1>
  <p class="subtitle">{inline(SUBTITLE)}</p>
  <p class="orn">❧ ❈ ❧</p>
</header>
<div class="preface">
  <div class="pf-card"><p class="pf-h">How to read this</p>{render_blocks(preface) if preface else ''}</div>
</div>
<div class="layout">
  <main class="reading">
    {''.join(read_html)}
  </main>
  <nav class="rail" aria-label="In this page">
    <p class="rh">In this page</p>
    <ul>{toc_html}</ul>
  </nav>
</div>
<footer class="foot">
  A field guide, produced with the instrument &mdash; every factual claim traces to a named source; every reading is marked as the instrument&rsquo;s own. See <a href="#provenance">Where did this come from</a>. &nbsp;·&nbsp; <a href="index.html">the door</a>
</footer>
<script>
// scroll-spy: highlight the rail entry for the section currently in view
(function(){{
  var links=[].slice.call(document.querySelectorAll('.rail a[data-sec]'));
  var secs=links.map(function(a){{return document.getElementById(a.getAttribute('data-sec'));}}).filter(Boolean);
  function onScroll(){{
    var y=window.scrollY+120, cur=secs[0];
    secs.forEach(function(s){{ if(s.offsetTop<=y) cur=s; }});
    links.forEach(function(a){{ a.classList.toggle('on', a.getAttribute('data-sec')===(cur&&cur.id)); }});
  }}
  window.addEventListener('scroll',onScroll,{{passive:true}}); onScroll();
}})();
</script>
</body>
</html>'''

open(OUT, 'w', encoding='utf-8').write(PAGE)
print(f'wrote {OUT}  ({len(PAGE)} bytes)  · chapters:', [c[1] for c in chapters],
      '· TOC:', [t[1] for t in TOC])
