"""Build gaps.md: every 'NOT DISCLOSED (read: ...)' / 'NOT RETRIEVED (tried: ...)' in dossier.md, one per line,
with the item it refers to and the dossier section; then every manifest row with status NOT RETRIEVED.
Usage: python3 -I research/out/kla/calc/build_gaps.py (run build_dossier.py first)"""
import csv, os, re
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
MARK = re.compile(r"NOT (DISCLOSED|RETRIEVED) \((read|tried):")

def close_paren(s, i):
    d = 0
    for j in range(i, len(s)):
        if s[j] == "(": d += 1
        elif s[j] == ")":
            d -= 1
            if d == 0: return j + 1
    return len(s)

out = ["# Gap log - KLA (KLAC), FY ends June 30", "",
       "Built by calc/build_gaps.py. Part 1 lists every NOT DISCLOSED / NOT RETRIEVED marker in dossier.md (one per line, with the item and the section). "
       "Part 2 lists every document attempt logged NOT RETRIEVED in sources/kla/_manifest.csv. The same item can appear in two sections when two parts of the dossier record it.", "",
       "## 1. Items in dossier.md", ""]
seen, sec, n, header, prev = set(), "", 0, [], ""
for line in open(os.path.join(HERE, "dossier.md"), encoding="utf-8"):
    line = line.rstrip("\n")
    if line.startswith("#"):
        sec = line.lstrip("# ").strip(); continue
    if line.startswith("|---"):
        header = [c.strip() for c in prev.strip("|").split("|")]; prev = line; continue
    if not line.startswith("|"): header = []
    prev = line
    pieces = [c.strip() for c in line.strip("|").split("|")] if line.startswith("|") else [line.strip("- ").strip()]
    rowlabel = pieces[0] if line.startswith("|") else ""
    for ci, p in enumerate(pieces):
        col = header[ci] if line.startswith("|") and ci < len(header) and ci > 0 else ""
        for m in MARK.finditer(p):
            end = close_paren(p, m.start() + len("NOT DISCLOSED ") if m.group(1) == "DISCLOSED" else m.start() + len("NOT RETRIEVED "))
            marker = p[m.start():end]
            if "(read: ...)" in marker or "(tried: ...)" in marker: continue
            before = p[:m.start()].strip(" :;,.-")
            before = re.split(r"(?<=[.;])\s", before)[-1] if before else ""
            item = (rowlabel + " - " if rowlabel and rowlabel not in before else "") + (col + " - " if col and col not in before else "") + before
            item = re.sub(r"\*\*", "", item)[-160:].strip(" -:") or "(see section)"
            key = re.sub(r"\W+", "", (item + marker).lower())
            if key in seen: continue
            seen.add(key); n += 1
            out.append(f"- [{sec[:60]}] {item}: {marker}")
out += ["", f"({n} items)", "", "## 2. Documents attempted and NOT RETRIEVED (manifest)", ""]
k = 0
for r in csv.DictReader(open(os.path.join(ROOT, "research/sources/kla/_manifest.csv"), encoding="utf-8")):
    if r["status"] == "NOT RETRIEVED":
        k += 1
        out.append(f"- {r['doctype']} ({r['issuer']}, {r['date']}): NOT RETRIEVED (tried: {r['url']}; HTTP {r['http_code'] or 'n/a'}; {r['note'][:140]})")
out.append(f"\n({k} documents)")
open(os.path.join(HERE, "gaps.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("dossier items", n, "manifest", k)
