#!/usr/bin/env python3
"""DS (dossier) B4 pointer: count the gap lines in research/out/advantest/gaps.md by section and form.

A gap line is a line that starts with 'NOT DISCLOSED (read:' or 'NOT RETRIEVED (tried:'.
The bullet list under 'Files the user can save by hand' is counted separately (it repeats
NOT RETRIEVED items as save instructions and is not a gap line).

Run from the repo root: python3 -I research/out/advantest/calc/DS_gap_counts.py
"""
import os, re, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
GAPS = os.path.join(ROOT, "research", "out", "advantest", "gaps.md")


def main():
    sec = None
    cnt = collections.OrderedDict()
    save_items = 0
    for line in open(GAPS, encoding="utf-8"):
        s = line.rstrip("\n")
        m = re.match(r"^##\s+(.*)$", s)
        if m:
            sec = m.group(1).strip()
            cnt.setdefault(sec, collections.Counter())
            continue
        if sec is None:
            continue
        if sec.startswith("Files the user can save") and s.startswith("- "):
            save_items += 1
            continue
        if s.startswith("NOT DISCLOSED (read:"):
            cnt[sec]["NOT DISCLOSED"] += 1
        elif s.startswith("NOT RETRIEVED (tried:"):
            cnt[sec]["NOT RETRIEVED"] += 1
    tot = collections.Counter()
    print("section | NOT DISCLOSED | NOT RETRIEVED | total")
    for k, c in cnt.items():
        if k.startswith("Files the user can save"):
            continue
        tot.update(c)
        print(f"{k} | {c['NOT DISCLOSED']} | {c['NOT RETRIEVED']} | {c['NOT DISCLOSED'] + c['NOT RETRIEVED']}")
    print(f"RESULT gap lines: NOT DISCLOSED {tot['NOT DISCLOSED']}; NOT RETRIEVED {tot['NOT RETRIEVED']}; "
          f"total {tot['NOT DISCLOSED'] + tot['NOT RETRIEVED']}")
    print(f"RESULT items listed under 'Files the user can save by hand': {save_items}")


if __name__ == "__main__":
    main()
