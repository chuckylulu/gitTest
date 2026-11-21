#!/usr/bin/env python3
"""Find which page(s) of a saved document contain a phrase.

Usage: python3 -I research/tools/findpage.py <local_file (pdf/html) or _text .txt> "<phrase>" [more phrases...]
Matching ignores case, whitespace runs and soft hyphenation. Prints page:line-snippet for each hit.
For PDFs, page numbers are physical PDF pages (1-based), from the form feeds pdftotext writes.
"""
import os, re, sys


def text_path(p):
    if p.endswith(".txt"):
        return p
    d, f = os.path.split(p)
    return os.path.join(d, "_text", os.path.splitext(f)[0] + ".txt")


def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"\s+", " ", s).strip().lower()


def main():
    tp = text_path(sys.argv[1])
    raw = open(tp, encoding="utf-8", errors="replace").read()
    pages = raw.split("\f")
    for phrase in sys.argv[2:]:
        q = norm(phrase)
        hits = []
        for i, pg in enumerate(pages, 1):
            if q in norm(pg):
                hits.append(i)
        print(f"{phrase!r}: pages {hits if hits else 'NOT FOUND'}")
        for i in hits[:5]:
            for line in pages[i - 1].splitlines():
                if q[:30] and norm(line).find(q[:30]) >= 0:
                    print(f"  p{i}: {line.strip()[:200]}")
                    break


if __name__ == "__main__":
    main()
