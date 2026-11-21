#!/usr/bin/env python3
"""Build out/nova/parts/A1..A6.csv (Module A evidence rows) for Nova Ltd.

Usage: python3 -I research/out/nova/calc/build_parts_A.py
Release figures come from quarterly_items.csv (parse_releases.py); every quote is validated
against the saved document by evrow.row(). Derived figures ([I]) cite calc/metrics.py outputs.
FY = calendar year. Periods: FQ4 FY2025 = Oct-Dec 2025 ... FQ3 FY2026 = Jul-Sep 2026.
"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evrow import row, write

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(HERE, "..", "parts")
items = {}
for r in csv.DictReader(open(os.path.join(HERE, "quarterly_items.csv"))):
    items[(r["quarter"], r["item"])] = r

REL = {"Q4-2025": ("2026-02-12_nova_results-release-Q4-2025.pdf", "2026-02-12", "FQ4 FY2025", "Oct-Dec 2025"),
       "Q1-2026": ("2026-05-14_nova_results-release-Q1-2026.pdf", "2026-05-14", "FQ1 FY2026", "Jan-Mar 2026"),
       "Q2-2026": ("2026-08-06_nova_results-release-Q2-2026.pdf", "2026-08-06", "FQ2 FY2026", "Apr-Jun 2026"),
       "Q3-2026": ("2026-11-05_nova_results-release-Q3-2026.pdf", "2026-11-05", "FQ3 FY2026", "Jul-Sep 2026"),
       "Q3-2025": ("2025-11-06_nova_results-release-Q3-2025.pdf", "2025-11-06", "FQ3 FY2025", "Jul-Sep 2025"),
       "Q2-2025": ("2025-08-07_nova_results-release-Q2-2025.pdf", "2025-08-07", "FQ2 FY2025", "Apr-Jun 2025"),
       "Q1-2025": ("2025-05-08_nova_results-release-Q1-2025.pdf", "2025-05-08", "FQ1 FY2025", "Jan-Mar 2025"),
       "Q4-2024": ("2025-02-13_nova_results-release-Q4-2024.pdf", "2025-02-13", "FQ4 FY2024", "Oct-Dec 2024"),
       "Q3-2024": ("2024-11-07_nova_results-release-Q3-2024.pdf", "2024-11-07", "FQ3 FY2024", "Jul-Sep 2024")}
F20 = "2026-02-17_nova_20-F-FY2025.pdf"
F20_24 = "2025-02-20_nova_20-F-FY2024.pdf"
F20_23 = "2024-02-20_nova_20-F-FY2023.pdf"
IDD = "2025-03-13_nova_investor-day-2025-presentation.pdf"
TR = {"Q4-2025": "2026-02-12_stockanalysis_transcript-Q4-2025-call.html",
      "Q1-2026": "2026-05-14_stockanalysis_transcript-Q1-2026-call.html",
      "Q2-2026": "2026-08-06_stockanalysis_transcript-Q2-2026-call.html",
      "Q3-2026": "2026-11-05_stockanalysis_transcript-Q3-2026-call.html"}


def q2(line, n):
    """Label + first n numeric tokens of a statement line (whitespace-normalised)."""
    toks = line.split()
    out, k = [], 0
    for t in toks:
        out.append(t)
        if any(c.isdigit() for c in t):
            k += 1
            if k == n:
                break
    return " ".join(out)


def rel_row(rid, q, item, claim, unit="USD k", n=2, note=""):
    it = items[(q, item)]
    f, d, pf, pc = REL[q]
    v = float(it["value"])
    return row(rid, "[F]", claim, f"{v:,.0f}" if unit == "USD k" else f"{v}", unit, pf, pc,
               f"Nova results release {pf}", d, f, q2(it["line"], n), "", note)


A1, A2, A3, A4, A5, A6 = [], [], [], [], [], []
n = 0
def nid(prefix, lst):
    return f"{prefix}-{len(lst) + 1:03d}"

# ---------------- A1 results: last four quarters ----------------
for q in ("Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026"):
    f, d, pf, pc = REL[q]
    it = items[(q, "rev_products")]; its = items[(q, "rev_services")]
    quote = q2(it["line"], 2) + " " + q2(its["line"], 2)
    # products and services lines are consecutive in the release; validate as one quote
    try:
        A1.append(row(nid("A1", A1), "[F]", f"Revenue {pf}: products and services (total in value)",
                      f"total {float(items[(q,'rev_total')]['value']):,.0f}; products {float(it['value']):,.0f}; services {float(its['value']):,.0f}",
                      "USD k", pf, pc, f"Nova results release {pf}", d, f, quote, "", "first column = three months; second = same quarter prior year"))
    except SystemExit:
        A1.append(rel_row(nid("A1", A1), q, "rev_products", f"Product revenue {pf}"))
        A1.append(rel_row(nid("A1", A1), q, "rev_services", f"Service revenue {pf}"))
    A1.append(rel_row(nid("A1", A1), q, "rev_total", f"Total revenue {pf} (second number = same quarter prior year)"))
    A1.append(rel_row(nid("A1", A1), q, "gross_profit", f"GAAP gross profit {pf}"))
    A1.append(rel_row(nid("A1", A1), q, "op_income", f"GAAP operating income {pf}"))
    A1.append(rel_row(nid("A1", A1), q, "ng_gross_profit", f"Non-GAAP (company-adjusted) gross profit {pf}", n=1,
                      note="adds back stock-based compensation and amortization of acquired intangibles (and step-up where listed)"))
    A1.append(rel_row(nid("A1", A1), q, "ng_op_income", f"Non-GAAP (company-adjusted) operating income {pf}", n=1))
    A1.append(rel_row(nid("A1", A1), q, "cfo", f"Net cash provided by operating activities {pf}"))
    A1.append(rel_row(nid("A1", A1), q, "capex", f"Purchase of property and equipment {pf}"))
    A1.append(rel_row(nid("A1", A1), q, "sbc", f"Share-based compensation {pf}"))

# FY2025 from the audited 20-F
A1 += [
    row(nid("A1", A1), "[F]", "FY2025 revenue by type: products and services", "products 705,598; services 174,979; total 880,577", "USD k", "FY2025", "Jan-Dec 2025",
        "Nova Form 20-F FY2025, consolidated statements of operations", "2026-02-17", F20, "Products 705,598 538,350 405,037 Services 174,979 134,046 112,885 Total revenues 880,577 672,396 517,922", "", "columns 2025, 2024, 2023"),
]
A1.append(row(nid("A1", A1), "[F]", "FY2025 cost of revenues by type (products, services)", "products 282,127; services 93,250", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025", "2026-02-17", F20, "Products 282,127 210,639 163,981 Services 93,250 74,671 60,764", "", "used for product vs service gross margin in calc"))
A1.append(row(nid("A1", A1), "[F]", "FY2025 GAAP gross profit and operating income", "gross profit 505,200; operating income 253,468", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025", "2026-02-17", F20, "Gross profit 505,200 387,086 293,177", ""))
A1.append(row(nid("A1", A1), "[F]", "FY2025 GAAP operating income", "253,468", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025", "2026-02-17", F20, "Operating income 253,468 187,540 132,263", ""))
A1.append(row(nid("A1", A1), "[F]", "FY2025 operating cash flow", "245,613", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025", "2026-02-17", F20, "Net cash provided by operating activities 245,613 235,266 123,531", ""))
A1.append(row(nid("A1", A1), "[F]", "FY2025 capital expenditure", "27,698", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025", "2026-02-17", F20, "Purchase of property, plant and equipment (27,698) (17,215) (17,188)", ""))
A1.append(row(nid("A1", A1), "[F]", "FY2025 share-based compensation", "26,291", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025", "2026-02-17", F20, "Share-based compensation 26,291 25,209 18,286", ""))
f, d = REL["Q4-2025"][0], REL["Q4-2025"][1]
A1.append(row(nid("A1", A1), "[F]", "FY2025 non-GAAP (company-adjusted) gross profit and operating income", "non-GAAP GP 523,129; non-GAAP OI 291,976", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova results release FQ4 FY2025 (annual reconciliation)", d, f, "Non-GAAP gross profit 523,129 399,383", "", "non-GAAP OI 291,976 on the same page"))
A1.append(row(nid("A1", A1), "[F]", "One-off items management itself named in FY2025 reconciliation: acquisition inventory step-up 2,258; acquisition expenses 859; discrete tax reserve release 203 (in OI)", "2,258; 859; 203", "USD k", "FY2025", "Jan-Dec 2025",
              "Nova results release FQ4 FY2025 (annual reconciliation)", d, f, "Acquisition related inventory step-up 2,258 -", "", "acquisition expenses 859 and discrete tax reserve release 203 on same page"))
A1.append(row(nid("A1", A1), "[F]", "One-off item in FQ4 FY2025 reconciliation: discrete tax reserve release, net (203 in operating income; -4,229 in net income)", "203 / -4,229", "USD k", "FQ4 FY2025", "Oct-Dec 2025",
              "Nova results release FQ4 FY2025", d, f, "Discrete tax reserve release, net 203", "", "no acquisition step-up or acquisition expenses in FQ1-FQ3 FY2026 reconciliations"))
A1.append(row(nid("A1", A1), "[S]", "Opex rise in FQ3 FY2026 partly from 'costs related to ongoing strategic evaluations' (named by CFO; not quantified, not excluded from non-GAAP)", "not quantified", "", "FQ3 FY2026", "Jul-Sep 2026",
              "Third-party transcript of Nova Q3 2026 call (stockanalysis.com)", "2026-11-05", TR["Q3-2026"], "as well as costs related to ongoing strategic evaluations", "", "management statement; amount NOT DISCLOSED"))

# derived metrics (calc/metrics.py -> quarterly_metrics.csv, summary.txt)
qm = {r["quarter"]: r for r in csv.DictReader(open(os.path.join(HERE, "quarterly_metrics.csv")))}
for q in ("Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026"):
    r = qm[q]; pf, pc = REL[q][2], REL[q][3]
    A1.append(row(nid("A1", A1), "[I]", f"{pf}: revenue YoY; gross margin GAAP / non-GAAP / ex one-offs; operating margin GAAP / non-GAAP / ex one-offs",
                  f"YoY {r['yoy_pct']}%; GM {r['gm_gaap_pct']} / {r['gm_nongaap_pct']} / {r['gm_ex_oneoffs_pct']}%; OM {r['om_gaap_pct']} / {r['om_nongaap_pct']} / {r['om_ex_oneoffs_pct']}%",
                  "%", pf, pc, "calc/metrics.py -> calc/quarterly_metrics.csv", "2026-11-21", "", "", "High",
                  "inputs: release rows above (revenue, GP, OI, non-GAAP GP/OI, prior-year quarter revenue); one-offs = management-named acquisition/discrete items only; High because simple ratios of printed figures"))
    A1.append(row(nid("A1", A1), "[I]", f"{pf}: free cash flow (CFO minus capex) and SBC/FCF", f"FCF {float(r['fcf_k']):,.0f}; SBC {float(r['sbc_k']):,.0f}; SBC/FCF {r['sbc_to_fcf_pct']}%",
                  "USD k / %", pf, pc, "calc/metrics.py -> calc/quarterly_metrics.csv", "2026-11-21", "", "", "High",
                  "inputs: CFO, capex, SBC rows above; FCF definition is ours (Nova's CFO quotes the same FCF on calls)"))
A1.append(row(nid("A1", A1), "[I]", "LTM (Oct 2025-Sep 2026) revenue, YoY, margins, FCF, SBC/FCF",
              "revenue 1,000,731 (+17.4% vs Oct 2024-Sep 2025); GM GAAP 57.4% / non-GAAP 59.0%; OM GAAP 30.0% / non-GAAP 33.8%; FCF 254,539; SBC/FCF 11.0%",
              "USD k / %", "FQ4 FY2025-FQ3 FY2026", "Oct 2025-Sep 2026", "calc/metrics.py -> calc/summary.txt", "2026-11-21", "", "", "High",
              "sum of four quarterly releases; no one-offs named in these four quarters except 203k (FQ4 FY2025), immaterial"))
A1.append(row(nid("A1", A1), "[I]", "FY2025 margins and FCF: GM GAAP / non-GAAP / ex one-offs; OM GAAP / non-GAAP / ex one-offs; FCF; SBC/FCF; product vs service gross margin",
              "GM 57.4 / 59.4 / 57.6%; OM 28.8 / 33.2 / 29.2%; FCF 217,915; SBC/FCF 12.1%; product GM 60.0%, service GM 46.7%",
              "% / USD k", "FY2025", "Jan-Dec 2025", "calc/metrics.py -> calc/summary.txt", "2026-11-21", "", "", "High",
              "inputs: 20-F FY2025 statement rows above; product GM = (705,598-282,127)/705,598; service GM = (174,979-93,250)/174,979"))
A1.append(row(nid("A1", A1), "[F]", "Nova reports one operating segment (CODM = CEO)", "1 segment", "", "FY2025", "Jan-Dec 2025",
              "Nova Form 20-F FY2025, Note 16A", "2026-02-17", F20, "The Company operates as one operating segment.", ""))
# product revenue split by end market (calls; third-party transcripts)
splits = {"Q4-2025": "Product revenue distribution was approximately 75% from logic and foundry, and 25% from memory.",
          "Q1-2026": "Revenue mix was approximately 66% from logic and foundry customers and 34% from memory customers",
          "Q2-2026": "Product revenue distribution was approximately 73% from logic and foundry and 27% from memory and others.",
          "Q3-2026": "Product revenue distribution was approximately 61% from logic and foundry and 39% from memory and others."}
vals = {"Q4-2025": "75 / 25", "Q1-2026": "66 / 34", "Q2-2026": "73 / 27", "Q3-2026": "61 / 39"}
for q, qt in splits.items():
    pf, pc = REL[q][2], REL[q][3]
    A1.append(row(nid("A1", A1), "[S]", f"Product revenue split logic&foundry / memory {pf} (CFO on call)", vals[q], "% of product revenue", pf, pc,
                  f"Third-party transcript of Nova {pf} call (stockanalysis.com)", REL[q][1], TR[q], qt, "",
                  "company statement on call; not in release or filing; advanced packaging is not a third bucket on calls (allocated to logic or memory)"))
# advanced packaging share and definition
A1.append(row(nid("A1", A1), "[F]", "Company definition: 'Advanced packaging includes hybrid bonding and HBM processes'; specialty devices (sensors, power, analog) listed separately", "definition", "",
              "FY2024", "Mar 2025", "Nova Investor Day 2025 presentation, slide 7 footnote", "2025-03-13", IDD, "Advanced packaging includes hybrid bonding and HBM processes; Specialty Devices - sensors, power, analog", ""))
A1.append(row(nid("A1", A1), "[F]", "2024 product revenue by segment: logic 62%, memory 23%, advanced packaging 15% (vs semi capex 61/29/10)", "62 / 23 / 15", "% of product revenue", "FY2024", "Jan-Dec 2024",
              "Nova Investor Day 2025 presentation, slide 10 (chart read from rendered slide image)", "2025-03-13", IDD, "Advanced nodes: =<14nm, sources: Gartner, Yole, 2024", "",
              "values are chart labels (15%, 23%, 62%) read from the rendered slide; quote is the slide footnote; slide 71 repeats 2024 split as Logic/Memory/'Pkg & Adv Pkg'"))
apq = [("Q4-2025", "FY2025", "Jan-Dec 2025", "In advanced packaging, revenue rose more than 60% year-over-year, representing approximately 20% of product revenue.", "~20% (FY2025), AP revenue +60% YoY"),
       ("Q1-2026", "FQ1 FY2026", "Jan-Mar 2026", "advanced packaging for Nova is edging towards the mid-$20s of product revenue this quarter with the majority coming from logic", "'mid-20s' % of product revenue"),
       ("Q2-2026", "FQ2 FY2026", "Apr-Jun 2026", "with record sales contributing nearly one-quarter of our overall product revenue, driven by our dimensional metrology portfolio", "'nearly one-quarter' of product revenue")]
for q, pf, pc, qt, v in apq:
    A1.append(row(nid("A1", A1), "[S]", f"Advanced packaging share of product revenue ({pf}) as stated by management", v, "% of product revenue", pf, pc,
                  f"Third-party transcript of Nova call ({REL[q][2]})", REL[q][1], TR[q], qt, "", "company statement on call; transcript wording 'mid-$20s' read as mid-20s percent"))
A1.append(row(nid("A1", A1), "[S]", "HBM is about one-third of Nova's advanced packaging product revenue (FQ1 FY2025 call)", "~1/3", "% of AP product revenue", "FQ1 FY2025", "Jan-Mar 2025",
              "Third-party transcript of Nova Q1 2025 call", "2025-05-08", "2025-05-08_stockanalysis_transcript-Q1-2025-call.html", "I can say that HBM represents about a third of our advanced packaging product revenues", "", "company statement on call"))
A1.append(row(nid("A1", A1), "NOT USED" if False else "[S]", "Advanced packaging share NOT stated for FQ3 FY2026 (record AP revenue only)", "NOT DISCLOSED", "", "FQ3 FY2026", "Jul-Sep 2026",
              "Nova Q3 2026 results release and call transcript", "2026-11-05", REL["Q3-2026"][0], "Record revenue from Advanced Packaging solutions, driven by capacity expansions in HBM and advanced logic", "",
              "NOT DISCLOSED (read: Q3 2026 release p.1; Q3 2026 call transcript) - AP share for the quarter"))
A1[-1]["tag"] = "[F]"

# ---------------- A2 leading signals ----------------
for q in ("Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026"):
    A2.append(rel_row(nid("A2", A2), q, "inventories", f"Inventories (balance sheet, end of {REL[q][2]})", n=1))
    A2.append(rel_row(nid("A2", A2), q, "deferred_revenues", f"Deferred revenues, current (end of {REL[q][2]})", n=1))
    A2.append(rel_row(nid("A2", A2), q, "ar", f"Trade accounts receivable, net (end of {REL[q][2]})", n=1))
A2.append(row(nid("A2", A2), "[I]", "DSO (AR / quarterly revenue x days) and inventory days on cost of revenue, FQ4 FY2025-FQ3 FY2026",
              "DSO 62.8 / 67.7 / 75.1 / 63.3 days; inventory days 179 / 162 / 152 / 152", "days", "FQ4 FY2025-FQ3 FY2026", "Oct 2025-Sep 2026",
              "calc/metrics.py -> calc/quarterly_metrics.csv", "2026-11-21", "", "", "High", "days in quarter 92/90/91/92; inputs are the release rows above"))
A2.append(row(nid("A2", A2), "[F]", "Inventory split at 31 Dec 2025: raw materials 58,350; service inventory 43,195; WIP 41,606; finished goods 40,520 (total 183,671)", "58,350 / 43,195 / 41,606 / 40,520", "USD k", "FY2025", "Dec 2025",
              "Nova Form 20-F FY2025, Note 5", "2026-02-17", F20, "Raw materials 58,350 43,965 Service inventory 43,195 36,232 Work in process 41,606 37,036 Finished goods 40,520 39,366", "",
              "quarterly split NOT DISCLOSED in releases"))
A2.append(row(nid("A2", A2), "[F]", "Inventory split at 31 Dec 2023: raw 50,156; service 31,407; WIP 31,873; finished 24,762", "50,156 / 31,407 / 31,873 / 24,762", "USD k", "FY2023", "Dec 2023",
              "Nova Form 20-F FY2024, Note 4", "2025-02-20", F20_24, "Raw materials 43,965 50,156 Service inventory 36,232 31,407 Work in process 37,036 31,873 Finished goods 39,366 24,762", ""))
A2.append(row(nid("A2", A2), "[F]", "Inventory write-downs 2025 / 2024 / 2023", "8,560 / 7,821 / 8,748", "USD k", "FY2023-FY2025", "Jan 2023-Dec 2025",
              "Nova Form 20-F FY2025, Note 5B", "2026-02-17", F20, "the Company wrote down inventories in a total amount of $8,560, $7,821 and $8,748, respectively", ""))
A2.append(row(nid("A2", A2), "[F]", "Remaining performance obligations at 31 Dec 2025 (deferred revenue + billed-not-recognised; excludes unbilled orders)", "93,087", "USD k", "FY2025", "Dec 2025",
              "Nova Form 20-F FY2025, Note 2 (revenue recognition)", "2026-02-17", F20, "As of December 31, 2025, the aggregate amount of the RPOs was $93,087", "", "not a backlog measure"))
A2.append(row(nid("A2", A2), "[F]", "RPO at 31 Dec 2024", "92,099", "USD k", "FY2024", "Dec 2024", "Nova Form 20-F FY2024", "2025-02-20", F20_24,
              "RPOs was $92,099, comprised of $76,502 deferred revenues and $15,597 of uncollected amounts", ""))
A2.append(row(nid("A2", A2), "[F]", "RPO at 31 Dec 2023", "65,509", "USD k", "FY2023", "Dec 2023", "Nova Form 20-F FY2023", "2024-02-20", F20_23,
              "the aggregate amount of the RPOs was $65,509, comprised of $41,978 deferred revenues and $23,531 of uncollected amounts", ""))
A2.append(row(nid("A2", A2), "[F]", "Non-cancelable inventory purchase obligations at 31 Dec 2025 (for 2026-2028)", "152,965", "USD k", "FY2025", "Dec 2025",
              "Nova Form 20-F FY2025, Note 13", "2026-02-17", F20, "As of December 31, 2025, non-cancelable purchase obligations were approximately $152,965.", ""))
A2.append(row(nid("A2", A2), "[F]", "Non-cancelable purchase obligations at 31 Dec 2024", "127,145", "USD k", "FY2024", "Dec 2024", "Nova Form 20-F FY2024, Note 12", "2025-02-20", F20_24,
              "As of December 31, 2024, non-cancelable purchase obligations were approximately $127,145.", ""))
A2.append(row(nid("A2", A2), "[F]", "Backlog is not a reliable indicator (risk factor); no order, backlog or book-to-bill figures in filings or releases", "NOT DISCLOSED", "", "FY2025", "2025-2026",
              "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "our backlog may not be a reliable indicator of actual sales and financial results", "",
              "NOT DISCLOSED (read: 20-F FY2025; releases FQ4 FY2025-FQ3 FY2026; call transcripts) - orders, backlog, book-to-bill"))
A2.append(row(nid("A2", A2), "[S]", "Memory revenue and bookings at record in FQ3 FY2026 (qualitative only)", "record (no figure)", "", "FQ3 FY2026", "Jul-Sep 2026",
              "Third-party transcript of Nova Q3 2026 call", "2026-11-05", TR["Q3-2026"], "Memory was an important growth engine this quarter, reaching record levels of both revenue and bookings", "", "company statement"))
A2.append(row(nid("A2", A2), "[S]", "Management claims visibility into 2027 (FQ2 FY2026 call)", "qualitative", "", "FQ2 FY2026", "Apr-Jun 2026",
              "Third-party transcript of Nova Q2 2026 call", "2026-08-06", TR["Q2-2026"], "We do have visibility into 2027, where our customers are planning further ahead", "", "company statement"))

# ---------------- A3 guidance record ----------------
g = {r["quarter"]: r for r in csv.DictReader(open(os.path.join(HERE, "guidance_record.csv")))}
for q in ("Q4-2024", "Q1-2025", "Q2-2025", "Q3-2025", "Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026"):
    gq = g[q]; src = gq["guidance_from_release"]
    f, d, pf, pc = REL[src]
    it = items[(src, "guide_rev_low")]
    A3.append(row(nid("A3", A3), "[F]", f"Guidance for {q.replace('-', ' ')} given in {pf} release (revenue, GAAP EPS, non-GAAP EPS)",
                  f"rev ${gq['rev_low']}-{gq['rev_high']}M; GAAP EPS ${gq['eps_gaap_low']}-{gq['eps_gaap_high']}; non-GAAP EPS ${gq['eps_nongaap_low']}-{gq['eps_nongaap_high']}",
                  "USD M / USD", pf, pc, f"Nova results release {pf} (outlook)", d, f, it["line"], "", ""))
    A3.append(row(nid("A3", A3), "[I]", f"Result vs guidance {q.replace('-', ' ')}: revenue / GAAP EPS / non-GAAP EPS",
                  f"rev {gq['rev_actual']}M ({gq['rev_verdict']}, {gq['rev_vs_mid_pct']}% vs mid); GAAP EPS {gq['eps_gaap_actual']} ({gq['eps_gaap_verdict']}); non-GAAP EPS {gq['eps_nongaap_actual']} ({gq['eps_nongaap_verdict']})",
                  "", q.replace("-", " "), "", "calc/metrics.py -> calc/guidance_record.csv", "2026-11-21", "", "", "High",
                  "beat = above top of range; in-line = within range; miss = below bottom; actuals from that quarter's release"))
A3.append(row(nid("A3", A3), "[I]", "Guidance record, last 8 quarters (FQ4 FY2024-FQ3 FY2026): revenue 3 beats / 5 in-line / 0 misses; GAAP EPS 4 / 4 / 0; non-GAAP EPS 6 / 2 / 0", "3/5/0; 4/4/0; 6/2/0", "count", "FQ4 FY2024-FQ3 FY2026", "Oct 2024-Sep 2026",
              "calc/metrics.py -> calc/guidance_record.csv", "2026-11-21", "", "", "High", "five of eight revenue results inside the range (upper half); no intra-quarter guidance updates found, so no 'maintained late then missed' case"))
A3.append(row(nid("A3", A3), "[I]", "Longer record: no revenue or EPS guidance miss found in any quarter FQ2 FY2020-FQ3 FY2026 with adjacent releases saved (21 quarters)", "0 misses", "count", "FQ2 FY2020-FQ3 FY2026", "Apr 2020-Sep 2026",
              "calc/guidance_record.csv", "2026-11-21", "", "", "Medium", "2021 quarters except Q4 not saved (FQ1-FQ3 FY2021 releases not downloaded); Nova gives no annual numeric guidance"))
A3.append(row(nid("A3", A3), "[F]", "Current outlook FQ4 FY2026 (Oct-Dec 2026): revenue $305-315M; GAAP EPS $2.78-2.93; non-GAAP EPS $3.03-3.18", "305-315", "USD M", "FQ4 FY2026", "Oct-Dec 2026",
              "Nova results release FQ3 FY2026", "2026-11-05", REL["Q3-2026"][0], "$305 million to $315 million in revenue", ""))
A3.append(row(nid("A3", A3), "[F]", "Annual target model (2027, non-GAAP): revenue $1B; GM 57%-60%; operating margin 28%-33%; EPS ~$10", "$1B; 57-60%; 28-33%; ~$10", "", "FY2027 target", "Jan-Dec 2027",
              "Nova Investor Day 2025 presentation, slide 80", "2025-03-13", IDD, "Update Financial Target Model", "",
              "values are slide labels; LTM revenue passed $1B in FQ3 FY2026 (calc/summary.txt); new plan due at Investor Day 9 Mar 2027"))

# ---------------- A4 concentration and geography ----------------
A4 += [
    row(nid("A4", A4), "[F]", "Revenue by customer location, % of total: 2025 China 33, Taiwan 29, Korea 16, USA 9, Other 13; 2024 39/20/18/14/9; 2023 36/18/20/13/13", "China 33% (2025), 39% (2024), 36% (2023)", "% of total revenue", "FY2023-FY2025", "Jan 2023-Dec 2025",
        "Nova Form 20-F FY2025, Note 16B", "2026-02-17", F20, "China 33 39 36 Taiwan, R.O.C. 29 20 18 Korea 16 18 20 USA 9 14 13", ""),
    row(nid("A4", A4), "[F]", "Same table in prior filing: 2024 39/20/18/14/9; 2023 36/18/20/13/13; 2022 China 28, Taiwan 32, Korea 13, USA 16, Other 11", "2022 China 28%", "% of total revenue", "FY2022-FY2024", "Jan 2022-Dec 2024",
        "Nova Form 20-F FY2024, Note 15B", "2025-02-20", F20_24, "China 39 36 28 Taiwan, R.O.C. 20 18 32 Korea 18 20 13", "", "no restatement of prior-period geography or customer percentages found across 20-F FY2023, FY2024, FY2025"),
    row(nid("A4", A4), "[F]", "Customers above 10% of total revenue: Customer A 23% (2025), 18% (2024), 19% (2023); Customer B 10%, 14%, 18%", "A 23%; B 10% (2025)", "% of total revenue", "FY2023-FY2025", "Jan 2023-Dec 2025",
        "Nova Form 20-F FY2025, Note 16C", "2026-02-17", F20, "Customer A 23 18 19 Customer B 10 14 18", "", "customers not named; labels may refer to different customers in different years (not stated)"),
    row(nid("A4", A4), "[F]", "Five largest customers: 52% (2023), 53% (2024), 51% (2025) of total revenue; range 6-23% in 2025", "51% (2025)", "% of total revenue", "FY2023-FY2025", "Jan 2023-Dec 2025",
        "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "Total revenues from five largest customers 52% 53% 51%", "", "57% in 2022 and 70% in 2021 per FY2023 20-F"),
    row(nid("A4", A4), "[F]", "Five largest customers 2021 / 2022 / 2023", "70% / 57% / 52%", "% of total revenue", "FY2021-FY2023", "Jan 2021-Dec 2023",
        "Nova Form 20-F FY2023", "2024-02-20", F20_23, "Total revenues from five largest customers 70% 57% 52%", ""),
]
cust = {"Q4-2025": "Product revenue included three customers and four territories, which contributed each 10% or more to product revenues.",
        "Q1-2026": "four customers and five geographic regions, each contributing more than 10% of total product revenue",
        "Q2-2026": "Product revenues included two customers and four territories, which contributed each 10% or more to product revenues.",
        "Q3-2026": "Product revenues included four customers and four territories, which contributed each 10% or more to product revenues."}
cv = {"Q4-2025": "3 customers; 4 territories", "Q1-2026": "4 customers; 5 regions", "Q2-2026": "2 customers; 4 territories", "Q3-2026": "4 customers; 4 territories"}
for q, qt in cust.items():
    A4.append(row(nid("A4", A4), "[S]", f"Customers and territories at or above 10% of product revenue, {REL[q][2]} (CFO on call)", cv[q], "count", REL[q][2], REL[q][3],
                  f"Third-party transcript of Nova {REL[q][2]} call", REL[q][1], TR[q], qt, "", "quarterly revenue by region and China % NOT DISCLOSED (read: releases and calls FQ4 FY2025-FQ3 FY2026)"))
A4 += [
    row(nid("A4", A4), "[S]", "Only quarterly China figure found since 2023: 'approximately a third' of sales in FQ2 FY2023", "~33%", "% of sales", "FQ2 FY2023", "Apr-Jun 2023",
        "Third-party transcript of Nova Q2 2023 call", "2023-08-03", "2023-08-03_stockanalysis_transcript-Q2-2023-call.html", "with China generating approximately a third of our sales", "",
        "all other quarters Q1 2023-Q3 2026: China % NOT DISCLOSED (read: 15 releases and 15 call transcripts)"),
    row(nid("A4", A4), "[S]", "Management (Q4 2025 call, Feb 2026): China expected to 'represent around 30% of our sales'; relative share falls as advanced nodes and DRAM invest more", "~30%", "% of sales", "FY2026 outlook", "Feb 2026",
        "Third-party transcript of Nova Q4 2025 call", "2026-02-12", TR["Q4-2025"], "China is a large and very important territory for us, and we expect it to continue and represent around 30% of our sales.", "", "company statement"),
    row(nid("A4", A4), "[S]", "Management (Q1 2026 call, May 2026): long-term China share to stabilise at 25%-30%", "25-30%", "% of business", "long term", "May 2026",
        "Third-party transcript of Nova Q1 2026 call", "2026-05-14", TR["Q1-2026"], "In the long term, we expect China to stabilize in the range of 25%-30% of our business.", "", "company statement"),
    row(nid("A4", A4), "[S]", "Management (Q3 2026 call, Nov 2026): China rose in revenue and share in Q3 2026 (mature nodes); 2026 China share lower than 2025 but nominally growing", "qualitative", "", "FQ3 FY2026 / FY2026", "Jul-Sep 2026",
        "Third-party transcript of Nova Q3 2026 call", "2026-11-05", TR["Q3-2026"], "But overall, this year, we expect China's shares to be lower than 2025, but still nominally grow.", "", "company statement"),
    row(nid("A4", A4), "[S]", "Management (Q3 2025 call): China revenue 2025 nominally higher, share lower; China 'normalized' in 2H 2025", "qualitative", "", "FY2025", "Nov 2025",
        "Third-party transcript of Nova Q3 2025 call", "2025-11-06", "2025-11-06_stockanalysis_transcript-Q3-2025-call.html", "Of course, the share of the overall business from China should be lower than last year.", "", "company statement"),
    row(nid("A4", A4), "[F]", "Export rules: Chinese customers on the EAR Entity List 'have acquired and continue to acquire' Nova tools; Nova's U.S. subsidiary needs a BIS licence to ship tools, parts or service to them", "licence required (U.S. subsidiary)", "", "FY2025", "as of Feb 2026",
        "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "our U.S. subsidiary is currently restricted from shipping tools or parts, or to provide any form of service to such customers", ""),
    row(nid("A4", A4), "[F]", "Oct 2022 BIS rules limited the U.S. subsidiary's ability to serve 'a small portion' of the Chinese market; later rules Oct 2023, Sep 2024 (GAAFET), Dec 2024 (SME, HBM, 140 entities)", "qualitative", "", "FY2025", "as of Feb 2026",
        "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "have limited the ability of our U.S. subsidiary to serve a small portion of the available Chinese market", ""),
    row(nid("A4", A4), "[F]", "XPS and SIMS product lines are made in Fremont, CA (U.S.); optical CD and Raman in Rehovot/Nes Ziona, Israel; chemical metrology in Bad Urach and packaging optics in Mannheim, Germany", "sites", "", "FY2025", "as of Feb 2026",
        "Nova Form 20-F FY2025, risk factors (manufacturing facilities)", "2026-02-17", F20, "one main manufacturing facility for our XPS and secondary ion mass spectrometry (“SIMS”) technology related product lines, which is", "",
        "so U.S. EAR binds VeraFlex (XPS/XRF) and Metrion (SIMS) directly"),
    row(nid("A4", A4), "[F]", "Nova's products are 'not currently subject to control under Israeli law' (Israeli dual-use regime follows Wassenaar list)", "not controlled (Israel)", "", "FY2025", "as of Feb 2026",
        "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "Our products are not currently subject to control under Israeli law.", ""),
    row(nid("A4", A4), "[F]", "BIS Affiliates Rule (50% ownership extension of Entity List) issued Sep 2025, suspended for one year from 10 Nov 2025", "suspended", "", "FY2025", "Sep-Nov 2025",
        "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "this rule has been suspended for one year, effective November 10, 2025.", ""),
    row(nid("A4", A4), "[F]", "BIS extended the Affiliates Rule suspension through 10 Jan 2027 (final rule 2026-22793, 91 FR 70789, 9 Nov 2026)", "to 10 Jan 2027", "", "n/a", "Nov 2026",
        "Federal Register API record for document 2026-22793", "2026-11-09", "2026-11-09_federal-register_BIS-affiliates-rule-suspension-extension-api.json",
        "This final rule extends the suspension through January 10, 2027.", "", "regulator record (abstract field)"),
    row(nid("A4", A4), "[F]", "China's gallium/germanium export ban suspended until 27 Nov 2026 (per 20-F); supply-chain exposure", "to 27 Nov 2026", "", "FY2025", "as of Feb 2026",
        "Nova Form 20-F FY2025, risk factors", "2026-02-17", F20, "though the export ban is currently suspended until November", "", "status after 27 Nov 2026 not checked"),
]

# ---------------- A5 balance sheet and capital ----------------
q3f = REL["Q3-2026"][0]
A5 += [
    rel_row(nid("A5", A5), "Q3-2026", "cash", "Cash and cash equivalents, 30 Sep 2026", n=1),
    rel_row(nid("A5", A5), "Q3-2026", "st_deposits", "Short-term interest-bearing bank deposits, 30 Sep 2026", n=1),
    rel_row(nid("A5", A5), "Q3-2026", "mkt_sec_current", "Marketable securities (current), 30 Sep 2026", n=1),
    row(nid("A5", A5), "[F]", "Marketable securities (non-current) 711,846 and LT bank deposits incl. restricted 11,448, 30 Sep 2026", "711,846; 11,448", "USD k", "FQ3 FY2026", "Sep 2026",
        "Nova results release FQ3 FY2026 (balance sheet)", "2026-11-05", q3f, "Marketable securities 711,846 584,731 Interest-bearing bank deposits and restricted deposits 11,448 12,508", ""),
    rel_row(nid("A5", A5), "Q3-2026", "conv_notes_current", "Convertible senior notes, net (non-current), 30 Sep 2026", n=1),
    row(nid("A5", A5), "[I]", "Net cash at 30 Sep 2026: cash + deposits + securities 1,800,612 less convertible notes (principal 750,000) = 1,050,612 (or 1,066,053 vs net carrying 734,559)", "1,050,612", "USD k", "FQ3 FY2026", "Sep 2026",
        "calc/metrics.py -> calc/summary.txt", "2026-11-21", "", "", "High", "inputs: five balance-sheet rows above; includes restricted deposits 11,448"),
    row(nid("A5", A5), "[F]", "2030 notes: $750,000k principal, 0% coupon, issued Sep 2025, mature 15 Sep 2030", "750,000", "USD k", "FY2025", "Sep 2025",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "In September 2025, the Company issued $750,000 aggregate principal amount, 0% coupon rate of Convertible Senior Notes due 2030", ""),
    row(nid("A5", A5), "[F]", "2030 notes initial conversion rate 3.1234 shares per $1,000 (conversion price ~$320.16); settlement in cash, shares or both at Nova's election", "$320.16", "USD/share", "FY2025", "Sep 2025",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "initial conversion rate of 3.1234 of the Company's ordinary shares per $1,000 principal amount", ""),
    row(nid("A5", A5), "[F]", "2030 notes: holders may convert before 15 Jun 2030 only on conditions (e.g., share price >=130% of conversion price for 20 of 30 trading days); freely from 15 Jun 2030", "conditions", "", "FY2025", "Sep 2025",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "Prior to June 15, 2030, a holder may convert all or a portion of its Convertible Notes only under the following circumstances", ""),
    row(nid("A5", A5), "[F]", "2030 notes redemption: not before 20 Sep 2028 per one sentence, 'on or after October 20, 2028' per the next (internal inconsistency in the 20-F); pricing release says on or after 20 Sep 2028", "Sep/Oct 2028", "", "FY2025", "Feb 2026",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "The Company may not redeem the notes prior to September 20, 2028", "", "flag: date inconsistency inside Note 11"),
    row(nid("A5", A5), "[F]", "2030 notes net carrying 731,680 at 31 Dec 2025; issuance costs 19,551; effective rate 0.526%; fair value ~936,270 (Level 2)", "731,680; FV 936,270", "USD k", "FY2025", "Dec 2025",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "the total estimated fair value of the 2030 convertible senior notes was approximately $ 936,270", ""),
    row(nid("A5", A5), "[F]", "Capped calls: Nova paid $51,826k (+$1,407k costs); cap price ~$415.03 (75% premium to $237.16 on 2 Sep 2025); equity-classified, not remeasured", "cap $415.03", "USD/share", "FY2025", "Sep 2025",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "The cap price of the capped call transactions is initially approximately $415.03 per share", "", "cap price on p.158; amounts paid ($51,826k and $1,407k costs) at the foot of p.157 (Note 11)"),
    row(nid("A5", A5), "[F]", "Pricing release: conversion premium ~35% over $237.16; capped calls cover shares initially underlying the notes", "35%", "%", "FY2025", "Sep 2025",
        "Nova press release 3 Sep 2025 (pricing of 0.00% notes due 2030)", "2025-09-03", "2026-11-21_nova_pr-convertible-2030-pricing.html",
        "equivalent to an initial conversion price of approximately $320.16 per share, which represents a conversion premium of approximately 35.0%", "", "web page saved 21 Nov 2026; release dated 3 Sep 2025"),
    row(nid("A5", A5), "[F]", "2025 notes ($200M, 0%, issued Oct 2020, due 15 Oct 2025, conversion price ~$74.60): $181,495k converted in 2025 into 2,432,803 shares; none outstanding at 31 Dec 2025", "0 outstanding", "USD k", "FY2025", "Jan-Dec 2025",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "During 2025, a principal amount of $181,495 Convertible Notes was converted into 2,432,803 Company's ordinary shares", ""),
    row(nid("A5", A5), "[F]", "Financial covenants for the notes: none described in the 20-F (notes are senior unsecured; fundamental-change put at 100%)", "NOT DISCLOSED", "", "FY2025", "Feb 2026",
        "Nova Form 20-F FY2025, Note 11", "2026-02-17", F20, "The Convertible Notes are senior unsecured obligations of the Company.", "", "NOT DISCLOSED (read: 20-F FY2025 Note 11) - covenants; indenture itself not retrieved (sec.gov refused)"),
    row(nid("A5", A5), "[F]", "No other debt on the balance sheet at 30 Sep 2026 besides the convertible notes and leases", "none", "", "FQ3 FY2026", "Sep 2026",
        "Nova results release FQ3 FY2026 (balance sheet)", "2026-11-05", q3f, "Convertible senior notes, net 734,559 731,680", ""),
    row(nid("A5", A5), "[F]", "Buyback: $100M programme (Mar 2022): $86.531M spent for 560,001 shares through 31 Dec 2025", "86.531", "USD M", "FY2022-FY2025", "Mar 2022-Dec 2025",
        "Nova Form 20-F FY2025, Note 14B", "2026-02-17", F20, "the Company spent an aggregate of $86.531 million to repurchase 560,001 ordinary shares", ""),
    row(nid("A5", A5), "[F]", "New $200M repurchase programme authorised 2 Sep 2026; CEO: primary priority remains investing and strategic acquisitions", "200", "USD M", "FQ3 FY2026", "Sep 2026",
        "Nova press release 2 Sep 2026", "2026-09-02", "2026-11-21_nova_pr-buyback-200m.html", "authorized a new share repurchase program providing for the repurchase of up to $200 million", ""),
    rel_row(nid("A5", A5), "Q3-2026", "treasury_purchases", "Purchases of treasury shares in FQ3 FY2026", n=1),
    row(nid("A5", A5), "[F]", "M&A: ancosys GmbH acquired 25 Jan 2022: cash 81,708 + contingent consideration fair value 8,480 = 90,188 (earn-out up to 10,115, fully paid in 2022)", "90,188", "USD k", "FY2022", "Jan 2022",
        "Nova Form 20-F FY2022, Note 3", "2023-03-01", "2023-03-01_nova_20-F-FY2022.pdf", "for a cash amount of $81,708", ""),
    row(nid("A5", A5), "[F]", "M&A: Sentronics Metrology GmbH acquired 30 Jan 2025 for cash 60,158; acquisition expenses 859 (2025) and 917 (2024)", "60,158", "USD k", "FY2025", "Jan 2025",
        "Nova Form 20-F FY2025, Note 3", "2026-02-17", F20, "On January 30, 2025, the Company acquired 100% of the outstanding shares of Sentronics Metrology GmbH", ""),
    row(nid("A5", A5), "[F]", "No goodwill impairment and no impairment losses identified in 2023-2025; goodwill 88,425 and intangibles 37,546 at 30 Sep 2026", "0", "USD k", "FY2023-FY2025", "Jan 2023-Dec 2025",
        "Nova Form 20-F FY2025, Note 2", "2026-02-17", F20, "There was no impairment of goodwill during the periods presented.", ""),
]
# M&A intent
ma = [
    ("[F]", "CEO (buyback release, 2 Sep 2026): 'primary capital allocation priority' = invest in the business and pursue strategic acquisitions; preserves capacity for M&A", "2026-09-02", "2026-11-21_nova_pr-buyback-200m.html",
     "Our primary capital allocation priority remains investing in our business and pursuing strategic acquisitions", "FQ3 FY2026", "Sep 2026"),
    ("[F]", "Investor Day 2025 slide: 'The Next Step: $1B Organically With Continued Focus on Acquisitions'; M&A listed as a use of $1.7B (slide 81)", "2025-03-13", IDD,
     "The Next Step: $1B Organically", "FY2025", "Mar 2025"),
    ("[S]", "Named technology areas (Investor Day 2025): 'complementary technologies such as materials, emerging metrology and cross-control solutions, and adjacent high-growth market segments'", "2025-03-13", "2025-03-13_stockanalysis_transcript-investor-day-2025.html",
     "our inorganic product strategy targets complementary technologies such as materials, emerging metrology and cross-control solutions", "FY2025", "Mar 2025"),
    ("[S]", "Target of $150-200M inorganic revenue on top of $1B organic for 2027 (Investor Day 2025)", "2025-03-13", "2025-03-13_stockanalysis_transcript-investor-day-2025.html",
     "We previously published about $150 million-$200 million of inorganic opportunities", "FY2027 target", "Mar 2025"),
    ("[S]", "CEO (Q3 2025 call): looking 'predominantly' at semiconductor process control, open to other segments with a strong semi business; dedicated M&A team", "2025-11-06", "2025-11-06_stockanalysis_transcript-Q3-2025-call.html",
     "We are looking predominantly on the semiconductor area process control", "FY2025", "Nov 2025"),
    ("[S]", "CFO (Cantor, Mar 2026): three M&A criteria - fit financial model (GM, OM), EPS-accretive within 12 months, clear top-line or technology synergies", "2026-03-10", "2026-03-10_stockanalysis_transcript-cantor-conf-2026.html",
     "It needs to be accretive up to 12 months after acquisition on an EPS basis, and we need to identify clear synergies.", "FY2026", "Mar 2026"),
    ("[S]", "CEO (Evercore, Jun 2026): ~$1.7B cash, most designated for M&A; looking at targets 'at scale' versus past deals", "2026-06-03", "2026-06-03_stockanalysis_transcript-evercore-tmt-conf-2026.html",
     "We now have about $1.7 billion in cash, and most of it is dedicated or designated towards having M&A.", "FY2026", "Jun 2026"),
    ("[S]", "CFO (Citi, Sep 2026): inorganic growth is the top capital-allocation priority; balance sheet allows bigger-scale targets", "2026-09-08", "2026-09-08_stockanalysis_transcript-citi-tmt-conf-2026.html",
     "where the key top priority for us is inorganic growth, and it does not change", "FY2026", "Sep 2026"),
]
for tag, claim, d, fname, qt, pf, pc in ma:
    A5.append(row(nid("A5", A5), tag, claim, "", "", pf, pc, "see file", d, fname, qt, "", "company statement" if tag == "[S]" else ""))
A5.append(row(nid("A5", A5), "[I]", "No named acquisition target or specific technology (e.g., X-ray CD) has been stated publicly; stated areas are generic (materials, emerging metrology, process control, adjacent segments)", "", "", "FY2025-FY2026", "Mar 2025-Nov 2026",
              "review of 20-F FY2025, releases, Investor Day 2025 deck and 22 transcripts", "2026-11-21", "", "", "Medium", "absence of evidence in documents read; private discussions unknown"))

# ---------------- A6 cycle ----------------
A6 += [
    row(nid("A6", A6), "[F]", "Annual revenue and operating income 2016-2020 (selected data): 2018 revenue 251,134, OI 60,442; 2019 revenue 224,909, OI 36,408", "2018 251,134; 2019 224,909", "USD k", "FY2018-FY2019", "Jan 2018-Dec 2019",
        "Nova Form 20-F FY2020, Item 3A", "2021-03-01", "2021-03-01_nova_20-F-FY2020.pdf", "Revenues $ 163,903 $ 221,992 $ 251,134 $ 224,909 $ 269,396", ""),
    row(nid("A6", A6), "[F]", "Q2 2019 revenue 51,120 and operating income 6,775 (prior-year column of Q2 2020 release)", "51,120; 6,775", "USD k", "FQ2 FY2019", "Apr-Jun 2019",
        "Nova results release FQ2 FY2020", "2020-08-04", "2020-08-04_nova_results-release-Q2-2020.pdf", items[("Q2-2020", "rev_total")]["line"].split("  ")[0] and q2(items[("Q2-2020", "rev_total")]["line"], 2), ""),
    row(nid("A6", A6), "[I]", "Downturn 2019: revenue -10.4% (FY2018 to FY2019); GAAP operating margin 24.1% to 16.2% (-7.9 pts); quarterly trough Q2 2019 at 13.3% GAAP OM; 2018 quarterly peak NOT RETRIEVED", "-10.4%; -7.9 pts", "% / pts", "FY2018-FY2019", "Jan 2018-Dec 2019",
        "calc/metrics.py -> calc/cycle.csv", "2026-11-21", "", "", "Medium", "annual granularity understates quarterly drawdown; 2019 releases with 2018 quarters only on sec.gov (refused)"),
]
for q in ("Q4-2022", "Q2-2023"):
    f = {"Q4-2022": "2023-02-15_nova_results-release-Q4-2022.pdf", "Q2-2023": "2023-08-03_nova_results-release-Q2-2023.pdf"}[q]
    d = f[:10]; pf = "F" + q[:2] + " FY" + q[-4:]; pc = {"Q4": "Oct-Dec", "Q2": "Apr-Jun"}[q[:2]] + " " + q[-4:]
    A6.append(row(nid("A6", A6), "[F]", f"Revenue {pf}", f"{float(items[(q,'rev_total')]['value']):,.0f}", "USD k", pf, pc, f"Nova results release {pf}", d, f, q2(items[(q, 'rev_total')]['line'], 2), ""))
    A6.append(row(nid("A6", A6), "[F]", f"GAAP operating income {pf}", f"{float(items[(q,'op_income')]['value']):,.0f}", "USD k", pf, pc, f"Nova results release {pf}", d, f, q2(items[(q, 'op_income')]['line'], 2), ""))
A6.append(row(nid("A6", A6), "[F]", "GAAP operating income Q1 2022 (peak quarterly GAAP OM of the 2022-23 cycle) 37,106 on revenue 133,957", "37,106; 133,957", "USD k", "FQ1 FY2022", "Jan-Mar 2022",
              "Nova results release FQ1 FY2022", "2022-05-12", "2022-05-12_nova_results-release-Q1-2022.pdf", q2(items[("Q1-2022", "op_income")]["line"], 2), ""))
A6.append(row(nid("A6", A6), "[I]", "Downturn 2023: revenue peak Q4 2022 151.2M to trough Q2 2023 122.7M (-18.9%); GAAP OM 27.7% (Q1 2022) to 23.4% (Q2 2023), -4.3 pts; non-GAAP OM 34.7% to 27.6%, -7.1 pts; annual FY2022 to FY2023 -9.3%", "-18.9%; -4.3 pts GAAP", "% / pts", "FQ4 FY2022-FQ2 FY2023", "Oct 2022-Jun 2023",
              "calc/metrics.py -> calc/cycle.csv", "2026-11-21", "", "", "High", "inputs: quarterly releases FQ1 FY2022-FQ4 FY2023"))

os.makedirs(PARTS, exist_ok=True)
for name, lst in (("A1", A1), ("A2", A2), ("A3", A3), ("A4", A4), ("A5", A5), ("A6", A6)):
    for i, r in enumerate(lst, 1):
        r["id"] = f"{name}-{i:03d}"   # sequential ids (list literals above evaluate nid() before appending)
    write(os.path.join(PARTS, f"{name}.csv"), lst)
