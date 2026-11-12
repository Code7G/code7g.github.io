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
- `assets/img/code7g/`: the Code7G logo. `logo-source.png` is the original (460 px, the GitHub avatar); `apple-touch-icon.png` (180 px) is made from it and linked from every page. The favicon and the header mark are a "7G" tile in the logo's gradient, because the full "code7G" text can't be read at 16 to 30 px.
- `assets/img/<app>/`: `icon.webp` (256 px), store screenshots (540 x 960 WebP) and `feature.webp`. G7Keyboard's are PNG at the same sizes (made without an image library, see below); converting them to WebP later is fine, just update the links.
- Colours: sampled from the logo, aqua `#1ff2cb` (top-left) to purple `#b260ee` (bottom-right). These are `--logo-*` in `site.css` and the stops in `favicon.svg`, and are used only where nothing has to be read on them (logo mark, favicon, glows, card hover border, button glow). White text on a gradient uses `--grad-*` (`#08826b` to `#a23fea`), gradient text on the light background uses `--text-grad-*` (`#077c66` to `#9d35e9`) and light-mode links use `#8918dd`: deeper shades of the same two hues that pass WCAG AA. In dark mode the headline gradient and links use the logo colours themselves.
- Animations: scroll reveal (in `site.js`), hero headline shimmer, hero icon float, card and button hover. All of them are off when the visitor's system asks for reduced motion.
- `tools/check_links.py`: offline check of every link, image and anchor (see below)
- `PUBLISH-NOTES.md`: the public URL of each privacy policy, for Play Console

Keep these files exactly as they are: `app-ads.txt` (AdMob), `google298c2faf006c294c.html` (Search Console) and `robots.txt`.

## Adding an app

1. Copy `apps/square-race/` to `apps/<new-app>/` and change the text, images and links.
2. Add its images to `assets/img/<new-app>/`, resized to the sizes above.
3. Add a card to `apps/index.html` and `index.html` (and its icon to the home page's `hero-art` block if it is live). Once it's on Google Play, set its status to `status-live` "On Google Play" and add the "Get it on Google Play" button on its page.
4. If it has a privacy policy, add `apps/<new-app>/privacy/index.html` (copy an existing one) and list it in `privacy/index.html`.
5. Add the new URLs to `sitemap.xml`, and any new privacy policy URL to `PUBLISH-NOTES.md`.
6. Run `python tools/check_links.py` and fix anything it reports.

## Preview locally

From this folder: `python -m http.server 8000`, then open http://localhost:8000/.

## Checking links

`python tools/check_links.py` reads every `.html` file and reports links or images that point to a missing file, `#anchors` with no matching id, images without `alt` or `width`/`height`, unknown `mailto:` addresses and em-dashes. External links are only listed, not fetched. It exits with 1 when something is wrong.

## Images without an image library

G7Keyboard's screenshots and icon were downscaled from its store-listing PNGs with a small pure-Python script (zlib only, 2x box filter), because no image tool was available when they were added. Any tool that writes 540 x 960 images works the same.
