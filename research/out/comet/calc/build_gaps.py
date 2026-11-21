#!/usr/bin/env python3
"""Collect every NOT DISCLOSED / NOT RETRIEVED line from parts/*_notes.md Gaps sections (plus RV table gaps)
into gaps.md, one line each, prefixed by module. RV's comparison-table ND/NR cells are covered by its Gaps lines."""
import os, re
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
out = ["# Gap log - Comet Holding AG (COTN)", "",
       "One line per item. Forms: NOT DISCLOSED (read: ...) = read the document, item absent; NOT RETRIEVED (tried: ...) = could not obtain.",
       "Module prefixes: XS = CA20; RV = rival systems; IXM = x-ray modules; DV = divisions/IXS/PCT/CMD; A = group Module A; B = Module B.", ""]
n = 0
for m in ["XS", "RV", "IXM", "DV", "A"]:
    t = open(os.path.join(D, "parts", f"{m}_notes.md"), encoding="utf-8").read()
    sec = re.split(r"\n## Gaps\s*\n", t, maxsplit=1)
    if len(sec) < 2:
        continue
    body = re.split(r"\n## ", sec[1], maxsplit=1)[0]
    for line in body.splitlines():
        s = line.strip().lstrip("-* ").strip()
        if "NOT DISCLOSED" in s or "NOT RETRIEVED" in s:
            out.append(f"- [{m}] {s}"); n += 1
extra = [
 "NOT DISCLOSED (read: Comet Q3 2026 trading update corporate calendar; comet.tech corporate calendar page): dates of the H1 2027 results and Q3 2027 trading update",
 "NOT DISCLOSED (read: Comet H1 2026 report note 07 and XP Power appeal release Jul 2026): date of the XP Power retrial",
 "NOT RETRIEVED (tried: nothing beyond web leads in this run): independent peer-reviewed data on X-ray total-ionising-dose damage thresholds for DRAM/HBM/NAND (needed to test the dose claim; customer-side literature not searched systematically)",
 "NOT RETRIEVED (tried: git push): 2026-01-09_comet_capital-markets-day-2025.pdf (142 MB) is kept locally but not in the repository (GitHub 100 MB limit); its extracted text and sha256 are committed",
]
for s in extra:
    out.append(f"- [B] {s}"); n += 1
out.append(""); out.append(f"Total: {n} lines.")
open(os.path.join(D, "gaps.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print(n)
