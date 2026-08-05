# DWS — Design Work-State (design-SB SSOT)

**Read this first if you are a new design-SB.** It + the two JSON artifacts below tell you the whole render layer without archaeology.

- **`engine/data/dws_manifest.json`** — AUTO-generated (`_scripts/build_dws_manifest.py`): every page → the data it `fetch()`es → which SB owns that data → where it lives in twelve-laws. Re-run the scanner whenever a page's fetches change or a new data file is mirrored; it flags any `unmapped` fetch (a drift-detector).
- **`engine/data/dws_status.json`** — hand-maintained: the open threads (what's waiting on whom) + the conventions. Edit when a thread opens/closes.
- **Watchable page:** `/engine/design-state.html` (noindex) renders both — the PI author-watches this, parallel to reading-SB's `schema.html` (IWS) and the Librarian's `library-schema.html` (LWS).

---

## 1. What design-SB is

The **render layer**. design-SB does **not** author content — reading-SB authors the method, the Librarian authors the library; design-SB **renders every drawer and page from their DATA exports**, and owns the deploy repo.

- **Owns:** `grammarofmeaning-site` (this repo) — the deployed site at grammarofmeaning.org. Self-merges its own site PRs.
- **Read-only on `twelve-laws`:** `git fetch` + `git show origin/main:…` only — never writes there. (That's why this SSOT lives in the deploy repo, not Obsidian; the watchable page is how the PI sees it.)

## 2. The 3-way ownership model

| SB | SSOT page | Owns (exports the SSOT-accurate DATA) |
|---|---|---|
| **reading-SB** | `schema.html` (IWS · the Method) | Resituate · method · coded-move data |
| **Librarian** | `library-schema.html` (LWS · the Library) | Frame / atlas / morphospace · library data |
| **design-SB** | `design-state.html` (DWS · this) | renders EVERY page from those exports |

The rule that keeps drawers from drifting: **one owner-SB produces the render-from-data DATA export (SSOT-accurate) + flags current-vs-stale; design-SB renders from it; the Librarian runs off the latest.** Never hand-author a drawer's content — mirror the export and render it.

## 3. The workflow (one loop)

```
owner-SB exports DATA on twelve-laws main
   → design-SB:  git show origin/main:<path> > engine/data/<X>.json     (mirror — pure data swap)
   → the page fetch()es /engine/data/<X>.json and renders it            (render-from-data)
   → design-SB: commit + PR + `gh pr merge --merge` (self-merge)         (deploy)
   → curl-verify the live artifact + page
```

Re-run `python3 _scripts/build_dws_manifest.py` after any new mirror so the manifest stays true.

## 4. Conventions (the non-negotiables)

- **Render-from-data, never hardcode (§2.16).** If a page can't render from a mirrored artifact yet, that's a *flagged gap*, not licence to hardcode. (The cautionary tales: the `MS_PTS` morphospace fork ×15; the "38 moves → 151 gaps" hard-typed tile.)
- **`schema.html` is the flagship — the PI author-watches it.** Change it ONLY via **fail-safe monkey-patches** in an isolated `<script>` block: main script stays byte-identical; `typeof`-guards + `try/catch` → fall back to the prior render, so an error can never blank the page. Never hand-edit the ~175KB single-line `const P` blob.
- **Offline validation (no pane needed for static pages):** regex-aware JS balance scan + replay the render logic against the real data in Python + curl the deployed file; confirm **zero bracket-delta vs known-good HEAD**. This is how the drawers / moves.html / the insight strip shipped without a working pane.
- **Pane-gated** = scroll/drag/step interaction that only exists live and can't be verified offline. Build those with a live browser (design-SB's pane, or the PI as eyes). Everything else is offline-validatable.

## 5. How to hand over

1. Read this doc.
2. Read `dws_manifest.json` → you know every page + its data sources + owners.
3. Read `dws_status.json` → you know what's open and who it's waiting on.
4. `git log --oneline` in this repo → the detailed trail (each PR's commit message says exactly what shipped + why).

That's it — no need to reverse-engineer the render layer from the pages.

---

<!--
HOW PRODUCED: design-SB, 2026-08-05, at the PI's request ("what do you want the SSOT to be, and how are you documenting, so handover to a new SB is easy?"). Named DWS (Design Work-State) parallel to IWS (reading/schema.html) + LWS (library/library-schema.html).
SCHOLARLY SOURCES: CLAUDE.md §2.16 (SSOT / render-from-data), §2.13 (single store of record), §2.7 (documented≠enforced — the manifest's unmapped-flag is the enforcement layer); reading-SB's 3-way ownership proposal (S160).
WHAT NEEDS VERIFICATION: dws_status.json open_threads are hand-maintained — keep them current; the manifest auto-detects fetch drift but owner/source mapping (MIRROR_MAP) is hand-kept; a few twelve-laws source paths in the map are marked "verify".
-->
