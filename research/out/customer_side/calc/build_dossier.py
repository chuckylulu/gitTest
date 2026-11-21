#!/usr/bin/env python3
"""Assemble dossier.md and gaps.md from the template and generated pieces.
Order of operations (run each time a part changes):
  build_tables.py -> method_matrix.py -> merge_parts.py -> awards_summary.py -> build_gaps.py -> this script
Usage: python3 -I research/out/customer_side/calc/build_dossier.py
"""
import csv, os, re, subprocess, sys
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
OUT = os.path.join(ROOT, "research", "out", "customer_side")
C = os.path.join(OUT, "calc")
PY = [sys.executable, "-I"]


def run(*a):
    r = subprocess.run(PY + list(a), capture_output=True, text=True)
    if r.returncode:
        raise SystemExit(r.stdout + r.stderr)
    return r.stdout


run(os.path.join(C, "build_tables.py"))
run(os.path.join(ROOT, "research", "tools", "merge_parts.py"), "customer_side", "PAPM", "PAPL", "TALK", "XR", "SMP", "AW")  # first pass so SYN ids can be checked
print(run(os.path.join(C, "method_matrix.py")).splitlines()[0])
print(run(os.path.join(ROOT, "research", "tools", "merge_parts.py"), "customer_side", "PAPM", "PAPL", "TALK", "XR", "SMP", "AW", "SYN", "MAIN").splitlines()[-1])
run(os.path.join(C, "awards_summary.py"))
print(run(os.path.join(C, "build_gaps.py")).strip())

ev = list(csv.DictReader(open(os.path.join(OUT, "evidence.csv"), encoding="utf-8")))
tc = Counter(r["tag"] for r in ev)
s1 = list(csv.DictReader(open(os.path.join(C, "section1_table.csv"), encoding="utf-8")))
smp = open(os.path.join(OUT, "parts", "SMP_notes.md"), encoding="utf-8").read()
m = re.search(r"## Direction table\n(.*?)\n## ", smp, re.S)
direction = m.group(1).strip() if m else "NOT RETRIEVED (tried: parts/SMP_notes.md 'Direction table' section)"
t = open(os.path.join(C, "dossier_template.md"), encoding="utf-8").read()
fill = {
    "{{N_ROWS}}": str(len(ev)),
    "{{TAG_COUNTS}}": ", ".join(f"{k} {tc[k]}" for k in ["[F]", "[C]", "[S]", "[I]"]),
    "{{N_DOCS}}": str(len(s1)),
    "{{N_DOCS_INSCOPE}}": str(sum(r["in_scope_step"] == "Y" for r in s1)),
    "{{SECTION1_TABLE}}": open(os.path.join(C, "section1_table.md"), encoding="utf-8").read().strip(),
    "{{SMP_DIRECTION_TABLE}}": direction,
    "{{AWARDS_TABLE}}": open(os.path.join(C, "awards_summary.md"), encoding="utf-8").read().strip(),
    "{{MATRIX}}": open(os.path.join(C, "method_matrix.md"), encoding="utf-8").read().strip(),
    "{{METHOD_COUNTS}}": run(os.path.join(C, "method_counts.py")).strip(),
}
for k, v in fill.items():
    t = t.replace(k, v)
left = re.findall(r"\{\{[A-Z0-9_]+\}\}", t)
if left:
    raise SystemExit(f"unfilled placeholders: {left}")
# every evidence id cited in the dossier must exist
ids = {r["id"] for r in ev}
cited = set(re.findall(r"\b(?:PAPM|PAPL|TALK|XR|SMP|AW|SYN|MAIN)-\d{3}\b", t))
bad = sorted(cited - ids)
if bad:
    raise SystemExit(f"dossier cites ids not in evidence.csv: {bad}")
open(os.path.join(OUT, "dossier.md"), "w", encoding="utf-8").write(t)
g = open(os.path.join(OUT, "gaps_body.md"), encoding="utf-8").read()
open(os.path.join(OUT, "gaps.md"), "w", encoding="utf-8").write(open(os.path.join(C, "gaps_header.md"), encoding="utf-8").read() + "\n" + g)
os.remove(os.path.join(OUT, "gaps_body.md"))
print(f"dossier.md {len(t)} chars; ids cited {len(cited)}; evidence rows {len(ev)} {dict(tc)}")
