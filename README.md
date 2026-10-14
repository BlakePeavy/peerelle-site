# Peerelle website (peerelle.app)

Static marketing and compliance site for **Peerelle** - local-first guided rental-vehicle photo capture for hosts and renters.

No build step. No framework. Open any `.html` file or serve the folder as static files.

## Contents

| File | Purpose |
|------|---------|
| `index.html` | Landing |
| `privacy.html` | Privacy Policy (store URL) |
| `support.html` | Support + FAQ (store URL) |
| `terms.html` | Terms of Use |
| `404.html` | Custom not-found page |
| `styles.css` | Shared styles (source; run `python3 tools/inline-css.py` to inline into pages) |
| `favicon.svg` | Teal lens mark |
| `CNAME` | Custom domain `peerelle.app` |
| `robots.txt` | Allow crawlers |
| `LISTING.md` | Play / App Store listing copy |

## Publish with GitHub Pages

1. Create a GitHub repository (e.g. `peerelle-site` or `peerelle.app`).
2. Push this folder to the `main` branch (as the repo root, or into `/docs`).
3. In the repo: **Settings → Pages**.
 - **Source:** Deploy from a branch.
 - **Branch:** `main`, folder **`/ (root)`** if these files are at the repo root, or **`/docs`** if you placed them under `docs/`.
4. After the first deploy, GitHub assigns a `*.github.io` URL. Custom domain steps below.

Store URLs once live:

- Privacy: `https://peerelle.app/privacy.html`
- Support: `https://peerelle.app/support.html`

## Custom domain (peerelle.app)

This repo includes a `CNAME` file with exactly:

```
peerelle.app
```

### DNS at your registrar

Pick one approach:

**Apex (`peerelle.app`) - recommended A/AAAA records for GitHub Pages**

Use GitHub’s current Pages IPs (confirm in [GitHub Docs: managing a custom domain](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)):

- `A` → `185.199.108.153`
- `A` → `185.199.109.153`
- `A` → `185.199.110.153`
- `A` → `185.199.111.153`
- Optional IPv6: GitHub’s published `AAAA` values for Pages

**Or** a `CNAME` for `www` (e.g. `www.peerelle.app` → `YOURUSER.github.io`), and redirect apex → www (or the reverse) per your DNS host.

Then in GitHub Pages settings:

1. Set **Custom domain** to `peerelle.app`.
2. Wait for DNS to verify.
3. Enable **Enforce HTTPS**.

DNS can take minutes to hours to propagate.

## Email: support@peerelle.app

App stores and the site list **`support@peerelle.app`**. Set up **email forwarding** (or a mailbox) at your domain host so that address reaches a monitored inbox. The static site only provides `mailto:` links; it does not send or receive mail.

## Local preview

```bash
cd peerelle-site
python3 -m http.server 8080
# open http://localhost:8080
```

## Design notes

- Teal accent `#0D9488` on cream/white
- Andika (Google Fonts) with system-ui fallback
- Mobile-first, accessible landmarks, skip link, focus styles
- App Store / Play badges on the landing page are placeholders (`#`, disabled) until the apps are live

## License / affiliation

Peerelle is an independent tool and is not affiliated with Turo or any insurer. See `terms.html`.
