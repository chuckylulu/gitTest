#!/usr/bin/env python3
"""Mechanical lint of evidence rows beyond quote presence.

Usage: python3 -I research/tools/row_check.py <evidence.csv> [--out flags.csv] [--fy-start-month 4]

Checks per row:
  PERIOD   fiscal label (FY2026 Q2, FY2025, FY2026 1H, FY2025 9M, FY2025 end, FY2026 Q2 end)
           does not map to the calendar label (fiscal year named by its start year, FY start = April)
  VALUE    [F]/[C] row: a number in `value` appears neither in the quote nor on the cited page
           (commas, parentheses, signs ignored; 1-decimal rounding of the page figures tolerated)
  VERDICT  verdict word (validates/refutes/confirms/proves) in a row that is not [I]
  SECONDARY [F] row whose local file comes from a press/trade/aggregator site
  NOPERIOD [F]/[C] numeric row with an empty period label
"""
import csv, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MON = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SECONDARY_HINTS = ("rcrwireless", "trendforce", "technews", "wing-vc", "simplywallst", "techinsights",
                   "fourweekmba", "bloomberg", "reuters", "nikkei")
VERDICT = re.compile(r"\b(validat\w*|refut\w*|confirm\w*|prove[sn]?|proving)\b", re.I)


def cal(start_m, start_y, n):
    """calendar label for n months starting at (month index 0-11, year)."""
    end_m = (start_m + n - 1) % 12
    end_y = start_y + (start_m + n - 1) // 12
    if start_y == end_y:
        return f"{MON[start_m]}-{MON[end_m]} {end_y}"
    return f"{MON[start_m]} {start_y}-{MON[end_m]} {end_y}"


def expected(pf, fs=3):
    pf = pf.strip()
    m = re.fullmatch(r"FY(\d{4})", pf)
    if m:
        y = int(m.group(1)); return [cal(fs, y, 12)]
    m = re.fullmatch(r"FY(\d{4}) Q([1-4])", pf)
    if m:
        y, q = int(m.group(1)), int(m.group(2)); s = fs + 3 * (q - 1)
        return [cal(s % 12, y + s // 12, 3)]
    m = re.match(r"FY(\d{4}) (1H|2H|9M|6M)\b", pf)
    if m:
        y, k = int(m.group(1)), m.group(2)
        if k in ("1H", "6M"):
            return [cal(fs, y, 6)]
        if k == "2H":
            s = fs + 6; return [cal(s % 12, y + s // 12, 6)]
        return [cal(fs, y, 9)]
    m = re.fullmatch(r"FY(\d{4}) (Q([1-4]) )?end", pf)
    if m:
        y = int(m.group(1)); q = int(m.group(3) or 4)
        e = fs + 3 * q - 1
        return [f"{d} {MON[e % 12]} {y + e // 12}" for d in ("30", "31")] + [f"{MON[e % 12]} {y + e // 12}"]
    return None


def nums(s):
    out = []
    for t in re.findall(r"-?\(?\d[\d,]*\.?\d*\)?", s or ""):
        t = t.replace(",", "").replace("(", "").replace(")", "").lstrip("-")
        if t and t not in (".",):
            out.append(t.rstrip("."))
    return out


def page_text(local, pages):
    p = os.path.join(ROOT, local)
    d, f = os.path.split(p)
    tp = os.path.join(d, "_text", os.path.splitext(f)[0] + ".txt")
    if not os.path.exists(tp):
        return ""
    chunks = open(tp, encoding="utf-8", errors="replace").read().split("\f")
    if not pages:
        return "\n".join(chunks)
    return "\n".join(chunks[i - 1] for i in pages if 0 < i <= len(chunks))


def present(n, hay):
    if n in hay:
        return True
    try:
        v = float(n)
    except ValueError:
        return False
    for h in hay:
        try:
            if abs(float(h) - v) < 1e-9 or round(float(h), 1) == v:
                return True
        except ValueError:
            pass
    return False


def main():
    src = sys.argv[1]
    out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
    fs = int(sys.argv[sys.argv.index("--fy-start-month") + 1]) - 1 if "--fy-start-month" in sys.argv else 3
    rows = list(csv.DictReader(open(src, encoding="utf-8")))
    flags, counts, cache = [], {}, {}
    for r in rows:
        tag, f = r["tag"].strip(), []
        pf, pc = r["period_fiscal"].strip(), r["period_calendar"].strip()
        exp = expected(pf, fs)
        if exp is not None and pc and not any(pc.startswith(e) or e in pc for e in exp):
            f.append(f"PERIOD {pf!r} -> expected {exp[0]!r}, got {pc!r}")
        vn = nums(r["value"])
        if tag in ("[F]", "[C]") and vn and not pf and not pc:
            f.append("NOPERIOD")
        if tag in ("[F]", "[C]") and vn and r["local_file"].strip():
            qn = nums(r["quote"])
            missing = [n for n in vn if not present(n, qn)]
            if missing:
                pg = [int(x) for x in re.findall(r"(?:^|p\.|pp\.|page )\s*(\d+)", r["page_or_section"])[:3]]
                key = (r["local_file"], tuple(pg))
                if key not in cache:
                    cache[key] = nums(page_text(r["local_file"].strip(), pg))
                still = [n for n in missing if not present(n, cache[key])]
                if still:
                    f.append(f"VALUE not on cited page: {still[:4]}")
        if tag != "[I]" and VERDICT.search(" ".join([r["claim"], r["note"]])):
            f.append("VERDICT word outside [I]: " + VERDICT.search(" ".join([r["claim"], r["note"]])).group(0))
        lf = r["local_file"].lower()
        if tag == "[F]" and (any(h in lf for h in SECONDARY_HINTS) or re.search(r"_press-(?!release)", lf)):
            f.append("SECONDARY source tagged [F]")
        for x in f:
            k = x.split(" ")[0]
            counts[k] = counts.get(k, 0) + 1
        if f:
            flags.append(dict(id=r["id"], tag=tag, flags=" | ".join(f), value=r["value"][:60],
                              period_fiscal=pf, period_calendar=pc, page=r["page_or_section"][:40]))
    print("rows", len(rows), "flagged", len(flags), counts)
    for x in flags[:400]:
        print(f"{x['id']}\t{x['tag']}\t{x['flags']}\t{x['value']}\t{x['page']}")
    if out:
        with open(out, "w", newline="") as fh:
            w = csv.DictWriter(fh, fieldnames=["id", "tag", "flags", "value", "period_fiscal", "period_calendar", "page"])
            w.writeheader(); w.writerows(flags)


if __name__ == "__main__":
    main()
