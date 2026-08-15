# Lovable handoff — the Gospels Labyrinth

**A Chartres labyrinth made of the gospel's own images — flat, aerial, illuminated.**
For: Lovable · From: Design SB · 2026-08-14

---

## The prompt — paste this into Lovable

> Build a contemplative React app: **the Gospels Labyrinth** — a pilgrimage you walk toward the empty tomb. Start from the working reference **viz_labyrinth.html** (a Leaflet **CRS.Simple** pan/zoom map: a path through six gospel signposts, with 72 curated public-domain miniatures) and its data feed **journey_gospels.json**. **Port the proven mechanics** — the path layout, the tile placement, and the click-a-tile detail drawer — into React + **react-leaflet**; **render everything from the feed** (never hardcode tiles). Then make it a **flat, aerial, circular Chartres labyrinth made *of* the images themselves** — a Christian gospel-wheel in the spirit of a Beatus Lamb-wheel (the devotional cousin of the Tibetan Wheel of Life — see the attached reference images).
>
> 1. **Form:** a **circular, unicursal labyrinth** (one winding path, no dead ends, spiralling inward) whose **concentric circuits are tiled with the curated miniatures**, so the labyrinth itself is *made of* the artworks (the way a Beatus wheel is composed of radiating figures). Lay the tiles out **intentionally and composed** — even, orderly, rhythmic rings following the circuits, deliberate — **never a random scatter**.
> 2. **The center holds an actual artwork** — a resurrection / Lamb miniature (where the Beatus wheel sets the Lamb), the focal image the whole labyrinth winds toward.
> 3. **Interaction:** flat and aerial — you pan and **zoom into a cell** and it resolves into that miniature, with its quiet museum label. **No 3D, no tunnel, no vertigo.**
> 4. **Decorative flourish around the edges** — an **illuminated-manuscript border**: vine-scroll / acanthus ornament, gold-leaf, jewel color, with **corner flourishes** (optionally the four evangelist symbols — Matthew-angel · Mark-lion · Luke-ox · John-eagle). A real decorative frame, not a plain ring.
> 5. **Palette:** illuminated-manuscript jewel tones — gold, lapis blue, vermilion, verdure green on a dark ground; flat, luminous, no modeling.
> 6. **The flip-card** — miniature front, museum label (title · culture · date · museum · license) back; ≤6° tilt, slow spring.
> 7. Responsive (desktop / tablet / mobile); v2: OpenSeadragon deep-zoom into a leaf.
>
> Use the **Garden tokens** from the reference's stylesheet (ink #14110d, gold #c9a227 / #e6c65a, parchment #e8ddc7, Cormorant + IBM Plex Mono) — port, don't invent. **Hard rules:** 2D only · provenance is a quiet museum label, always present · silence is the default soundtrack · no metrics, urgency, or infinite scroll.

---

## How Lovable gets the files

Lovable can't read a file path — give it the actual files one of two ways:
- **Upload / attach three files:** the reference `viz_labyrinth.html`, the feed `journey_gospels.json`, and this handoff. *(The upload option in Lovable's "how should I get the files?" dialog — pick that one.)*
- **Or connect the GitHub repo** `tamaracsanderson/grammarofmeaning-site` — it can then read the reference, the feed, and this spec directly.
- **Also attach the reference IMAGES** for the look-and-feel (Lovable takes image refs): the **Beatus Lamb-wheel** (the primary model), the **gold mandala thangka** (concentric + framed), the **millefleur / verdure tapestry** (the dense "intentional" packing + the Garden), and a **Chartres labyrinth** image for the path shape.

## What Lovable receives (reuse, don't reinvent)

| What | Where |
|---|---|
| Working reference (the mechanics) | `viz_labyrinth.html` |
| The data feed (6 signposts × tiles) | `journey_gospels.json` |
| The curation script (re-runnable) | `build_labyrinth_journey.py` |
| The charter (DWS) | `labyrinth_DWS_v2_2026-08-14.md` |
| Design tokens | inline in the reference's `<style>` |

## Components to build

- `<LabyrinthMap>` — react-leaflet, `CRS.Simple`; hosts the circular labyrinth + the tiled circuits.
- `<LabyrinthCircuits>` — the concentric unicursal path; tiles laid in **orderly, composed rings** (deterministic, never random).
- `<CenterIcon>` — the focal artwork at the middle (a resurrection / Lamb miniature).
- `<IlluminatedBorder>` — the decorative flourish framing the whole (vine-scroll / acanthus, gold-leaf, corner ornaments).
- `<Tile>` — a miniature; click → the card.
- `<FlipCard>` — front = artwork, back = museum label; ≤6° tilt, slow spring.

**One bespoke piece only:** the circular labyrinth layout + the orderly tile placement. Everything else is Leaflet + Framer-Motion glue.

## The data contract

Every tile, label, and count comes from this shape — add a signpost or tile by editing the feed (or re-running the curation script). No code change.

```json
{
  "signposts": [
    {
      "n": "VI", "key": "resurrection", "title": "Resurrection",
      "latin": "Resurrectio", "refs": "Mt 28 · Mk 16 · Lk 24 · Jn 20",
      "line": "The empty tomb told four ways…",
      "tiles": [
        {
          "img": "…/…_web.jpg",       // the miniature
          "full": "…/…_print.jpg",    // larger, for deep-zoom
          "title": "The Resurrection",
          "culture": "France, Paris", "date": "c. 1375",
          "museum": "Cleveland Museum of Art", "license": "CC0",
          "medium": "ink, tempera and gold on parchment",
          "scene": "resurrection", "url": "https://…"
        }
      ]
    }
  ]
}
```

## Hard rules

- 2D only. No 3D camera, no scroll-jack, no forced parallax.
- Honor `prefers-reduced-motion` globally — every flip/transition degrades to a crossfade.
- Provenance = a quiet museum label, always present per image.
- Silence is the default soundtrack. Sound is opt-in, never per-image.
- No metrics, no urgency, no infinite scroll.
- Render-from-data; tokens ported, not invented.

## Done means

A first-time visitor sees a flat, aerial illuminated labyrinth **made of gospel miniatures**, winding to a resurrection at the center, framed by a decorative illuminated border. They zoom into any cell and it becomes the artwork, with its quiet museum label. Contemplative, motion-safe, rendered from a feed any new theme can flow through.

<!-- METHODOLOGY FOOTER
HOW PRODUCED: Design SB 2026-08-14. PI chose the Chartres-labyrinth direction from the thumbnail sketches, then refined:
  intentional/composed tile layout, an artwork at the center, a decorative illuminated flourish around the edges. PI also asked
  for a plain markdown file (not an HTML artifact) to hand to Lovable. This is that file — the finalized handoff.
SCHOLARLY SOURCES: labyrinth_DWS_v2_2026-08-14.md; viz_labyrinth.html (the kernel); journey_gospels.json + build_labyrinth_journey.py;
  the PI's moodboard (Beatus Lamb-wheel, Wheel of Life, mandala thangka, millefleur/unicorn tapestry, mappa mundi, Pavias icon).
WHAT NEEDS VERIFICATION: (1) the circular-labyrinth layout + orderly tile placement is the one bespoke build — play-test the packing.
  (2) attach the reference images so Lovable matches the illuminated aesthetic. (3) the center artwork wants a good resurrection/Lamb miniature.
-->
