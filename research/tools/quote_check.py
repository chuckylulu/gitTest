#!/usr/bin/env python3
"""Mechanical check of evidence rows: does each quote occur in the cited local file?

Usage: python3 -I research/tools/quote_check.py <evidence.csv> [--out report.csv]
For every row with a local_file and a quote: normalise whitespace/case/quotes in both,
search page by page, and report FOUND (with pages) / NOT FOUND / NO FILE / NO TEXT.
Also flags: quote longer than 25 words, tag not in [F]/[C]/[S]/[I], [F] row without local_file,
and a cited page that differs from where the quote was found.
"""
import csv, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))  # repo root


def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("‘", "'")
    s = s.replace("“", '"').replace("”", '"').replace("–", "-").replace("—", "-")
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl").replace("¥", "yen ").replace("¥", "yen ")
    s = re.sub(r"\s+", " ", s).strip().lower()
    return s


def squash(s):
    return re.sub(r"[^a-z0-9%.]", "", norm(s))


def text_for(local):
    p = local if os.path.isabs(local) else os.path.join(ROOT, local)
    if not os.path.exists(p):
        return None, "NO FILE"
    d, f = os.path.split(p)
    tp = os.path.join(d, "_text", os.path.splitext(f)[0] + ".txt")
    if not os.path.exists(tp):
        return None, "NO TEXT"
    return open(tp, encoding="utf-8", errors="replace").read().split("\f"), ""


def main():
    src = sys.argv[1]
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    rows = list(csv.DictReader(open(src, encoding="utf-8")))
    cache, results = {}, []
    counts = {}
    for r in rows:
        tag = (r.get("tag") or "").strip()
        flags = []
        if tag not in ("[F]", "[C]", "[S]", "[I]"):
            flags.append("BAD TAG")
        q = (r.get("quote") or "").strip()
        if q and len(q.split()) > 25:
            flags.append("QUOTE>25W")
        lf = (r.get("local_file") or "").strip()
        if tag == "[F]" and not lf:
            flags.append("[F] WITHOUT LOCAL FILE")
        status, pages = "", []
        if lf and q:
            if lf not in cache:
                cache[lf] = text_for(lf)
            texts, err = cache[lf]
            if texts is None:
                status = err
            else:
                nq, sq = norm(q), squash(q)
                pages = [i for i, t in enumerate(texts, 1) if nq in norm(t)]
                if not pages and len(sq) >= 12:
                    pages = [i for i, t in enumerate(texts, 1) if sq in squash(t)]
                    status = "FOUND (layout-insensitive)" if pages else "NOT FOUND"
                else:
                    status = "FOUND" if pages else "NOT FOUND"
                cited = re.findall(r"\d+", r.get("page_or_section") or "")
                if pages and cited and re.match(r"\s*(p|pp|page|pages)?\.?\s*\d", (r.get("page_or_section") or "").lower()):
                    if int(cited[0]) not in pages:
                        flags.append(f"CITED PAGE {cited[0]} != FOUND {pages[:5]}")
        elif tag in ("[F]", "[C]") and not q:
            status = "NO QUOTE"
        counts[status or "-"] = counts.get(status or "-", 0) + 1
        results.append(dict(id=r.get("id"), tag=tag, status=status, pages=" ".join(map(str, pages[:8])),
                            flags="; ".join(flags), local_file=lf, quote=q[:160]))
    for k, v in sorted(counts.items()):
        print(f"{k}: {v}")
    bad = [x for x in results if x["status"] in ("NOT FOUND", "NO FILE", "NO TEXT", "NO QUOTE") or x["flags"]]
    for x in bad:
        print(f"{x['id']}\t{x['tag']}\t{x['status']}\t{x['flags']}\t{x['local_file']}\t{x['quote'][:90]}")
    if out:
        with open(out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=list(results[0].keys()) if results else ["id"])
            w.writeheader(); w.writerows(results)


if __name__ == "__main__":
    main()
