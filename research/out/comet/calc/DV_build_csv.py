#!/usr/bin/env python3
"""Builds research/out/comet/parts/DV.csv (division module) from saved Comet documents.

Table-row quotes are extracted from the saved text (whitespace collapsed) so they match exactly;
PDF page numbers are located automatically (physical page = form-feed page in _text).
No arithmetic here: computed values come from DV_halfyears.py / DV_targets.py (cited in [I] rows).
"""
import csv, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
SRC = "research/sources/comet"
OUT = os.path.join(ROOT, "research/out/comet/parts/DV.csv")
HDR = "id,tag,claim,value,unit,period_fiscal,period_calendar,document,date,page_or_section,url,local_file,quote,confidence,note".split(",")

DOCS = {
    "HY22": ("2022-07-27_comet_half-year-report-H1-2022.pdf", "Comet Half-Year Report 2022"),
    "HY23": ("2023-07-27_comet_half-year-report-H1-2023.pdf", "Comet Half-Year Report 2023"),
    "HY24": ("2024-07-30_comet_half-year-report-H1-2024.pdf", "Comet Half-Year Report 2024"),
    "HY25": ("2025-07-30_comet_half-year-report-H1-2025.pdf", "Comet Half-Year Report 2025"),
    "HY26": ("2026-07-30_comet_half-year-report-H1-2026.pdf", "Comet Half-Year Report 2026"),
    "AR21": ("2022-03-03_comet_annual-report-FY2021.pdf", "Comet Annual Report 2021"),
    "AR22": ("2023-03-01_comet_annual-report-FY2022.pdf", "Comet Annual Report 2022"),
    "AR23": ("2024-03-03_comet_annual-report-FY2023.pdf", "Comet Annual Report 2023"),
    "AR24": ("2025-03-05_comet_annual-report-FY2024.pdf", "Comet Annual Report 2024"),
    "AR25": ("2026-03-05_comet_annual-report-FY2025.pdf", "Comet Annual Report 2025"),
    "PHY22": ("2022-07-27_comet_results-presentation-H1-2022.pdf", "H1 2022 results presentation"),
    "PFY22": ("2023-03-01_comet_results-presentation-FY2022.pdf", "FY2022 results presentation"),
    "PHY23": ("2023-07-27_comet_results-presentation-H1-2023.pdf", "H1 2023 results presentation"),
    "PFY24": ("2025-03-05_comet_results-presentation-FY2024.pdf", "FY2024 results presentation"),
    "PHY25": ("2025-07-30_comet_results-presentation-H1-2025.pdf", "H1 2025 results presentation"),
    "PFY25": ("2026-03-06_comet_results-presentation-FY2025.pdf", "FY2025 results presentation"),
    "PHY26": ("2026-07-30_comet_results-presentation-H1-2026.pdf", "H1 2026 results presentation"),
    "CMD21": ("2021-11-14_comet_capital-markets-day-2021.pdf", "Capital Markets Day 2021 deck"),
    "CMD22": ("2022-11-15_comet_capital-markets-day-2022.pdf", "Capital Markets Day 2022 deck"),
    "CMD23": ("2023-11-08_comet_capital-markets-day-2023.pdf", "Capital Markets Day 2023 deck (9 Nov 2023)"),
    "CMD25": ("2026-01-09_comet_capital-markets-day-2025.pdf", "Capital Markets Day 2025 deck (13 Nov 2025)"),
    "PRCMD25": ("2025-11_comet_press-release-CMD-2025.html", "Press release: Capital Markets Day 2025 (13 Nov 2025)"),
    "PRFY25": ("2026-03_comet_press-release-FY2025-results.html", "Press release: FY2025 results (6 Mar 2026)"),
    "TUQ125": ("2025-04_comet_press-release-Q1-2025-trading-update.html", "Trading update Q1 2025 (Apr 2025)"),
    "TUQ325": ("2025-10_comet_press-release-Q3-2025-trading-update.html", "Trading update Q3 2025 (Oct 2025)"),
    "TUQ126": ("2026-04_comet_press-release-Q1-2026-trading-update.html", "Trading update Q1 2026 (Apr 2026)"),
    "TUQ326": ("2026-10_comet_press-release-Q3-2026-trading-update.html", "Trading update Q3 2026 (Oct 2026)"),
}


def manifest():
    m = {}
    for r in csv.DictReader(open(os.path.join(ROOT, SRC, "_manifest.csv"), encoding="utf-8")):
        if r.get("status", "").startswith("RETRIEVED") or r["local_file"] not in m:
            m[r["local_file"]] = (r["url"], r["date"])
    return m


MAN = manifest()


def norm(s):
    s = s.replace("­", "").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    s = s.replace("–", "-").replace("—", "-").replace("ﬁ", "fi").replace("ﬂ", "fl")
    return re.sub(r"\s+", " ", s).strip().lower()


def squash(s):
    return re.sub(r"[^a-z0-9%.]", "", norm(s))


_cache = {}


def pages(key):
    if key not in _cache:
        f = DOCS[key][0]
        tp = os.path.join(ROOT, SRC, "_text", os.path.splitext(f)[0] + ".txt")
        _cache[key] = open(tp, encoding="utf-8", errors="replace").read().split("\f")
    return _cache[key]


def find_page(key, q):
    ps = pages(key)
    hits = [i for i, t in enumerate(ps, 1) if norm(q) in norm(t)]
    if not hits:
        hits = [i for i, t in enumerate(ps, 1) if squash(q) in squash(t)]
    return hits[0] if hits else None


def line(key, start, *contains):
    """Return the whitespace-collapsed text line that starts with `start` and contains all `contains`."""
    for t in pages(key):
        for ln in t.split("\n"):
            c = re.sub(r"\s+", " ", ln).strip()
            if c.startswith(start) and all(x in c for x in contains):
                return c
    raise SystemExit(f"line not found in {key}: {start} {contains}")


ROWS = []


def add(tag, claim, value, unit, pf, pc, key=None, quote="", conf="High", note="", section=None, url=None, doc=None,
        date=None):
    if key:
        f, title = DOCS[key]
        lf = f"{SRC}/{f}"
        u, d = MAN.get(lf, ("", ""))
        doc = doc or title
        date = date or d
        url = url or u
        if quote:
            p = find_page(key, quote)
            if p is None:
                raise SystemExit(f"quote not found {key}: {quote}")
            if f.endswith(".pdf"):
                section = section or f"p{p}"
            else:
                section = section or "press release body"
    else:
        lf = ""
    assert len(quote.split()) <= 25, quote
    ROWS.append(dict(tag=tag, claim=claim, value=value, unit=unit, period_fiscal=pf, period_calendar=pc,
                     document=doc or "", date=date or "", page_or_section=section or "", url=url or "",
                     local_file=lf, quote=quote, confidence=conf, note=note))
    return f"DV-{len(ROWS):03d}"


def seg(key, period, cal, rows, note=""):
    """rows: list of (label_start, contains-list, metric name, value string)."""
    for start, cont, metric, val in rows:
        add("[F]", f"Segment {metric} by division, {period} (note: segment reporting)", val, "CHF thousand",
            period, cal, key, line(key, start, *cont), "High", note)


# ---------------- 1. Segment tables (DV-001..040) ----------------
seg("HY22", "H1 2022", "Jan-Jun 2022", [
    ("External net sales", ["173,470"], "external net sales", "PCT 173,470; IXS 59,716; IXM 34,312; group 267,498"),
    ("Total net sales", ["173,470"], "total net sales", "PCT 173,470; IXS 59,990; IXM 40,985; elim (6,947); group 267,498"),
    ("Segment operating income", ["29,328"], "operating income (EBIT)", "PCT 29,328; IXS (4,185); IXM 3,738; elim (457); group seg 28,424; corporate (715)"),
    ("EBITDA", ["34,289"], "EBITDA", "PCT 34,289; IXS (1,585); IXM 6,149; elim (457); corp (715); group 37,681")],
    "No ebeam segment: ebeam business was divested in 2020 (three segments only from 2021)")
seg("AR22", "FY2022", "Jan-Dec 2022", [
    ("External net sales", ["381,424"], "external net sales", "PCT 381,424; IXS 129,944; IXM 75,026; group 586,395"),
    ("Total net sales", ["381,424", "130,351"], "total net sales", "PCT 381,424; IXS 130,351; IXM 88,643; elim (14,023)"),
    ("Segment operating income", ["94,497"], "operating income (EBIT)", "PCT 94,497; IXS (3,104); IXM 10,868; elim (1,227); corp (2,059)"),
    ("EBITDA", ["104,915"], "EBITDA", "PCT 104,915; IXS 1,607; IXM 15,677; elim (1,227); corp (2,059); group 118,913")])
seg("HY23", "H1 2023", "Jan-Jun 2023", [
    ("External net sales", ["106,791"], "external net sales", "PCT 106,791; IXS 56,784; IXM 43,450; group 207,025"),
    ("Total net sales", ["106,791"], "total net sales", "PCT 106,791; IXS 56,796; IXM 50,830; elim (7,392)"),
    ("Segment operating income", ["344"], "operating income (EBIT)", "PCT 344; IXS (1,957); IXM 8,272; elim (229); corp (1,720)"),
    ("EBITDA", ["5,696"], "EBITDA", "PCT 5,696; IXS 151; IXM 10,375; elim (229); corp (1,720); group 14,275")])
seg("AR23", "FY2023", "Jan-Dec 2023", [
    ("External net sales", ["193,155"], "external net sales", "PCT 193,155; IXS 116,826; IXM 87,472; group 397,453"),
    ("Total net sales", ["193,155", "116,961"], "total net sales", "PCT 193,155; IXS 116,961; IXM 100,258; elim (12,921)"),
    ("Segment operating income", ["7,192"], "operating income (EBIT)", "PCT 7,192; IXS 671; IXM 19,580; elim 761; corp (3,226)"),
    ("EBITDA", ["18,719"], "EBITDA", "PCT 18,719; IXS 4,923; IXM 23,819; elim 761; corp (3,226); group 44,996")])
seg("HY24", "H1 2024", "Jan-Jun 2024", [
    ("External net sales", ["94,257"], "external net sales", "PCT 94,257; IXS 55,138; IXM 39,920; group 189,315"),
    ("Total net sales", ["94,257"], "total net sales", "PCT 94,257; IXS 55,173; IXM 46,472; elim (6,587)"),
    ("Segment operating income", ["3,298"], "operating income (EBIT)", "PCT 3,298; IXS (4,082); IXM 4,971; elim (152); corp (1,344)"),
    ("EBITDA", ["9,111"], "EBITDA", "PCT 9,111; IXS (1,933); IXM 7,298; elim (152); corp (1,344); group 12,980")],
    "H1 2024 comparatives unchanged in the H1 2025 report (not restated)")
seg("AR24", "FY2024 (as first reported)", "Jan-Dec 2024", [
    ("External net sales", ["247,391"], "external net sales", "PCT 247,391; IXS 115,836; IXM 82,135; group 445,362"),
    ("Total net sales", ["247,391", "115,888"], "total net sales", "PCT 247,391; IXS 115,888; IXM 94,571; elim (12,488)"),
    ("Segment operating income", ["40,225"], "operating income (EBIT)", "PCT 40,225; IXS (8,854); IXM 9,474; elim (138); corp (2,478)"),
    ("EBITDA", ["52,734"], "EBITDA", "PCT 52,734; IXS (4,306); IXM 14,567; elim (138); corp (2,478); group 60,380")],
    "Superseded for PCT by restated FY2024 in AR FY2025 (see restated rows)")
seg("AR25", "FY2024 restated", "Jan-Dec 2024", [
    ("Segment operating income restated", ["37,856"], "operating income (EBIT), restated", "PCT 37,856; IXS (8,854); IXM 9,474; group seg 38,338"),
    ("EBITDA restated", ["50,365"], "EBITDA, restated", "PCT 50,365; IXS (4,306); IXM 14,567; group 58,011")],
    "Restatement (AR FY2025 note 02.3) changed only PCT: EBITDA -2,369k vs first report")
seg("HY25", "H1 2025 (as first reported)", "Jan-Jun 2025", [
    ("External net sales", ["134,262"], "external net sales", "PCT 134,262; IXS 48,681; IXM 44,211; group 227,154"),
    ("Total net sales", ["134,262"], "total net sales", "PCT 134,262; IXS 48,689; IXM 48,402; elim (4,199)"),
    ("Segment operating income or (loss)", ["14,955"], "operating income (EBIT)", "PCT 14,955; IXS (9,628); IXM 5,893; elim (80); corp (1,165)"),
    ("EBITDA", ["21,151"], "EBITDA", "PCT 21,151; IXS (7,520); IXM 8,322; elim (80); corp (1,165); group 20,708")],
    "Superseded for PCT by restated H1 2025 in HY26 note 01.1")
seg("HY26", "H1 2025 restated", "Jan-Jun 2025", [
    ("Segment operating income or (loss)", ["17,225"], "operating income (EBIT), restated", "PCT 17,225; IXS (9,628); IXM 5,893; group seg 13,410"),
    ("EBITDA", ["23,421"], "EBITDA, restated", "PCT 23,421; IXS (7,520); IXM 8,322; group 22,978")],
    "Restatement (HY26 note 01.1): PCT EBITDA +2,270k vs first report; sales unchanged")
seg("AR25", "FY2025", "Jan-Dec 2025", [
    ("External net sales", ["257,102"], "external net sales", "PCT 257,102; IXS 110,804; IXM 89,137; group 457,044"),
    ("Total net sales", ["257,102", "110,816"], "total net sales", "PCT 257,102; IXS 110,816; IXM 99,078; elim (9,953)"),
    ("Segment operating income", ["27,807"], "operating income (EBIT)", "PCT 27,807; IXS (11,646); IXM 10,722; elim 263; corp (2,590)"),
    ("EBITDA", ["40,407"], "EBITDA", "PCT 40,407; IXS (7,516); IXM 15,771; elim 263; corp (2,590); group 46,335")],
    "FY2025 is on the corrected basis (opening balances restated)")
seg("HY26", "H1 2026", "Jan-Jun 2026", [
    ("External net sales", ["143,570"], "external net sales", "PCT 143,570; IXS 48,734; IXM 47,530; group 239,834"),
    ("Total net sales", ["143,570"], "total net sales", "PCT 143,570; IXS 48,739; IXM 53,539; elim (6,014)"),
    ("Segment operating income or (loss)", ["22,630"], "operating income (EBIT)", "PCT 22,630; IXS (5,807); IXM 5,793; elim (640); corp (1,585)"),
    ("EBITDA", ["28,947"], "EBITDA", "PCT 28,947; IXS (3,985); IXM 8,630; elim (640); corp (1,585); group 31,367")])
assert len(ROWS) == 40, len(ROWS)

# ---------------- 2. One-offs, restatement (DV-041..054) ----------------
add("[F]", "H1 2022 XP Power trial expense CHF 9.0m (PCT); group adj. EBITDA 46.7m / 17.4%", "9.0", "CHF million",
    "H1 2022", "Jan-Jun 2022", "PHY22", "adj. EBITDA H1 2022 (excl. CHF 9.0 million trial expense) = CHF 46.7 million / adj. EBITDA margin 17.4%")
add("[F]", "FY2022 PCT EBITDA excluding XP Power legal one-off: CHF 113.9m, 29.9% margin (reported 104.9m, 27.5%)", "113.9", "CHF million",
    "FY2022", "Jan-Dec 2022", "AR22", "Comet's trade secrets, EBITDA of the PCT division amounted to CHF 113.9 million, at a margin of 29.9%.")
add("[F]", "Restatement cause 1: CHF 2.1m of stock items erroneously excluded from YE2024 inventory write-down assessment", "2.1", "CHF million",
    "FY2024 / H1 2025", "Dec 2024 / Jan-Jun 2025", "HY26", "certain stock items totaling CHF 2.1 million were erroneously excluded from the assessment",
    note="Effect sits in PCT segment (only PCT segment income changed)")
add("[F]", "Restatement cause 2: CHF 0.3m expenses and liabilities not recognized at YE2024", "0.3", "CHF million",
    "FY2024", "Dec 2024", "HY26", "certain expenses and related liabilities totaling CHF 0.3 mil- lion had erroneously not been recognized",
    note="Hyphenated line break as in source")
add("[F]", "H1 2023 PCT EBITDA includes one-time expenses for cost reduction measures (amount not disclosed)", "", "",
    "H1 2023", "Jan-Jun 2023", "HY23", "one year earlier. This includes one-time expenses for cost reduction measures.",
    note="Amount NOT DISCLOSED, so no ex-one-off margin can be shown")
add("[F]", "H1 2024 PCT margin improvement partly from absence of one-off costs of closing San Jose matchbox volume production (in H1 2023)", "", "",
    "H1 2024", "Jan-Jun 2024", "HY24", "absence of one-off costs from the closure of volume pro duction of matchboxes in San Jose, USA.",
    note="Amount NOT DISCLOSED")
add("[F]", "PCT H1 2023 capacity adaptation: operations headcount reduction of nearly 40%", "~40", "% of PCT operations headcount",
    "H1 2023", "Jan-Jun 2023", "PHY23", "Capacity adaptations: operations headcount")
add("[F]", "PCT short-time working planned for ~150 employees at Flamatt, 14 Aug - end 2023", "150", "employees",
    "H2 2023", "Aug-Dec 2023", "HY23", "short-time working for around 150 employees")
add("[F]", "Q4 2025 fire at Flamatt HQ: ~CHF 2.1m insurance recoveries in other operating income FY2025", "2.1", "CHF million",
    "FY2025 (Q4)", "Oct-Dec 2025", "AR25", "included insurance recoveries of approximately CHF 2.1 million re- lating to this event.",
    note="Segment of the income not stated; impairment of CHF 0.3m allocated to PCT (next row)")
add("[F]", "Fire-related impairment CHF 0.3m allocated to PCT (below EBITDA)", "0.3", "CHF million", "FY2025", "Jan-Dec 2025", "AR25",
    "as a result of the fire incident. The amount relates to the PCT segment.")
add("[F]", "H1 2026 EBITDA includes one-time costs CHF 4.5m (Penang ramp-up + efficiency program); split by division not given", "4.5",
    "CHF million", "H1 2026", "Jan-Jun 2026", "HY26", "EBITDA includes one-time costs of CHF 4.5 million related to the ramp-",
    note="Division split NOT DISCLOSED")
add("[F]", "FY2026 EBITDA margin guidance includes one-off items of ~3pp (Penang, efficiency)", "~3", "pp", "FY2026", "Jan-Dec 2026",
    "HY26", "This EBITDA margin includes one-off items totaling approximately 3 percentage points")
add("[C]", "Efficiency program: sustainable EBITDA improvement CHF 20-30m per year from 2028, fully implemented by end-2027", "20-30",
    "CHF million p.a.", "FY2028", "Jan-Dec 2028", "HY26", "sustainable EBITDA improvement of CHF 20-30 million per year from 2028")
add("[F]", "FY2025 deck shows H1/25 EBITDA margin 9.1% (as first reported) vs H2/25 11.1%", "9.1 / 11.1", "%", "H1 2025 / H2 2025",
    "Jan-Jun / Jul-Dec 2025", "PFY25", "EBITDA margin 9.1% 11.1% 10.1%",
    note="11.1% = FY2025 (corrected basis) minus H1 2025 as first reported; on consistent basis H2 2025 = 10.2% (see [I] row)")

# ---------------- 3. H2 and derived figures ([I]) ----------------
S1 = "research/out/comet/calc/DV_halfyears.py"
H2I = [
    ("H2 2022", "Jul-Dec 2022", "PCT", "sales 208.0; EBIT 65.2; EBITDA 70.6; margin 34.0%", "DV-005..008 minus DV-001..004"),
    ("H2 2022", "Jul-Dec 2022", "IXS", "sales 70.4; EBIT 1.1; EBITDA 3.2; margin 4.5%", "DV-005..008 minus DV-001..004"),
    ("H2 2022", "Jul-Dec 2022", "IXM", "sales 47.7; EBIT 7.1; EBITDA 9.5; margin 20.0%", "DV-005..008 minus DV-001..004"),
    ("H2 2023", "Jul-Dec 2023", "PCT", "sales 86.4; EBIT 6.8; EBITDA 13.0; margin 15.1%", "DV-013..016 minus DV-009..012"),
    ("H2 2023", "Jul-Dec 2023", "IXS", "sales 60.2; EBIT 2.6; EBITDA 4.8; margin 7.9%", "DV-013..016 minus DV-009..012"),
    ("H2 2023", "Jul-Dec 2023", "IXM", "sales 49.4; EBIT 11.3; EBITDA 13.4; margin 27.2%", "DV-013..016 minus DV-009..012"),
    ("H2 2024 (as first reported)", "Jul-Dec 2024", "PCT", "sales 153.1; EBIT 36.9; EBITDA 43.6; margin 28.5%", "DV-021..024 minus DV-017..020"),
    ("H2 2024 (restated)", "Jul-Dec 2024", "PCT", "sales 153.1; EBIT 34.6; EBITDA 41.3; margin 26.9%", "DV-025..026 minus DV-017..020"),
    ("H2 2024", "Jul-Dec 2024", "IXS", "sales 60.7; EBIT -4.8; EBITDA -2.4; margin -3.9%", "DV-021..024 minus DV-017..020"),
    ("H2 2024", "Jul-Dec 2024", "IXM", "sales 48.1; EBIT 4.5; EBITDA 7.3; margin 15.1%", "DV-021..024 minus DV-017..020"),
    ("H2 2025 (consistent basis)", "Jul-Dec 2025", "PCT", "sales 122.8; EBIT 10.6; EBITDA 17.0; margin 13.8% (15.7% if original H1 used)", "DV-033..036 minus DV-027..028, DV-031..032"),
    ("H2 2025", "Jul-Dec 2025", "IXS", "sales 62.1; EBIT -2.0; EBITDA 0.0; margin 0.0%", "DV-033..036 minus DV-027..030"),
    ("H2 2025", "Jul-Dec 2025", "IXM", "sales 50.7; EBIT 4.8; EBITDA 7.4; margin 14.7%", "DV-033..036 minus DV-027..030"),
    ("H2 2025 (consistent basis)", "Jul-Dec 2025", "Group", "sales 229.9; EBITDA 23.4; margin 10.2% (11.1% on mixed basis); ex ~2.1 fire insurance 9.2%", "DV-036 minus DV-032 (group), DV-049"),
]
for pf, pc, div, val, inp in H2I:
    add("[I]", f"{div} results {pf} = FY minus H1 (CHF m; EBITDA margin on total division sales)", val, "CHF million / %", pf, pc,
        note=f"inputs {inp}; script {S1}; confidence High - straight subtraction of audited FY and reviewed/unaudited H1 segment figures",
        conf="High")
add("[I]", "PCT share of group EBITDA by half-year: H1-22 91%, H2-22 87%, H1-23 40%, H2-23 42%, H1-24 70%, H2-24 92% (restated), H1-25 102% (restated), H2-25 73%, H1-26 92%",
    "40-102", "% of group EBITDA", "H1 2022 - H1 2026", "Jan 2022 - Jun 2026",
    note=f"inputs DV-001..040; script {S1}; confidence High - ratio of reported segment EBITDA to group EBITDA (>100% when IXS and corporate negative)")
add("[I]", "PCT EBITDA margin H1 2022 ex CHF 9.0m XP trial expense = 25.0% (reported 19.8%)", "25.0", "%", "H1 2022", "Jan-Jun 2022",
    note=f"inputs DV-002, DV-004, DV-041; script {S1}; confidence High - company slide shows the same 25.0%")
add("[I]", "Group EBITDA margin H1 2026 ex CHF 4.5m one-time costs = 15.0% (reported 13.1%)", "15.0", "%", "H1 2026", "Jan-Jun 2026",
    note=f"inputs DV-040, DV-051; script {S1}; confidence High - simple add-back; division split of the 4.5m not disclosed")
add("[I]", "IXS EBITDA FY2024 before CA20 investment of CHF 10-15m would be CHF 5.7-10.7m (4.9%-9.2%), vs reported -3.7%", "4.9-9.2", "%",
    "FY2024", "Jan-Dec 2024", note=f"inputs DV-022, DV-024, DV-086 (CMD 2025 CA20 CHF 10-15m); script {S1}; confidence Medium - Comet did not call the CA20 spend a one-off; illustration of scale only")

# ---------------- 4. IXS economics ----------------
add("[F]", "IXS sales by market 2021: Electronics 34.0%, Automotive 36.9%, Science/new materials 15.8%, Aerospace 9.8%, Others 3.5% (2020: Electronics 32.8%)",
    "34.0", "% of IXS sales (Electronics)", "FY2021", "Jan-Dec 2021", "AR21", "Sales of X-Ray Systems division by market",
    conf="Medium", note="Percentages read from the chart graphic on the cited page (rendered); caption quoted. Comet category is 'Electronics' - no separate semiconductor share disclosed")
add("[F]", "IXS sales by market 2022: Electronics 44.7%, Automotive 28.9%, Science/new materials 13.4%, Aerospace 9.2%, Others 3.8% (2021 comparatives 34.2/37.0/15.8/9.8/3.2)",
    "44.7", "% of IXS sales (Electronics)", "FY2022", "Jan-Dec 2022", "AR22", "Sales of X-Ray Systems division by market",
    conf="Medium", note="Chart read. 2021 comparative differs from AR2021 (Electronics 34.0 vs 34.2; Automotive 36.9 vs 37.0; Others 3.5 vs 3.2) without explanation")
add("[F]", "IXS sales by market 2023: Electronics 44.1%, Automotive 27.7%, Science/new materials 16.4%, Aerospace 9.0%, Others 2.8%",
    "44.1", "% of IXS sales (Electronics)", "FY2023", "Jan-Dec 2023", "AR23", "Sales of X-Ray Systems division by market",
    conf="Medium", note="Chart read from rendered page")
add("[F]", "IXS sales by market 2024: Electronics 41.2%, Automotive 25.3%, Science/new materials 19.0%, Aerospace 8.7%, Others 5.8%",
    "41.2", "% of IXS sales (Electronics)", "FY2024", "Jan-Dec 2024", "AR24", "division by market",
    conf="Medium", note="Chart read from rendered page (high-resolution crop)")
add("[F]", "IXS sales by market 2025: Electronics 36.0%, Automotive 37.9%, Science/new materials 16.0%, Aerospace 5.6%, Others 4.5%; PCT Semiconductor 93.9% (2024: 91.6%)",
    "36.0", "% of IXS sales (Electronics)", "FY2025", "Jan-Dec 2025", "AR25", "Sales by market",
    conf="Medium", note="Chart read (high-resolution crop). Electronics share fell 41.2->36.0 while automotive rose 25.3->37.9")
add("[F]", "PCT sales by market 2023: Semiconductor 90.6% (2022: 94.1%)", "90.6", "% of PCT sales", "FY2023", "Jan-Dec 2023", "AR23",
    "Sales of Plasma Control Technologies division by market", conf="Medium", note="Chart read from rendered page at low resolution")
add("[F]", "IXS 2023: less profitable volume business still a substantial portion of IXS earnings; realignment not complete", "", "", "FY2023",
    "Jan-Dec 2023", "AR23", "electronics sector is not yet complete, which is why the less profitable")
add("[F]", "IXS 2024: forward-looking investments and still significant contribution from lower margin contracts hit profitability", "", "",
    "FY2024", "Jan-Dec 2024", "AR24", "still significant contribution from lower margin contracts have impact- ed profitability in the short term.")
add("[F]", "IXS 2024: first purchase order for the CA20", "1", "purchase order", "FY2024", "Jan-Dec 2024", "AR24",
    "A significant milestone was achieved with the first purchase order for the CA20.")
add("[C]", "CA20 funnel (CMD 2025): 2025 >60 evaluation, >25 qualification, 5 orders; 2023: 5, 2, 0", "5", "CA20 orders (2025, as of Nov)",
    "FY2025", "Jan-Nov 2025", "CMD25", "2025 >60 >25 5", note="Funnel slide 63; layout-insensitive match")
add("[C]", "More than 80 active collaborations on CA20; >100 engagements on Synertia", "80", "CA20 collaborations", "FY2025", "Nov 2025",
    "PRCMD25", "more than 80 active collaborations on the x-ray system for semiconductor component inspection, CA20")
add("[F]", "Q3 2025: a handful of purchase orders for CA20 from various customers", "", "", "Q3 2025", "Jul-Sep 2025", "TUQ325",
    "a handful of purchase orders for the x-ray system CA20 from various customers")
add("[F]", "FY2025 IXS profitability hit by double-digit million investments in CA20 development and commercialization", "double-digit million",
    "CHF", "FY2025", "Jan-Dec 2025", "PRFY25", "Profitability was impacted by double-digit million investments in the development and commercialization")
add("[C]", "CMD 2025 IXS bridge: CA20 investment CHF 10-15m in 2024 -> above break-even 2028e", "10-15", "CHF million (2024)", "FY2024 / 2028e",
    "Jan-Dec 2024", "CMD25", "CHF 10-15 mn", note="Slide 87 'IXS Non-semi Business and CA20 Both Contribute to 2028 Earnings Improvement'")
add("[C]", "CMD 2025 IXS bridge: CA20 > break-even in 2028e", "> break-even", "", "2028e", "Jan-Dec 2028", "CMD25", "CA20 > break-even")
add("[C]", "CMD 2025 IXS bridge: non-semi EBITDA margin 5%-10% (2024) -> >10% (2028e)", "5-10 -> >10", "% EBITDA margin", "FY2024 / 2028e",
    "", "CMD25", "Non-semi 5% – 10% > 10%")
add("[C]", "CMD 2025 IXS EBITDA margin: -3.7% (2024) -> 5%-9% (2028e)", "5-9", "% EBITDA margin", "2028e", "Jan-Dec 2028", "CMD25",
    "Total IXS –3.7% 5% – 9%")
add("[F]", "H1 2026: IXS more than doubled number of CA20 purchase orders", "", "", "H1 2026", "Jan-Jun 2026", "HY26",
    "more than doubling the number of purchase orders for the CA20 x-ray system")
add("[C]", "H1 2026: break-even point for CA20 still projected for 2028", "2028", "year", "H1 2026", "Jan-Jun 2026", "HY26",
    "The break-even point for CA20 is still projected for 2028.")
add("[F]", "IXS goodwill (CGU IXS) CHF 20.2m at YE2023; plan growth 13.3% p.a. 2024-2026 (prior 22.2%)", "20,226", "CHF thousand", "FY2023",
    "Dec 2023", "AR23", "2024 to 2026 is assumed to be 13.3% for IXS (prior year: 22.2%)")
add("[F]", "IXS goodwill CHF 20.4m at YE2024; impairment test assumes 17.4% p.a. sales growth 2025-2027; no impairment", "17.4",
    "% p.a. assumed IXS sales growth", "FY2024", "Dec 2024", "AR24", "2025 to 2027 is assumed to be 17.4% for IXS (prior year: 13.3%)",
    note="Actual IXS FY2025 sales growth -4.4%")
add("[F]", "IXS goodwill CHF 19.9m at YE2025; pre-tax WACC 11.4% (8.8%); no reasonably possible change causes impairment", "19,869",
    "CHF thousand", "FY2025", "Dec 2025", "AR25", "Discount rate (WACC) before tax 11.4% 8.8% 10.0% 9.0%",
    note="No IXS impairment recognized 2022-2025; growth assumptions no longer disclosed in AR2025")
add("[F]", "IXS employees at year-end: 430 (2022)", "430", "employees", "FY2022", "Dec 2022", "AR22",
    line("AR22", "Number of employees at year-end", "998"))
add("[F]", "IXS employees at year-end: 506 (2024) vs 463 (2023)", "506", "employees", "FY2024", "Dec 2024", "AR24",
    line("AR24", "Number of employees at year-end", "942"), note="FY2025 segment note gives no headcount by division")

# ---------------- 5. IXS strategic statements chronology ----------------
add("[C]", "CMD 2021: IXS repositioning on track; rigorous focus on high quality business", "", "", "Nov 2021", "Nov 2021", "CMD21",
    "IXS: repositioning on track")
add("[C]", "H1 2022: strategic realignment of IXS toward semi/electronics and advanced packaging continues as planned", "", "", "H1 2022",
    "Jul 2022", "HY22", "The strategic realignment of the X-Ray Systems division with the ex pansion of its presence in the semiconductor/electronics market")
add("[C]", "CMD 2022: IXS portfolio transformation on track; financial improvement back-end loaded toward 2025 targets", "", "", "Nov 2022",
    "Nov 2022", "CMD22", "Improvement in financial performance back-end loaded towards 2025 targets")
add("[F]", "FY2022: IXS sales fell partly due to focus on higher-return semi/electronics orders instead of less profitable volume business", "", "",
    "FY2022", "Jan-Dec 2022", "AR22", "IXS's focus on winning higher-return orders in the semiconductor and electronics market instead of less profitable volume business")
add("[F]", "H1 2023: ORS (Dragonfly software, acquired Dec 2020) fully integrated into IXS to cut cost base", "", "", "H1 2023", "Jan-Jun 2023",
    "HY23", "IXS has fully integrated Object Research Systems (ORS)")
add("[C]", "CMD 2023 IXS growth plan: focus on more profitable sales; serve legacy opportunistically", "", "", "Nov 2023", "Nov 2023", "CMD23",
    "serve legacy opportunistically")
add("[F]", "H1 2024: IXS sales stagnant due to sluggish auto, price pressure and discontinuation of low-margin products", "", "", "H1 2024",
    "Jan-Jun 2024", "HY24", "discontinuation of low-margin products")
add("[C]", "FY2024 chair/CEO letter: IXS semiconductor focus pursued with unwavering commitment", "", "", "FY2024", "Mar 2025", "AR24",
    "ductor and electronics industry has been pursued with unwavering commitment.")
add("[F]", "H1 2025: Comet decided strategic changes at IXS - organizational adjustments and cost reductions focused on traditional markets", "", "",
    "H1 2025", "Jul 2025", "HY25", "While cost reductions are focused on activities linked to traditional markets")
add("[F]", "H1 2025 deck: IXS strategic realignment to drive workforce reduction measures; cost efficiency program", "", "", "H1 2025", "Jul 2025",
    "PHY25", "IXS division to undergo a cost efficiency program")
add("[C]", "CMD 2025: IXS profitability enhancement via restructuring in traditional markets", "", "", "Nov 2025", "13 Nov 2025", "CMD25",
    "Profitability enhancement via restructuring in")
add("[C]", "CMD 2025: efficiency gains include restructuring non-semi IXS", "", "", "Nov 2025", "13 Nov 2025", "CMD25", "− restructuring non-semi IXS")
add("[C]", "CMD 2025: turnaround or phasing-out of unprofitable activities, especially non-Semi", "", "", "Nov 2025", "13 Nov 2025", "CMD25",
    "• Turnaround or phasing-out unprofitable")
add("[C]", "CMD 2025: IXS profitability drivers = downsizing low-profitability businesses, right-sizing cost base, CA20", "", "", "Nov 2025",
    "13 Nov 2025", "CMD25", "• Operating leverage, price/mix, • Downsizing low-profitability • Volume growth, efficiency")
add("[F]", "FY2025 results release: IXS restructuring measures initiated in the third quarter [2025]", "Q3 2025", "", "FY2025", "Mar 2026", "PRFY25",
    "The positive impact of the restructuring measures initiated in the third quarter will have its full effect in the upcoming quarters.",
    note="Conflicts with AR2025 ('fourth quarter of 2025') and HY26 ('last quarter of 2025')")
add("[F]", "AR2025: restructuring program at IXS in Hamburg initiated in Q4 2025 to support pivot into semiconductor equipment", "Q4 2025", "",
    "FY2025", "Oct-Dec 2025", "AR25", "In the fourth quarter of 2025, we initiated a restructuring program at",
    note="Restructuring cost, headcount and provision NOT DISCLOSED (provisions note 23 shows only warranties/other)")
add("[C]", "AR2025: comprehensive strategic review in 2025 reaffirmed core focus", "", "", "FY2025", "2025", "AR25",
    "Following a comprehensive strategic review in 2025, Comet reaffirmed")
add("[C]", "AR2025: product-line profitability review; focused actions rather than large structural exits", "", "", "FY2025", "Mar 2026", "AR25",
    "These fo- cused actions, rather than large structural exits, are designed to en- hance profitability")
add("[F]", "FY2025 deck: IXS 'Restructuring to sharpen semi focus'; 'IXS faces weak profitability, prioritizing growth investments'", "", "",
    "FY2025", "Mar 2026", "PFY25", "Restructuring to sharpen semi focus")
add("[F]", "H1 2026: restructuring measures implemented in last quarter of 2025 improved IXS profitability", "", "", "H1 2026", "Jan-Jun 2026",
    "HY26", "Restructuring measures imple- mented in the last quarter of 2025 have contributed to improved prof- itability.")
add("[C]", "H1 2026: IXS remains committed to downsizing low-margin businesses, right-sizing costs, focusing on CA20", "", "", "H1 2026", "Jul 2026",
    "HY26", "The division remains committed to its strategy of downsiz- ing low-margin businesses, right-sizing costs, and focusing on the CA20")
add("[C]", "Q3 2026: CA20 orders/qualifications reinforce confidence in sustained growth for IXS in semiconductor market", "", "", "Q3 2026",
    "Jul-Sep 2026", "TUQ326", "reinforce our confidence in sustained growth for IXS in the semiconductor market")

# ---------------- 6. PCT concentration and share ----------------
for key, yr, val, q in [
    ("AR21", "FY2021", "156 / 30.4% (FY2020: 128 / 32.4%)", "recorded sales of CHF 156 million with its largest customer, which rep"),
    ("AR22", "FY2022", "211 / 36.1%", "recorded sales of CHF 211 million with its largest customer, which rep"),
    ("AR23", "FY2023", "71 / 17.7%", "recorded sales of CHF 71 million with its largest customer, which repre"),
    ("AR24", "FY2024", "106 / 23.8%", "recorded sales of CHF 106 million with its largest customer, which rep-"),
    ("AR25", "FY2025", "104.4 / 22.8% (FY2024: 106.2 / 23.8%)", "recorded sales of CHF 104.4 million with its largest customer, which")]:
    add("[F]", f"PCT sales with its largest customer, {yr} (CHF m / % of Group sales; customer not named)", val, "CHF million / % of group",
        yr, f"Jan-Dec {yr[2:]}", key, q, note="Note 'Sales with key accounts'; customer name NOT DISCLOSED")
add("[I]", "Largest customer as % of PCT external sales: FY2021 51.0%, FY2022 55.3%, FY2023 36.8%, FY2024 42.9%, FY2025 40.6%", "36.8-55.3",
    "% of PCT sales", "FY2021-FY2025", "Jan 2021 - Dec 2025",
    note="inputs DV-119..123 and PCT external sales (FY2021 306.1 from AR FY2022 comparative; DV-005, DV-013, DV-021, DV-033); script research/out/comet/calc/DV_halfyears.py; confidence High - simple ratio; customer identity not disclosed")
add("[F]", "CMD 2023: competitors across plasma chain - Advanced Energy and MKS Instruments (matchboxes and RF generators), Trumpf, Meiden, Daihen", "", "",
    "Nov 2023", "Nov 2023", "CMD23", "Advanced Energy X X")
add("[C]", "CMD 2023: PCT #1 with ~40% market share in matchboxes and ~70% in vacuum capacitors", "40 / 70", "% market share", "FY2023", "Nov 2023",
    "CMD23", "∼40% / ∼70% market share", note="Slide 72: '#1 ... Matchboxes / Vacuum Capacitors'; Comet's own estimate, source not given")
add("[C]", "CMD 2025: PCT #1 in vaccaps & matches", "#1", "rank", "FY2024", "Nov 2025", "CMD25", "in Vaccaps")
add("[C]", "CMD 2022: RF generator market 2025e ~USD 1.7bn, Synertia targeted market share by 2025 ~10%", "~10", "% RF generator share target 2025",
    "Nov 2022", "Nov 2022", "CMD22", "Market for RF generators in 2025e: ~USD 1.7 bn, targeted market share by 2025: ~10%",
    note="No later disclosure of achieved RF generator share (NOT DISCLOSED in AR2025/CMD 2025)")
add("[C]", "H1 2022 priorities: expand market share in RF matchbox, maintain vaccaps share", "", "", "H1 2022", "Jul 2022", "PHY22",
    "expand market share in RF matchbox, maintain vaccaps share")
add("[C]", "FY2022: growing market share in vacuum capacitors and matchboxes", "", "", "FY2022", "Jan-Dec 2022", "PFY22",
    "Growing market share in vacuum")
add("[C]", "H1 2025: PCT double-digit growth highlights market share gains in a WFE market growing single-digit", "", "", "H1 2025",
    "Jan-Jun 2025", "HY25", "share gains in a WFE market growing at a single-digit rate")
add("[C]", "CMD 2025 Synertia RFG funnel: >50 evaluation, >30 qualification, 15 HVM orders (2023: 11, 9, 0); >100 active engagements", "15",
    "HVM orders", "FY2025", "Nov 2025", "CMD25", ">50 >30 15")
add("[C]", "CMD 2025: etch top three players hold ~80% of market; deposition top two ~70% (OEM concentration PCT sells into)", "80 / 70", "%",
    "FY2024", "Nov 2025", "CMD25", "Top three players hold Top two players hold", note="Source: Gartner per slide 68")
add("[C]", "CMD 2023 PCT resilience: influence customer mix, less dependent on Memory", "", "", "Nov 2023", "Nov 2023", "CMD23",
    "influence customer mix, less dependent on Memory")
add("[F]", "H1 2026: PCT book-to-bill above Group average (Group 1.48)", ">1.48", "book-to-bill", "H1 2026", "Jan-Jun 2026", "HY26",
    "With a book-to-bill ratio above the Group average")
add("[C]", "Q3 2026: CEO cites market share gains from new products", "", "", "Q3 2026", "Jul-Sep 2026", "TUQ326",
    "market share gains from new products")

# ---------------- 7. Targets ----------------
S2 = "research/out/comet/calc/DV_targets.py"
add("[C]", "CMD 2025 target: net sales CHF 670-770m at next cycle peak (from CHF 800-900m)", "670-770", "CHF million", "peak of cycle (2028e)",
    "Jan-Dec 2028", "PRCMD25", "Net sales of CHF 670 million to CHF 770 million (from CHF 800 million to CHF 900 million)")
add("[C]", "CMD 2025 target: EBITDA margin 22-27% (previously 25-30%)", "22-27", "% of net sales", "peak of cycle (2028e)", "Jan-Dec 2028",
    "PRCMD25", "EBITDA margin between 22% and 27% of net sales (previously 25% to 30%)")
add("[C]", "CMD 2025 target: ROCE 27-32% (from 30-35%)", "27-32", "%", "peak of cycle (2028e)", "Jan-Dec 2028", "PRCMD25",
    "Return on capital employed (ROCE) of 27% to 32% (from 30% to 35%)")
add("[C]", "CMD 2025: peak of cycle now expected 2028 (previously 2027); USD/CHF 0.70 (previously 0.90)", "2028", "year", "", "", "PRCMD25",
    "new assumption for the USD/CHF exchange rate of 0.70 (previously 0.90)")
add("[C]", "CMD 2025 divisional 2028e sales: PCT 430-480 (2024: 247), IXS 130-160 (116), IXM 110-130 (95)", "PCT 430-480; IXS 130-160; IXM 110-130",
    "CHF million", "2028e", "Jan-Dec 2028", "CMD25", "247 to 480 116 to 160 95 to 130",
    conf="Medium", note="Slide 86; lower bounds 430/130/110 on the line above in the text layout")
add("[C]", "CMD 2025 divisional 2028e EBITDA margin: PCT 27-33% (2024: 21%), IXS 5-9% (-4%), IXM 23-27% (15%)", "PCT 27-33; IXS 5-9; IXM 23-27",
    "% EBITDA margin", "2028e", "Jan-Dec 2028", "CMD25", "EBITDA +6 PP to +9 PP",
    conf="Medium", note="Slide 86 layout scrambled in text; values read from slide; baselines use FY2024 as first reported (PCT 21.3%, group 13.6%)")
add("[C]", "CMD 2025 share of group sales at peak: PCT ~60-70%, IXS ~15-25%, IXM ~10-20%", "PCT 60-70", "% of group sales", "2028e", "",
    "CMD25", "PCT: ∼ 60%-70% Above group average")
add("[C]", "CMD 2023 target for next peak (seen 2027): net sales CHF 800-900m, EBITDA 25-30%, ROCE 30-35%", "800-900", "CHF million",
    "peak of cycle (2027e)", "Jan-Dec 2027", "CMD23", "CHF 800 million to 900 million")
add("[C]", "CMD 2023 assumption: peak of semiconductor cycle seen in 2027; previous 2025 targets (2019): >CHF 830m, ~25% EBITDA, ~30% ROCE", "2027",
    "year", "", "", "CMD23", "Previous targets 2025 issued in 2019: Net sales > CHF 830 million / EBITDA margin of ∼25% / ROCE of ∼30%")
add("[C]", "CMD 2023 divisional share at peak: PCT 60-70%, IXS 20-25%, IXM 10-15%", "IXS 20-25", "% of group sales", "2027e", "", "CMD23",
    "IXS: 20%–25% Below group average")
add("[F]", "FY2025 ROCE 5.2% (FY2024 restated 9.7%)", "5.2", "%", "FY2025", "Jan-Dec 2025", "AR25", "decreased to 5.2% (previous year: 9.7%).")
add("[F]", "FY2026 guidance raised (Oct 2026): net sales CHF 570-590m, reported EBITDA margin 17.0-19.0% incl. up to 3pp one-time costs", "570-590 / 17-19",
    "CHF million / %", "FY2026", "Jan-Dec 2026", "TUQ326", "For FY26, Comet expects net sales of CHF 570 – 590 million, with a reported EBITDA margin of 17.0% – 19.0%.")
add("[I]", "Gap to CMD 2025 targets from FY2025: sales +213 to +313 CHF m (CAGR 13.6-19.0% needed 2025-28); EBITDA margin +11.9 to +16.9pp; ROCE +21.8 to +26.8pp",
    "13.6-19.0", "% CAGR required", "FY2025 -> 2028e", "", note=f"inputs DV-033..036, CMD rows, ROCE row; script {S2}; confidence High - arithmetic on stated targets")
add("[I]", "LTM Jul-2025-Jun-2026 (corrected basis): group sales 469.7, EBITDA 11.7%; PCT 266.4 / 17.2%; IXS 110.9 / -3.6%; IXM 104.2 / 15.4%", "11.7",
    "% group EBITDA margin", "LTM H1 2026", "Jul 2025 - Jun 2026", note=f"inputs DV-031..040; script {S2}; confidence High")
add("[I]", "Divisional gaps to CMD 2025 2028e: PCT margin +9.8 to +15.8pp vs LTM, sales CAGR 18.7-23.1% needed; IXS margin +8.6 to +12.6pp; IXM margin +7.6 to +11.6pp",
    "", "pp", "LTM H1 2026 -> 2028e", "", note=f"inputs LTM row, CMD 2025 divisional rows; script {S2}; confidence Medium - divisional targets read from scrambled slide text")
add("[I]", "Gap to CMD 2023 peak targets (800-900, 25-30%, 30-35%) from FY2025: sales -343 to -443, margin -14.9 to -19.9pp; targets cut 15.3% at sales midpoint in Nov 2025",
    "-15.3", "% change of sales midpoint", "FY2025", "", note=f"inputs CMD 2023 rows, DV-036; script {S2}; confidence High")

# ---------------- 8. Quarters / trading updates ----------------
add("[F]", "Q1 2025: all divisions double-digit revenue growth y/y, led by PCT", "", "", "Q1 2025", "Jan-Mar 2025", "TUQ125",
    "All divisions reported double-digit revenue growth compared to the previous year, led by the Plasma Control Technologies (PCT) division.")
add("[F]", "Q3 2025: sales decline mainly from lower PCT activity", "", "", "Q3 2025", "Jul-Sep 2025", "TUQ325",
    "The decline in Q3/25 net sales was primarily due to lower business activity in the Plasma Control Technologies (PCT) division")
add("[F]", "H1 2025: slowdown in PCT incoming orders; some orders deferred from Q3/Q4 2025 to FY26", "", "", "H1 2025", "Jun-Jul 2025", "HY25",
    "with some orders being deferred from Q3 and Q4 to FY26.")
add("[F]", "Q1 2026: lower revenues in PCT and IXS; IXM solid growth", "", "", "Q1 2026", "Jan-Mar 2026", "TUQ126",
    "primarily driven by lower revenues in the PCT and IXS divisions, while IXM delivered solid growth")
add("[F]", "Q1 2026: book-to-bill 1.4 supported by all divisions, PCT benefiting most", "1.4", "book-to-bill (group)", "Q1 2026", "Jan-Mar 2026",
    "TUQ126", "supported by all divisions, with PCT benefiting most from the unfolding semiconductor cycle")
add("[F]", "Q3 2026: IXS net sales slightly lower than strong Q3 2025; PCT drove growth", "", "", "Q3 2026", "Jul-Sep 2026", "TUQ326",
    "the X-Ray Systems (IXS) division recorded slightly lower net sales than in the strong corresponding quarter of the previous year")
add("[F]", "Q3 2026: incoming orders and backlog rose across all divisions; book-to-bill 1.77", "1.77", "book-to-bill (group)", "Q3 2026",
    "Jul-Sep 2026", "TUQ326", "Incoming orders and the order backlog continued to rise across all divisions")
add("[S]", "Q3 2023 trading update (newswire copy): IXS sales fell significantly; order intake below expectations at IXS and IXM; PCT order intake persistently low",
    "", "", "Q3 2023", "Jul-Sep 2023", None, "", "Medium",
    "Original comet.tech page NOT RETRIEVED (Wayback snapshot exists; web.archive.org connection reset). Lead only; no local file",
    section="web copy", url="https://ca.marketscreener.com/quote/stock/COMET-HOLDING-AG-34658185/news/Comet-adjusts-full-year-guidance-after-Q3-below-expectations-45097446/",
    doc="EQS ad hoc via MarketScreener, 19 Oct 2023", date="2023-10-19")
add("[S]", "Q1 2024 trading update (newswire copy): both X-ray divisions IXS and IXM had lower sales y/y; group book-to-bill 1.09", "1.09",
    "book-to-bill (group)", "Q1 2024", "Jan-Mar 2024", None, "", "Medium",
    "Original NOT RETRIEVED; lead only", section="web copy",
    url="https://wallstreet-online.de/nachricht/17998961-comet-confirms-guidance-despite-the-expected-slow-start-to-the-financial-year",
    doc="EQS release via wallstreet-online, 19 Apr 2024", date="2024-04-19")
add("[S]", "Q3 2024 trading update (newswire copy): subdued business in both X-ray divisions; further commercial negotiations for CA20 initiated", "", "",
    "Q3 2024", "Jul-Sep 2024", None, "", "Medium",
    "Original comet.tech page NOT RETRIEVED (Wayback snapshot 2026-06-16 exists; connection reset); lead only", section="web copy",
    url="https://finanzen.net/nachricht/aktien/comet-gradual-recovery-in-the-semiconductor-cycle-in-q3-13927547",
    doc="EQS release via finanzen.net, 18 Oct 2024", date="2024-10-18")
add("[S]", "Lam Research is a PCT customer (Comet PCT news: ESG award from 'Lam Research, our valuable customer'); not confirmed as largest customer", "", "",
    "", "", None, "", "Low", "Search-result snippet only; page not saved; AR2023 mentions an ESG award 'from one of our largest customers' without naming it",
    section="web search snippet", url="https://pct.comet.tech/en/news", doc="pct.comet.tech news (snippet)", date="")

os.makedirs(os.path.dirname(OUT), exist_ok=True)
with open(OUT, "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=HDR)
    w.writeheader()
    for i, r in enumerate(ROWS, 1):
        r["id"] = f"DV-{i:03d}"
        w.writerow(r)
from collections import Counter
print(len(ROWS), "rows", Counter(r["tag"] for r in ROWS))
for i, r in enumerate(ROWS, 1):
    print(f"DV-{i:03d} {r['tag']} {r['claim'][:90]}")
