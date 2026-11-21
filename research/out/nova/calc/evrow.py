#!/usr/bin/env python3
"""Helper used to write evidence rows for out/nova/parts/*.csv.

Each row's quote is checked against the saved document's extracted text (same normalisation as
research/tools/quote_check.py). The physical PDF page is filled in automatically; the URL is taken
from research/sources/nova/_manifest.csv. A row whose quote is not found raises an error, so no
row can be written with a quote that is absent from its cited file.
"""
import csv, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "research", "sources", "nova")
COLS = ["id", "tag", "claim", "value", "unit", "period_fiscal", "period_calendar", "document", "date",
        "page_or_section", "url", "local_file", "quote", "confidence", "note"]
_MAN = None
_CACHE = {}


def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"\s+", " ", s).strip().lower()


def squash(s):
    return re.sub(r"[^a-z0-9%.]", "", norm(s))


def manifest():
    global _MAN
    if _MAN is None:
        _MAN = {}
        for r in csv.DictReader(open(os.path.join(SRC, "_manifest.csv"))):
            if r["status"] == "RETRIEVED":
                _MAN[os.path.basename(r["local_file"])] = r["url"]
    return _MAN


def pages_for(fname):
    if fname not in _CACHE:
        tp = os.path.join(SRC, "_text", os.path.splitext(fname)[0] + ".txt")
        _CACHE[fname] = open(tp, encoding="utf-8", errors="replace").read().split("\f")
    return _CACHE[fname]


def find(fname, quote):
    pages = pages_for(fname)
    nq, sq = norm(quote), squash(quote)
    hits = [i for i, t in enumerate(pages, 1) if nq in norm(t)]
    if not hits and len(sq) >= 12:
        hits = [i for i, t in enumerate(pages, 1) if sq in squash(t)]
    return hits


def row(id, tag, claim, value, unit, pf, pc, document, date, fname, quote, confidence="", note="", section=None):
    assert tag in ("[F]", "[C]", "[S]", "[I]"), tag
    url, lf, pg = "", "", ""
    if fname:
        assert os.path.exists(os.path.join(SRC, fname)), f"missing source {fname}"
        url = manifest().get(fname, "")
        lf = f"research/sources/nova/{fname}"
        if quote:
            assert len(quote.split()) <= 25, f"{id}: quote > 25 words"
            hits = find(fname, quote)
            if not hits:
                raise SystemExit(f"{id}: QUOTE NOT FOUND in {fname}: {quote!r}")
            if fname.endswith(".pdf"):
                pg = "p." + str(hits[0])
            else:
                pg = section or "web page text"
        else:
            pg = section or ""
    else:
        pg = section or ""
    return dict(id=id, tag=tag, claim=claim, value=value, unit=unit, period_fiscal=pf, period_calendar=pc,
                document=document, date=date, page_or_section=pg, url=url, local_file=lf, quote=quote,
                confidence=confidence, note=note)


def write(path, rows):
    ids = [r["id"] for r in rows]
    assert len(ids) == len(set(ids)), "duplicate ids"
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=COLS)
        w.writeheader(); w.writerows(rows)
    print(f"wrote {path}: {len(rows)} rows")
