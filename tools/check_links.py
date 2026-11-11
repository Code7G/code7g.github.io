"""Check every link and image in the site's HTML files, offline.

Run from anywhere: python tools/check_links.py
Exits with 1 if anything is broken. External links are listed, not fetched.

Checks:
- href/src that point inside the site resolve to an existing file (a folder means its index.html),
  including absolute https://code7g.github.io/ URLs and root-relative "/..." links.
- "#fragment" targets exist as an id on the target page.
- mailto: links use one of the known contact addresses.
- every <img> has an alt attribute and width/height, and its file exists.
- no page contains an em-dash (U+2014).
"""
import os
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://code7g.github.io"
# Motivational Alarm keeps its own support address.
ALLOWED_MAIL = {"coder.7g@gmail.com", "contact.motivationalalarm@gmail.com"}
EM_DASH = chr(0x2014)


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []  # (attr, value, line)
        self.ids = set()
        self.img_problems = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        line = self.getpos()[0]
        if "id" in a:
            self.ids.add(a["id"])
        for attr in ("href", "src"):
            if a.get(attr):
                self.links.append((attr, a[attr], line))
        if tag == "meta" and a.get("property") == "og:image":
            self.links.append(("content", a.get("content", ""), line))
        if tag == "img":
            if "alt" not in a:
                self.img_problems.append((line, "img without alt"))
            if not a.get("width") or not a.get("height"):
                self.img_problems.append((line, "img without width/height"))


def html_files():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if not d.startswith(".")]
        for f in filenames:
            if f.endswith(".html"):
                yield os.path.normpath(os.path.join(dirpath, f))


def resolve(page_path, url):
    """Return the local file a site-internal URL points to, or None for external URLs."""
    parts = urlsplit(url)
    if parts.scheme in ("http", "https"):
        if not url.startswith(SITE):
            return None
        base = ROOT
    elif parts.scheme:
        return None
    else:
        base = ROOT if parts.path.startswith("/") else os.path.dirname(page_path)
    path = unquote(parts.path)
    if path == "":
        return page_path
    target = os.path.normpath(os.path.join(base, path.lstrip("/")))
    if path.endswith("/") or os.path.isdir(target):
        target = os.path.join(target, "index.html")
    return target


def main():
    pages, problems, external = {}, [], set()
    for path in html_files():
        p = Page()
        text = open(path, encoding="utf-8").read()
        p.feed(text)
        pages[path] = p
        if EM_DASH in text:
            problems.append((path, 0, "contains an em-dash"))
        for line, msg in p.img_problems:
            problems.append((path, line, msg))

    for path, p in pages.items():
        for _attr, url, line in p.links:
            if url.startswith("mailto:"):
                addr = url[7:].split("?")[0]
                if addr not in ALLOWED_MAIL:
                    problems.append((path, line, f"unexpected mail address {addr}"))
                continue
            target = resolve(path, url)
            if target is None:
                external.add(url)
                continue
            if not target.startswith(ROOT):
                problems.append((path, line, f"{url} points outside the site"))
                continue
            if not os.path.isfile(target):
                problems.append((path, line, f"{url} -> missing {os.path.relpath(target, ROOT)}"))
                continue
            frag = urlsplit(url).fragment
            if frag and target.endswith(".html") and frag not in pages.get(target, Page()).ids:
                problems.append((path, line, f"{url}: no id '{frag}' on target page"))

    print(f"Checked {len(pages)} pages.")
    print(f"External links ({len(external)}, not fetched):")
    for u in sorted(external):
        print("  " + u)
    if problems:
        print(f"\n{len(problems)} problem(s):")
        for path, line, msg in problems:
            print(f"  {os.path.relpath(path, ROOT)}:{line}: {msg}")
        return 1
    print("\nNo problems found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
