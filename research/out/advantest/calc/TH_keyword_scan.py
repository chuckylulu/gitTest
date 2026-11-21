#!/usr/bin/env python3
"""TH module premise check: which technology terms appear in Advantest-issued documents saved in
research/sources/advantest/ (issuer == advantest in _manifest.csv). Reads the _text copies only.
Run from the repo root: python3 -I research/out/advantest/calc/TH_keyword_scan.py
"""
import csv, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
SRC = os.path.join(ROOT, "research", "sources", "advantest")
TERMS = {
    "hybrid bond(ing)": r"hybrid[\s-]*bond",
    "HBM": r"\bHBM",
    "chiplet": r"chiplet",
    "known good die/stack or KGD/KGS": r"known[\s-]*good|\bKGD|\bKGS",
    "die-level": r"die[\s-]*level",
    "advanced packaging": r"advanced[\s-]*packag",
    "2.5D/3D": r"2\.5D|3\.5D|\b3D\b",
    "system level test / SLT": r"system[\s-]*level[\s-]*test|\bSLT\b",
    "burn-in": r"burn[\s-]*in",
    "metrology": r"metrology",
    "CD-SEM / mask SEM": r"CD-SEM|Mask[\s-]*SEM|E36[0-9]0",
    "wafer inspection / defect inspection": r"wafer inspection|defect inspection|optical inspection",
    "CoWoS": r"CoWoS",
    "probe card": r"probe[\s-]*card",
}
rows = [r for r in csv.DictReader(open(os.path.join(SRC, "_manifest.csv"), encoding="utf-8"))
        if r["issuer"] == "advantest" and r["status"] == "RETRIEVED"]
seen, docs = set(), []
for r in rows:
    base = os.path.splitext(os.path.basename(r["local_file"]))[0]
    tp = os.path.join(SRC, "_text", base + ".txt")
    if base in seen or not os.path.exists(tp):
        continue
    seen.add(base)
    # skip web index/navigation pages whose menus list product names on every page
    nav = base.split("_", 2)[-1].startswith(("ir-", "news-index"))
    docs.append((base, open(tp, encoding="utf-8", errors="replace").read(), nav))
content = [d for d in docs if not d[2]]
print(f"Advantest-issued text files scanned: {len(docs)} (of which {len(docs)-len(content)} IR/news index web pages excluded below)")
print(f"Documents counted: {len(content)}\n")
for name, pat in TERMS.items():
    rx = re.compile(pat, re.I)
    hits = [b for b, t, _ in content if rx.search(t)]
    print(f"{name:<40} {len(hits):>3} documents")
    if len(hits) <= 6:
        for b in hits:
            print(f"    - {b}")
