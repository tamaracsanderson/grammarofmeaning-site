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
- **Latest-run data, never stale — the read-rule (avoid the *old-data problem*).** Old visualizations / DRs / comparisons (partiture, translation, sonic constellation, etc.) are **reference for the APPROACH only**. The DATA you render is ALWAYS the **latest run** of the feed — filter to the current grammar version's latest run; never a bare `source_key` or an old run's frozen output. Reusing a stale run's output is the old-data problem (the **M56–M60** case: a figure fed by a 55-move `moves.json` while the edges were coded on the 60-move run). If a brief's or handover's data-claim conflicts with what's actually on `main`, **trust the data and correct the brief** (§2.16) — never build on the stale claim.

## 5. How to hand over

1. Read this doc.
2. Read `dws_manifest.json` → you know every page + its data sources + owners.
3. Read `dws_status.json` → you know what's open and who it's waiting on.
4. `git log --oneline` in this repo → the detailed trail (each PR's commit message says exactly what shipped + why).

That's it — no need to reverse-engineer the render layer from the pages.

---

## 5b. Session cadence — the handover discipline (keep the DWS current)

design-SB is a **render layer**, so it does NOT run main-Claude's full standup/standdown ritual (no PROJECT_TRACKER, no ratio-retrospective, no thesis-arc framing — none of that applies). But it keeps the **same rigor** as the other SBs via one light, consistent loop, because the SSOT is only as good as its currency (the tell: `deploy_status` had gone stale Aug-6 → Aug-10 because updates were ad-hoc).

**STANDUP (session start, ~2 min):**
1. Read this doc §6 (current focus) + `dws_status.json` `open_threads[0]` (the latest record + its `note_for_next_llm` kickoff).
2. Read the relevant SSOT page(s) for what you're building — the drawer / engine schema (§2.16: orient from the SSOT, not memory or an LLM-written brief).
3. **Confirm LIVE state before building** (curl / browser). Never trust a status field.

**WHEN TO CLOSE (don't stop at a convenient checkpoint — PI directive 2026-08-11):** STAY OPEN and work the queue. Close only when (a) the work is genuinely COMPLETE, (b) every remaining item is BLOCKED (data / PI-input / another SB), or (c) the PI signals close. Do NOT close while buildable-now, unblocked work remains just because you hit a clean arc boundary — press through it (*"holding is like ending early"*). When you finish an item, update the DWS and move **straight to the next queued item**; a full closing standdown fires only at a genuine stop. Keep a **WORK-QUEUE** in the active thread's `note_for_next_llm` and work it in order, flag-and-skipping blocked items (note the block + ping the owner, then continue).

**STANDDOWN (at a genuine close — ALWAYS, not only when the PI asks):**
1. Update `dws_status.json`: `open_threads` (what shipped · what's now blocked/owed · on-whom), `last_updated`, un-stale `deploy_status`. Prepend a new dated thread for a substantial session.
2. Update `design_engine.json` node statuses (built / blocked) for any figure touched.
3. Write the paste-ready next-chat **KICKOFF** as that thread's `note_for_next_llm`.
4. Commit + push (deploy) — the DWS page re-renders.

**HANDOVER:** hand the PI the paste-block kickoff (lifted verbatim from the thread's `note_for_next_llm`) to open the next chat — same shape as main-Claude's handover.

**Chat hygiene:** a single chat can span the whole queue — keep going as long as it's productive (the default now, per WHEN TO CLOSE). Start a **fresh chat only** when the chat has grown long enough to drift OR a genuinely new arc begins — NOT after every small build. The standdown is what makes a fresh chat cheap on the occasions you do need one.

This matches the other SBs' rigor (IWS/LWS keep their schema pages current; design-SB keeps the DWS current) without the research-arc overhead a render layer doesn't need.

---

## 6. Current focus (updated 2026-08-11 · S169)

**The reading figures** (Grammar of Meaning reading room) are the active build — all render-from-data, reader-first, staged (`_staging/`, noindex):

- **Move Score v1** (`_staging/viz_move_score_v2.html`) — the Decompose figure (Mark 16:1–20), **DONE**. v2 enhancements (post-Situate-data) in `_staging/move_score_v2_backlog_2026-08-10.md`.
- **Plate v1** (`_staging/viz_plate.html`) — the Text figure, reader-first.
- **Connect figures v2 — P1 + P2(phase 1) SHIPPED (S169, verified live).** The 3 figures (`viz_connect_arcband/loom/topology.html`) are relabelled Trace / Scan / Map and now render the **real 5 `edge_kind`s** (LINKAGE/LINEAGE/RESONANCE/SHAPE/SONIC) from **one shared source** — `engine/connect_core.js` + `engine/data/connect_taxonomy.json` (render-from-data, §2.16; fixes the S168 invented-3-family error). Adds: 5-kind colour key (SHAPE corrected gold→olive), sub-type drill-down with live counts, declared-but-absent kinds (LINEAGE/RESONANCE/SONIC show 0 in the WEB feed; SONIC → "on the Plate"), plain-language relation cards (NEST_REPORTS → "the speech reported inside M3"), honest drop-note. **P2 phase 1**: a shared Trace/Scan/Map view-switch + **selection & filter state carried in the URL hash**, so a selected move survives the switch (verified: select M12 in Trace → Scan opens with M12 selected + same filters). Separate deep-linkable URLs kept (per the lock).
- **method-engine.html** — Connect = one node like Decompose (unchanged from S168).

**Next Connect builds (deferred):** **P3 (DATA-BLOCKED)** — sonic-on-the-Plate (word-level, `pronouncing`+`panphon`) + the EN↔GRC comparison (GRC edges exist, 79, unexported) — waits on Method SB feeds. **P2 remainder** — the Move Score → Connect tie (#7) + the 60-sec "same relation, three views" worked example (#10); optional full single-page SPA shell (zero-reload). Spec: `_staging/connect_v2_reconciliation_2026-08-10.md`. See `dws_status.json` open_threads[0] for the full record + next-chat kickoff.

**Browser pane:** WORKING this session (unlike S168) — all figures verified with live DOM inspection + screenshots.

---

<!--
HOW PRODUCED: design-SB, 2026-08-05, at the PI's request ("what do you want the SSOT to be, and how are you documenting, so handover to a new SB is easy?"). Named DWS (Design Work-State) parallel to IWS (reading/schema.html) + LWS (library/library-schema.html).
SCHOLARLY SOURCES: CLAUDE.md §2.16 (SSOT / render-from-data), §2.13 (single store of record), §2.7 (documented≠enforced — the manifest's unmapped-flag is the enforcement layer); reading-SB's 3-way ownership proposal (S160).
WHAT NEEDS VERIFICATION: dws_status.json open_threads are hand-maintained — keep them current; the manifest auto-detects fetch drift but owner/source mapping (MIRROR_MAP) is hand-kept; a few twelve-laws source paths in the map are marked "verify".
-->
