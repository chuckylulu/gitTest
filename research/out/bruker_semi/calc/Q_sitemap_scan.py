#!/usr/bin/env python3
"""Q: scan the saved bruker.com English sitemap (2026-11-21) for 2026 news, 2026 webinars and
event pages, and flag any whose URL slug mentions X-ray metrology, hybrid metrology, Rigaku,
Onto, SEMICON, SPIE, FCMN, semiconductor, CD-SAXS / XCD. Reads only the saved file."""
import re, sys
p = sys.argv[1] if len(sys.argv) > 1 else "research/sources/bruker_semi/_text/2026-11-21_bruker_sitemap-en.txt"
s = open(p, encoding="utf-8", errors="ignore").read()
urls = sorted(set(re.findall(r"https://www\.bruker\.com/en/news-and-events/[^<\s]+", s)))
news26 = [u for u in urls if "/news/2026/" in u]
web26 = [u for u in urls if "/webinars/2026/" in u]
events = [u for u in urls if "/events/" in u]
pat = re.compile(r"x-ray-metrolog|xray-metrolog|hybrid|rigaku|onto|semicon|spie|fcmn|saxs|xcd|semiconductor|semi-", re.I)
print("2026 news items:", len(news26))
for u in news26:
    print("  NEWS", "FLAG" if pat.search(u) else "    ", u.rsplit("/", 1)[-1])
print("2026 webinars:", len(web26), "flagged:", [u.rsplit("/", 1)[-1] for u in web26 if pat.search(u)])
print("event pages:", len(events), "flagged:", [u.rsplit("/", 1)[-1] for u in events if pat.search(u)])
