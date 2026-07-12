> ## ⚠️ SOURCE-OF-TRUTH NOTICE — read before ANY bulk copy (design-SB, 2026-07-11)
>
> **This repo (`grammarofmeaning-site`) is the live site and the current source of truth.**
> The `twelve-laws:web/site-deploy/` bundle that originally seeded it (Step 1 below) is now a
> **stale, partial mirror.** As of 2026-07-11 the live repo holds **~150 files that do NOT exist
> in twelve-laws** — the entire `_staging/_mocks/` design corpus (the persona interactives:
> slot machine, space map, scrolly/board/split; plus thurman, brandmark, bakeoff, altar, companion)
> and public pages `about / essays / library / reference / romans / garden-walk` — and **~20 public
> pages have diverged**, including `method.html` (holds the live §06 flywheel), `index.html`, and
> `coding-lab.html`.
>
> **DO NOT follow the old "edit in twelve-laws, re-copy into this bundle" instruction below.**
> A wholesale copy from `twelve-laws:web/site-deploy` → here would **delete the persona suite,
> the flywheel section, and most of the site.** Edit **directly in this repo** (PR → merge; Pages
> auto-builds).
>
> **DECIDED 2026-07-11 (approved by the researcher + reading-SB): this repo is THE single source
> of truth. The `twelve-laws:web/site-deploy/` mirror is RETIRED — do not read from it, write to
> it, or deploy from it.** All site hand-offs (content drafts, gap-picker wiring, new pages) route
> to **this** repo, where design-SB deploys them — that is already the working pattern (others hand
> content to design-SB; design-SB deploys). Anything written to the old mirror silently rots, so
> nothing should be written there. Retiring/stubbing the twelve-laws mirror directory itself is a
> `twelve-laws` write owned by main-Claude (design-SB can't touch that tree); until it's stubbed,
> this notice is the guardrail.

# Deploy this bundle → grammarofmeaning.org (GitHub Pages + Cloudflare DNS)

This folder is a **self-contained static site** (the garden hub + the pitch + the
method instruments, images included). It deploys as-is — no build step.

**Why a new public repo:** `twelve-laws` is private, and free GitHub Pages needs a
**public** repo. So the site lives in its own minimal public repo; all your
research stays private.

---

## Step 1 — put this bundle in a new PUBLIC repo (~5 min)

From this folder (`web/site-deploy/`):

```bash
cd web/site-deploy
git init -b main
git add .
git commit -m "grammarofmeaning.org — v0 hub + pitch"
gh repo create grammarofmeaning-site --public --source=. --push
```
(or create `grammarofmeaning-site` on github.com manually, then `git remote add origin …` + `git push -u origin main`.)

## Step 2 — turn on GitHub Pages (~2 min)

On github.com → the new repo → **Settings → Pages**:
- **Source:** Deploy from a branch
- **Branch:** `main` · **Folder:** `/ (root)` → **Save**

It builds in ~1 min. A `CNAME` file is already in this bundle (= `grammarofmeaning.org`), so Pages will pick up the custom domain automatically once DNS resolves (Step 3).

## Step 3 — point the domain at GitHub, at Cloudflare (~10 min + propagation)

Cloudflare dashboard → `grammarofmeaning.org` → **DNS → Records**. Add the **4 apex A-records** (delete any conflicting existing A/AAAA for `@` first):

| Type | Name | Value | Proxy |
|---|---|---|---|
| A | `@` | `185.199.108.153` | **DNS only** (grey cloud) |
| A | `@` | `185.199.109.153` | **DNS only** |
| A | `@` | `185.199.110.153` | **DNS only** |
| A | `@` | `185.199.111.153` | **DNS only** |

(Optional `www`: a CNAME `www` → `<your-github-username>.github.io`, DNS only.)

> **Set proxy to "DNS only" (grey cloud), not proxied (orange).** GitHub Pages issues its own HTTPS cert; Cloudflare's proxy can block that handshake at first. You can switch to proxied later once the cert is issued, if you want Cloudflare's CDN.

## Step 4 — enforce HTTPS (~1 min, after DNS propagates)

Back in the repo's **Settings → Pages**, once the green "DNS check successful" appears, tick **Enforce HTTPS**. Done — `https://grammarofmeaning.org` is live.

---

## Notes
- **Unlisted, not secret.** `robots.txt` (Disallow: /) + `noindex` meta keep it out of search. It's a send-a-link site, not password-protected. Fine for the pitch; don't put anything truly private here.
- **What's deployed:** the hub (`index.html`), the pitch, and the method instruments (schema, influence-grammar, tree, workbench, explainer, t-stages). The **image-heavy moodboards are NOT here** (museum-image rights) — they stay local.
- **To update the site (CURRENT process, supersedes the original below):** edit **directly in this repo** via PR → merge; GitHub Pages auto-builds in ~1 min. ~~*(Original, now unsafe: "edit in twelve-laws, re-copy into this bundle" — see the SOURCE-OF-TRUTH NOTICE at the top; the twelve-laws bundle has diverged and re-copying would delete the live site.)*~~
- The **bookshelf essay-site** (`web/grammar-of-meaning/`, the S85 mock) is a *separate* surface — not deployed here. When you pick a skin, that becomes the `/essays` section.
