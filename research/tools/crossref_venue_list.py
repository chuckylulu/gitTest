#!/usr/bin/env python3
"""Build Crossref listing URLs for whole conference volumes and save them with fetch.py.

Usage: python3 -I research/tools/crossref_venue_list.py <company-folder> <venues.tsv>
venues.tsv columns: slug, exact container-title, from-pub-date (YYYY-MM-DD)
Each volume is saved once (rows=1000, one request) as
sources/<company>/<today>_crossref_<slug>-volume-list.json via fetch.py.
"""
import datetime, os, subprocess, sys, urllib.parse
HERE = os.path.dirname(os.path.abspath(__file__))
SELECT = "DOI,title,author,container-title,published,issued,page,abstract,type"


def main():
    company, tsv = sys.argv[1], sys.argv[2]
    today = datetime.date.today().isoformat()
    for line in open(tsv):
        if not line.strip() or line.startswith("#"):
            continue
        slug, title, frm = line.rstrip("\n").split("\t")
        q = {"filter": f"container-title:{title},from-pub-date:{frm}", "rows": "1000", "select": SELECT}
        url = "https://api.crossref.org/works?" + urllib.parse.urlencode(q)
        subprocess.run([sys.executable, "-I", os.path.join(HERE, "fetch.py"), "--company", company,
                        "--url", url, "--date", today, "--issuer", "crossref",
                        "--doctype", f"{slug}-volume-list", "--ext", "json",
                        "--note", f"Crossref volume listing: {title}"])


if __name__ == "__main__":
    main()
