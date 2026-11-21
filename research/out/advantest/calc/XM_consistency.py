#!/usr/bin/env python3
"""XM: cross-module consistency scan of the Advantest evidence parts.

Run: python3 -I research/out/advantest/calc/XM_consistency.py > research/out/advantest/calc/XM_consistency.out.txt
Reads research/out/advantest/parts/<MOD>.csv for MOD in A1 A2 A3 A4 A5 A6 TH CL.

(a) SAME-SOURCE CONFLICTS. [F]/[C] rows from DIFFERENT modules that cite the same local_file and
    the same first page and appear to be the same quantity, but disagree on value, unit or period.
    "Same quantity" is decided two ways:
      a1  same normalised quote and same period_fiscal  -> value or unit differs
      a2  same normalised quote and same numeric value   -> period_fiscal or period_calendar differs
      a3  different quotes, same period_fiscal and the same set of metric keywords in the claim
          -> numeric values (after JPY million/billion scaling) do not overlap within rounding
(b) TAG CONFLICTS. Every pair of rows (any module, including the same module) that cites the same
    local_file and the same normalised quote but carries different tags. (b2) also lists pairs whose
    quotes nearly match (one normalised quote of 30+ characters contains the other).
(c) KEY-FIGURE TABLE. For the cross-module checks in the reconcile task, every row that mentions
    each key quantity, printed side by side by module (for review by hand, no verdict).
"""
import csv, itertools, os, re
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
PARTS = os.path.join(os.path.dirname(HERE), "parts")
MODS = ["A1", "A2", "A3", "A4", "A5", "A6", "TH", "CL"]


def load():
    rows = []
    for m in MODS:
        p = os.path.join(PARTS, f"{m}.csv")
        for r in csv.DictReader(open(p, encoding="utf-8")):
            r = {k: (v or "").strip() for k, v in r.items()}
            r["_mod"] = m
            rows.append(r)
    return rows


def normq(q):
    q = q.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    q = q.replace("–", "-").replace("—", "-").replace("¥", "(y)").replace("￥", "(y)")
    q = re.sub(r"\s+", " ", q).strip().lower()
    return q.strip(" .,;:'\"")


def page1(ps):
    m = re.search(r"(?:^|\b)(?:pp?\.|page)\s*(\d+)", ps or "")
    return m.group(1) if m else (ps or "").split(";")[0].strip()


def numbers(v):
    out = []
    for t in re.findall(r"-?\(?\d[\d,]*\.?\d*\)?", v or ""):
        neg = t.startswith("(") or t.startswith("-")
        t = t.replace(",", "").replace("(", "").replace(")", "").lstrip("-").rstrip(".")
        if not t:
            continue
        try:
            x = float(t)
        except ValueError:
            continue
        out.append(-x if neg else x)
    return out


def scaled(r):
    """numbers in value, scaled to JPY billion when the unit is JPY million."""
    u = r["unit"].lower()
    xs = numbers(r["value"])
    if u.startswith("jpy million"):
        return [x / 1000 for x in xs], "JPY bn"
    if u.startswith("jpy billion"):
        return xs, "JPY bn"
    if u.startswith("usd million"):
        return [x / 1000 for x in xs], "USD bn"
    if u.startswith("usd billion"):
        return xs, "USD bn"
    return xs, u


def overlap(a, b):
    for x in a:
        for y in b:
            tol = max(0.051, abs(x) * 0.0006)
            if abs(abs(x) - abs(y)) <= tol:
                return True
    return False


METRICS = [
    ("sales", r"\bnet sales\b|\bsales\b|revenue"),
    ("gross", r"gross (margin|profit)"),
    ("opinc", r"operating (income|profit|margin)|\bOPM\b"),
    ("netinc", r"net income|profit attributable"),
    ("soc", r"\bSoC\b"),
    ("memory", r"\bmemory\b"),
    ("inventory", r"inventor"),
    ("china", r"\bChina\b|\bChinese\b"),
    ("nvidia", r"NVIDIA"),
    ("tsmc", r"TSMC|Taiwan Semiconductor"),
    ("samsung", r"Samsung"),
    ("buyback", r"repurchase|buyback|treasury"),
    ("dividend", r"dividend"),
    ("cash", r"\bcash\b"),
    ("cb", r"convertible|\bCB\b"),
    ("sga", r"SG&A|selling, general"),
    ("eps", r"\bEPS\b|per share"),
    ("tam", r"\bTAM\b|market size|tester market"),
    ("share", r"\bshare\b"),
    ("yoy", r"YoY|year on year|year-on-year"),
    ("ltm", r"\bLTM\b|last twelve|trailing"),
    ("forecast", r"forecast|guidance|outlook|target"),
    # discriminating keys: segment lines, regions, cash-flow and balance lines, cost lines
    ("seg_test", r"Test System Business"),
    ("seg_serv", r"Services and Others|Services, Support"),
    ("seg_elim", r"Elimination|Corporate"),
    ("seg_total", r"\btotal\b|consolidated"),
    ("other_sys", r"Other (test )?systems?"),
    ("region", r"\b(Japan|Korea|Taiwan|Americas|Europe|Others|region)\b"),
    ("cost", r"cost of sales|\bcost\b"),
    ("cf_op", r"operating activities|operating cash"),
    ("cf_inv", r"investing activities"),
    ("adv", r"advance receipts|contract liab|opening contract"),
    ("ibt", r"before (income )?tax"),
    ("fin", r"financial income|valuation gain"),
]


def mkeys(claim):
    return frozenset(k for k, p in METRICS if re.search(p, claim, re.I))


def fmt(r):
    return (f"  {r['id']:<7} {r['tag']} | {r['value'][:38]:<38} | {r['unit'][:18]:<18} | "
            f"{r['period_fiscal'][:24]:<24} | {r['period_calendar'][:44]:<44} | {r['claim'][:90]}")


def main():
    rows = load()
    print(f"rows loaded: {len(rows)} from {', '.join(MODS)}")
    fc = [r for r in rows if r["tag"] in ("[F]", "[C]") and r["local_file"]]

    # ---------- (a) same-source conflicts ----------
    print("\n=== (a) SAME local_file + first page, different modules, same quantity, disagreement ===")
    groups = defaultdict(list)
    for r in fc:
        groups[(r["local_file"], page1(r["page_or_section"]))].append(r)
    found = defaultdict(list)
    for key, g in sorted(groups.items()):
        for x, y in itertools.combinations(g, 2):
            if x["_mod"] == y["_mod"]:
                continue
            same_q = x["quote"] and normq(x["quote"]) == normq(y["quote"])
            vx, ux = scaled(x)
            vy, uy = scaled(y)
            kx, ky = mkeys(x["claim"]), mkeys(y["claim"])
            if same_q and x["period_fiscal"] == y["period_fiscal"] and kx == ky:
                if (vx and vy and not overlap(vx, vy)) or (vx and vy and ux != uy and ux and uy):
                    found["a1 same quote+period, value/unit differ"].append((key, x, y))
                elif x["period_calendar"] != y["period_calendar"]:
                    found["a1b same quote+period_fiscal, period_calendar differs"].append((key, x, y))
            elif (same_q and vx and vy and sorted(vx) == sorted(vy) and ux == uy
                  and (x["period_fiscal"], x["period_calendar"]) != (y["period_fiscal"], y["period_calendar"])):
                found["a2 same quote+value, period differs"].append((key, x, y))
            elif (not same_q) and x["period_fiscal"] == y["period_fiscal"] and x["period_fiscal"]:
                if kx and kx == ky and vx and vy and ux == uy and not overlap(vx, vy):
                    found["a3 same claim keywords+period, values do not overlap"].append((key, x, y))
    total = 0
    for kind in sorted(found):
        items = found[kind]
        total += len(items)
        print(f"\n-- {kind}: {len(items)} pair(s)")
        for (lf, pg), x, y in items:
            print(f"[{os.path.basename(lf)} p.{pg}] {x['id']} vs {y['id']}")
            print(fmt(x)); print(fmt(y))
    print(f"\n(a) total flagged pairs: {total}")

    # ---------- (b) tag conflicts ----------
    print("\n=== (b) SAME local_file + quote, DIFFERENT tags (all modules) ===")
    qg = defaultdict(list)
    for r in rows:
        if r["local_file"] and r["quote"]:
            qg[(r["local_file"], normq(r["quote"]))].append(r)
    nb = 0
    for (lf, q), g in sorted(qg.items()):
        for x, y in itertools.combinations(g, 2):
            if x["tag"] != y["tag"]:
                nb += 1
                print(f"[{os.path.basename(lf)}] {x['id']} {x['tag']} vs {y['id']} {y['tag']} | quote: {q[:110]}")
                print(fmt(x)); print(fmt(y))
    print(f"\n(b) total pairs with different tags: {nb}")
    print("\n=== (b2) SAME local_file, one quote contains the other (30+ chars), DIFFERENT tags ===")
    nb2 = 0
    byfile = defaultdict(list)
    for r in rows:
        if r["local_file"] and len(normq(r["quote"])) >= 30:
            byfile[r["local_file"]].append(r)
    for lf, g in sorted(byfile.items()):
        for x, y in itertools.combinations(g, 2):
            qx, qy = normq(x["quote"]), normq(y["quote"])
            if qx != qy and (qx in qy or qy in qx) and x["tag"] != y["tag"]:
                nb2 += 1
                print(f"[{os.path.basename(lf)}] {x['id']} {x['tag']} vs {y['id']} {y['tag']}")
                print(fmt(x)); print(fmt(y))
    print(f"\n(b2) total near-same-quote pairs with different tags: {nb2}")

    # ---------- (c) key-figure table ----------
    print("\n=== (c) KEY FIGURES BY MODULE (review by hand) ===")
    checks = [
        ("FY2026 Q2 net sales / YoY", lambda r: r["period_fiscal"] == "FY2026 Q2" and re.search(r"net sales|^sales|\bsales\b", r["claim"], re.I) and not re.search(r"SoC|memory|China|Taiwan|Korea|Japan|Americas|Europe|region|segment|Services|Test System|forecast|cost", r["claim"], re.I)),
        ("FY2026 Q2 gross margin", lambda r: r["period_fiscal"] == "FY2026 Q2" and re.search(r"gross", r["claim"], re.I)),
        ("FY2026 Q2 operating income / margin", lambda r: r["period_fiscal"] == "FY2026 Q2" and re.search(r"operating (income|margin|profit)", r["claim"], re.I) and not re.search(r"forecast|segment", r["claim"], re.I)),
        ("FY2026 Q2 SoC / memory sales", lambda r: r["period_fiscal"] == "FY2026 Q2" and re.search(r"\bSoC\b|\bmemory\b", r["claim"], re.I) and re.search(r"sales", r["claim"], re.I)),
        ("LTM sales / GM / OPM / China", lambda r: "LTM" in r["period_fiscal"] or "Oct 2025-Sep 2026" in r["period_calendar"]),
        ("NVIDIA / TSMC / Samsung shares", lambda r: re.search(r"NVIDIA|TSMC|Samsung|Taiwan Semiconductor", r["claim"]) and r["tag"] != "[S]"),
        ("Inventories (balance)", lambda r: re.search(r"^inventor|inventories", r["claim"], re.I) and re.search(r"end|\d{4}$|Mar|Sep|Jun|Dec", r["period_fiscal"] + r["period_calendar"]) and r["unit"].startswith(("JPY", "%")) and not re.search(r"days|valuation|write|loss|reversal", r["claim"], re.I)),
        ("China share", lambda r: re.search(r"China", r["claim"]) and re.search(r"%", r["unit"] + r["value"])),
        ("FY2026 guidance (sales / OI / NI / OPM / GM)", lambda r: r["period_fiscal"].startswith("FY2026") and not re.search(r"Q1|Q2|end", r["period_fiscal"]) and re.search(r"forecast|guidance|expected", r["claim"], re.I) and r["unit"].startswith(("JPY", "%"))),
        ("Buybacks / share repurchases", lambda r: re.search(r"repurchase|buyback", r["claim"], re.I) and r["unit"].lower().startswith(("jpy", "shares", "%"))),
        ("One-off SG&A", lambda r: re.search(r"SG&A|one[- ]time|one[- ]off", r["claim"] + " " + r["note"] + " " + r["quote"], re.I) and re.search(r"SG&A|selling", r["claim"] + r["quote"] + r["note"], re.I)),
        ("Inventory write-down reversal", lambda r: re.search(r"reversal|obsolescence", r["claim"] + " " + r["quote"], re.I)),
    ]
    for title, f in checks:
        hit = [r for r in rows if f(r)]
        print(f"\n-- {title}: {len(hit)} row(s)")
        bymod = defaultdict(list)
        for r in hit:
            bymod[r["_mod"]].append(r)
        for m in MODS:
            for r in bymod.get(m, []):
                print(fmt(r))


if __name__ == "__main__":
    main()
