# Site style — one look across every posted doc

**The rule:** every HTML posted to grammarofmeaning.org links the shared stylesheet and uses its tokens — so the site looks like one thing, and the whole look is changeable from one file.

## To add a new doc
1. Copy `_template.html` → rename.
2. Keep the `<link rel="stylesheet" href="assets/gom.css">` (it gives you the palette, type, header, cards, badges, tables, channel colors).
3. Put only **doc-specific** CSS in the doc's own `<style>` — and use the shared tokens (`var(--moss-d)`, `var(--gold)`, `var(--engine)`…), never a new hard-coded palette.
4. Use the shared classes: `.gom-header` `.eyebrow` `.tagline` `.sub` `.summary` · `.card` `.card.star` · `.st ready|draft|concept|live` · `.wrap` · `.gom-foot`.

## To restyle the WHOLE site (e.g. when the final skin is chosen)
Edit the `:root` tokens in **`assets/gom.css`** once. Every doc that links it updates. No per-doc editing.

## Retrofitting the existing docs (incremental, not all at once)
The current docs carry their own inline palettes (built before the system). Convert them as each is **finalized / "marked ready"**: delete the doc's palette block, add the `gom.css` link, swap hard-coded colors for the tokens. The hub/pitch/landing are already on the garden palette, so they're closest. The schema/instruments use a different accent palette — restyle those when they're next touched.

## The skin is not locked yet
v0 of `gom.css` codifies the **garden skin** (parchment/moss/gold) — the current de-facto look. When the final skin emerges from the design-pattern prototypes / Lovable, it becomes the new `:root` in `gom.css`. The *system* (one linked sheet, token-based) is what makes that swap a one-file change.

## METHODOLOGY FOOTER
**HOW PRODUCED.** design-SB, 2026-06-17, at researcher request for a common look across all posted docs. Establishes the shared-stylesheet + template + convention so consistency is structural (and skin-swappable from one file). **SCHOLARLY SOURCES.** `assets/gom.css`; `_template.html`; the garden palette from pilgrimage_pitch_v0 + the catalog landing; Universal Principles of Design (consistency, hierarchy). **WHAT NEEDS VERIFICATION.** (1) retrofit existing docs incrementally; (2) update `:root` when the final skin locks; (3) subfolder docs adjust the `gom.css` href depth.
