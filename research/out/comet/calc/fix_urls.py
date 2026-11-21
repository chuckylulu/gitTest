#!/usr/bin/env python3
"""Replace placeholder/generic url fields in parts/*.csv with the exact download URL from the manifest for the cited local_file."""
import csv, glob, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
man = {r["local_file"]: r["url"] for r in csv.DictReader(open(os.path.join(ROOT, "research/sources/comet/_manifest.csv"))) if r["status"] == "RETRIEVED"}
for p in glob.glob(os.path.join(ROOT, "research/out/comet/parts/*.csv")):
    rows = list(csv.DictReader(open(p, encoding="utf-8"))); cols = list(rows[0].keys()); n = 0
    for r in rows:
        u, lf = r["url"].strip(), r["local_file"].strip()
        if lf in man and (not u.startswith("http") or " " in u or u.rstrip("/").endswith(("/investors", "/en/investors"))):
            r["url"] = man[lf]; n += 1
    with open(p, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader(); w.writerows(rows)
    print(os.path.basename(p), "fixed", n)
