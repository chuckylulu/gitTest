#!/usr/bin/env python3
"""A3 (fix round 1, 2026-11-21): do the FY2026 (Apr 2026-Mar 2027) guidance documents name any one-off item?

Scans the saved text of every document that carries or explains a version of the FY2026 guidance
(initial 27 Apr 2026, raised 29 Jul 2026 and 28 Oct 2026) for one-off wording in English and Japanese,
and prints each hit with its page (form-feed page of the saved text) and a snippet, so a reader can see
whether the hit concerns the forecast or a reported period.
Reads only saved text files under research/sources/advantest/_text/; never executes downloaded content.
Run from the repo root: python3 -I research/out/advantest/calc/A3_guidance_oneoff_scan.py
"""
import os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
TXT = os.path.join(ROOT, "research", "sources", "advantest", "_text")
DOCS = [
    "2026-04-27_advantest_financial-results-FY2025Q4-full-year.txt",   # FY2026 initial guidance (tanshin 1.(4) Outlook)
    "2026-04-27_advantest_earnings-briefing-slides-FY2025Q4.txt",     # FY2026 forecast slide
    "2026-04-27_advantest_earnings-briefing-notes-FY2025Q4.txt",
    "2026-04-27_advantest_earnings-call-QA-FY2025Q4.txt",
    "2026-07-29_advantest_forecast-revision-E-Info-20260729.txt",     # revision notice
    "2026-07-29_advantest_financial-results-FY2026Q1.txt",
    "2026-07-29_advantest_earnings-briefing-slides-FY2026Q1.txt",
    "2026-07-29_advantest_earnings-briefing-notes-FY2026Q1.txt",
    "2026-07-29_advantest_earnings-call-QA-FY2026Q1.txt",
    "2026-10-28_advantest_financial-results-FY2026Q2.txt",            # current guidance (no separate notice)
    "2026-10-28_advantest_earnings-briefing-slides-FY2026Q2.txt",
    "2026-10-28_advantest_earnings-briefing-notes-FY2026Q2.txt",
    "2026-10-28_advantest_earnings-call-QA-FY2026Q2.txt",
]
TERMS = re.compile(r"one-off|one-time|one time|non-recurring|nonrecurring|extraordinary|special factor|一過性|一時的|特殊要因", re.I)


def main():
    total = 0
    for d in DOCS:
        p = os.path.join(TXT, d)
        if not os.path.exists(p):
            print(f"MISSING {d}")
            continue
        pages = open(p, encoding="utf-8", errors="replace").read().split("\f")
        hits = []
        for i, pg in enumerate(pages, 1):
            for m in TERMS.finditer(pg):
                snip = re.sub(r"\s+", " ", pg[max(0, m.start() - 110):m.end() + 90])
                hits.append((i, m.group(0), snip))
        total += len(hits)
        print(f"== {d}: {len(hits)} hit(s)")
        for i, t, s in hits:
            print(f"   p.{i} [{t}] ...{s}...")
    print(f"RESULT documents scanned: {len(DOCS)}; hits: {total}")
    print("Reading (by hand, from the snippets above): every hit concerns a reported period or a board meeting "
          "(FY2025 Q4 call-option gain and one-off SG&A; 1H FY2026 inventory write-down reversal; 'extraordinary meeting'); "
          "none names a one-off item inside the FY2026 forecast.")


if __name__ == "__main__":
    main()
