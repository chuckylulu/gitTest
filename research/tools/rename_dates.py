#!/usr/bin/env python3
"""Rename saved sources so the file-name date is the printed document date, and rewrite every reference.

Usage: python3 -I research/tools/rename_dates.py <company> <mapping.tsv> [--apply]
mapping.tsv: old_basename <TAB> new_date (YYYY-MM-DD) <TAB> reason
Rewrites: sources/<company>/<file> and _text/<stem>.txt (git mv), _manifest.csv (local_file, date, note),
and every text file under out/<company>/ (csv, md, py, txt, json).
"""
import csv, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # research/
company, mp = sys.argv[1], sys.argv[2]
apply = "--apply" in sys.argv
src = os.path.join(ROOT, "sources", company)
pairs = []
for line in open(mp):
    if not line.strip() or line.startswith("#"):
        continue
    old, new_date, reason = (line.rstrip("\n").split("\t") + ["", ""])[:3]
    new = new_date + old[10:]
    assert os.path.exists(os.path.join(src, old)), old
    assert not os.path.exists(os.path.join(src, new)), new
    pairs.append((old, new, new_date, reason))
for old, new, d, why in pairs:
    print(f"{old} -> {new}  ({why})")
if not apply:
    sys.exit(0)
for old, new, d, why in pairs:
    subprocess.run(["git", "mv", os.path.join(src, old), os.path.join(src, new)], check=True)
    ot = os.path.join(src, "_text", os.path.splitext(old)[0] + ".txt")
    if os.path.exists(ot):
        subprocess.run(["git", "mv", ot, os.path.join(src, "_text", os.path.splitext(new)[0] + ".txt")], check=True)
man = os.path.join(src, "_manifest.csv")
rows = list(csv.DictReader(open(man)))
for r in rows:
    for old, new, d, why in pairs:
        if os.path.basename(r["local_file"]) == old:
            r["local_file"] = r["local_file"][: -len(old)] + new
            r["date"] = d
            r["note"] = (r["note"] + f" | renamed {old[:10]} -> {d} on 2026-11-21: {why}").strip(" |")
with open(man, "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
n = 0
for dp, _, fs in os.walk(os.path.join(ROOT, "out", company)):
    for f in fs:
        if f.rsplit(".", 1)[-1] not in ("csv", "md", "py", "txt", "json"):
            continue
        p = os.path.join(dp, f)
        s = open(p, encoding="utf-8").read()
        t = s
        for old, new, d, why in pairs:
            t = t.replace(os.path.splitext(old)[0], os.path.splitext(new)[0])
        if t != s:
            open(p, "w", encoding="utf-8").write(t); n += 1
print("files rewritten:", n)
