#!/usr/bin/env python3
"""Parse Nova quarterly results releases (saved PDFs -> pdftotext text) into a long table.

Usage: python3 -I research/out/nova/calc/parse_releases.py
Reads  research/sources/nova/_text/<date>_nova_results-release-QX-YYYY.txt
Writes research/out/nova/calc/quarterly_items.csv  (quarter, item, value_k, page, line, file)

Values are in USD thousands as printed (EPS in USD). The FIRST numeric column of each
statement line is taken (= the three months ended on the quarter date in every release
checked), plus the SECOND column for income-statement/cash-flow lines (= same quarter of
the prior year), stored as item '<name>__prior_year_q'.
Guidance for the NEXT quarter is read from the outlook bullets.
"""
import csv, glob, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", ".."))  # repo root
TXT = os.path.join(ROOT, "research", "sources", "nova", "_text")
OUT = os.path.join(ROOT, "research", "out", "nova", "calc", "quarterly_items.csv")

NUM = re.compile(r"\(?-?\$?[0-9][0-9,]*\.?[0-9]*\)?")


def nums(line):
    s = re.sub(r"(\d),(\d) (\d)", r"\1,\2\3", line)  # repair '36,4 08'
    out = []
    for tok in NUM.findall(s):
        neg = tok.startswith("(") and tok.endswith(")")
        t = tok.strip("()$").replace(",", "")
        if t in ("", "-", "."):
            continue
        try:
            v = float(t)
        except ValueError:
            continue
        out.append(-v if neg else v)
    return out


# (item, regex on the line label, section keyword that must have appeared earlier on the page or before)
IS_ITEMS = [
    ("rev_products", r"^\s*Products\s+[\d(]"),
    ("rev_services", r"^\s*Services\s+[\d(]"),
    ("rev_total", r"^\s*Total revenues\s+[\d(]"),
    ("cost_of_revenues", r"^\s*Total cost of revenues\s+[\d(]|^\s*Cost of revenues\s+[\d(]"),
    ("gross_profit", r"^\s*Gross profit\s+[\d(]"),
    ("rnd", r"^\s*Research and development,? net\s+[\d(]|^\s*Research and development\s+[\d(]"),
    ("sm", r"^\s*Sales and marketing\s+[\d(]"),
    ("ga", r"^\s*General and administrative\s+[\d(]"),
    ("opex_total", r"^\s*Total operating expenses\s+[\d(]"),
    ("op_income", r"^\s*Operating income\s+[\d(]"),
    ("fin_income", r"^\s*Financ\w+ income,? net\s+[\d(]|^\s*Financ\w+ income \(expenses?\),? net\s+[\d(]"),
    ("tax", r"^\s*Income tax expenses?\s+[\d(]|^\s*Income tax (benefit|expense)s?\s+[\d(]|^\s*Taxes on income\s+[\d(]"),
    ("net_income", r"^\s*Net income( for the period)?\s+[\d(]"),
]
CF_ITEMS = [
    ("sbc", r"^\s*Share-based compensation\s+[\d(]|^\s*Stock-based compensation\s+[\d(]"),
    ("depreciation", r"^\s*Depreciation (of property and equipment)?\s*[\d(]"),
    ("amortization_intangibles", r"^\s*Amortization of (acquired )?intangible assets\s+[\d(]"),
    ("cfo", r"^\s*Net cash provided by (\(used in\) )?operating activities\s+[\d(]"),
    ("capex", r"^\s*Purchase of property,? (plant )?and equipment\s+[\d(]"),
    ("cf_ar_change", r"^\s*Trade accounts receivables?,? net\s+[\d(]"),
    ("cf_inventory_change", r"^\s*Inventories\s+[\d(]"),
    ("cf_deferred_rev_change", r"^\s*Deferred revenues\s+[\d(]"),
    ("treasury_purchases", r"^\s*Purchases? of treasury shares\s+[\d(]"),
]
BS_ITEMS = [
    ("cash", r"^\s*Cash and cash equivalents\s+[\d(]"),
    ("st_deposits", r"^\s*Short-term interest-bearing bank deposits\s+[\d(]"),
    ("ar", r"^\s*Trade accounts receivables?,? net\s+[\d(]"),
    ("inventories", r"^\s*Inventories\s+[\d(]"),
    ("deferred_revenues", r"^\s*Deferred revenues\s+[\d(]"),
    ("conv_notes_current", r"^\s*Convertible senior notes,? net\s+[\d(]"),
    ("lt_deposits", r"^\s*(Long-term )?[Ii]nterest-bearing bank deposits( and restricted deposits)?\s+[\d(]"),
    ("equity", r"^\s*(Total )?[Ss]hareholders.? equity\s+[\d(]"),
    ("total_assets", r"^\s*Total assets\s+[\d(]"),
    ("trade_payables", r"^\s*Trade accounts payable\s+[\d(]"),
]
NG_ITEMS = [
    ("ng_gross_profit", r"^\s*Non-GAAP gross profit\s+[\d(]"),
    ("ng_op_income", r"^\s*Non-GAAP operating income\s+[\d(]"),
    ("ng_net_income", r"^\s*Non-GAAP net income\s+[\d(]"),
    ("ng_eps_diluted", r"^\s*Non-GAAP diluted earnings per share\s+[\d(]"),
    ("gaap_eps_diluted_recon", r"^\s*GAAP diluted earnings per share\s+[\d(]"),
]


def parse(path):
    quarter = re.search(r"results-release-(Q\d-\d{4})", path).group(1)
    pages = open(path, encoding="utf-8", errors="replace").read().split("\f")
    rows = []
    found = set()
    section = None
    ms_seen = 0
    ng_tables = 0
    for pno, pg in enumerate(pages, 1):
        for line in pg.splitlines():
            u = line.upper()
            if "BALANCE SHEETS" in u:
                section = "BS"; ms_seen = 0
            elif "STATEMENTS OF OPERATIONS" in u or "STATEMENTS OF INCOME" in u:
                section = "IS"
            elif "STATEMENTS OF CASH FLOWS" in u:
                section = "CF"
            elif "RECONCILIATION OF GAAP TO NON-GAAP" in u and "GUIDANCE" not in u:
                if section in ("NG", "NGFY") or ng_tables:
                    section = "NGFY"
                else:
                    section = "NG"
                ng_tables += 1
            elif "GUIDANCE" in u and "RECONCILIATION" in u:
                section = "GUIDE"
            items = {"IS": IS_ITEMS, "CF": CF_ITEMS, "BS": BS_ITEMS, "NG": NG_ITEMS, "NGFY": NG_ITEMS}.get(section, [])
            for name, rx in items:
                key = (section, name)
                if re.search(rx, line):
                    v = nums(line)
                    if not v:
                        continue
                    if section == "BS" and name == "conv_notes_current" and key in found:
                        name = "conv_notes_noncurrent"; key = (section, name)
                    if section == "BS" and "Marketable securities" in line:
                        pass
                    if section == "NGFY":
                        name = name + "__fy"; key = (section, name)
                    if key in found:
                        continue
                    found.add(key)
                    rows.append((quarter, name, v[0], pno, line.strip()[:160]))
                    if section in ("IS", "CF") and len(v) > 1:
                        rows.append((quarter, name + "__prior_year_q", v[1], pno, line.strip()[:160]))
                    # Q4 releases: third column = full fiscal year (Jan-Dec), fourth = prior fiscal year
                    if quarter.startswith("Q4") and section in ("IS", "CF") and len(v) > 3:
                        rows.append((quarter, name + "__fy", v[2], pno, line.strip()[:160]))
                        rows.append((quarter, name + "__prior_fy", v[3], pno, line.strip()[:160]))
            if section == "BS" and re.search(r"^\s*Marketable securities\s+[\d(]", line):
                ms_seen += 1
                v = nums(line)
                if v:
                    rows.append((quarter, "mkt_sec_current" if ms_seen == 1 else "mkt_sec_noncurrent", v[0], pno, line.strip()[:160]))
    # headline diluted EPS (GAAP and non-GAAP), from the summary tables on page 1
    first = pages[0]
    m = re.findall(r"Earnings per Diluted Share\s+\$?([\d.]+)", first)
    if len(m) >= 2:
        rows.append((quarter, "eps_diluted_gaap", float(m[0]), 1, "headline table"))
        rows.append((quarter, "eps_diluted_nongaap", float(m[1]), 1, "headline table"))
    # outlook for next quarter
    full = "\f".join(pages)
    for name, rx in [("guide_rev", r"\$([\d.]+)\s*million to \$([\d.]+)\s*million in revenue"),
                     ("guide_eps_gaap", r"\$([\d.]+)\s*to \$([\d.]+)\s*in diluted GAAP EPS"),
                     ("guide_eps_nongaap", r"\$([\d.]+)\s*to \$([\d.]+)\s*in diluted non-GAAP EPS")]:
        mm = re.search(rx, full)
        if mm:
            pno = full[:mm.start()].count("\f") + 1
            rows.append((quarter, name + "_low", float(mm.group(1)), pno, mm.group(0)))
            rows.append((quarter, name + "_high", float(mm.group(2)), pno, mm.group(0)))
    return rows


def main():
    files = sorted(glob.glob(os.path.join(TXT, "*_nova_results-release-Q*-*.txt")))
    allrows = []
    for f in files:
        for r in parse(f):
            allrows.append(r + (os.path.relpath(f.replace("/_text/", "/").replace(".txt", ".pdf"), ROOT),))
    with open(OUT, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["quarter", "item", "value", "page", "line", "file"])
        w.writerows(allrows)
    print(f"{len(files)} releases, {len(allrows)} rows -> {OUT}")


if __name__ == "__main__":
    main()
