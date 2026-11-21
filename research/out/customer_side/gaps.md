# Gaps - customer_side (21 Nov 2026)

## Save these by hand first (priority order)

Each of these would change a finding if saved into `research/sources/customer_side/`. All of them sit on hosts that refuse scripted access.

1. TSMC keynote abstract, SEMICON Taiwan 2026 (Zhihua Zou): https://www.semicontaiwan.org/en/node/18506. Also save the forum agenda https://semicontaiwan.org/en/Metrology_2026 and the speaker bio https://www.semicontaiwan.org/en/node/17406.
2. Onto Innovation's release on its SK hynix 2026 Best Partner Award for HBM hidden-defect prevention. It is the only award found that ties an inspection tool to HBM production: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production/default.aspx
3. SK hynix, VLSI 2026, "High Bandwidth Memory 4 (HBM4) Package Development Challenges". Semantic Scholar marks it open access. https://doi.org/10.1109/vlsitechnologyandcir65830.2026.11577576
4. Intel, ECTC 2026, 100% chip-to-wafer bond-overlay metrology: https://doi.org/10.1109/ECTC51846.2026.00354. Also Intel, ECTC 2026, chiplet distortion / NIR overlay: https://doi.org/10.1109/ECTC51846.2026.00030
5. Samsung, IRPS 2025, HBM buffer-die interface-resistance pre-screen: https://doi.org/10.1109/irps48204.2025.10983202
6. ASE, ECTC 2026, chip-on-wafer hybrid-bonding voids. The detection method is missing from the abstract. https://doi.org/10.1109/ECTC51846.2026.00059
7. Samsung, ECTC 2026, leakage-current metrology for hybrid Cu bonding: https://doi.org/10.1109/ectc51846.2026.00250. Also Micron, ECTC 2025, wafer-to-wafer bonding for HBM density: https://doi.org/10.1109/ectc51687.2025.00097
8. SPIE 2026 papers on HBM and hybrid bonding. Their affiliations are unknown, and they may be chipmaker co-authored:
   - https://doi.org/10.1117/12.3095356 (picosecond laser acoustics, buried voids in HBM)
   - https://doi.org/10.1117/12.3093061 (e-beam process control for HBM hybrid bonding)
   - https://doi.org/10.1117/12.3090618 (3D X-ray of micro-bumps and hybrid bonds)
9. Award lists from the chipmakers themselves:
   - TSMC: https://pr.tsmc.com/english/news/3274 (2025) and https://pr.tsmc.com/english/news/3355 (2026)
   - Intel: https://newsroom.intel.com/intel-foundry/intel-announces-2025-epic-supplier-award-recipients and https://newsroom.intel.com/corporate/intel-announces-2026-epic-supplier-award-recipients
   - ASE: https://www.aseglobal.com/press-room/supplier-day-2025 and https://www.aseglobal.com/press-room/supplier-day-2026
10. Micron keynote at SEMICON Taiwan 2026 ("AI-Powered Smart Quality Ecosystem"): https://semicontaiwan.org/en/node/20171
11. SK hynix earnings-call scripts, Q4 2025 to Q3 2026 (the page is JavaScript-only): https://www.skhynix.com/ir/UI-FR-IR06/. Also Micron prepared remarks on investors.micron.com (URLs in the SMP lines below).
12. Intel Foveros Direct 3D tech brief: https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-11/foveros-direct-3d-tech-brief.pdf

# Gap log - customer_side (one line per item)

Source of each line in brackets: the module that recorded it (PAPM, PAPL, TALK, XR, SMP, AW) or MAIN (main session). Lines are copied from the module notes; near-duplicates across modules are kept when they name different documents.

## NOT RETRIEVED (83)

- [ADDL] NOT RETRIEVED (tried: https://pr.tsmc.com/system/files/newspdf/attachment/1e7873e182523d3351afd810dc413e0bce01ca5f/2026%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29-final_wmn.pdf with fetch.py, HTTP 403; the 2025 PDF https://pr.tsmc.com/system/files/newspdf/attachment/ce3c12707f578ed01449842b2d7d4b3d1b6c1cbf/2025%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29_final_wmn.pdf not tried after that refusal) - TSMC's own 2026 and 2025 supplier-award lists with English category names. AW-001 to AW-016 stay [S]. Please save both PDFs by hand
- [ADDL] NOT RETRIEVED (tried: https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-11/foveros-direct-3d-tech-brief.pdf with fetch.py, HTTP 403; https://www.intel.com/content/www/us/en/foundry/packaging.htm not tried, host refuses scripted access) - Intel Foundry packaging page ("Advanced Chiplet Test", "Test Services") and the Foveros Direct 3D tech brief. gaps.md item 12 stays NOT RETRIEVED; it cannot be closed as NOT DISCLOSED from this run. Please save both by hand
- [ADDL] NOT RETRIEVED (tried: none; ieeexplore.ieee.org bot challenge) - full texts of https://doi.org/10.1109/impact67645.2025.11281768 (TSMC) and https://doi.org/10.1109/impact67645.2025.11281550 (ASE)
- [ADDL] NOT RETRIEVED (tried: Amkor event page only) - slides or paper of the ITC 2026 talk "Advanced Packages, AI & Amkor: The OSAT Test Perspective" and of the ITC 2025 talk "Best Practices for Testing 2.5D Chiplet Package Designs"
- [ADDM] NOT RETRIEVED (tried: https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production.pdf with fetch.py, HTTP 404; investors.ontoinnovation.com not tried, host refuses scripts; stocktitan.net copy not used, republisher) - Onto release on its SK hynix 2026 Best Partner Award. Please save by hand: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production/default.aspx
- [ADDM] NOT RETRIEVED (tried: https://www.globenewswire.com/news-release/2025/07/08/3111447/0/en/Infinitesima-Metron-3D-300mm-System-Released-for-In-line-Process-Control-by-Leading-DRAM-Manufacturer.html with fetch.py, HTTP 403; https://infinitesima.com/news/ HTTP 404; https://infinitesima.com/insights lists 2026 items only; storagenewsletter.com copy not used, republisher) - Infinitesima release of 8 Jul 2025 saying SK hynix released Metron3D for volume production. Please save the GlobeNewswire page by hand
- [ADDM] NOT RETRIEVED (tried: https://pubs.acs.org/doi/10.1021/acsaelm.6c00446 with fetch.py, HTTP 403) - abstract and full text of the SK hynix co-authored bond-wave / scaling-error paper
- [ADDM] NOT RETRIEVED (tried: https://onlinelibrary.wiley.com/doi/10.1002/sia.70044 with fetch.py, HTTP 403) - full text of the Micron XRR paper
- [ADDM] NOT RETRIEVED (tried: none, ieeexplore.ieee.org bot challenge) - full texts of https://doi.org/10.1109/icmts63811.2025.11068899 and https://doi.org/10.1109/sispad66650.2025.11186319
- [AW] NOT RETRIEVED (tried: https://pr.tsmc.com/english/news/3274 with fetch.py, HTTP 403; same-host PDF https://pr.tsmc.com/system/files/newspdf/attachment/ce3c12707f578ed01449842b2d7d4b3d1b6c1cbf/2025%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29_final_wmn.pdf not tried) - TSMC's own 2025 Excellent Performance Award list with English category names. Please save by hand
- [AW] NOT RETRIEVED (tried: https://pr.tsmc.com/english/news/3355 with fetch.py, HTTP 403; same-host PDF https://pr.tsmc.com/system/files/newspdf/attachment/1e7873e182523d3351afd810dc413e0bce01ca5f/2026%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29-final_wmn.pdf not tried) - TSMC's own 2026 list. Please save by hand
- [AW] NOT RETRIEVED (tried: web search for a TSMC OIP 2025/2026 Partner of the Year page; tsmc.com refuses scripts) - TSMC's own OIP award lists; the 2026 3DFabric Testing winner is unknown
- [AW] NOT RETRIEVED (tried: https://newsroom.intel.com/intel-foundry/intel-announces-2025-epic-supplier-award-recipients with fetch.py, HTTP 403; https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-announces-2025-epic-supplier-award-recipients.html not tried, host refuses) - Intel's 2025 list with English categories. Please save by hand
- [AW] NOT RETRIEVED (tried: https://newsroom.intel.com/corporate/intel-announces-2026-epic-supplier-award-recipients with fetch.py, HTTP 403; https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-announces-2026-epic-supplier-award-recipients.html not tried, host refuses) - Intel's 2026 list (41 recipients) and categories. Please save by hand
- [AW] NOT RETRIEVED (tried: Korean and English web searches for 2025 Partners Day winners) - 13 of 14 SK hynix 2025 winners (ULVAC only identified)
- [AW] NOT RETRIEVED (tried: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production/default.aspx not fetched, host refuses; https://www.businesswire.com/news/home/20261012570961/en/ with fetch.py, curl stream error) - Onto's release on its SK hynix 2026 Best Partner Award. Please save by hand
- [AW] NOT RETRIEVED (tried: https://www.aseglobal.com/press-room/supplier-day-2025 with fetch.py, HTTP 403; https://www.businesswire.com/news/home/20250411042346/en not tried after Business Wire stream errors) - ASE's own release for the 2024 awards (Apr 2025). Please save by hand
- [AW] NOT RETRIEVED (tried: https://www.aseglobal.com/press-room/supplier-day-2026 with fetch.py, HTTP 403; https://www.businesswire.com/news/home/20260424628552/en/ with fetch.py, curl stream error) - ASE's own release for the 2025 awards (Apr 2026). Please save by hand
- [AW] NOT RETRIEVED (tried: Chinese and English web searches for an SPIL-only supplier award) - a separate SPIL event; none found
- [AW] NOT RETRIEVED (tried: amkor.com blog index and web searches; ir.amkor.com refuses scripts) - Amkor's full Supplier Excellence Award 2025 winner list (9 Dec 2025)
- [AW] NOT RETRIEVED (tried: web searches 'Amkor Supplier Excellence Award 2026', 'Amkor Supplier Day 2026') - an Amkor 2026 supplier-award event. I found none and do not assume whether it has been held
- [AW] NOT RETRIEVED (tried: https://ec.ltn.com.tw/article/paper/1778949 with fetch.py, HTTP 403) - Liberty Times article on the TSMC 2026 awards (says V5 won 'again')
- [AW] NOT RETRIEVED (tried: https://www.funder.co.il/article/198109 with fetch.py, HTTP 403) - Hebrew article on Israeli Intel 2026 winners
- [AW] NOT RETRIEVED (tried: none; appliedmaterials.com refuses scripts) - Applied Materials blogs on its TSMC 2025 award (https://www.appliedmaterials.com/us/en/newsroom/blogs/tsmc-award.html) and Intel EPIC 2025/2026 awards (https://www.appliedmaterials.com/us/en/newsroom/blogs/applied-materials-earns-intel-s-2025-epic-supplier-award.html, https://www.appliedmaterials.com/us/en/newsroom/blogs/applied-receives-intel-epic-supplier-award.html). These are for an 'other'-class winner and are optional
- [PAPL] NOT RETRIEVED (tried: fetch.py https://doi.org/10.31399/asm.cp.istfa2026p0194 -> https://dl.asminternational.org/istfa/proceedings/ISTFA2026/85458/194/35954, HTTP 403, 2026-11-21) - ISTFA full texts. . Same host for istfa2026p0419, p0587, p0424 and istfa2025p0011, p0482
- [PAPL] NOT RETRIEVED (tried: none; ieeexplore.ieee.org bot challenge per access rules) - IEEE full texts (all ECTC, IRPS, ITC, IPFA, VLSI, EPTC, ASMC papers above). . URLs are in the save-by-hand list
- [PAPL] NOT RETRIEVED (tried: api.semanticscholar.org DOI:10.1109/IITC66087.2025.11075360, abstract null; Crossref listing has no abstract) - Amkor IITC 2025 "Advanced Interconnection Technology Overview" abstract
- [PAPL] NOT RETRIEVED (tried: saved S2 batch, abstract null) - Abstracts of 26 TSMC/Intel VLSI 2025 papers. . All titles are device or circuit topics
- [PAPL] NOT RETRIEVED (tried: saved Crossref volume listings, 0 items) - IPFA 2026 and IITC 2026 papers
- [PAPM] NOT RETRIEVED (tried: none, per brief; ieeexplore.ieee.org returns a 202 bot challenge) - Full texts of the 35 IEEE papers (34 with prefix 10.1109, 1 with 10.23919) in the table and evidence: . URLs are in each row's `url` column
- [PAPM] NOT RETRIEVED (tried: Semantic Scholar and Crossref records only; dl.asminternational.org not tried) - Full texts of the 10 ISTFA papers
- [PAPM] NOT RETRIEVED (tried: Crossref volume listings and Semantic Scholar batch; spie.org / spiedigitallibrary.org refuse scripted access) - Full texts and affiliations of the SPIE MIPC XXXIX/XL papers
- [PAPM] NOT RETRIEVED (tried: Semantic Scholar batch record, where the abstract is elided or null; Crossref volume listing, which has no abstract) - Abstracts of Micron "High Bandwidth Memory for AI" (VLSI 2025) and SK hynix "Metal interconnection of high bandwidth memory in wafer level packaging" (IITC 2025)
- [SMP] NOT RETRIEVED (tried: fetch.py on https://www.skhynix.com/ir/UI-FR-IR06/ returns a Nuxt JS shell with no file links, the payload.js data file is empty, and firecrawl_scrape failed with a DNS error for www.skhynix.com) - SK hynix earnings-call scripts and presentations Q4 2024 to Q3 2026. Please save the Q4 2025, Q1 2026, Q2 2026 and Q3 2026 conference-call PDFs from that page by hand. A secondary Q3 2026 transcript says lower-stack HBM "requires more cubes, which in turn increases the need for base dies and back-end processing" (lead only, see section 4)
- [SMP] NOT RETRIEVED (tried: none; host refuses scripted access per brief) - Micron FQ4 FY25 prepared remarks https://investors.micron.com/static-files/5ea95475-639b-4cfc-91fd-b9b4a2bb5e63 ; FQ1 FY26 https://investors.micron.com/static-files/088991c5-a249-4f66-a0a6-258d9b66f3f9 ; FQ2 FY26 https://investors.micron.com/static-files/e089f8c0-065d-47b8-9d02-bfa863cdb357
- [SMP] NOT RETRIEVED (tried: fetch.py, HTTP 404) - https://s25.q4cdn.com/621799436/files/doc_financials/2026/q1/Q1-FY26-Prepared-Remarks.pdf and https://s25.q4cdn.com/621799436/files/doc_financials/2026/q2/Q2-FY26-Prepared-Remarks.pdf
- [SMP] NOT RETRIEVED (tried: fetch.py via https://doi.org/ redirects to spiedigitallibrary.org, which returned an Incapsula bot challenge) - SPIE pages for 10.1117/1.JMM.24.4.041405, 10.1117/12.3085527, 10.1117/12.3093590, 10.1117/12.3090223. The four challenge pages were deleted. Their `_manifest.csv` rows dated 2025-09-12 and 2026-04-08 with issuer `spie` read RETRIEVED, but they were challenge pages, not documents
- [SMP] NOT RETRIEVED (tried: none; intel.com refuses scripted access) - Intel Foveros Direct 3D tech brief https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-11/foveros-direct-3d-tech-brief.pdf
- [SMP] NOT RETRIEVED (tried: none; hosts refuse scripted access) - TSMC quarterly earnings-call transcripts https://investor.tsmc.com/english/quarterly-results and TSMC newsroom https://pr.tsmc.com ; ASE earnings-call materials https://ir.aseglobal.com/ ; Amkor earnings-call materials https://ir.amkor.com/
- [TALK] NOT RETRIEVED (tried: none; host semicontaiwan.org refuses scripted access per brief) - https://semicontaiwan.org/en/node/20171 (Micron keynote "AI-Powered Smart Quality Ecosystem: Manufacturing Next-Generation AI Memory", Jack Lee, Micron)
- [TALK] NOT RETRIEVED (tried: none; semicontaiwan.org refuses) - https://www.semicontaiwan.org/en/node/18506 (TSMC keynote abstract, Zhihua Zou, SEMICON Taiwan 2026; also flagged by XR)
- [TALK] NOT RETRIEVED (tried: none; semicontaiwan.org refuses) - https://www.semicontaiwan.org/zh/3DIC_2026 (3DIC Global Summit, 1 Sep 2026, TSMC/ASE talks)
- [TALK] NOT RETRIEVED (tried: none; semi.org refuses) - https://www.semi.org/zh/SEMICON-Taiwan-2025/3DICAMA and https://www.semi.org/sites/semi.org/files/2025-11/01%20Ilan%20intro%20and%20Standards.pdf (3DICAMA "Metrology & Inspection" working group led by TSMC and ASE)
- [TALK] NOT RETRIEVED (tried: none; semi.org refuses) - https://www.semi.org/en/connect/events/advanced-packaging-summit-2025 (Suwon, 16 Jul 2025; D2W M&I session), https://www.semi.org/en/event/are-we-there-yet-metrology-and-inspection-angstrom-level-manufacturing, https://www.semi.org/en/imaging-across-assembly-and-test-enabling-manufacturable-complexity
- [TALK] NOT RETRIEVED (tried: fetch.py, HTTP 403) - https://www.semi.org.cn/site/semi/article/59e65455dbe84bc49f4acdd17994d2c5.html (SEMICON China 2026 heterogeneous-integration conference write-up; a female speaker on hybrid-bonding yield and cleanliness, affiliation unknown)
- [TALK] NOT RETRIEVED (tried: none; investor.tsmc.com refuses) - https://investor.tsmc.com/sites/ir/annual-report/2025/2025%20Annual%20Report.E.pdf (section 5.3.6 Quality and Reliability, advanced packaging)
- [TALK] NOT RETRIEVED (tried: none; pr.tsmc.com refuses) - https://pr.tsmc.com/static/campaign/2025March/tsmc_na/index.html (TSMC 2025 Technology Symposium); 2026 symposium pages likewise
- [TALK] NOT RETRIEVED (tried: none; www.intel.com refuses) - https://www.intel.com/content/dam/www/central-libraries/us/en/documents/2025-11/foveros-direct-3d-tech-brief.pdf and https://www.intel.com/content/www/us/en/newsroom/press-hub/press-kit/corporate/intel-foundry-direct-connect-2025.html
- [TALK] NOT RETRIEVED (tried: fetch.py, HTTP 403) - https://newsroom.intel.com/intel-foundry/intel-foundry-gathers-customers-partners-outlines-priorities
- [TALK] NOT RETRIEVED (tried: WebFetch of intc.com IR calendar; no Foundry Direct Connect presentation listed) - Intel Foundry Direct Connect 2025/2026 slide decks
- [TALK] NOT RETRIEVED (tried: fetch.py; page body behind member login) - https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=767040 and id=764808 (TSMC Jun He, Aug/Sep 2026), https://www.digitimes.com.tw/tech/dt/n/shwnws.asp?id=767019 (ASE Hung Song-jing on manufacturing bottlenecks)
- [TALK] NOT RETRIEVED (tried: Amkor blog only; ir.amkor.com refuses per brief) - Amkor 2026 Investor Day presentation (URL on ir.amkor.com not identified)
- [TALK] NOT RETRIEVED (tried: none; investors.micron.com refuses) - https://investors.micron.com/news/press-release/2025/Micron-Breaks-Ground-on-New-HBM-Advanced-Packaging-Facility-in-Singapore-01-08-2025/default.aspx
- [TALK] NOT RETRIEVED (tried: IEEE.tv page; video members-only, speaker not shown) - https://ieeetv.ieee.org/repp/metrology-challenges-in-advanced-packaging-focus-on-die-to-die-and-die-to-wafer-bonding
- [TALK] NOT RETRIEVED (tried: none; semiconkorea.org refuses) - SEMICON Korea 2025/2026 STS abstracts for the SK hynix and Samsung talks
- [TALK] NOT RETRIEVED (tried: web searches in EN/KR/ZH) - Samsung Foundry Forum / SAFE Forum 2025 material on inspection; none surfaced
- [TALK] NOT RETRIEVED (tried: web searches) - inspection/metrology content in SK hynix and Samsung 2025-26 IR presentations. No lead was found and the decks were not downloaded
- [TALK] NOT RETRIEVED (tried: WebFetch, timeout) - news.samsung.com site search for hybrid bonding
- [XR] NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/node/18506, keynote abstract, fetch.py HTTP 403; refused host, no workaround)
- [XR] NOT RETRIEVED (tried: https://semicontaiwan.org/en/Metrology_2026, 2026 forum agenda, fetch.py HTTP 403)
- [XR] NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/node/17406, speaker bio, fetch.py HTTP 403; zh version https://semicontaiwan.org/zh/node/17406 not attempted, same refused host)
- [XR] NOT RETRIEVED (tried: https://www.semicontaiwan.org/en/semiconductor_advanced_inspection_and_metrology_forum_2025, 2025 forum page, fetch.py HTTP 403)
- [XR] NOT RETRIEVED (tried: https://semihub.io/en/blog/semicon-taiwan-2026-guide.html, third-party attendee guide with the Zou slot, fetch.py HTTP 403)
- [XR] NOT RETRIEVED (tried: https://www.digitimes.com/news/a20260904VL218/tsmc-inspection-hbm-packaging-design.html full text; paywall serves teaser only)
- [XR] NOT RETRIEVED (tried: https://www.mdpi.com/2079-9292/15/22/5391, fetch.py HTTP 403; Crossref abstract used instead)
- [XR] NOT RETRIEVED (tried: full texts of https://doi.org/10.1109/TNS.2025.3561936, https://doi.org/10.1109/IRPS61424.2026.11499239, https://doi.org/10.1109/TNS.2026.3739333; ieeexplore.ieee.org refuses scripts, abstracts used)
- [XR] NOT RETRIEVED (tried: Semantic Scholar search API, 4 of 5 keyword queries returned HTTP 429; Crossref searches used instead)
- [XR] NOT RETRIEVED (tried: https://www.circuitinsight.com/uploads/2/dram_damage_due_xray_inspections_post_pcb_assembly_smta.pdf; served a non-PDF page; same paper read in SMT007 Apr 2025 PDF)
- [XR] NOT RETRIEVED (tried: https://manuscript.isc.ac/Inventory/49/1053941.htm, record said to give Micron affiliation of the 2006 IRPS paper; connection failed)
- [XR] NOT RETRIEVED (tried: https://ectc.net/wp-content/uploads/2025/06/ECTC2025_SpecialSession_6-Advances-in-Chiplets.pdf identified via search; ectc.net is a refused host, not fetched)
- [XR] NOT RETRIEVED (tried: not fetched; https://lcdproduct.com/tsmc-urges-hbm-makers-to-design-for-x-ray-inspection-as-packaging-grows-more-complex/ appears to republish the paywalled DIGITIMES article)
- [MAIN] NOT RETRIEVED (tried: Crossref container-title listing on 2026-11-21, 0 records) - IITC 2026 proceedings in Crossref; programme page read instead (sources/customer_side/2026-11-21_iitc_IITC2026-program-page.html)
- [MAIN] NOT RETRIEVED (tried: Crossref container-title listing on 2026-11-21, 0 records) - IPFA 2026 proceedings
- [MAIN] NOT RETRIEVED (tried: fetch.py, Incapsula / 'Pardon Our Interruption' challenge on spiedigitallibrary.org and spie.org) - SPIE paper pages, author affiliations and full texts for all SPIE AL+P 2025/2026 papers
- [MAIN] NOT RETRIEVED (tried: api.openalex.org, HTTP 429, network's free daily budget exhausted; an API key would require the user's email) - OpenAlex records
- [MAIN] NOT RETRIEVED (tried: ieeexplore.ieee.org, HTTP 202 bot challenge) - full texts of all IEEE conference papers (ECTC, IEDM, IRPS, VLSI, IITC, ASMC, EPTC, IPFA, ITC, IMW)
- [MAIN] NOT RETRIEVED (tried: https://www.ectc.net/, HTTP 403) - ECTC 2025/2026 programmes and special-session slides
- [MAIN] NOT RETRIEVED (tried: tsmc.com, pr.tsmc.com, esg.tsmc.com, investor.tsmc.com; Cloudflare challenge) - all TSMC-hosted documents (releases, technology symposium, annual report, ESG report)
- [MAIN] NOT RETRIEVED (tried: www.semi.org, www.semicontaiwan.org, www.semiconkorea.org; Cloudflare challenge) - SEMICON forum agendas and talk abstracts
- [MAIN] NOT RETRIEVED (tried: www.intel.com and newsroom.intel.com, HTTP 403) - Intel newsroom, Foundry Direct Connect material, Foveros Direct brief
- [MAIN] NOT RETRIEVED (tried: www.aseglobal.com and ir.aseglobal.com, HTTP 403) - ASE releases and IR material
- [MAIN] NOT RETRIEVED (tried: ir.amkor.com, HTTP 403) - Amkor IR material
- [MAIN] NOT RETRIEVED (tried: investors.micron.com, HTTP 403) - Micron IR releases and prepared remarks hosted there

## NOT DISCLOSED (68)

- [ADDL] NOT DISCLOSED (read: 2026-06-08_swtest_tsmc-hpc-testing-ai-era-deck.pdf, pp1-28) - production status of each test insertion, production counts, tester/prober/probe-card vendors, and any HBM test or inspection method beyond the "HBM Base die" label
- [ADDL] NOT DISCLOSED (read: 2026-06-08_swtest_intel-formfactor-microbump-probing-hvm-deck.pdf, pp1-16) - HBM; the X-ray technique used in materials characterization; the bump-deformation measurement method
- [ADDL] NOT DISCLOSED (read: 2026-06-08_swtest_intel-technoprobe-native-pitch-microbump-probing-deck.pdf, p13) - bump-height instrument and values
- [ADDL] NOT DISCLOSED (read: 2026-11-21_semanticscholar_record-10.1109-impact67645.2025.11281768.json, abstract) - optical principle, tool vendor, reference instruments, and whether AOM runs in production
- [ADDL] NOT DISCLOSED (read: 2026-11-21_semanticscholar_record-10.1109-impact67645.2025.11281550.json, abstract) - whether the models run on ASE production lines, and the product or inspection station
- [ADDL] NOT DISCLOSED (read: 2026-09-07_aseh_sustainability-report-2025-en.pdf, full-text search of 248 pages for "HBM", "high bandwidth memory", "hybrid bond") - any HBM or hybrid-bond inspection or metrology
- [ADDL] NOT DISCLOSED (read: 2026-11-21_amkor_web-smart-manufacturing.html, full page) - which package lines or process steps use ADC; HBM
- [ADDL] NOT DISCLOSED (read: 2026-11-21_amkor_event-itc-2026-osat-test-perspective.html, body) - test-time numbers, HBM, test methods
- [ADDL] NOT DISCLOSED (read: 2025-01-02_googlepatents_intel-US20250006651A1-slit-fiducials.html, description) - production use and metrology tool vendor
- [ADDM] NOT DISCLOSED (read: 2026-03-18_pathlms_fcmn2026-samsung-hybrid-metrology-se-xrd-deck.pdf, pp1-17) - conference name and place; only the date 26.03.18 is printed. One check of a NIST page found nothing
- [ADDM] NOT DISCLOSED (read: 2025-04-10_nova_spie-mipc39-samsung-nova-3dnand-hcb-metrology-paper.pdf, pp1-7) - SAM, AFM and interferometry tool vendors used for voids and Cu recess, and the correlation coefficient between the interferometry map and the SAM void map
- [ADDM] NOT DISCLOSED (read: 2026-10-27_imaps_samsung-warpage-control-3d-packaging-paper.pdf, pp1-6) - warpage measurement principle and tool vendor ("automated inspection tools" only)
- [ADDM] NOT DISCLOSED (read: 2025-06-23_pmc_acsomega-sicn-wafer-bonding-skhynix-ynu-tel.html, sections 2 and 3.2) - SAM instrument and vendor
- [ADDM] NOT DISCLOSED (read: 2025-06-10_micron_release-hbm4-ships-key-customers.html, release body) - what Micron's HBM4 MBIST covers
- [ADDM] NOT DISCLOSED (read: 2026-09-03_bnext_micron-deboer-semicon-taiwan-2026-vertical-hbm.html, article body) - any metrology method named by DeBoer
- [AW] NOT DISCLOSED (read: SK hynix Newsroom KR, '2025 파트너스데이' 2025-09-30, full article) - names of the 14 winners of 2025
- [AW] NOT DISCLOSED (read: SK hynix Newsroom KR, '2026 파트너스데이' 2026-09-29, full article and three photo-caption pages) - names of the 11 winners of 2026
- [AW] NOT DISCLOSED (read: Samsung Newsroom KR, 'DS부문 2026년 상생협력 DAY' 2026-04-03, and the identical Samsung Semiconductor newsroom copy) - 13 of 17 Samsung DS 2026 winners
- [AW] NOT DISCLOSED (read: Samsung Semiconductor Newsroom KR, '2025년 DS 상생협력 Day 현장' 2025-04-30) - the reason for Korea Instrument's award
- [AW] NOT DISCLOSED (read: Micron blog 2025-10-31) - the exact date of the 2025 Micron Supplier Awards ceremony ('last week')
- [AW] NOT DISCLOSED (read: Micron blog 2026-10-22 and Micron 'Supplier day & awards' page) - the exact date of the 2026 Supplier Day
- [AW] NOT DISCLOSED (read: FormFactor blog 2026-03-25; Lasertec release 2026-03-25; AEM announcement 2026-03-19; Camtek release 2025-04-08; Lasertec release 2025-04-09) - Intel award categories in the vendors' own texts
- [PAPL] NOT DISCLOSED (read: research/sources/customer_side/2026-11-21_semanticscholar_chipmaker-papers-2025-26-part1.json, abstract of 10.1109/ECTC51846.2026.00059) - Void-detection method in ASE CoW hybrid-bonding void paper
- [PAPL] NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51846.2026.00354) - Imaging wavelength, tool, repeatability and throughput values of Intel 100% overlay metrology
- [PAPL] NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51846.2026.00030) - NIR overlay tool maker and overlay accuracy numbers
- [PAPL] NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51687.2025.00026) - Warpage and in-line inspection methods for large CoWoS-R
- [PAPL] NOT DISCLOSED (read: same part1 file, abstract of 10.1109/ECTC51846.2026.00224) - Cu pad recess measurement method
- [PAPL] NOT DISCLOSED (read: same part1 file, abstract of 10.1109/EPTC67330.2025.11392617) - Wafer warpage measurement method, FOEB-T
- [PAPL] NOT DISCLOSED (read: same part1 file, abstracts of 10.1109/ECTC51687.2025.00313, 10.1109/ECTC51846.2026.00245, 10.1109/ECTC51846.2026.00249) - Makers of the cSAM, FIB-SEM and 3D XRM tools used by Intel and ASE
- [PAPL] NOT DISCLOSED (read: abstracts of all 26 in-table papers, same part1/part2 files) - Production or HVM status of any inspection method in the table. . The only production words concern the CoWoS-R platform ([C] PAPL-008, PAPL-136), not an inspection step
- [PAPM] NOT DISCLOSED (read: 2026-11-21_semanticscholar_chipmaker-papers-2025-26-part1.json and -part2.json, abstracts of all 264 three-company papers that have one) - X-ray CT / laminography / 2D X-ray for HBM, TSV or bonding in SK hynix, Samsung or Micron abstracts
- [PAPM] NOT DISCLOSED (read: same files, abstracts) - AFM for pre-bond Cu recess or dishing in the three companies' abstracts: . The Samsung wet-ALE paper targets nm-level Cu recess, but its abstract names no measurement
- [PAPM] NOT DISCLOSED (read: same files, abstracts) - Infrared inspection of bonded interfaces or bond overlay in the three companies' conference abstracts: . The conference mention of IR is Samsung's statement that IR OBIRCH/photoemission reach their limits in V-NAND FA (PAPM-086). IR for post-bond die shift/tilt does appear in SK hynix's JSTS 2025 paper (PAPM-213)
- [PAPM] NOT DISCLOSED (read: 2026-11-21_jsts_paper-hbm-chip-warpage-thin-wafer.html, full text) - Supplier of SK hynix's commercialized in-line chip-warpage solution
- [PAPM] NOT DISCLOSED (read: 2025-10-31_jsts_paper-hbm-stacked-die-ir-metrology-cv.html, full text) - Supplier or wavelength of the IR die-shift tool in SK hynix's JSTS paper
- [PAPM] NOT DISCLOSED (read: 2026-11-21_crossref_cr-jsts-2025-25-5-585-skhynix-hbm-warpage.json and 2026-11-21_crossref_search-jsts-2025-26-affiliation.json, author records; the affiliation query returned 0 results) - Affiliations in Crossref for JSTS 2025-26 records
- [PAPM] NOT DISCLOSED (read: 2026-11-21_semanticscholar_chipmaker-papers-2025-26-part2.json, abstract of 10.1109/vlsitechnologyandcir65830.2026.11577576) - Die-warpage measurement method in SK hynix HBM4
- [PAPM] NOT DISCLOSED (read: 2026-11-21_semanticscholar_chipmaker-papers-2025-26-part2.json, abstract of 10.1109/vlsitechnologyandcir65830.2026.11577637) - Bond-overlay metrology in Samsung CMB V-NAND
- [PAPM] NOT DISCLOSED (read: same files, abstracts, and the three SK hynix JSTS full texts) - Tool maker for any HBM / hybrid-bonding measurement by the three companies
- [PAPM] NOT DISCLOSED (read: abstracts as cited in `PAPM_table.csv`) - Status (pilot, HVM, in-line) for 21 of 45 table rows
- [PAPM] NOT DISCLOSED (read: 2026-11-21_crossref_SPIE-MIPC-XXXIX-2025-volume-list.json and -XL-2026-volume-list.json, author records) - Affiliations of all SPIE MIPC XXXIX/XL records
- [SMP] NOT DISCLOSED (read: Intel Q4 2025, Q1 2026 and Q2 2026 earnings-call prepared remarks, full text) - no statement on test or inspection steps, sampling or test time for Foveros/hybrid bonding or advanced packaging
- [SMP] NOT DISCLOSED (read: Micron FQ3 FY25, FQ3 FY26 and FQ4 FY26 earnings-call prepared remarks, full text) - no statement on HBM test time, test insertions or inspection sampling
- [SMP] NOT DISCLOSED (read: Samsung Electronics 3Q26 results release, news.samsung.com, full text) - no statement on HBM test or inspection intensity
- [SMP] NOT DISCLOSED (read: Samsung Semiconductor newsroom interview 2026-04-14, full text) - no sampling rate, throughput or defect-rate numbers for the new HBM monitoring solution
- [SMP] NOT DISCLOSED (read: SK hynix newsroom 2025-05-02 Doh article, full text) - no % reduction in physical measurements and no cycle-time figure for VM
- [SMP] NOT DISCLOSED (read: Micron blog 2025-12-09, full text) - no HBM-specific inspection or test intensity statement
- [TALK] NOT DISCLOSED (read: SK hynix Newsroom, [Tech Note] Hybrid Bonding, 2026-08-25, full text) - any inspection or metrology method for hybrid-bonded HBM
- [TALK] NOT DISCLOSED (read: SK hynix Newsroom, HBM4 development completion, 2025-09-12, full text) - inspection or test method for HBM4 / Advanced MR-MUF
- [TALK] NOT DISCLOSED (read: SK hynix Newsroom, 12-layer HBM4E samples, 2026-06-18, full text) - inspection or test method
- [TALK] NOT DISCLOSED (read: SK hynix Newsroom (KR), Technology Innovation Companies 8th cohort, 2025-08-25) - measurement principle of the NexSensor warpage tool and of the Cobis "hybrid wafer" metrology tool
- [TALK] NOT DISCLOSED (read: SK hynix Newsroom, SEMICON Korea 2026, 2026-02-12) - content of the STS overlay/CMP talk beyond its title
- [TALK] NOT DISCLOSED (read: Samsung Newsroom, "Samsung ships industry-first commercial HBM4", 2026-02-12) - bonding method and any inspection method
- [TALK] NOT DISCLOSED (read: Samsung Semiconductor HBM3E product page, FAQ) - inspection method for HCB; dates of adoption
- [TALK] NOT DISCLOSED (read: VLSI 2025 Workshop 9 program page, Samsung and Micron abstracts) - production status, throughput, resolution, sample damage
- [TALK] NOT DISCLOSED (read: Micron blog "Smart manufacturing at Micron", 2025-12-09) - HBM-specific inspection steps or tools
- [TALK] NOT DISCLOSED (read: Amkor IMAPS 2025 paper "Module Stress Reduction for 2.5D TSV-based Heterogeneous Package", pp1-5) - warpage measurement method/tool; SAT tool vendor and resolution
- [TALK] NOT DISCLOSED (read: Amkor blog "2026 Investor Day", 2026-05-29 and "ECTC 2026", 2026-06-05) - any inspection or metrology content
- [XR] NOT DISCLOSED (read: SMT007 Apr 2025 Intel article pp46-56, DRAM manufacturer's X-ray dose limit value and supplier name)
- [XR] NOT DISCLOSED (read: SMT007 Apr 2025 Intel article pp49-55, numeric dosimeter readings; figures only)
- [XR] NOT DISCLOSED (read: Semantic Scholar abstract of 10.1109/TNS.2025.3561936, X-ray dose values)
- [XR] NOT DISCLOSED (read: Semantic Scholar abstract of 10.1109/IRPS61424.2026.11499239, TID threshold value)
- [XR] NOT DISCLOSED (read: US 2026/0126403 A1 description, dose numbers and failure mode)
- [XR] NOT DISCLOSED (read: Crossref abstract of 10.31399/asm.cp.istfa2026p0587, dose or damage)
- [XR] NOT DISCLOSED (read: Semantic Scholar abstract of 10.23919/ICEP-IAAC64884.2025.11003029, dose or damage)
- [XR] NOT DISCLOSED (read: DIGITIMES 2026-09-04 teaser and caption, dose numbers and TSMC's exact wording)
- [MAIN] NOT DISCLOSED (read: 2026-11-21_iitc_IITC2026-program-page.html, full programme) - any IITC 2026 paper by the seven on inspecting or measuring HBM or hybrid bonds
- [MAIN] NOT DISCLOSED (read: Crossref records of 85 of 3,378 IEEE/ASM records in the volume listings) - author affiliations (those papers are invisible to the affiliation scan)
