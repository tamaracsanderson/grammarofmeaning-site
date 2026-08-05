# Lovable → static-site handoff — paste-ready query template

**Purpose.** A Lovable mock is a *running React app*; grammarofmeaning.org is *static HTML*. design-SB rebuilds the mock as static pages. The translation is near-1:1 when the mock separates **content (data) · presentation (components) · tokens (theme)** — and painful when content is baked inside `.tsx` components. This template is what the PI pastes to Lovable (at project start, or when asking it to prep a handoff) so the export drops straight into design-SB's render-from-data architecture.

Maintained by design-SB · referenced in the DWS (`engine/data/dws_status.json`) · source memory `reference_lovable_mock_handoff_files.md`.

---
═══════════════════════════════════════════════════════════════
PASTE-START — copy from here to PASTE-END into Lovable
═══════════════════════════════════════════════════════════════

When this design is ready to hand off, please produce the following so a developer can rebuild it as a **static site** with minimal friction. The guiding principle: **keep content, presentation, and design tokens in separate files** — never bake content or styling constants inside the components.

1. **HANDOVER.md** — a short design-decisions doc:
   - the **default / production** direction (what actually ships)
   - what is **LOCKED** vs. what is a **BACKUP / alternate** (keep, don't promote)
   - the **key files** and what each holds
   - any **implementation notes** and **"do not change" rules**

2. **Content as DATA, not hardcoded** — put every piece of content (lists, items, captions, copy, labels, refs, any repeated structured data) in a **single JSON file or a `/data` folder** that the components read from. Do **not** embed content inside `.tsx` components.

3. **A theme / tokens file** — all design tokens in one place: color palette (hex), fonts, any shared text-shadow / effects, spacing scale, radii, breakpoints. A `tokens.json`, a theme object, or a CSS `:root` block — whichever is cleanest.

4. **IMAGE-CREDITS.md** *(only if the design uses curated media)* — per-asset provenance:
   - source, **license** (e.g. public-domain / CC0), and the **canonical URL or object ID**
   - which assets are **externally sourced** vs. **project-rendered/owned**
   - **rules of engagement**: "these were chosen deliberately — don't swap or regenerate them; crops are intentional (tune, don't reset); if a URL breaks, re-fetch the **same** object, don't substitute a different one."

5. **An INTERACTIONS note** *(one paragraph, can live inside HANDOVER)* — what animates and how: rotation / shuffle cadence, transition durations, scroll behavior, hover / crop mechanics, responsive breakpoints. A static rebuild loses behavior unless it's written down.

Please keep **content (data)**, **presentation (components)**, and **tokens (theme)** in separate files — that separation is exactly what makes the design portable to a static build (and it's good practice in Lovable regardless).

═══════════════════════════════════════════════════════════════
PASTE-END — stop copying here
═══════════════════════════════════════════════════════════════
---

## How to adapt per project
- **No curated media?** Drop #4.
- **Purely static / no animation?** Drop #5 (or note "no interactions").
- **Tiny mock?** #1 (HANDOVER) + #2 (content-as-data) are the non-negotiables; the rest are bonuses.
- **The magic short form** if you only say one sentence: *"Give me a HANDOVER.md and an IMAGE-CREDITS.md, and put all content + design tokens in separate data files, not hardcoded in the components."*

## What design-SB does on receipt
1. Read **HANDOVER.md first** (before anything else).
2. Consume the **DATA file** directly as a render-from-data source (or run an extractor if content is still in components — see `_scripts/extract_gospels_room_config.py` for the worked example).
3. Match the look from the **tokens file**; honor **IMAGE-CREDITS** rules (preserve assets + crops, re-fetch same object on 404).
4. Build to a **staging URL** → PI eyeballs the feel → flip to live.
5. Record the mock's location + the config in the **DWS** so it's never "lost."

<!--
HOW PRODUCED: design-SB S161 (2026-08-05), at the PI's request to turn the "what files make a Lovable mock easy to pick up?" learning into a reusable paste-ready template stored on the DWS, so future Lovable queries start from it. Distilled from the gospel-depths-explorer handoff (HANDOVER.md + IMAGE-CREDITS.md were gold; content-in-components forced an extractor).
SOURCES: reference_lovable_mock_handoff_files.md (memory); the gospel-depths-explorer mock; CLAUDE.md §2.16 (render-from-data), §2.13 (single store); the IRR PASTE-START/END marker convention (§2.6) reused here for copy-clarity.
WHAT NEEDS VERIFICATION: firms up as more Lovable mocks exercise it — e.g. whether a standard tokens-file shape emerges worth naming.
-->
