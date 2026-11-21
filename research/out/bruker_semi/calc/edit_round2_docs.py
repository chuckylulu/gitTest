"""Exact-match text edits to dossier/handoff/review_packet/gaps after the second review (2026-11-21)."""
import sys
def apply(path, pairs):
    s = open(path, encoding='utf-8').read()
    for old, new in pairs:
        n = s.count(old)
        if n != 1:
            sys.exit(f'{path}: expected 1 match, found {n}: {old[:90]!r}')
        s = s.replace(old, new)
    open(path, 'w', encoding='utf-8').write(s)
    print(path, 'ok', len(pairs))

D = [
 # premise 4 calendar months
 ("   - Q2 FY2026, $134.9M total:", "   - Q2 FY2026 (Apr-Jun 2026), $134.9M total:"),
 ("   - Q3 FY2026: BSB&CA", "   - Q3 FY2026 (Jul-Sep 2026): BSB&CA"),
 ("   - 9M FY2026 total: $309.4M [F] S063.", "   - 9M FY2026 (Jan-Sep 2026) total: $309.4M [F] S063."),
 # premise 7 V003
 ("   - \"~$300M by year-end, mid-to-high single digit growth, 30% EBIT\" [S] V003.",
  "   - \"~$300M by year-end, mid-to-high single digit growth, 30% EBIT\", which the analyst carried into a \"mid-teens grower, call it $400 million\" in 2027 [S] V003."),
 # Q1 missing forms
 ("- **Launch dates** are NOT DISCLOSED on any current product page (read: every page in the P notes). The dates below come from dated releases or papers.",
  "- **Launch dates**: NOT DISCLOSED (read: every current product page listed in the P notes, retrieved 2026-11-21). The dates below come from dated releases or papers. A bare \"NOT DISCLOSED\" in the tables below means the same read-list."),
 ("- **Named fab customers** are NOT DISCLOSED in any Bruker document read.",
  "- **Named fab customers**: NOT DISCLOSED (read: Bruker releases 2016, 2017 and 2025; 10-K FY2025 Item 1; product pages; AN5001)."),
 ("SPIE AL 2026 talks on ML for X-ray CD are leads only (NOT RETRIEVED)",
  "SPIE AL 2026 talks on ML for X-ray CD: NOT RETRIEVED (tried: bruker.com event page 404; Wayback reset)"),
 # Q2 intro
 ("Figures come from earnings and conference decks [F] and from third-party transcripts [S].",
  "Figures come from earnings and conference decks [F] and from third-party transcripts [S]. Where a row mixes sources, each statement carries its own tag inline."),
 # Q2 table rows with mixed tags -> inline tags
 ("| 2024-08-06 / 2024-11-05 | Q2-24, Q3-24 decks; 10-Q Q3-24 | H1 / 9M FY2024 | \"Strong growth\" in semi metrology; no rate given | [F] | S008-S010 |",
  "| 2024-08-06 / 2024-11-05 / 2024-11-07 | Q2-24 deck; Q3-24 10-Q; Q3-24 deck | H1 FY2024 (Jan-Jun 2024); Q3 FY2024 (Jul-Sep 2024); 9M FY2024 (Jan-Sep 2024) | \"Strong growth in ... semicon metrology\" (H1); \"strong demand in its semiconductor metrology market\" (Q3, 10-Q); \"Strength also in ... semicon metrology\" (9M). No rate given | [F] | S008-S010 |"),
 ("| 2025-02-13 | Q4-24 deck p8 | Q4 FY2024 (Oct-Dec 2024) / FY2024 | Organic revenue growth >20% in Q4-24 and low-teens in FY24; >$250M annual revenue; margins \"well above corporate average\" | [F] / [C] | S012-S015 |",
  "| 2025-02-13 | Q4-24 deck p8 | Q4 FY2024 (Oct-Dec 2024) / FY2024 (Jan-Dec 2024) | Organic revenue growth >20% in Q4-24 and low-teens in FY24 [F]; >$250M annual revenue [F]; margins \"well above corporate average\" [C] | inline | S012-S015 |"),
 ("| 2025-02-13 | Q4-24 call | FY2024 (Jan-Dec 2024) | \"north of $125 million\" AI/HPC-related; total \"north of $250 million\", \"maybe half\" to HPC and AI (≈50%, calc/semi_mix_calc.py) | [S] | G050, G051 |",
  "| 2025-02-13 | Q4-24 call | FY2024 (Jan-Dec 2024) | \"north of $125 million\" AI/HPC-related; total \"north of $250 million\", \"maybe half\" to HPC and AI [S]. Ratio ≈50% [I, Low] V007 | inline | G050, G051, V007 |"),
 ("| 2025-11-03 | Q3-25 deck p7; call | 9M FY2025 (Jan-Sep 2025) | \"Softness in X-Ray Semi\". Call: semi \"approaching or is around $300 million\"; \"flattish this year\" | [F]; [S] | S019-S021 |",
  "| 2025-11-03 | Q3-25 deck p7; call | 9M FY2025 (Jan-Sep 2025); FY2025 (Jan-Dec 2025) | \"Softness in X-Ray Semi\" (9M) [F]. Call: semi \"approaching or is around $300 million\" a year; orders \"flattish this year\"; revenue \"a little weaker\" [S] | inline | S019-S021 |"),
 ("| 2026-02-27 | 10-K FY2025 p50 | FY2025 | Group gross-margin", "| 2026-02-27 | 10-K FY2025 p50 | FY2025 (Jan-Dec 2025) | Group gross-margin"),
 ("| 2026-02-12 / 2026-05-06 | Q4-25 and Q1-26 calls | FY2026 outlook (Jan-Dec 2026) | Semi revenue guided \"up in the low-single-digits range\", reaffirmed in Q1 | [S] | S027, S034 |",
  "| 2026-02-12 / 2026-05-06 | Q4-25 and Q1-26 calls | FY2026 outlook (Jan-Dec 2026) | Semi revenue guided \"up in the low-single-digits range\"; tentatively repeated in Q1 (\"Someone is nodding, so the answer seems to be, yes\") | [S] | S027, S034 |"),
 ("| 2026-05-06 | Q1-26 call; deck p6; release | Q1 FY2026 (Jan-Mar 2026) | \"greater than $300 million annual revenue business\" (run-rate, period NOT DISCLOSED); organic bookings >20%; only \"some\" of the Q4-25 pushout recaptured; strong HBM and advanced-packaging orders | [S]; [F] | S031-S036 |",
  "| 2026-05-06 | Q1-26 call; deck p6; release | Q1 FY2026 (Jan-Mar 2026) | Call [S]: \"greater than $300 million annual revenue business\" (run-rate; period NOT DISCLOSED (read: Q1-26 transcript, prepared remarks)); organic bookings >20%; only \"some\" of the Q4-25 pushout recaptured. Deck and release [F]: strong AI-driven HBM and advanced-packaging orders | inline | S031-S036 |"),
 ("| 2026-06-04 | Jefferies conference (CFO) | Annual run-rate stated 2026-06-04 (period NOT DISCLOSED) | ~$300M, of which ~$200M production QA/QC (≈67%), ~$50M R&D and ~$50M mask repair. On the analyst's \"$40 million pushout\": $10-15M recaptured in Q1-26, \"similar amount in Q2 and Q3\" expected. Capacity to at least double by end-2026 | [S] | G060-G066 |",
  "| 2026-06-04 | Jefferies conference (CFO) | Annual run-rate stated 2026-06-04; period NOT DISCLOSED (read: Jefferies transcript, semiconductors section) | ~$300M, of which ~$200M production QA/QC, ~$50M R&D and ~$50M mask repair [S]; shares ≈67/17/17% [I, Low] V008. On the analyst's \"$40 million pushout\": $10-15M recaptured in Q1-26 (Jan-Mar 2026), \"similar amount in Q2 and Q3\" expected [S]. Capacity to at least double by end-2026 [S] | inline | G060-G066, V008 |"),
 ("| 2026-08-05 | 10-Q Q2-26 MD&A | Q2 / H1 FY2026 | BSI NANO", "| 2026-08-05 | 10-Q Q2-26 MD&A | Q2 FY2026 (Apr-Jun 2026) / H1 FY2026 (Jan-Jun 2026) | BSI NANO"),
 ("| 2026-11-04 | Q3-26 call | FY2026 outlook | Analyst: \"~$300M to end the year, mid to high single digit growth, 30% EBIT\". CEO: \"I think the direction is correct\" | [S] | V003 |",
  "| 2026-11-04 | Q3-26 call | FY2026 (Jan-Dec 2026) and FY2027 (Jan-Dec 2027) outlook | Analyst: \"$300 million to end the year, mid to high single digit growth, 30% EBIT margins\", then a \"mid-teens grower, call it $400 million business next year\". CEO: no 2027 guidance, \"I think the direction is correct\" | [S] | V003 |"),
 ("| 2026-11-04 | Q3-26 deck p7; release | 9M FY2026 | \"Strong Semi ... revenues\" and \"Strong AI-driven orders for memory and advanced packaging\"; no figure | [F] / [C] | S051, S052 |",
  "| 2026-11-04 | Q3-26 deck p7; release | 9M FY2026 (Jan-Sep 2026) | Deck: \"Strong Semi ... revenues\" and \"Strong AI-driven orders for memory and advanced packaging\" [F]; release: \"poised for growth acceleration\" [C]; no figure | inline | S051, S052 |"),
 ("**Never disclosed:**\n- Semi revenue in dollars for any single quarter or for LTM to Q3 FY2026.",
  "**NOT DISCLOSED (read: decks Q4-24 to Q3-26; JPM 2026 deck; releases Q4-25 to Q3-26; 10-Qs Q1-Q3 FY2026 MD&A):**\n- Semi revenue in dollars for any single quarter or for LTM to Q3 FY2026."),
 # Q3 HRXRD row ok; Company A bullet edition
 ("Implied 2023 revenue within the same Yole edition: Rigaku about $141M, Company A about $113M [I, Low] M006 (calc/M_calc.py).",
  "Implied CY2023 (Jan-Dec 2023) revenue within the same Yole edition (Q4 2024, $470M market): Rigaku about $141M, Company A about $113M [I, Low] M006 (calc/M_calc.py)."),
 # Q4 competitor table tags
 ("| Park Systems | NX-Wafer, FX, NX-Hybrid WLI | \"No practical solution other than AFM\" for hybrid bonding | Taiwan \"T company\" AFMs for advanced packaging [S]; 2-year imec project [C] | [S]/[C] | H031-H038 |",
  "| Park Systems | NX-Wafer, FX, NX-Hybrid WLI | \"No practical solution other than AFM\" for hybrid bonding [S] (Park executives in Korean press, 2025) | Taiwan \"T company\" AFMs for advanced packaging [S] (2025-04); 2-year imec project [C] (2026-06-10) | inline | H031-H038 |"),
 ("| Nova | Prism (spectral interferometry + OCD), VTS-ML | Inline Cu recess with reduced \"reliance on reference data\" | IBM Research co-authored a SPIE 2026 paper | [F]/[C] | H018-H021, H050-H052 |",
  "| Nova | Prism (spectral interferometry + OCD), VTS-ML | Inline Cu recess with reduced \"reliance on reference data\" [C] (Nova blog 2025-08-03) | IBM Research co-authored a SPIE AL 2026 paper [F] | inline | H018-H021, H050-H052 |"),
 ("| Infinitesima; Nearfield; Camtek (Hawk) | in-line AFM; QUADRA; inspection | | SK hynix (Infinitesima) [C]; imec (Nearfield) [S]; >$50M of Hawk orders, customers unnamed [C] | | H040-H042, H062 |",
  "| Infinitesima; Nearfield; Camtek (Hawk) | in-line AFM; QUADRA; inspection | in-line 3D process control; pad roughness and dishing; hybrid-bonding inspection | SK hynix volume production (Infinitesima release 2025-07-08) [C]; imec deployment [S]; >$50M initial Hawk orders, customers unnamed (Camtek release 2024-11-29) [C] | inline | H040-H042, H062 |"),
 ("**Tool counts per line:** NOT DISCLOSED in any document read (list in gaps.md; H070).",
  "**Tool counts per line:** NOT DISCLOSED (read: Bruker AN5001, InSight 300 page, webinar AF324; Onto G5 release 2026-03-16; Camtek Hawk release 2024-11-29; Infinitesima release 2025-07-08; greened.kr 2025-12-22; ddaily 2025-04-14; SemiEngineering 2026-11-10; KLA FY25 annual report) (H070)."),
 # B1 (b) 9M FY2025 months; (d); (f)
 ("9M FY2025 memory ¥3.6bn vs ¥1.1bn a year earlier;", "9M FY2025 (Jan-Sep 2025) memory ¥3.6bn vs ¥1.1bn in 9M FY2024 (Jan-Sep 2024);"),
 ("| (d) Semi metrology is a ~$300M business at ~30% EBIT margin | Analyst framing on the Q3-26 call (V003). CEO: \"I think the direction is correct\" |",
  "| (d) Semi metrology is a ~$300M business at ~30% EBIT margin | Analyst framing on the Q3-26 call, 2026-11-04, in a question that ran into 2027 (V003). CEO: no 2027 guidance, \"I think the direction is correct\" |"),
 ("Revenue: FY2025 flat (S025); Q3 FY2026 down double digits (S047). LTM to Q3 FY2026: NOT DISCLOSED. EBIT basis undefined. The analyst's \"mid to high single digit growth\" conflicts with the low-single-digit FY2026 guide (S027, S034)",
  "Revenue: FY2025 (Jan-Dec 2025) flat (S025); Q3 FY2026 (Jul-Sep 2026) down double digits (S047). LTM to Q3 FY2026: NOT DISCLOSED (read: Q3-26 deck p7; Q3-26 release; 10-Q Q3 FY2026 MD&A). EBIT basis undefined. The analyst's \"mid to high single digit growth\" for FY2026 differs from the low-single-digit FY2026 guide (S027, S034)"),
 ("If that holds, 75-112% is recaptured by end Q3 [I, Low] V005 |",
  "Expected recapture by end Q3-26: 75-112% if \"similar amount\" means $10-15M per quarter, 50-75% if it means Q2 and Q3 combined [I, Low] V005 |"),
 ("| FY2025 revenue flat (S025), with \"Softness in X-Ray Semi\" (S019).",
  "| FY2025 (Jan-Dec 2025) revenue flat (S025); \"Softness in X-Ray Semi\" in 9M FY2025 (Jan-Sep 2025) (S019)."),
 # B2
 ("1. No CD-SAXS (X-ray CD) tool appears on Bruker's 2026 X-ray product pages or brochure [F] R053, P notes.",
  "1. Bruker's 2026 X-ray metrology page for silicon and compound semiconductors lists SIRIUS-RF, SIRIUS-FW, 7300LSI, Delta-X, QCVelox-HR, QCVelox-E and QC5-R, none of them a CD-SAXS tool [F] R053."),
 ("3. Semi revenue was flat in FY2025 (Jan-Dec 2025), with \"Softness in X-Ray Semi\" [F] S025, S019.",
  "3. Semi revenue was flat in FY2025 (Jan-Dec 2025) [F] S025, after \"Softness in X-Ray Semi\" in 9M FY2025 (Jan-Sep 2025) [F] S019."),
 ("Q3 FY2026 semi revenue fell by double digits on pushouts [S] S047.", "Q3 FY2026 (Jul-Sep 2026) semi revenue fell by double digits on pushouts [S] S047."),
 # B3 move undated rows
 ("| FY2027 (Jan-Dec 2027), with some in FY2028 | Conversion of 2026 semi orders to revenue | Tests ledger claims (a), (d) and (f) | [S] S046 |\n| FY2026 (Jan-Dec 2026), reported in early 2027 | Rigaku's forecast of >JPY 6bn MF-3400 + predecessor sales | Measures Rigaku's memory XRR push | [C] C006 |\n", ""),
 ("**Watch list, no confirmed date** [I]:\n",
  "**Watch list, no confirmed date** [I]:\n- **Conversion of 2026 semi orders to revenue:** \"mostly in fiscal year 2027 and some in fiscal year 2028\" (FY2027 = Jan-Dec 2027) [S] S046. Tests ledger claims (a), (d) and (f).\n- **Rigaku MF-3400:** forecast of >JPY 6bn MF-3400 + predecessor sales in FY2026 (Jan-Dec 2026) [C] C006; reported with Rigaku's FY2026 results (below).\n"),
 ("  - SPIE Advanced Lithography + Patterning 2027: NOT RETRIEVED (spie.org bot page); search lead says 2027-02-21 to 02-25.\n  - IEEE ECTC 2027: NOT RETRIEVED (ectc.net 403); search lead says 2027-06-01 to 06-04.",
  "  - SPIE Advanced Lithography + Patterning 2027: NOT RETRIEVED (tried: spie.org, returned a bot-check page); search lead says 2027-02-21 to 02-25.\n  - IEEE ECTC 2027: NOT RETRIEVED (tried: ectc.net, HTTP 403); search lead says 2027-06-01 to 06-04."),
 ("- **Export controls:** no dated deadline found. The CEO said China restrictions",
  "- **Export controls:** dated deadline NOT DISCLOSED (read: 10-K FY2025 risk factors; call transcripts). On the Q4-24 call (2025-02-13) the CEO said China restrictions"),
]
apply('dossier.md', D)

H = [
 ("1 guide, unresolved: FY2026 semi revenue \"up in the low-single-digits range\" (Q4-25 call, reaffirmed on Q1-26 call) [S] S027, S034. On the Q3-26 call the CEO accepted the \"direction\" of an analyst framing of mid-to-high single-digit growth [S] V003. 0 beats / 0 misses resolved. No business-unit guidance in company documents (read: releases and decks Q4-25 to Q3-26)",
  "1 guide, unresolved: FY2026 (Jan-Dec 2026) semi revenue \"up in the low-single-digits range\" (Q4-25 call; tentatively repeated on the Q1-26 call) [S] S027, S034. 0 beats / 0 misses resolved. Business-unit guidance in company documents: NOT DISCLOSED (read: releases and decks Q4-25 to Q3-26)"),
 ("AI/HPC-related: \"north of $125 million\" of a \"north of $250 million\" FY2024 business, \"maybe half\" [S] G050, G051",
  "AI/HPC-related: \"north of $125 million\" of a \"north of $250 million\" FY2024 (Jan-Dec 2024) business, \"maybe half\" [S] G050, G051"),
 ("FY2025 flat [F] S025;", "FY2025 (Jan-Dec 2025) flat [F] S025;"),
 ("H1 FY2026 >15% organic [F] S037; Q3 FY2026 down double digits [S] S047", "H1 FY2026 (Jan-Jun 2026) >15% organic [F] S037; Q3 FY2026 (Jul-Sep 2026) down double digits [S] S047"),
 ("Only EBIT is given: ~30% for H1 FY2026 [F] S038", "Only EBIT is given: ~30% for H1 FY2026 (Jan-Jun 2026) [F] S038"),
 ("Q2 FY2026 >50% [S] S039;", "Q2 FY2026 (Apr-Jun 2026) >50% [S] S039;"),
 ("Lead times 9-24 months; conversion mostly FY2027, some FY2028 [S] S040, S046. Dollar backlog NOT DISCLOSED (read: Q3-26 deck; 10-Q Q3 FY2026 RPO note, group-level only)",
  "Lead times 9-24 months; conversion mostly FY2027 (Jan-Dec 2027), some FY2028 [S] S040, S046. Dollar backlog NOT DISCLOSED (read: Q3-26 deck; 10-Q Q3 FY2026 RPO note, group-level only)"),
 ("NOT DISCLOSED at business-unit level (read: 10-Q Q3 FY2026 balance sheet and debt note, group-level only)",
  "NOT DISCLOSED (read: 10-Q Q3 FY2026 balance sheet and debt note; figures are group-level only)"),
 ("Closest: low-teens organic growth FY2024 [F] S013, then flat FY2025 with \"Softness in X-Ray Semi\" [F] S025, S019",
  "Closest: low-teens organic growth in FY2024 (Jan-Dec 2024) [F] S013, then flat FY2025 (Jan-Dec 2025) [F] S025"),
 ("Rigaku claims 38% of semiconductor X-ray metrology in CY2024 (citing Yole), and Onto-Rigaku CD-SAXS was \"selected by two key customers\"; Bruker lists no CD-SAXS tool (V006 [I]) [C] R012, R004",
  "Rigaku claims 38% of semiconductor X-ray metrology in CY2024 (Jan-Dec 2024, citing Yole), and the Onto-Rigaku CD-SAXS offering was \"selected by two key customers\" (2026-04-20) [C] R012, R004"),
]
apply('handoff.md', H)

R = [
 ("| 3 | Semi metrology size and margin | [F] | >$300M revenue, >25% EBIT |", "| 3 | Semi metrology size and margin; no one-offs named, EBIT basis undefined | [F] | >$300M revenue, >25% EBIT |"),
 ("| blind-test R² ~0.8 | SPIE AL 2026 | https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf | p4 |",
  "| blind-test R² ~0.8 | SPIE AL 2026 (Feb 2026) | https://www.novami.com/wp-content/uploads/2026/04/13981-16-timoney-spie-alp-2026-vts-ml-cu-recess-final.pdf | p4 (training set); p7 (R² ~0.8) |"),
 ("1. **No 2026 goodwill impairment touched semiconductor metrology** (G080; confidence High).",
  "1. **None of the three named 2026 goodwill charges is in a semiconductor unit; whether a semi unit was among the units tested in Q3 is NOT DISCLOSED (read: 10-Q Q3 FY2026 MD&A goodwill section; Note 5)** (G080; confidence Medium)."),
 ("   - Reason: all three 2026 charges are in named life-science units.",
  "   - Reason: all three 2026 charges are in named life-science units, but the units that passed the Q3 test are not named."),
 ("(Rigaku MTP Feb 2025 p11; Rigaku 3Q FY2025 deck p10)", "(Rigaku MTP Feb 2025 p11 for FY2024; Rigaku annual securities report FY2025, EDINET S100XTB1, p25 for FY2025)"),
 ("75-112% expected by Q3)", "75-112% expected by Q3 if read per quarter, 50-75% if Q2+Q3 combined)"),
 ("1. **Does any Bruker document confirm >30% semi bookings growth", "1. **Does any Bruker document state >30% semi bookings growth"),
]
apply('review_packet.md', R)

G = [
 ("- Hysitron model: the page heading says ATI 8800, the URL and brochure say 8900. NOT DISCLOSED which is current (read: product page; brochure).",
  "- Which Hysitron model is current (page heading ATI 8800; URL and brochure 8900). NOT DISCLOSED (read: product page; brochure B5000)."),
 ("- Rigaku's own XHENA AX-3000 release. NOT RETRIEVED (only a trade reprint was found).", "- Rigaku's own XHENA AX-3000 release. NOT RETRIEVED (tried: web search; only a trade reprint was found)."),
 ("- Onto 8-Ks on the Rigaku deal. NOT RETRIEVED (sec.gov only). Onto's q4cdn release PDFs were used instead.", "- Onto 8-Ks on the Rigaku deal. NOT RETRIEVED (tried: sec.gov, 403 without contact User-Agent). Onto's q4cdn release PDFs were used instead."),
 ("- MarketsandMarkets, QY Research and TechInsights databases. NOT RETRIEVED (paid or 403).", "- MarketsandMarkets, QY Research and TechInsights databases. NOT RETRIEVED (tried: marketsandmarkets.com 403; QY and TechInsights paywalls)."),
 ("- KLA Kronos 1190 release and Zeta-6xx datasheet. NOT RETRIEVED (server returned HTML, not PDF).", "- KLA Kronos 1190 release and Zeta-6xx datasheet. NOT RETRIEVED (tried: kla.com PDF URLs; server returned HTML, not PDF)."),
 ("- Full text of the 2016 CEA Grenoble TED notice that mentions \"Jordan Valley\". NOT RETRIEVED (WAF challenge).", "- Full text of the 2016 CEA Grenoble TED notice that mentions \"Jordan Valley\". NOT RETRIEVED (tried: ted.europa.eu notice page; WAF challenge)."),
 ("- IEEE Xplore originals (ECTC 2023/2024 Adeia and Niazi et al.). NOT RETRIEVED (tried: paywall).", "- IEEE Xplore originals (ECTC 2023/2024 Adeia and Niazi et al.). NOT RETRIEVED (tried: ieeexplore.ieee.org; paywall)."),
 ("- Bruker Q4 FY2026 earnings date. NOT DISCLOSED as of 2026-11-21 (no announcement found).", "- Bruker Q4 FY2026 earnings date. NOT RETRIEVED (tried: web search for an announcement, 2026-11-21; none found)."),
 ("- Consensus paper search: monthly quota exhausted. Firecrawl search: credits exhausted. Discovery fell back to WebSearch.", "- Tool limits (not data gaps): Consensus monthly quota and Firecrawl credits ran out. Discovery fell back to WebSearch."),
]
apply('gaps.md', G)
