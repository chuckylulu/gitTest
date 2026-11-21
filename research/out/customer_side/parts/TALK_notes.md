# TALK module notes: chipmakers' non-paper statements on inspecting HBM stacks and hybrid-bonded interfaces (Jan 2025 to 21 Nov 2026)

Files: evidence `research/out/customer_side/parts/TALK.csv` (61 rows: 28 [F], 5 [C], 25 [S], 3 [I]; quote_check: 58 of 58 quotes FOUND), table `research/out/customer_side/parts/TALK_table.csv` (43 rows), sources in `research/sources/customer_side/`.

Method: discovery with WebSearch and Firecrawl search (English, Korean, Chinese). I also listed the WordPress REST search on news.skhynix.com and news.skhynix.co.kr; those listings went to the scratchpad only and are not cited. Firecrawl search credits ran out for about 10 minutes mid-run and then came back. Every document cited was saved with fetch.py.

## 1. Findings

**Overall.** In the non-paper material I could open, none of the seven names a production method for post-bond void or bond-overlay inspection of HBM or hybrid-bonded stacks in its own words (TALK-055, [I], Medium). The only claim of a method on a production line is Samsung with picosecond laser-acoustic tools, and it comes from trade press citing industry sources, not from Samsung (TALK-024 to TALK-029). When chipmakers do speak, they describe needs, and three needs recur:
- particles and surface condition before bonding;
- warpage at wafer and chip level;
- detection of buried or lower-interface voids (TALK-056, [I]).

**SK hynix**
- Its own 2025-26 statements are about fab-wide AI rather than physical inspection of HBM stacks (TALK-057, [I]):
  - an AI defect-image analysis system that "drastically reduced the time required for defect analysis" (TALK-001);
  - AI virtual metrology that screens "quality anomalies across all wafers without increasing the total production time" (TALK-002), in an article framed around HBM smart factories. The 31% productivity and 21% yield gains are company claims (TALK-003).
- It names its virtual-metrology vendor itself: Gauss Labs' "Panoptes VM", used "in its production lines since 2022". This is front-end lithography overlay, not HBM stacking (TALK-004).
- Its Korean newsroom describes the DMI function (Defect analysis, Metrology, Inspection). Metrology covers nm-scale line width, thickness and alignment in vertical stacking (TALK-005). Inspection uses optical and electron-microscope tools at each process step (TALK-006). DMI works across development and mass production (TALK-007).
- An SK hynix metrology engineer states a limit: areas that used to be measurable are increasingly hard to measure accurately (TALK-008).
- SK hynix's supplier co-development programme is the clearest sign of where it wants new inspection tools. The chipmaker names both vendors itself:
  - NexSensor (넥센서), selected in Aug 2025 to develop wafer and chip warpage measurement equipment (TALK-009). SK hynix calls warpage measurement and control essential (TALK-010) and expects the work to reduce its reliance on overseas tools (TALK-011, [C]).
  - Cobis Technology, whose "hybrid wafer metrology equipment" got an interim review (TALK-012). The term is undefined; do not read it as "hybrid-bonded wafers".
- SEMICON Korea 2026: an SK hynix DRAM engineer presented on overlay control for CMP. The talk content beyond its title was not published (TALK-013).
- SK hynix's own Hybrid Bonding Tech Note (Aug 2026) says die-to-wafer hybrid bonding for HBM is "progressing toward commercialization" (TALK-014). It calls current TCB unsuitable below about 7 µm pitch (TALK-015) and names no inspection method.
- Advanced MR-MUF is said to allow thinner stacking "without warpage" (TALK-016, [C]). No measurement is given.
- Press (TrendForce, citing Korean media) reports an HBM4 system-level/SiP test tool, co-developed with partners, that passed SK hynix's internal qualification (TALK-017, [S]).

**Samsung**
- The richest chipmaker-authored item is the VLSI Symposium 2025 Workshop 9 talk "Metrology and Inspection Challenges in Hybrid Bonding..." (Suyoung Lee, Samsung). The abstract says:
  - metrology must ensure "precise alignment, large area 3-dimensional topology and warpage metrology at both wafer level and chip level" (TALK-018);
  - as stack layers increase, "nanoscale defects and void detection at the lower interface" is needed (TALK-019);
  - optical inspection, X-ray microscopy, AFM and acoustic microscopy, plus AI defect classification, "are examined" (TALK-020).
  It gives no production status, throughput or resolution. This is abstract-only evidence.
- Samsung's Su Jin Ahn, on an ECTC 2025 special-session panel (a panel, not a paper), said:
  - the many process steps leave particles on the bonding surface (TALK-030);
  - advanced metrology/inspection tools and methods are needed (TALK-031, [S]).
- Samsung VP Choi Won-kyung (Nano Korea 2026) named particle minimisation and precise warpage control as key to commercialising hybrid bonding (TALK-032, [S]).
- Samsung's HBM page says HCB is "sensitive to even microscopic particles or vibrations" (TALK-033). It says Samsung is "preparing to adopt" HCB (TALK-034, [C]).
- TheElec (31 Mar 2026, industry sources) reports:
  - Samsung has begun introducing hybrid-bonding inspection equipment;
  - Onto Innovation picosecond laser-ultrasound systems are under validation on mass-production lines through a joint development programme (TALK-024, TALK-025), and the technique can also measure overlay (TALK-026);
  - Samsung is in talks or joint development with ultrasound and X-ray vendors (TALK-027) for both HBM TSVs and hybrid-bonding interfaces (TALK-028);
  - qualification takes about 6 months (TALK-029).
  All of this is [S]. The vendor is named by the press, not by Samsung.

**Micron**
- CTO Scott DeBoer (ITF World 2025, quoted by Semiconductor Engineering):
  - Micron uses daisy chains in HBM development "to evaluate thousands of connections at once" (TALK-035);
  - a resistance shift reveals "voids or bond degradation even before visual inspection sees it" (TALK-036);
  - the industry lacks standard hybrid-bonding test structures, so Micron invents its own test vehicles (TALK-037). All [S].
- Micron's Dec 2025 blog describes AI-enhanced imaging and classification in testing and inspection (TALK-038), applied across "front end, assembly and test" (TALK-039). It also cites deep-learning AI-ADC (TALK-041) and 100 million wafer images a week (TALK-040, [C]). It is not HBM-specific.
- VLSI 2025 Workshop 9 talk by Micron's Charles Wang (abstract): it covers challenges in "Processing, Measuring and Testing" C2W-bonded memory stacks. No method is named (TALK-021).
- SEMICON Taiwan 2025 keynote by Chang Yu-lin (Micron Taiwan VP, advanced packaging & test operations):
  - pre-applied NCF lets Micron expel bubbles, i.e. voids are controlled by the process (TALK-042);
  - warpage, cracks and particles are amplified in stacking (TALK-043). [S]

**Intel**
- Intel organised VLSI 2025 Workshop 9. Its description lists the needed metrology: "ultra-dense sampling highthroughput surface topography, real-time defect analyses, subsurface void detection" (TALK-022).
- The organiser bio says Haris Khan Niazi leads Intel's hybrid-bonding and 3D HI metrology and inspection (TALK-023).
- Intel Foundry Direct Connect 2025/2026 material and the Foveros Direct tech brief sit on hosts that refuse (see gaps).
- An Intel Fellow's deck (Tadayon: "metrologies to detect defects at all levels – surface and buried") is dated Apr 2024. It is out-of-period context only and not used in the table (TALK-054).

**TSMC and ASE (press only; primary sites refuse)**
- TSMC's only in-period technical talk on this topic that I found is the SEMICON Taiwan 2026 keynote by Zhihua Zou (TSMC), "Challenges and Opportunities for Metrology and Inspection of Advanced Packaging" (Advanced Inspection and Metrology Forum, Sep 2026). The XR module found it first; my rows reuse its saved files.
  - Per DIGITIMES (teaser only), TSMC called for HBM and DRAM designs to be more compatible with X-ray inspection (TALK-058). The stated reasons are that buried defects are harder to detect and radiation exposure is a concern (TALK-059).
  - Per WindowsForum, the public abstract lists "DRAM/HBM damage concern by X-ray" (TALK-060). It names collaboration with HBM and equipment vendors and "design for metrology" as opportunities (TALK-061).
  - The abstract itself is NOT RETRIEVED. No method type, tool, status or dose is given. Dose analysis belongs to XR (XR-013 to XR-018).
- At the 3DICAMA launch on 9 Sep 2025, TSMC VP Jun He said:
  - in 3D/3.5D packaging every small defect is amplified;
  - automated handling, "第一時間偵測" (immediate detection) and cross-company real-time support must be baseline (TALK-044);
  - the alliance should align tool capability, metrology flows and data formats (TALK-045).
- ASE SVP Hung Song-jing said in-situ inspection plus AI must move onto the line (TALK-046).
- Commercial Times paraphrases both companies as saying in-process measurement demand has risen markedly (TALK-047).
- At its June 2026 AGM, ASE named "high-efficiency image anomaly-detection AI" as one of three focus areas (TALK-048).
- No method, tool, status or limit is given in any of these. All [S].

**Amkor**
- Amkor's SEMICON West 2025 poster abstract covers the impact of hybrid bonding and micro-pad technologies on wafer-level test (TALK-049).
- Its VP Omer Dossani says intermediate test during HBM assembly is becoming critical (TALK-050, [S]).
- Amkor's IMAPS 2025 talk/proceedings on a 2.5D CoW vehicle with mimic HBMs:
  - SAT at thermal-cycling read-points showed "signs of cracking or delamination" (TALK-051), and destructive cross-sections were needed to confirm the underfill crack (TALK-052);
  - package warpage was measured at 25, 125 and 260 °C, method not named (TALK-053).

## 2. Gaps

- NOT DISCLOSED (read: SK hynix Newsroom, [Tech Note] Hybrid Bonding, 2026-08-25, full text): any inspection or metrology method for hybrid-bonded HBM.
- NOT DISCLOSED (read: SK hynix Newsroom, HBM4 development completion, 2025-09-12, full text): inspection or test method for HBM4 / Advanced MR-MUF.
- NOT DISCLOSED (read: SK hynix Newsroom, 12-layer HBM4E samples, 2026-06-18, full text): inspection or test method.
- NOT DISCLOSED (read: SK hynix Newsroom (KR), Technology Innovation Companies 8th cohort, 2025-08-25): measurement principle of the NexSensor warpage tool and of the Cobis "hybrid wafer" metrology tool.
- NOT DISCLOSED (read: SK hynix Newsroom, SEMICON Korea 2026, 2026-02-12): content of the STS overlay/CMP talk beyond its title.
- NOT DISCLOSED (read: Samsung Newsroom, "Samsung ships industry-first commercial HBM4", 2026-02-12): bonding method and any inspection method.
- NOT DISCLOSED (read: Samsung Semiconductor HBM3E product page, FAQ): inspection method for HCB; dates of adoption.
- NOT DISCLOSED (read: VLSI 2025 Workshop 9 program page, Samsung and Micron abstracts): production status, throughput, resolution, sample damage.
- NOT DISCLOSED (read: Micron blog "Smart manufacturing at Micron", 2025-12-09): HBM-specific inspection steps or tools.
- NOT DISCLOSED (read: Amkor IMAPS 2025 paper "Module Stress Reduction for 2.5D TSV-based Heterogeneous Package", pp1-5): warpage measurement method/tool; SAT tool vendor and resolution.
- NOT DISCLOSED (read: Amkor blog "2026 Investor Day", 2026-05-29 and "ECTC 2026", 2026-06-05): any inspection or metrology content.
- NOT RETRIEVED (tried: none; host semicontaiwan.org refuses scripted access per brief): https://semicontaiwan.org/en/node/20171 (Micron keynote "AI-Powered Smart Quality Ecosystem: Manufacturing Next-Generation AI Memory", Jack Lee, Micron).
- NOT RETRIEVED (tried: none; semicontaiwan.org refuses): https://www.semicontaiwan.org/en/node/18506 (TSMC keynote abstract, Zhihua Zou, SEMICON Taiwan 2026; also flagged by XR).
- NOT RETRIEVED (tried: none; semicontaiwan.org refuses): https://www.semicontaiwan.org/zh/3DIC_2026 (3DIC Global Summit, 1 Sep 2026, TSMC/ASE talks).
- NOT RETRIEVED (tried: none; semi.org refuses): https://www.semi.org/zh/SEMICON-Taiwan-2025/3DICAMA and https://www.semi.org/sites/semi.org/files/2025-11/01%20Ilan%20intro%20and%20Standards.pdf (3DICAMA "Metrology & Inspection" working group led by TSMC and ASE).
- NOT RETRIEVED (tried: none; semi.org refuses): https://www.semi.org/en/connect/events/advanced-packaging-summit-2025 (Suwon, 16 Jul 2025; D2W M&I session), https://www.semi.org/en/event/are-we-there-yet-metrology-and-inspection-angstrom-level-manufacturing, https://www.semi.org/en/imaging-across-assembly-and-test-enabling-manufacturable-complexity.
- NOT RETRIEVED (tried: fetch.py, HTTP 403): https://www.semi.org.cn/site/semi/article/59e65455dbe84bc49f4acdd17994d2c5.html (SEMICON China 2026 heterogeneous-integration conference write-up; a female speaker on hybrid-bonding yield and cleanliness, affiliation unknown).
- NOT RETRIEVED (tried: none; investor.tsmc.com refuses): https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20Annual%20Report.E.pdf (section 5.3.6 Quality and Reliability, advanced packaging).
- NOT RETRIEVED (tried: none; pr.tsmc.com refuses): https://pr.tsmc.com/static/campaign/2025March/tsmc_na/index.html (TSMC 2025 Technology Symposium); 2026 symposium pages likewise.
- NOT RETRIEVED (tried: none; www.intel.com refuses): https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-11/foveros-direct-3d-tech-brief.pdf and https://www.intel.com/content/www/us/en/newsroom/press-hub/press-kit/corporate/intel-foundry-direct-connect-2025.html.
- NOT RETRIEVED (tried: fetch.py, HTTP 403): https://newsroom.intel.com/intel-foundry/intel-foundry-gathers-customers-partners-outlines-priorities.
- NOT RETRIEVED (tried: WebFetch of intc.com IR calendar; no Foundry Direct Connect presentation listed): Intel Foundry Direct Connect 2025/2026 slide decks.
- NOT RETRIEVED (tried: fetch.py; page body behind member login): https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=767040 and id=764808 (TSMC Jun He, Aug/Sep 2026), https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=767019 (ASE Hung Song-jing on manufacturing bottlenecks).
- NOT RETRIEVED (tried: Amkor blog only; ir.amkor.com refuses per brief): Amkor 2026 Investor Day presentation (URL on ir.amkor.com not identified).
- NOT RETRIEVED (tried: none; investors.micron.com refuses): https://investors.micron.com/news/press-release/2025/Micron-Breaks-Ground-on-New-HBM-Advanced-Packaging-Facility-in-Singapore-01-08-2025/default.aspx.
- NOT RETRIEVED (tried: IEEE.tv page; video members-only, speaker not shown): https://ieeetv.ieee.org/repp/metrology-challenges-in-advanced-packaging-focus-on-die-to-die-and-die-to-wafer-bonding.
- NOT RETRIEVED (tried: none; semiconkorea.org refuses): SEMICON Korea 2025/2026 STS abstracts for the SK hynix and Samsung talks.
- NOT RETRIEVED (tried: web searches in EN/KR/ZH): Samsung Foundry Forum / SAFE Forum 2025 material on inspection; none surfaced.
- NOT RETRIEVED (tried: web searches): inspection/metrology content in SK hynix and Samsung 2025-26 IR presentations. No lead was found and the decks were not downloaded.
- NOT RETRIEVED (tried: WebFetch, timeout): news.samsung.com site search for hybrid bonding.

## 3. Premise problems

1. The Korean SK hynix newsroom is on `news.skhynix.co.kr`, not `news.skhynix.com`. fetch.py (honest UA) was accepted there, but WebFetch got HTTP 403.
2. Two more hosts refuse scripted access and are not in the brief's list: `newsroom.intel.com` (403) and `www.semi.org.cn` (403).
3. The intc.com IR calendar does not carry Foundry Direct Connect material; Intel puts it on intel.com and newsroom.intel.com, both of which refuse.
4. The prompt implies Samsung hybrid bonding in HBM4. Samsung's own texts do not say so:
   - the HBM4 shipment release (Feb 2026) names no bonding method;
   - the HBM page says Samsung is "preparing to adopt" HCB (TALK-034);
   - TheElec says the industry expects HCB from HBM4E 16+ layers.
5. For SK hynix, its own Tech Note (Aug 2026) puts hybrid-bonded HBM as "progressing toward commercialization", not in production (TALK-014).
6. I could not confirm "intelligent packaging fab (AP7/AP8)" as a TSMC term in any document I could retrieve. My TSMC rows rest on press accounts only: 3DICAMA remarks and the SEMICON Taiwan 2026 keynote, which XR found.
7. The VLSI 2025 Workshop 9 page gives the Samsung speaker as "Suyoung Lee" in the talk line but "Suyoung Yang" in the bio heading. Search snippets also gave "Yusin Yang". I used the page's talk line.
8. Tool problem for the merge step: `research/tools/merge_parts.py` globs every `parts/*.csv`, so it will pick up `TALK_table.csv`. That file has a different header and no `id` column. Exclude it, or merge only `TALK.csv`, when building evidence.csv. I did not edit the tool.

## 4. Unverified leads

- semicontaiwan.org/en/node/20171. The snippet says the Micron keynote describes three "AI defense lines", including the MicronCraft 3D simulation platform with a claimed ~20x cut in root-cause time. This is the most detailed Micron quality/inspection talk found, but it is not retrieved.
- SEMI HiCONNECTS deck (semi.org, Nov 2025). The snippet says the 3DICAMA working group "Metrology & Inspection: Defect detection & yield" is led by Jun He (TSMC) and Mike Hung (ASE).
- mirrormedia/SETN, 1 Sep 2026: TSMC will launch a "physical verification platform" (3DIC Global Summit 2026). Not read.
- I-Connect007 ECTC 2025 write-up (saved, `2025-06-26_iconnect007_article-ectc-2025-review.html`): Intel's Kumar Abhishek Singh on CPO named foreign particles, misalignment and cracks as packaging challenges. This is CPO, not HBM/HB, so it was not tabled.
- ASE plus three universities, 18 packaging research projects (uanalyze, 2026; saved): SiP warpage evaluation model and a high-warpage dicing method "introduced into actual products". This is simulation and process work, not measurement.
- `2025-11-06_darpa_ngmm-summit-3d-hybrid-bonding.pdf` (TechSearch International, not a chipmaker): says post-bond overlay sampling is not accurate and current methods are too slow for die overlay.
- Out-of-period context:
  - ZDNet Korea, 27 Aug 2024: SK hynix VP Moon Ki-il on CMP and particle problems for HBM hybrid bonding.
  - ETNews/KMEPS 2024: SK hynix's Kangwook Lee at ISMP-IRSP 2024.
- Leads for other modules, one line each:
  - Supplier awards: TheElec headline "SEC Wins 5.8 Billion Won HBM Inspection Order From Micron" (sidebar in `2026-03-31_thelec_...`).
  - Sampling trend: cs.com.cn reports the KLA 2026 Investor Day saying inspection steps grow about 30% per advanced-logic node and extend to buried defects.
  - Vendor claims: Nextin "Iris3" IR inspection for non-metal-area voids in W2W/C2W bonding (greened.kr, SEMICON Korea 2026); Onto EchoScan voids ≥1 µm (3D InCites); Semiconductor Engineering cites acoustic void sensitivity ≥10 µm with water-immersion contamination risk. Vendor statements, not chipmaker.
  - X-ray dose: no statement found.

## Papers seen (not tabled; for the paper-inventory module)

- SK hynix (Lee Sangyeop, Yoon Gwangmin, Lee Sangyup; with Georgia Tech), "Industry's First In-line Chip Warpage Measurement Methods for HBM Manufacturing Using UV-Induced Delamination and a Flux-based Support Layer", JSTS vol. 25 no. 5 (2025), DOI 10.5573/JSTS.2025.25.5.585. JSTS is not IEEE/SPIE. The abstract says the non-destructive method "has been transferred to measurement equipment suppliers and ... commercialized as a LSCW measurement solution". Saved: `research/sources/customer_side/2026-11-21_jsts_paper-hbm-chip-warpage-thin-wafer.html`. This is a strong lead for wafer shape.
- SK hynix and Gauss Labs, SPIE Advanced Lithography + Patterning 2026: "A Virtual Metrology-Driven Tool-to-Tool Matching: Toward Early Anomaly Detection and Diagnosis" and "GRACE: A Gradient-Based Model-Agnostic Explainability Framework for Photolithography Overlay Virtual Metrology". DOIs were not looked up (titles from the SK hynix newsroom, 2026-02-19).
- Samsung, ISSCC 2026 paper on 4F² VCT DRAM made with wafer-to-wafer hybrid bonding (mentioned by TheElec 2026-03-31). Title and DOI not looked up.
- Not a chipmaker, for exclusion: R. Chang et al. (A*STAR), ECTC 2025, DOI 10.1109/ECTC51687.2025.00161 (HBM bump visual inspection with AI).
