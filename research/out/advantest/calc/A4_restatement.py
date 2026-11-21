#!/usr/bin/env python3
"""A4 - restatement check: prior-period figures as first reported vs as comparatives in later documents.
Advantest, fiscal year ends 31 March. Inputs hard-coded from research/out/advantest/parts/A4.csv (evidence id per comment).
Also: segment reclassification (three old segments -> two new segments from FY2025): amounts moved between segments.
"""

# (label, first-reported value, later value)
REGION_PAIRS = [
    ('FY2024 Q3 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 3.4, 3.4),  # A4-139, A4-075
    ('FY2024 Q3 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 54.9, 54.9),  # A4-140, A4-076
    ('FY2024 Q3 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 78.8, 78.8),  # A4-141, A4-077
    ('FY2024 Q3 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 51.8, 51.8),  # A4-142, A4-078
    ('FY2024 Q3 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 12.6, 12.6),  # A4-143, A4-079
    ('FY2024 Q3 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 5.0, 5.0),  # A4-144, A4-080
    ('FY2024 Q3 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 11.7, 11.7),  # A4-145, A4-081
    ('FY2024 Q3 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 218.2, 218.2),  # A4-146, A4-082
    ('FY2024 Q4 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 2.5, 2.5),  # A4-147, A4-083
    ('FY2024 Q4 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 23.7, 23.7),  # A4-148, A4-084
    ('FY2024 Q4 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 133.1, 133.1),  # A4-149, A4-085
    ('FY2024 Q4 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 44.6, 44.6),  # A4-150, A4-086
    ('FY2024 Q4 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 13.0, 13.0),  # A4-151, A4-087
    ('FY2024 Q4 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 5.7, 5.7),  # A4-152, A4-088
    ('FY2024 Q4 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 9.7, 9.7),  # A4-153, A4-089
    ('FY2024 Q4 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 232.3, 232.3),  # A4-154, A4-090
    ('FY2025 Q1 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 3.8, 3.8),  # A4-155, A4-091
    ('FY2025 Q1 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 32.7, 32.7),  # A4-156, A4-092
    ('FY2025 Q1 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 162.1, 162.1),  # A4-157, A4-093
    ('FY2025 Q1 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 39.0, 39.0),  # A4-158, A4-094
    ('FY2025 Q1 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 9.6, 9.6),  # A4-159, A4-095
    ('FY2025 Q1 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 4.4, 4.4),  # A4-160, A4-096
    ('FY2025 Q1 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 12.2, 12.2),  # A4-161, A4-097
    ('FY2025 Q1 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 263.8, 263.8),  # A4-162, A4-098
    ('FY2025 Q2 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 5.2, 5.2),  # A4-163, A4-099
    ('FY2025 Q2 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 56.1, 56.1),  # A4-164, A4-100
    ('FY2025 Q2 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 115.4, 115.4),  # A4-165, A4-101
    ('FY2025 Q2 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 52.1, 52.1),  # A4-166, A4-102
    ('FY2025 Q2 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 11.3, 11.3),  # A4-167, A4-103
    ('FY2025 Q2 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 6.1, 6.1),  # A4-168, A4-104
    ('FY2025 Q2 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 16.7, 16.7),  # A4-169, A4-105
    ('FY2025 Q2 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 262.9, 262.9),  # A4-170, A4-106
    ('FY2025 Q3 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 8.5, 8.5),  # A4-171, A4-107
    ('FY2025 Q3 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 57.0, 57.0),  # A4-172, A4-108
    ('FY2025 Q3 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 103.2, 103.2),  # A4-173, A4-109
    ('FY2025 Q3 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 65.4, 65.4),  # A4-174, A4-110
    ('FY2025 Q3 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 12.0, 12.0),  # A4-175, A4-111
    ('FY2025 Q3 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 5.9, 5.9),  # A4-176, A4-112
    ('FY2025 Q3 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 21.8, 21.8),  # A4-177, A4-113
    ('FY2025 Q3 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 273.8, 273.8),  # A4-178, A4-114
    ('FY2025 Q4 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 7.6, 7.6),  # A4-179, A4-115
    ('FY2025 Q4 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 34.5, 34.5),  # A4-180, A4-116
    ('FY2025 Q4 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 188.8, 188.8),  # A4-181, A4-117
    ('FY2025 Q4 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 56.8, 56.8),  # A4-182, A4-118
    ('FY2025 Q4 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 11.6, 11.6),  # A4-183, A4-119
    ('FY2025 Q4 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 6.7, 6.7),  # A4-184, A4-120
    ('FY2025 Q4 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 22.1, 22.1),  # A4-185, A4-121
    ('FY2025 Q4 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 328.1, 328.1),  # A4-186, A4-122
    ('FY2026 Q1 Japan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 3.3, 3.3),  # A4-187, A4-123
    ('FY2026 Q1 S. Korea ship-to, first deck vs Q2 FY26 deck (JPY bn)', 67.4, 67.4),  # A4-188, A4-124
    ('FY2026 Q1 Taiwan ship-to, first deck vs Q2 FY26 deck (JPY bn)', 178.6, 178.6),  # A4-189, A4-125
    ('FY2026 Q1 China ship-to, first deck vs Q2 FY26 deck (JPY bn)', 69.4, 69.4),  # A4-190, A4-126
    ('FY2026 Q1 Americas ship-to, first deck vs Q2 FY26 deck (JPY bn)', 13.2, 13.2),  # A4-191, A4-127
    ('FY2026 Q1 Europe ship-to, first deck vs Q2 FY26 deck (JPY bn)', 6.1, 6.1),  # A4-192, A4-128
    ('FY2026 Q1 Others ship-to, first deck vs Q2 FY26 deck (JPY bn)', 29.5, 29.5),  # A4-193, A4-129
    ('FY2026 Q1 Total ship-to, first deck vs Q2 FY26 deck (JPY bn)', 367.5, 367.5),  # A4-194, A4-130
    ('FY2024 Q3 Japan ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 3.4, 3.4),  # A4-139, A4-195
    ('FY2024 Q3 S. Korea ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 54.9, 54.9),  # A4-140, A4-196
    ('FY2024 Q3 Taiwan ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 78.8, 78.8),  # A4-141, A4-197
    ('FY2024 Q3 China ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 51.8, 51.8),  # A4-142, A4-198
    ('FY2024 Q3 Americas ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 12.6, 12.6),  # A4-143, A4-199
    ('FY2024 Q3 Europe ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 5.0, 5.0),  # A4-144, A4-200
    ('FY2024 Q3 Others ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 11.7, 11.7),  # A4-145, A4-201
    ('FY2024 Q3 Total ship-to, FY24 3Q deck vs Q3 FY25 deck (JPY bn)', 218.2, 218.2),  # A4-146, A4-202
    ('FY2024 annual Japan ship-to, FY24 deck vs FY25 deck (JPY bn)', 15.8, 15.8),  # A4-067, A4-051
    ('FY2024 annual S. Korea ship-to, FY24 deck vs FY25 deck (JPY bn)', 157.0, 157.0),  # A4-068, A4-052
    ('FY2024 annual Taiwan ship-to, FY24 deck vs FY25 deck (JPY bn)', 326.5, 326.5),  # A4-069, A4-053
    ('FY2024 annual China ship-to, FY24 deck vs FY25 deck (JPY bn)', 175.1, 175.1),  # A4-070, A4-054
    ('FY2024 annual Americas ship-to, FY24 deck vs FY25 deck (JPY bn)', 47.1, 47.1),  # A4-071, A4-055
    ('FY2024 annual Europe ship-to, FY24 deck vs FY25 deck (JPY bn)', 20.0, 20.0),  # A4-072, A4-056
    ('FY2024 annual Others ship-to, FY24 deck vs FY25 deck (JPY bn)', 38.2, 38.2),  # A4-073, A4-057
    ('FY2024 annual Total ship-to, FY24 deck vs FY25 deck (JPY bn)', 779.7, 779.7),  # A4-074, A4-058
    ('FY2024 Japan customer location, 83rd vs 84th annual report (JPY m)', 15849, 15849),  # A4-032, A4-016
    ('FY2024 Americas customer location, 83rd vs 84th annual report (JPY m)', 47119, 47119),  # A4-034, A4-018
    ('FY2024 Europe customer location, 83rd vs 84th annual report (JPY m)', 19962, 19962),  # A4-036, A4-020
    ('FY2024 Asia customer location, 83rd vs 84th annual report (JPY m)', 696777, 696777),  # A4-038, A4-022
    ('FY2024 Taiwan customer location, 83rd vs 84th annual report (JPY m)', 326506, 326506),  # A4-042, A4-026
    ('FY2024 China customer location, 83rd vs 84th annual report (JPY m)', 175105, 175105),  # A4-044, A4-028
    ('FY2024 S. Korea customer location, 83rd vs 84th annual report (JPY m)', 156994, 156994),  # A4-046, A4-030
    ('FY2024 Total customer location, 83rd vs 84th annual report (JPY m)', 779707, 779707),  # A4-040, A4-024
    ('FY2025 1H Japan, 84th 1H vs 85th 1H report (JPY m)', 8961, 8961),  # A4-209, A4-208
    ('FY2025 1H Americas, 84th 1H vs 85th 1H report (JPY m)', 20874, 20874),  # A4-211, A4-210
    ('FY2025 1H Europe, 84th 1H vs 85th 1H report (JPY m)', 10499, 10499),  # A4-213, A4-212
    ('FY2025 1H Asia, 84th 1H vs 85th 1H report (JPY m)', 486399, 486399),  # A4-215, A4-214
    ('FY2025 1H Total, 84th 1H vs 85th 1H report (JPY m)', 526733, 526733),  # A4-217, A4-216
    ('FY2024 1H Japan, 83rd 1H vs 84th 1H report (JPY m)', 9939, 9939),  # A4-219, A4-218
    ('FY2024 1H Americas, 83rd 1H vs 84th 1H report (JPY m)', 21482, 21482),  # A4-221, A4-220
    ('FY2024 1H Europe, 83rd 1H vs 84th 1H report (JPY m)', 9261, 9261),  # A4-223, A4-222
    ('FY2024 1H Asia, 83rd 1H vs 84th 1H report (JPY m)', 288524, 288524),  # A4-225, A4-224
    ('FY2024 1H Total, 83rd 1H vs 84th 1H report (JPY m)', 329206, 329206),  # A4-227, A4-226
]

CUSTOMER_PAIRS = [
    ('FY2024 TSMC net sales, 83rd vs 84th (JPY m)', 96158, 96158),  # A4-005, A4-003
    ('FY2024 Samsung Group net sales, 83rd vs 84th (JPY m)', 87734, 87734),  # A4-006, A4-004
    ('FY2024 top-five customer share, 83rd vs 84th (%)', 48, 48),  # A4-012, A4-009
]

SEGMENT_IDENTITY_PAIRS = [
    ('FY2025 1H TS, 84th 1H vs 85th 1H (JPY m)', 477957, 477957),  # A4-258, A4-264
    ('FY2025 1H SO, 84th 1H vs 85th 1H (JPY m)', 48776, 48776),  # A4-259, A4-265
    ('FY2025 1H TSi, 84th 1H vs 85th 1H (JPY m)', 240556, 240556),  # A4-260, A4-266
    ('FY2025 1H SOi, 84th 1H vs 85th 1H (JPY m)', 3048, 3048),  # A4-261, A4-267
    ('FY2025 1H CORPi, 84th 1H vs 85th 1H (JPY m)', -9052, -9052),  # A4-262, A4-268
    ('FY2025 1H TOTi, 84th 1H vs 85th 1H (JPY m)', 234552, 234552),  # A4-263, A4-269
    ('FY2025 Q1 TS, FY25 Q1 vs FY26 Q1 results (JPY m)', 240554, 240554),  # A4-291, A4-294
    ('FY2025 Q1 SO, FY25 Q1 vs FY26 Q1 results (JPY m)', 23222, 23222),  # A4-292, A4-295
    ('FY2025 Q1 TOT, FY25 Q1 vs FY26 Q1 results (JPY m)', 263776, 263776),  # A4-293, A4-296
]

# --- segment tables: old basis (Semiconductor & Component Test System 'SCT', Mechatronics 'MECH', Services/Support/Others 'SSO')
#     vs new basis (Test System 'TS', Services and Others 'SO'); JPY million
FY2024 = dict(
    SCT=598128, MECH=73180, SSO=108399,  # A4-228, A4-229, A4-230
    TS=682819, SO=96888,  # A4-236, A4-237
    SCTi=244021, MECHi=16786, SSOi=-10914, CORPi_old=-18839, TOTi_old=231054,  # A4-231, A4-232, A4-233, A4-234, A4-235
    TSi=262120, SOi=-16125, CORPi_new=-14941, TOTi_new=231054,  # A4-238, A4-239, A4-240, A4-241
)
H1_FY2024 = dict(
    SCT=246578, MECH=31506, SSO=51122,  # A4-243, A4-244, A4-245
    TS=284575, SO=44631,  # A4-251, A4-252
    SCTi=94723, MECHi=6265, SSOi=4106, CORPi_old=-8976, TOTi_old=96118,  # A4-246, A4-247, A4-248, A4-249, A4-250
    TSi=102308, SOi=604, CORPi_new=-6794, TOTi_new=96118,  # A4-253, A4-254, A4-255, A4-256
)
M9_FY2024 = dict(
    SCT=414185, MECH=55069, SSO=78104,  # A4-270, A4-271, A4-272
    TS=478659, SO=68699,  # A4-278, A4-279
    SCTi=160748, MECHi=13310, SSOi=5734, CORPi_old=-13664, TOTi_old=166128,  # A4-273, A4-274, A4-275, A4-276, A4-277
    TSi=176012, SOi=465, CORPi_new=-10349, TOTi_new=166128,  # A4-280, A4-281, A4-282, A4-283
)
Q1_FY2024 = dict(
    SCT=101108, MECH=14261, SSO=23356,  # A4-284, A4-285, A4-286
    TS=117286, SO=21439,  # A4-288, A4-289
    TOT_old=138725, TOT_new=138725,  # A4-287, A4-290
)


changed = 0
print("== Same prior-period figure in two documents ==")
for lab, a, b in REGION_PAIRS + CUSTOMER_PAIRS + SEGMENT_IDENTITY_PAIRS:
    flag = "SAME" if a == b else "CHANGED"
    changed += a != b
    print(f"{flag:8s} {lab}: {a} -> {b}")
n = len(REGION_PAIRS) + len(CUSTOMER_PAIRS) + len(SEGMENT_IDENTITY_PAIRS)
print(f"RESULT pairs_compared = {n}")
print(f"RESULT pairs_changed = {changed}")

print()
print("== Segment reclassification (explained by the company as a change of reportable segments) ==")
for name, d in [("FY2024", FY2024), ("FY2024 1H", H1_FY2024), ("FY2024 9M", M9_FY2024), ("FY2024 Q1", Q1_FY2024)]:
    old_test = d["SCT"] + d["MECH"]
    moved_sales = d["TS"] - old_test           # moved from old SSO into new Test System
    tot_old = d["SCT"] + d["MECH"] + d["SSO"]; tot_new = d["TS"] + d["SO"]
    print(f"{name}: sales old SCT+MECH {old_test:,} -> new TS {d['TS']:,} (moved {moved_sales:+,}); old SSO {d['SSO']:,} -> new SO {d['SO']:,} ({d['SO'] - d['SSO']:+,}); total {tot_old:,} vs {tot_new:,}")
    key = name.replace(' ', '_')
    print(f"RESULT sales_moved_to_TS_{key} = {moved_sales}")
    print(f"RESULT sales_total_change_{key} = {tot_new - tot_old}")
    if "SCTi" in d:
        old_ti = d["SCTi"] + d["MECHi"]
        d_ts = d["TSi"] - old_ti; d_so = d["SOi"] - d["SSOi"]; d_corp = d["CORPi_new"] - d["CORPi_old"]
        print(f"   segment income: TS {d['TSi']:,} vs old SCT+MECH {old_ti:,} ({d_ts:+,}); SO {d['SOi']:,} vs old SSO {d['SSOi']:,} ({d_so:+,}); "
              f"Corporate {d['CORPi_new']:,} vs {d['CORPi_old']:,} ({d_corp:+,}); total {d['TOTi_old']:,} vs {d['TOTi_new']:,} (sum of moves {d_ts + d_so + d_corp:+,})")
        print(f"RESULT income_TS_change_{key} = {d_ts}")
        print(f"RESULT income_SO_change_{key} = {d_so}")
        print(f"RESULT income_corporate_change_{key} = {d_corp}")
        print(f"RESULT income_total_change_{key} = {d['TOTi_new'] - d['TOTi_old']}")
