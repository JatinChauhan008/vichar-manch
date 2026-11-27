# Vichar Manch website

Static website for Vichar Manch (nukkad natak / street theatre).

## Layout

| Path | What it is |
| --- | --- |
| `build_site.py` | Generates every page. All content (text, services, videos, clients) lives in its data section. |
| `site/` | The generated website — this folder is what gets published. Do not hand-edit; re-run the build. |
| `source-material/` | Original photos and PDFs supplied for the site. Not published. |
| `.github/workflows/pages.yml` | Deploys `site/` to GitHub Pages. |
| `netlify.toml`, `wrangler.jsonc` | Same `site/` folder, published on Netlify and Cloudflare Workers. |

## Editing

```
python build_site.py
```

Then commit `build_site.py` and `site/` and push to `main`. Every host redeploys from `site/`.

Preview locally:

```
python -m http.server 8765 --directory site
```

## GitHub Pages

All links in `site/` are relative, so the site works at the project URL
(`https://jatinchauhan008.github.io/vichar-manch/`) or on a custom domain.
Custom domain: **vicharmanchnukkadnatak.in** (set in Settings → Pages).

One-time setup: **Settings → Pages → Build and deployment → Source: GitHub Actions**.
After that, each push to `main` that changes `site/` publishes automatically
(or run the workflow by hand from the Actions tab).

If GitHub Pages becomes the main address, set `SITE_URL` in `build_site.py`
to the Pages URL (or custom domain) and rebuild, so canonical links,
the sitemap and `robots.txt` point to it.
