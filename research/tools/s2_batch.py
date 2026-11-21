#!/usr/bin/env python3
"""Fetch Semantic Scholar paper records (title, abstract, authors, venue, date) for a DOI list
with the batch endpoint (POST, max 500 ids per request) and save each response like fetch.py does.

Usage: python3 -I research/tools/s2_batch.py <company> <doi_list.txt> <doctype-stem>
Saves sources/<company>/<today>_semanticscholar_<doctype-stem>-partN.json, a text copy in _text/,
and one manifest row per request. Unauthenticated, honest User-Agent, >= 3 s between requests,
one retry after 60 s on HTTP 429, nothing else.
"""
import datetime, hashlib, json, os, subprocess, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import fetch  # noqa: E402  (local helper: rate_wait, manifest_append, ROOT, UA_DEFAULT)

URL = ("https://api.semanticscholar.org/graph/v1/paper/batch?fields="
       "title,abstract,authors,venue,publicationDate,externalIds")


def post(ids, out):
    body = json.dumps({"ids": ids})
    for attempt in (1, 2):
        fetch.rate_wait(); time.sleep(2)
        r = subprocess.run(["curl", "-sS", "-m", "180", "-A", fetch.UA_DEFAULT, "-H", "Content-Type: application/json",
                            "-X", "POST", "--data-binary", "@-", "-o", out, "-w", "%{http_code}", URL],
                           input=body, capture_output=True, text=True)
        if r.stdout.strip() == "429" and attempt == 1:
            time.sleep(60); continue
        return r.stdout.strip()


def main():
    company, lst, stem = sys.argv[1:4]
    ids = ["DOI:" + l.strip() for l in open(lst) if l.strip()]
    d = os.path.join(fetch.ROOT, "sources", company)
    today = datetime.date.today().isoformat()
    for n in range(0, len(ids), 500):
        part = n // 500 + 1
        name = f"{today}_semanticscholar_{stem}-part{part}"
        local = os.path.join(d, name + ".json")
        code = post(ids[n:n + 500], local)
        row = dict(local_file=os.path.relpath(local, os.path.dirname(fetch.ROOT)), url=URL + " (POST batch)",
                   date=today, issuer="semanticscholar", doctype=f"{stem}-part{part}", http_code=code,
                   retrieved_utc=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
                   note=f"POST batch of {len(ids[n:n+500])} DOIs from {lst}")
        if code == "200" and os.path.getsize(local) > 0:
            raw = open(local, "rb").read()
            recs = json.loads(raw)
            row.update(status="RETRIEVED", bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
            # text copy: one block per paper so quotes can be located
            with open(os.path.join(d, "_text", name + ".txt"), "w") as fh:
                for rec in recs:
                    if not rec:
                        continue
                    fh.write(f"DOI {rec.get('externalIds', {}).get('DOI')} | {rec.get('title')}\n{rec.get('abstract') or ''}\n\n")
            print(f"RETRIEVED {row['local_file']}: {sum(1 for x in recs if x)} records, "
                  f"{sum(1 for x in recs if x and x.get('abstract'))} with abstract")
        else:
            row.update(status="NOT RETRIEVED")
            if os.path.exists(local):
                os.remove(local)
            print(f"NOT RETRIEVED http={code}")
        fetch.manifest_append(company, row)


if __name__ == "__main__":
    main()
