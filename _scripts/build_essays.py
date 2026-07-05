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
import argparse, os, re, sys, html, datetime
import feedparser
from bs4 import BeautifulSoup

FEED = "https://grammarofmeaning.substack.com/feed"
BASE = "https://grammarofmeaning.org"
CRUFT_CLASSES = ("image-link-expand", "subscribe-widget", "subscription-widget-wrap",
                 "button-wrapper", "pencraft")  # pencraft only removed when it wraps a button/icon

def slug_of(link):
    return link.rstrip("/").split("/")[-1]

def big_img(src):
    # prefer the w_1456 rendition Substack already serves
    return src

def clean_body(raw):
    """Sanitize Substack content:encoded -> clean house HTML. Returns (body_html, hero_src, hero_cap)."""
    soup = BeautifulSoup(raw, "html.parser")
    # kill interactive cruft (restack/share/expand buttons, inline svgs, subscribe widgets)
    for t in soup.find_all(["button", "svg"]):
        t.decompose()
    for t in soup.find_all(attrs={"class": lambda c: c and any(k in " ".join(c) for k in ("image-link-expand", "subscribe", "pencraft-button"))}):
        t.decompose()
    for t in soup.find_all(attrs={"data-component-name": True}):
        t.decompose()
    # normalize every captioned image to a clean <figure><img><figcaption>
    hero_src, hero_cap = None, None
    for i, cont in enumerate(soup.find_all(class_="captioned-image-container")):
        img = cont.find("img")
        src = big_img(img.get("src")) if img else None
        cap_el = cont.find("figcaption")
        cap = cap_el.get_text(" ", strip=True) if cap_el else ""
        if i == 0 and src:
            hero_src, hero_cap = src, cap
            cont.decompose()          # hero is shown separately in the header
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
    # drop empty spans/divs left behind
    for t in soup.find_all(["span", "div"]):
        if not t.get_text(strip=True) and not t.find("img"):
            t.unwrap() if t.name == "span" else t.decompose()
    # if no captioned hero, fall back to the first bare <img>
    if not hero_src:
        im = soup.find("img")
        if im:
            hero_src = big_img(im.get("src")); im.find_parent("figure") and im.find_parent("figure").decompose()
    return str(soup), hero_src, hero_cap

def esc(s): return html.escape(html.unescape(s or ""), quote=True)

def render_essay(e):
    title = e.get("title", "").strip()
    deck = re.sub(r"\s+", " ", (e.get("summary") or "")).strip()
    link = e.get("link")
    slug = slug_of(link)
    pp = e.get("published_parsed")
    dt = datetime.date(*pp[:3]) if pp else datetime.date.today()
    date_h = dt.strftime("%B %-d, %Y")
    date_iso = dt.strftime("%Y-%m-%d")
    raw = e.content[0].value if e.get("content") else (e.get("summary") or "")
    body, hero, hero_cap = clean_body(raw)
    url = f"{BASE}/essays/{slug}"
    hero_meta = hero or f"{BASE}/favicon.svg"
    hero_block = (f'<img class="e-img" src="{esc(hero)}" alt="{esc(title)}">'
                  + (f'<div class="e-imgcap">{esc(hero_cap)}</div>' if hero_cap else "")) if hero else ""
    return slug, url, title, deck, date_iso, date_h, hero_meta, PAGE.format(
        title=esc(title), deck=esc(deck), url=url, hero=esc(hero_meta), date_iso=date_iso,
        date_h=esc(date_h), body=body, slug=slug, hero_block=hero_block, sub_link=esc(link))

# ---- the house template (mirrors _staging/essays/the-god-at-the-threshold.html) ----
PAGE = """<!DOCTYPE html>
<html lang="en"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Grammar of Meaning</title>
<meta name="description" content="{deck}">
<link rel="canonical" href="{url}">
<link rel="author" href="/mission.html">
<meta property="og:type" content="article"><meta property="og:site_name" content="Grammar of Meaning">
<meta property="og:title" content="{title}"><meta property="og:description" content="{deck}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{hero}">
<meta property="article:published_time" content="{date_iso}"><meta property="article:author" content="Tamara Sanderson">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{deck}">
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Article","@id":"{url}","headline":"{title}","description":"{deck}","author":{{"@type":"Person","name":"Tamara Sanderson","url":"/mission.html"}},"publisher":{{"@type":"Organization","name":"Grammar of Meaning","url":"/"}},"datePublished":"{date_iso}","mainEntityOfPage":"{url}","isPartOf":{{"@type":"CreativeWorkSeries","name":"Field Notes from the Archive"}},"image":"{hero}"}}
</script>
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/gom.css">
<style>
 .wrap{{max-width:1080px}} .essay-wrap{{max-width:680px;margin:0 auto}}
 .backlink{{font-family:var(--mono);font-size:12px;color:var(--ink-2);text-decoration:none;display:inline-block;margin:6px 0 2px}} .backlink:hover{{color:var(--fern)}}
 .e-kicker{{font-family:var(--mono);font-size:11.5px;letter-spacing:.14em;text-transform:uppercase;color:var(--olive);margin:26px 0 10px}}
 .e-title{{font-family:var(--serif);font-weight:600;font-size:40px;line-height:1.12;color:var(--moss);margin:0 0 14px;letter-spacing:-.01em}}
 @media(max-width:640px){{.e-title{{font-size:31px}}}}
 .e-deck{{font-family:var(--serif);font-style:italic;font-size:20px;line-height:1.5;color:var(--ink-2);margin:0 0 20px;max-width:60ch}}
 .e-meta{{display:flex;align-items:center;gap:12px;flex-wrap:wrap;font-family:var(--sans);font-size:13.5px;color:var(--ink-2);border-top:1px solid var(--rule);border-bottom:1px solid var(--rule);padding:12px 0;margin:0 0 8px}}
 .e-meta a{{color:var(--fern);text-decoration:none;font-weight:500}} .e-meta .sep{{color:var(--rule)}}
 .e-img{{width:100%;border-radius:12px;margin:28px 0 6px;display:block;border:1px solid var(--rule)}}
 .e-imgcap{{font-family:var(--sans);font-size:12px;color:var(--ink-3);text-align:center;margin:0 0 30px;font-style:italic}}
 .essay{{font-family:var(--serif);font-size:19.5px;line-height:1.72;color:var(--ink)}}
 .essay p{{margin:0 0 24px}} .essay p:first-of-type::first-letter{{font-size:3.1em;line-height:.82;float:left;font-weight:600;color:var(--moss);padding:6px 10px 0 0}}
 .essay em{{font-style:italic}} .essay b,.essay strong{{font-weight:600;color:var(--moss)}}
 .essay h2,.essay h3{{font-family:var(--serif);color:var(--moss);line-height:1.2;margin:34px 0 12px}} .essay h2{{font-size:26px}} .essay h3{{font-size:21px}}
 .essay blockquote{{margin:28px 0;padding:4px 0 4px 22px;border-left:3px solid var(--sage);font-style:italic;color:var(--ink-2)}}
 .essay hr{{border:none;border-top:1px solid var(--rule);margin:38px auto;width:80px}}
 .essay figure{{margin:28px 0}} .essay figure img{{width:100%;border-radius:10px;border:1px solid var(--rule)}} .essay figcaption{{font-family:var(--sans);font-size:12px;color:var(--ink-3);text-align:center;margin-top:8px;font-style:italic}}
 .essay a{{color:var(--fern)}} .essay ol,.essay ul{{padding-left:24px}} .essay li{{margin:0 0 10px}}
 .also{{max-width:680px;margin:34px auto 0;padding:16px 20px;border:1px solid var(--rule);border-radius:12px;background:var(--paper-3);display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}}
 .also .t{{font-family:var(--sans);font-size:13.5px;color:var(--ink-2)}} .also a{{font-family:var(--sans);font-size:13.5px;font-weight:600;color:var(--fern);text-decoration:none;white-space:nowrap}}
 .byline-foot{{max-width:680px;margin:28px auto 0;font-family:var(--sans);font-size:13px;color:var(--ink-3);border-top:1px solid var(--rule);padding-top:16px;line-height:1.6}} .byline-foot a{{color:var(--fern);text-decoration:none}}
</style></head><body>
<div class="topbar"><div class="wrap">
 <a class="brandmark" href="/index.html" style="color:var(--moss)"><svg class="mark" viewBox="0 0 200 200" fill="none" aria-hidden="true"><path d="M100 30 C74 52 58 92 62 126 C64 152 82 168 100 176 L100 30 Z" fill="#2C4A38"/><path d="M100 30 C126 52 142 92 138 126 C136 152 118 168 100 176 L100 30 Z" fill="#8AA88B"/><line x1="100" y1="34" x2="100" y2="174" stroke="#FCFBF7" stroke-width="3"/><line x1="100" y1="176" x2="100" y2="194" stroke="#2C4A38" stroke-width="11" stroke-linecap="round"/></svg> Grammar&nbsp;of&nbsp;Meaning</a>
 <nav class="nav"><a href="/index.html">Home</a><a href="/mission.html">About</a><a href="/library.html">Library</a><a href="/essays.html" class="active">Essays</a><a href="/garden.html">Garden</a><a href="/method.html">Method</a><a href="/glossary.html">Reference</a><a href="https://grammarofmeaning.substack.com/" target="_blank" rel="noopener" class="nav-out">Substack&nbsp;&#8599;</a></nav>
</div></div>
<div class="wrap"><article class="essay-wrap">
 <a class="backlink" href="/essays.html">&#8592; The Essays</a>
 <div class="e-kicker">Field Note · Grammar of Meaning</div>
 <h1 class="e-title">{title}</h1>
 <p class="e-deck">{deck}</p>
 <div class="e-meta"><span>By <a href="/mission.html">Tamara Sanderson</a></span><span class="sep">·</span><span>{date_h}</span><span class="sep">·</span><span>Field Notes from the Archive</span></div>
 {hero_block}
 <div class="essay">{body}</div>
 <div class="also"><span class="t">This essay is also on the newsletter.</span><a href="{sub_link}" target="_blank" rel="noopener">Read / subscribe on Substack &#8599;</a></div>
 <div class="byline-foot"><b>Tamara Sanderson</b> writes <em>Field Notes on how meaning gets made</em> — reading one life, image, or word at a time. <a href="/mission.html">About the project &#8594;</a></div>
</article></div>
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
    d = feedparser.parse(FEED)
    cards = []
    urls = []
    SKIP_SLUGS = {"hello", "coming-soon", "welcome"}
    for e in d.entries:
        if slug_of(e.get("link", "")) in SKIP_SLUGS or (e.get("title", "").lower().startswith("hello there")):
            print(f"  skip (welcome/non-essay): {e.get('title')}")
            continue
        slug, url, title, deck, date_iso, date_h, hero, page = render_essay(e)
        with open(os.path.join(outdir, f"{slug}.html"), "w") as f:
            f.write(page)
        cards.append((slug, title, deck, date_h, date_iso, hero))
        urls.append((url, date_iso))
        print(f"  wrote {slug}.html   ({title})")
    # index
    cards_html = "\n".join(
        f'<a class="ecard" href="{s}.html"><div class="ec-date">{dh}</div><div class="ec-title">{esc(t)}</div><div class="ec-deck">{esc(dk)}</div></a>'
        for (s, t, dk, dh, di, h) in cards)
    with open(os.path.join(outdir, "index.html"), "w") as f:
        f.write(INDEX.format(cards=cards_html))
    print(f"  wrote index.html ({len(cards)} essays)")
    # sitemap (essays only; the full-site sitemap is generated at unpark)
    sm = "\n".join(f'<url><loc>{u}</loc><lastmod>{di}</lastmod></url>' for (u, di) in urls)
    with open(os.path.join(outdir, "sitemap-essays.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sm}\n</urlset>\n')
    print(f"  wrote sitemap-essays.xml")
    print(f"DONE — {len(cards)} essays -> {outdir}")

INDEX = """<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>The Essays — meaning-making in public · Grammar of Meaning</title>
<meta name="description" content="Field notes on how meaning gets made — reading one life, image, or word at a time.">
<link rel="canonical" href="https://grammarofmeaning.org/essays/">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Newsreader:ital,opsz,wght@0,6..72,400;0,6..72,500;0,6..72,600;1,6..72,400;1,6..72,500&family=IBM+Plex+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/gom.css">
<style>
 .wrap{{max-width:960px}}
 .ecard{{display:block;text-decoration:none;border:1px solid var(--rule);border-radius:14px;padding:22px 24px;margin-bottom:14px;background:var(--paper-3);transition:border-color .15s}}
 .ecard:hover{{border-color:var(--sage)}}
 .ec-date{{font-family:var(--mono);font-size:11px;letter-spacing:.05em;color:var(--ink-3);text-transform:uppercase}}
 .ec-title{{font-family:var(--serif);font-size:24px;font-weight:600;color:var(--moss);margin:6px 0 6px;line-height:1.2}}
 .ec-deck{{font-family:var(--serif);font-style:italic;font-size:16px;color:var(--ink-2);line-height:1.5;max-width:64ch}}
</style></head><body>
<div class="topbar"><div class="wrap">
 <a class="brandmark" href="/index.html" style="color:var(--moss)"><svg class="mark" viewBox="0 0 200 200" fill="none" aria-hidden="true"><path d="M100 30 C74 52 58 92 62 126 C64 152 82 168 100 176 L100 30 Z" fill="#2C4A38"/><path d="M100 30 C126 52 142 92 138 126 C136 152 118 168 100 176 L100 30 Z" fill="#8AA88B"/><line x1="100" y1="34" x2="100" y2="174" stroke="#FCFBF7" stroke-width="3"/><line x1="100" y1="176" x2="100" y2="194" stroke="#2C4A38" stroke-width="11" stroke-linecap="round"/></svg> Grammar&nbsp;of&nbsp;Meaning</a>
 <nav class="nav"><a href="/index.html">Home</a><a href="/mission.html">About</a><a href="/library.html">Library</a><a href="/essays.html" class="active">Essays</a><a href="/garden.html">Garden</a><a href="/method.html">Method</a><a href="/glossary.html">Reference</a><a href="https://grammarofmeaning.substack.com/" target="_blank" rel="noopener" class="nav-out">Substack&nbsp;&#8599;</a></nav>
</div></div>
<header class="hero"><div class="wrap">
 <div class="kicker">The Essays · <b>meaning-making in public</b></div>
 <h1>Field Notes from the Archive</h1>
 <div class="sub">Where the project thinks out loud — one figure, one image, one word, read closely enough to see what it is doing. Published here first for keeps; also on the newsletter.</div>
</div></header>
<div class="wrap" style="padding-top:26px">
{cards}
</div>
<footer><div class="wrap"><div class="flabel">Grammar of Meaning</div><h3>How meaning gets made — read each tradition in its own vocabulary first.</h3><p class="foot-note"><em>Grammar of Meaning</em> · Tamara Sanderson · 2026</p></div></footer>
</body></html>"""

if __name__ == "__main__":
    main()
