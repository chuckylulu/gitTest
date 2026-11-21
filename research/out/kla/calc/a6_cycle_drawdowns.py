#!/usr/bin/env python3
"""A6 cycle drawdowns for KLA (FY ends June 30). All $ thousands, typed from saved filings (see A6.csv).
GAAP operating income (OI): taken directly where the filing reports 'Income from operations' (FY09/FY13 10-K Note,
FY16 10-Qs); for FY23-FY24 KLA reports no operating subtotal, so OI = revenue - costs of revenues - R&D - SG&A
- goodwill/intangible impairment (i.e. before interest, debt-extinguishment and other income/expense).
Non-GAAP OI (FY23-FY24 only) = GAAP OI + pre-tax non-GAAP adjustments booked in operating lines
(costs of revenues, R&D, SG&A, impairment), from the earnings-release tables."""
def pct(a,b): return (a/b-1)*100
# ---------- CY2022-23 downturn ----------
# Q2FY23 10-Q: 3M Dec-22 and 6M; Q3FY23 10-Q: 3M Mar-23 and 9M; FY23 10-K annual; FY24 10-Qs and 10-K.
d = {}
d["Q1FY23"] = dict(cal="Jul-Sep 2022", rev=2724424, cor=1041226, rd=318515, sga=253980, imp=0)       # Q1FY24 10-Q comparative
d["Q2FY23"] = dict(cal="Oct-Dec 2022", rev=2983887, cor=1208786, rd=332826, sga=243096, imp=0)
d["Q3FY23"] = dict(cal="Jan-Mar 2023", rev=2432608, cor=1005346, rd=328276, sga=238393, imp=0)
fy23 = dict(rev=10496056, cor=4218307, rd=1296727, sga=986326, imp=0); m9_23 = dict(rev=8140919, cor=3255358, rd=979617, sga=735469, imp=0)
d["Q4FY23"] = dict(cal="Apr-Jun 2023", **{k: fy23[k]-m9_23[k] for k in fy23})
d["Q1FY24"] = dict(cal="Jul-Sep 2023", rev=2396956, cor=946891, rd=311214, sga=239645, imp=0)
d["Q2FY24"] = dict(cal="Oct-Dec 2023", rev=2486726, cor=976746, rd=320418, sga=237244, imp=219000)
d["Q3FY24"] = dict(cal="Jan-Mar 2024", rev=2359830, cor=993885, rd=321590, sga=237514, imp=70474)
fy24 = dict(rev=9812247, cor=3928073, rd=1278981, sga=969509, imp=289474); m9_24 = dict(rev=7243512, cor=2917522, rd=953222, sga=714403, imp=289474)
d["Q4FY24"] = dict(cal="Apr-Jun 2024", **{k: fy24[k]-m9_24[k] for k in fy24})
# Q4FY22 = FY22 annual (FY23 10-K: 9,211,883) - 9M FY22 (Q3FY23 10-Q comparative: 6,725,144)
print(f"Q4FY22 (Apr-Jun 2022) revenue {(9211883-6725144)/1000:.1f} -> confirms Q2FY23 as local peak")
# check: Q1FY23 = 6M - Q2 from Q2FY23 10-Q (6M rev 5,708,311)
assert 5708311-2983887 == 2724424
# pre-tax non-GAAP adjustments in operating lines ($K) from releases
adj = {"Q1FY23": 45056+9156+37276, "Q2FY23": 66689, "Q3FY23": 84139, "Q4FY23": 72699,
       "Q1FY24": 63244, "Q2FY24": 279577, "Q3FY24": 131089, "Q4FY24": 76498}
print("CY2022-23: quarter|cal|rev $M|QoQ|GAAP OI $M|GAAP OM|GAAP OM ex-impairment|non-GAAP OM")
for q,v in d.items():
    oi = v["rev"]-v["cor"]-v["rd"]-v["sga"]-v["imp"]
    v["om"] = oi/v["rev"]*100; v["om_x"] = (oi+v["imp"])/v["rev"]*100; v["om_ng"] = (oi+adj[q])/v["rev"]*100
    print(f"{q}|{v['cal']}|{v['rev']/1000:.1f}|{oi/1000:.1f}|{v['om']:.1f}%|{v['om_x']:.1f}%|{v['om_ng']:.1f}%")
pk = "Q2FY23"; tr = min(d, key=lambda q: d[q]["rev"])
print(f"Revenue peak {pk} {d[pk]['rev']/1000:.1f} -> trough {tr} {d[tr]['rev']/1000:.1f}: {pct(d[tr]['rev'],d[pk]['rev']):.1f}%")
for key,lab in [("om","GAAP OM"),("om_x","GAAP OM ex-impairment"),("om_ng","non-GAAP OM")]:
    t = min(d, key=lambda q: d[q][key])
    print(f"{lab}: peak {pk} {d[pk][key]:.1f}% -> low {t} {d[t][key]:.1f}% = {d[t][key]-d[pk][key]:+.1f} pts")
# peak OM may not be at revenue peak
for key in ["om","om_ng"]:
    p = max(d, key=lambda q: d[q][key]); print(f"  max {key} in window: {p} {d[p][key]:.1f}%")
print("Quarters below Q2FY23 revenue peak until Q2FY25 (3,076.9 > 2,983.9): Q3FY23..Q1FY25 = 7 quarters")
# ---------- earlier reported-revenue history ($K) ----------
H = [("Q1FY08","Jul-Sep 2007",693020,177278),("Q2FY08","Oct-Dec 2007",635783,93487),("Q3FY08","Jan-Mar 2008",602219,125200),
     ("Q4FY08","Apr-Jun 2008",590694,103411),("Q1FY09","Jul-Sep 2008",532513,34938),("Q2FY09","Oct-Dec 2008",396589,-505631),
     ("Q3FY09","Jan-Mar 2009",309612,-72281),("Q4FY09","Apr-Jun 2009",281502,-34967),
     ("Q1FY12","Jul-Sep 2011",796476,254289),("Q2FY12","Oct-Dec 2011",642482,159463),("Q3FY12","Jan-Mar 2012",840521,284274),
     ("Q4FY12","Apr-Jun 2012",892465,318299),("Q1FY13","Jul-Sep 2012",720709,186557),("Q2FY13","Oct-Dec 2012",673011,153247),
     ("Q3FY13","Jan-Mar 2013",729029,202246),("Q4FY13","Apr-Jun 2013",720032,187635),
     ("Q1FY14","Jul-Sep 2013",658337,None),("Q2FY14","Oct-Dec 2013",705129,None),("Q3FY14","Jan-Mar 2014",831599,261163),("Q4FY14","Apr-Jun 2014",734343,None),
     ("Q1FY15","Jul-Sep 2014",642901,109153),("Q2FY15","Oct-Dec 2014",676357,154714),("Q3FY15","Jan-Mar 2015",738459,194986),
     ("Q4FY15","Apr-Jun 2015",756332,202487),("Q1FY16","Jul-Sep 2015",642644,160794),("Q2FY16","Oct-Dec 2015",710245,214461),
     ("Q3FY16","Jan-Mar 2016",712433,712433-274599-115589-87407),("Q4FY16","Apr-Jun 2016",919171,None),
     ("Q1FY18","Jul-Sep 2017",969581,None),("Q2FY18","Oct-Dec 2017",975822,None),("Q3FY18","Jan-Mar 2018",1021294,None),("Q4FY18","Apr-Jun 2018",1070004,None),
     ("Q1FY19","Jul-Sep 2018",1093260,None),("Q2FY19","Oct-Dec 2018",1119898,None),("Q3FY19","Jan-Mar 2019",1097311,None),("Q4FY19","Apr-Jun 2019",1258435,None),
     ("Q1FY20","Jul-Sep 2019",1413414,None),("Q2FY20","Oct-Dec 2019",1509453,None),("Q3FY20","Jan-Mar 2020",1423964,None),("Q4FY20","Apr-Jun 2020",1459593,None)]
h = {q:(c,r,o) for q,c,r,o in H}
def dd(p,t,label):
    c1,r1,o1 = h[p]; c2,r2,o2 = h[t]
    s = f"{label}: {p} ({c1}) {r1/1000:.1f} -> {t} ({c2}) {r2/1000:.1f}: revenue {pct(r2,r1):.1f}%"
    if o1 is not None and o2 is not None:
        s += f"; GAAP OM {o1/r1*100:.1f}% -> {o2/r2*100:.1f}% ({(o2/r2-o1/r1)*100:+.1f} pts)"
    print(s)
print()
dd("Q1FY08","Q4FY09","2008-09")
c,r,o = h["Q2FY09"]; print(f"   Q2FY09 GAAP OM {o/r*100:.1f}% (includes impairment; not separated in Note 21)")
dd("Q4FY12","Q2FY13","2012")
dd("Q3FY14","Q1FY15","2014")
dd("Q4FY15","Q1FY16","2015 (sub-swing)")
dd("Q4FY12","Q1FY16","2012-15 full plateau (Jun-2012 peak to Sep-2015 low)")
dd("Q4FY12","Q1FY15","2012-15 to OM low (Sep-2014)")
dd("Q3FY14","Q1FY16","2014-15 (peak Mar-2014 to Sep-2015 low)")
dd("Q2FY19","Q3FY19","2018-19 reported")
orb = 161344
print(f"2018-19 ex-Orbotech: Q3FY19 {(1097311-orb)/1000:.1f} vs Q2FY19 {1119898/1000:.1f}: {pct(1097311-orb,1119898):.1f}% (Orbotech Q3FY19 revenue $161.3M, from 2019-02-20)")
dd("Q2FY20","Q3FY20","2020 COVID")
# peak regained
print("Mar-2014 peak 831.6 first exceeded Q4FY16 (919.2) = 9 quarters below peak")
print("Jun-2012 peak 892.5 first exceeded Q4FY16 (919.2); Jun-2015 peak 756.3 first exceeded Q4FY16")
# Management-named one-offs, 2015: restructuring $22.4M in Q4FY15 (FY15 10-K MD&A), $7.1M in Q1FY16 (Q1FY16 10-Q MD&A)
for q,rs in [("Q4FY15",22400),("Q1FY16",7100)]:
    c,r,o = h[q]; print(f"{q} GAAP OM {o/r*100:.1f}% ; ex-restructuring {(o+rs)/r*100:.1f}%")
