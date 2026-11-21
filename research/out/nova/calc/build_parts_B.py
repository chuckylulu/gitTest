#!/usr/bin/env python3
"""Build out/nova/parts/B.csv: Module B rows (ledger assessments [I], catalysts, extra facts).
Usage: python3 -I research/out/nova/calc/build_parts_B.py
"""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from evrow import row, write

HERE = os.path.dirname(os.path.abspath(__file__))
T = lambda d, k: f"{d}_stockanalysis_transcript-{k}.html"
F20 = "2026-02-17_nova_20-F-FY2025.pdf"


def R(tag, claim, value, pf, pc, doc, date, f, quote, conf="", note="", unit=""):
    return row("x", tag, claim, value, unit, pf, pc, doc, date, f, quote, conf, note)


B = [
    # ---- extra facts used in Module B ----
    R("[F]", "Investor Day set for 9 Mar 2027 at Nasdaq MarketSite, New York (new strategy and model expected)", "9 Mar 2027", "FQ4 FY2026", "Nov 2026",
      "Nova press release 2 Nov 2026", "2026-11-02", "2026-11-21_nova_pr-investor-day-2027.html", "it will host an Investor Day on March 9, 2027, at the Nasdaq MarketSite in New York City"),
    R("[S]", "New Asia cleanroom expected operational by end-2026 (Q3 2026 call)", "by end-2026", "FQ4 FY2026", "Oct-Dec 2026",
      "Third-party transcript of Nova Q3 2026 call", "2026-11-05", T("2026-11-05", "Q3-2026-call"), "including the new cleanroom in Asia, which is expected to become operational by year-end", "", "company statement"),
    R("[F]", "Fremont, CA cleanroom (XPS and SIMS lines) expansion to double production bays expected in 1H 2026", "2x bays", "FY2026", "Jan-Jun 2026",
      "Nova Form 20-F FY2025, Item 4D", "2026-02-17", F20, "we expect to complete the expansion of our cleanroom in Fremont, CA, U.S., doubling the amount of production bays", "", "completion not confirmed in later documents read"),
    R("[S]", "GAA: cumulative 2024-26 revenue target of $500M 'on track' (Q3 2026 call); GAA metrology intensity ~30% above FinFET", "$500M (target)", "FY2024-FY2026", "Jan 2024-Dec 2026",
      "Third-party transcript of Nova Q3 2026 call (TradingKey)", "2026-11-05", "2026-11-05_tradingkey_transcript-Q3-2026-call.html", "We are on track with the accumulated revenue from '24 to '26 of a total of $500 million.", "", "GAA revenue NOT DISCLOSED in filings; claim untestable"),
    R("[S]", "Q4 2025 call: management expected 'double-digit' AP growth in 2026 after ~60% in 2025 (analyst read it as low double digits)", "double-digit", "FY2026 outlook", "Feb 2026",
      "Third-party transcript of Nova Q4 2025 call", "2026-02-12", T("2026-02-12", "Q4-2025-call"), "And we believe that advanced packaging will still have a double-digit growth this year.", "", "company statement"),
    R("[S]", "Q4 2025 call: per external data Nova cited, process-control spending in China declined in 2025 while Nova's China revenue grew", "qualitative", "FY2025", "Feb 2026",
      "Third-party transcript of Nova Q4 2025 call", "2026-02-12", T("2026-02-12", "Q4-2025-call"), "process control in China actually went down", "", "company statement; external source not named"),
    R("[S]", "Shorter lead times in China reduce visibility (Q4 2025 call)", "qualitative", "FY2026 outlook", "Feb 2026",
      "Third-party transcript of Nova Q4 2025 call", "2026-02-12", T("2026-02-12", "Q4-2025-call"), "We do see shorter lead times in China, which reduce visibility", "", "company statement"),
    R("[S]", "Q3 2026 call: memory growth 'supported equally' by dimensional and materials metrology", "qualitative", "FQ3 FY2026", "Jul-Sep 2026",
      "Third-party transcript of Nova Q3 2026 call (TradingKey)", "2026-11-05", "2026-11-05_tradingkey_transcript-Q3-2026-call.html", "This performance was supported equally by our dimensional and materials metrology solutions.", "", "company statement"),
    R("[F]", "20-F: Nova 'intends to increase its focus on the evolving materials engineering market'", "strategy", "FY2025", "as of Feb 2026",
      "Nova Form 20-F FY2025, Item 4B", "2026-02-17", F20, "the Company intends to increase its focus on the evolving materials engineering market", ""),
    # ---- calculations ----
    R("[I]", "China revenue in USD: FY2023 186.5M; FY2024 262.2M; FY2025 290.6M (+10.8% YoY) while share fell 39% -> 33%", "290.6M (FY2025)", "FY2023-FY2025", "Jan 2023-Dec 2025",
      "calc/china.py -> calc/china.txt", "2026-11-21", "", "", "High", "inputs: A4-001/A4-002 shares x 20-F revenue (517,922; 672,396; 880,577); shares rounded to whole %"),
    R("[I]", "2030 notes conditional-conversion price trigger: 130% x $320.16 = $416.21 for 20 of 30 trading days in a quarter (cap of capped calls $415.03)", "$416.21", "FY2025", "from Q1 2026",
      "arithmetic on A5-008, A5-009, A5-012", "2026-11-21", "", "", "High", "simple product of printed terms"),
    R("[I]", "Implied end-market product revenue (rounded call %): memory ~43.7M (FQ4 FY2025), ~63.3M, ~54.4M, ~90.4M (FQ3 FY2026); logic/foundry ~131.2M, ~122.9M, ~147.1M, ~141.4M", "see calc/segments.csv", "FQ4 FY2025-FQ3 FY2026", "Oct 2025-Sep 2026",
      "calc/segments.py -> calc/segments.csv", "2026-11-21", "", "", "Low", "inputs: A1 product revenue rows and A1-062..065 [S] percentages; +/-2.5 pts rounding swings memory dollars by ~+/-5M"),
    # ---- ledger assessments ----
    R("[I]", "Ledger 1 (OCD+ML keeps pace in HAR memory; X-ray stays a niche reference): in logic GAA the papers and IRDS support OCD as the in-line workhorse and lab CD-SAXS as reference; in HAR memory the evidence points the other way - in-line CD-SAXS is already in fabs and is used as the label source for ML-OCD", "mixed: holds for logic, not for HAR memory", "n/a", "2021-2026",
      "inputs: TH-003, TH-004, TH-007, TH-009, TH-010, TH-012, TH-020, TH-021, TH-022, TH-031, TH-036, TH-043, TH-045, XR-022, XR-026, XR-027, XR-039", "2026-11-21", "", "", "Medium", "full texts read for logic papers; memory-side SAXS evidence is mainly abstracts plus IRDS and vendor claims"),
    R("[I]", "Ledger 2 (materials grows faster than dimensional): not testable from disclosures; Nova reports one segment and gave a division range (40-50 / 30-40 / 10-20) it expects to stay 'intact' through 2027, i.e. similar growth, not outgrowth", "unsupported by company data", "FY2024-FY2027", "2024-2027",
      "inputs: A1-061, Q1-047, B 'supported equally' row, Q1-030, Q1-036, Q3-007, XR-031, XR-032", "2026-11-21", "", "", "Medium", "division revenue NOT DISCLOSED; only qualitative 'record' statements favour materials"),
    R("[I]", "Ledger 3 (AP becomes a material share): already material by company statements - ~15% (2024, [F] slide), ~20% (2025), mid-20s % of product revenue in 1H 2026 ([S]); ~20% of FY2025 product revenue is ~$141M, ~16% of total revenue", "~$141M (FY2025)", "FY2024-FQ2 FY2026", "2024-Jun 2026",
      "inputs: A1-066..A1-071, Q5-001..Q5-004; FY2025 products 705,598 (A1-040)", "2026-11-21", "", "", "Medium", "AP is not a reported segment; shares are rounded call statements and the base switched from total to product revenue (Q5-003)"),
    R("[I]", "Ledger 4 (China revenue sustainable under current rules): FY2025 China revenue grew ~11% in dollars and management guides ~25-30% long-term share; current rules bind the U.S.-made XPS/SIMS lines for Entity-List customers, while Israel-made OCD is not controlled under Israeli law; the 50% Affiliates Rule pause ends 10 Jan 2027 unless extended", "sustainable under current rules; rule-change risk dated", "FY2025-FY2027", "2025-Jan 2027",
      "inputs: A4-001, A4-011..A4-020, B China USD row, B process-control-in-China row", "2026-11-21", "", "", "Medium", "Nova does not disclose China revenue by product line or by Entity-List exposure; 'small portion' is the company's wording"),
    R("[I]", "Ledger 5 (found; Nova CEO Jun/Nov 2026): Nova is sole source in in-line XPS and will hold the position when XPS competitors arrive ~2H 2027; GlobalFoundries runs VeraFlex as POR for SiGeB, but Rigaku markets light-element XRF against XPS for dipole films and claims No.1 in film/materials metrology (Yole, competitors unnamed)", "open; first test 2H 2027", "FY2026-FY2027", "2026-2027",
      "inputs: Q3-007, Q3-009, Q1-030, XR-003, XR-028, XR-030, XR-031, XR-032, XR-033, XR-044", "2026-11-21", "", "", "Low", "no non-vendor share data for XPS vs XRF sockets; competing market definitions"),
    R("[I]", "Ledger 6 (found; Onto Apr 2026, Rigaku Nov 2026): the Onto-Rigaku CD-SAXS + OCD hybrid will take memory OCD sockets; two key customers selected the Onto/Rigaku CD-SAXS offering and Rigaku targets memory mass-production lines in 1Q 2027, but no Nova memory loss is visible yet (Nova memory product revenue at a record in FQ3 FY2026)", "open; first test 1Q 2027", "FY2026-FY2027", "Apr 2026-Mar 2027",
      "inputs: XR-019..XR-027, XR-046, XR-047, A2-023, A1-065, TH-010, TH-036", "2026-11-21", "", "", "Low", "vendor claims on both sides; customer names undisclosed"),
    R("[I]", "Documented packaging overlap between Nova and Onto is limited: Nova's 20-F names Merck and Camtek as its direct packaging rivals, while Onto describes its packaging lines as inspection and lithography", "limited overlap", "FY2025-FY2026", "2025-2026",
      "inputs: Q5-012, XR-017, XR-043", "2026-11-21", "", "", "Medium", "neither company publishes a product-by-product comparison; both sell OCD-type metrology that can be used on packaging wafers"),
]
for i, r in enumerate(B, 1):
    r["id"] = f"B-{i:03d}"
write(os.path.join(HERE, "..", "parts", "B.csv"), B)
