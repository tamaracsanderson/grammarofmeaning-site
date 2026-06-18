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
- **To update the site:** edit in `twelve-laws` (the source of truth), re-copy into this bundle, push to `grammarofmeaning-site`. Or later: wire Cloudflare Pages git-connect for auto-deploy.
- The **bookshelf essay-site** (`web/grammar-of-meaning/`, the S85 mock) is a *separate* surface — not deployed here. When you pick a skin, that becomes the `/essays` section.
