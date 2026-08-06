#!/usr/bin/env python3
"""Extract the Gospels reading-room image config from the Lovable gospel-depths mock.
render-from-data (§2.16). Preserves EXACT img URLs + crops (curation, per IMAGE-CREDITS.md
'never swap/regenerate'). Re-run if the mock updates.

Usage: extract_gospels_room_config.py <path-to-extracted-mock-root>
Emits: reading-room-preview/data/gospels_room_config.json
  - movements: 6 × candidate plates (MET CDN urls + crop + credit) from plates.tsx
  - grounds:   9 entry-page material grounds (mirrored local images + tokens) from index.tsx
  - entry:     landing tagline + shared shadows + default ground
"""
import re, json, sys

GDE = sys.argv[1] if len(sys.argv) > 1 else "."

def match_close(s, i):
    depth = 0; instr = None
    while i < len(s):
        c = s[i]
        if instr:
            if c == '\\': i += 2; continue
            if c == instr: instr = None
        elif c in '"\'`': instr = c
        elif c in '[{': depth += 1
        elif c in ']}':
            depth -= 1
            if depth == 0: return i
        i += 1
    return -1

def objs(body):
    i = 0
    while i < len(body):
        if body[i] == '{':
            j = match_close(body, i); yield body[i:j+1]; i = j+1
        else: i += 1

def field(o, k):
    m = re.search(k + r'\s*:\s*"((?:[^"\\]|\\.)*)"', o)
    return m.group(1).replace('\\"', '"') if m else None

def array_after(src, name):
    si = src.index(name); eq = src.index('=', si); lb = src.index('[', eq)
    return src[lb:match_close(src, lb)+1]

# ---- movements + candidate plates (plates.tsx) ----
plates_src = open(GDE + "/src/routes/plates.tsx").read()
movements = []
for sec in objs(array_after(plates_src, "const SECTIONS")[1:-1]):
    ci = sec.index('cands'); clb = sec.index('[', ci); cbody = sec[clb:match_close(sec, clb)+1]
    cands = []
    for c in objs(cbody[1:-1]):
        img = field(c, 'img')
        if not img: continue
        t = field(c, 't'); d = field(c, 'd'); a = field(c, 'a'); note = field(c, 'note')
        cm = re.search(r'crop\s*:\s*\[([^\]]+)\]', c)
        crop = [float(x) for x in cm.group(1).split(',')] if cm else None
        cands.append({"img": img, "title": t, "date": d, "artist": a, "crop": crop,
                      "current": bool(re.search(r'current\s*:\s*true', c)),
                      "credit": " · ".join(x for x in [t, a, d, "The Met"] if x),
                      **({"note": note} if note else {})})
    movements.append({"n": field(sec, 'n'), "title": field(sec, 'title'),
                      "latin": field(sec, 'latin'), "brief": field(sec, 'brief'),
                      "candidates": cands})

# ---- entry grounds (index.tsx VARIANTS + entry.ts hAlign overrides) ----
idx_src = open(GDE + "/src/routes/index.tsx").read()
ent_src = open(GDE + "/src/config/entry.ts").read()
# per-variant hAlign override (entry.ts VARIANT_OVERRIDES); default = ENTRY_DEFAULTS lower-middle.
# alignPosition() uses the focus's X but the hAlign's Y — so object-position-Y comes from hAlign.
HALIGN_Y = {'top': '0%', 'upper': '20%', 'upper-middle': '35%', 'center': '50%', 'lower-middle': '62%', 'bottom': '100%'}
halign_over = {}
for mm in re.finditer(r'(\w+):\s*\{[^}]*?hAlign:\s*"([^"]+)"', ent_src):
    halign_over[mm.group(1)] = mm.group(2)
imp = {}
for m in re.finditer(r'import\s+(\w+)\s+from\s+"@/assets/([^"]+?)(?:\.asset\.json)?"', idx_src):
    imp[m.group(1)] = m.group(2)
WANT = ['coptic', 'gold', 'stone', 'glass', 'ivory', 'enamel', 'ktisis', 'lawrence', 'armenian']
# per IMAGE-CREDITS.md: which ground filenames are MET Open Access (CC0) vs project-rendered textures.
MET_SOURCED = {  # filename -> Met collection object URL (where IMAGE-CREDITS gives one)
    'four-gospels-armenian.jpg': 'https://www.metmuseum.org/art/collection/search/478665',
    'met-ktisis.jpg': 'https://www.metmuseum.org/art/collection/search/469960',
    'met-lawrence.jpg': None, 'met-eleousa.jpg': None,
    'ivory-diptych.jpg': None, 'limoges-enamel.jpg': None,
    'coptic-tapestry.jpg': None, 'glass-plate.jpg': None,
}
grounds = []
for o in objs(array_after(idx_src, "const VARIANTS")[1:-1]):
    vid = field(o, 'id')
    if vid not in WANT: continue
    sm = re.search(r'src\s*:\s*(\w+)(?:\.url)?', o)
    fn = imp.get(sm.group(1)) if sm else None
    vig = re.search(r'vignette\s*:\s*"([^"]+)"', o)
    filt = re.search(r'imgFilter\s*:\s*\n?\s*"([^"]+)"', o)
    is_met = fn in MET_SOURCED
    # cropping (match the mock's WideLayout): object-position = focus-X + hAlign-Y; scale = wideZoom; origin = wideOrigin; flip
    focus = field(o, 'focus') or '50% 50%'
    focus_x = focus.split()[0]
    ha = halign_over.get(vid, 'lower-middle')
    obj_pos = focus_x + ' ' + HALIGN_Y.get(ha, '62%')
    wz = re.search(r'wideZoom\s*:\s*([\d.]+)', o)
    wide_zoom = float(wz.group(1)) if wz else 1.05
    wo = re.search(r'wideOrigin\s*:\s*"([^"]+)"', o)
    wide_origin = wo.group(1) if wo else 'center center'
    flip = bool(re.search(r'flip\s*:\s*true', o))
    grounds.append({"id": vid, "label": field(o, 'label'), "note": field(o, 'note'),
                    "alt": field(o, 'alt'),
                    "img": ("assets/grounds/" + fn) if fn else None,
                    "source": "met" if is_met else "project",
                    "credit_tail": ("The Met — Open Access (CC0)" if is_met else "ground texture — Grammar of Meaning"),
                    "met_url": MET_SOURCED.get(fn) if is_met else None,
                    "ground_color": field(o, 'ground'), "focus": field(o, 'focus'),
                    "object_position": obj_pos, "wide_zoom": wide_zoom, "wide_origin": wide_origin, "flip": flip,
                    "vignette": vig.group(1) if vig else None,
                    "imgFilter": filt.group(1) if filt else None,
                    "kicker": field(o, 'kicker'), "title_color": field(o, 'title'),
                    "rule": field(o, 'rule'), "body_color": field(o, 'body')})

config = {
 "_note": "Gospels reading-room image config — extracted from the Lovable gospel-depths mock via _scripts/extract_gospels_room_config.py. render-from-data (§2.16). Images MET Open Access (CC0) or project-owned ground textures; provenance authoritative in the mock's IMAGE-CREDITS.md. RULES: never swap/regenerate images; crop = curation, tune don't reset; on 404 look up SAME object via Met API. 'credit' = museum caption + PD-source record (§2.4).",
 "source": "gospel-depths-explorer mock · plates.tsx + index.tsx + IMAGE-CREDITS.md",
 "license": "MET Open Access (CC0) for museum images; entry-ground textures are project-owned",
 "entry": {
   "title": "The Gospels",
   "tagline": "Six movements. Four witnesses. One life, told four times over — read slowly, in the old manner.",
   "default_ground": "coptic", "rotate": True,
   "title_shadow": "0 1px 2px rgba(0,0,0,.42), 0 0 18px rgba(0,0,0,.32), 0 0 40px rgba(0,0,0,.14)",
   "body_shadow": "0 1px 2px rgba(0,0,0,.38), 0 0 12px rgba(0,0,0,.26), 0 0 28px rgba(0,0,0,.1)"
 },
 "grounds": grounds,
 "movements": movements,
}
open("reading-room-preview/data/gospels_room_config.json", "w").write(json.dumps(config, indent=2, ensure_ascii=False))
print("grounds:", len(grounds), "| movements:", len(movements), "| candidates:", sum(len(m['candidates']) for m in movements))
for g in grounds: print(f"  {g['id']:9s} {g['label']:26s} {g['img']}")
