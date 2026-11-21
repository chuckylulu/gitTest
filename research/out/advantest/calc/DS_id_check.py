#!/usr/bin/env python3
"""DS (dossier) mechanical checks on research/out/advantest/dossier.md.

1. Every evidence id cited in the dossier exists in evidence.csv (ranges 'X-001 to X-005' expanded).
2. Tag consistency: for each '[T] (ids)' or '[T] High|Medium|Low (ids)' group, every id in the
   parentheses carries tag T in evidence.csv.
3. Every [I] tag is followed by a confidence word (High / Medium / Low).
4. Verdict words (validates, refutes, confirms, proves and their stems) - listed for review;
   the project rules allow them only inside [I] statements.
5. Valuation / price / recommendation vocabulary - listed for review.
6. How often the fiscal-year-end sentence appears (the dossier states it once).
7. Informational: a number written just before '[T] (one id)' should appear in that evidence row.

Run from the repo root: python3 -I research/out/advantest/calc/DS_id_check.py
Exit code 1 if check 1, 2 or 3 finds a problem.
"""
import csv, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
OUT = os.path.join(ROOT, "research", "out", "advantest")
DOSSIER = os.path.join(OUT, "dossier.md")
EV = os.path.join(OUT, "evidence.csv")

ID = r"(?:A[1-6]|TH|CL|DS)-\d{3}"


def expand(text):
    """Return the list of ids in a text span, expanding 'X-nnn to X-mmm' and 'X-nnn..X-mmm' ranges."""
    ids = []
    for m in re.finditer(rf"({ID})\s*(?:to|\.\.)\s*({ID})", text):
        a, b = m.group(1), m.group(2)
        pa, na = a.split("-")
        pb, nb = b.split("-")
        if pa == pb and int(na) <= int(nb):
            ids += [f"{pa}-{i:03d}" for i in range(int(na), int(nb) + 1)]
    text2 = re.sub(rf"({ID})\s*(?:to|\.\.)\s*({ID})", " ", text)
    ids += re.findall(ID, text2)
    return ids


def main():
    tags = {r["id"]: r["tag"] for r in csv.DictReader(open(EV, encoding="utf-8"))}
    lines = open(DOSSIER, encoding="utf-8").read().splitlines()
    problems = 0

    # 1. ids exist
    cited = []
    for n, l in enumerate(lines, 1):
        for i in expand(l):
            cited.append((n, i))
    missing = sorted({(i, n) for n, i in cited if i not in tags})
    uniq = sorted({i for _, i in cited})
    print(f"[1] distinct ids cited: {len(uniq)}; total citations: {len(cited)}")
    print(f"[1] cited ids not found in evidence.csv: {len(missing)}")
    for i, n in missing:
        print(f"    MISSING {i} (line {n})")
    problems += len(missing)

    # 2. tag consistency
    pat = re.compile(r"\[(F|C|S|I)\](?:\s+(?:High|Medium|Low))?\s*\(([^()]*)\)")
    mism = []
    for n, l in enumerate(lines, 1):
        for m in pat.finditer(l):
            t = f"[{m.group(1)}]"
            for i in expand(m.group(2)):
                if i in tags and tags[i] != t:
                    mism.append((n, t, i, tags[i]))
    print(f"[2] tag mismatches (cited tag vs evidence tag): {len(mism)}")
    for n, t, i, et in mism:
        print(f"    line {n}: cited {t} for {i}, evidence has {et}")
    problems += len(mism)

    # 3. [I] without confidence
    noconf = []
    for n, l in enumerate(lines, 1):
        for m in re.finditer(r"\[I\](?!\s+(?:High|Medium|Low)\b)", l):
            ctx = l[m.start():m.start() + 40]
            # allow the tag legend and generic mentions ("[I] rows", "[I] check", "[I] with")
            if re.match(r"\[I\]\s*(=|rows|check|with|[.,]|, a calculation)", ctx) or "every calculation is [I]" in l:
                continue
            noconf.append((n, ctx))
    print(f"[3] [I] tags without High/Medium/Low: {len(noconf)}")
    for n, c in noconf:
        print(f"    line {n}: {c}")
    problems += len(noconf)

    # 4. verdict words
    vw = re.compile(r"\b(validat\w*|refut\w*|confirm\w*|prov(?:e|es|ed|ing)\b)", re.I)
    hits = [(n, m.group(0)) for n, l in enumerate(lines, 1) for m in vw.finditer(l)]
    print(f"[4] verdict-word occurrences: {len(hits)}")
    for n, w in hits:
        print(f"    line {n}: {w}")

    # 5. valuation vocabulary
    vv = re.compile(r"\b(valuation|multiple[s]?|P/E|EV/|price target|target price|market cap\w*|undervalued|overvalued|"
                    r"buy rating|sell rating|outperform|underperform|upside|downside)\b", re.I)
    vh = [(n, m.group(0)) for n, l in enumerate(lines, 1) for m in vv.finditer(l)]
    print(f"[5] valuation-vocabulary occurrences (review by hand): {len(vh)}")
    for n, w in vh:
        print(f"    line {n}: {w} | {lines[n-1][:140]}")

    # 6. FY-end sentence
    fy = [n for n, l in enumerate(lines, 1) if re.search(r"[Ff]iscal year ends 31 March", l)]
    print(f"[6] lines stating the fiscal-year end: {len(fy)} {fy}")

    # 7. value spot check (informational): a number written immediately before '[T] (one id)' should
    #    appear in that row's value, claim, quote or note
    rows = {r["id"]: r for r in csv.DictReader(open(EV, encoding="utf-8"))}
    vp = re.compile(r"([-+(]?\d[\d,]*(?:\.\d+)?%?\)?)(?:\s*(?:bn|m|pp|days|x))?\s*\[(F|C|S|I)\](?:\s+(?:High|Medium|Low))?\s*\((" + ID + r")\)")
    miss7 = []
    norm = lambda x: x.replace(",", "").replace("(", "").replace(")", "").replace("+", "").replace("%", "").lstrip("-")
    for n, l in enumerate(lines, 1):
        for m in vp.finditer(l):
            num, i = m.group(1), m.group(3)
            r = rows.get(i)
            if not r:
                continue
            hay = " ".join([r["value"], r["claim"], r["quote"], r["note"]]).replace(",", "")
            if re.fullmatch(r"20[0-3]\d", norm(num)):
                continue  # a year in a period label, not a value
            if norm(num) and norm(num) not in hay:
                miss7.append((n, num, i, r["value"][:40]))
    print(f"[7] number-before-tag not found in the cited row (review by hand): {len(miss7)}")
    for n, num, i, v in miss7:
        print(f"    line {n}: '{num}' vs {i} value '{v}'")

    # 8. period labels (informational): in each line, every fiscal label (FY2025, FY2026 Q2, 1H FY2026 ...)
    #    should appear at least once with calendar months next to it, e.g. 'FY2026 Q2 (Jul-Sep 2026)'
    MON = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)"
    lab = re.compile(r"(?<![\w-])((?:[12]H )?FY20\d\d(?: Q[1-4]| 1H| 2H| 9M)?)(?![\w-])")
    nolab = []
    for n, l in enumerate(lines, 1):
        if l.startswith("#"):
            continue
        labels = {}
        for m in lab.finditer(l):
            after = l[m.end():m.end() + 30]
            before = l[max(0, m.start() - 30):m.start()]
            ok = bool(re.match(rf"\s*\(?\s*(?:end\s*,?\s*)?(?:\d{{1,2}} )?{MON}", after)) or \
                 bool(re.match(rf",?\s*{MON}", after)) or bool(re.search(rf"{MON}[a-z]* \d{{4}}\s*\($", before))
            labels.setdefault(m.group(1), False)
            labels[m.group(1)] = labels[m.group(1)] or ok
        bad = [k for k, v in labels.items() if not v]
        if bad:
            nolab.append((n, bad))
    print(f"[8] lines with a fiscal label that never carries calendar months in that line (review): {len(nolab)}")
    for n, bad in nolab:
        print(f"    line {n}: {', '.join(bad)} | {lines[n-1][:90]}")

    print(f"RESULT problems in checks 1-3: {problems}")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
