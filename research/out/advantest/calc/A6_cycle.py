#!/usr/bin/env python3
"""A6 - Cycle: peak-to-trough decline in net sales and operating margin in Advantest's last downturns
(Advantest Corporation, TSE Prime 6857; IFRS from FY2014, U.S. GAAP before; JPY). Fiscal year ends 31 March and is
named by its start year (FY2025 = Apr 2025-Mar 2026).

What it does
  1. Builds single-quarter net sales and operating income FY2015 Q1 - FY2026 Q2 by differencing the cumulative (YTD)
     figures printed on page 1 of each quarterly/annual results release (tanshin). Q1 = YTD Q1.
  2. Cross-checks every derived quarter against the single-quarter figures the company itself printed (JPY bn, 1 dp) in
     the full-year releases' "Consolidated Financial Results Overview" page (FY2017-FY2025) and the FY2026 Q2 slides.
  3. Removes the one-off items management named (amounts as disclosed; sign + = gain inside OI, - = charge) to give
     margins with and without them. Items named without an amount are listed, not removed.
  4. Screens for downturns. Definition used: trailing-four-quarter (T4Q) net sales falling >= 5% below their running
     peak. Also prints the single-quarter screen (>= 10%, >= 15%) as a sensitivity.
  5. Annual (fiscal-year) peak-to-trough as a secondary view, FY2007-FY2025.
Inputs: constants below, each with the evidence id (research/out/advantest/parts/A6.csv) it comes from.
Outputs: stdout (saved as A6_cycle.out.txt), A6_quarterly_series.csv, A6_cycle_metrics.json (same folder).
Run: python3 -I research/out/advantest/calc/A6_cycle.py > research/out/advantest/calc/A6_cycle.out.txt
"""

# =====================================================================================================================
# Inputs (hard-coded; evidence id in the comment). YTD = cumulative from 1 April, JPY million.
# S_Q_BN / OI_Q_BN = single quarter as printed by the company, JPY billion. OM_* = printed margins (%).
# =====================================================================================================================
S_YTD_FY2015_Q1 = 40166  # A6-001
OI_YTD_FY2015_Q1 = 2475  # A6-002
S_YTD_FY2015_Q2 = 86347  # A6-003
OI_YTD_FY2015_Q2 = 6677  # A6-004
S_YTD_FY2015_Q3 = 116232  # A6-005
OI_YTD_FY2015_Q3 = 6458  # A6-006
S_YTD_FY2015_FY = 162111  # A6-007
OI_YTD_FY2015_FY = 12597  # A6-008
S_YTD_FY2016_Q1 = 40669  # A6-009
OI_YTD_FY2016_Q1 = 5738  # A6-010
S_YTD_FY2016_Q2 = 76195  # A6-011
OI_YTD_FY2016_Q2 = 8318  # A6-012
S_YTD_FY2016_Q3 = 107571  # A6-013
OI_YTD_FY2016_Q3 = 9291  # A6-014
S_YTD_FY2016_FY = 155916  # A6-015
OI_YTD_FY2016_FY = 13905  # A6-016
S_YTD_FY2017_Q1 = 40697  # A6-017
OI_YTD_FY2017_Q1 = 2226  # A6-018
S_YTD_FY2017_Q2 = 88412  # A6-019
OI_YTD_FY2017_Q2 = 7412  # A6-020
S_YTD_FY2017_Q3 = 139288  # A6-021
OI_YTD_FY2017_Q3 = 10645  # A6-022
S_YTD_FY2017_FY = 207223  # A6-023
OI_YTD_FY2017_FY = 24487  # A6-024
S_YTD_FY2018_Q1 = 70931  # A6-025
OI_YTD_FY2018_Q1 = 15818  # A6-026
S_YTD_FY2018_Q2 = 143577  # A6-027
OI_YTD_FY2018_Q2 = 33763  # A6-028
S_YTD_FY2018_Q3 = 218497  # A6-029
OI_YTD_FY2018_Q3 = 54466  # A6-030
S_YTD_FY2018_FY = 282456  # A6-031
OI_YTD_FY2018_FY = 64662  # A6-032
S_YTD_FY2019_Q1 = 66165  # A6-033
OI_YTD_FY2019_Q1 = 15160  # A6-034
S_YTD_FY2019_Q2 = 137751  # A6-035
OI_YTD_FY2019_Q2 = 32878  # A6-036
S_YTD_FY2019_Q3 = 207668  # A6-037
OI_YTD_FY2019_Q3 = 47131  # A6-038
S_YTD_FY2019_FY = 275894  # A6-039
OI_YTD_FY2019_FY = 58708  # A6-040
S_YTD_FY2020_Q1 = 66725  # A6-041
OI_YTD_FY2020_Q1 = 13458  # A6-042
S_YTD_FY2020_Q2 = 144102  # A6-043
OI_YTD_FY2020_Q2 = 30937  # A6-044
S_YTD_FY2020_Q3 = 222174  # A6-045
OI_YTD_FY2020_Q3 = 46178  # A6-046
S_YTD_FY2020_FY = 312789  # A6-047
OI_YTD_FY2020_FY = 70726  # A6-048
S_YTD_FY2021_Q1 = 97116  # A6-049
OI_YTD_FY2021_Q1 = 26125  # A6-050
S_YTD_FY2021_Q2 = 187990  # A6-051
OI_YTD_FY2021_Q2 = 47476  # A6-052
S_YTD_FY2021_Q3 = 300067  # A6-053
OI_YTD_FY2021_Q3 = 81042  # A6-054
S_YTD_FY2021_FY = 416901  # A6-055
OI_YTD_FY2021_FY = 114734  # A6-056
S_YTD_FY2022_Q1 = 135943  # A6-057
OI_YTD_FY2022_Q1 = 44783  # A6-058
S_YTD_FY2022_Q2 = 274806  # A6-059
OI_YTD_FY2022_Q2 = 87916  # A6-060
S_YTD_FY2022_Q3 = 412799  # A6-061
OI_YTD_FY2022_Q3 = 129140  # A6-062
S_YTD_FY2022_FY = 560191  # A6-063
OI_YTD_FY2022_FY = 167687  # A6-064
S_YTD_FY2023_Q1 = 101251  # A6-065
OI_YTD_FY2023_Q1 = 14269  # A6-066
S_YTD_FY2023_Q2 = 217511  # A6-067
OI_YTD_FY2023_Q2 = 35269  # A6-068
S_YTD_FY2023_Q3 = 350744  # A6-069
OI_YTD_FY2023_Q3 = 62099  # A6-070
S_YTD_FY2023_FY = 486507  # A6-071
OI_YTD_FY2023_FY = 81628  # A6-072
S_YTD_FY2024_Q1 = 138725  # A6-073
OI_YTD_FY2024_Q1 = 31325  # A6-074
S_YTD_FY2024_Q2 = 329206  # A6-075
OI_YTD_FY2024_Q2 = 94859  # A6-076
S_YTD_FY2024_Q3 = 547358  # A6-077
OI_YTD_FY2024_Q3 = 164126  # A6-078
S_YTD_FY2024_FY = 779707  # A6-079
OI_YTD_FY2024_FY = 228161  # A6-080
S_YTD_FY2025_Q1 = 263776  # A6-081
OI_YTD_FY2025_Q1 = 123952  # A6-082
S_YTD_FY2025_Q2 = 526733  # A6-083
OI_YTD_FY2025_Q2 = 232435  # A6-084
S_YTD_FY2025_Q3 = 800537  # A6-085
OI_YTD_FY2025_Q3 = 346006  # A6-086
S_YTD_FY2025_FY = 1128610  # A6-087
OI_YTD_FY2025_FY = 499120  # A6-088
S_YTD_FY2026_Q1 = 367473  # A6-089
OI_YTD_FY2026_Q1 = 189990  # A6-090
S_YTD_FY2026_Q2 = 845200  # A6-091
OI_YTD_FY2026_Q2 = 456809  # A6-092
S_Q_BN_FY2017_Q1 = 40.7  # A6-093
OI_Q_BN_FY2017_Q1 = 2.2  # A6-094
S_Q_BN_FY2017_Q2 = 47.7  # A6-095
OI_Q_BN_FY2017_Q2 = 5.2  # A6-096
S_Q_BN_FY2017_Q3 = 50.9  # A6-097
OI_Q_BN_FY2017_Q3 = 3.2  # A6-098
S_Q_BN_FY2017_Q4 = 67.9  # A6-099
OI_Q_BN_FY2017_Q4 = 13.9  # A6-100
S_Q_BN_FY2018_Q1 = 70.9  # A6-101
OI_Q_BN_FY2018_Q1 = 15.8  # A6-102
S_Q_BN_FY2018_Q2 = 72.7  # A6-103
OI_Q_BN_FY2018_Q2 = 18.0  # A6-104
S_Q_BN_FY2018_Q3 = 74.9  # A6-105
OI_Q_BN_FY2018_Q3 = 20.7  # A6-106
S_Q_BN_FY2018_Q4 = 64.0  # A6-107
OI_Q_BN_FY2018_Q4 = 10.2  # A6-108
S_Q_BN_FY2019_Q1 = 66.2  # A6-109
OI_Q_BN_FY2019_Q1 = 15.2  # A6-110
S_Q_BN_FY2019_Q2 = 71.6  # A6-111
OI_Q_BN_FY2019_Q2 = 17.7  # A6-112
S_Q_BN_FY2019_Q3 = 69.9  # A6-113
OI_Q_BN_FY2019_Q3 = 14.2  # A6-114
S_Q_BN_FY2019_Q4 = 68.2  # A6-115
OI_Q_BN_FY2019_Q4 = 11.6  # A6-116
S_Q_BN_FY2020_Q1 = 66.7  # A6-117
OI_Q_BN_FY2020_Q1 = 13.5  # A6-118
S_Q_BN_FY2020_Q2 = 77.4  # A6-119
OI_Q_BN_FY2020_Q2 = 17.4  # A6-120
S_Q_BN_FY2020_Q3 = 78.1  # A6-121
OI_Q_BN_FY2020_Q3 = 15.3  # A6-122
S_Q_BN_FY2020_Q4 = 90.6  # A6-123
OI_Q_BN_FY2020_Q4 = 24.5  # A6-124
S_Q_BN_FY2021_Q1 = 97.1  # A6-125
OI_Q_BN_FY2021_Q1 = 26.1  # A6-126
S_Q_BN_FY2021_Q2 = 90.9  # A6-127
OI_Q_BN_FY2021_Q2 = 21.4  # A6-128
S_Q_BN_FY2021_Q3 = 112.1  # A6-129
OI_Q_BN_FY2021_Q3 = 33.5  # A6-130
S_Q_BN_FY2021_Q4 = 116.8  # A6-131
OI_Q_BN_FY2021_Q4 = 33.7  # A6-132
S_Q_BN_FY2022_Q1 = 135.9  # A6-133
OI_Q_BN_FY2022_Q1 = 44.8  # A6-134
S_Q_BN_FY2022_Q2 = 138.9  # A6-135
OI_Q_BN_FY2022_Q2 = 43.1  # A6-136
S_Q_BN_FY2022_Q3 = 138.0  # A6-137
OI_Q_BN_FY2022_Q3 = 41.2  # A6-138
S_Q_BN_FY2022_Q4 = 147.4  # A6-139
OI_Q_BN_FY2022_Q4 = 38.6  # A6-140
S_Q_BN_FY2023_Q1 = 101.3  # A6-141
OI_Q_BN_FY2023_Q1 = 14.3  # A6-142
S_Q_BN_FY2023_Q2 = 116.2  # A6-143
OI_Q_BN_FY2023_Q2 = 21.0  # A6-144
S_Q_BN_FY2023_Q3 = 133.2  # A6-145
OI_Q_BN_FY2023_Q3 = 26.8  # A6-146
S_Q_BN_FY2023_Q4 = 135.8  # A6-147
OI_Q_BN_FY2023_Q4 = 19.5  # A6-148
S_Q_BN_FY2024_Q1 = 138.7  # A6-149
OI_Q_BN_FY2024_Q1 = 31.3  # A6-150
S_Q_BN_FY2024_Q2 = 190.5  # A6-151
OI_Q_BN_FY2024_Q2 = 63.6  # A6-152
S_Q_BN_FY2024_Q3 = 218.2  # A6-153
OI_Q_BN_FY2024_Q3 = 69.2  # A6-154
S_Q_BN_FY2024_Q4 = 232.3  # A6-155
OI_Q_BN_FY2024_Q4 = 64.1  # A6-156
S_Q_BN_FY2025_Q1 = 263.8  # A6-157
OI_Q_BN_FY2025_Q1 = 124.0  # A6-158
S_Q_BN_FY2025_Q2 = 262.9  # A6-159
OI_Q_BN_FY2025_Q2 = 108.4  # A6-160
S_Q_BN_FY2025_Q3 = 273.8  # A6-161
OI_Q_BN_FY2025_Q3 = 113.6  # A6-162
S_Q_BN_FY2025_Q4 = 328.1  # A6-163
OI_Q_BN_FY2025_Q4 = 153.1  # A6-164
S_Q_BN_FY2026_Q2 = 477.7  # A6-165
OI_Q_BN_FY2026_Q2 = 266.8  # A6-166
OM_Q_PRINTED_FY2018_Q3 = 27.6  # A6-167
OM_Q_PRINTED_FY2018_Q4 = 15.9  # A6-168
OM_Q_PRINTED_FY2022_Q1 = 32.9  # A6-169
OM_Q_PRINTED_FY2022_Q4 = 26.2  # A6-170
OM_Q_PRINTED_FY2023_Q1 = 14.1  # A6-171
OM_Q_PRINTED_FY2023_Q4 = 14.4  # A6-172
S_FY_FY2007_USGAAP = 182767  # A6-173
OI_FY_FY2007_USGAAP = 22716  # A6-174
S_FY_FY2008_USGAAP = 76652  # A6-175
OI_FY_FY2008_USGAAP = -49457  # A6-176
S_FY_FY2009_USGAAP = 53225  # A6-177
OI_FY_FY2009_USGAAP = -11639  # A6-178
S_FY_FY2010_USGAAP = 99634  # A6-179
OI_FY_FY2010_USGAAP = 6111  # A6-180
S_FY_FY2011_USGAAP = 141048  # A6-181
OI_FY_FY2011_USGAAP = 837  # A6-182
S_FY_FY2012_USGAAP = 132903  # A6-183
OI_FY_FY2012_USGAAP = 80  # A6-184
S_FY_FY2013_USGAAP = 111878  # A6-185
OI_FY_FY2013_USGAAP = -36369  # A6-186
S_FY_FY2014_USGAAP = 163329  # A6-187
OI_FY_FY2014_USGAAP = 14619  # A6-188
S_FY_FY2014_IFRS = 163803  # A6-189
OI_FY_FY2014_IFRS = 16858  # A6-190
OM_FY_PRINTED_FY2007 = 12.4  # A6-191
OM_FY_PRINTED_FY2008 = -64.5  # A6-192
OM_FY_PRINTED_FY2009 = -21.9  # A6-193
OM_FY_PRINTED_FY2011 = 0.6  # A6-194
OM_FY_PRINTED_FY2013 = -32.5  # A6-195
OM_FY_IAR_FY2015 = 7.8  # A6-196
OM_FY_IAR_FY2016 = 8.9  # A6-197
OM_FY_IAR_FY2017 = 11.8  # A6-198
OM_FY_IAR_FY2018 = 22.9  # A6-199
OM_FY_IAR_FY2019 = 21.3  # A6-200
OM_FY_IAR_FY2020 = 22.6  # A6-201
OM_FY_IAR_FY2021 = 27.5  # A6-202
OM_FY_IAR_FY2022 = 29.9  # A6-203
OM_FY_IAR_FY2023 = 16.8  # A6-204
OM_FY_IAR_FY2024 = 29.3  # A6-205
OM_FY_IAR_FY2025 = 44.2  # A6-206
ONEOFF_FY2017_Q3_INV_WRITEDOWN_BN = 3.3  # A6-207
ONEOFF_FY2018_Q3_PENSION_BN = 2.5  # A6-208
ONEOFF_FY2018_TOTAL_BN = 3.5  # A6-209
OTHER_INC_BN_FY2018_Q1 = 0.1  # A6-210
OTHER_INC_BN_FY2018_Q2 = 1.0  # A6-211
OTHER_INC_BN_FY2018_Q3 = 2.7  # A6-212
OTHER_INC_BN_FY2018_Q4 = 0.0  # A6-213
ONEOFF_FY2018_1H_FIXEDASSET_BN = 1.0  # A6-214
ONEOFF_FY2020_Q2_PROBECARD_M = 2451  # A6-217
ONEOFF_FY2020_DE_PENSION_M = 5569  # A6-218
ONEOFF_FY2022_Q4_INV_BN = 3  # A6-219
ONEOFF_FY2023_1H_SETTLEMENT_M = 3179  # A6-220
ONEOFF_FY2023_Q4_IMPAIRMENT_M = 8998  # A6-221
ONEOFF_FY2024_Q4_IMPAIRMENT_M = 21393  # A6-223
ONEOFF_FY2025_Q1_DIVEST_M = 2504  # A6-225
OTHER_NET_BN_FY2020_Q1 = 0.0  # A6-226
OTHER_NET_BN_FY2020_Q2 = 2.6  # A6-227
OTHER_NET_BN_FY2020_Q3 = 0.0  # A6-228
OTHER_NET_BN_FY2020_Q4 = 5.7  # A6-229
OTHER_NET_BN_FY2023_Q1 = 0.2  # A6-230
OTHER_NET_BN_FY2023_Q2 = 3.2  # A6-231
OTHER_NET_BN_FY2023_Q3 = 0.1  # A6-232
OTHER_NET_BN_FY2023_Q4 = -8.9  # A6-233
ONEOFF_FY2008_INV_BN = 8.7  # A6-234
ONEOFF_FY2008_RESTR_BN = 5.1  # A6-235
ONEOFF_FY2008_IMP_BN = 13.8  # A6-236
ONEOFF_FY2013_INV_BN = 4.0  # A6-237
ONEOFF_FY2013_IMP_BN = 13.5  # A6-237
SOC_MKT_CY2015 = 1650  # A6-252
SOC_MKT_CY2016 = 2000  # A6-253
SOC_MKT_CY2018 = 2550  # A6-254
SOC_MKT_CY2019 = 2700  # A6-255
SOC_MKT_CY2022 = 4000  # A6-256
SOC_MKT_CY2023 = 3300  # A6-257
MEM_MKT_CY2015 = 470  # A6-258
MEM_MKT_CY2016 = 470  # A6-259
MEM_MKT_CY2018 = 1150  # A6-260
MEM_MKT_CY2019 = 650  # A6-261
MEM_MKT_CY2022 = 1200  # A6-262
MEM_MKT_CY2023 = 1100  # A6-263
WSTS_CY2015 = 335  # A6-264
WSTS_CY2016 = 339  # A6-265
WSTS_CY2018 = 469  # A6-266
WSTS_CY2019 = 412  # A6-267
WSTS_CY2022 = 574  # A6-268
WSTS_CY2023 = 527  # A6-269

# =====================================================================================================================
# Computation (everything below uses only the constants above)
# =====================================================================================================================
import csv, json, os

HERE = os.path.dirname(os.path.abspath(__file__))
G = globals()

QS = ["Q1", "Q2", "Q3", "Q4"]
CALM = {"Q1": "Apr-Jun", "Q2": "Jul-Sep", "Q3": "Oct-Dec", "Q4": "Jan-Mar"}
QEND = {"Q1": "06-30", "Q2": "09-30", "Q3": "12-31", "Q4": "03-31"}


def cal(fy, q):
    y = int(fy[2:])
    return f"{CALM[q]} {y + 1 if q == 'Q4' else y}"


def qend(fy, q):
    y = int(fy[2:])
    return f"{y + 1 if q == 'Q4' else y}-{QEND[q]}"


def pct(a, b):
    return 100.0 * a / b


# ---------------------------------------------------------------- 1. single quarters from cumulative (YTD) figures
quarters = []
for y in range(2015, 2027):
    F = f"FY{y}"
    prev_s = prev_o = 0
    for i, q in enumerate(QS):
        key = q if q != "Q4" else "FY"
        sn, on = f"S_YTD_{F}_{key}", f"OI_YTD_{F}_{key}"
        if sn not in G:
            break
        s, o = G[sn] - prev_s, G[on] - prev_o
        quarters.append(dict(fq=f"{F} {q}", fy=F, q=q, cal=cal(F, q), end=qend(F, q), sales=s, oi=o,
                             method="Q1 = YTD Q1" if q == "Q1" else f"YTD {key} minus YTD {QS[i - 1] if QS[i - 1] != 'Q4' else 'FY'}"))
        prev_s, prev_o = G[sn], G[on]
idx = {r["fq"]: i for i, r in enumerate(quarters)}

# ---------------------------------------------------------------- 2. one-off items named by management (sign: + = gain inside reported OI, - = charge)
ONEOFFS = {
    "FY2017 Q3": [(-ONEOFF_FY2017_Q3_INV_WRITEDOWN_BN * 1000, "inventory write-down, nanotechnology (~3.3 bn)")],
    "FY2018 Q2": [(+ONEOFF_FY2018_1H_FIXEDASSET_BN * 1000, "gain on sale of fixed assets (~1.0 bn; named for 1H, placed in Q2 by quarterly other income Q1 0.1 / Q2 1.0 bn)")],
    "FY2018 Q3": [(+ONEOFF_FY2018_Q3_PENSION_BN * 1000, "pension transfer to defined contribution (~2.5 bn)")],
    "FY2020 Q2": [(+ONEOFF_FY2020_Q2_PROBECARD_M, "gain on transfer of probe card business (30 Jul 2020)")],
    "FY2020 Q4": [(+ONEOFF_FY2020_DE_PENSION_M, "pension plan transfer, Advantest Europe GmbH (named for FY; placed in Q4 by quarterly other income-expenses Q2 2.6 / Q4 5.7 bn)")],
    "FY2022 Q4": [(-ONEOFF_FY2022_Q4_INV_BN * 1000, "inventory valuation losses (~3 bn, Q&A)")],
    "FY2023 Q2": [(+ONEOFF_FY2023_1H_SETTLEMENT_M, "settlement income (named for 1H; placed in Q2 by quarterly other income-expenses Q1 0.2 / Q2 3.2 bn)")],
    "FY2023 Q4": [(-ONEOFF_FY2023_Q4_IMPAIRMENT_M, "goodwill impairment, Essai (SLT)")],
    "FY2024 Q4": [(-ONEOFF_FY2024_Q4_IMPAIRMENT_M, "goodwill and intangibles impairment, Essai (SLT)")],
    "FY2025 Q1": [(+ONEOFF_FY2025_Q1_DIVEST_M, "gain on partial divestiture of a business")],
}
UNQUANTIFIED = {
    "FY2019 Q3": "one-time amortisation expense on transferred SLT business (amount not disclosed)",
    "FY2025 Q4": "one-off SG&A expenses named by management, amount not disclosed (A1-311)",
    "FY2026 Q1": "reversal of inventory write-down named by management, amount not disclosed (A1-315)",
    "FY2026 Q2": "1H reversal of inventory write-down named by management, amount not disclosed (A1-316)",
}
# placement checks for the items named for a half or a full year
assert OTHER_INC_BN_FY2018_Q2 >= ONEOFF_FY2018_1H_FIXEDASSET_BN - 0.05 and OTHER_INC_BN_FY2018_Q1 < 0.5
assert OTHER_NET_BN_FY2020_Q4 >= ONEOFF_FY2020_DE_PENSION_M / 1000 - 0.05 and OTHER_NET_BN_FY2020_Q3 < 0.5
assert OTHER_NET_BN_FY2023_Q2 >= ONEOFF_FY2023_1H_SETTLEMENT_M / 1000 - 0.05 and OTHER_NET_BN_FY2023_Q1 < 0.5
# FY2018: 3.5 bn total one-off profit = 2.5 bn pension (Q3) + 1.0 bn fixed-asset gain (1H)
assert abs(ONEOFF_FY2018_TOTAL_BN - ONEOFF_FY2018_Q3_PENSION_BN - ONEOFF_FY2018_1H_FIXEDASSET_BN) < 1e-9

for r in quarters:
    items = ONEOFFS.get(r["fq"], [])
    r["oneoff"] = int(round(sum(a for a, _ in items)))
    r["oneoff_note"] = "; ".join(n for _, n in items)
    if r["fq"] in UNQUANTIFIED:
        r["oneoff_note"] = (r["oneoff_note"] + "; " if r["oneoff_note"] else "") + UNQUANTIFIED[r["fq"]]
    r["oi_ex"] = r["oi"] - r["oneoff"]
    r["om"] = pct(r["oi"], r["sales"])
    r["om_ex"] = pct(r["oi_ex"], r["sales"])

# ---------------------------------------------------------------- 3. cross-check against single-quarter figures the company printed (JPY bn, 1 dp)
mism = []
for r in quarters:
    ks, ko = f"S_Q_BN_{r['fy']}_{r['q']}", f"OI_Q_BN_{r['fy']}_{r['q']}"
    r["printed_s"] = G.get(ks)
    r["printed_oi"] = G.get(ko)
    if r["printed_s"] is not None:
        ds, do = abs(r["sales"] / 1000 - r["printed_s"]), abs(r["oi"] / 1000 - r["printed_oi"])
        # the company derives its printed quarters from rounded JPY bn cumulative figures, so two roundings: tolerance 0.1 bn
        r["check"] = (f"OK (diff sales {ds:.2f}, OI {do:.2f} bn)") if ds <= 0.1001 and do <= 0.1001 else f"MISMATCH sales {ds:.2f} OI {do:.2f}"
        if not r["check"].startswith("OK"):
            mism.append((r["fq"], r["check"]))
    else:
        r["check"] = "Q1 = YTD Q1 (no differencing)" if r["q"] == "Q1" else "no company-printed single quarter in the files read"

# ---------------------------------------------------------------- 4. trailing four quarters (T4Q)
for i, r in enumerate(quarters):
    if i >= 3:
        w = quarters[i - 3:i + 1]
        r["t4q_s"] = sum(x["sales"] for x in w)
        r["t4q_oi"] = sum(x["oi"] for x in w)
        r["t4q_oi_ex"] = sum(x["oi_ex"] for x in w)
        r["t4q_om"] = pct(r["t4q_oi"], r["t4q_s"])
        r["t4q_om_ex"] = pct(r["t4q_oi_ex"], r["t4q_s"])
    else:
        r["t4q_s"] = r["t4q_oi"] = r["t4q_oi_ex"] = r["t4q_om"] = r["t4q_om_ex"] = None

# T4Q at each fiscal year end must equal the reported annual figure
for r in quarters:
    if r["q"] == "Q4" and r["t4q_s"] is not None:
        assert r["t4q_s"] == G[f"S_YTD_{r['fy']}_FY"] and r["t4q_oi"] == G[f"OI_YTD_{r['fy']}_FY"]


# ---------------------------------------------------------------- 5. drawdown episodes
def drawdowns(series, keyname, min_depth):
    """Running-peak drawdowns on series (list of (label, value)); an episode runs from a peak to the first value above it."""
    eps, i, n = [], 0, len(series)
    peak_i = 0
    while i < n:
        if series[i][1] >= series[peak_i][1]:
            peak_i = i
            i += 1
            continue
        # in a drawdown from peak_i
        j, trough_i = i, i
        while j < n and series[j][1] <= series[peak_i][1]:
            if series[j][1] < series[trough_i][1]:
                trough_i = j
            j += 1
        depth = pct(series[trough_i][1] - series[peak_i][1], series[peak_i][1])
        rec = j if j < n else None
        if -depth >= min_depth:
            eps.append(dict(peak=peak_i, trough=trough_i, recovery=rec, depth=depth))
        if rec is None:
            break
        peak_i, i = j, j + 1
    return eps


t4 = [(r["fq"], r["t4q_s"]) for r in quarters if r["t4q_s"] is not None]
t4_off = next(i for i, r in enumerate(quarters) if r["t4q_s"] is not None)
sq = [(r["fq"], r["sales"]) for r in quarters]

print("=" * 110)
print("A6 - Advantest cycle analysis. IFRS, JPY million unless stated. Fiscal year ends 31 March; FY named by start year.")
print("Quarter = YTD minus prior YTD from the tanshin releases; checked against company-printed single quarters (JPY bn).")
print("=" * 110)
print("\n1. Quarterly series (also saved to A6_quarterly_series.csv)")
print(f"{'quarter':10} {'months':13} {'sales':>9} {'OI':>9} {'OM%':>6} {'one-offs':>9} {'OM ex%':>7} {'T4Q sales':>10} {'T4Q OM%':>8} check")
for r in quarters:
    t4s = f"{r['t4q_s']:>10,}" if r["t4q_s"] is not None else f"{'':>10}"
    t4m = f"{r['t4q_om']:>8.1f}" if r["t4q_om"] is not None else f"{'':>8}"
    print(f"{r['fq']:10} {r['cal']:13} {r['sales']:>9,} {r['oi']:>9,} {r['om']:>6.1f} {r['oneoff']:>9,.0f} {r['om_ex']:>7.1f} {t4s} {t4m} {r['check']}")
print(f"\nCross-check mismatches vs company-printed quarters: {mism if mism else 'none'}")

print("\n2. Downturn screens (all drawdowns from a running peak)")
print("2a. T4Q net sales drawdowns of at least 1% (T4Q starts FY2015 Q4 because IFRS quarterly data start FY2015 Q1)")
t4_eps = drawdowns(t4, "t4q", 1.0)
for e in t4_eps:
    p, t = quarters[t4_off + e["peak"]], quarters[t4_off + e["trough"]]
    rc = quarters[t4_off + e["recovery"]]["fq"] if e["recovery"] is not None else "not yet"
    print(f"   T4Q peak {p['fq']} ({p['t4q_s']:,}) -> trough {t['fq']} ({t['t4q_s']:,}): {e['depth']:.1f}%; recovered above peak in {rc}")
print("2b. Single-quarter net sales drawdowns of at least 10%")
sq_eps = drawdowns(sq, "q", 10.0)
for e in sq_eps:
    p, t = quarters[e["peak"]], quarters[e["trough"]]
    rc = quarters[e["recovery"]]["fq"] if e["recovery"] is not None else "not yet"
    print(f"   quarter peak {p['fq']} ({p['sales']:,}) -> trough {t['fq']} ({t['sales']:,}): {e['depth']:.1f}%; regained in {rc}")

# Definition used: a downturn = T4Q net sales falling >= 5% below its running peak.
DEF_T4Q = 5.0
episodes = []
for e in t4_eps:
    if -e["depth"] < DEF_T4Q:
        continue
    pk_i, tr_i = t4_off + e["peak"], t4_off + e["trough"]
    rec_i = t4_off + e["recovery"] if e["recovery"] is not None else None
    win_lo = max(0, pk_i - 3)
    # single-quarter peak: highest quarter among the four quarters that make up the T4Q peak
    qp_i = max(range(win_lo, pk_i + 1), key=lambda k: quarters[k]["sales"])
    end_i = (rec_i - 1) if rec_i is not None else len(quarters) - 1
    qt_i = min(range(qp_i + 1, end_i + 1), key=lambda k: quarters[k]["sales"])
    # first quarter whose sales exceed the single-quarter peak
    qrec = next((k for k in range(qt_i, len(quarters)) if quarters[k]["sales"] > quarters[qp_i]["sales"]), None)
    # margin peak = highest quarterly margin from the window start up to the sales trough; margin trough = lowest after it
    om_max_i = max(range(win_lo, qt_i + 1), key=lambda k: quarters[k]["om"])
    om_min_i = min(range(om_max_i, end_i + 1), key=lambda k: quarters[k]["om"])
    omx_max_i = max(range(win_lo, qt_i + 1), key=lambda k: quarters[k]["om_ex"])
    omx_min_i = min(range(omx_max_i, end_i + 1), key=lambda k: quarters[k]["om_ex"])
    episodes.append(dict(t4_peak=pk_i, t4_trough=tr_i, t4_rec=rec_i, t4_depth=e["depth"], q_peak=qp_i, q_trough=qt_i, q_rec=qrec,
                         om_max=om_max_i, om_min=om_min_i, omx_max=omx_max_i, omx_min=omx_min_i, win=(win_lo, end_i)))

print(f"\n3. Downturns under the stated definition (T4Q net sales down >= {DEF_T4Q:.0f}% from its running peak)")
print("   Every T4Q drawdown of 1% or more is listed in 2a; a threshold anywhere from 1% to 5.2% selects the same three episodes.")
metrics = {"episodes": []}
for n, e in enumerate(episodes, 1):
    Q = quarters
    p, t = Q[e["q_peak"]], Q[e["q_trough"]]
    tp, tt = Q[e["t4_peak"]], Q[e["t4_trough"]]
    dur_pt = e["q_trough"] - e["q_peak"]
    dur_rec = (e["q_rec"] - e["q_peak"]) if e["q_rec"] is not None else None
    t4dur = e["t4_trough"] - e["t4_peak"]
    t4rec = (e["t4_rec"] - e["t4_peak"]) if e["t4_rec"] is not None else None
    m = dict(
        n=n, window=f"{Q[e['win'][0]]['fq']} .. {Q[e['win'][1]]['fq']}",
        q_peak=p["fq"], q_peak_cal=p["cal"], q_peak_sales=p["sales"], q_trough=t["fq"], q_trough_cal=t["cal"], q_trough_sales=t["sales"],
        q_decline_pct=round(pct(t["sales"] - p["sales"], p["sales"]), 1),
        om_at_q_peak=round(p["om"], 1), om_at_q_trough=round(t["om"], 1), om_pp_change_peak_to_trough=round(t["om"] - p["om"], 1),
        om_ex_at_q_peak=round(p["om_ex"], 1), om_ex_at_q_trough=round(t["om_ex"], 1), om_ex_pp_change=round(t["om_ex"] - p["om_ex"], 1),
        oi_q_peak=p["oi"], oi_q_trough=t["oi"], oi_decline_pct=round(pct(t["oi"] - p["oi"], p["oi"]), 1),
        oi_ex_q_peak=p["oi_ex"], oi_ex_q_trough=t["oi_ex"], oi_ex_decline_pct=round(pct(t["oi_ex"] - p["oi_ex"], p["oi_ex"]), 1),
        om_max_q=Q[e["om_max"]]["fq"], om_max=round(Q[e["om_max"]]["om"], 1), om_min_q=Q[e["om_min"]]["fq"], om_min=round(Q[e["om_min"]]["om"], 1),
        om_max_to_min_pp=round(Q[e["om_min"]]["om"] - Q[e["om_max"]]["om"], 1),
        omx_max_q=Q[e["omx_max"]]["fq"], omx_max=round(Q[e["omx_max"]]["om_ex"], 1), omx_min_q=Q[e["omx_min"]]["fq"], omx_min=round(Q[e["omx_min"]]["om_ex"], 1),
        omx_max_to_min_pp=round(Q[e["omx_min"]]["om_ex"] - Q[e["omx_max"]]["om_ex"], 1),
        quarters_peak_to_trough=dur_pt, quarters_peak_to_regain=dur_rec, regain_q=Q[e["q_rec"]]["fq"] if e["q_rec"] is not None else None,
        t4_peak=tp["fq"], t4_peak_sales=tp["t4q_s"], t4_trough=tt["fq"], t4_trough_sales=tt["t4q_s"], t4_decline_pct=round(e["t4_depth"], 1),
        t4_om_peak=round(tp["t4q_om"], 1), t4_om_trough=round(tt["t4q_om"], 1), t4_om_pp=round(tt["t4q_om"] - tp["t4q_om"], 1),
        t4_om_ex_peak=round(tp["t4q_om_ex"], 1), t4_om_ex_trough=round(tt["t4q_om_ex"], 1), t4_om_ex_pp=round(tt["t4q_om_ex"] - tp["t4q_om_ex"], 1),
        t4_quarters_peak_to_trough=t4dur, t4_quarters_to_recovery=t4rec, t4_recovery_q=Q[e["t4_rec"]]["fq"] if e["t4_rec"] is not None else None,
        censored=(e["t4_peak"] - t4_off < 4),
    )
    metrics["episodes"].append(m)
    print(f"\n  Episode {n}: window {m['window']}" + ("  [T4Q peak lies in the first year of computable IFRS T4Q data (quarters start FY2015 Q1): earlier T4Q values unknown, depth may be understated]" if m["censored"] else ""))
    print(f"   single-quarter peak {p['fq']} ({p['cal']}) sales {p['sales']:,}  -> trough {t['fq']} ({t['cal']}) sales {t['sales']:,}: {m['q_decline_pct']:+.1f}%")
    print(f"   operating income {p['oi']:,} -> {t['oi']:,}: {m['oi_decline_pct']:+.1f}%; ex named one-offs {p['oi_ex']:,} -> {t['oi_ex']:,}: {m['oi_ex_decline_pct']:+.1f}%")
    print(f"   operating margin at peak {m['om_at_q_peak']:.1f}% -> at trough {m['om_at_q_trough']:.1f}%: {m['om_pp_change_peak_to_trough']:+.1f} pp"
          f"   | ex one-offs {m['om_ex_at_q_peak']:.1f}% -> {m['om_ex_at_q_trough']:.1f}%: {m['om_ex_pp_change']:+.1f} pp")
    print(f"   highest quarterly margin up to the sales trough {m['om_max_q']} {m['om_max']:.1f}% -> lowest after it {m['om_min_q']} {m['om_min']:.1f}%: {m['om_max_to_min_pp']:+.1f} pp"
          f"   | ex one-offs {m['omx_max_q']} {m['omx_max']:.1f}% -> {m['omx_min_q']} {m['omx_min']:.1f}%: {m['omx_max_to_min_pp']:+.1f} pp")
    print(f"   duration: {dur_pt} quarter(s) peak to trough; quarterly sales regained the peak in {m['regain_q']} ({dur_rec} quarters after the peak)")
    print(f"   T4Q: peak {tp['fq']} {tp['t4q_s']:,} -> trough {tt['fq']} {tt['t4q_s']:,}: {m['t4_decline_pct']:+.1f}% over {t4dur} quarters; "
          f"T4Q margin {m['t4_om_peak']:.1f}% -> {m['t4_om_trough']:.1f}% ({m['t4_om_pp']:+.1f} pp); ex one-offs {m['t4_om_ex_peak']:.1f}% -> {m['t4_om_ex_trough']:.1f}% ({m['t4_om_ex_pp']:+.1f} pp); "
          f"T4Q back above peak in {m['t4_recovery_q']}")
    for k in range(e["win"][0], e["win"][1] + 1):
        r = Q[k]
        if r["oneoff_note"]:
            print(f"     one-offs {r['fq']}: {r['oneoff']:+,.0f} ({r['oneoff_note']}) -> OM {r['om']:.1f}% reported, {r['om_ex']:.1f}% ex")

# ---------------------------------------------------------------- 6. single-quarter screen: what a >=15% single-quarter rule would select
print("\n4. Sensitivity: a '>= 15% single-quarter decline from the running peak' rule selects")
for e in sq_eps:
    if -e["depth"] >= 15:
        p, t = quarters[e["peak"]], quarters[e["trough"]]
        print(f"   {p['fq']} ({p['cal']}) {p['sales']:,} -> {t['fq']} ({t['cal']}) {t['sales']:,}: {e['depth']:.1f}%; OM {p['om']:.1f}% -> {t['om']:.1f}% ({t['om'] - p['om']:+.1f} pp)")
        metrics.setdefault("sq15", []).append(dict(peak=p["fq"], trough=t["fq"], depth=round(e["depth"], 1), om_peak=round(p["om"], 1), om_trough=round(t["om"], 1),
                                                   om_pp=round(t["om"] - p["om"], 1), peak_sales=p["sales"], trough_sales=t["sales"]))
for e in sq_eps:
    if 10 <= -e["depth"] < 15:
        p, t = quarters[e["peak"]], quarters[e["trough"]]
        metrics.setdefault("sq10to15", []).append(dict(peak=p["fq"], trough=t["fq"], depth=round(e["depth"], 1)))
        print(f"   (10-15% band, not selected) {p['fq']} -> {t['fq']}: {e['depth']:.1f}%")

# ---------------------------------------------------------------- 7. 2015-16 dip on quarterly IFRS data (pre-dates the T4Q screen)
print("\n5. FY2015-FY2016 quarterly detail (IFRS; T4Q not computable before FY2015 Q4)")
for k in range(idx["FY2015 Q1"], idx["FY2017 Q2"] + 1):
    r = quarters[k]
    print(f"   {r['fq']} {r['cal']}: sales {r['sales']:,} OI {r['oi']:,} OM {r['om']:.1f}%")
p, t = quarters[idx["FY2015 Q2"]], quarters[idx["FY2015 Q3"]]
t2 = quarters[idx["FY2016 Q3"]]
metrics["d2015"] = dict(peak=p["fq"], peak_sales=p["sales"], trough=t["fq"], trough_sales=t["sales"], depth=round(pct(t["sales"] - p["sales"], p["sales"]), 1),
                        om_peak=round(p["om"], 1), om_trough=round(t["om"], 1), om_pp=round(t["om"] - p["om"], 1),
                        second_low=t2["fq"], second_low_sales=t2["sales"], second_low_depth=round(pct(t2["sales"] - p["sales"], p["sales"]), 1),
                        second_low_om=round(t2["om"], 1), oi_peak=p["oi"], oi_trough=t["oi"])
print(f"   peak {p['fq']} {p['sales']:,} -> {t['fq']} {t['sales']:,}: {metrics['d2015']['depth']:+.1f}%, OM {p['om']:.1f}% -> {t['om']:.1f}%; "
      f"second low {t2['fq']} {t2['sales']:,} ({metrics['d2015']['second_low_depth']:+.1f}% vs FY2015 Q2), OM {t2['om']:.1f}%")

# ---------------------------------------------------------------- 8. annual (fiscal-year) view
annual = [  # (FY, basis, sales, OI, named one-offs inside OI (+gain/-charge) in JPY million, note)
    ("FY2007", "US GAAP", S_FY_FY2007_USGAAP, OI_FY_FY2007_USGAAP, 0, ""),
    ("FY2008", "US GAAP", S_FY_FY2008_USGAAP, OI_FY_FY2008_USGAAP, -(ONEOFF_FY2008_INV_BN + ONEOFF_FY2008_RESTR_BN + ONEOFF_FY2008_IMP_BN) * 1000,
     "inventory valuation 8.7 + restructuring 5.1 + PP&E impairment 13.8 bn"),
    ("FY2009", "US GAAP", S_FY_FY2009_USGAAP, OI_FY_FY2009_USGAAP, 0, "no item named in the text read"),
    ("FY2010", "US GAAP", S_FY_FY2010_USGAAP, OI_FY_FY2010_USGAAP, 0, ""),
    ("FY2011", "US GAAP", S_FY_FY2011_USGAAP, OI_FY_FY2011_USGAAP, 0, ""),
    ("FY2012", "US GAAP", S_FY_FY2012_USGAAP, OI_FY_FY2012_USGAAP, 0, ""),
    ("FY2013", "US GAAP", S_FY_FY2013_USGAAP, OI_FY_FY2013_USGAAP, -(ONEOFF_FY2013_INV_BN + ONEOFF_FY2013_IMP_BN) * 1000, "inventory valuation 4.0 + impairment 13.5 bn (Q3)"),
    ("FY2014", "IFRS", S_FY_FY2014_IFRS, OI_FY_FY2014_IFRS, 0, "US GAAP: %s / %s" % (S_FY_FY2014_USGAAP, OI_FY_FY2014_USGAAP)),
]
for y in range(2015, 2026):
    F = f"FY{y}"
    one = sum(r["oneoff"] for r in quarters if r["fy"] == F)
    note = "; ".join(f"{r['q']}: {r['oneoff_note']}" for r in quarters if r["fy"] == F and r["oneoff_note"])
    annual.append((F, "IFRS", G[f"S_YTD_{F}_FY"], G[f"OI_YTD_{F}_FY"], one, note))

print("\n6. Annual series and fiscal-year peak-to-trough (U.S. GAAP to FY2013, IFRS from FY2014)")
for F, b, s, o, one, note in annual:
    pr = G.get(f"OM_FY_IAR_{F}", G.get(f"OM_FY_PRINTED_{F}"))
    print(f"   {F} {b:7} sales {s:>9,} OI {o:>9,} OM {pct(o, s):6.1f}% (printed {pr}) | one-offs {one:+,.0f} -> OM ex {pct(o - one, s):6.1f}%  {note}")
    if pr is not None:
        assert abs(pct(o, s) - pr) <= 0.051, (F, pct(o, s), pr)

ann_eps = []
# local fiscal-year peaks: sales above the prior FY (or first year in the series) and not below the next FY;
# trough = lowest FY after the peak and before sales exceed the peak again
pairs = []
for i in range(len(annual) - 1):
    s_prev = annual[i - 1][2] if i > 0 else None
    if (s_prev is None or annual[i][2] > s_prev) and annual[i + 1][2] < annual[i][2]:
        j, tr = i + 1, i + 1
        while j < len(annual) and annual[j][2] <= annual[i][2]:
            if annual[j][2] < annual[tr][2]:
                tr = j
            j += 1
        pairs.append((annual[i][0], annual[tr][0]))
print("   local FY peaks -> troughs found:", pairs)
for a, b in pairs:
    A = next(x for x in annual if x[0] == a)
    B = next(x for x in annual if x[0] == b)
    d = dict(peak=a, trough=b, peak_sales=A[2], trough_sales=B[2], decline=round(pct(B[2] - A[2], A[2]), 1),
             om_peak=round(pct(A[3], A[2]), 1), om_trough=round(pct(B[3], B[2]), 1), om_pp=round(pct(B[3], B[2]) - pct(A[3], A[2]), 1),
             omx_peak=round(pct(A[3] - A[4], A[2]), 1), omx_trough=round(pct(B[3] - B[4], B[2]), 1),
             omx_pp=round(pct(B[3] - B[4], B[2]) - pct(A[3] - A[4], A[2]), 1), basis=A[1] + ("" if A[1] == B[1] else "/" + B[1]))
    ann_eps.append(d)
# lowest operating margin year inside 2007-09 (FY2008) for context
f08 = next(x for x in annual if x[0] == "FY2008")
metrics["fy2008"] = dict(sales=f08[2], oi=f08[3], om=round(pct(f08[3], f08[2]), 1), om_ex=round(pct(f08[3] - f08[4], f08[2]), 1), oi_ex=int(round(f08[3] - f08[4])))
f15 = next(x for x in annual if x[0] == "FY2015")
metrics["fy2015"] = dict(om=round(pct(f15[3], f15[2]), 1))
metrics["annual"] = ann_eps
print("\n   Fiscal-year peak -> trough (each FY local peak to the lowest FY before regaining it; FY2006 not retrieved, so 2007-09 starts at FY2007):")
for d in ann_eps:
    print(f"   {d['peak']} -> {d['trough']} ({d['basis']}): sales {d['peak_sales']:,} -> {d['trough_sales']:,} {d['decline']:+.1f}%; "
          f"OM {d['om_peak']:.1f}% -> {d['om_trough']:.1f}% ({d['om_pp']:+.1f} pp); ex one-offs {d['omx_peak']:.1f}% -> {d['omx_trough']:.1f}% ({d['omx_pp']:+.1f} pp)")
print(f"   FY2008 (inside 2007-09): OM {metrics['fy2008']['om']:.1f}% reported, {metrics['fy2008']['om_ex']:.1f}% ex named items (OI ex {metrics['fy2008']['oi_ex']:,})")

# ---------------------------------------------------------------- 9. market context (company estimates / WSTS)
print("\n7. Market context from the Integrated Annual Report 2026 (company estimates; WSTS)")
for lab, k in [("Memory tester market (USD m)", "MEM_MKT"), ("SoC tester market (USD m)", "SOC_MKT"), ("WSTS semiconductor sales (USD bn)", "WSTS")]:
    for a, b in [(2015, 2016), (2018, 2019), (2022, 2023)]:
        va, vb = G[f"{k}_CY{a}"], G[f"{k}_CY{b}"]
        metrics.setdefault("market", {})[f"{k}_{a}_{b}"] = round(pct(vb - va, va), 1)
        print(f"   {lab} CY{a} {va:,} -> CY{b} {vb:,}: {pct(vb - va, va):+.1f}%")

# ---------------------------------------------------------------- 10. latest position vs. prior peak (context)
last = quarters[-1]
metrics["latest"] = dict(fq=last["fq"], sales=last["sales"], oi=last["oi"], om=round(last["om"], 1), t4q_s=last["t4q_s"], t4q_om=round(last["t4q_om"], 1))
print(f"\n8. Latest quarter {last['fq']} ({last['cal']}): sales {last['sales']:,}, OI {last['oi']:,}, OM {last['om']:.1f}%; T4Q sales {last['t4q_s']:,}, T4Q OM {last['t4q_om']:.1f}%")

# ---------------------------------------------------------------- outputs
with open(os.path.join(HERE, "A6_quarterly_series.csv"), "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["fiscal_quarter", "calendar_months", "quarter_end", "net_sales_jpy_m", "operating_income_jpy_m", "operating_margin_pct",
                "named_oneoffs_in_oi_jpy_m", "oneoff_note", "oi_ex_oneoffs_jpy_m", "operating_margin_ex_oneoffs_pct",
                "t4q_net_sales_jpy_m", "t4q_operating_income_jpy_m", "t4q_operating_margin_pct", "t4q_operating_margin_ex_oneoffs_pct",
                "company_printed_sales_jpy_bn", "company_printed_oi_jpy_bn", "check_vs_printed", "derivation"])
    for r in quarters:
        w.writerow([r["fq"], r["cal"], r["end"], r["sales"], r["oi"], f"{r['om']:.1f}", f"{r['oneoff']:.0f}", r["oneoff_note"], f"{r['oi_ex']:.0f}", f"{r['om_ex']:.1f}",
                    r["t4q_s"] if r["t4q_s"] is not None else "", r["t4q_oi"] if r["t4q_oi"] is not None else "",
                    f"{r['t4q_om']:.1f}" if r["t4q_om"] is not None else "", f"{r['t4q_om_ex']:.1f}" if r["t4q_om_ex"] is not None else "",
                    r["printed_s"] if r["printed_s"] is not None else "", r["printed_oi"] if r["printed_oi"] is not None else "", r["check"], r["method"]])
metrics["quarters"] = {r["fq"]: dict(sales=r["sales"], oi=r["oi"], om=round(r["om"], 1), om_ex=round(r["om_ex"], 1), oi_ex=r["oi_ex"],
                                     t4q_s=r["t4q_s"], t4q_om=None if r["t4q_om"] is None else round(r["t4q_om"], 1)) for r in quarters}
with open(os.path.join(HERE, "A6_cycle_metrics.json"), "w", encoding="utf-8") as fh:
    json.dump(metrics, fh, indent=1)
print("\nWrote A6_quarterly_series.csv and A6_cycle_metrics.json")
