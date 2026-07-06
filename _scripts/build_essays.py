#!/usr/bin/env python3
"""
build_essays.py — mirror the Grammar of Meaning Substack (the FINAL/published source
of truth) into owned, house-styled, SEO'd reader pages on grammarofmeaning.org.

Write-once flow: Tamara publishes on Substack; this reads the RSS full-text feed and
regenerates the on-site essay pages + index + sitemap. She never touches the site.

Source of truth = Substack (NOT the repo drafts, which carry [[verify]] markers).

Usage:  python3 _scripts/build_essays.py [--out DIR] [--base URL]
Default: writes staging pages to _staging/essays/ ; pass --out essays for production.
"""
import argparse, os, re, sys, html, json, datetime, urllib.request
from io import BytesIO
import feedparser
from bs4 import BeautifulSoup
try:
    from PIL import Image
    HAVE_PIL = True
except Exception:
    HAVE_PIL = False

FEED = "https://grammarofmeaning.substack.com/feed"
BASE = "https://grammarofmeaning.org"

# house palette (from gom.css) — the border snaps to the nearest of these
PALETTE = {"moss": (44, 74, 56), "fern": (63, 125, 87), "sage": (138, 168, 139),
           "olive": (110, 123, 58), "gold": (201, 162, 39), "honey": (224, 169, 59),
           "terra": (196, 96, 47), "slate": (91, 124, 147)}

# series map — RSS doesn't expose "part N of a series", so it's maintained here.
SERIES = {
    "What's Worth Wanting": {
        "intro": "whats-worth-wanting",
        "parts": ["the-man-who-threw-away-his-cup", "the-useless-tree",
                  "the-woman-who-set-fire-to-heaven", "the-length-of-a-road"],
    },
}
def series_of(slug):
    for name, s in SERIES.items():
        if slug == s["intro"]:
            return {"name": name, "role": "intro", "intro": s["intro"], "parts": s["parts"], "total": len(s["parts"])}
        if slug in s["parts"]:
            return {"name": name, "role": "part", "intro": s["intro"], "parts": s["parts"],
                    "n": s["parts"].index(slug) + 1, "total": len(s["parts"])}
    return None

# ---- cross-linking (The Marginalian's "Complement with…", HAND-CURATED) ----
# Tamara names the connections. Format: slug -> [(related_slug, "why they resonate"), ...].
# STARTER set (renunciation / letting-go) with descriptive glosses — edit into your own voice + extend.
RELATIONS = {
    "the-length-of-a-road": [
        ("the-man-who-threw-away-his-cup", "Diogenes, who also found freedom by giving things up"),
        ("the-woman-who-set-fire-to-heaven", "Rabiʿa, renouncing the reward itself, not just the property"),
    ],
    "the-man-who-threw-away-his-cup": [
        ("the-length-of-a-road", "Francis, who gave away everything — not just a cup"),
        ("the-useless-tree", "Zhuangzi on the freedom of being good-for-nothing"),
    ],
    "the-woman-who-set-fire-to-heaven": [
        ("the-length-of-a-road", "Francis, letting go of distance itself"),
    ],
    "the-useless-tree": [
        ("the-man-who-threw-away-his-cup", "Diogenes, the other great dropout"),
    ],
}

def complement_html(slug, meta):
    """The 'Complement with…' end-block — hand-picked related essays (like The Marginalian)."""
    items = []
    for rslug, gloss in RELATIONS.get(slug, []):
        m = meta.get(rslug)
        if not m:
            continue
        items.append(f'<a class="cw-item" href="/essays/{rslug}.html">'
                     f'<span class="cw-t">{esc(m["title"])}</span>'
                     f'<span class="cw-g">{esc(gloss)}</span></a>')
    if not items:
        return ""
    return ('<aside class="complement"><div class="cw-label">Complement with</div>'
            + "".join(items) + '</aside>')

def rewrite_substack_links(page, slugs):
    """Her own cross-links written on Substack point at substack.com/p/<slug>; rewrite them to the
    on-site /essays/<slug>.html so readers stay on the site (only for essays we actually mirror)."""
    def repl(m):
        s = m.group(1)
        return f'href="/essays/{s}.html"' if s in slugs else m.group(0)
    return re.sub(r'href="https?://grammarofmeaning\.substack\.com/p/([a-z0-9][a-z0-9-]*)[^"]*"', repl, page)

# ---- tags / subjects (Substack drops them from RSS; scrape the post page's _preloads JSON) ----
def fetch_tags(url):
    """Returns [(name, slug), ...] of the post's non-hidden tags. Robust: [] on any failure."""
    if not url:
        return []
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        page = urllib.request.urlopen(req, timeout=25).read().decode("utf-8", "replace")
        m = re.search(r'\\"postTags\\":\s*(\[.*?\])', page)
        if not m:
            return []
        arr = json.loads(m.group(1).replace('\\"', '"'))
        return [(t["name"], t["slug"]) for t in arr if not t.get("hidden") and t.get("name") and t.get("slug")]
    except Exception:
        return []

def tag_chips_html(slug, TAGS, SHARED):
    """Reader-page chips — only the SHARED subjects (tags on >=2 essays), which link to a subject page."""
    chips = [f'<a class="tag" href="/essays/topic/{ts}.html">{esc(name)}</a>'
             for name, ts in TAGS.get(slug, []) if ts in SHARED]
    if not chips:
        return ""
    return '<div class="tags"><span class="tags-label">Subjects</span>' + "".join(chips) + '</div>'

def slug_of(link):
    return link.rstrip("/").split("/")[-1]

def image_meta(url):
    """Returns (border_hex, orientation): dominant color snapped to the house palette + landscape/portrait/square."""
    if not (url and HAVE_PIL):
        return "#8AA88B", "portrait"
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        data = urllib.request.urlopen(req, timeout=18).read()
        src = Image.open(BytesIO(data)).convert("RGB")
        w, h = src.size
        orient = "landscape" if w > h * 1.15 else ("portrait" if h > w * 1.15 else "square")
        im = src.resize((64, 64))
        q = im.quantize(colors=6).convert("RGB")
        counts = sorted(q.getcolors(64 * 64) or [], reverse=True)  # [(count,(r,g,b))]
        cands = [c for _, c in counts[:6]] or [(138, 168, 139)]
        def sat(c):
            mx, mn = max(c), min(c)
            return (mx - mn) / (mx + 1)
        def midness(c):  # prefer not-too-dark / not-too-light
            return 1 - abs(sum(c) / 3 - 128) / 128
        dom = max(cands, key=lambda c: sat(c) * 0.7 + midness(c) * 0.3)
        def dist(a, b):
            return sum((x - y) ** 2 for x, y in zip(a, b))
        name = min(PALETTE, key=lambda k: dist(dom, PALETTE[k]))
        r, g, b = PALETTE[name]
        return "#%02X%02X%02X" % (r, g, b), orient
    except Exception:
        return "#8AA88B", "portrait"

def clean_body(raw):
    """Sanitize Substack content:encoded -> clean house HTML. Returns (body_html, hero_src, hero_cap)."""
    soup = BeautifulSoup(raw, "html.parser")
    # (1) strip Substack subscribe CTAs + interactive cruft (restack/share/expand buttons, inline svgs)
    for t in soup.select('[class*="subscription-widget"], [class*="subscribe"], [class*="button-wrapper"], [data-component-name]'):
        t.decompose()
    for t in soup.find_all(["button", "svg"]):
        t.decompose()
    for t in soup.select('[class*="image-link-expand"]'):
        t.decompose()
    # (4) neutralize footnote links (they error on our page) -> plain superscripts + clean numbers
    for a in soup.select("a.footnote-anchor"):
        sup = soup.new_tag("sup"); sup["class"] = "fn-ref"; sup.string = a.get_text(); a.replace_with(sup)
    for a in soup.select("a.footnote-number"):
        sp = soup.new_tag("span"); sp["class"] = "fn-num"; sp.string = a.get_text(); a.replace_with(sp)
    # normalize captioned images -> clean <figure>; pull the first as the hero (shown as the header thumbnail)
    hero_src, hero_cap = None, None
    for i, cont in enumerate(soup.find_all(class_="captioned-image-container")):
        img = cont.find("img")
        src = img.get("src") if img else None
        cap_el = cont.find("figcaption")
        cap = cap_el.get_text(" ", strip=True) if cap_el else ""
        if i == 0 and src:
            hero_src, hero_cap = src, cap
            cont.decompose()
            continue
        if src:
            fig = soup.new_tag("figure")
            ni = soup.new_tag("img", src=src, alt=(img.get("alt") or ""))
            fig.append(ni)
            if cap:
                fc = soup.new_tag("figcaption"); fc.string = cap; fig.append(fc)
            cont.replace_with(fig)
        else:
            cont.decompose()
    # tidy leftover empties
    for t in soup.find_all(["span", "div"]):
        if not t.get_text(strip=True) and not t.find("img"):
            (t.unwrap() if t.name == "span" else t.decompose())
    if not hero_src:
        im = soup.find("img")
        if im:
            hero_src = im.get("src")
            fp = im.find_parent("figure")
            if fp: fp.decompose()
    return str(soup), hero_src, hero_cap

def esc(s):
    return html.escape(html.unescape(s or ""), quote=True)

def inject_region(path, start, end, content):
    """Idempotently replace text between two marker comments in a hand-authored page."""
    if not os.path.exists(path):
        return False
    txt = open(path).read()
    if start not in txt or end not in txt:
        return False
    pre = txt.split(start)[0]
    post = txt.split(end, 1)[1]
    open(path, "w").write(pre + start + "\n" + content + "\n" + end + post)
    return True

def render_essay(e):
    title = e.get("title", "").strip()
    deck = re.sub(r"\s+", " ", (e.get("summary") or "")).strip()
    link = e.get("link"); slug = slug_of(link)
    pp = e.get("published_parsed")
    dt = datetime.date(*pp[:3]) if pp else datetime.date.today()
    date_h = dt.strftime("%B %-d, %Y"); date_iso = dt.strftime("%Y-%m-%d")
    raw = e.content[0].value if e.get("content") else (e.get("summary") or "")
    body, hero, hero_cap = clean_body(raw)
    url = f"{BASE}/essays/{slug}"
    hero_meta = hero or f"{BASE}/favicon.svg"
    border, orient = image_meta(hero)
    is_land = bool(hero) and orient == "landscape"
    # portrait/square -> left thumbnail in the header; landscape -> full-width framed figure below the header
    thumb = "" if is_land else ((f'<div class="e-thumb-wrap"><span class="e-thumb-frame" style="border-color:{border}">'
             f'<img class="e-thumb {orient}" src="{esc(hero)}" alt="{esc(title)}"></span></div>') if hero else "")
    if is_land:
        post_head = (f'<figure class="e-hero-fig"><span class="e-hero-frame" style="border-color:{border}">'
                     f'<img src="{esc(hero)}" alt="{esc(title)}"></span>'
                     + (f'<figcaption>{esc(hero_cap)}</figcaption>' if hero_cap else "") + '</figure>')
    else:
        post_head = f'<div class="e-cap">{esc(hero_cap)}</div>' if hero_cap else ""
    si = series_of(slug)
    if si and si["role"] == "part":
        kicker = f'<a href="/essays/{si["intro"]}.html">{esc(si["name"])}</a> · Day {si["n"]} of {si["total"]}'
    elif si and si["role"] == "intro":
        kicker = f'A {si["total"]}-part series · Grammar of Meaning'
    else:
        kicker = "Essay · Grammar of Meaning"
    series_nav = ""
    if si:
        items = [f'<a href="/essays/{si["intro"]}.html" class="sn-item{" sn-cur" if slug==si["intro"] else ""}">Intro</a>']
        for i, ps in enumerate(si["parts"], 1):
            items.append(f'<a href="/essays/{ps}.html" class="sn-item{" sn-cur" if slug==ps else ""}">Day {i}</a>')
        series_nav = (f'<div class="series-nav"><div class="sn-label">{esc(si["name"])} — a {si["total"]}-part series</div>'
                      f'<div class="sn-row">{"".join(items)}</div></div>')
    page = PAGE.format(title=esc(title), deck=esc(deck), url=url, hero=esc(hero_meta),
                       date_iso=date_iso, date_h=esc(date_h), body=body, thumb=thumb,
                       kicker=kicker, post_head=post_head, series_nav=series_nav)
    return slug, url, title, deck, date_iso, date_h, hero_meta, page

PAGE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Grammar of Meaning</title>
<meta name="description" content="{deck}">
<link rel="canonical" href="{url}">
<link rel="author" href="/about.html">
<meta property="og:type" content="article"><meta property="og:site_name" content="Grammar of Meaning">
<meta property="og:title" content="{title}"><meta property="og:description" content="{deck}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{hero}">
<meta property="article:published_time" content="{date_iso}"><meta property="article:author" content="Tamara Sanderson">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{deck}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","@id":"{url}","headline":"{title}","description":"{deck}","author":{{"@type":"Person","name":"Tamara Sanderson","url":"/about.html"}},"publisher":{{"@type":"Organization","name":"Grammar of Meaning","url":"/"}},"datePublished":"{date_iso}","mainEntityOfPage":"{url}","isPartOf":{{"@type":"CreativeWorkSeries","name":"Essays from the Archive"}},"image":"{hero}"}}
</script>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/gom.css">
<style>
 .wrap{{max-width:1080px}} .essay-wrap{{max-width:680px;margin:0 auto;padding-bottom:56px}}
 .backlink{{font-family:var(--mono);font-size:12px;color:var(--ink-2);text-decoration:none;display:inline-block;margin:6px 0 18px}} .backlink:hover{{color:var(--fern)}}
 .e-head{{display:flex;gap:28px;align-items:flex-start;margin:0 0 6px}}
 @media(max-width:680px){{.e-head{{flex-direction:column;gap:16px}}}}
 .e-thumb-wrap{{flex:0 0 auto}} @media(max-width:680px){{.e-thumb-wrap{{flex:none}}}}
 .e-thumb-frame{{display:inline-block;border:5px solid var(--sage);background:#C9A227;padding:1.6px;border-radius:6px;
   box-shadow:0 0 0 1px rgba(36,48,42,.10), 0 10px 26px -14px rgba(36,48,42,.4)}}
 .e-thumb{{display:block;height:auto;max-width:52vw;border-radius:3px}}
 .e-thumb.portrait{{width:178px}} .e-thumb.landscape{{width:252px}} .e-thumb.square{{width:206px}}
 .e-htext{{flex:1;min-width:0}}
 .e-kicker{{font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--olive);margin:0 0 10px}}
 .e-kicker a{{color:var(--olive);text-decoration:none;border-bottom:1px solid rgba(110,123,58,.4)}} .e-kicker a:hover{{color:var(--fern)}}
 .e-cap{{font-family:var(--sans);font-size:12px;color:var(--ink-3);font-style:italic;line-height:1.5;max-width:640px;margin:16px 0 0}}
 .e-hero-fig{{margin:26px 0 6px}}
 .e-hero-frame{{display:block;border:6px solid var(--sage);background:#C9A227;padding:2px;border-radius:8px;box-shadow:0 0 0 1px rgba(36,48,42,.10),0 12px 30px -16px rgba(36,48,42,.42)}}
 .e-hero-frame img{{display:block;width:100%;border-radius:4px}}
 .e-hero-fig figcaption{{font-family:var(--sans);font-size:12px;color:var(--ink-3);font-style:italic;line-height:1.5;margin-top:12px}}
 .series-nav{{max-width:680px;margin:34px auto 0;padding:14px 18px;border:1px solid var(--rule);border-radius:12px;background:var(--paper-3)}}
 .sn-label{{font-family:var(--mono);font-size:11px;letter-spacing:.05em;text-transform:uppercase;color:var(--olive);margin-bottom:9px}}
 .sn-row{{display:flex;gap:8px;flex-wrap:wrap}}
 .sn-item{{font-family:var(--sans);font-size:13px;text-decoration:none;color:var(--ink-2);border:1px solid var(--rule);border-radius:999px;padding:4px 13px}} .sn-item:hover{{border-color:var(--sage)}}
 .sn-cur{{background:var(--moss);color:#fff;border-color:var(--moss)}}
 .e-title{{font-family:var(--serif);font-weight:600;font-size:38px;line-height:1.13;color:var(--moss);margin:0 0 14px;letter-spacing:-.01em}}
 @media(max-width:640px){{.e-title{{font-size:30px}}}}
 .e-deck{{font-family:var(--serif);font-style:italic;font-size:19px;line-height:1.5;color:var(--ink-2);margin:0 0 18px}}
 .e-meta{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-family:var(--sans);font-size:13.5px;color:var(--ink-2);border-top:1px solid var(--rule);padding:12px 0 0;margin:2px 0 0}}
 .e-meta a{{color:var(--fern);text-decoration:none;font-weight:500}} .e-meta .sep{{color:var(--rule)}}
 .essay{{font-family:var(--serif);font-size:19.5px;line-height:1.72;color:var(--ink);margin-top:30px}}
 .essay p{{margin:0 0 24px}}
 .essay em{{font-style:italic}} .essay b,.essay strong{{font-weight:600;color:var(--moss)}}
 .essay sup.fn-ref{{font-size:.62em;color:var(--fern);font-weight:600;padding-left:1px}}
 .essay h2,.essay h3{{font-family:var(--serif);color:var(--moss);line-height:1.2;margin:34px 0 12px}} .essay h2{{font-size:26px}} .essay h3{{font-size:21px}}
 .essay blockquote{{margin:28px 0;padding:4px 0 4px 22px;border-left:3px solid var(--sage);font-style:italic;color:var(--ink-2)}}
 .essay hr{{border:none;border-top:1px solid var(--rule);margin:40px auto;width:90px}}
 .essay figure{{margin:28px 0}} .essay figure img{{width:100%;border-radius:10px;border:1px solid var(--rule)}} .essay figcaption{{font-family:var(--sans);font-size:12px;color:var(--ink-3);text-align:center;margin-top:8px;font-style:italic}}
 .essay a{{color:var(--fern)}} .essay ol,.essay ul{{padding-left:24px}} .essay li{{margin:0 0 10px}}
 /* footnotes (Substack .footnote blocks), de-linked + spaced */
 .essay .footnote{{display:flex;gap:12px;align-items:baseline;margin:0 0 16px;font-family:var(--sans);font-size:14.5px;line-height:1.6;color:var(--ink-2)}}
 .essay .fn-num{{flex:0 0 auto;font-family:var(--mono);font-size:12px;font-weight:600;color:var(--olive);min-width:16px}}
 .essay .footnote-content{{flex:1;min-width:0}} .essay .footnote-content p{{margin:0 0 8px}} .essay .footnote-content em{{color:var(--ink)}}
 .complement{{max-width:680px;margin:40px auto 0;padding:20px 24px;border:1px solid var(--rule);border-radius:12px;background:var(--paper-3)}}
 .cw-label{{font-family:var(--mono);font-size:11px;letter-spacing:.08em;text-transform:uppercase;color:var(--olive);margin-bottom:12px}}
 .cw-item{{display:block;text-decoration:none;padding:10px 0;border-top:1px solid var(--rule)}} .cw-item:first-of-type{{border-top:none;padding-top:0}}
 .cw-t{{display:block;font-family:var(--serif);font-size:17px;font-weight:600;color:var(--moss);line-height:1.25}} .cw-item:hover .cw-t{{color:var(--fern)}}
 .cw-g{{display:block;font-family:var(--serif);font-style:italic;font-size:14px;color:var(--ink-2);margin-top:2px;line-height:1.45}}
 .tags{{max-width:680px;margin:32px auto 0;display:flex;flex-wrap:wrap;align-items:center;gap:8px}}
 .tags-label{{font-family:var(--mono);font-size:10.5px;letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);margin-right:2px}}
 .tag{{font-family:var(--sans);font-size:12.5px;color:var(--fern);text-decoration:none;background:var(--paper-3);border:1px solid var(--rule);border-radius:999px;padding:4px 12px}} .tag:hover{{border-color:var(--fern)}}
 .also{{max-width:680px;margin:36px auto 0;padding:16px 20px;border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}}
 .also .t{{font-family:var(--sans);font-size:13.5px;color:var(--ink-2)}} .also a{{font-family:var(--sans);font-size:13.5px;font-weight:600;color:var(--fern);text-decoration:none;white-space:nowrap}}
 .byline-foot{{max-width:680px;margin:28px auto 0;font-family:var(--sans);font-size:13px;color:var(--ink-3);border-top:1px solid var(--rule);padding-top:16px;line-height:1.6}} .byline-foot a{{color:var(--fern);text-decoration:none}}
</style></head><body>
<div class="topbar"><div class="wrap">
 <a class="brandmark" href="/index.html" style="color:var(--moss)"><svg class="mark" viewBox="0 0 200 200" fill="none" aria-hidden="true"><path d="M100 30 C74 52 58 92 62 126 C64 152 82 168 100 176 L100 30 Z" fill="#2C4A38"/><path d="M100 30 C126 52 142 92 138 126 C136 152 118 168 100 176 L100 30 Z" fill="#8AA88B"/><line x1="100" y1="34" x2="100" y2="174" stroke="#FCFBF7" stroke-width="3"/><line x1="100" y1="176" x2="100" y2="194" stroke="#2C4A38" stroke-width="11" stroke-linecap="round"/></svg> Grammar&nbsp;of&nbsp;Meaning</a>
 <nav class="nav"><a href="/index.html">Home</a><a href="/about.html">About</a><a href="/library.html">Library</a><a href="/essays.html" class="active">Essays</a><a href="/garden.html">Garden</a><a href="/method.html">Method</a><a href="/reference.html">Reference</a><a href="https://grammarofmeaning.substack.com/" target="_blank" rel="noopener" class="nav-out">Substack&nbsp;&#8599;</a></nav>
</div></div>
<div class="wrap"><article class="essay-wrap">
 <a class="backlink" href="/essays.html">&#8592; The Essays</a>
 <div class="e-head">
   {thumb}
   <div class="e-htext">
     <div class="e-kicker">{kicker}</div>
     <h1 class="e-title">{title}</h1>
     <p class="e-deck">{deck}</p>
     <div class="e-meta"><span>By <a href="/about.html">Tamara Sanderson</a></span><span class="sep">·</span><span>{date_h}</span><span class="sep">·</span><span>Essays from the Archive</span></div>
   </div>
 </div>
 {post_head}
 <div class="essay">{body}</div>
 {series_nav}
 <!--TAGS-->
 <!--COMPLEMENT-->
 <div class="also"><span class="t">Get new essays by email as they're published.</span><a href="https://grammarofmeaning.substack.com/subscribe" target="_blank" rel="noopener">Subscribe &#8599;</a></div>
 <div class="byline-foot"><b>Tamara Sanderson</b> writes <em>Field Notes on how meaning gets made</em> — reading one life, image, or word at a time. <a href="/about.html">About the project &#8594;</a></div>
</article></div>
<footer><div class="wrap"><div class="flabel">Grammar of Meaning</div><h3>How meaning gets made — read each tradition in its own vocabulary first.</h3><p class="foot-note"><em>Grammar of Meaning</em> · Tamara Sanderson · 2026</p></div></footer>
</body></html>"""

INDEX = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Essays — meaning-making in public · Grammar of Meaning</title>
<meta name="description" content="Field notes on how meaning gets made — reading one life, image, or word at a time.">
<link rel="canonical" href="https://grammarofmeaning.org/essays/">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/gom.css">
<style>
 .wrap{{max-width:920px}}
 .ecard{{display:flex;gap:20px;align-items:center;text-decoration:none;border:1px solid var(--rule);border-radius:14px;padding:18px 20px;margin-bottom:14px;background:var(--paper-3);transition:border-color .15s}}
 .ecard:hover{{border-color:var(--sage)}}
 .ecard img{{flex:0 0 92px;width:92px;height:92px;object-fit:cover;border-radius:8px;border:3px solid var(--sage)}}
 @media(max-width:560px){{.ecard img{{display:none}}}}
 .ec-body{{flex:1;min-width:0}}
 .ec-series{{font-family:var(--mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--fern);margin-bottom:4px}}
 .ec-date{{font-family:var(--mono);font-size:11px;letter-spacing:.05em;color:var(--ink-3);text-transform:uppercase}}
 .ec-title{{font-family:var(--serif);font-size:23px;font-weight:600;color:var(--moss);margin:4px 0 5px;line-height:1.2}}
 .ec-deck{{font-family:var(--serif);font-style:italic;font-size:15.5px;color:var(--ink-2);line-height:1.5}}
</style></head><body>
<div class="topbar"><div class="wrap">
 <a class="brandmark" href="/index.html" style="color:var(--moss)"><svg class="mark" viewBox="0 0 200 200" fill="none" aria-hidden="true"><path d="M100 30 C74 52 58 92 62 126 C64 152 82 168 100 176 L100 30 Z" fill="#2C4A38"/><path d="M100 30 C126 52 142 92 138 126 C136 152 118 168 100 176 L100 30 Z" fill="#8AA88B"/><line x1="100" y1="34" x2="100" y2="174" stroke="#FCFBF7" stroke-width="3"/><line x1="100" y1="176" x2="100" y2="194" stroke="#2C4A38" stroke-width="11" stroke-linecap="round"/></svg> Grammar&nbsp;of&nbsp;Meaning</a>
 <nav class="nav"><a href="/index.html">Home</a><a href="/about.html">About</a><a href="/library.html">Library</a><a href="/essays.html" class="active">Essays</a><a href="/garden.html">Garden</a><a href="/method.html">Method</a><a href="/reference.html">Reference</a><a href="https://grammarofmeaning.substack.com/" target="_blank" rel="noopener" class="nav-out">Substack&nbsp;&#8599;</a></nav>
</div></div>
<header class="hero"><div class="wrap">
 <div class="kicker">The Essays · <b>meaning-making in public</b></div>
 <h1>Essays from the Archive</h1>
 <div class="sub">Where the project thinks out loud — one figure, one image, one word, read closely enough to see what it is doing. Published here for keeps; also on the newsletter.</div>
</div></header>
<div class="wrap" style="padding-top:26px">
{cards}
</div>
<footer><div class="wrap"><div class="flabel">Grammar of Meaning</div><h3>How meaning gets made — read each tradition in its own vocabulary first.</h3><p class="foot-note"><em>Grammar of Meaning</em> · Tamara Sanderson · 2026</p></div></footer>
</body></html>"""

SUBJECT = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{name} — Essays · Grammar of Meaning</title>
<meta name="description" content="Essays touching on {name} — from the Grammar of Meaning.">
<link rel="canonical" href="https://grammarofmeaning.org/essays/topic/{tslug}.html">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/gom.css">
<style>
 .wrap{{max-width:920px}}
 .ecard{{display:flex;gap:20px;align-items:center;text-decoration:none;border:1px solid var(--rule);border-radius:14px;padding:18px 20px;margin-bottom:14px;background:var(--paper-3);transition:border-color .15s}}
 .ecard:hover{{border-color:var(--sage)}}
 .ecard img{{flex:0 0 92px;width:92px;height:92px;object-fit:cover;border-radius:8px;border:3px solid var(--sage)}}
 @media(max-width:560px){{.ecard img{{display:none}}}}
 .ec-body{{flex:1;min-width:0}}
 .ec-series{{font-family:var(--mono);font-size:10px;letter-spacing:.06em;text-transform:uppercase;color:var(--fern);margin-bottom:4px}}
 .ec-date{{font-family:var(--mono);font-size:11px;letter-spacing:.05em;color:var(--ink-3);text-transform:uppercase}}
 .ec-title{{font-family:var(--serif);font-size:23px;font-weight:600;color:var(--moss);margin:4px 0 5px;line-height:1.2}}
 .ec-deck{{font-family:var(--serif);font-style:italic;font-size:15.5px;color:var(--ink-2);line-height:1.5}}
 .backlink{{font-family:var(--mono);font-size:12px;color:var(--fern);text-decoration:none;display:inline-block;margin-top:14px}}
</style></head><body>
<div class="topbar"><div class="wrap">
 <a class="brandmark" href="/index.html" style="color:var(--moss)"><svg class="mark" viewBox="0 0 200 200" fill="none" aria-hidden="true"><path d="M100 30 C74 52 58 92 62 126 C64 152 82 168 100 176 L100 30 Z" fill="#2C4A38"/><path d="M100 30 C126 52 142 92 138 126 C136 152 118 168 100 176 L100 30 Z" fill="#8AA88B"/><line x1="100" y1="34" x2="100" y2="174" stroke="#FCFBF7" stroke-width="3"/><line x1="100" y1="176" x2="100" y2="194" stroke="#2C4A38" stroke-width="11" stroke-linecap="round"/></svg> Grammar&nbsp;of&nbsp;Meaning</a>
 <nav class="nav"><a href="/index.html">Home</a><a href="/about.html">About</a><a href="/library.html">Library</a><a href="/essays.html" class="active">Essays</a><a href="/garden.html">Garden</a><a href="/method.html">Method</a><a href="/reference.html">Reference</a><a href="https://grammarofmeaning.substack.com/" target="_blank" rel="noopener" class="nav-out">Substack&nbsp;&#8599;</a></nav>
</div></div>
<header class="hero"><div class="wrap">
 <div class="kicker">The Essays · <b>by subject</b></div>
 <h1>{name}</h1>
 <div class="sub">{n} {essays_word} touching on {name} — read across the archive.</div>
 <a class="backlink" href="/essays.html">&#8592; All essays</a>
</div></header>
<div class="wrap" style="padding-top:26px">
{cards}
</div>
<footer><div class="wrap"><div class="flabel">Grammar of Meaning</div><h3>How meaning gets made — read each tradition in its own vocabulary first.</h3><p class="foot-note"><em>Grammar of Meaning</em> · Tamara Sanderson · 2026</p></div></footer>
</body></html>"""

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="_staging/essays")
    ap.add_argument("--base", default=BASE)
    ap.add_argument("--repo", default=os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    args = ap.parse_args()
    outdir = os.path.join(args.repo, args.out)
    os.makedirs(outdir, exist_ok=True)
    # fetch a FRESH feed (Substack CDN-caches its RSS; bust it so new posts/edits show)
    try:
        import time
        busted = FEED + ("&" if "?" in FEED else "?") + "_=" + str(int(time.time()))
        req = urllib.request.Request(busted, headers={"User-Agent": "Mozilla/5.0", "Cache-Control": "no-cache", "Pragma": "no-cache"})
        d = feedparser.parse(urllib.request.urlopen(req, timeout=20).read())
        assert d.entries
    except Exception:
        d = feedparser.parse(FEED)
    SKIP = {"hello", "coming-soon", "welcome"}
    cards, urls = [], []
    # pass 1: render all (collect; don't write yet — complement blocks + link-rewrite need every essay known)
    rendered, post_urls = [], {}
    for e in d.entries:
        if slug_of(e.get("link", "")) in SKIP or e.get("title", "").lower().startswith("hello there"):
            print(f"  skip: {e.get('title')}"); continue
        r = render_essay(e); rendered.append(r); post_urls[r[0]] = e.get("link")
    META = {r[0]: {"title": r[2], "deck": r[3], "hero": r[6], "date_h": r[5]} for r in rendered}
    SLUGS = set(META)
    # scrape tags (Substack drops them from RSS) -> subject cross-linking; shared = tags on >=2 essays
    TAGS = {slug: fetch_tags(post_urls.get(slug)) for slug in SLUGS}
    tag_index = {}
    for slug, tags in TAGS.items():
        for name, ts in tags:
            tag_index.setdefault(ts, {"name": name, "essays": []})["essays"].append(slug)
    SHARED = {ts for ts, dd in tag_index.items() if len(dd["essays"]) >= 2}
    print(f"  tags: {len(tag_index)} total, {len(SHARED)} shared (>=2 essays)")
    # pass 2: fill subject chips + the 'Complement with…' block + rewrite her Substack cross-links, then write
    for slug, url, title, deck, date_iso, date_h, hero, page in rendered:
        page = page.replace("<!--TAGS-->", tag_chips_html(slug, TAGS, SHARED))
        page = page.replace("<!--COMPLEMENT-->", complement_html(slug, META))
        page = rewrite_substack_links(page, SLUGS)
        with open(os.path.join(outdir, f"{slug}.html"), "w") as f:
            f.write(page)
        cards.append((slug, title, deck, date_h, hero)); urls.append((url, date_iso))
        print(f"  wrote {slug}.html  ({title})")
    def card_html(s, t, dk, dh, h):
        si = series_of(s)
        tag = ""
        if si:
            label = "Intro" if si["role"] == "intro" else f'Day {si["n"]} of {si["total"]}'
            tag = f'<div class="ec-series">{esc(si["name"])} · {label}</div>'
        return (f'<a class="ecard" href="/essays/{s}.html"><img src="{esc(h)}" alt="">'
                f'<div class="ec-body">{tag}<div class="ec-date">{dh}</div>'
                f'<div class="ec-title">{esc(t)}</div><div class="ec-deck">{esc(dk)}</div></div></a>')
    cards_html = "\n".join(card_html(*c) for c in cards)
    with open(os.path.join(outdir, "index.html"), "w") as f:
        f.write(INDEX.format(cards=cards_html))
    print(f"  wrote index.html ({len(cards)} essays)")
    sm = "\n".join(f'<url><loc>{u}</loc><lastmod>{di}</lastmod></url>' for (u, di) in urls)
    with open(os.path.join(outdir, "sitemap-essays.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
    print(f"  wrote sitemap-essays.xml")

    # subject pages (one per shared tag) — the Marginalian 'browse by subject'
    card_by_slug = {c[0]: card_html(*c) for c in cards}
    forder = {c[0]: i for i, c in enumerate(cards)}
    topicdir = os.path.join(outdir, "topic")
    os.makedirs(topicdir, exist_ok=True)
    for ts in SHARED:
        d2 = tag_index[ts]
        eslist = sorted(d2["essays"], key=lambda s: forder.get(s, 999))
        ecs = "\n".join(card_by_slug[s] for s in eslist if s in card_by_slug)
        with open(os.path.join(topicdir, f"{ts}.html"), "w") as f:
            f.write(SUBJECT.format(name=esc(d2["name"]), tslug=ts, n=len(eslist),
                                   essays_word=("essay" if len(eslist) == 1 else "essays"), cards=ecs))
    print(f"  wrote {len(SHARED)} subject pages -> topic/")

    # ---- wire the hand-authored pages (idempotent marker-injection) + a site-wide sitemap ----
    repo = args.repo
    eslugs = "[" + ",".join('"%s"' % c[0] for c in cards) + "]"
    _btn = ('<div style="margin:2px 0 24px"><button onclick="__surprise()" style="font-family:var(--mono);'
            'font-size:12.5px;letter-spacing:.04em;color:var(--fern);background:var(--paper-3);'
            'border:1px solid var(--rule);border-radius:999px;padding:9px 18px;cursor:pointer">'
            '&#10022; Surprise me — read a random essay &#8594;</button></div>')
    _scr = (f'<script>const __ES={eslugs};function __surprise(){{location.href="/essays/"+'
            f'__ES[Math.floor(Math.random()*__ES.length)]+".html"}}</script>')
    _browse = ""
    if SHARED:
        _chips = "".join(
            f'<a href="/essays/topic/{ts}.html" style="font-family:var(--sans);font-size:12.5px;color:var(--ink);'
            f'text-decoration:none;background:var(--paper-3);border:1px solid var(--rule);border-radius:999px;'
            f'padding:5px 13px;display:inline-flex;align-items:center;gap:6px">{esc(tag_index[ts]["name"])}'
            f'<span style="font-family:var(--mono);font-size:10px;color:var(--ink-3)">{len(tag_index[ts]["essays"])}</span></a>'
            for ts in sorted(SHARED, key=lambda t: (-len(tag_index[t]["essays"]), tag_index[t]["name"].lower())))
        _browse = ('<div style="margin:2px 0 26px"><div style="font-family:var(--mono);font-size:10.5px;'
                   'letter-spacing:.08em;text-transform:uppercase;color:var(--ink-3);margin-bottom:10px">Browse by subject</div>'
                   '<div style="display:flex;flex-wrap:wrap;gap:8px">' + _chips + '</div></div>')
    ess_cards = _btn + _scr + _browse + "\n" + "\n".join(card_html(*c) for c in cards)
    if inject_region(os.path.join(repo, "essays.html"), "<!-- ESSAYS:START -->", "<!-- ESSAYS:END -->", ess_cards):
        print("  injected essay list -> essays.html")
    def home_card(c):
        s, t, dk, dh, h = c
        si = series_of(s)
        label = esc(si["name"]) if si else "Essay"
        return (f'<a class="he-card" href="/essays/{s}.html"><img src="{esc(h)}" alt="">'
                f'<span class="he-body"><span class="he-eyebrow">{label} · {dh}</span>'
                f'<span class="he-title">{esc(t)}</span><span class="he-deck">{esc(dk)}</span></span></a>')
    latest = '<div class="hp-essays">' + "".join(home_card(c) for c in cards[:2]) + '</div>'
    if inject_region(os.path.join(repo, "index.html"), "<!-- LATEST-ESSAY:START -->", "<!-- LATEST-ESSAY:END -->", latest):
        print("  injected latest card -> index.html")
    MAIN = ["", "essays.html", "about.html", "library.html", "garden.html", "method.html", "reference.html", "glossary.html", "bibliography.html", "principles.html", "scholars.html"]
    all_urls = [f"{BASE}/{p}" for p in MAIN] + [u for (u, _) in urls]
    smx = "\n".join(f'<url><loc>{u}</loc></url>' for u in all_urls)
    with open(os.path.join(repo, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{smx}\n</urlset>\n')
    print(f"  wrote site sitemap.xml\nDONE — {len(cards)} essays -> {outdir}")

if __name__ == "__main__":
    main()
