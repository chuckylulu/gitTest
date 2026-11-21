#!/usr/bin/env python3
"""Build the dossier's Section 1 evidence table (one row per paper or talk) from the module tables
parts/PAPM_table.csv, parts/PAPL_table.csv and parts/TALK_table.csv.

Usage: python3 -I research/out/customer_side/calc/build_tables.py
Outputs: calc/section1_table.md (markdown, grouped by chipmaker) and calc/section1_table.csv.
Rows are grouped by (chipmaker, venue/date/title); steps, methods, vendors, status and limits of the
(step, method) rows of one document are joined with " ; ". Nothing is paraphrased here: the text is
the module tables' own wording (quotes from the cited documents or NOT DISCLOSED lines).

Also reads parts/ADDM_table.csv and parts/ADDL_table.csv (completeness round) and calc/section1_extra_rows.csv (papers found by the SMP and XR modules).
"""
import csv, os, re
from collections import OrderedDict
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
P = os.path.join(ROOT, "research", "out", "customer_side", "parts")
C = os.path.join(ROOT, "research", "out", "customer_side", "calc")
ORDER = ["SK hynix", "Samsung", "Micron", "TSMC", "Intel", "ASE", "Amkor"]
STEPS6 = ["pre-bond surface", "bond overlay", "post-bond voids", "TSV / micro-bump", "wafer shape", "film and CD metrology in memory"]


def company_key(c):
    for i, k in enumerate(ORDER):
        if c.lower().startswith(k.lower()):
            return i
    return len(ORDER)


def clean(s):
    s = re.sub(r"\s+", " ", (s or "").strip())
    return s.replace("|", "/")


def nd_short(s):
    # keep NOT DISCLOSED lines but shorten the "(read: ...)" path to the file stem
    return re.sub(r"\(read: ([^)]*)\)", lambda m: "(read: " + os.path.basename(m.group(1).split(",")[0]).strip() +
                  ("," + ",".join(m.group(1).split(",")[1:]) if "," in m.group(1) else "") + ")", s)


groups = OrderedDict()
for fn, mod in [("PAPM_table.csv", "PAPM"), ("PAPL_table.csv", "PAPL"), ("TALK_table.csv", "TALK"), ("ADDM_table.csv", "ADDM"), ("ADDL_table.csv", "ADDL"), ("../calc/section1_extra_rows.csv", "EXTRA")]:
    # EXTRA = method-bearing papers found by the SMP and XR modules, entered by the main session from their evidence rows
    for i, r in enumerate(csv.DictReader(open(os.path.join(P, fn), encoding="utf-8")), 1):
        key = (clean(r["chipmaker"]), clean(r["venue_date_title"]))
        g = groups.setdefault(key, dict(rows=[], src=set(), doi=clean(r.get("doi", ""))))
        g["rows"].append(r); g["src"].add(f"{mod}_table row {i}")


def joined(rows, col, transform=lambda x: x):
    out = []
    for r in rows:
        v = transform(clean(r.get(col, "")))
        if v and v not in out:
            out.append(v)
    return " ; ".join(out)


recs = []
for (co, ven), g in groups.items():
    rows = g["rows"]
    steps = joined(rows, "process_step")
    tags = sorted({t for r in rows for t in clean(r["tag"]).split("/") if t})  # split "[F]/[C]" before joining
    ev = []
    for r in rows:
        for e in re.split(r"[;,\s]+", r.get("evidence_ids", "")):
            if e and e not in ev:
                ev.append(e)
    recs.append(dict(
        chipmaker=co, venue_date_title=ven + (f" (doi {g['doi']})" if g["doi"] and g["doi"] not in ven else ""),
        process_step=steps, method=joined(rows, "method"),
        tool_vendor=joined(rows, "tool_vendor", nd_short),
        status_in_authors_words=joined(rows, "status_in_authors_words", nd_short),
        limits_stated=joined(rows, "limits_stated", nd_short),
        tag="/".join(tags), evidence_ids=", ".join(ev),
        in_scope_step="Y" if any(s in steps for s in STEPS6) else "N",
        source_rows="; ".join(sorted(g["src"]))))
recs.sort(key=lambda r: (company_key(r["chipmaker"]), r["in_scope_step"] != "Y", r["venue_date_title"]))
cols = ["chipmaker", "venue_date_title", "process_step", "method", "tool_vendor", "status_in_authors_words",
        "limits_stated", "tag", "evidence_ids", "in_scope_step", "source_rows"]
with open(os.path.join(C, "section1_table.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=cols); w.writeheader(); w.writerows(recs)
md = []
cur = None
for r in recs:
    co = ORDER[company_key(r["chipmaker"])] if company_key(r["chipmaker"]) < len(ORDER) else r["chipmaker"]
    if co != cur:
        cur = co
        n = sum(1 for x in recs if (ORDER[company_key(x["chipmaker"])] if company_key(x["chipmaker"]) < len(ORDER) else x["chipmaker"]) == co)
        md.append(f"\n#### {co} ({n} documents)\n")
        md.append("| Chipmaker | Venue, date, title | Process step | Method | Tool vendor if named | Production, pilot or lab, in the authors' words | Limits the authors state | Tag | Evidence |")
        md.append("|---|---|---|---|---|---|---|---|---|")
    md.append("| " + " | ".join(r[c] for c in cols[:9]) + " |")
open(os.path.join(C, "section1_table.md"), "w", encoding="utf-8").write("\n".join(md) + "\n")
from collections import Counter
print("documents:", len(recs), dict(Counter(ORDER[company_key(r['chipmaker'])] if company_key(r['chipmaker']) < len(ORDER) else r['chipmaker'] for r in recs)))
print("in-scope-step documents:", sum(r["in_scope_step"] == "Y" for r in recs))
