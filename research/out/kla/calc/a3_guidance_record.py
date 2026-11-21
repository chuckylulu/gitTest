#!/usr/bin/env python3
"""A3 guidance record for KLA (FY ends June 30).
Inputs typed from shareholder letters (guidance) and earnings releases (results); sources in A3.csv.
Rule: value > top of range = BEAT; bottom <= value <= top = IN-LINE; value < bottom = MISS.
EPS: guidance issued before the 10-for-1 split (effective after close 2026-06-11) is divided by 10
to compare with post-split results (Q4 FY26 guidance issued 2026-04-29 pre-split, reported post-split)."""
SPLIT = 10
# quarter, calendar, rev_mid($M), rev_pm, gm_mid(%), gm_pm, ngeps_mid, ngeps_pm, geps_mid, geps_pm, guide_presplit,
# actual rev($M), actual ng GM, actual ng EPS, actual GAAP EPS, results_postsplit
Q = [
 ("Q2 FY25","Oct-Dec 2024",2950,150,61.5,1.0,7.75,0.60,7.45,0.60,True, 3076.851,61.7,8.20,6.16,False),
 ("Q3 FY25","Jan-Mar 2025",3000,150,62.0,1.0,8.05,0.60,7.77,0.60,True, 3063.029,63.0,8.41,8.16,False),
 ("Q4 FY25","Apr-Jun 2025",3075,150,63.0,1.0,8.53,0.78,8.28,0.78,True, 3174.741,63.2,9.38,9.06,False),
 ("Q1 FY26","Jul-Sep 2025",3150,150,62.0,1.0,8.53,0.77,8.28,0.77,True, 3209.696,62.5,8.81,8.47,False),
 ("Q2 FY26","Oct-Dec 2025",3225,150,62.0,1.0,8.70,0.78,8.46,0.78,True, 3297.146,62.6,8.85,8.68,False),
 ("Q3 FY26","Jan-Mar 2026",3350,150,61.75,1.0,9.08,0.78,8.85,0.78,True, 3415.078,62.2,9.40,9.12,False),
 ("Q4 FY26","Apr-Jun 2026",3575,200,61.75,1.0,9.87,1.00,9.66,1.00,True, 3657.556,62.4,1.05,1.04,True),
 ("Q1 FY27","Jul-Sep 2026",4000,200,62.5,1.0,1.16,0.10,1.14,0.10,False,4136.015,62.7,1.22,1.18,True),
]
def cls(v, mid, pm):
    lo, hi = round(mid-pm,4), round(mid+pm,4)
    return ("BEAT" if v > hi else "MISS" if v < lo else "IN-LINE"), lo, hi
counts = {}
print("quarter|cal|metric|guide_mid|low|high|actual|vs_mid|class")
for q in Q:
    (n,c,rm,rp,gm,gp,nm,npm,gem,gep,pre,ar,agm,aen,aeg,post) = q
    f = SPLIT if (pre and post) else 1
    rows = [("Revenue $M",rm,rp,ar),("Non-GAAP GM %",gm,gp,agm),
            ("Non-GAAP EPS",nm/f,npm/f,aen),("GAAP EPS",gem/f,gep/f,aeg)]
    for m,mid,pm,a in rows:
        k,lo,hi = cls(a,mid,pm)
        counts.setdefault(m,{}).setdefault(k,0); counts[m][k]+=1
        print(f"{n}|{c}|{m}|{mid:.4g}|{lo:.4g}|{hi:.4g}|{a}|{a-mid:+.4g} ({(a-mid)/mid*100:+.1f}%)|{k}")
print("\nCOUNTS (8 quarters):")
for m,d in counts.items(): print(m, d)
# One-off: Q2 FY25 GAAP EPS incl. $239.1M goodwill/intangible impairment = $1.76/share (release)
ex = 6.16+1.76
print(f"\nQ2 FY25 GAAP EPS ex-impairment: {ex:.2f} vs range {7.45-0.60:.2f}-{7.45+0.60:.2f} -> {cls(ex,7.45,0.60)[0]}")
# Tax-rate effect named by management: non-GAAP EPS at guided 13.5% tax rate
for n,v,mid,pm in [("Q4 FY25",9.00,8.53,0.78),("Q3 FY25",8.55,8.05,0.60)]:
    print(f"{n} non-GAAP EPS at guided tax rate {v} -> {cls(v,mid,pm)[0]}")
# Current guidance Q2 FY27 (Oct-Dec 2026), post-split
print("\nQ2 FY27 guide: rev 4500-4900 mid 4700; ngGM 61.5-63.5; ngEPS 1.33-1.55; GAAP EPS 1.30-1.52")
# --- Calendar-year checks ---
cy25 = [3063.029,3174.741,3209.696,3297.146]
print(f"\nCY25 revenue {sum(cy25):.1f}")
h2cy25 = 3209.696+3297.146; h1cy26 = 3415.078+3657.556
print(f"H1 CY26 vs H2 CY25: {h1cy26:.1f} vs {h2cy25:.1f} = {(h1cy26/h2cy25-1)*100:+.1f}%")
h2cy26 = 4136.015+4700
print(f"H2 CY26 (Q1FY27 actual + Q2FY27 guide mid) {h2cy26:.1f} vs H1 CY26: {(h2cy26/h1cy26-1)*100:+.1f}%; range {(4136.015+4500)/h1cy26*100-100:+.1f}% to {(4136.015+4900)/h1cy26*100-100:+.1f}%")
cy26 = h1cy26+h2cy26
print(f"CY26 implied revenue {cy26:.1f} (range {h1cy26+4136.015+4500:.1f}-{h1cy26+4136.015+4900:.1f}); YoY vs CY25 {(cy26/sum(cy25)-1)*100:+.1f}%")
print(f"2022 Investor Day CY26 target 14000 +/-500 (13500-14500): implied CY26 exceeds top by {cy26-14500:.1f}")
# CY26 non-GAAP GM and OM (Q3FY26..Q1FY27 actual, Q2FY27 guide mid)
rev = [3415.078,3657.556,4136.015,4700]; gmp=[62.2,62.4,62.7,62.5]; omp=[42.6,43.7,46.1,None]
om_g = (4700*0.625-710)/4700*100
omp[3]=om_g
gm = sum(r*g for r,g in zip(rev,gmp))/sum(rev); om = sum(r*o for r,o in zip(rev,omp))/sum(rev)
print(f"Q2FY27 implied non-GAAP OM from guide (rev*GM - opex $710M)/rev = {om_g:.1f}%")
print(f"CY26 implied non-GAAP GM {gm:.2f}% (target ~63%; CY26 guide 62% +/-0.5) ; OM {om:.1f}% (target 41-43%)")
eps = 9.40/SPLIT+1.05+1.22+1.44
print(f"CY26 implied non-GAAP EPS (post-split) {eps:.2f} = pre-split {eps*SPLIT:.1f} vs target 38 +/-1.50 (pre-split; {3.80-0.15:.3f}-{3.80+0.15:.3f} post-split)")
