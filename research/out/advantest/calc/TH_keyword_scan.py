#!/usr/bin/env python3
"""TH module premise check: which technology terms appear in Advantest-issued documents saved in
research/sources/advantest/ (file names containing "_advantest_"). Reads the _text copies only.
Run from the repo root: python3 -I research/out/advantest/calc/TH_keyword_scan.py

Changes by the TH verifier (2026-11-21):
- the document list is now taken from the _text folder itself (every *_advantest_*.txt), not from
  _manifest.csv, and is printed in full below, so the count can be reproduced;
- Japanese terms were added, because about half of the saved documents are bilingual (JE_*);
- further hybrid-bonding synonyms were added (Cu-Cu, direct bond).
Other agents may save more documents later, so the counts are valid for the file list printed.
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TXT = os.path.join(ROOT, "research", "sources", "advantest", "_text")
TERMS = {
    "hybrid bond(ing) incl. Cu-Cu / direct bond / Japanese": r"hybrid[\s-]*bond|Cu[\s-]*to[\s-]*Cu|Cu[\s-]*Cu\b|direct[\s-]*bond|ハイブリッド[・\s]*ボンディング|ハイブリッド接合",
    "HBM": r"\bHBM",
    "chiplet": r"chiplet|チップレット",
    "known good die/stack or KGD/KGS": r"known[\s-]*good|\bKGD|\bKGS",
    "die-level": r"die[\s-]*level|ダイレベル",
    "advanced packaging": r"advanced[\s-]*packag|先端パッケージ",
    "2.5D/3D": r"2\.5D|3\.5D|\b3D\b",
    "system level test / SLT": r"system[\s-]*level[\s-]*test|\bSLT\b",
    "burn-in": r"burn[\s-]*in|バーンイン",
    "metrology": r"metrology|計測",
    "CD-SEM / mask SEM": r"CD-SEM|Mask[\s-]*SEM|E36[0-9]0",
    "wafer inspection / defect inspection (EN/JA)": r"wafer inspection|defect inspection|optical inspection|ウェーハ検査|ウエハ検査|欠陥検査",
    "CoWoS": r"CoWoS",
    "probe card": r"probe[\s-]*card|プローブカード",
}
files = sorted(f for f in os.listdir(TXT) if "_advantest_" in f and f.endswith(".txt"))
docs = []
for f in files:
    base = f[:-4]
    # skip web index/navigation pages whose menus list product names on every page
    nav = base.split("_", 2)[-1].startswith(("ir-", "news-index"))
    docs.append((base, open(os.path.join(TXT, f), encoding="utf-8", errors="replace").read(), nav))
content = [d for d in docs if not d[2]]
print(f"Advantest-issued text files found: {len(docs)} (of which {len(docs)-len(content)} IR/news index web pages excluded)")
print(f"Documents counted: {len(content)}\n")
for name, pat in TERMS.items():
    rx = re.compile(pat, re.I)
    hits = [b for b, t, _ in content if rx.search(t)]
    print(f"{name:<55} {len(hits):>3} documents")
    if len(hits) <= 6:
        for b in hits:
            print(f"    - {b}")
rx_hb = re.compile(TERMS["hybrid bond(ing) incl. Cu-Cu / direct bond / Japanese"], re.I)
rx_neg = re.compile(TERMS["wafer inspection / defect inspection (EN/JA)"] + "|CoWoS", re.I)
print(f"\nCheck including the excluded web pages ({len(docs)} files): hybrid-bonding terms in "
      f"{sum(1 for _, t, _ in docs if rx_hb.search(t))}; wafer/defect inspection or CoWoS in "
      f"{sum(1 for _, t, _ in docs if rx_neg.search(t))}")
print("\nExcluded navigation pages:")
for b, _, nav in docs:
    if nav:
        print(f"  - {b}")
print("\nDocuments counted (file list):")
for b, _, _ in content:
    print(f"  - {b}")
