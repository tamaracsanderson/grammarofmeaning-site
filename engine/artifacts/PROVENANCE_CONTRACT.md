# The provenance render-contract

**PI-directed, S156 (trust-critical).** The site must **render from real engine data, never hardcode its own version of a reading.** Every displayed reading — moves, gaps, frames, coordinates, gloss — must trace to a real DB row / engine artifact. **If a reading is not engine-grounded, it renders as DRAFT (visibly marked) or not at all.** Essay-SB polish is welcome and wanted — as a *styling* layer **on** the engine's data, never as authored substance.

`coded_ledger.json` is the ground-truth check: if a `source_key` isn't in the ledger (with counts), its "reading" isn't grounded.

## How a reading declares its source

Include the helper once per page:

```html
<script src="/engine/artifacts/provenance.js"></script>
```

Declare the source on any reading element:

```html
<!-- badge appended to the element -->
<div data-prov-source="MATT-28"> … the reading … </div>

<!-- badge placed into an explicit slot -->
<div data-prov-source="JOHN-20">
  <span data-prov-slot></span>
  … the reading …
</div>

<!-- require a non-zero count of a kind (moves | gaps | gloss_rows) to count as grounded -->
<div data-prov-source="BRAID-RESURRECTION" data-prov-need="gaps"> … </div>
```

The helper derives the badge from the ledger:

| condition | render |
|---|---|
| `source_key` in `coded_ledger.json` (and `data-prov-need` count > 0, if set) | green **provenance line** — `source: coded_ledger · KEY · N moves` |
| `source_key` **not** in the ledger | amber **DRAFT · not engine-grounded** badge |
| ledger unreachable | **DRAFT** (fail-safe — never render as grounded unverified) |

Dynamically-injected readings (rendered after page load): call `window.Provenance.rescan()` after injecting them. `window.Provenance.check(source_key)` returns the ledger entry or `null`.

## Why this can't regress

A reading with no `data-prov-source`, or one whose declared key isn't in the ledger, cannot show a grounded badge — it shows DRAFT. So a hand-authored reading can't silently pass as coded, and a reading auto-flips to grounded the moment its source lands in the ledger (no code change). This is the structural form of CLAUDE.md §13 (no fabricated provenance) at the render layer.

## Adoption checklist (for each reading surface)

1. Include `provenance.js`.
2. Give every reading container a `data-prov-source` = its real `source_key` (+ `data-prov-need` if a gap/gloss count is what makes it a "reading").
3. If the reading is injected dynamically, call `Provenance.rescan()` after injection.
4. If a reading is hand-authored / reasoning-mode (not in the ledger), it will render DRAFT — that is correct; ground it (add it to the coded corpus so it enters `coded_ledger.json`) to make it render coded.

## Current state (S156)

- **Grounded (render provenance line):** the four gospel accounts in the reading-room Compare (`MATT-28`, `MARK-16`, `LUKE-24`, `JOHN-20`), and the other 31 ledger sources.
- **DRAFT (not in ledger):** `BRAID-RESURRECTION` — the braided reading's composite-gap gloss is reasoning-mode (hand-authored); grounding via the #20 cross-source scanner is queued for S157. When it lands in the ledger, the rail badge auto-flips to grounded.
- The data-driven viz already fetch named real artifacts (coded_ledger, gaps→answers with its grounding_key + grounded/inferred tags, the MCA data, provenance) — those declare their source by construction.
