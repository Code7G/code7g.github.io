# code7g.github.io

The Code7G website, served by GitHub Pages from `main`. Plain HTML and one CSS file, with no build step, trackers or external requests.

## Layout

- `index.html`: home page
- `apps/index.html`: all apps, one card each
- `apps/<app>/index.html`: one page per app
- `apps/<app>/privacy/index.html`: that app's privacy policy
- `privacy/index.html`: list of all privacy policies
- `404.html`: shown for any missing page (its links are absolute because it can be served at any depth)
- `assets/css/site.css`, `assets/js/site.js`, `assets/favicon.svg`: shared by every page
- `assets/img/<app>/`: `icon.webp` (256 px), store screenshots (540 x 960 WebP) and `feature.webp`

Keep these files exactly as they are: `app-ads.txt` (AdMob), `google298c2faf006c294c.html` (Search Console) and `robots.txt`.

## Adding an app

1. Copy `apps/square-race/` to `apps/<new-app>/` and change the text, images and links.
2. Add its images to `assets/img/<new-app>/`, resized to the sizes above.
3. Add a card to `apps/index.html` and `index.html`.
4. If it has a privacy policy, add `apps/<new-app>/privacy/index.html` (copy an existing one) and list it in `privacy/index.html`.
5. Add the new URLs to `sitemap.xml`.

## Preview locally

From this folder: `python -m http.server 8000`, then open http://localhost:8000/.
