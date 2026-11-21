"""A4: parse KLA revenue-by-region tables from saved 10-Q/10-K text files.
Prints every geography table found (region -> list of amounts in $ thousands, in column order),
plus the header lines, so column mapping can be checked by eye. Output also saved as JSON."""
import json, re, sys, pathlib
TXT = pathlib.Path(__file__).resolve().parents[3] / "sources/kla/_text"
REGIONS = ["China","Taiwan","Korea","Japan","North America","Europe and Israel","Rest of Asia","Total"]
PHRASES = ["summary of revenues by geographic region", "Revenues by region, based on ship-to location"]
out = {}
for f in sorted(TXT.glob("*")):
    if not re.search(r"10-[QK]", f.name):
        continue
    lines = [l.strip() for l in f.read_text(errors="ignore").splitlines()]
    tables = []
    for i, l in enumerate(lines):
        if not any(p in l for p in PHRASES):
            continue
        # header = lines until first region label
        j = i + 1; header = []
        while j < len(lines) and lines[j] not in REGIONS and j < i + 40:
            if lines[j]: header.append(lines[j])
            j += 1
        tab = {}; cur = None
        while j < len(lines) and j < i + 400:
            t = lines[j].replace(" ", " ").strip()
            if t in REGIONS:
                cur = t; tab[cur] = []
            elif cur and re.fullmatch(r"\(?[\d,]+\)?", t) and "," in t:
                v = int(t.strip("()").replace(",", ""))
                tab[cur].append(-v if t.startswith("(") else v)
            elif cur == "Total" and re.match(r"[A-Za-z]", t) and len(t) > 25:
                break
            j += 1
        tables.append({"line": i + 1, "header": header[:14], "amounts": tab})
    out[f.name] = tables
json.dump(out, open(pathlib.Path(__file__).with_name("a4_region_tables.json"), "w"), indent=1)
for fn, tabs in out.items():
    for t in tabs:
        print("==", fn, "line", t["line"], "|", " / ".join(t["header"]))
        for r, v in t["amounts"].items():
            print("   ", r, v)
