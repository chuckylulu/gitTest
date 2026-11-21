#!/usr/bin/env python3
"""Polite downloader for primary documents.

Saves to research/sources/<company>/<date>_<issuer>_<doctype>.<ext>, extracts text to
research/sources/<company>/_text/<stem>.txt (pages separated by form feed for PDFs),
and appends one row per attempt to research/sources/<company>/_manifest.csv.

Usage:
  python3 -I research/tools/fetch.py --company advantest --url URL --date 2026-10-28 \
      --issuer advantest --doctype financial-results-FY2026Q2 [--ext pdf] [--note TEXT]
  python3 -I research/tools/fetch.py --company advantest --batch list.tsv
      (tsv columns: url, date, issuer, doctype[, ext[, note]]; lines starting with # skipped)

Rules honoured: honest User-Agent, >=1.2 s between requests across processes, no retries
around refusals (403/401/429 are logged as NOT RETRIEVED), sec.gov only when SEC_UA is set
by the user in the environment. Downloaded content is never executed.
"""
import argparse, csv, datetime, fcntl, hashlib, os, re, subprocess, sys, time
from urllib.parse import urlparse

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # research/
UA_DEFAULT = "research-script/1.0 (non-commercial document research)"
LOCK = os.path.join(ROOT, "tools", ".fetch_rate.lock")
MIN_GAP = 1.2
FIELDS = ["local_file", "url", "date", "issuer", "doctype", "status", "http_code",
          "bytes", "sha256", "pages", "retrieved_utc", "note"]


def rate_wait():
    os.makedirs(os.path.dirname(LOCK), exist_ok=True)
    with open(LOCK, "a+") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        f.seek(0)
        try:
            last = float(f.read().strip() or 0)
        except ValueError:
            last = 0
        gap = time.time() - last
        if gap < MIN_GAP:
            time.sleep(MIN_GAP - gap)
        f.seek(0); f.truncate(); f.write(str(time.time()))
        fcntl.flock(f, fcntl.LOCK_UN)


def manifest_append(company, row):
    path = os.path.join(ROOT, "sources", company, "_manifest.csv")
    new = not os.path.exists(path)
    with open(path, "a", newline="") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        w = csv.DictWriter(f, fieldnames=FIELDS)
        if new or os.path.getsize(path) == 0:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in FIELDS})
        fcntl.flock(f, fcntl.LOCK_UN)


def slug(s):
    return re.sub(r"[^A-Za-z0-9.\-]+", "-", s).strip("-")


def to_text(local, ext, txt_path):
    pages = ""
    if ext == "pdf":
        subprocess.run(["pdftotext", "-layout", local, txt_path], check=False,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        info = subprocess.run(["pdfinfo", local], capture_output=True, text=True)
        m = re.search(r"Pages:\s+(\d+)", info.stdout)
        pages = m.group(1) if m else ""
    elif ext in ("html", "htm"):
        from bs4 import BeautifulSoup
        with open(local, "rb") as fh:
            soup = BeautifulSoup(fh.read(), "html.parser")
        for t in soup(["script", "style", "noscript"]):
            t.decompose()
        text = soup.get_text("\n")
        text = re.sub(r"\n\s*\n+", "\n\n", text)
        with open(txt_path, "w") as fh:
            fh.write(text)
    elif ext in ("txt", "csv", "json", "xml"):
        with open(local, "rb") as src, open(txt_path, "wb") as dst:
            dst.write(src.read())
    return pages


def fetch_one(company, url, date, issuer, doctype, ext=None, note=""):
    host = urlparse(url).hostname or ""
    if not ext:
        p = urlparse(url).path.lower()
        ext = p.rsplit(".", 1)[-1] if "." in p.rsplit("/", 1)[-1] else "html"
        if ext not in ("pdf", "html", "htm", "xlsx", "xls", "csv", "txt", "json", "xml", "zip"):
            ext = "html"
    d = os.path.join(ROOT, "sources", company)
    os.makedirs(os.path.join(d, "_text"), exist_ok=True)
    auto = date == "auto"
    if auto:
        # reuse an earlier download of the same URL if the manifest has one
        mp = os.path.join(d, "_manifest.csv")
        if os.path.exists(mp):
            for mr in csv.DictReader(open(mp)):
                if mr["url"] == url and mr["status"] == "RETRIEVED":
                    print(f"EXISTS {mr['local_file']}")
                    return mr["local_file"]
    stem = f"{date}_{slug(issuer)}_{slug(doctype)}"
    local = os.path.join(d, f"{stem}.{ext}")
    rel = os.path.relpath(local, os.path.dirname(ROOT))
    row = dict(local_file=rel, url=url, date=date, issuer=issuer, doctype=doctype, note=note,
               retrieved_utc=datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"))
    if not auto and os.path.exists(local) and os.path.getsize(local) > 0:
        print(f"EXISTS {rel}")
        return rel
    ua = os.environ.get("RESEARCH_UA", UA_DEFAULT)
    if host.endswith("sec.gov"):
        ua = os.environ.get("SEC_UA", "")
        if not ua:
            row.update(status="NOT RETRIEVED", note=(note + " | sec.gov requires contact User-Agent; SEC_UA not set").strip(" |"))
            manifest_append(company, row)
            print(f"NOT RETRIEVED (SEC_UA not set) {url}")
            return None
    rate_wait()
    tmp = os.path.join(d, f"_tmp_{slug(doctype)}.part")
    r = subprocess.run(["curl", "-sS", "-L", "--max-time", "180", "-A", ua, "-o", tmp,
                        "-w", "%{http_code} %{content_type}", url], capture_output=True, text=True)
    code, _, ctype = (r.stdout.strip() + "  ").partition(" ")
    ok = r.returncode == 0 and code.startswith("2") and os.path.exists(tmp) and os.path.getsize(tmp) > 0
    if ok and ext == "pdf":
        with open(tmp, "rb") as fh:
            if not fh.read(5).startswith(b"%PDF"):
                ok = False
                ctype = "not a PDF: " + ctype.strip()
    if not ok:
        if os.path.exists(tmp):
            os.remove(tmp)
        row.update(status="NOT RETRIEVED", http_code=code,
                   note=(note + f" | curl rc={r.returncode} {ctype.strip()} {r.stderr.strip()[:120]}").strip(" |"))
        manifest_append(company, row)
        print(f"NOT RETRIEVED http={code} {url}")
        return None
    if auto:
        date = ""
        if ext == "pdf":
            info = subprocess.run(["pdfinfo", "-isodates", tmp], capture_output=True, text=True).stdout
            for key in ("CreationDate", "ModDate"):
                m = re.search(key + r":\s+(\d{4}-\d{2}-\d{2})", info)
                if m:
                    date = m.group(1); note = (note + f" | date from PDF {key}").strip(" |"); break
        if not date:
            date = datetime.date.today().isoformat(); note = (note + " | date = retrieval date").strip(" |")
        stem = f"{date}_{slug(issuer)}_{slug(doctype)}"
        local = os.path.join(d, f"{stem}.{ext}")
        rel = os.path.relpath(local, os.path.dirname(ROOT))
        row.update(local_file=rel, date=date, note=note)
        if os.path.exists(local) and os.path.getsize(local) > 0:
            os.remove(tmp); print(f"EXISTS {rel}"); return rel
    os.replace(tmp, local)
    with open(local, "rb") as fh:
        sha = hashlib.sha256(fh.read()).hexdigest()
    pages = to_text(local, ext, os.path.join(d, "_text", f"{stem}.txt"))
    row.update(status="RETRIEVED", http_code=code, bytes=os.path.getsize(local), sha256=sha, pages=pages)
    manifest_append(company, row)
    print(f"RETRIEVED {rel} ({row['bytes']} bytes, {pages or '-'} pages)")
    return rel


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--company", required=True)
    ap.add_argument("--url"); ap.add_argument("--date"); ap.add_argument("--issuer")
    ap.add_argument("--doctype"); ap.add_argument("--ext"); ap.add_argument("--note", default="")
    ap.add_argument("--batch")
    a = ap.parse_args()
    if a.batch:
        with open(a.batch) as fh:
            for line in fh:
                if not line.strip() or line.startswith("#"):
                    continue
                parts = line.rstrip("\n").split("\t")
                parts += [""] * (6 - len(parts))
                fetch_one(a.company, parts[0], parts[1], parts[2], parts[3], parts[4] or None, parts[5])
    else:
        if not all([a.url, a.date, a.issuer, a.doctype]):
            sys.exit("need --url --date --issuer --doctype or --batch")
        fetch_one(a.company, a.url, a.date, a.issuer, a.doctype, a.ext, a.note)


if __name__ == "__main__":
    main()
