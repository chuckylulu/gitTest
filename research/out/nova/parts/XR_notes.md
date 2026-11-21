# XR module: Nova and X-ray metrology, the Onto-Rigaku alliance, and the overlap with Rigaku's film tools

Fiscal years: Nova and Rigaku use the calendar year; Onto's fiscal year ends near 31 Dec (FY2025 ended 3 Jan 2026). Evidence ids refer to `parts/XR.csv`. Earnings-call and conference transcripts belong to the main agent. The only call items used here come from the third-party Q3 2026 transcript (XR-007, XR-008, both [S]).

## (a) Nova and X-ray

- **Products.** Nova's only X-ray products are the VeraFlex in-line XPS tools. Each carries an optional low-energy XRF channel that measures at the same time as the XPS, from the same X-ray source. The models are VeraFlex III LE-XF, III+ XF (described as fourth-generation) and IV LE-XRF [F] XR-002, XR-004, XR-006. Nova does not sell XRF as a stand-alone tool [F] XR-006; [S] XR-007.
- **Leadership claims.** Nova says it has the largest installed base of automated XPS/XRF systems and calls VeraFlex the industry standard for HKMG [C] XR-003. It says VeraFlex IV launched in 2021 [C] XR-005.
- **Acquisition.** XPS came to Nova with ReVera (acquired April 2015, merged into Nova's US subsidiary Dec 2017) [F] XR-001. The price paid is not in the 20-F text read (see gaps).
- **Programmes and partnerships.** Nova has published in-line XPS/XRF work with IBM Research and GlobalFoundries [F] XR-012, XR-013, XR-033, XR-034. Since 2016 it has offered a hybrid that combines X-ray film parameters with Optical CD geometry [F] XR-011. It was applied to Cu voids (2019) and to SiGe indent (2026) [F] XR-012, XR-013. These hybrids use film signals (XPS/XRF), not X-ray CD.
- **X-ray CD (SAXS).** We found no Nova X-ray CD product, development programme, partnership or acquisition [I] XR-018 (Medium).
  - Nova's hybrid-metrology web page lists OCD, SEM and AFM only [F] XR-010.
  - The only X-ray-CD-type asset is a patent family on X-ray reflectance scatterometry for periodic structures, which came from ReVera. One patent was granted in Jan 2024 and a continuation was published in Mar 2026 [F] XR-014. This is intellectual property, not a disclosed product.
- **Competitors as Nova frames them.** The 20-F FY2025 names Onto and KLA as main competitors and does not mention Rigaku [F] XR-016. On the Q3 2026 call the CEO said the new competition he expects (around 2H 2027) is "centered around XPS only" [S] XR-008.

## (b) Onto-Rigaku alliance (primary documents) and Nova statements since April 2026

| Date | Event | Evidence |
|---|---|---|
| May 2025 | Rigaku and Onto start joint development of hybrid metrology: Rigaku CD-SAXS plus Onto analytics software | [F] XR-020 |
| 13, 20, 21 Apr 2026 | Rigaku board resolution, CEO decision, then the agreement is signed. Onto is to buy 61,123,436 shares (27.0%) from Atom (Carlyle); Atom drops from 42.03% to 15.03%. Onto may nominate one director (CEO Plisinski); a standstill applies | [F] XR-019 |
| 20 Apr 2026 (US) | Onto release: about $710M. Onto's AiDiffract software combined with Rigaku CD-SAXS "already selected by two key customers", with systems delivered for V-NAND/DRAM. External analysts (TechInsights) put the market above $1B within five years | [C] XR-022, XR-023; [C] XR-024 |
| 10 Aug 2026 | Deal closes: JPY 113,078,356,600 (about US$720M). Onto carries the stake at fair value and does not consolidate Rigaku | [F] XR-025 |
| 1 Oct 2026 | Onto moves the shares to its subsidiary Onto Innovation Japan | [F] XR-025 (note) |
| 1Q FY12/27 (Jan-Mar 2027) | Rigaku targets: CD-SAXS-OCD "Hybrid Engine" on memory mass-production lines; first GI-SAXS logic unit, with Onto software on board | [C] XR-026, XR-027 |

**Stated targets.** Rigaku targets a SAM of at least $300M by 2030 [C] XR-021. For hybrid metrology it targets a $100mn SAM in 2030 with more than 50% share [C] XR-026. Rigaku says the work began with OCD-based software on its T-SAXS tool, now in memory mass-production lines [C] XR-027.

**Nova statements since April 2026, outside the earnings calls.** We found none on the Onto-Rigaku alliance or on hybrid X-ray CD plus OCD. We checked:
- the Nova press releases of Apr-Nov 2026 (the Q1-Q3 2026 results releases have no X-ray terms);
- two Nova blog posts of 22 Apr 2026, which cover XPS with complementary XRF, Raman and SIMS only [F] XR-015;
- the GlobalFoundries-Nova ASMC 2026 paper, which is about XPS throughput [F] XR-033;
- Globes' interview with CEO Gaby Waisman (30 Jun 2026), which does not mention X-ray, XPS or Rigaku.

## (c) Q4 overlap: Nova's XPS, SIMS and Raman tools against XRF, XRD and XRR

| Measurement | Nova tool | X-ray tool(s) | Competing or complementary | Socket holder per non-vendor source | Evidence ids |
|---|---|---|---|---|---|
| SiGe/Si nanosheet superlattice: Ge %, sheet thickness, strain | Elipson (Raman); Metrion (SIMS); VeraFlex XPS/XRF on structures | Rigaku XTRAIA XD (HR-XRD); Bruker JVX7300 (HR-XRD) | Mostly complementary: HR-XRD on unpatterned targets after epitaxy, and as reference; Raman, XPS and SIMS in-die. They compete at the post-epi monitor step | None names a holder. At IBM, Bruker in-line HR-XRD was the reference for Nova Raman. Trade press: Raman fits HVM; HR-XRD takes hours per wafer. Rigaku's "POR at a majority" is a vendor claim | XR-029, XR-035, XR-036, XR-041, XR-045 |
| Source/drain epi composition and dopant (SiGeB) | VeraFlex XPS; Metrion SIMS | XRF/XRD measured on pads (e.g. Rigaku MF, XD) | Competing (same measurand) | GlobalFoundries (paper co-authored with Nova): VeraFlex XPS is the legacy POR for SiGeB at a GF high-volume fab. GF lists SIMS, XRD, XRF and XPS as the usual pad methods | XR-033, XR-034, XR-009 |
| HKMG and dipole ultra-thin films (high-k, Al-O dipole) | VeraFlex XPS + LE-XRF | Rigaku MF-3400 (XRF/XRD); ONYX 3200 (light-element XRF) | Competing. Rigaku markets ONYX explicitly against XPS | No non-vendor source found that names the holder. IRDS: XPS is widely used for thin films | XR-003, XR-028, XR-030, XR-037, XR-044 |
| Barrier, liner and metal films | VeraFlex XPS/LE-XRF (BEOL work with IBM) | XRF, XRR (e.g. Rigaku WaferX/MF) | Competing at technique level | IRDS lists acoustic methods, XRR and XRF for a barrier under Cu seed; XPS is not listed; no vendor named | XR-012, XR-038 |
| Shape of high-aspect-ratio memory structures (3D NAND holes, DRAM deep trench) | Nova OCD (integrated and stand-alone) | Rigaku T-SAXS (CD-3200T/3300T) running Onto OCD-based software | Competes for dimensional sockets; complementary inside the Onto-Rigaku hybrid | IRDS: in-line CD-SAXS tools recently introduced; holder not named | XR-022, XR-026, XR-027, XR-039, XR-040, XR-046 |
| 3D shape of GAA/CFET logic structures | Nova OCD (incl. Prism) | Rigaku GI-SAXS CD-3200G with Onto software (first unit 1Q FY2027) | Future competition with, or add-on to, OCD | IRDS: in-line SAXS for logic still needs brighter X-ray sources | XR-027, XR-039, XR-042 |
| 3D DRAM Si/SiGe stacks | Not mapped to this step in the Nova sources read | Rigaku XD (HR-XRD); CD-3300T | Not established | No non-vendor source found | XR-029 |

## (d) Handoff: where Nova's tools compete with or complement Rigaku and Onto

Nova names Onto Innovation and KLA, not Rigaku, as its main competitors in CD, thin-film and chemical metrology [F] XR-016. In optical CD, where Nova sells both integrated and stand-alone platforms [F] XR-002, Onto is the direct rival: Onto reports that its Atlas G6 OCD was selected by a second logic customer for gate-all-around metrology in Q1 2026 [C] XR-042. In materials and film metrology, Nova's VeraFlex (XPS plus LE-XRF) competes with Rigaku's XRF/XRD and light-element XRF tools for HKMG and dipole films; Rigaku markets ONYX 3200 explicitly against XPS and targets more than 70% of a $200mn HKMG market [C] XR-028, XR-030, while Nova claims the largest installed base of automated XPS/XRF [C] XR-003. No non-vendor source found names who holds the production socket there [I] XR-044 (Medium). Citing Yole, Rigaku claims the No.1 share of X-ray metrology (39.4%) and of film and materials metrology (20.6%) in 2025, with competitors left anonymous [C] XR-031, XR-032. In packaging, Nova's 20-F names Merck and Camtek as its direct competitors [F] XR-017, while Onto describes its packaging lines as inspection and lithography [F] XR-043. The documented packaging overlap with Onto is therefore limited [I] (inputs XR-017, XR-043; Medium: neither company publishes a product-by-product comparison). Nova's tools also work alongside X-ray tools: X-ray diffraction was the reference for Nova's Raman and XPS in IBM studies [F] XR-035, XR-036; GlobalFoundries runs VeraFlex XPS as the process of record for SiGeB epi [F] XR-033; and Nova has combined X-ray film signals with OCD since 2016 [F] XR-011, XR-013. The Onto-Rigaku hybrid instead feeds CD-SAXS shape data into OCD, first on memory lines (target 1Q FY12/27) [C] XR-026. Its main threat to Nova is therefore in dimensional OCD sockets rather than in XPS [I] XR-046 (Low). Onto now owns 27% of Rigaku and nominates a director [F] XR-019, XR-025. Nova's main OCD rival is now tied to the X-ray film vendor that competes with VeraFlex [I] XR-047 (Medium).

## (e) Gaps

- NOT DISCLOSED (read: Nova 20-F FY2023 notes 1 and 7, 20-F FY2024 note 7, 20-F FY2025 Item 4A) - price paid for ReVera (April 2015).
- NOT DISCLOSED (read: Nova 20-F FY2025 Items 3D and 4B; Nova website product sitemap and Hybrid Metrology, XPS and XRF pages; Investor Day 2025 deck pp.39-60) - any Nova X-ray CD (SAXS or XRS) product, development programme, partnership or acquisition.
- NOT DISCLOSED (read: Nova 20-F FY2025 Item 3D risk factors and Item 4B Competition) - Rigaku as a named competitor, and any Nova assessment of the Onto-Rigaku alliance.
- NOT DISCLOSED (read: Nova press-release index and sitemap titles Apr-Nov 2026; Q1, Q2 and Q3 2026 results releases; Nova blogs of 22 Apr 2026; Globes interview with CEO Gaby Waisman, 30 Jun 2026) - any Nova statement since April 2026 on the Onto-Rigaku alliance or on hybrid X-ray CD plus optical CD.
- NOT DISCLOSED (read: Rigaku FY2026 2Q earnings presentation p.13) - names of the anonymised competitors (Company A-E) in the Yole X-ray and film-metrology share charts, and so Nova's share.
- NOT DISCLOSED (read: Onto press release of 20 Apr 2026) - identity of the two key customers that selected AiDiffract plus CD-SAXS.
- NOT DISCLOSED (read: Rigaku FY2026 3Q presentation p.11, 3Q speech and Q&A pp.10-11, FY2026 2Q presentation p.14, FY2025 presentation pp.17-18) - names of customers using XTRAIA XD as POR, or MF-3400, ONYX 3200 or T-SAXS in mass production.
- NOT RETRIEVED (tried: nothing; sec.gov is blocked in this session) - Onto 10-K FY2025 competition section, 2026 10-Qs and 8-K exhibits (Rigaku share purchase agreement, financing).
- NOT RETRIEVED (tried: Onto PDFs on s24.q4cdn.com, which gave the releases only; investors.ontoinnovation.com not tried because the lead says it refuses scripts) - Onto 2026 earnings presentation slides.
- NOT RETRIEVED (tried: the spiedigitallibrary.org PDF link, which returned a non-PDF page) - IBM Research review "Review of nanosheet metrology opportunities for technology readiness" (JM3 21(2) 021206, 2022).
- NOT RETRIEVED (tried: patents.justia.com assignee listing, HTTP 403) - full list of Nova's X-ray patents; only the XRS family was checked, via Google Patents.
- NOT RETRIEVED (tried: web search found no public copy; paywalled) - Yole "WFE Market Monitor 2026/Q2" and the TechInsights market estimate cited by Rigaku and Onto.
- NOT RETRIEVED (tried: web searches for chipmaker, imec and IRDS documents naming the in-line tool of record for HKMG/dipole films and 3D DRAM Si/SiGe stacks; the imec JAP 2025 paper on 120 Si/SiGe bilayers was found but not fetched) - a non-vendor source naming the production socket holder for HKMG/dipole and 3D DRAM stack metrology.
