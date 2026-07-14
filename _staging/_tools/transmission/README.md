# transmission-structure.html — builder + feed (design-SB, internal)

Regenerate the case-study page:
    python3 build_transmission.py feed_enriched.json ../../../transmission-structure.html

- `feed.json` — reading-SB's v1 seven-figure coordinate feed (DATA_seven_figures_coordinates_for_designSB_2026-07-14).
- `feed_enriched.json` — v1 + the V13–V15 framer enrichment (built by enrich_feed.py from the HANDOFF table).
- `enrich_feed.py` — applies reading-SB's V13–V15 framer data + `mystical` flags to the v1 feed.
- `build_transmission.py` — seed-agnostic + idempotent HTML builder (spectrum + interactive A/B stage + cards).

When reading-SB emits the official per-framer JSON, replace feed_enriched.json (or point the builder at it) and re-run.
View C (reception era-axis) is intentionally NOT built — gated on reading-SB's per-tradition periodizations (IRR192: multi-clock, not a single Küng line).
