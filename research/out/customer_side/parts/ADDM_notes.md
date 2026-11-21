# ADDM notes: gap-fill for SK hynix, Samsung and Micron (critic list, 11 candidates; run 2026-11-21)

Files: `ADDM.csv` (65 evidence rows: 54 [F], 6 [C], 5 [S], 0 [I]; all 65 quotes FOUND by `quote_check.py`), `ADDM_table.csv` (15 method rows, 9 documents).
All documents were fetched with `research/tools/fetch.py` and saved under `research/sources/customer_side/`. Period: 1 Jan 2025 to 21 Nov 2026. Every added item falls inside it, so there are no out-of-period rows.
Nothing here is about an HBM stack except the Micron HBM4 release (ADDM-057 to ADDM-059) and the DeBoer report (ADDM-060 to ADDM-062). The hybrid-bonding items are 3D NAND CMOS-to-array wafer-to-wafer bonding (Samsung) or lab SiCN wafer bonding (SK hynix co-authored).

## 1. Findings

### 1.1 Samsung
- **Samsung-led paper: metrology for hybrid Cu bonding in 3D NAND (SPIE MIPC XXXIX, Feb 2025).** This is the most specific item added.
  - Authors: two of three are from the Samsung Flash Process Development Team, Semiconductor R&D Center, including the first and corresponding author. The third author is from Nova (Strategic Marketing) (ADDM-001). The Crossref record confirms the DOI 10.1117/12.3050400, the venue and the title (ADDM-002).
  - Source: the full text is the author manuscript that co-author Nova posts on novami.com. It is not the SPIE page.
  - Scope: wafer-to-wafer HCB of the CMOS periphery wafer to the memory-array wafer in 3D NAND (ADDM-003).
  - Key monitoring items: five factors drive bonding voids (Cu pad recess, erosion, local step height, edge roll-off, particles) (ADDM-004). The authors say warpage must be monitored at every step (ADDM-005). Voids larger than 100 um cause wafer breakage at backside thinning (ADDM-006).
  - Post-bond voids:
    - SAM produces the void maps, including before and after CMP optimisation (ADDM-010).
    - A full-wafer SAM scan takes 10-20 min, so Samsung "developed" an interferometry alternative (ADDM-007). It gives a surface map in under a minute that "closely correlates" with the SAM void map; the correlation is not quantified (ADDM-008).
    - SAM limits stated: penetration depth and slow throughput limit small-void detection (ADDM-009).
  - Pre-bond Cu recess:
    - AFM achieves sub-nm vertical resolution (ADDM-011).
    - Its low throughput "remains a challenge" for HVM (ADDM-012).
    - The three types of high-speed AFM are "still in their early stages" (ADDM-013).
  - Wafer edge roll-off: four technologies were compared (stylus, AFM, confocal, interferometer; Table 1 read from the page image) (ADDM-014). ERO profiles were measured with Nova's broadband spectral interferometry (ADDM-015). The paper concludes that current methods "show performance limitations" (ADDM-016).
- **Samsung-led deck on memory CD metrology (dated 2026-03-18; venue not printed in the deck).**
  - Authors: three Samsung DS Division authors, plus one co-author each from Onto and Rigaku (ADDM-017).
  - Optical SE limit: SE loses structural resolution in deep VNAND, word lines ~200 to ~400 (ADDM-018). X-ray diffraction CD (XCD, with a CD-SAXS slide) is adopted for deep structures (ADDM-019).
  - Results: measurement time fell from 30 min to about 5.7 min with correlation kept (ADDM-021). Onto's MGML raised correlation, e.g. 0.63 to 0.72 (ADDM-023).
  - Claims tagged [C]: "Production-Level Measurement Capability" (ADDM-020) and "production-ready recipes" (ADDM-024).
  - Limits stated: a "Remaining Challenges in Production XCD Metrology" slide (ADDM-022) and future work to cut scan time (ADDM-025).
  - This is VNAND, not HBM. The deck has no wording on X-ray dose or damage.
- **Samsung warpage paper at IMAPS 2026 Symposium (Oct 2026; all 12 authors Samsung).**
  - Vehicle: a TSV silicon interposer with C4 micro-bumps and chip-on-wafer stacking; HBM is not stated (ADDM-049, ADDM-050).
  - Measurement: warpage is quantified right after debonding "using automated inspection tools"; the tool type and vendor are not named (ADDM-051). Results are cross-checked against FEA (ADDM-052).
  - Results: EMC Material B gave about -500 um (ADDM-053); more interposer BEOL metal gave about +500 um (ADDM-054); material changes gave up to -1000 um cumulatively (ADDM-055); TEL-processed carriers showed more warpage than SUSS ones (ADDM-056).
- **Samsung virtual-metrology paper (SISPAD 2025, Sep 2025; all 12 authors Samsung: 7 SR&D Center, 5 Foundry).** It combines data-driven VM with 3D TCAD to predict CMP surface non-uniformity on full-chip layouts: about two billion points in four hours (ADDM-037 to ADDM-040). The abstract does not mention bonding, memory or HBM. Do not cite it for hybrid bonding without the full text.

### 1.2 SK hynix
- **SiCN wafer bonding paper, ACS Omega (Jun 2025; full text on PMC).**
  - Authorship: university-led. The corresponding author is at Yokohama National University. Three of eight authors are SK hynix, with one each from TEL Kyushu and the University of Tsukuba (ADDM-041).
  - SK hynix role: per the contribution statement, SK hynix authors supervised process procedures and prepared samples with TEL (ADDM-042).
  - Methods:
    - a SAM image of the as-bonded interface (ADDM-043);
    - a double-cantilever-beam bond-strength test on a custom rig (ADDM-044), with a time-dependent DCB in N2 for interfacial water (ADDM-045);
    - PAS, TEM/EELS (JEOL), XPS, ellipsometry (J.A. Woollam), TDS, RBS-ERDA and ESR (ADDM-046).
  - Result: higher bond strength after a 250 C anneal (ADDM-047).
  - Status: lab study on 300 mm wafers, not HBM.
- **Companion paper, ACS Applied Electronic Materials (Apr 2026).** It covers bond-wave dynamics and distortion-induced scaling errors (bond overlay). Three of eight authors are SK hynix, one is TEL Kyushu and four are YNU (ADDM-048). Only the title and affiliations were read; no method is disclosed in the saved records.
- **Infinitesima Metron3D (in-line high-speed AFM).** The vendor's homepage quotes "Young-Hyun Choi, Head of DMI, SK hynix" (ADDM-063). The quote says Metron3D "has demonstrated excellent sub-nanometre 3D metrology with the required cost-of-ownership necessary for HVM implementation", in the context of "advanced DRAM processes" (ADDM-064). This is vendor material quoting a chipmaker executive, so it is tagged [S].
  - The volume-production release of 8 Jul 2025 is NOT RETRIEVED (see section 2), so "released for use in volume production" is not in any row.
  - The vendor separately claims that Metron3D measures hybrid-bonding Cu recess, dishing and erosion at 60 WPH (ADDM-065, [C], no chipmaker named). This matches the high-speed AFM need that Samsung states in ADDM-012 and ADDM-013. Whether SK hynix uses Metron3D for HBM or hybrid bonding is not shown in any saved document.

### 1.3 Micron
- **HBM4 press release (10 Jun 2025).**
  - Micron says it shipped HBM4 36GB 12-high samples to multiple key customers (ADDM-057).
  - HBM4 has a "highly capable memory built-in self-test (MBIST) feature" (ADDM-058); its scope is not described.
  - Micron plans to ramp in CY2026 (ADDM-059).
  - All three rows are [C].
- **XRR paper, Surface and Interface Analysis (Jan 2026; all 6 authors Micron Boise).**
  - Method: 3D NAND ONON stacks measured by XRR against TEM (ADDM-026, ADDM-027).
  - Purpose: to "validate XRR as a process line monitoring tool" (ADDM-028).
  - Status: the paper supports "future implementation" in manufacturing and does not state production use (ADDM-029).
  - Limits are "discussed" but not given in the abstract (ADDM-030).
  - Read from the abstract only.
- **E-beam inspection paper, ICMTS 2025 (Mar 2025; Micron-led, 4 of 6 authors Micron).** The other 2 authors are ASML field-application engineers (ADDM-031, ADDM-032). Fractal points for EBI in DRAM manufacturing (ADDM-033) gave -98.1% nuisance defects and +255.7% defects of interest (ADDM-034), plus a 10,000x resolution gain (ADDM-035). The stated aim is faster yield learning before probe (ADDM-036). Read from the abstract only; DRAM front end, not HBM.
- **DeBoer keynote, SEMICON Taiwan 2026 Master Forum (2 Sep 2026), as reported by Business Next on 3 Sep 2026 [S].**
  - Speaker: Scott DeBoer, Micron President and Chief Technology & Products Officer (ADDM-060).
  - Reported quote: in large-scale mass-production capability, hybrid bonding is "clearly behind" (ADDM-061).
  - Reporter's paraphrase: D2W and W2W bonding "and related metrology" still need substantial improvement before vertical HBM reaches volume (ADDM-062).
  - DeBoer names no metrology method, so this item is not in `ADDM_table.csv`.

## 2. Gaps
- NOT RETRIEVED (tried: https://s24.q4cdn.com/480160064/files/doc_news/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production.pdf with fetch.py, HTTP 404; investors.ontoinnovation.com not tried, host refuses scripts; stocktitan.net copy not used, republisher) - Onto release on its SK hynix 2026 Best Partner Award. Please save by hand: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production/default.aspx
- NOT RETRIEVED (tried: https://www.globenewswire.com/news-release/2025/07/08/3111447/0/en/Infinitesima-Metron-3D-300mm-System-Released-for-In-line-Process-Control-by-Leading-DRAM-Manufacturer.html with fetch.py, HTTP 403; https://infinitesima.com/news/ HTTP 404; https://infinitesima.com/insights lists 2026 items only; storagenewsletter.com copy not used, republisher) - Infinitesima release of 8 Jul 2025 saying SK hynix released Metron3D for volume production. Please save the GlobeNewswire page by hand.
- NOT RETRIEVED (tried: https://pubs.acs.org/doi/10.1021/acsaelm.6c00446 with fetch.py, HTTP 403) - abstract and full text of the SK hynix co-authored bond-wave / scaling-error paper.
- NOT RETRIEVED (tried: https://onlinelibrary.wiley.com/doi/10.1002/sia.70044 with fetch.py, HTTP 403) - full text of the Micron XRR paper.
- NOT RETRIEVED (tried: none, ieeexplore.ieee.org bot challenge) - full texts of https://doi.org/10.1109/icmts63811.2025.11068899 and https://doi.org/10.1109/sispad66650.2025.11186319.
- NOT DISCLOSED (read: 2026-03-18_pathlms_fcmn2026-samsung-hybrid-metrology-se-xrd-deck.pdf, pp1-17) - conference name and place; only the date 26.03.18 is printed. One check of a NIST page found nothing.
- NOT DISCLOSED (read: 2025-04-10_nova_spie-mipc39-samsung-nova-3dnand-hcb-metrology-paper.pdf, pp1-7) - SAM, AFM and interferometry tool vendors used for voids and Cu recess, and the correlation coefficient between the interferometry map and the SAM void map.
- NOT DISCLOSED (read: 2026-10-27_imaps_samsung-warpage-control-3d-packaging-paper.pdf, pp1-6) - warpage measurement principle and tool vendor ("automated inspection tools" only).
- NOT DISCLOSED (read: 2025-06-23_pmc_acsomega-sicn-wafer-bonding-skhynix-ynu-tel.html, sections 2 and 3.2) - SAM instrument and vendor.
- NOT DISCLOSED (read: 2025-06-10_micron_release-hbm4-ships-key-customers.html, release body) - what Micron's HBM4 MBIST covers.
- NOT DISCLOSED (read: 2026-09-03_bnext_micron-deboer-semicon-taiwan-2026-vertical-hbm.html, article body) - any metrology method named by DeBoer.
- NOT DISCLOSED (read: 2026-11-21_crossref_record-10.1021-acsaelm.6c00446.json and 2026-11-21_semanticscholar_record-10.1021-acsaelm.6c00446.json) - measurement method of the AEM paper (no abstract in either record).

## 3. Premise problems in the critic list
- **Samsung/Nova paper.** Semantic Scholar gives the venue as "Advanced Lithography". The Crossref record says Metrology, Inspection, and Process Control XXXIX, San Jose, 23-27 Feb 2025, and I used Crossref. The critic's quote "SAM requires 10 to 20 minutes..." is correct.
- **FCMN deck.** "FCMN, Monterey, 18 Mar 2026" is not printed in the deck; only the date is. I kept FCMN as unconfirmed.
- **Onto award.** The critic proposed the StockTitan copy. That is a republishing site, so I did not use it (access rule).
- **Infinitesima.** The critic expanded DMI as "Defect Analysis, Metrology and Inspection Technology". The saved vendor page says only "Head of DMI, SK hynix", so I did not quote the expansion. A search snippet (GlobalSpec) attributes Choi to Infinitesima; the saved page attributes him to SK hynix. The critic cited a StorageNewsletter copy, which is a republisher and was not used.
- **ACS Omega authors.** The critic listed 3 SK hynix authors with YNU and TEL. The author list also has a University of Tsukuba author (Uedono, PAS measurements). The contribution statement names "H.K.", who is not among the authors.
- **Micron XRR status.** "Not yet in production" is the critic's inference. The abstract says only "future implementation"; I recorded it in the authors' words (ADDM-029).
- **DeBoer quote.** The English wording is a translation of a Chinese press report. No Micron transcript was retrieved.

## 4. Candidates not added, or added in part
- Onto Innovation release on the SK hynix Best Partner Award (2026-10-12): **not added**. The issuer copy is NOT RETRIEVED and republisher copies are barred. SK hynix's own Partners Day article does not name Onto; it is already in the dossier as AW-034.
- Infinitesima release "SK hynix ... released it for use in volume production" (2025-07-08): **added in part**. The release is NOT RETRIEVED. Only the SK hynix executive quote on the vendor's own homepage was added, as [S] (ADDM-063, ADDM-064), plus a vendor self-claim (ADDM-065). The Bits&Chips article tying Metron3D to HBM was not fetched; it remains an unverified lead (https://bits-chips.com/article/sk-hynix-to-use-infinitesimas-afm-metrology-in-hbm-production/).
- ACS AEM companion paper (10.1021/acsaelm.6c00446): **added in part**, title and affiliations only (ADDM-048).
- The other 8 candidates were added in full: the Samsung/Nova SPIE paper, the FCMN deck, Micron XRR, Micron DeBoer [S], Micron ICMTS EBI, the Micron HBM4 release, Samsung SISPAD, and Samsung IMAPS.

## 5. Unverified leads
- Bits&Chips, "SK hynix to use Infinitesima's AFM metrology in HBM production" (https://bits-chips.com/article/sk-hynix-to-use-infinitesimas-afm-metrology-in-hbm-production/). It would tie Metron3D to HBM, as [S]. Not fetched.
- Onto Innovation FCMN 2026 abstract "Spectrum-to-Structure Hybrid Metrology" (https://cdn.fs.pathlms.com/t3l4lLXrS1uu6KBlZ64w?dl=true, from a search result). This is vendor material; whether a chipmaker co-authored it is unknown. Not fetched.
