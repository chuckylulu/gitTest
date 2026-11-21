#!/usr/bin/env python3
"""Builds out/comet/parts/B.csv: catalyst-calendar rows for Module B3 (quotes copied from saved text)."""
import csv, os
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
COLS = ["id","tag","claim","value","unit","period_fiscal","period_calendar","document","date","page_or_section","url","local_file","quote","confidence","note"]
Q3 = "research/sources/comet/2026-10_comet_press-release-Q3-2026-trading-update.html"
H1 = "research/sources/comet/2026-07_comet_press-release-H1-2026-results.html"
U3 = "https://comet.tech/news/comet-net-sales-growth-accelerates-further-in-q3-26-en-2026-10-7076a047"
UH = "https://comet.tech/news/a-successful-first-half-of-2026-sets-the-stage-for-the-second-half-en-2026-07-e03aad58"
rows = [
 ["B-001","[F]","Corporate calendar: full-year results 2026 published 5 March 2027","2027-03-05","date","FY2026","Jan-Dec 2026","Comet Q3 2026 trading update (corporate calendar box)","2026-10","Corporate Calendar",U3,Q3,"Full-year results 2026","High","Date 'March 5, 2027' printed directly above the item in the same box"],
 ["B-002","[F]","Corporate calendar: 78th AGM and Q1 2027 trading update on 15 April 2027","2027-04-15","date","Q1 FY2027","Jan-Mar 2027","Comet Q3 2026 trading update (corporate calendar box)","2026-10","Corporate Calendar",U3,Q3,"78th Annual General Meeting, Trading Update Q1","High","Date 'April 15, 2027' printed in the same box"],
 ["B-003","[C]","Penang (Malaysia) plant planned to be fully operational by 2027","2027","year","FY2027","Jan-Dec 2027","Comet H1 2026 results media release","2026-07","PCT section",UH,H1,"The new plant is planned to be fully operational by 2027","Medium","Company plan; first product qualifications pending"],
 ["B-004","[C]","Efficiency program fully implemented by end of 2027; CHF 20-30m annual EBITDA improvement from 2028","20-30","CHF m","FY2027-FY2028","Dec 2027 / 2028","Comet H1 2026 results media release","2026-07","H1/26 results",UH,H1,"expected to be fully implemented by the end of 2027","Medium","Same statement as DV-053"],
]
with open(os.path.join(ROOT,"research/out/comet/parts/B.csv"),"w",newline="") as f:
    w = csv.writer(f); w.writerow(COLS); w.writerows(rows)
print("wrote", len(rows))
