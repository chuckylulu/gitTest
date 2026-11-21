#!/usr/bin/env python3
"""A3 - FY2026 (Apr 2026-Mar 2027) current guidance: progress and implied 2H.
Guidance current at 2026-11-21 is the 2026-10-28 version (A3-104..A3-108; IR page A3-109).
JPY million unless stated.
"""


def pct(a, b):
    return (a - b) / b * 100


FYG = dict(s=1863000, oi=967000, ibt=1021500, ni=741500)        # A3-104..A3-107
EPSG = 1027.08                                                   # A3-108
H1 = dict(s=845200, oi=456809, ibt=510234, ni=368083)           # A3-217, A3-218, A3-258, A3-219
EPSH1 = 508.99                                                   # A3-220
SL2H = dict(s=1017.8, oi=510.2, ni=373.4)                        # A3-150..A3-152 (slide, JPY bn)
SL2H_EPS = 517.23                                                # A3-153
VAL_H1 = 54171                                                   # A3-260 valuation gains in 1H financial income

print("FY2026 guidance (2026-10-28) vs 1H FY2026 actual")
for k, name in [("s", "Net sales"), ("oi", "Operating income"), ("ibt", "Income before tax"), ("ni", "Net income")]:
    h2 = FYG[k] - H1[k]
    print(f"  {name:18s}: FY guidance {FYG[k]:>10,} | 1H actual {H1[k]:>9,} = {H1[k]/FYG[k]*100:5.1f}% of FY | implied 2H {h2:>9,}"
          + (f" (slide 2H {SL2H[k]:,.1f} bn)" if k in SL2H else ""))
print(f"  Basic EPS: FY {EPSG} | 1H {EPSH1} | implied 2H {EPSG-EPSH1:.2f} (slide 2H {SL2H_EPS})")
h2s = FYG["s"] - H1["s"]
h2oi = FYG["oi"] - H1["oi"]
print(f"  Implied 2H sales vs 1H: {pct(h2s, H1['s']):+.1f}% (management: 'approximately 20%', A3-111)")
print(f"  Implied 2H OPM {h2oi/h2s*100:.1f}% vs 1H OPM {H1['oi']/H1['s']*100:.1f}% (management: 2H OPM to exceed 50%, A3-110)")
print(f"  FY OPM guidance {FYG['oi']/FYG['s']*100:.1f}%")
fin_fy = FYG["ibt"] - FYG["oi"]
fin_h1 = H1["ibt"] - H1["oi"]
print(f"  IBT - OI (net financial income etc.): FY guidance {fin_fy:,}; 1H actual {fin_h1:,}; implied 2H {fin_fy-fin_h1:,}")
print(f"  1H valuation gains on strategic investments {VAL_H1:,} -> guidance assumes about {fin_fy-fin_h1:,} of net financial items in 2H (no repeat of 1H valuation gains implied)")
print(f"  Implied 2H tax share (IBT-NI)/IBT: {((FYG['ibt']-H1['ibt'])-(FYG['ni']-H1['ni']))/(FYG['ibt']-H1['ibt'])*100:.1f}% vs 1H {(H1['ibt']-H1['ni'])/H1['ibt']*100:.1f}%")
