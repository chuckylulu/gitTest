#!/usr/bin/env python3
"""DS (dossier) premise check: what research/prior/ actually holds, against the layout note in
research/CLAUDE.md that describes it as 'the 12 files exported from AI Studio'.

Run from the repo root: python3 -I research/out/advantest/calc/DS_prior_check.py
Only file names are listed; no file content is read.
"""
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
PRIOR = os.path.join(ROOT, "research", "prior")
RULES = os.path.join(ROOT, "research", "CLAUDE.md")


def main():
    names = []
    for dp, dn, fn in os.walk(PRIOR):
        for f in fn:
            names.append(os.path.relpath(os.path.join(dp, f), ROOT))
    names.sort()
    print(f"files under research/prior/: {len(names)}")
    for n in names:
        print("  ", n)
    js = [n for n in names if n.lower().endswith(".json")]
    other = [n for n in names if not n.endswith(".gitkeep")]
    note = [l.strip() for l in open(RULES, encoding="utf-8") if "prior/" in l and "AI Studio" in l]
    print("layout note in research/CLAUDE.md:", note[0] if note else "(none found)")
    print(f"RESULT JSON exports in prior/: {len(js)}; files other than .gitkeep: {len(other)}; "
          f"layout note describes 12 AI Studio exports: {'yes' if note and '12' in note[0] else 'no'}")


if __name__ == "__main__":
    main()
