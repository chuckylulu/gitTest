"""A4: parse the MD&A 'Revenues by segment' tables (three-month columns) from each saved 10-Q/10-K text.
Prints amounts ($ thousands) per segment in column order (current, prior[, delta])."""
import re, pathlib
TXT = pathlib.Path(__file__).resolve().parents[3] / "sources/kla/_text"
SEGS = ["Semiconductor Process Control", "Specialty Semiconductor Process",
        "PCB, Display and Component Inspection", "PCB and Component Inspection",
        "Total revenues for reportable segments"]
for f in sorted(TXT.glob("*10-[QK]*.txt")):
    lines = [l.strip() for l in f.read_text(errors="ignore").splitlines()]
    for i, l in enumerate(lines):
        if l != "Revenues by segment":
            continue
        hdr = [x for x in lines[i+1:i+12] if x][:9]
        j = i + 1; cur = None; tab = {}
        while j < i + 120:
            t = lines[j]
            if t in SEGS:
                cur = t; tab[cur] = []
            elif cur and re.fullmatch(r"\(?[\d,]+\)?", t) and "," in t:
                tab[cur].append(int(t.strip("()").replace(",", "")) * (-1 if t.startswith("(") else 1))
            if t.startswith("Total revenues for reportable") and cur:
                pass
            if cur == "Total revenues for reportable segments" and len(tab[cur]) >= 3:
                break
            j += 1
        print("==", f.name, i+1, "|", " / ".join(hdr))
        for k, v in tab.items():
            print("   ", k, v)
