#!/usr/bin/env python3
"""Self-check fix (2026-11-21) to XM_period_labels.py.

The clean-context self-check found that A1-316 described 1H FY2026 but was labelled FY2026 Q3, the
quarter in which the statement was made. XM_period_labels.py had moved every 'past' statement
(branch P, and the manual rows whose note reads 'Statement refers to ...') to its statement quarter.
That hides the period the statement is about. This script restores the referenced period and keeps
the statement date in brackets:
    period_fiscal   = <referenced period>            e.g. FY2026 1H
    period_calendar = <months> (stated D Mon YYYY)   e.g. Apr-Sep 2026 (stated 28 Oct 2026)
It changes only rows whose note holds 'Statement refers to <label> (<months>).'
Run from the repo root: python3 -I research/out/advantest/calc/XM_period_labels_fix.py [--apply]
"""
import csv, glob, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
PARTS = os.path.join(ROOT, "research", "out", "advantest", "parts")
PAT = re.compile(r"Statement refers to (.+?) \(([^()]*\d{4})\)\.\s*")
apply = "--apply" in sys.argv
n = 0
for p in sorted(glob.glob(os.path.join(PARTS, "*.csv"))):
    rows = list(csv.DictReader(open(p, encoding="utf-8")))
    if not rows:
        continue
    changed = False
    for r in rows:
        m = PAT.search(r["note"])
        if not m:
            continue
        label, months = m.group(1).strip(), m.group(2).strip()
        d = re.search(r"\((?:stated|asked|published|presented)[^)]*\)", r["period_calendar"])
        when = d.group(0) if d else ""
        new_pf, new_pc = label, (months + " " + when).strip()
        new_note = PAT.sub("", r["note"]).strip()
        new_note = (new_note + " | period = the period the statement refers to; statement date in brackets (self-check fix 2026-11-21)").strip(" |")
        if (new_pf, new_pc) != (r["period_fiscal"], r["period_calendar"]):
            print(f"{r['id']} | {r['period_fiscal']} -> {new_pf} | {r['period_calendar']} -> {new_pc}")
            n += 1
            r["period_fiscal"], r["period_calendar"], r["note"] = new_pf, new_pc, new_note
            changed = True
    if changed and apply:
        with open(p, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
print(f"rows relabelled to their referenced period: {n} ({'applied' if apply else 'dry run'})")
