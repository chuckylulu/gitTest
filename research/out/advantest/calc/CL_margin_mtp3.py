"""CL: MTP3 three-year operating margin vs revised target, with and without company-named one-offs (JPY million)."""
# CL-037 FY2024 and FY2025 actual (FY2025 tanshin p.1) [F]
S24, OI24 = 779_707, 228_161
S25, OI25 = 1_128_610, 499_120
# CL-033 FY2026 forecast [C]
S26, OI26 = 1_863_000, 967_000
# CL-038 one-offs named by the company: impairment ~21.4bn in FY2024 Q4 (add back); divestiture gain ~2.5bn in FY2025 Q1 (remove)
IMP24, GAIN25 = 21_400, 2_500
# CL-073 FY2026 1H inventory write-down reversal: amount not disclosed -> FY2026 cannot be adjusted
# CL-077 MTP3 revised targets (FY2024-FY2026 averages): OP margin 33-36%; sales 835-930bn
# CL-078 Teradyne Q3 2026 non-GAAP operating margin 31.6%; CL-025 Advantest FY26 Q2 55.9%
m = [OI24/S24, OI25/S25, OI26/S26]
m_x = [(OI24+IMP24)/S24, (OI25-GAIN25)/S25, OI26/S26]
print("Operating margin reported FY24/FY25/FY26e: " + ", ".join(f"{x*100:.1f}%" for x in m))
print("Operating margin ex named one-offs FY24/FY25/FY26e: " + ", ".join(f"{x*100:.1f}%" for x in m_x))
print(f"Simple 3-yr average, reported: {sum(m)/3*100:.1f}%; ex one-offs: {sum(m_x)/3*100:.1f}%")
agg = (OI24+OI25+OI26)/(S24+S25+S26)
agg_x = (OI24+IMP24+OI25-GAIN25+OI26)/(S24+S25+S26)
print(f"Aggregate 3-yr margin, reported: {agg*100:.1f}%; ex one-offs: {agg_x*100:.1f}%  (MTP3 target 33-36%)")
print(f"3-yr average sales: {(S24+S25+S26)/3/1000:,.1f} JPY bn (MTP3 target 835-930)")
print(f"Advantest FY26 Q2 operating margin 55.9% minus Teradyne Q3 2026 non-GAAP 31.6%: {55.9-31.6:.1f} points")
