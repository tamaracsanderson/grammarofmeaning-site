# The Reading-Room House Pattern — a spec

**A reading room is a TEMPLATE, not a page.** One fixed skeleton + one swappable **tradition config**. Build the Gospels room once; spin up a Buddhist / Sufi / Vedic / Yoruba room by swapping the config — and each *feels native* to its tradition, not reskinned. This is the same "build the instrument, not just the finding" ethos as the rest of the project (§2.15: consolidate the exploration into a repeatable process).

Sibling references: the GoM house pattern (`_staging/_bakeoff/HOUSE_PATTERN.html`); the current reading-room pages (`reading-room-preview/*.html`); the Lovable "Night Gallery · FINAL" TOC + gospel landing mock. Aesthetic north star (PI-supplied): the fine-art / luxury publishers — Taschen, Assouline, Rizzoli, Phaidon, Gestalten. The feeling to hit: **a coffee-table book that comes to life.**

---

## 1. The two grounds (one palette, two room-tones)

The single move that keeps Lovable + current reading as ONE site — not two — is to name the pattern as **one system with two grounds**:

| Ground | Where it's used | Tone | Texture |
|---|---|---|---|
| **PAPER ground** | reading surfaces — landing, essays, braid, the reading itself | warm rag-paper (`--paper #FCFBF7` light / `#1C1813` dark) | **vellum / linen** low-opacity fiber overlay — the tactility. *This is where vellum/linen lives (PI-confirmed) — NOT the gallery.* |
| **PLATE ground** | art galleries — the Night Gallery TOC, art displays | deep near-black (`~#0d0b06`) | none — clean black so the plates GLOW |

The **same accent palette** ties both grounds together (moss/fern green · illuminated gold · terracotta), so moving from a dark gallery to a paper reading page feels like *turning a page in one book*, not switching sites. That shared palette is the coherence guarantee.

---

## 2. The fixed skeleton (shared across every tradition)

These never change room-to-room — they ARE the house:

**Type system** — Fraunces (display, the big illuminated titles) · Newsreader (serif body / reading) · Inter (UI) · IBM Plex Mono (eyebrows + museum captions). Already the GoM reading-room stack.

**Structure** — landing (icon hero + rotating background + ambient player) → **gallery TOC** (horizontal, movement-ordered, PLATE ground) → reading surfaces (PAPER ground).

**The "coffee-table-alive" elements** (what makes a reading room *experiential* vs. the schema/method pages):
1. **Material texture** — the vellum/linen fiber overlay on the PAPER ground (subtle, ~4–8% opacity noise/fiber). The biggest single "comes-to-life" lever.
2. **The plate-frame** — art gets a thin gold border + soft inner shadow (the Assouline/Taschen "the object is precious" treatment). On the PLATE ground the plate glows out of the black.
3. **Illuminated moments** — gold drop-caps, hairline gold rules, Roman-numeral movement markers (I · II · III), Latin/native movement names (ADVENTUS · DESERTUM).
4. **Slow reveal** — plates fade / gently parallax in on scroll; restrained (Phaidon-minimal, not flashy). **Always `prefers-reduced-motion`-aware.**
5. **The caption voice** — mono, museum-label ("THE ADORATION OF THE SHEPHERDS, CA. 1605–10 · THE MET"). Provenance + license, always credited.

**Interactions** — theme toggle · the ambient player · horizontal scroll (gallery) · keyboard nav. All identical across traditions.

---

## 3. The tradition config (the swappable layer) — THE point

Everything a new tradition-room needs to *feel native* is a config object. Swap it → new room. Nothing else changes.

```js
tradition = {
  id:        "gospels",
  name:      "The Gospels",
  tagline:   "Four accounts · one door",
  hero_icon: "christ-pantocrator.jpg",        // the landing icon

  accent:    { /* optional per-tradition tint OVER the base palette — */
               /* e.g. Byzantine gold-forward vs. a jade-forward Buddhist room */
               gold: "#B08A3C", green: "#2C4A38" },

  background_pool: [ "plate-nativity.jpg", "plate-wilderness.jpg", ... ],
             // rotating landing backgrounds (per-visit pick + slow crossfade)

  music_manifest: [ { title, tradition, performer, src, license, credit_line }, ... ],
             // the ambient player pool — Librarian-sourced, open-license, credited
             // (Gospels: Palestrina + Ethiopian/Coptic/Syriac/Georgian/Byzantine/…)

  movements: [ { numeral:"I", title:"NATIVITY", label:"ADVENTUS",
                 refs:"MT 1–2 · LK 1–2",
                 one_line:"A birth reported by two witnesses and passed over in silence by two others.",
                 plate:"adoration-shepherds.jpg",
                 caption:"THE ADORATION OF THE SHEPHERDS, CA. 1605–10 · THE MET" }, ... ],
             // the Night Gallery TOC — order + art + the thesis-bearing one-liners

  voices: [ { name:"Matthew", emblem:"matthew-angel.svg" }, ... ],
             // the four evangelists → OR a tradition's key figures/schools

  captions_voice: "museum-label, provenance + license",
}
```

**The Gospels room = this config, filled.** A Buddhist room = the same skeleton with `hero_icon` = a Buddha image, `movements` = its own arc, `music_manifest` = its own chant traditions, `plates` = its own art, `voices` = its schools/sutra-collections. The *experience* (dark gallery, illuminated plates, ambient sound, slow reveal, museum captions) is identical; the *content* is native.

---

## 4. Fixed vs. swappable — the contract

| Layer | Fixed (the house) | Swappable (the tradition config) |
|---|---|---|
| Type system | ✅ Fraunces/Newsreader/Inter/Plex Mono | — |
| Two grounds + palette structure | ✅ paper + plate, accent scheme | accent *tint* only |
| Coffee-table-alive elements | ✅ texture, plate-frame, illumination, reveal, caption voice | — |
| Interactions | ✅ theme / player / scroll / keyboard | — |
| Hero icon | — | ✅ `hero_icon` |
| Background pool | — | ✅ `background_pool` |
| Music | — | ✅ `music_manifest` (Librarian-sourced) |
| Movements / TOC | — | ✅ `movements` (art + one-liners + refs) |
| Voices / figures | — | ✅ `voices` |

**Rule (per §2.13/§2.16):** the config is DATA — a JSON the page renders from, never hardcoded in the HTML. Same discipline as the library/method pages: change the tradition → change the config → the room re-renders. This is what makes the reading room a repeatable instrument, not a bespoke page.

---

## 5. The Gospels instance (the first build)

- **Landing:** Christ Pantocrator hero · rotating background pool (the illuminated plates — *decision pending: plates only vs. broader icon/manuscript set*) · the existing **evensong player ported as-is**, then extended to the Librarian's expanded manifest.
- **TOC:** the **Night Gallery · FINAL** dark-room horizontal gallery — movements ADVENTUS/DESERTUM/… with their plates, refs, and the thesis-bearing one-liners.
- **Reading surfaces (resurrection.html etc.):** unchanged in structure; gain the **vellum/linen** PAPER-ground texture so they sit in the same book as the new landing.
- Art plates: `reading-room-plates-svg.zip` (nativity/baptism/teaching/miracle/passion/resurrection + the four voices).

---

## 6. Build sequence + the pane gate

1. **Now (no pane):** this spec + the Librarian music request (sent) + lock the one open decision (background pool).
2. **Build (pane-gated — experiential, needs a working pane to verify the *feel*):**
   - a. the **reading-room config JSON** (Gospels) + a `_HOUSE_PATTERN.css` the pages share;
   - b. the **landing** (rotating bg + evensong player) — smaller, self-contained, first;
   - c. the **Night Gallery TOC** (from the mock's selected variant);
   - d. retrofit the vellum/linen texture onto the existing reading surfaces.
3. A visual **house-pattern page** (sibling to `HOUSE_PATTERN.html`) documenting the two grounds + the swappable layer — built when a pane's up.

Each page is a NEW standalone file (no flagship-SSOT risk) but heavily aesthetic, so verified on a working pane (PI's or reading-SB's) before it's called done.

---

## HOW PRODUCED
design-SB, S159 (2026-08-04), PI-directed. The PI is rebuilding the Gospels reading-room landing + TOC from a Lovable mock (gospel-depths-explorer) and asked for (a) a way to make Lovable + current read as ONE site, and (b) a reusable "reading room house pattern" that feels like a coffee-table book come to life — AND is easy to re-skin per tradition (swap backgrounds/music/touches). This spec answers all three via the two-grounds model + the parameterized tradition-config.

## SCHOLARLY / DESIGN SOURCES
The GoM reading-room house tokens (`reading-room-preview/*.html`); the Lovable Night Gallery + gospel landing mock; the PI's fine-art-publisher references (Taschen/Assouline/Rizzoli/Phaidon/Gestalten); §2.8 (bias-visibility — the reading room should sound + look like the corpus, not the Anglophone default); §2.13/§2.16 (render-from-data, single store of record); §2.15 (diverge → consolidate into a repeatable process).

## WHAT NEEDS VERIFICATION
The build is pane-gated (both CCD panes stuck all S159) — the *feel* (rotation timing, parallax, dark-room glow, texture weight) must be eyeball-verified on a working pane before ship. Open decision: the homepage background pool (plates only vs. broader curated set). The tradition-config schema above is a strawman — it firms up as the first (Gospels) build exercises it.
