"""Build gaps.md: every NOT DISCLOSED / NOT RETRIEVED line from the part notes, plus manifest NOT RETRIEVED rows.
Usage: python3 -I research/out/kla/calc/build_gaps.py  (run from repo root or anywhere)"""
import csv, os, re
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # out/kla
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))         # repo root
NOTES = [("Q1/Q4/Nova", "Q14_notes.md"), ("Q2/Q3", "Q23_notes.md"), ("A1/A2", "A12_notes.md"),
         ("A3/A6/Q5", "A36Q5_notes.md"), ("A4/A5", "A45_notes.md")]
out = ["# Gap log - KLA (KLAC), FY ends June 30", "",
       "One line per item. Built by calc/build_gaps.py from the part notes ('Gaps' sections) and from sources/kla/_manifest.csv. "
       "Items were de-duplicated by text only, so near-duplicates across parts can remain.", ""]
seen = set()
for label, f in NOTES:
    txt = open(os.path.join(HERE, "parts", f), encoding="utf-8").read()
    m = re.search(r"^## Gaps.*?$(.*?)(?=^## |\Z)", txt, re.S | re.M)
    block = m.group(1) if m else ""
    items = [l.strip()[2:].strip() for l in block.splitlines() if l.strip().startswith("- ")]
    items = [i for i in items if "NOT DISCLOSED" in i or "NOT RETRIEVED" in i or "Not retrieved" in i]
    out.append(f"## {label}")
    for i in items:
        k = re.sub(r"\W+", "", i.lower())[:120]
        if k in seen: continue
        seen.add(k); out.append(f"- {i}")
    out.append("")
out.append("## Manifest: documents attempted and NOT RETRIEVED")
for r in csv.DictReader(open(os.path.join(ROOT, "research/sources/kla/_manifest.csv"), encoding="utf-8")):
    if r["status"] == "NOT RETRIEVED":
        out.append(f"- NOT RETRIEVED (tried: {r['url']}; {r['http_code'] or 'no code'}; {r['note'][:160]}) - {r['doctype']}")
open(os.path.join(HERE, "gaps.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("lines", len(out))
