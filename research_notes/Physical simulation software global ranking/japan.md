# Japan: physical-simulation software vendors, trust boundary, national computing and entry points (as of 12 Nov 2026)

**Summary for the report writer.**
1. Japan is mainly a channel market for foreign solvers. Yano put Japan's mechanical CAE market at JPY 104.2bn for 2024 (forecast, published Mar 2025). Revenue flows largely through distributors and integrators: Cybernet (main Ansys channel; JPY 25.4bn revenue in 2025; private, under KKR via Fuji Soft), IDAJ, Dentsu Soken and others. No public source splits the market between domestic and foreign vendors.
2. Japanese-owned solvers of note are niche and mostly not investable: JMAG (motor electromagnetics; JSOL, a 50/50 NTT DATA and SMFG/JRI venture with JPY 61.3bn revenue in FY3/2026), Matlantis (universal machine-learned interatomic potential PFP; "150+" organisations claimed; owned by Preferred Networks, ENEOS, Mitsubishi Corp), Particleworks (GPU particle CFD; Prometech, private), Femtet (Murata Software), AdvanceSoft. Software Cradle's CFD is Japanese in origin but now sits inside Cadence (Hexagon D&E deal closed Feb 2026). None has third-party share data. In a global ranking, JMAG and Matlantis fit at most as niche leaders in one physics; the rest are channels or small.
3. Listed names are small: Zuken (PCB and harness EDA with SI/PI analysis; JPY 114bn; net cash JPY 36.6bn; guidance raised 9 Nov 2026), KKE Holdings (structural, seismic and CAE consulting plus resale; JPY 30bn), JEDAT (IC layout EDA; JPY 4bn; 51% owned by ARGO GRAPHICS), Fixstars (acceleration engineering services; JPY 55bn), HPC Systems (HPC hardware integrator; JPY 11bn), Sakura Internet (GPU cloud; JPY 132bn). Labour hours, resale and hardware dominate; recurring own-software revenue is clearest at Zuken (maintenance about 42% of sales).
4. Trust boundary: Japan's own "judges" are domestic and narrow: minister-certified structural calculation programs under Building Standards Act Art. 20 (post-2007 certifications only for SEIN La CREA, ABUS-5, BUILD.一貫V, ASCAL-EX), ClassNK's own free PrimeShip-HULL for CSR ships, and NRA case-by-case review of safety-analysis codes. Vehicle type approval moved toward more physical checking after the 2024 certification-fraud cases; JAXA's certification by analysis is at guideline stage; PMDA has expert reports, not binding rules.
5. FugakuNEXT (RIKEN; Fujitsu MONAKA-X CPUs; NVIDIA GPUs; around 2030; 40 MW or less): FP64 about 2.65 EFLOPS (about 4.8x Fugaku) versus 600+ EFLOPS FP8 with sparsity; "zettascale" refers to low-precision AI peak, not FP64. RIKEN's 100x application target relies on surrogates, mixed precision and FP64 emulation. Double-precision codes get only about 5x more hardware, and GPU porting is unavoidable (JMA is porting its weather models).
6. Coverage is thin for private firms, third-party share data (paid Yano reports) and independent accuracy benchmarks; WebSearch, Firecrawl, Exa and Consensus budgets all ran out during this pass.

## 1. Map of the field: who matters, ownership, size, what they sell

### Takeaway
The field splits into (a) a few own-solver developers, nearly all private or captive; (b) large distributors and integrators of Ansys, Siemens, Dassault, Cadence/Hexagon and Gamma codes; (c) small listed EDA, HPC and engineering-service firms; (d) public bodies that write their own codes (JMA, JAXA, RIKEN). Take-privates since 2024 removed Cybernet, Fuji Soft, NTT DATA and SCSK from the market.

### Cited Findings
General engineering simulation
- Cybernet Systems: est. 1985; revenue JPY 25.398bn (year to 31 Dec 2025); 624 staff (1 Jan 2026) — [Cybernet overview](https://www.cybernet.co.jp/company/about/overview/). Delisted Feb 2024 after Fuji Soft's tender offer — [history](https://www.cybernet.co.jp/company/about/history/). KKR's FK Co. took Fuji Soft private (second tender ended 19 Feb 2025; delisted 16 May 2025) — [Nihon M&A Center, 20 Feb 2025](https://www.nihon-ma.co.jp/news/20250220_9749-13/). Sells Ansys (Mechanical, Fluent, HFSS, Maxwell, Lumerical, Zemax), owns Maplesoft, Noesis and Sigmetrix, plus own MBD/MBSE services, CAE cloud and medical imaging — [Cybernet site](https://www.cybernet.co.jp/company/about/). Claims six Ansys Partner of the Year awards for 2025 and sole Japanese "Ansys Elite Channel" status (company claim, unconfirmed) — [PR Times](https://prtimes.jp/main/html/rd/p/000000528.000004714.html).
- JSOL (JMAG, J-OCTA): est. 2006; NTT DATA 50%, Japan Research Institute (SMFG) 50%; 1,418 staff (Apr 2026) — [JSOL outline](https://www.jsol.co.jp/company/outline.html). FY3/2026 (Apr 2025-Mar 2026, notice dated 12 Jun 2026): revenue JPY 61,310m, operating profit JPY 8,515m (13.9%), net JPY 6,612m; merchandise sales only JPY 1,002m; JMAG not broken out — [JSOL 決算公告](https://www.jsol.co.jp/company/sn2u4r000000086z-att/202606.pdf). JMAG dates from 1983 and is used mainly for motors in automotive (sponsored article, company claim) — [Toyo Keizai AD, 24 Aug 2023](https://toyokeizai.net/articles/-/688351). JMAG-Designer 25.2 released 7 Oct 2026; FMI export of surrogate models; user conferences in Detroit (Jun 2026, with distributor POWERSYS) and Tokyo (9-10 Dec 2026) — [JMAG site](https://www.jmag-international.com/jp/). NTT DATA itself was delisted 26 Sep 2025 after NTT's JPY 2.37tn tender — [Nihon M&A Center](https://www.nihon-ma.co.jp/news/20250620_9432-27/).
- Prometech Software (Particleworks, Granuleworks): capital JPY 50m, sole shareholder Prometech Group; group includes GDEP Solutions (NVIDIA GPU systems) and Particleworks Europe S.r.l. (Italy); capital and business alliance with Kozo Keikaku Engineering — [Prometech company page](https://www.prometech.co.jp/company/). 69 staff (job site, Oct 2026) — [r-agent](https://www.r-agent.com/company/h2878/). Particleworks 9.0 and Granuleworks 4.0 released 1 Oct 2026; PSC2026 user conference 19 Nov 2026 — [Prometech news](https://www.prometech.co.jp/news/). Revenue undisclosed.
- Software Cradle (STREAM, scFLOW, SCRYU/Tetra, PICLS): founded 1984; site now branded "Cradle CFD | Cadence"; news of 6 Mar 2026 on completion of Cadence's purchase of Hexagon's design and engineering business; Cradle CFD 2026.2 released 5 Nov 2026 — [cradle.co.jp](https://www.cradle.co.jp/). Deal about EUR 2.7bn (70% cash, 30% Cadence stock), adding about USD 160m to Cadence's 2026 revenue — [DE247, 24 Feb 2026](https://www.digitalengineering247.com/article/cadence-finalizes-purchase-of-hexagons-design-and-engineering-business).
- AdvanceSoft: est. 2002 from MEXT's strategic basic software project; capital JPY 37m; about 85-97 staff; own codes for fluids, structures, nano, semiconductors, EM, nuclear; nuclear safety-analysis unit ISO 9001 — [company overview](https://www.advancesoft.jp/company/company-info-ka/).
- Murata Software (Femtet, Murata Manufacturing group): 8 coupled solvers; from JPY 238,000/year; "1,200+" adopting organisations (company claim) — [muratasoftware.com](https://www.muratasoftware.com/).
- IDAJ: sells GT-SUITE, CONVERGE, Simcenter STAR-CCM+, Ansys Fluent, Abaqus, modeFRONTIER, CST — [IDAJ](https://www.idaj.co.jp/company/).
- Toray Engineering D Solutions (Toray group): product list not visible; rheology paper award Jun 2026 — [TDS](https://www.toray-eng.co.jp/tds/).
- KKE Holdings (構造計画研究所HD, 208A): holding company formed Jul 2024 — [KKE segments](https://www.kke-hd.co.jp/ir/financial/segment/); see sections 2 and 3.
- Dentsu Soken (電通総研, 4812): FY12/2025 revenue JPY 164.8bn; manufacturing segment grew on CAE and PLM sales to transport-equipment makers but profit fell; third-party software sales weak — [logmi, 17 Feb 2026](https://finance.logmi.jp/articles/383835). Manufacturing segment FY2025 sales JPY 61.0bn, profit JPY 7.5bn — [the-shashi](https://the-shashi.com/tse/4812/financials/segment/).
- SCSK: Sumitomo Corp tender (JPY 5,700/share, about JPY 880bn) completed 12 Dec 2025 — [Nihon M&A Center](https://www.nihon-ma.co.jp/news/20251213_8053-57/).

Chips
- Zuken (図研, 6947): own CR-8000 (PCB), E3.series (harness), DS-CR/DS-E3 (data management), GENESYS (MBSE); SI/PI/EMI "Analysis Module Advance Multicore"; R&D JPY 5,445m in FY3/2026; no customer above 10% of sales — [securities report, 19 Jun 2026](https://pdf.irpocket.com/C6947/uOn6/LHs8/Xr3L.pdf). Joined TSMC OIP EDA Alliance; AI design partnership with Valeo — [MTP progress, 24 Jul 2026](https://pdf.irpocket.com/C6947/xoA3/Ef45/rz9M/YJmG.pdf).
- JEDAT (ジーダット, 3841): own EDA for LSI, FPD and MEMS layout plus design services; 130 staff; owned 51.4% by ARGO GRAPHICS and 21.2% by Seiko Instruments (31 Mar 2026) — [securities report FY3/2026](https://disclosure2dl.edinet-fsa.go.jp/searchdocument/pdf/S100YAUW.pdf).
- Nippon Control System: sells NDE mask-data-preparation software (fracturing, mask rule check, proximity and mask process correction); ownership not shown — [NCS](https://www.nippon-control-system.co.jp/).
- Rapidus (private, state-funded): Synopsys, Cadence, Siemens (Calibre PDK) and Keysight (PDK from fab data) partnerships; own "Raads" design tools from FY2026, Raads Generator/Predictor planned as open source — [MONOist, 18 Dec 2025](https://monoist.itmedia.co.jp/mn/spv/2512/18/news057_2.html); [Converge Digest](https://convergedigest.com/rapidus-taps-keysight-to-sharpen-2nm-pdk-and-boost-yield-at-iim-1/). 2026: JPY 150bn government round (5 Jun), Cadence agentic-AI deal (17 Jul), "Rapidus CORE" ecosystem (5 Oct) — [Rapidus news](https://www.rapidus.inc/en/news_topics/).
- Tokyo Electron, SCREEN, Lasertec: no evidence found of external simulation-software sales.

Materials
- Matlantis Corp (ex-Preferred Computational Chemistry, renamed Jul 2025): est. 2021 (PFN 51%, ENEOS 49% at founding); Mitsubishi Corp joined Jun 2024; PFP v7 covers 96 elements; v8 on r2SCAN data (Jul 2025); US unit in Cambridge MA — [profile](https://matlantis.com/en/company/profile/). "Over 150 companies and organizations"; crystal-structure prediction launched with Honda R&D as early adopter — [release, 28 Jan 2026](https://matlantis.com/en/news/release-260128/). NVIDIA ALCHEMI integration (14 Apr 2026), AI-agent integration with Claude Code and Codex (27 May 2026), pricing by quotation — [product page](https://matlantis.com/en/product/) via the materials strand.
- Quemix: "Quloud" cloud materials-calculation platform, quantum algorithms; lists Honda, Denso, Nissan, Toyota, Idemitsu, SCSK as partners — [quemix.com](https://quemix.com/). Parent not shown.

Weather (Weathernews covered by the weather strand)
- Japan Weather Association (日本気象協会): own Japan-specific AI forecast model, 4 km and hourly, trial operation targeted FY2027 (release 6 Oct 2026, company claim) — [JWA news](https://www.jwa.or.jp/news/).

AI-for-physics start-ups
- RICOS: Series A about JPY 300m (Oct 2021) — [MONOist](https://monoist.itmedia.co.jp/mn/articles/2201/25/news013.html); "Generative CAE" won a CES 2025 Innovation Award; Suzuki evaluating RICOS Lightning; NEDO deep-tech support — [MONOist, 22 Jan 2025](https://monoist.itmedia.co.jp/mn/spv/2501/22/news007.html). MotorAI's design agent operates JMAG-Designer (deal 3 Dec 2025; service from Apr 2026) — [MONOist, 26 Dec 2025](https://monoist.itmedia.co.jp/mn/articles/2512/26/news007.html).

Cloud and HPC services
- HPC Systems (6597): HPC servers and integration for science and CAE, CTO industrial computers, computational-chemistry software sales (Gaussian) — [IPROS profile](https://mono.ipros.com/company/detail/303412). FY6/2026 sales JPY 7,906m, ordinary profit JPY 685m — [kabuyoho](https://kabuyoho.jp/sp/report?bcode=6597).
- Fixstars (3687): FY9/2026 (published 6 Nov 2026) sales JPY 10,650m (+10.7%), operating profit JPY 2,901m (27.2%), missing its raised forecast; Solution (acceleration engineering) JPY 9,988m, SaaS (Amplify quantum cloud, AIBooster, Vega) JPY 663m with a JPY 641m loss; customers about 40% auto, 35% semiconductors — [tanshin](https://www2.jpx.co.jp/disc/36870/140120261106567809.pdf); [deck](https://www2.jpx.co.jp/disc/36870/140120261106567816.pdf).
- Sakura Internet (3778): H1 FY3/2027 sales JPY 22.8bn (+46%), operating profit JPY 3.0bn; very high GPU utilisation; Rubin additions to be built against advance orders — [minkabu, 28 Oct 2026](https://minkabu.jp/news/4649295).

### Inferences
- The investable own-solver universe in Japan is close to empty; solver IP sits in private or captive firms (JSOL, Matlantis, Prometech, Murata Software, Cradle inside Cadence).

### Gaps
- Revenue of JMAG, Prometech, Matlantis, IDAJ, AdvanceSoft; ownership of IDAJ, Quemix, NCS; Quint, X-Ability, MI-6, QunaSys, Araya, Xtreme-D and ITOCHU Techno-Solutions were not verified in this pass.

## 2. Own solver versus resale and labour; distribution exposure

### Takeaway
Most Japanese revenue is resale of foreign licences, consulting hours or hardware. Resellers are exposed to supplier decisions: Synopsys ended Cybernet's optical-software agency in 2021, and Synopsys now owns Ansys, Cybernet's main line.

### Cited Findings
- Cybernet FY2022 (last public report): simulation segment JPY 15.78bn of JPY 19.94bn sales; simulation-segment purchases JPY 5.95bn; most software bought directly from developers, "dependence is high", agency contracts "non-exclusive and renewed over short periods", with risk if suppliers appoint other agents or sell direct; Synopsys ended the 36-year optical-design agency on 1 Oct 2021, cutting 2022 sales 12.2% and operating profit 37.9%; Ansys distribution listed as a material contract — [Cybernet securities report FY2022](https://disclosure2dl.edinet-fsa.go.jp/searchdocument/pdf/S100QDET.pdf); [FY2021](https://disclosure2dl.edinet-fsa.go.jp/searchdocument/pdf/S100NP2R.pdf).
- Synopsys completed the Ansys purchase on 17 Jul 2025 — [EE Times Japan](https://eetimes.itmedia.co.jp/ee/articles/2507/24/news058.html).
- KKE Q1 FY6/2027 (Jul-Sep 2026): Engineering Consulting 47% of sales (gross margin 37.7%); Products Services 50% (38.9%), where weak-yen purchase and royalty costs on overseas products cut margins; cloud ARR JPY 4,426m (+19.6%); cloud lines include Twilio SendGrid, RemoteLOCK and NavVis — [tanshin, 9 Nov 2026](https://www.kke-hd.co.jp/cms/uploads/2026/11/NewsRelease_ir_20261109_01.pdf); [supplementary deck](https://www.kke-hd.co.jp/cms/uploads/2026/11/NewsRelease_ir_20261109_02.pdf); [segments](https://www.kke-hd.co.jp/ir/financial/segment/).
- Zuken FY3/2026: client services (maintenance, recurring) JPY 18,492m of JPY 43,101m (43%); H1 FY3/2027 IT Solutions JPY 6,653m (+58.7%, 28% of sales), driven by a subsidiary's network-security resale (FortiGate, Darktrace) and storage-server demand — [MTP progress](https://pdf.irpocket.com/C6947/xoA3/Ef45/rz9M/YJmG.pdf); [Q2 tanshin, 9 Nov 2026](https://pdf.irpocket.com/C6947/xoA3/DnNg/ah0Z/sqpN.pdf).
- Fixstars: 94% of FY9/2026 sales from Solution engineering services (acceleration, firmware, algorithms); SaaS still loss-making — [deck](https://www2.jpx.co.jp/disc/36870/140120261106567816.pdf).
- JSOL: merchandise only 1.6% of FY3/2026 revenue — [決算公告](https://www.jsol.co.jp/company/sn2u4r000000086z-att/202606.pdf).
- IDAJ lists almost only third-party brands — [IDAJ](https://www.idaj.co.jp/company/). Dentsu Soken's third-party software sales fell short of plan in 2025 — [logmi](https://finance.logmi.jp/articles/383835).

### Inferences
- Synopsys's 2021 move to direct sales in optics is the precedent for the main risk to Cybernet under Synopsys-owned Ansys; no 2026 change to the Ansys channel was found.
- Own-solver and recurring revenue: Zuken, JMAG, Matlantis, Femtet, Particleworks, JEDAT. Labour-hour heavy: KKE consulting, Fixstars, Dentsu Soken, JSOL overall. Resale heavy: Cybernet, IDAJ, Zuken's security line, KKE's cloud line. Hardware: HPC Systems, Sakura.

### Gaps
- Cybernet's Ansys share of sales is not disclosed; no third-party estimate of the distribution share of Japan's CAE market was found.

## 3. Framework applied to the strongest candidates

### Takeaway
JMAG and Matlantis are the strongest Japanese solver owners but lack outside evidence of a lead; Zuken is the strongest listed business but is a design-authoring vendor with limited simulation; Particleworks is a small GPU-native niche; KKE is mainly a services firm.

### Cited Findings
JMAG (JSOL; private)
- (a) Position: own low-frequency EM solver used for motor design; a design-level judge inside OEM workflows, not a regulatory one. (b) Lead: only company claims ("domestic top share", [JSOL recruitment](https://hrmos.co/pages/jsol/jobs/25-008000302)); vendor-listed cases include Mazda, Honda R&D, Ford, GM, Mercedes-Benz, Bosch, Aisin ([JMAG automotive](https://www.jmag-international.com/solutions/automotive/)); outside evidence is a third party (MotorAI) choosing JMAG for its agent ([MONOist](https://monoist.itmedia.co.jp/mn/articles/2512/26/news007.html)). (c) Revenue: licences inside an IT-services company; JMAG-Express Online free. (d) JSOL FY3/2026 margin 13.9%, no borrowings, JPY 23.4bn deposited with group ([決算公告](https://www.jsol.co.jp/company/sn2u4r000000086z-att/202606.pdf)). (e) Tied to EV and motor programmes rather than AI capex: little change in the steady (55%) or acceleration (20%) cases, while a 2028 financing pause (25%) matters mainly via automotive budgets.
- Transitions, said vs done: agents (3) — said "AI agents will operate JMAG" (company); done: MotorAI integration, open interface and script library. Learned models (5) — done: FMI surrogate export (Nov 2026 leaflet). GPU (2), usage pricing (1), open source (4): nothing found. Must go right: keep motor-EM accuracy ahead of Ansys Maxwell and Siemens bundles, and stay open to agents.

Matlantis (private)
- (a) Own AI-native atomistic simulator (PFP); a screening tool, not sign-off; exposed to open universal potentials and DFT on GPUs. (b) Lead: PFP paper an Editor's Highlight in Nature Communications (Jun 2022, developers' own work; [profile](https://matlantis.com/en/company/profile/)); "150+" users and accuracy gains are company claims, unconfirmed ([release](https://matlantis.com/en/news/release-260128/); [v8 release, 16 Jul 2025](https://matlantis.com/en/news/release-250716/)). (c) Cloud subscription, quote-based. (d) Undisclosed. (e) Depends on GPU supply and chemical/materials R&D budgets; a 2028 pause would hit customers' R&D, not its own capex.
- Transitions: GPU (2) and learned models (5) are the product; agents (3) done (27 May 2026 integration); open source (4) is the main threat; usage pricing (1) not confirmed. Must go right: independent benchmarks and a price/accuracy edge over free models.

Zuken (listed)
- (a) Owns system-of-record design and data tools (PCB, harness, MBSE) with SI/PI/EMI checks; sign-off grade SI/PI is usually Ansys, Cadence or Siemens (inference). (b) TSMC OIP membership and Valeo partnership are outside acknowledgements; no share data. (c) 43% maintenance revenue; licences; plus third-party security resale. (d) FY3/2026 sales JPY 43.1bn, operating profit JPY 5,865m (13.6%), ROE 13.3%, equity ratio 61%, operating cash flow JPY 6.1bn ([securities report](https://pdf.irpocket.com/C6947/uOn6/LHs8/Xr3L.pdf)); H1 FY3/2027 sales +21.9%, operating profit +55.5%; full-year guidance raised to sales JPY 48.5bn, operating profit JPY 7.3bn, close to the FY3/2028 plan of JPY 49.0bn/7.4bn ([Kabutan, 9 Nov 2026](https://s.kabutan.jp/news/k202611090003/); [MTP](https://pdf.irpocket.com/C6947/xoA3/Ef45/rz9M/YJmG.pdf)). Japan 68% of FY3/2026 sales; top five domestic customers 11.3% of parent sales. (e) Zuken cites AI-server boards (AI/HPC share of PCB value about 25% in 2026 rising to 40-45% by 2030, via an Interconnection Technologies report) — helps in steady and acceleration cases; a 2028 pause would hit AI-server and equipment customers; cyber attack on servers of Zuken GmbH (Germany) detected 23 Oct 2026, impact excluded from guidance ([Q2 tanshin](https://pdf.irpocket.com/C6947/xoA3/DnNg/ah0Z/sqpN.pdf)). Export-control exposure looks low: Asia including China direct sales was 4.3% of H1 sales (same tanshin).
- Transitions: agents and AI (3) — done: AI place-and-route, Valeo agent link; usage pricing, GPUs, regulators: not relevant or not found. Must go right: chip-package-board co-design (3DIC) against Cadence and Siemens.

Particleworks (Prometech; private)
- (a) Own MPS particle CFD for lubrication, splashing, mixing; niche, not sign-off. (b) No third-party share; foreign distribution and KKE alliance. (c) Licences plus consulting and GPU hardware (GDEP). (d) Undisclosed; 69 staff. (e) GPU-native, so the GPU shift helps; small scale is the risk. Transitions: GPU done (company); agents, surrogates, pricing not found.

KKE Holdings (listed)
- (a) Mostly consulting and resale; its structural programs are absent from MLIT's certified-program registers (2000-2023, section 4). (b) No outside evidence of a lead. (c) Labour hours plus resale; KPI is "total value added" (operating profit plus people costs), target +8% a year. (d) FY6/2026 sales JPY 22,453m, operating profit JPY 3,540m (15.8%); FY6/2027 guide JPY 24,380m/3,850m; Q1 loss JPY 269m is seasonal ([Monex, 10 Aug 2026](https://scouter.monex.co.jp/news/detail/208A_20260810_act_20260810_160025_3); [Q1 tanshin](https://www.kke-hd.co.jp/cms/uploads/2026/11/NewsRelease_ir_20261109_01.pdf)). (e) Domestic construction and disaster-prevention demand; weak yen raises import costs; little AI-capex exposure.

### Inferences
- None of the five has a regulator-accepted judge or third-party share evidence; all rank below global mid-size vendors.

### Gaps
- JMAG GPU solver status, pricing model and user count; independent PFP benchmarks (search tools exhausted).

## 4. Boundary of trust in Japan: who certifies

### Takeaway
Domestic gates protect a few domestic programs (building structure) and the class society's own software; elsewhere Japan follows foreign or international practice and keeps physical tests in charge.

### Cited Findings
- Building Standards Act Art. 20: minister-certified programs (大臣認定プログラム) speed review and cut fees — [MLIT 2008](https://www.mlit.go.jp/kisha/kisha08/07/070118_.html); [Osaka fees](https://www.pref.osaka.lg.jp/documents/8294/kouzoutekihan.pdf); Aichi requires electronic data for other programs — [Aichi](https://www.pref.aichi.jp/soshiki/kenchikushido/program.html). MLIT's register for Apr 2000-Mar 2013 lists about 106 old-law certifications (Union System, Kozo Soft, NTT DATA, TIS, Arc Data, contractors, house builders) but new-law certifications only for NTT DATA's SEIN La CREA (2009-10) — [register](https://www.mlit.go.jp/common/001109045.pdf). The Apr 2013-Apr 2023 register adds SEIN La CREA (NTT Facilities Research Institute, Aug 2015), ABUS-5 (Kozo System) and BUILD.一貫V (Kozo Soft) (Jun 2016), ASCAL-EX (Arc Data, Dec 2016) — [register](https://www.mlit.go.jp/common/001489237.pdf).
- NRA: reviews code validity case by case; for the Joyo reactor (24 Feb 2022) it accepted the applicant's validation by experiments and sensitivity analysis except SIMMER-III/IV — [NRA](https://www.nra.go.jp/data/000401927.pdf). Codes used at licensing are confirmed via topical reports or per-applicant review; post-operation checks can rely on operators' QMS (search summary of NRA documents) — [NRA](https://www.nra.go.jp/data/000302202.pdf).
- PMDA: science-committee report on reviewing medical-device software that uses computer simulation, for use in routine work (30 Mar 2021); earlier report on FE analysis for orthopaedic implants (2016); evaluation indices are not legal standards — [PMDA report](https://www.pmda.go.jp/files/000240657.pdf); [PMDA slides](https://www.pmda.go.jp/files/000231852.pdf).
- ClassNK: PrimeShip-HULL (HCSR) implements IACS CSR, with FE direct strength assessment, free to shipyards; ClassNK says most yards building CSR ships use it (claim) — [Maritime Professional](https://www.maritimeprofessional.com/news/classnk-primeship-hull-hcsr-software-313971).
- Vehicles: after certification fraud by several makers, MLIT added internal-control checks and post-approval physical testing of production vehicles (31 Mar 2025) — [MLIT](https://www.mlit.go.jp/report/press/jidosha08_hh_005422.html); type-approval fees doubled from 1 Apr 2026 — [BSR](https://bsrweb.jp/article/810930). Virtual-testing demand comes from Euro NCAP (from 2026) — [Yano, 13 Mar 2025](https://www.yano.co.jp/press-release/show/press_id/3741).
- Aviation: JAXA, Kawasaki and Mitsubishi Heavy are building a certification-by-analysis process and guidelines with the civil aviation bureau (FY2022-2026); no type certificate by analysis found — [JAXA CHAIN-X, Dec 2025](https://www.aero.jaxa.jp/news/event/pdf/event251202/chain-x2025_07.pdf).
- Weather: revised Meteorological Business Act (effective May 2026) adds forecast-permit rules for foreign firms — [Weathernews, 26 Aug 2026](https://jp.weathernews.com/news/57281/).

### Inferences
- Building-structure certification is a small, domestic, regulation-protected judge market; foreign FE vendors are absent from the registers.

### Gaps
- Current validity of each certified program after 2023; NRA's list of accepted codes; any MLIT virtual-testing rule.

## 5. National computing and what it means for double precision

### Takeaway
FugakuNEXT gives FP64 codes about 5x more hardware but low-precision AI about 70x more; RIKEN plans to close the gap with algorithms (surrogates, mixed precision, FP64 emulation) and AI-assisted porting.

### Cited Findings
- Design targets (RIKEN workshop, 6 Mar 2026): GPU FP64 2.6+ EFLOPS plus CPU 48+ PFLOPS (Fugaku 537 PFLOPS; x4.8); FP16/BF16 150+ EFLOPS (Fugaku 2.15; x70.5); FP8 300+, 600+ with sparsity; memory bandwidth 800+ PB/s; 3,400+ nodes; 40 MW or less; 2 CPU: 4 GPU nodes with NVLink-C2C; basic design FY2025, then detailed design, build, operation from about FY2030 — [RIKEN](https://www.r-ccs.riken.jp/events/20260306-1/fugakunext-3.pdf). Up to 100x application speed: hardware up to 6x, software up to 20x via surrogates/PINNs (10-20x), mixed precision and Ozaki-scheme FP64 emulation (2-8x) — same deck; [MEXT HPCI committee, 22 Aug 2025](https://www.mext.go.jp/content/20250822-mxt-jyohoka01-000044312_41.pdf), which also lists AI-assisted porting tools.
- "Zettascale": RIKEN says world's first zetta-scale "AI performance (FP8)" — [RIKEN FugakuNEXT](https://www.r-ccs.riken.jp/fugaku-next/); NVIDIA's Ian Buck quoted on "zettascale performance" — [RIKEN, 22 Aug 2025](https://www.riken.jp/en/news_pubs/news/2025/20250822_1/index.html); The Next Platform infers zettascale only at sparse FP4 (about 1,200 EFLOPS), its own inference — [Next Platform, 22 Aug 2025](https://www.nextplatform.com/hpc/2025/08/22/nvidia-tapped-to-accelerate-rikens-fugakunext-supercomputer/1638019).
- Roles: RIKEN leads; Fujitsu CPU and system integration; NVIDIA GPU and scale-up network; site next to RIKEN Kobe; basic-design report 29 May 2026; no detailed-design award listed — [RIKEN](https://www.r-ccs.riken.jp/fugaku-next/).
- ABCI 3.0 (AIST; operated by AIST Solutions; from Jan 2025): 766 nodes, 6,128 H200; about 415 PFLOPS FP64, 6.2 EFLOPS FP16 — [MONOist, 10 Apr 2025](https://monoist.itmedia.co.jp/mn/articles/2504/10/news016_2.html); [ABCI](https://abci.ai/ja/about_abci/).
- Porting: an AI agent (Claude Code) ported 162 kernels of the 250,000-line Fortran storm model CReSS to GPUs on Miyabi (GH200), 5.1x faster than the Grace CPU, single-precision tolerance; not in production — [arXiv 2608.13122, Aug 2026](https://arxiv.org/html/2608.13122).
- JMA plan (26 Jun 2026): AI and physical models "on two wheels"; GPU porting of global, meso and local models first; AI models used first for typhoon tracks; compute is the constraint — [JMA summary](https://www.jma.go.jp/jma/press/2606/26a/nwp_strategic_plan_2030_260626_1summary.pdf). JMA tested FourCastNetv2, Pangu-Weather and GraphCast and formed an advanced-AI team — [NPD report 2025](https://d2borx18t6gdx.cloudfront.net/jma/kishou/books/npdc/2025/npdc_report_2025.pdf). No operational JMA AI model found.

### Inferences
- Japanese CPU-tuned FP64 codes (national-project codes, AdvanceSoft) must port to GPUs; vendors with GPU-native or learned solvers (Particleworks, Matlantis) gain relative position.

### Gaps
- FugakuNEXT budget and detailed-design contracts; Fujitsu's commercial computing services.

## 6. Market data: size and domestic versus foreign vendors

### Takeaway
Only Yano publishes free headline sizes; vendor shares sit in paid reports.

### Cited Findings
- Mechanical CAE (structure, thermal-fluid, moulding, casting; vendor revenue basis): 2022 JPY 90.16bn (actual), 2023 JPY 97.01bn (estimate), 2024 JPY 104.18bn (forecast); drivers: chips, software-defined vehicles, giga-casting, Euro NCAP virtual testing; no domestic/foreign split — [Yano No.3741, 13 Mar 2025](https://www.yano.co.jp/press-release/show/press_id/3741). The paid report (31 Jan 2025, JPY 220,000) has shares — [IPROS](https://mono.ipros.com/product/detail/2000383035). No 2025 figure found.

### Inferences
- Cybernet's JPY 25.4bn revenue equals about a quarter of Yano's 2024 figure, though scopes differ.

### Gaps
- Vendor shares (Yano, Fuji Chimera, Techno Systems Research) not publicly available.

## 7. Entry-point data (valuation and access), separate from quality evidence

### Takeaway
All are Tokyo-only listings with 100-share lots; liquidity is thin except Sakura and Dentsu Soken; most private solver owners offer no route.

### Cited Findings
Prices are 12 Nov 2026 closes; daily value traded that day; Kabutan market values include treasury shares.
- Zuken (6947): JPY 5,140; JPY 114.3bn; P/E 17.7x (forecast), 16.8x trailing; P/S 2.3x; EV/EBIT 8.9x; FCF yield 7.3%; net cash JPY 36.6bn; 52-week +9.6%; JPY 223m traded — [Kabutan](https://s.kabutan.jp/stocks/6947/); [StockAnalysis](https://stockanalysis.com/quote/tyo/6947/statistics/). Year-end FY3/2022-26: P/E 23.4, 25.0, 25.9, 19.6, 16.9; P/S 2.1-2.6; EV/EBIT 9.7-14.1; price JPY 2,711 (Mar 2022) to 4,266 (Mar 2026) — [ratios](https://stockanalysis.com/quote/tyo/6947/financials/ratios/). Events: cancels 1.17m treasury shares 30 Nov 2026; Q3 results around Feb 2027 (not confirmed); cyber-attack impact.
- KKE Holdings (208A): JPY 2,695; JPY 29.6bn; P/E 11.0x (Kabutan), 11.6x on FY6/2027 guided EPS JPY 231.81; trailing 14.1x; EV/EBIT 10.1x; yield 4.1%; JPY 34m traded — [Kabutan](https://s.kabutan.jp/stocks/208A/); [ratios](https://stockanalysis.com/quote/tyo/208A/financials/ratios/). Year-end P/E 12.8 (Jun 2025), 13.9 (Jun 2026); price JPY 2,381 to 2,779; longer history is the predecessor KKE (4748).
- JEDAT (3841): JPY 1,081; JPY 4.2bn; P/E 19.8x; P/B 1.15x; cash JPY 2.7bn (Mar 2026); free float under 28%; JPY 5m traded — [Kabutan](https://s.kabutan.jp/stocks/3841/). No usable five-year multiples found.
- Fixstars (3687): JPY 1,634; JPY 54.9bn; P/E 23.9x on FY9/2027 guide (EPS JPY 68.10), 27.0x trailing; EV/EBIT 16.0x; JPY 632m traded — [Kabutan](https://s.kabutan.jp/stocks/3687/). Year-end FY9/2022-26: P/E 31.3, 26.0, 34.4, 30.4, 37.0; P/S 5.4-6.8; EV/EBIT 16.7-22.8; price JPY 2,240 at 30 Sep 2026, down 27% since — [ratios](https://stockanalysis.com/quote/tyo/3687/financials/ratios/). AGM 23 Dec 2026 — [tanshin](https://www2.jpx.co.jp/disc/36870/140120261106567809.pdf).
- HPC Systems (6597): JPY 2,604; JPY 11.3bn; P/E 16.2x forecast, 21.8x trailing; EV JPY 17.1bn (net debt); EV/EBIT 24.0x; negative FCF; 52-week high JPY 7,500 (5 Jun 2026), low JPY 1,585 (15 Dec 2025); Q1 results 13 Nov 2026 — [Kabutan](https://s.kabutan.jp/stocks/6597/); [ratios](https://stockanalysis.com/quote/tyo/6597/financials/ratios/).
- Sakura Internet (3778): JPY 3,160; JPY 132.3bn; P/E 49.6x; trailing 46x; EV/EBIT 40x; debt/equity 1.1; JPY 2.35bn traded. Year-end P/S FY3/2022-26: 1.0, 1.1, 9.3, 4.7, 2.8; price JPY 564 (Mar 2022), 5,660 (Mar 2024), 2,479 (Mar 2026) — [Kabutan](https://s.kabutan.jp/stocks/3778/); [ratios](https://stockanalysis.com/quote/tyo/3778/financials/ratios/).
- Dentsu Soken (4812): JPY 2,873; JPY 561.8bn; P/E 31.1x; EV/EBIT 19.9x; JPY 1.8bn traded. Year-end FY2021-25 P/E 28.2, 20.3, 25.9, 25.2, 32.7; EV/EBIT 10.9-23.2 — [Kabutan](https://s.kabutan.jp/stocks/4812/); [ratios](https://stockanalysis.com/quote/tyo/4812/financials/ratios/).
- Weathernews (4825) snapshot: JPY 1,854; JPY 82.4bn (ex-treasury); P/E 22.1x trailing, 19.6x forward; EV/EBITDA 11.7x; net cash JPY 15.7bn; 52-week -8.1% — [StockAnalysis](https://stockanalysis.com/quote/tyo/4825/statistics/).
- Tokyo Electron (8035, in-house simulation only): JPY 9,304; JPY 21.06tn; P/E 30.0x trailing, 20.9x forward — [StockAnalysis](https://stockanalysis.com/quote/tyo/8035/statistics/).
- Parent and no-route cases: JSOL via NTT (9432) or SMFG (8316), negligible exposure; Matlantis via ENEOS (5020) or Mitsubishi Corp (8058), negligible; Femtet via Murata Manufacturing (6981); TDS via Toray (3402); Cradle via Cadence (Nasdaq); Cybernet (KKR), SCSK (Sumitomo Corp 8053), JEDAT also via ARGO GRAPHICS (7595); no route to Preferred Networks, Prometech, AdvanceSoft, IDAJ, RICOS, Quemix, Rapidus.

### Inferences
- Thin trading (KKE, JEDAT) limits position sizes for foreign funds.

### Gaps
- ADR availability not checked; consensus estimates not collected.

## 8. Coverage limits, could-not-verify list and dated sources

### Takeaway
Coverage is good for listed firms' filings and national computing, thin for private vendors, market shares and independent accuracy evidence.

### Cited Findings
Dated source list (publication date — source):
- 12 Nov 2026 — Kabutan quotes ([Zuken](https://s.kabutan.jp/stocks/6947/), [KKE](https://s.kabutan.jp/stocks/208A/), [JEDAT](https://s.kabutan.jp/stocks/3841/), [Fixstars](https://s.kabutan.jp/stocks/3687/), [HPC](https://s.kabutan.jp/stocks/6597/), [Sakura](https://s.kabutan.jp/stocks/3778/), [Dentsu Soken](https://s.kabutan.jp/stocks/4812/)); StockAnalysis ratio pages (S&P Global data, 6-11 Nov 2026).
- 9 Nov 2026 — Zuken Q2 tanshin and revision; KKE Q1 tanshin and deck. 6 Nov 2026 — Fixstars FY tanshin and deck. 6 Oct 2026 — JWA AI model. 28 Oct 2026 — Sakura H1.
- 24 Jul 2026 — Zuken MTP progress. 26 Jun 2026 — JMA NWP plan. 19 Jun 2026 — Zuken securities report. 12 Jun 2026 — JSOL 決算公告. Jun 2026 — JEDAT securities report. 29 May 2026 / 6 Mar 2026 — RIKEN FugakuNEXT report and workshop. 28 Jan 2026 — Matlantis CSP. 24 Feb 2026 — DE247 Cadence-Hexagon. 17 Feb 2026 — logmi Dentsu Soken.
- 2025 — Yano (13 Mar), MLIT type approval (31 Mar), ABCI 3.0 (MONOist 10 Apr), RIKEN/NVIDIA/Next Platform FugakuNEXT (21-22 Aug), MEXT HPCI (22 Aug), MONOist MotorAI (26 Dec), Nihon M&A (Feb, Jun, Dec), JAXA CHAIN-X (Dec).
- Older, flagged: Cybernet securities reports FY2021-22 (2022-23); NRA Joyo (Feb 2022); PMDA (Mar 2021); MLIT registers (to Apr 2023); ClassNK PrimeShip press (about 2020); Toyo Keizai AD (Aug 2023); RICOS Series A (2021).

### Inferences
- Rankings of Japanese firms rest mostly on company claims and filings, not outside validation.

### Gaps
Could not verify:
- Revenue of JMAG, Prometech, Matlantis, IDAJ, AdvanceSoft, Murata Software; Cybernet's Ansys share; any 2026 change to Ansys's Japan channel.
- Third-party CAE vendor shares for Japan; a 2025 Yano market figure.
- Independent benchmarks of PFP, JMAG or Particleworks; JMAG GPU and pricing; Matlantis usage pricing.
- Ownership of IDAJ, Quemix and NCS; status of ITOCHU Techno-Solutions, Quint, X-Ability, MI-6, QunaSys, Araya, Xtreme-D; Fujitsu computing services.
- TEL, SCREEN, Lasertec simulation tools; Rapidus's final EDA choices beyond announced partners.
- Currently valid certified structural programs; NRA accepted-code list; any MLIT virtual-testing rule; JMA AI operational start.
- ADRs, consensus forecasts, next earnings dates other than HPC Systems (13 Nov 2026) and Fixstars AGM.
