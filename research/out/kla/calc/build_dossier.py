"""Assemble dossier.md = parts/_dossier_head.md + module notes (headings demoted one level).
Usage: python3 -I research/out/kla/calc/build_dossier.py"""
import os, re
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
order = [("Part Q1, Q4, Nova: X-ray vs Rigaku, EUV mask vs Lasertec, Nova overlap", "Q14_notes.md"),
         ("Part Q2, Q3: advanced packaging, hybrid bonding", "Q23_notes.md"),
         ("Part A1, A2: results, segments, services, leading signals", "A12_notes.md"),
         ("Part A3, A6, Q5: guidance record, cycle, supply limits", "A36Q5_notes.md"),
         ("Part A4, A5: concentration, China, export rules, balance sheet, capital", "A45_notes.md")]
out = [open(os.path.join(HERE, "parts", "_dossier_head.md"), encoding="utf-8").read().rstrip(), ""]
for title, f in order:
    t = open(os.path.join(HERE, "parts", f), encoding="utf-8").read()
    t = re.sub(r"^(#+) ", lambda m: "#" + m.group(1) + " ", t, flags=re.M)  # demote
    t = re.sub(r"^## .*\n", "", t, count=1)  # drop the note's own title (now ##)
    # the fiscal year-end is stated once, in the head: drop the notes' own restatements
    t = re.sub(r"^(KLA )?[Ff]iscal year ends June 30\. ", "", t, flags=re.M)
    out += [f"## {title}", "", t.strip(), ""]
open(os.path.join(HERE, "dossier.md"), "w", encoding="utf-8").write("\n".join(out) + "\n")
print("dossier.md lines:", sum(1 for _ in open(os.path.join(HERE, "dossier.md"))))
