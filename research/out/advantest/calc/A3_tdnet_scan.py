#!/usr/bin/env python3
"""A3 (fix round 2, 2026-11-21): scan the public TDnet daily disclosure lists for Advantest (code 6857 / 68570).

Purpose: check whether Advantest filed any Japanese TDnet disclosure between the FY2026 Q2 results (28 Oct 2026)
and the run date (21 Nov 2026) that revises the FY2026 (Apr 2026-Mar 2027) forecast, beyond the English IR news index.

Fetching was done separately with plain GET requests (curl, User-Agent "research-script/1.0 (non-commercial document
research)", one request per page, 1.5 s apart, no retries), one page per URL
https://www.release.tdnet.info/inbs/I_list_<page>_<YYYYMMDD>.html for every calendar day 28 Oct-21 Nov 2026; the
request log is passed as the second argument. The saved pages are untrusted data: this script only reads them as text
with regular expressions and never follows links or runs anything from them.

Usage: python3 -I A3_tdnet_scan.py <dir with I_list_*.html> <fetch log tsv> > A3_tdnet_scan.out.txt
"""
import collections, glob, os, re, sys

ROW = re.compile(r'<td class="[a-z]+-L kjTime" noWrap>([^<]*)</td>\s*'
                 r'<td class="[a-z]+-M kjCode" noWrap>([^<]*)</td>\s*'
                 r'<td class="[a-z]+-M kjName" noWrap>([^<]*)</td>\s*'
                 r'<td class="[a-z]+-M kjTitle" align="left">(.*?)</td>', re.S)
HREF = re.compile(r'href="([^"]*)"')
TAG = re.compile(r"<[^>]+>")
TOTAL = re.compile(r"全(\d+)件")
FORECAST_WORDS = ("業績予想", "予想の修正", "配当予想", "forecast", "Forecast")


def main():
    d, logf = sys.argv[1], sys.argv[2]
    log = [l.rstrip("\n").split("\t") for l in open(logf, encoding="utf-8") if l.strip()]
    codes = collections.Counter(x[2] for x in log)
    print(f"requests logged: {len(log)}; HTTP status counts: {dict(codes)} ('cached' = page fetched once earlier in this round, not re-requested)")
    days = collections.OrderedDict()
    for f in sorted(glob.glob(os.path.join(d, "I_list_*_*.html"))):
        m = re.search(r"I_list_(\d{3})_(\d{8})\.html$", f)
        page, day = int(m.group(1)), m.group(2)
        s = open(f, encoding="utf-8", errors="replace").read()
        t = TOTAL.search(s)
        rows = ROW.findall(s)
        e = days.setdefault(day, {"total": None, "pages": 0, "rows": []})
        if t and e["total"] is None:
            e["total"] = int(t.group(1))
        e["pages"] += 1
        for tm, code, name, cell in rows:
            h = HREF.search(cell)
            e["rows"].append((day, page, tm.strip(), code.strip(), name.strip(), h.group(1) if h else "(no link: deleted item)",
                              TAG.sub("", cell).strip()))
    print(f"days covered: {len(days)} ({min(days)} to {max(days)})")
    all_rows, short = 0, []
    for day, e in days.items():
        n = len(e["rows"])
        all_rows += n
        ok = (e["total"] or 0) == n
        if not ok:
            short.append(day)
        print(f"  {day}: pages {e['pages']}, rows parsed {n}, total printed {e['total']} -> {'complete' if ok else 'INCOMPLETE'}")
    print(f"rows parsed in all: {all_rows}; days where parsed rows differ from the printed total: {len(short)} {short}")
    hits = [r for e in days.values() for r in e["rows"] if r[3] in ("68570", "6857") or "アドバンテスト" in r[4]]
    print(f"\nAdvantest rows (code 68570/6857 or name アドバンテスト): {len(hits)}")
    for day, page, tm, code, name, href, title in hits:
        fc = any(w in title for w in FORECAST_WORDS)
        print(f"  {day} {tm} page {page:03d} code {code} {name} | {title} | {href} | forecast wording: {'YES' if fc else 'no'}")
    fc_hits = [h for h in hits if any(w in h[6] for w in FORECAST_WORDS)]
    print(f"\nAdvantest rows whose title contains forecast wording ({', '.join(FORECAST_WORDS)}): {len(fc_hits)}")


if __name__ == "__main__":
    main()
