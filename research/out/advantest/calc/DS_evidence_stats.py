#!/usr/bin/env python3
"""DS (dossier) method section: evidence rows by tag and module, and saved sources by manifest status.

Inputs: research/out/advantest/evidence.csv (merged parts) and research/sources/advantest/_manifest.csv.
Run from the repo root: python3 -I research/out/advantest/calc/DS_evidence_stats.py
DS rows (the dossier's own [I] rows) are counted separately so the module totals are unaffected.
"""
import csv, os, collections

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..", ".."))
EV = os.path.join(ROOT, "research", "out", "advantest", "evidence.csv")
MAN = os.path.join(ROOT, "research", "sources", "advantest", "_manifest.csv")


def main():
    rows = list(csv.DictReader(open(EV, encoding="utf-8")))
    mods = collections.OrderedDict()
    for r in rows:
        mod = r["id"].split("-")[0]
        mods.setdefault(mod, collections.Counter())[r["tag"]] += 1
    tags = ["[F]", "[C]", "[S]", "[I]"]
    print("module | " + " | ".join(tags) + " | total")
    tot = collections.Counter()
    for m, c in mods.items():
        print(f"{m} | " + " | ".join(str(c[t]) for t in tags) + f" | {sum(c.values())}")
        if m != "DS":
            tot.update(c)
    print("RESULT module rows (excl. DS): " + ", ".join(f"{t} {tot[t]}" for t in tags) +
          f"; total {sum(tot.values())}")
    man = list(csv.DictReader(open(MAN, encoding="utf-8")))
    st = collections.Counter(r["status"] for r in man)
    print("RESULT manifest rows: " + ", ".join(f"{k} {v}" for k, v in sorted(st.items())) + f"; total {len(man)}")
    iss = collections.Counter(r["issuer"] for r in man if r["status"] == "RETRIEVED")
    print("RETRIEVED by issuer: " + ", ".join(f"{k} {v}" for k, v in iss.most_common()))
    adv = iss.get("advantest", 0)
    print(f"RESULT retrieved documents issued by Advantest: {adv}; by others: {sum(iss.values()) - adv}")


if __name__ == "__main__":
    main()
