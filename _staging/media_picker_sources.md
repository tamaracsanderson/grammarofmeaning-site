# Media-picker source matrix — what can the picker query, and how

Reconnaissance for the multi-source media picker (`viz_media_picker.html`). A source is usable **directly** from the client-side page only if it is BOTH keyless AND CORS-enabled (sends `access-control-allow-origin`) AND serves images that load cross-origin. Anything failing one of those needs the **proxy** (a small server-side Cloudflare Worker that holds keys + adds CORS).

Verified 2026-08-13 (design-SB, server-side curl with a foreign `Origin`/`Referer`).

## Tier 1 — DIRECT (keyless + CORS + cross-origin images) — live now / ready

| Source | Search endpoint | Keyless | CORS | Images x-origin | License handling | Status |
|---|---|---|---|---|---|---|
| **Cleveland Museum of Art** | `openaccess-api.clevelandart.org/api/artworks/?q=` | ✓ | `*` | ✓ | CC0 filter (`share_license_status`) | **shipped** |
| **The Met** | `collectionapi.metmuseum.org/.../search` → per-object | ✓ | ✓ | ✓ | `isPublicDomain` filter | **shipped** |
| **Wikimedia Commons** | `commons.wikimedia.org/w/api.php` (generator=search) | ✓ | `*` | ✓ | PD/CC0 filtered (drops CC-BY-SA) | **shipped** |
Rijksmuseum was investigated for Tier 1 and **deferred** — see below.

## Tier 2 — VIA PROXY (needs the Worker: key and/or CORS)

| Source | Why proxy | Keyless? | Notes |
|---|---|---|---|
| **Cooper Hewitt** | **no CORS header** (blocks browser POST) | keyless | GraphQL; `object(general:"…", hasImages:true)`; `multimedia[].cc0` flag; `preview`/`large` S3 URLs load x-origin; max query depth 2, `summary`/`multimedia` are scalars |
| **Smithsonian Open Access** | key | keyed (`SMITHSONIAN_API_KEY` in `.env`) | huge CC0 collection |
| **Europeana** | key | keyed (`EUROPEANA_API_KEY` in `.env`) | aggregates dozens of EU collections |
| **DPLA** | key | keyed (`DPLA_API_KEY` in `.env`) | aggregates dozens of US collections |
| **Harvard Art Museums** | key | keyed (key request submitted) | medieval / Islamic / manuscript strength |

## The linchpin insight

The **proxy solves TWO problems at once**, not just one:
1. **Hides keys** — the key lives in the Worker's env, never in the public page.
2. **Adds CORS** — the Worker echoes `access-control-allow-origin`, so even a *keyless* no-CORS source (Cooper Hewitt) becomes browser-callable.

So one small Cloudflare Worker unlocks Cooper Hewitt + Smithsonian + Europeana + DPLA + Harvard together. The picker's `SOURCES` adapter array already supports adding them as normalized modules; each Tier-2 source becomes `fetch(WORKER_URL + "?source=cooperhewitt&q=…")`.

## Deferred from the live picker

- **Rijksmuseum Search API** (`data.rijksmuseum.nl/search/collection`) — keyless + CORS `*` + JSON, so it *technically* qualifies, BUT the image is **four hops deep** in the Linked-Art graph: search → object URI → resolve → `shows` VisualItem URI → resolve → `digitally_shown_by` DigitalObject URI → resolve → IIIF `access_point`. That's ~4 content-negotiation resolves per result (≈25 requests to render 8 thumbnails), relevance on `description=` is loose (a "resurrection" search surfaced a Saenredam architectural interior), and — decisively — **Rijksmuseum is already coming in via OAI-PMH on the library side**, so a heavy live-picker path would be redundant. Deferred: Rijksmuseum's route in is the library harvest; the picker reaches it later via step-2 (library-complement).

## Not for the picker (library lane)

- **Rijksmuseum OAI-PMH** (`data.rijksmuseum.nl/oai`) — keyless, CORS `*`, XML, but a *bulk-harvest* protocol (no keyword search). Handed to the Librarian as a CRADLE harvest feed (§2.10) → becomes library content → the picker's eventual "step 2" (library-complement) draws on it. **This is Rijksmuseum's route in.**

---

<!-- METHODOLOGY FOOTER
HOW PRODUCED: design-SB 2026-08-13, PI-driven multi-source media-picker expansion. The PI fed museum-API docs
  (Rijksmuseum Search/SRU/IIIF/OAI-PMH; Cooper Hewitt GraphQL) mid-session; each was probed server-side (curl with
  foreign Origin/Referer) for keyless + CORS + cross-origin-image viability. Captured here (§2.13 single-store) so the
  recon is a durable artifact, not chat-only — the "which source, and how" question has one answer of record.
SCHOLARLY SOURCES: §2.16 render-from-data (picker keywords/themes derive from the passage); §2.13 single-store;
  §2.10 CRADLE (Rijksmuseum OAI-PMH → library lane); IMAGE-CREDITS.md (the Lovable API index this extends).
WHAT NEEDS VERIFICATION: (1) Rijksmuseum image path (shows→VisualItem→IIIF) before it joins Tier 1. (2) Cooper Hewitt
  via the Worker (GraphQL POST passthrough). (3) Smithsonian/Europeana/DPLA query shapes + image fields once the
  Worker is live. (4) whether Wikimedia's occasional geo-wrong hits (Ming tombs) want a stricter query.
-->
