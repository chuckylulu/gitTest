# R findings: Bruker vs Rigaku in semiconductor X-ray metrology (Q3)

Evidence rows: `research/out/bruker_semi/parts/R.csv` (R001-R072). quote_check: 68 FOUND, 0 NOT FOUND; the 4 [I] rows have no quotes.
Calculations: `research/out/bruker_semi/calc/R_calc.py`. CSV builder: `calc/R_build_csv.py`.
Fiscal years: Rigaku's FY ends Dec 31, so FY2025 = Jan-Dec 2025 (R047; yuho FY2025 covers 2025-01-01 to 2025-12-31). Bruker's FY also ends Dec 31.

## 1. Tool-class table

| Tool class | Bruker product(s) (2026 web/brochure) | Rigaku product(s) (2026 web) | Chipmaker usage evidence (who, vendor, source, tag) | Market-share figure (value, who claims, year, tag) |
|---|---|---|---|---|
| HRXRD (epi, Si/SiGe superlattice, GAA) | 7300LSI (formerly JVX7300LSI), SIRIUS-XRD, QCVelox-HR, QCVelox-E, QC5-R, Delta-X (R053, R054) | TFXRD, XTRAIA TF, XTRAIA XD / XD-3300 (R026) | Bruker 2016: "multiple leading logic and foundry manufacturers" chose JVX7300LSI, unnamed [C] (R068). Rigaku: XD-3300 "delivered to multiple leading-edge" chipmakers, unnamed [C] (R034); "already adopted by major foundry and memory manufacturers" [C] (R036). No named chipmaker found. | Rigaku 2030 target: >70% of a $100m Si/SiGe SAM [C] (R019). Bruker brochure: "#1 inline ... XRD" with no source or year [C] (R067). |
| XRR | SIRIUS-RF, SIRIUS-XRD, 7300LSI, 6300-XRR (R053, R054) | XTRAIA MF-2000/3000/3400, XTRAIA CD-3010G (XRR mode) (R024, R027) | Rigaku: MF-3400 GEN4 "adopted by major memory player" [C] (R038). Nothing named. | None specific to this class. |
| XRF, incl. micro-XRF for bumps and plating | SIRIUS-RF (dual-source µXRF), SIRIUS-FW (single-bump %Ag in SnAg, UBM), 6300-RF (R053, R058) | WaferX 310, WDA-3650, AZX 400 (WDXRF); ONYX 3000/3200 (micro-EDXRF + 3D confocal, bumps and BEOL); XHEMIS EX-2000 (R024, R025, R031) | Rigaku: first ONYX 3200 shipped to "a major global foundry" advanced-packaging line [C] (R032); light-element XRF "adopted by major logic manufacturer" [C] (R037). Bruker 2022 interview: HBM and logic activity "in Taiwan" by tier-ones [S] (R062). | Bruker: "#1 inline ... µXRF" [C] (R067). Rigaku ONYX target ¥1.5bn FY2026 [C] (R033). |
| TXRF / VPD-TXRF (contamination) | None on the 2026 semi pages. Bruker AXS sells TXRF in its lab analytical line per the 10-K (R059); no wafer-fab TXRF is listed. | TXRF 3760, TXRF 310Fab, XHEMIS TX-2000/TX-3000; VPD: TXRF-V310, XHEMIS TX-3000V (R023) | No chipmaker-named source found. | Rigaku: "overwhelming market share" and "effective global standard" in TXRF, no % given [C] (R015, R016, R018). Conventional TXRF sales ~¥5bn in 2025, a forecast [C] (R017). |
| X-ray CD (CD-SAXS / T-SAXS / GI-SAXS) | None in the 2026 lineup. Bruker showed its own "XCD" CD-SAXS tool for 3D-NAND/DRAM HAR at FCMN 2022 (R051). | XTRAIA CD-3200T (T-SAXS, launched 2020), CD-3010G (GISAXS); CD-3200G in development (R027, R028, R019) | **Samsung Electronics** (Device Solutions) slides with Onto and Rigaku co-authors on XCD/CD-SAXS for deep VNAND, dated 2026-03-18 [F] (R048, R049). Onto: joint CD-SAXS+Ai Diffract "selected by two key customers"; "systems delivered for advanced V-NAND and DRAM" [C] (R004, R006). Rigaku: CD-3200 "Implemented by Major Memory" and WFE makers [C] (R039). Lam benchmarked "3 ... CD-SAXS world leading suppliers", names not given [F] (R050). | Rigaku 2030 targets: >50% of a $100m DRAM/NAND HAR SAM and >50% of a $100m logic-3D SAM [C] (R019). Onto: >$1bn market over 5 years, per "external analysts" (footnote: TechInsights) [C] (R005). |
| X-ray imaging / inspection for packaging (2D/3D, CT, bumps, TSV, hybrid-bond voids) | None in the 2026 lineup. XRDI tools (JVSENSUS-600F, QC-TT, QC-RT) list "advanced packaging defect inspection" (R055). Bruker presented X-ray imaging (XRI) for voids/non-wets at FCMN 2022 (R052). | XHENA AX-3000 (3D laminography for micro-bumps/TSVs in CoWoS, HBM, hybrid bonding; at customer evaluation, Sep 2026) [S] (R030). The FY25 3Q deck lists AXI with an alpha system in demo and a beta under development (R019). | None found for either vendor. | Rigaku 2030 target: >30% of a $300m AXI packaging SAM [C] (R019). |
| (Adjacent) crystal-defect imaging | XRDI: JVSENSUS-600F, QC-TT, QC-RT (R055) | XRTmicron, XTRAIA XT (R029) | Bruker 2017: "multiple leading logic and foundry customers" ordered JVSensus-600E, unnamed [C] (R061). | Bruker: "#1 ... XRDI" [C] (R067). |

**Overall share claims, all from Rigaku and sourced to Yole:**
- 2023: Rigaku 30%, "Company A" 24%, others 46% (MTP Feb 2025, Fig.13, read from the chart image) [C] (R011).
- 2024: Rigaku 38%, others 62%, of a ~$498m market (yuho FY2025 p20/p25, citing Yole WFE Market Monitor Q4 2025) [C] (R012, R013).

The competitor is not named in either source. The 2023 and 2024 figures come from different Yole editions.

Bruker publishes no X-ray-specific share figure. Its brochure claims "#1" in inline AFM, XRD, µXRF and XRDI with over 1000 tools installed, giving no source or year (R067). The web claim that "75% of top-25 chipmakers rely on Bruker" covers all Bruker semiconductor instruments, not X-ray only (R021).

Implied Rigaku X-ray metrology revenue, from Rigaku's own Yole figures: ~$141m (2023) and ~$189m (2024) [I, Low] (R070).

## 2. Onto–Rigaku alliance (facts only)
- **Announcement, 2026-04-20.** Onto agreed to buy 27% of Rigaku from Atom Investment L.P., a Carlyle affiliate, for ~$710m (R001). The stake is 61,123,436 shares, 27.0% of outstanding shares excluding treasury shares at 2026-03-31 (R002). Onto gets the right to nominate one director, uses the fair-value option and does not consolidate Rigaku (R003). Rigaku keeps management independence, and the agreement restricts share transfers and further purchases (R002 note).
- **Technology.** The companies were already integrating Rigaku CD-SAXS with Onto software, which Onto names as Ai Diffract (R010). Onto says the offering was "selected by two key customers" (R004). Onto's subtitle reads "Systems delivered for advanced V-NAND and DRAM metrology" (R006). Rigaku targets at least $300m of incremental market opportunity by 2030 (R009).
- **Closing, 2026-08-10.** The price was JPY 113,078,356,600, about US$720m (R007), which implies JPY 1,850 per share (calc). The release literally says "113,078,356,600 billion yen", a drafting error in the source.
- **Onto Q3 2026 (Jul–Sep 2026).** Onto booked an unrealized loss of $40.841m on the Rigaku investment (R008).
- **Customers.** Neither company names the customers.

## 3. Claim: "Bruker leads X-ray metrology in logic fabs and Rigaku leads in memory"
**Who said it:** I found no primary source, press article or market-research summary that makes this claim (searches listed in section 4). Treat it as unattributed.

**Evidence for:**
- Samsung's memory unit co-presented CD-SAXS/XCD work with Rigaku and Onto on VNAND [F] (R048).
- Onto's release mentions V-NAND and DRAM deliveries [C] (R006).
- Rigaku's memory revenue rose sharply in 9M FY2025: ¥3.6bn vs ¥1.1bn, while logic fell from ¥5.5bn to ¥3.9bn [F] (R040, R041).
- Memory (26%) passed logic/foundry (21%) in Rigaku's FY2025 semi revenue mix [F] (R043).
- Rigaku says T-SAXS is "implemented by major memory" makers [C] (R039).
- Bruker's past PRs and interview stress logic and foundry customers [C/S] (R061, R062, R068).

**Evidence against:**
- In FY2024, Rigaku's semi revenue was logic-heavy: logic/foundry 35% vs memory 10% [F] (R042).
- Rigaku claims adoption by a "major logic manufacturer" and a "major foundry" (XRF, ONYX, XD) [C] (R032, R036, R037).
- Rigaku states its revenue is deliberately balanced across memory, logic and power [C] (R044, R042).
- Bruker markets Sirius-RF and 7300LSI for both memory and logic, and showed XCD for 3D-NAND in 2022 [C/F] (R051, R056, R057).
- Bruker's Q2 2026 orders strength is "memory and advanced packaging" [C] (R063).
- Rigaku claims overall X-ray metrology leadership, 30% (2023) and 38% (2024) [C], and Bruker claims "#1" in inline XRD/µXRF [C]. Neither gives a split by fab type, so both conflict with the claim as stated.

**[I] (Medium):** The available evidence does not support a clean logic/memory split. Rigaku's mix changed sharply from FY2024 to FY2025 (R069). No source gives either vendor's share by fab type.

## 4. NOT DISCLOSED / NOT RETRIEVED
- **Named chipmaker customers, Rigaku:** NOT DISCLOSED (read: yuho FY2025, p52 says no customer ≥10%; FY25 3Q deck p17; ONYX/XD-3300/TX-3000 releases).
- **Named chipmaker customers, Bruker:** NOT DISCLOSED (read: 2016/2017 PRs; 10-K FY2025 Item 1).
- **Bruker X-ray metrology revenue or share:** NOT DISCLOSED (read: 10-K FY2025 Item 1; Q2 2026 and Q3 2025 decks).
- **Identity of "Company A" (24%, 2023):** NOT DISCLOSED (read: MTP Feb 2025 p11).
- **Rigaku Integrated Report 2025 and IR library PDFs:** NOT RETRIEVED (tried: rigaku-holdings.com/english/ir/library/reports, presentations and securities; the pages load lists by JavaScript and contain no PDF links).
- **Rigaku FY26 1Q deck (2026-05-13), 1H FY2025 deck, 3Q FY2024 deck:** NOT RETRIEVED (tried: ircms.irstreet.com URLs from search, HTTP 404).
- **Rigaku IPO prospectus (Oct 2024):** NOT RETRIEVED (not located; I used the FY2025 yuho from EDINET instead).
- **Onto 8-K on the Rigaku deal:** NOT RETRIEVED (sec.gov only; scripts refused or SEC_UA not set; not attempted per instruction). I used Onto's own q4cdn releases.
- **Onto closing release on businesswire.com:** NOT RETRIEVED (HTTP 000/timeout). I used the q4cdn PDF.
- **SPIE Digital Library abstracts and PDFs:** NOT RETRIEVED (tried: JM3 22(3) 031205 Bruker/Lam HAR tilt SAXS; JM3 031206 CD-SAXS review; SPIE 12955 129550K; SPIE 11325 113250W). The site returns an Incapsula bot page; junk files deleted.
- **Kioxia R&D topics-29 page and semi.org Bruker 2021 slides:** NOT RETRIEVED (HTTP 000 and 403).
- **Rigaku's own XHENA AX-3000 release:** NOT RETRIEVED. Only a trade reprint was saved ([S], R030).
- **Consensus paper search:** NOT RETRIEVED (monthly free quota exhausted).
- **Firecrawl web search:** NOT RETRIEVED (credits exhausted). The Firecrawl research index returned no vendor-specific papers.
- **Supplier awards** (Intel PQS/EPIC, TSMC, Samsung, SK hynix, Micron) to either vendor for X-ray metrology: none found in searches. Rigaku's 2025 award is an SPIE best-paper award, not a supplier award (R065).

## 5. Premise checks
- **Bruker product names.**
  - "JVX" and "D8 FABLINE" are not used on Bruker's 2026 semi pages. JVX7300LSI is now sold as "7300LSI" (R068 note); D8 FABLINE appears only in 2009/2011 orders (search leads, not saved).
  - "QC-TT" exists, but it is an XRDI defect-inspection tool, not metrology (R055).
  - "Delta-X" exists and is listed under compound-semiconductor metrology (R053).
  - "Sirius XRI" was not found. Bruker showed "XRI" X-ray imaging in 2022 (R051, R052), but the current lineup lists only Sirius-RF, Sirius-FW and Sirius-XRD.
  - Bruker has no current CD-SAXS or fab TXRF product.
- **Rigaku product names.** All named products are verified: XTRAIA, WaferX (WaferX 310), TXRF 3760, TXRF 310Fab, XHEMIS (TX-2000/3000/3000V, EX-2000) and ONYX (3000/3200). "CD-SAXS" is the XTRAIA CD series (CD-3200T, CD-3010G).
- **Onto–Rigaku deal.**
  - Announcement date 2026-04-20, 27% stake, CD-SAXS + Ai Diffract: confirmed.
  - The ~$710m figure is the signing value. Closing on 2026-08-10 was JPY 113.08bn, about $720m.
  - The stake was bought from Carlyle's Atom Investment, not issued new by Rigaku.
- **Rigaku listing and FY.** The "TSE 268A, listed Oct 2024" premise is confirmed. The yuho FY2025 p3 note 7 states the listing on TSE Prime on 2024-10-25 ("2024年10月25日付で東京証券取引所プライム市場に上場"). The Dec 31 FY end is verified (R047).
