#!/usr/bin/env python3
"""Module A arithmetic for Nova Ltd. (FY = calendar year; FQ3 FY2026 = Jul-Sep 2026).

Usage: python3 -I research/out/nova/calc/metrics.py
Input : research/out/nova/calc/quarterly_items.csv (from parse_releases.py; USD thousands, EPS in USD)
Output: research/out/nova/calc/quarterly_metrics.csv, guidance_record.csv, cycle.csv, summary.txt

All inputs are figures printed in Nova's quarterly results releases (saved under
research/sources/nova/). One-off items are ONLY those management itself lists in the
GAAP-to-non-GAAP reconciliations as acquisition-related (inventory step-up, acquisition
expenses) or discrete (tax reserve release); recurring adjustments (stock-based
compensation, amortization of acquired intangibles, lease/intercompany revaluation,
debt-issuance-cost amortization) stay in the "company-adjusted" (non-GAAP) figure only.
"""
import csv, os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
rows = list(csv.DictReader(open(os.path.join(HERE, "quarterly_items.csv"))))
D = defaultdict(dict)
for r in rows:
    D[r["quarter"]][r["item"]] = float(r["value"])

ORDER = ["Q1-2020", "Q2-2020", "Q3-2020", "Q4-2020", "Q4-2021", "Q1-2022", "Q2-2022", "Q3-2022", "Q4-2022",
         "Q1-2023", "Q2-2023", "Q3-2023", "Q4-2023", "Q1-2024", "Q2-2024", "Q3-2024", "Q4-2024",
         "Q1-2025", "Q2-2025", "Q3-2025", "Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026"]
CAL = {"Q1": "Jan-Mar", "Q2": "Apr-Jun", "Q3": "Jul-Sep", "Q4": "Oct-Dec"}
DAYS = {"Q1": 90, "Q2": 91, "Q3": 92, "Q4": 92}

# One-off items named by management in the reconciliations (USD thousands, added back to GAAP)
ONE_OFF_GP = {"Q1-2025": 1348, "Q2-2025": 910}                      # acquisition-related inventory step-up (Sentronics)
ONE_OFF_OI = {"Q4-2024": 917,                                       # acquisition-related expenses
              "Q1-2025": 1348 + 859,                                # step-up + acquisition expenses
              "Q2-2025": 910,                                       # step-up
              "Q4-2025": 203}                                       # discrete tax reserve release, net (in OI)
ONE_OFF_FY2025 = {"gp": 2258, "oi": 2258 + 859 + 203}


def pct(a, b):
    return None if (a is None or not b) else 100.0 * a / b


def fmt(x, nd=1):
    return "" if x is None else f"{x:.{nd}f}"


out = []
for q in ORDER:
    d = D.get(q, {})
    if not d:
        continue
    qq = q[:2]
    rev = d.get("rev_total")
    gp, oi = d.get("gross_profit"), d.get("op_income")
    ng_gp, ng_oi = d.get("ng_gross_profit"), d.get("ng_op_income")
    cfo, capex, sbc = d.get("cfo"), d.get("capex"), d.get("sbc")
    fcf = (cfo + capex) if (cfo is not None and capex is not None) else None
    cash_inv = sum(d.get(k, 0.0) for k in ("cash", "st_deposits", "mkt_sec_current", "mkt_sec_noncurrent", "lt_deposits"))
    conv = d.get("conv_notes_current", 0.0) + d.get("conv_notes_noncurrent", 0.0)
    out.append({
        "quarter": q,
        "fiscal": f"F{qq} FY{q[-4:]}",
        "calendar": f"{CAL[qq]} {q[-4:]}",
        "revenue_k": rev, "products_k": d.get("rev_products"), "services_k": d.get("rev_services"),
        "services_share_pct": fmt(pct(d.get("rev_services"), rev)),
        "yoy_pct": fmt(pct(rev - d["rev_total__prior_year_q"], d["rev_total__prior_year_q"]) if rev and d.get("rev_total__prior_year_q") else None),
        "gm_gaap_pct": fmt(pct(gp, rev)), "gm_nongaap_pct": fmt(pct(ng_gp, rev)),
        "gm_ex_oneoffs_pct": fmt(pct(gp + ONE_OFF_GP.get(q, 0), rev)) if gp is not None else "",
        "om_gaap_pct": fmt(pct(oi, rev)), "om_nongaap_pct": fmt(pct(ng_oi, rev)),
        "om_ex_oneoffs_pct": fmt(pct(oi + ONE_OFF_OI.get(q, 0), rev)) if oi is not None else "",
        "oneoffs_named_k": ONE_OFF_OI.get(q, 0),
        "cfo_k": cfo, "capex_k": capex, "fcf_k": fcf, "sbc_k": sbc,
        "sbc_to_fcf_pct": fmt(pct(sbc, fcf)) if fcf and fcf > 0 else "",
        "ar_k": d.get("ar"), "dso_days": fmt(d["ar"] / rev * DAYS[qq]) if d.get("ar") and rev else "",
        "inventories_k": d.get("inventories"),
        "inventory_days_on_cogs": fmt(d["inventories"] / d["cost_of_revenues"] * DAYS[qq]) if d.get("inventories") and d.get("cost_of_revenues") else "",
        "deferred_revenues_k": d.get("deferred_revenues"),
        "cash_and_investments_k": cash_inv if cash_inv else "",
        "convertible_notes_net_k": conv if conv else "",
        "net_cash_k": (cash_inv - conv) if cash_inv else "",
        "eps_gaap": d.get("gaap_eps_diluted_recon", d.get("eps_diluted_gaap")),
        "eps_nongaap": d.get("ng_eps_diluted", d.get("eps_diluted_nongaap")),
    })

with open(os.path.join(HERE, "quarterly_metrics.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(out[0].keys()))
    w.writeheader(); w.writerows(out)

# ---------- guidance record: guidance given in quarter N-1 release for quarter N ----------
prev = {ORDER[i]: ORDER[i - 1] for i in range(1, len(ORDER))}
prev["Q1-2021"] = "Q4-2020"
g_rows = []
for q in ORDER:
    p = prev.get(q)
    if not p or p not in D or q not in D:
        continue
    gp_ = D[p]
    if "guide_rev_low" not in gp_:
        continue
    # sanity: guidance must be for the adjacent quarter (skip gaps such as Q4-2020 -> Q4-2021)
    qi, pi = ORDER.index(q), ORDER.index(p)
    yq, yp = int(q[-4:]) * 4 + int(q[1]), int(p[-4:]) * 4 + int(p[1])
    if yq - yp != 1:
        continue
    a = D[q]
    rec = {"quarter": q, "guidance_from_release": p}
    for key, act, scale in [("rev", a.get("rev_total"), 1000.0),
                            ("eps_gaap", a.get("gaap_eps_diluted_recon", a.get("eps_diluted_gaap")), 1.0),
                            ("eps_nongaap", a.get("ng_eps_diluted", a.get("eps_diluted_nongaap")), 1.0)]:
        lo, hi = gp_.get(f"guide_{key}_low"), gp_.get(f"guide_{key}_high")
        actual = act / scale if (act is not None and key == "rev") else act
        mid = (lo + hi) / 2 if lo is not None else None
        verdict = "" if actual is None else ("beat" if actual > hi else ("miss" if actual < lo else "in-line"))
        rec.update({f"{key}_low": lo, f"{key}_high": hi, f"{key}_actual": round(actual, 3) if actual is not None else "",
                    f"{key}_vs_mid_pct": fmt(pct(actual - mid, mid)) if actual is not None and mid else "",
                    f"{key}_verdict": verdict})
    g_rows.append(rec)
with open(os.path.join(HERE, "guidance_record.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(g_rows[0].keys()))
    w.writeheader(); w.writerows(g_rows)

# ---------- cycle: last two downturns ----------
cyc = []
# 2018-2019, annual (FY2020 20-F selected data, USD thousands): 2018 rev 251,134 OI 60,442; 2019 rev 224,909 OI 36,408
a18, o18, a19, o19 = 251134.0, 60442.0, 224909.0, 36408.0
cyc.append({"downturn": "2019 (annual)", "peak": "FY2018 (Jan-Dec 2018)", "trough": "FY2019 (Jan-Dec 2019)",
            "revenue_change_pct": fmt(pct(a19 - a18, a18)), "gaap_om_peak_pct": fmt(pct(o18, a18)),
            "gaap_om_trough_pct": fmt(pct(o19, a19)), "om_change_pts": fmt(pct(o19, a19) - pct(o18, a18))})
# 2019 quarters from 2020 releases' prior-year columns
q19 = {q.replace("2020", "2019"): (D[q]["rev_total__prior_year_q"], D[q]["op_income__prior_year_q"]) for q in ("Q1-2020", "Q2-2020", "Q3-2020", "Q4-2020")}
tr = min(q19, key=lambda k: q19[k][0])
cyc.append({"downturn": "2019 (quarterly trough only; 2018 quarters NOT RETRIEVED)", "peak": "NOT RETRIEVED",
            "trough": f"{tr} rev {q19[tr][0]:.0f}k", "revenue_change_pct": "", "gaap_om_peak_pct": "",
            "gaap_om_trough_pct": fmt(pct(q19[tr][1], q19[tr][0])), "om_change_pts": ""})
# 2022-2023 quarterly
win = ["Q1-2022", "Q2-2022", "Q3-2022", "Q4-2022", "Q1-2023", "Q2-2023", "Q3-2023", "Q4-2023"]
revs = {q: D[q]["rev_total"] for q in win}
pk = max(revs, key=revs.get)
after = win[win.index(pk):]
tg = min(after, key=lambda k: revs[k])
om = {q: pct(D[q]["op_income"], D[q]["rev_total"]) for q in win}
ngom = {q: pct(D[q]["ng_op_income"], D[q]["rev_total"]) for q in win}
pk_om = max(om, key=om.get); tr_om = min(om, key=om.get)
pk_ng = max(ngom, key=ngom.get); tr_ng = min(ngom, key=ngom.get)
cyc.append({"downturn": "2023 (quarterly)", "peak": f"{pk} rev {revs[pk]:.0f}k", "trough": f"{tg} rev {revs[tg]:.0f}k",
            "revenue_change_pct": fmt(pct(revs[tg] - revs[pk], revs[pk])),
            "gaap_om_peak_pct": f"{fmt(om[pk_om])} ({pk_om})", "gaap_om_trough_pct": f"{fmt(om[tr_om])} ({tr_om})",
            "om_change_pts": fmt(om[tr_om] - om[pk_om])})
cyc.append({"downturn": "2023 (quarterly, non-GAAP OM)", "peak": "", "trough": "", "revenue_change_pct": "",
            "gaap_om_peak_pct": f"non-GAAP {fmt(ngom[pk_ng])} ({pk_ng})", "gaap_om_trough_pct": f"non-GAAP {fmt(ngom[tr_ng])} ({tr_ng})",
            "om_change_pts": fmt(ngom[tr_ng] - ngom[pk_ng])})
# annual 2022 -> 2023 from Q4 releases' FY columns
fy22, fy23 = D["Q4-2022"], D["Q4-2023"]
cyc.append({"downturn": "2023 (annual)", "peak": "FY2022", "trough": "FY2023",
            "revenue_change_pct": fmt(pct(fy23["rev_total__fy"] - fy22["rev_total__fy"], fy22["rev_total__fy"])),
            "gaap_om_peak_pct": fmt(pct(fy22["op_income__fy"], fy22["rev_total__fy"])),
            "gaap_om_trough_pct": fmt(pct(fy23["op_income__fy"], fy23["rev_total__fy"])),
            "om_change_pts": fmt(pct(fy23["op_income__fy"], fy23["rev_total__fy"]) - pct(fy22["op_income__fy"], fy22["rev_total__fy"]))})
with open(os.path.join(HERE, "cycle.csv"), "w", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=list(cyc[0].keys()))
    w.writeheader(); w.writerows(cyc)

# ---------- LTM and fiscal-year summary ----------
L = ["Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026"]
P = ["Q4-2024", "Q1-2025", "Q2-2025", "Q3-2025"]
s = lambda qs, k: sum(D[q][k] for q in qs)
ltm_rev, prv_rev = s(L, "rev_total"), s(P, "rev_total")
ltm_fcf = s(L, "cfo") + s(L, "capex"); ltm_sbc = s(L, "sbc")
ltm_gp, ltm_nggp = s(L, "gross_profit"), s(L, "ng_gross_profit")
ltm_svc = s(L, "rev_services")
lines = []
lines.append(f"LTM = FQ4 FY2025..FQ3 FY2026 (Oct 2025-Sep 2026). Prior LTM = Oct 2024-Sep 2025.")
lines.append(f"LTM revenue {ltm_rev:,.0f}k; prior LTM {prv_rev:,.0f}k; YoY {pct(ltm_rev - prv_rev, prv_rev):.1f}%")
lines.append(f"LTM gross margin GAAP {pct(ltm_gp, ltm_rev):.1f}%, non-GAAP {pct(ltm_nggp, ltm_rev):.1f}%, ex one-offs {pct(ltm_gp + sum(ONE_OFF_GP.get(q,0) for q in L), ltm_rev):.1f}%")
lines.append(f"LTM operating margin GAAP {pct(s(L,'op_income'), ltm_rev):.1f}%, non-GAAP {pct(s(L,'ng_op_income'), ltm_rev):.1f}%")
lines.append(f"LTM CFO {s(L,'cfo'):,.0f}k; capex {s(L,'capex'):,.0f}k; FCF {ltm_fcf:,.0f}k; SBC {ltm_sbc:,.0f}k; SBC/FCF {pct(ltm_sbc, ltm_fcf):.1f}%")
lines.append(f"LTM services revenue {ltm_svc:,.0f}k = {pct(ltm_svc, ltm_rev):.1f}% of revenue (company label: 'Services')")
q3 = D["Q3-2026"]
ci = q3["cash"] + q3["st_deposits"] + q3["mkt_sec_current"] + q3["mkt_sec_noncurrent"] + q3["lt_deposits"]
lines.append(f"30 Sep 2026: cash+deposits+securities {ci:,.0f}k (incl. LT deposits & restricted {q3['lt_deposits']:,.0f}k); convertible notes net {q3['conv_notes_current']:,.0f}k (principal 750,000k); net cash vs net carrying {ci - q3['conv_notes_current']:,.0f}k; vs principal {ci - 750000:,.0f}k")
for y in ("2023", "2024", "2025"):
    f = D[f"Q4-{y}"]
    r = f["rev_total__fy"]
    one_gp = ONE_OFF_FY2025["gp"] if y == "2025" else 0
    one_oi = ONE_OFF_FY2025["oi"] if y == "2025" else (917 if y == "2024" else 0)
    lines.append(f"FY{y} (Jan-Dec {y}): revenue {r:,.0f}k; products {f['rev_products__fy']:,.0f}k; services {f['rev_services__fy']:,.0f}k ({pct(f['rev_services__fy'], r):.1f}%); "
                 f"GM GAAP {pct(f['gross_profit__fy'], r):.1f}% / non-GAAP {pct(f.get('ng_gross_profit__fy'), r) or 0:.1f}% / ex one-offs {pct(f['gross_profit__fy'] + one_gp, r):.1f}%; "
                 f"OM GAAP {pct(f['op_income__fy'], r):.1f}% / non-GAAP {pct(f.get('ng_op_income__fy'), r) or 0:.1f}% / ex one-offs {pct(f['op_income__fy'] + one_oi, r):.1f}%; "
                 f"CFO {f['cfo__fy']:,.0f}k; capex {f['capex__fy']:,.0f}k; FCF {f['cfo__fy'] + f['capex__fy']:,.0f}k; SBC {f['sbc__fy']:,.0f}k; SBC/FCF {pct(f['sbc__fy'], f['cfo__fy'] + f['capex__fy']):.1f}%")
for y0, y1 in (("2023", "2024"), ("2024", "2025")):
    a, b = D[f"Q4-{y0}"]["rev_total__fy"], D[f"Q4-{y1}"]["rev_total__fy"]
    lines.append(f"FY{y1} revenue growth {pct(b - a, a):.1f}%; products {pct(D[f'Q4-{y1}']['rev_products__fy'] - D[f'Q4-{y0}']['rev_products__fy'], D[f'Q4-{y0}']['rev_products__fy']):.1f}%; services {pct(D[f'Q4-{y1}']['rev_services__fy'] - D[f'Q4-{y0}']['rev_services__fy'], D[f'Q4-{y0}']['rev_services__fy']):.1f}%")
# 9M 2026 vs 9M 2025 services and products
for k in ("rev_products", "rev_services"):
    a = sum(D[q][k] for q in ("Q1-2025", "Q2-2025", "Q3-2025")); b = sum(D[q][k] for q in ("Q1-2026", "Q2-2026", "Q3-2026"))
    lines.append(f"9M 2026 vs 9M 2025 {k}: {b:,.0f}k vs {a:,.0f}k = {pct(b - a, a):+.1f}%")
# guidance tally for last 8 quarters
last8 = [r for r in g_rows if r["quarter"] in ("Q4-2024", "Q1-2025", "Q2-2025", "Q3-2025", "Q4-2025", "Q1-2026", "Q2-2026", "Q3-2026")]
for key in ("rev", "eps_gaap", "eps_nongaap"):
    t = defaultdict(int)
    for r in last8:
        t[r[f"{key}_verdict"]] += 1
    lines.append(f"Guidance record last 8 quarters ({key}): " + ", ".join(f"{k} {v}" for k, v in sorted(t.items())))
open(os.path.join(HERE, "summary.txt"), "w").write("\n".join(lines) + "\n")
print("\n".join(lines))
