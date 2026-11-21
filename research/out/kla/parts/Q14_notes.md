# Q1 (X-ray metrology vs Rigaku), Q4 (EUV mask inspection vs Lasertec), NV (Nova overlap): notes

KLA fiscal year ends June 30. Lasertec fiscal year ends June 30 (Lasertec "FY2026" = Jul 2025-Jun 2026). Nova and Onto use calendar years. Rigaku: calendar year (not used for figures here).
Evidence rows: `parts/Q1.csv` (28), `parts/Q4.csv` (33), `parts/NV.csv` (6). Arithmetic: `calc/q14_calcs.py`. Text rebuild of OpenAlex abstract records: `calc/q14_openalex_to_text.py` (rebuilds `_text/*.txt` from saved JSON; quotes in rows were checked against that text).
Tag note: SPIE papers could not be opened on spiedigitallibrary.org (Incapsula bot block). Abstracts were saved from the OpenAlex index (copies of the publisher abstract). They are tagged [S], not [F].

## Premise issues
- "Axion does not appear in KLA's 10-K/10-Q text": wrong for the 10-K. "Axion® Series" is in the Item 1 metrology product list of the 10-K FY23 through FY26 [F] Q1-004. It does not appear in the 10-Qs or in any shareholder letter.
- KLA has one X-ray product line, Axion (T2000, launched 2022-12-06) [F] Q1-001. No Axion successor, and no KLA XRR, XRF or HRXRD product, appears in the 10-K FY26 product list, the Investor Day deck, or the KLA IR press releases for Jan-Nov 2026 [F] Q1-004, Q1-027.
- Onto–Rigaku: the "~April 2026" date is right (announced 2026-04-20). "Rigaku 27%" is right, but Onto bought the 27% stake in Rigaku, not the other way round. "Ai Diffract" is an Onto software product, not a joint product name [F] Q1-015, Q1-018.
- The SPIE paper doi 10.1117/12.3090197 has the title "Monitoring of hole-to-hole distance variance in 3D NAND using Axion x-ray critical dimension metrology". It is not a "twisting validation" paper. The prior chat's details (Lam co-authors, 2 wafers, 651 sites, R²>0.84) cannot be checked [S] Q1-014.
- "Teron 6xx" is not a KLA slide name. The names on Investor Day slide p91 are: Teron 610/630/640, Teron 640e/eS/eS2, Teron SL650/655/670, Teron SL670e/XP/XP2, Gen5 Agera Wafer Print Check, TeraBeam® 8xx and Actinic 7xx [F] Q4-001..004.
- In the Investor Day transcript, "extra metrology" (p42) stands for "X-ray metrology", and "Ectinic" (p40-41) stands for "actinic". These are transcription errors in KLA's own PDF.

## Q1 X-ray metrology vs Rigaku

### KLA X-ray products
| Product | Launch | Applications (KLA words) | Status, KLA words | Status, customer or partner papers | Throughput | Revenue or units |
|---|---|---|---|---|---|---|
| Axion T2000 (CD-SAXS, transmission) | 2022-12-06 [F] Q1-001 | 3D NAND and DRAM. Logic is not mentioned [F] Q1-001, Q1-002 | At launch: "multiple systems in operation at leading memory manufacturers" [C] Q1-003. Mar 2026: "used in high volume manufacturing today" for vertical NAND and DRAM capacitor [C] Q1-005. Apr 2026: adoption "took quite a while"; no "quick adoption of X-ray anytime soon" [S] Q1-007, Q1-008 | KLA+Lam 2024: CD-SAXS as a rapid screen for tilt and bending [S] Q1-011. Kioxia+WD+KLA 2024: CD-SAXS as the reference that trains OCD [S] Q1-012. Lam 2025: CD-SAXS has low depth sensitivity and averages over the spot [S] Q1-013. 2026 Axion 3D NAND hole-distance paper: title only [S] Q1-014 | NOT DISCLOSED (read: launch release; 10-K FY26 Item 1; Investor Day deck and transcripts). Fact sheet NOT RETRIEVED | NOT DISCLOSED (read: 10-K FY26 Item 1 and Item 7; letters Q4 FY24 to Q1 FY27; Investor Day deck). The CFO said the market is $75-100M and KLA's share is about 60% [S] Q1-009. Implied KLA revenue $45-60M a year [I] Q1-010 (Low) |
| Other X-ray (XRR/XRF/HRXRD) | none found | n/a | n/a | n/a | n/a | n/a |

- Investor Day 2026 lists "X-Ray Metrology" under "Portfolio Expansion" (slide p100). It gives no roadmap, revenue or units [F] Q1-006.
- The CFO (Q3 FY26 call) said X-ray CD metrology adoption has been mostly in memory. The market could reach about $150M "over the next few years" [S] Q1-009.

### Onto–Rigaku alliance
| Item | Value | Tag / id |
|---|---|---|
| Announcement | 2026-04-20 (Onto release; Rigaku release on the same deal, undated page) | [F] Q1-015, Q1-019 |
| Terms | Onto buys 61,123,436 Rigaku shares (27.0%) from Atom Investment L.P. (Carlyle) for about $710M. Onto gets one board seat, uses the fair value option and does not consolidate. Rigaku keeps management independence, and transfers and further share purchases are restricted | [F] Q1-015, Q1-020 |
| Close | 2026-08-10, JPY 113.08B (about $720M) | [F] Q1-018 |
| Product | Onto Ai Diffract analysis software combined with Rigaku CD-SAXS platforms. "selected by two key customers". Market above $1B within 5 years (TechInsights, per Onto) | [C] Q1-016 |
| Aim | "next-generation hybrid metrology" combining X-ray and optical for FEOL logic and memory. OCD gives speed and location, X-ray gives precision on deeper structures | [F] Q1-019, [C] Q1-017 |
| Rigaku target | At least $300M of incremental market opportunity for Rigaku products by 2030 | [C] Q1-021 |
| Prior work | The two companies were already collaborating on Rigaku CD-SAXS plus Onto analytics before the equity deal | [F] Q1-022 |

### KLA statements since April 2026 on the alliance or on hybrid X-ray + optical CD
| Document | What it says | Tag / id |
|---|---|---|
| Q3 FY26 call, 2026-04-29 (third-party transcript) | Analyst asks about "x-ray versus optical for CD". Wallace: Axion adoption was slow; X-ray may help debug, but cost and throughput block production; "I don't think you're going to see a quick adoption of X-ray anytime soon". Higgins: market $75-100M, KLA about 60%. Onto and Rigaku are not named by KLA | [S] Q1-007..009 |
| Shareholder letters Q3 FY26 (Apr 2026), Q4 FY26 (Jul 2026), Q1 FY27 (Oct 2026) | No mention of X-ray, Axion, Onto, Rigaku or hybrid metrology. NOT DISCLOSED (read: full text of all three letters) | — |
| 10-K FY26 (2026-08-06), 10-Q Q1 FY27 (2026-10-29) | Competition paragraph names Lasertec and Onto; Rigaku is not named; nothing on the alliance. NOT DISCLOSED (read: Item 1 Competition, Item 1A) | [F] Q1-025 |
| KLA IR press releases Jan-Nov 2026 | No product or metrology release | [F] Q1-027 |
| Q1 FY27 call, 2026-10-28 (third-party transcript) | No mention of X-ray, Onto or Rigaku. NOT DISCLOSED (read: full transcript, search for x-ray/Axion/Onto/Rigaku/hybrid) | — |
| Q4 FY26 call, 2026-07-28 | NOT RETRIEVED (tried: fool.com URL 404; fortune.com page holds only header and participants) | — |
| Earlier context (before the alliance), Investor Day Q&A 2026-03-12 | "Hybrid metrology 10 years ago was going to just take over everything but nothing." The remark answered an AI/data question | [C] Q1-026 |
- Summary [I] Q1-028: the only KLA reaction found is the Q3 FY26 call answer. Confidence is Medium because the Q4 FY26 call transcript is missing.

## Q4 EUV mask inspection vs Lasertec

### KLA reticle portfolio (Investor Day 2026 slide p91, checked against the page image)
| Product | Type | Litho / use case | Release (slide words) | Tag / id |
|---|---|---|---|---|
| Actinic 7xx | actinic (13.5 nm) patterned | EUV, 2x–3x nm, "*Requires NA Change" | "Early Demo Stage" | [F] Q4-001 |
| TeraBeam® 8xx | multi-column e-beam, mask shop | EUV, 1x–3x nm | 2026 | [F] Q4-002 |
| Teron 640e/eS/eS2 | optical, mask shop | EUV, >3x nm | 2017 | [F] Q4-003 |
| Teron 610/630/640 | optical, mask shop | 193/193i, >70 nm | 2009 | [F] Q4-003 |
| Teron SL670e/XP/XP2 | optical, IC fab requal | EUV particles | 2018 | [F] Q4-004 |
| Teron SL650/655/670 | optical, IC fab | 193/193i particles | 2014 | [F] Q4-004 |
| Gen5 Agera wafer print check | wafer inspection | EUV printing particles | 2019 | [F] Q4-004 |

- Actinic status in KLA's words (Mar 2026): a prototype in KLA's lab, with first images and a first inspection taken weeks before Investor Day [C] Q4-007. "We are developing an actinic inspection system" [C] Q4-011. KLA says each scanner NA needs a new actinic system [C] Q4-008. In the IC fab, actinic is "Defense 3", one inspection every 2,000-5,000 wafers, after SL670e XP2 (every 100-200) and Gen5 Agera (every 200-400) [C] Q4-009. KLA calls actinic cost of ownership for requal "quite bad" [C] Q4-010.
- TeraBeam history: the "8XX" e-beam mask platform shipped in 2021 and began customer qualification for 3nm and below [F] Q4-012. It was released to market in 2026 after five years of development at TSMC [C] Q4-005. Use on N2 HVM layers: NOT DISCLOSED (read: Investor Day transcript p40-41, slides p91-94).
- Customer adoption:
  - TSMC is named by KLA for TeraBeam development [C] Q4-005. The TSMC-KLA paper is SPIE 13981-231, DOI 12.3111792, title only [S] Q4-013.
  - Samsung + KLA paper (Photomask, Oct 2026) reports multi-column EBMI used at Samsung as a "production solution". Capture rates were 98% and 96% against specs of 84% and 79% [S] Q4-014.
  - Samsung also co-publishes with Lasertec on actinic (APMI) software [S] Q4-030.
  - SK hynix publishes on an APMI tool; the vendor is not named [S] Q4-031.
  - TSMC evaluated the Lasertec X9ULTRA 193nm tool for N3 EUV masks [S] Q4-032.
- Business signals: the letters cite strong reticle demand in Q1 FY26 and Q2 FY26 [C] Q4-015, Q4-016, and better CY25 mask-inspection share [C] Q4-017. Reticle revenue is reported only inside "Patterning" (Q1 FY27: +29% YoY, 21% of revenue) [F] Q4-018. Q1 FY26 call: KLA is "in conversations with all the leading mask manufacturers" on pellicle and requal strategy [S] Q4-019.
- EUV and reticle optics supplier: NOT DISCLOSED (read: 10-K FY26 Item 1 Manufacturing/Raw Materials, Item 1A supply risk). The 10-K gives only general single- and limited-source language [F] Q4-020. Zeiss is not mentioned.

### Lasertec ACTIS
| Item | Value | Tag / id |
|---|---|---|
| ACTIS A150 | first actinic EUV patterned mask inspection system, 2019 | [F] Q4-022 |
| ACTIS A200HiT | released 2025-10-31, "Triple inspection speed of ACTIS A150", for wafer-fab incoming and periodic QA | [F] Q4-021 |
| ACTIS A300 Series | listed in the Mar 2026 company profile (High-NA per a secondary lead only) | [F] Q4-023 |
| HVM adoption | "widely adopted in high-volume manufacturing" (Lasertec paper). The paper puts A200HiT at 3x the A100, while the release says 3x the A150 | [S] Q4-029 |
| FY2026 (Jul 2025-Jun 2026) orders | JPY 237.5B vs 105.2B (+125.7%). Semiconductor orders JPY 172.2B; semiconductor backlog JPY 301.3B at 2026-06-30 (93.3% of total backlog). Semiconductor book-to-bill 1.02 | [F] Q4-024, Q4-025; [I] Q4-028 |
| Q1 FY2027 (Jul-Sep 2026) | sales JPY 40.4B (-25.5%), semiconductor JPY 23.8B (-42.9%). FY2027 order outlook "exceeded previous expectations"; advances received +JPY 42.8B | [F] Q4-026; [C] Q4-027 |
| ACTIS sales or orders | NOT DISCLOSED (read: tanshin FY2026 pp5,18; tanshin Q1 FY2027 pp4,10; Business Report page). The results presentation, where any ACTIS split would be, is NOT RETRIEVED (tried: lasertec.co.jp/en/ir/data/result.html, which loads through a JS widget from eir-parts.net; publicnow copy 403) | — |

## NV: KLA vs Nova (light touch)
- Nova names Onto and KLA as its main competitors in CD, thin-film and chemical metrology [F] NV-001.
- KLA counterparts: SpectraShape (OCD), SpectraFilm and Aleris (films), Archer/ATL (overlay), Axion (X-ray CD) [F] NV-005. ECI Technology (chemical, acquired 2022) [F] NV-004, [C] NV-006.
- Nova's X-ray product is VeraFlex (XPS+XRF materials metrology). Nova also has Metrion (SIMS) and Elipson (Raman). KLA lists no XPS, SIMS or Raman product [F] NV-002, NV-003, NV-005.

## Competition table (handoff)
| Area | KLA product | Rigaku | Onto | Lasertec | Nova | Tags |
|---|---|---|---|---|---|---|
| X-ray CD (CD-SAXS) for HAR memory | Axion T2000 (2022). KLA claims HVM use and ~60% of a $75-100M market | XTRAIA CD-3200T (TSAXS), CD-3200G (GISAXS) | Ai Diffract software on Rigaku CD-SAXS, plus 27% equity in Rigaku | — | none found | [F] Q1-001, Q1-023, Q1-015; [S] Q1-009 |
| X-ray films/materials (XRR, XRF, HRXRD, XPS) | none listed | XTRAIA MF (EDXRF+XRR+XRD, hybrid with optical), XTRAIA XD (HRXRD), TXRF, WDXRF | via Rigaku | — | VeraFlex (XPS+XRF) | [F] Q1-024, NV-002 |
| Hybrid X-ray + optical CD | none announced; CEO skeptical | with Onto | with Rigaku | — | — | [F] Q1-019; [S] Q1-008 |
| OCD / films | SpectraShape, SpectraFilm, Aleris | — | Atlas OCD | — | i Platform, T-platform, VeloCD, Prism | [F] NV-005, NV-002, Q1-017 |
| Materials metrology (SIMS, Raman, chemical) | ECI chemical analysis only | — | — | — | Metrion, Elipson, Ancolyzer | [F] NV-002, NV-004 |
| EUV actinic patterned mask | Actinic 7xx, Early Demo Stage | — | — | ACTIS A150 (2019), A200HiT (2025), A300 | — | [F] Q4-001, Q4-021..023 |
| EUV e-beam patterned mask | TeraBeam 8xx (2026) | — | — | none found | — | [F] Q4-002 |
| EUV optical mask (mask shop / fab requal) | Teron 640e/eS/eS2; Teron SL670e/XP/XP2; Gen5 Agera print check | — | — | X9ULTRA (193nm, TSMC N3 evaluation) | — | [F] Q4-003, Q4-004; [S] Q4-032 |

## Disputed-claims ledger row
| Claim | Who said it, when | Evidence for | Evidence against | Strongest tag on each side |
|---|---|---|---|---|
| KLA's actinic patterned-mask inspection is close to production | Prior chat (Nov 2026) framing; the Investor Day question about actinic, Mar 2026 | KLA has a lab prototype with first images and a first inspection, and says results "look quite impressive" [C] Q4-007. "We are developing an actinic inspection system" [C] Q4-011 | Slide release column reads "Early Demo Stage" with no date [F] Q4-001. KLA itself places actinic as a low-frequency "Defense 3" and calls its cost of ownership poor [C] Q4-009, Q4-010. No actinic mention in letters Q3 FY26-Q1 FY27 or in any 2026 press release [F] Q1-027, Q4-018. Lasertec ACTIS has shipped since 2019, and the 3x-throughput A200HiT has been out since Oct 2025 [F] Q4-021, Q4-022. KLA's 2026 product launch was e-beam (TeraBeam), not actinic [F] Q4-002. [I] Q4-033: KLA's own disclosures refute "close to production" (Medium) | For: [C]. Against: [F] |

## Prior-claim check (kla_metrology_audit.md lines 21-68 and the KLA row at line 1033; Onto row at 1034 where it touches Rigaku)
| Prior claim | Result | Evidence |
|---|---|---|
| EUV reticle tools: Teron 640e/eS/eS2, Teron SL670e XP2, Gen5 Agera print check, TeraBeam 8xx | CONFIRMED (names) | Q4-002..004 |
| TeraBeam 8xx "12×12 multi-column EBMI at TSMC N2 HVM" | CORRECTED: KLA says 5 years of development at TSMC, released 2026 [C]. "N2 HVM" is NOT VERIFIABLE. "12×12" is in the transcript, but the same passage says "24 columns" | Q4-005, Q4-006 |
| "Actinic 7xx … Early Demo Stage, requires NA change" | CONFIRMED. "*Requires NA Change" is a footnote on the 2x–3x nm use case; "Early Demo Stage" is in the release-date column | Q4-001 |
| TeraBeam High-NA and nano-imprint reticle feasibility | NOT VERIFIABLE (nano-imprint appears in no saved doc) | — |
| 8xx shipped for ≤3 nm qualification "Q2 CY2021" (Q4 FY21 letter) | CORRECTED (minor): the letter says "shipped last quarter" in the Jun-2021-quarter letter, which may mean Jan-Mar or Apr-Jun 2021. Qualification at "3nm and below" is CONFIRMED | Q4-012 |
| Actinic 7xx milestone "MISSED" | NOT VERIFIABLE as "missed": no dated KLA commitment was found. Status is early demo | Q4-001, Q4-033 |
| Lasertec ACTIS A200HiT launched Oct 2025, 3× A150 speed | CONFIRMED (2025-10-31). A Lasertec paper uses the A100 as the 3x baseline | Q4-021, Q4-029 |
| Lasertec JPY 114.8B FY25 ACTIS sales | NOT VERIFIABLE: the presentation is NOT RETRIEVED and the tanshin has no product split. A secondary lead attributes the figure to the Lasertec FY6/2025 presentation script | — |
| Lasertec ACTIS "sole commercial 13.5 nm actinic HVM system" | NOT VERIFIABLE as "sole". Lasertec claims wide HVM adoption [S]. No other commercial actinic patterned inspector was found | Q4-029 |
| Axion: transmissive CD-SAXS, non-destructive HVM 3D shape/tilt metrology | CONFIRMED (CD-SAXS, transmissive; HVM as a KLA claim). "Twisting" is not in KLA's words (release says width, shape, tilt) | Q1-002, Q1-005 |
| Axion 3D NAND twisting validation (Lam + KLA, 2 wafers, 651 sites, R²>0.84, CD-SEM calibration), doi 10.1117/12.3090197 | CORRECTED: the DOI exists, but its title is about hole-to-hole distance variance. The figures and the Lam affiliation are NOT VERIFIABLE (abstract NOT RETRIEVED) | Q1-014 |
| TSMC + KLA: optical hits resolution limits on N2 curvilinear masks, requiring 12×12 e-beam (doi 12.3111792) | NOT VERIFIABLE (abstract NOT RETRIEVED). KLA's summary of the TSMC paper: DUV covers ≥36 nm reticle printed pitch, e-beam down to 20 nm | Q4-013; transcript p40 |
| Onto row: "Rigaku 27% / Ai Diffract X-ray tie-up" | CONFIRMED (Onto holds 27% of Rigaku; Ai Diffract is Onto software) | Q1-015, Q1-016, Q1-018 |
| Onto row: Rigaku optical+X-ray HVM guided ~2028+ (Onto Q1 2026 call) | NOT VERIFIABLE (Onto call transcript not retrieved) | — |

## Gaps (one line each)
- Axion fact sheet: NOT RETRIEVED (tried: kla.com/documents/pdf/KLA_Axion_T2000_ProductFactSheet.pdf returns HTML; kla.com Axion page and metrology product page are JS shells with no text).
- Axion throughput: NOT DISCLOSED (read: launch release 2022-12-06; 10-K FY26 Item 1; Investor Day deck and transcripts).
- Axion revenue and units: NOT DISCLOSED (read: 10-K FY26 Items 1 and 7; letters Q4 FY24-Q1 FY27; Investor Day deck). Only the CFO market and share remark exists [S].
- SPIE abstracts 10.1117/12.3090197 and 12.3111792: NOT RETRIEVED (tried: doi.org to spiedigitallibrary.org, Incapsula block; Crossref and OpenAlex have no abstract).
- KLA Q4 FY26 call transcript: NOT RETRIEVED (tried: fool.com 404; fortune.com header only).
- Lasertec FY2026 and Q1 FY2027 results presentations (ACTIS split): NOT RETRIEVED (tried: lasertec.co.jp IR result page JS widget; publicnow 403).
- ACTIS sales or orders: NOT DISCLOSED (read: Lasertec tanshin FY2026 p18, Q1 FY2027 p10).
- Actinic 7xx release date: NOT DISCLOSED (read: Investor Day slides p91-94, transcript p40-41, Q&A p12; letters Q3 FY26-Q1 FY27).
- TeraBeam unit count and customers beyond TSMC/Samsung: NOT DISCLOSED (read: Investor Day slides p91-93, transcript p40).
- Reticle inspection revenue: NOT DISCLOSED (read: letters Q1 FY26-Q1 FY27, Patterning paragraphs).
- KLA EUV/reticle optics supplier: NOT DISCLOSED (read: 10-K FY26 Item 1 Manufacturing, Item 1A).
- Onto-Rigaku Business Wire copies: NOT RETRIEVED (tried: three businesswire.com URLs, HTTP/2 stream error). Onto's own q4cdn PDFs were saved instead.
- Rigaku release date on rigaku.com: NOT DISCLOSED on the page (read: full page text). Date taken from Onto's same-day release.
- Onto Q1 2026 call / 10-Q (Rigaku HVM timing): NOT RETRIEVED (not tried: investors.ontoinnovation.com is a known 403).
