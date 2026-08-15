# Lovable handoff — the Gospels Labyrinth (the Garden's pilgrimage surface)

**For:** Lovable · **From:** Design SB · **Date:** 2026-08-14
**One line:** assemble the polished app around a *proven kernel* — Lovable does React app-assembly + immersion; the hard part (the labyrinth + the curated feed) is already built and de-risked.

---

## 0. Ready now? — YES
The pre-Lovable kernel exists and is live: **`viz_labyrinth.html`** (a Leaflet CRS.Simple pan/zoom map; a unicursal switchback path through the six gospel signposts; 72 curated CC0 miniatures clustered per signpost; renders from a JSON feed). Lovable's job is to make it a beautiful React app with the immersion below — *against this reference*, not from scratch. This is the DWS's marked "Lovable enters here" point.

## 1. The design evolution (PI, 2026-08-14): make it a REAL labyrinth — the "pulled-in" feel
The current kernel is a flat *aerial* map. The PI wants it to feel like **you're drawn inward as you circle the gallery — like a tunnel, or the entrance to a holy well.** The labyrinth-walk should *pull toward the center* (the empty tomb / resurrection at signpost VI), not just pan flat.

**How to build the pull — MOTION-SAFE (this is a hard rule, see §5):**
- **Compositional descent, not camera vertigo.** The "pulled-in" is done with *light + vignette + inward geometry*, NOT a 3D fly-through or scroll-jacked zoom (the Getty-nausea failure mode). The user still drives pan/zoom.
- **The center glows / draws the eye.** The resurrection cluster (VI, near center) is lit warmest; the outer signposts (Nativity, rim) are cooler/dimmer. Circling inward = moving toward light.
- **Vignette that deepens toward the middle** — a soft darkening at the edges (the "well mouth" / tunnel), lightening at the center. Subtle, contemplative — the *well*, not a spotlight.
- **The path spirals/switchbacks inward** (already unicursal) — reaching the center is arrival. Optionally a gentle *ease-toward-center* on zoom-in (the map recentres on the resurrection when you zoom past a threshold) — slow, opt-out under reduced-motion.
- **Depth by layering, not parallax** — a faint concentric-ring texture / stonework under the path (the well shaft), miniatures floating above it. No forced parallax (vestibular risk).
- Think **Chartres labyrinth seen from within a well** + illuminated-manuscript light — contemplative descent, not a rollercoaster.

## 2. What Lovable RECEIVES (the proven kernel — reuse, don't reinvent)
| Artifact | Path | What it is |
|---|---|---|
| **The working reference** | `_staging/viz_labyrinth.html` | Leaflet CRS.Simple map; the labyrinth-path layout (waypoint polyline + arc-length station sampler); tile-cluster placement; click-tile → detail drawer; the resurrection braid. **The proven mechanics — port these, don't redo them.** |
| **The data feed** | `engine/data/labyrinth/journey_gospels.json` | 6 signposts, each with `tiles[]`: `{img, full, title, culture, date, museum, license, medium, scene, url}`. The data contract Lovable renders from. |
| **The curation script** | `_scripts/build_labyrinth_journey.py` | Re-runnable; re-curates the feed (title-match + miniature-medium + CC0). Run to add tiles / new signposts. |
| **The charter** | (twelve-laws) `research/10_dr/labyrinth_DWS_v2_2026-08-14.md` | The full DWS — concept, six signposts, hard rules, Garden extensibility. |
| **Design tokens** | in `viz_labyrinth.html` `<style>` | ink `#14110d` / gold `#c9a227` / gold-lit `#e6c65a` / parchment `#e8ddc7`; Cormorant/Georgia (display) + IBM Plex Mono (labels). Port these; don't invent. |

## 3. What Lovable BUILDS (the app assembly — what it's best at)
1. **The polished React app** around the kernel — clean componentry, responsive (desktop dual-immersion / tablet / mobile-inline).
2. **The "pulled-in" immersion** (§1) — vignette, center-glow, inward geometry, gentle ease-to-center, well-shaft texture. Motion-safe.
3. **The flip-card / ENCOUNTER** — front = the miniature; back = the museum label (title · culture · date · museum · license) + the scene/braid tag. Framer-Motion or CSS-3D, **≤6° tilt, slow spring**.
4. **Deep-zoom into a miniature** (v2) — OpenSeadragon + IIIF for brushwork ("zoom into the illuminated leaf").
5. **The six-signpost walk** — Nativity → Wilderness → Teaching → Signs → Passion → Resurrection; the visuals *change per signpost* (Nativity ≠ Passion).
6. **(v2) media drop-on points** — video/song/a voice reading as droppable pins on the plane; **(v2) Garden extensibility** — Paul's well, the flood-story island as new regions on the same CRS plane.

## 4. React-from-HTML guidance (don't lose the proven parts)
- **Stack:** React + **react-leaflet** (`L.CRS.Simple`) — reuse the exact map paradigm. Framer-Motion (card + gentle transitions). OpenSeadragon (v2 deep-zoom). No Three.js / no 3D camera.
- **Port, don't reinvent:** the **labyrinth-path layout** (the waypoint polyline + arc-length station sampler in the kernel's JS) and the **tile-cluster scatter** (golden-angle placement) are the one bespoke piece — lift them into a hook/util, don't re-derive. The **journey feed is the data contract** — components read `journey_gospels.json`; never hardcode tiles.
- **Render-from-data:** every tile, label, and count comes from the feed (add a signpost/tile = edit the feed or re-run the curation script; no code change). This is non-negotiable (the project's §2.16).
- **State:** selected tile (→ flip-card), current zoom (→ immersion intensity), reduced-motion (→ disable ease/animations). Keep it simple.

## 5. Hard rules (non-negotiable — from the DWS + the PI's motion-sickness catch)
- **2D only. No 3D camera, no scroll-jack, no forced parallax.** The "pulled-in" is compositional (light/vignette/geometry), never vestibular.
- **Honor `prefers-reduced-motion` globally** — every ease/vignette-shift/flip degrades to a crossfade. A crossfade is still contemplative; nausea is not.
- **Provenance = a quiet museum label**, always present per image (title · culture · date · museum · license). Never a badge, never hover-only.
- **Silence is the default soundtrack.** Any sound is opt-in ("enter with sound"), never per-image wallpaper.
- **No metrics, no urgency, no infinite scroll.** Contemplation, not engagement.
- **Land via PR; render-from-data; tokens ported, not invented.**

## 6. Success criterion
A first-time visitor **circles the gallery and feels drawn inward** — the outer signposts cool and dim, the center (the empty tomb) warm and lit — meets each moment's illuminated miniatures, turns a card over for its museum label, and arrives at the resurrection at the center. Contemplative, motion-safe, rendered from a feed any new theme can flow through. *A pilgrimage, not a slideshow.*

---

## ⟐ The precise handover (paste to Lovable)
> Build a contemplative React app: **the Gospels Labyrinth** — a pilgrimage you walk by circling *inward* toward the empty tomb. Start from the working reference `viz_labyrinth.html` (a Leaflet `CRS.Simple` pan/zoom map with a unicursal switchback path through six gospel signposts and 72 curated CC0 miniatures) and its feed `journey_gospels.json`. **Port the proven mechanics** — the labyrinth-path layout, the tile-cluster placement, the click-tile detail drawer — into React + react-leaflet; **render everything from the feed** (never hardcode tiles). Then add what you're best at: (1) the **"pulled-in" immersion** — a holy-well / tunnel feel done *compositionally* (vignette deepening toward the edges, the center cluster warm and glowing, the outer signposts cool/dim, a gentle ease-to-center on zoom-in) — **motion-safe, no 3D camera, honor `prefers-reduced-motion`**; (2) the **flip-card** (miniature front / museum label back, ≤6° tilt, slow spring); (3) responsive layout; (4) v2: OpenSeadragon deep-zoom into a leaf. Use the Garden tokens in the reference's `<style>` (ink/gold/parchment, Cormorant + Plex Mono) — port, don't invent. **Hard rules:** 2D only, no scroll-jack, provenance = a quiet museum label always present, silence is the default, no metrics/urgency. Read `lovable_labyrinth_handoff_2026-08-14.md` (this doc) + `labyrinth_DWS_v2_2026-08-14.md` first.

<!-- ── METHODOLOGY FOOTER ──
HOW PRODUCED: Design SB 2026-08-14. PI asked whether the Lovable handoff is ready (yes) + to draft the spec + precise handover
  (React-from-HTML, the READMEs/docs, the feeds), and added the design evolution: make it a REAL labyrinth that pulls you inward
  like a tunnel / holy-well entrance. This spec hands Lovable the proven kernel (viz_labyrinth.html + journey_gospels.json +
  the curation script + the Garden tokens) with precise instructions: port the proven mechanics, render-from-data, build the
  motion-safe compositional "pulled-in" immersion + flip-card + responsive app. Mirrors the dispatch-brief format (kernel + what-
  to-build + hard-rules + data-contract + a paste-ready brief).
SCHOLARLY SOURCES: labyrinth_DWS_v2_2026-08-14.md (the charter, map-paradigm, hard rules, Garden extensibility);
  viz_labyrinth.html (the kernel); journey_gospels.json + build_labyrinth_journey.py (the feed + curation); the Garden June
  moodboards (tokens); §2.16 render-from-data; §2.12 land-via-PR. The Getty-nausea motion-safety rule (the PI's own catch).
WHAT NEEDS VERIFICATION: (1) the "pulled-in" immersion must be play-tested for motion-safety (the compositional approach is the
  guard, but confirm on device). (2) OpenSeadragon deep-zoom + the Garden-region extensibility are v2. (3) when to bring Lovable
  in vs continue in-house is the PI's call; this doc makes either path ready. -->
