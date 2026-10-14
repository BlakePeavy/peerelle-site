#!/usr/bin/env python3
"""Copy styles.css into the <style id="site-css"> block of every page.
Run from the repo root after editing styles.css: python3 tools/inline-css.py"""
import glob, re
css = open("styles.css").read()
for f in glob.glob("*.html"):
    h = open(f).read()
    n = re.sub(r'(<style id="site-css">\n).*?(  </style>)', lambda m: m.group(1) + css + m.group(2), h, flags=re.S)
    if n != h:
        open(f, "w").write(n); print("updated", f)
