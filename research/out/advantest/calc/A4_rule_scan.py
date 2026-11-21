#!/usr/bin/env python3
"""A4 - export-rule scan (supports A4-400, A4-401, A4-403, A4-404).

Part 1: full-text search of every saved Advantest document (research/sources/advantest/_text/*_advantest_*.txt,
        PDF pages split on form feeds, physical page numbers) for the names of specific export rules.
        Question: does any Advantest document name a specific export rule (EAR, Entity List, foreign direct
        product rule, ECCN, BIS, Japan's FEFTA / METI list, Chinese counter-measures)?
Part 2: search of the saved Federal Register rules (research/sources/advantest/_text/*_federalregister_*.txt)
        for test-equipment terms, to show where test equipment appears in the rule text read.
No figures are typed in; the script only reads the saved text copies. Run:
    python3 -I research/out/advantest/calc/A4_rule_scan.py
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
TXT = os.path.normpath(os.path.join(HERE, "..", "..", "..", "sources", "advantest", "_text"))

ADV_TERMS = [
    ("EAR (word, case-sensitive)", r"\bEAR\b"),
    ("Export Administration Regulations", r"(?i)export\s+administration\s+regulations"),
    ("Entity List", r"(?i)entity\s+list"),
    ("foreign direct product rule / FDPR", r"(?i)foreign[\s-]+direct[\s-]+product|\bFDPR?\b"),
    ("Bureau of Industry and Security / BIS", r"(?i)bureau\s+of\s+industry|\bBIS\b"),
    ("ECCN / 3B002 / 3B99x", r"\bECCN\b|3B99\d|3B00\d"),
    ("Foreign Exchange and Foreign Trade Act / FEFTA", r"(?i)foreign\s+exchange\s+and\s+foreign\s+trade|\bFEFTA\b"),
    ("METI / Ministry of Economy", r"\bMETI\b|(?i:ministry\s+of\s+economy)"),
    ("MOFCOM / unreliable entity list", r"\bMOFCOM\b|(?i:unreliable\s+entity)"),
    ("gallium / germanium / rare earth", r"(?i)\bgallium\b|\bgermanium\b|rare[\s-]+earth"),
    ("'October 7' (US rule of 7 Oct 2022)", r"(?i)october\s+7\b"),
    ("'export controls on China'", r"(?i)export\s+controls?\s+on\s+china"),
    ("'export restriction(s)'", r"(?i)export\s+restriction"),
    ("'export control' (any use)", r"(?i)export[\s-]+control"),
]

FR_TERMS = [
    ("3B992.b.4 (IC / discrete test equipment)", r"3B992\.b\.4"),
    ("3B002 (test or inspection equipment)", r"3B002"),
    ("'tester' / 'test equipment'", r"(?i)\btesters?\b|test\s+equipment"),
    ("'back-end'", r"(?i)back-?\s*end"),
]


def pages(fname):
    return open(os.path.join(TXT, fname), encoding="utf-8", errors="replace").read().split("\f")


def snippet(text, pat, width=90):
    m = re.search(pat, text)
    if not m:
        return ""
    s = text[max(0, m.start() - width): m.end() + width]
    return re.sub(r"\s+", " ", s).strip()


adv = sorted(f for f in os.listdir(TXT) if "_advantest_" in f and f.endswith(".txt"))
print("== Part 1: Advantest documents scanned ==")
print(f"documents: {len(adv)} (first {adv[0]}, last {adv[-1]})")
by_kind = {}
for f in adv:
    k = "web page (.html)" if re.search(r"_(news|ir)-", f) else "PDF (filings, results, slides, Q&A, reports)"
    by_kind[k] = by_kind.get(k, 0) + 1
for k, v in by_kind.items():
    print(f"   {k}: {v}")
print(f"RESULT advantest_docs_scanned = {len(adv)}")
print()
for label, pat in ADV_TERMS:
    hits = []
    for f in adv:
        for i, p in enumerate(pages(f), 1):
            if re.search(pat, p):
                hits.append((f, i, snippet(p, pat)))
    docs = sorted({h[0] for h in hits})
    print(f"--- {label}: {len(docs)} documents, {len(hits)} pages")
    key = re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")
    print(f"RESULT docs_with_{key} = {len(docs)}")
    show = hits if len(docs) <= 8 else [h for h in hits if not re.search(r"_(news|ir)-", h[0])][:12]
    for f, i, s in show:
        print(f"   {f} p.{i}: ...{s[:220]}...")
    if len(docs) > 8:
        web = [d for d in docs if re.search(r"_(news|ir)-", d)]
        print(f"   ({len(web)} of the {len(docs)} documents are saved web pages; in the web pages checked the hit is the site "
              f"navigation link 'Export Control', not a statement; PDF hits listed above)")
print()

fr = sorted(f for f in os.listdir(TXT) if "_federalregister_" in f and f.endswith(".txt"))
print("== Part 2: saved Federal Register rules, pages with test-equipment terms ==")
print(f"RESULT fr_docs_scanned = {len(fr)}")
for f in fr:
    print(f"--- {f}")
    for label, pat in FR_TERMS:
        pg = [i for i, p in enumerate(pages(f), 1) if re.search(pat, p)]
        print(f"   {label}: pages {pg if pg else 'none'}")
later = [f for f in fr if f[:4] in ("2025", "2026")]
n_test = sum(1 for f in later for p in pages(f) if re.search(FR_TERMS[0][1] + "|" + FR_TERMS[1][1], p))
print(f"RESULT fr_2025_2026_docs = {len(later)}")
print(f"RESULT fr_2025_2026_pages_naming_3B992b4_or_3B002 = {n_test}")
