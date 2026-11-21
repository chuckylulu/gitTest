# Module AW - supplier awards 2025-2026 (customer_side run, 2026-11-21)

Scope: supplier-award events held or announced 1 Jan 2025 - 21 Nov 2026 by SK hynix, Samsung Electronics (DS), Micron, TSMC, Intel, ASE (incl. SPIL) and Amkor, and which inspection, metrology or test vendors won.
Files: `parts/AW.csv` (60 evidence rows), `parts/AW_table.csv` (193 winner rows), `calc/AW_counts.py` (counts behind AW-058).
Reading rule used: a winner row is [F] only when the chipmaker's own page or the winning vendor's own release was saved and read; press lists are [S]. vendor_class is my classification by company type (single value: inspection, metrology, test or other), not by the product each award cites. KLA, Camtek, Lasertec, V5 and TRI are tagged inspection; Onto and Nova metrology; Advantest, Teradyne, Technoprobe, FormFactor, Keysight, AEM, Hon Precision and Korea Instrument test. Diversified tool makers (Applied Materials, ASML, Tokyo Electron, Canon, DISCO) are tagged other, because no award category names a process-control product.

## 1. Findings

### Overview (output of `calc/AW_counts.py`)

| chipmaker | event | date | winners listed in source | insp/metro/test | names |
|---|---|---|---|---|---|
| TSMC | 2025 SCM Forum - Excellent Performance Awards | 2025-11-25 | 30 | 3 | Advantest [test], KLA [inspection], Onto Innovation [metrology] |
| TSMC | 2026 SCM Forum - Excellent Performance Awards | 2026-11-17 | 35 | 4 | Advantest [test], KLA [inspection], Lasertec [inspection], V5 Technologies [inspection] |
| Intel | 2025 EPIC Supplier Awards | 2025-04-08 | 37 | 5 | Camtek [inspection], Keysight [test], KLA [inspection], Lasertec [inspection], Technoprobe [test] |
| Intel | 2026 EPIC Supplier Awards (41 recipients) | 2026-03-19 | 2 (partial list) | 2 | Camtek [inspection], Nova [metrology] (+ Lasertec, FormFactor, AEM from vendor releases) |
| Samsung Electronics (DS) | 2025 DS 상생협력 Day | 2025-04-25 | 9 | 1 | Korea Instrument [test] |
| Samsung Electronics (DS) | 2026 DS 상생협력 DAY (17 winners) | 2026-04-03 | 4 (partial list) | 0 | - |
| Micron | Micron Supplier Awards 2025 | 2025-10 | 14 | 0 | - |
| Micron | Micron Supplier Awards 2026 (Supplier Day, Boise) | 2026-10 | 13 companies / 14 awards | 0 | - |
| ASE (incl. SPIL) | 2024 Best Supplier Awards (ceremony Apr 2025) | 2025-04-11 | 17 | 2 | Teradyne [test], Test Research Inc. [inspection] |
| ASE (incl. SPIL) | 2025 Best Supplier + Sustainability Awards (ceremony Apr 2026) | 2026-04-24 | 22 | 2 | Advantest Taiwan [test], Hon Precision [test] |
| Amkor | Amkor Supplier Award to Henkel (blog) | 2025-04-17 | 1 (partial) | 0 | - |

Full lists only: 17 inspection/metrology/test entries out of 177 listed winner entries (9.6%) (AW-058, [I], Medium).
Events found but without readable winner names: SK hynix Partners Day 2025 (14 winners) and 2026 (11 winners); Amkor Supplier Excellence Award 2025 (9 Dec 2025); TSMC OIP Partner of the Year 2025 (only Teradyne's own release read).

### TSMC
- **2025 SCM Forum, 25 Nov 2025 (not December).** 30 winners; press reproduces TSMC's alphabetical list (AW-001, AW-002). Inspection/metrology/test winners, all in 卓越量產支援 (Excellent Production Support): Advantest (AW-003), KLA (AW-004), Onto Innovation (AW-005). Advantest and Onto state the same award in their own releases (AW-006, AW-008). Both describe the rationale, in the vendors' own words, as capacity flexibility and delivery support, not a specific inspection or test product (AW-007, AW-009; Onto's is its own paraphrase of TSMC, tagged [C]). Tokyo Electron was absent from the 2025 list (AW-010). TSMC's own release was not read (pr.tsmc.com refuses scripts).
- **2026 SCM Forum, 17 Nov 2026 (already held).** 35 winners, up from 30 (AW-011, AW-012). Inspection/metrology/test winners: Advantest (Excellent Production Support, second year running; AW-013); KLA with two awards, 卓越技術暨量產支援 (Excellent Technology and Production Support) and 卓越綠色製造 (Excellent Green Manufacturing) (AW-014); Lasertec, not on the 2025 list, Excellent Production Support (AW-015); and V5 Technologies (倍利科技), not on the 2025 list, Excellent Production Support (AW-016). V5 is a Taiwanese AI-plus-optical inspection maker that listed in March 2026 (AW-017). Onto is not on the 2026 list. Tokyo Electron returns in 2026 under Excellent Production Support (AW-018). SPIL is itself a 2026 TSMC award winner (卓越先進封測量產支援, Excellent Advanced Packaging and Test Production Support; AW_table, AW-011).
- **TSMC OIP Partner of the Year 2025 (24 Sep 2025, Santa Clara).** Teradyne states it won for "TSMC 3DFabric Testing", citing multi-die test methods for chiplets and CoWoS (AW-019). This is a design-ecosystem award, separate from the SCM Forum supplier awards. TSMC's own OIP list was not read. No 2026 3DFabric Testing winner was found.

### Intel
- **2025 EPIC Supplier Awards, announced 8 Apr 2025, 37 recipients** (AW-020; Camtek and Lasertec releases state the same count of 37, AW-026, AW-027). Inspection/metrology/test winners with mynavi's Japanese rendering of Intel's categories: Camtek, 技術開発での価格競争力 (price competitiveness in technology development) (AW-021); Keysight, 技術実装 (technology implementation) (AW-022); KLA, 技術開発 (technology development) (AW-023); Lasertec, EUVマスク技術開発 (EUV mask technology development) (AW-024); Technoprobe, ソート/テストの開発 (sort/test development) (AW-025). Intel's English category wording was not read.
- **2026 EPIC Supplier Awards, 41 recipients (announced 19 Mar 2026 per AEM's release date).** Vendor releases: Lasertec (AW-028), FormFactor (AW-029, category not stated) and AEM Holdings, which calls itself a global leader in test innovation (AW-030). Israeli press adds Camtek and Nova (AW-031). Intel's list and categories were not read. KLA's presence and the categories are search leads only (section 4).

### SK hynix
- **2025 Partners Day, 29 Sep 2025:** 14 winners in four categories (technology innovation, quality improvement, shared growth, ESG). SK hynix's page names none (AW-032). Only one winner was identified, ULVAC (Best Partner Award, sputtering tool; AW-033). ULVAC's claim that its ENTRON tool is qualified as POR at SK hynix is untestable ([C], AW-059). No inspection, metrology or test winner could be identified for 2025.
- **2026 Partners Day, 28 Sep 2026 (Co-Growth Council 25th anniversary):** 11 winners in four categories, again unnamed (AW-034). Onto Innovation reportedly received a Best Partner Award for technology achievement, tied to HBM hidden-defect inspection (Dragonfly G5). Its release could not be saved (investors.ontoinnovation.com refuses scripts; the Business Wire copy failed), so this is a lead only (section 4). It is the single most relevant item in this module.
- **First Japan Partners Day, 29 Oct 2026 (Chiba):** about 20 partners attended, including Advantest and DISCO. The article mentions no awards (AW-035).
- Out-of-period context: FormFactor reported an SK hynix Best Partner Award in Nov 2024 for HBM probe cards (AW-036).

### Samsung Electronics (DS)
- **2025 DS 상생협력 Day, 25 Apr 2025:** 9 winners, all named on Samsung's semiconductor newsroom (AW-037). Korea Instrument (코리아 인스트루먼트), a maker of memory MEMS probe cards for wafer test (AW-039), received an 우수상 (Excellence award) (AW-038). Samsung does not state a reason for that award. The other 8 winners are materials, wafer, deposition, pellicle/chiller and cleanroom or chemical-supply companies (my characterisation).
- **2026 DS 상생협력 DAY, 3 Apr 2026:** 17 winners, of which only 4 are named: KCTech, Komico, Linde Korea and Wonik IPS, none in inspection, metrology or test (AW-040). The other 13 are NOT DISCLOSED.
- No Samsung Electronics award called "Best Partner" was found. The DS and DX divisions have held separate 상생협력 Days since 2025 (AW-040 source).

### Micron
- **Micron Supplier Awards 2025** were celebrated in the week before 31 Oct 2025, with 14 recipients (AW-041). **The 2026 awards** were given at Supplier Day in Boise (blog dated 22 Oct 2026; AW-044). Micron's own page lists every winner and category for both years. Neither year has an award category named for inspection or metrology; by my classification ([I], Medium; the page gives no product lines) no winner is primarily an inspection, metrology or test-equipment vendor. Hanmi Semiconductor (a TC-bonder maker; my characterisation) won "Outstanding Performance in Assembly & Test Capital Equipment" in both years (AW-042, AW-043).

### ASE (incl. SPIL)
- **2024 Best Supplier Awards, ceremony 11 Apr 2025 (in period):** 17 winners (AW-045), including Teradyne (Asia) (AW-046) and Test Research Inc. (TRI), a maker of AOI, AXI and in-circuit test systems (AW-047, AW-048).
- **2025 Best Supplier Awards, ceremony 24 Apr 2026:** 19 Best Supplier and 3 Supplier Sustainability awards (AW-049). cnyes counts 22 (AW-053), while DigiTimes' headline says 18 (AW-054, unresolved). Test winners: Advantest Taiwan (AW-050) and Hon Precision, a test-handler and active-thermal-control maker (AW-051, AW-052). No separate SPIL award event was found (NOT RETRIEVED). ASE, SPIL and USI took part in ASEH's ceremony per TechNews; cnyes says ASEH held it jointly with them (AW-049, AW-055). ASE's own release was not read (aseglobal.com refuses scripts).

### Amkor
- Amkor's own blog shows an Amkor Supplier Award to Henkel (SiP business unit), posted 17 Apr 2025 (AW-056).
- Senju states it received Amkor's **Supplier Excellence Award 2025** on 9 Dec 2025 (vendor release, not Amkor's own statement; AW-057) and that it was chosen from more than 3,000 suppliers ([C], AW-060). ASMPT also announced a win. No inspection, metrology or test winner was found, but Amkor's full list was not read.

### Cross-event pattern ([I], see AW-058)
- KLA appears on every full TSMC and Intel list read: TSMC 2025 and 2026, Intel 2025, plus Intel 2026 as a lead. Advantest appears on TSMC 2025, TSMC 2026 and ASE 2025. Lasertec appears on Intel 2025, Intel 2026 and TSMC 2026; its Intel 2025 category is EUV mask development, not packaging.
- No award read names a product used for HBM stacks or hybrid-bond inspection, and no category names a process step. The only HBM-specific link is Onto's SK hynix 2026 award, which could not be retrieved (lead).
- None of these appears on any list read: Hitachi High-Tech, Zeiss, Bruker, Nordson, Thermo Fisher, Park Systems, Auros, Semes, ISC, Leeno, MPI, Chroma, Tokyo Seimitsu/Accretech, Nikon. This is absence from the lists read, not evidence that they won nothing, because several lists are partial.

## 2. Gaps

- NOT RETRIEVED (tried: https://pr.tsmc.com/english/news/3274 with fetch.py, HTTP 403; same-host PDF https://pr.tsmc.com/system/files/newspdf/attachment/ce3c12707f578ed01449842b2d7d4b3d1b6c1cbf/2025%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29_final_wmn.pdf not tried) - TSMC's own 2025 Excellent Performance Award list with English category names. Please save by hand.
- NOT RETRIEVED (tried: https://pr.tsmc.com/english/news/3355 with fetch.py, HTTP 403; same-host PDF https://pr.tsmc.com/system/files/newspdf/attachment/1e7873e182523d3351afd810dc413e0bce01ca5f/2026%20Supply%20Chain%20Management%20Forum%20Press%20Release%20%28E%29-final_wmn.pdf not tried) - TSMC's own 2026 list. Please save by hand.
- NOT RETRIEVED (tried: web search for a TSMC OIP 2025/2026 Partner of the Year page; tsmc.com refuses scripts) - TSMC's own OIP award lists; the 2026 3DFabric Testing winner is unknown.
- NOT RETRIEVED (tried: https://newsroom.intel.com/intel-foundry/intel-announces-2025-epic-supplier-award-recipients with fetch.py, HTTP 403; https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-announces-2025-epic-supplier-award-recipients.html not tried, host refuses) - Intel's 2025 list with English categories. Please save by hand.
- NOT RETRIEVED (tried: https://newsroom.intel.com/corporate/intel-announces-2026-epic-supplier-award-recipients with fetch.py, HTTP 403; https://www.intel.com/content/www/us/en/newsroom/news/corporate/intel-announces-2026-epic-supplier-award-recipients.html not tried, host refuses) - Intel's 2026 list (41 recipients) and categories. Please save by hand.
- NOT DISCLOSED (read: SK hynix Newsroom KR, '2025 파트너스데이' 2025-09-30, full article) - names of the 14 winners of 2025.
- NOT RETRIEVED (tried: Korean and English web searches for 2025 Partners Day winners) - 13 of 14 SK hynix 2025 winners (ULVAC only identified).
- NOT DISCLOSED (read: SK hynix Newsroom KR, '2026 파트너스데이' 2026-09-29, full article and three photo-caption pages) - names of the 11 winners of 2026.
- NOT RETRIEVED (tried: https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production/default.aspx not fetched, host refuses; https://www.businesswire.com/news/home/20261012570961/en/ with fetch.py, curl stream error) - Onto's release on its SK hynix 2026 Best Partner Award. Please save by hand.
- NOT DISCLOSED (read: Samsung Newsroom KR, 'DS부문 2026년 상생협력 DAY' 2026-04-03, and the identical Samsung Semiconductor newsroom copy) - 13 of 17 Samsung DS 2026 winners.
- NOT DISCLOSED (read: Samsung Semiconductor Newsroom KR, '2025년 DS 상생협력 Day 현장' 2025-04-30) - the reason for Korea Instrument's award.
- NOT RETRIEVED (tried: https://www.aseglobal.com/press-room/supplier-day-2025 with fetch.py, HTTP 403; https://www.businesswire.com/news/home/20250411042346/en not tried after Business Wire stream errors) - ASE's own release for the 2024 awards (Apr 2025). Please save by hand.
- NOT RETRIEVED (tried: https://www.aseglobal.com/press-room/supplier-day-2026 with fetch.py, HTTP 403; https://www.businesswire.com/news/home/20260424628552/en/ with fetch.py, curl stream error) - ASE's own release for the 2025 awards (Apr 2026). Please save by hand.
- NOT RETRIEVED (tried: Chinese and English web searches for an SPIL-only supplier award) - a separate SPIL event; none found.
- NOT RETRIEVED (tried: amkor.com blog index and web searches; ir.amkor.com refuses scripts) - Amkor's full Supplier Excellence Award 2025 winner list (9 Dec 2025).
- NOT RETRIEVED (tried: web searches 'Amkor Supplier Excellence Award 2026', 'Amkor Supplier Day 2026') - an Amkor 2026 supplier-award event. I found none and do not assume whether it has been held.
- NOT DISCLOSED (read: Micron blog 2025-10-31) - the exact date of the 2025 Micron Supplier Awards ceremony ('last week').
- NOT DISCLOSED (read: Micron blog 2026-10-22 and Micron 'Supplier day & awards' page) - the exact date of the 2026 Supplier Day.
- NOT DISCLOSED (read: FormFactor blog 2026-03-25; Lasertec release 2026-03-25; AEM announcement 2026-03-19; Camtek release 2025-04-08; Lasertec release 2025-04-09) - Intel award categories in the vendors' own texts.
- NOT RETRIEVED (tried: https://ec.ltn.com.tw/article/paper/1778949 with fetch.py, HTTP 403) - Liberty Times article on the TSMC 2026 awards (says V5 won 'again').
- NOT RETRIEVED (tried: https://www.funder.co.il/article/198109 with fetch.py, HTTP 403) - Hebrew article on Israeli Intel 2026 winners.
- NOT RETRIEVED (tried: none; appliedmaterials.com refuses scripts) - Applied Materials blogs on its TSMC 2025 award (https://www.appliedmaterials.com/us/en/newsroom/blogs/tsmc-award.html) and Intel EPIC 2025/2026 awards (https://www.appliedmaterials.com/us/en/newsroom/blogs/applied-materials-earns-intel-s-2025-epic-supplier-award.html, https://www.appliedmaterials.com/us/en/newsroom/blogs/applied-receives-intel-epic-supplier-award.html). These are for an 'other'-class winner and are optional.
- Paywalled: DigiTimes articles AW-010 and AW-054 were saved with the lede only. The DigiTimes count of 18 ASE suppliers cannot be reconciled.

Manifest housekeeping: I replaced several first downloads saved with `--date auto` by copies named with the printed publication date, and removed duplicates and empty pages (SK hynix p=54107/2026-partners-day first copies, managertoday, uanalyze, Samsung pages, Micron blogs, bnext, Amkor, Senju, AEM, FormFactor, techtime tag page, KLA ?p= redirects, semiconductorpackagingnews teaser, komachine, ASMPT, cnyes/uanalyze duplicate). Their rows remain in `_manifest.csv`, and the manifest now shows them as NOT RETRIEVED / missing. The dated copies are the files cited in AW.csv.

## 3. Premise problems in the prompt

1. "TSMC Excellent Performance Awards ... December 2025": the 2025 SCM Forum was held on **25 Nov 2025** (AW-001, AW-006). Advantest's release came out on 24 Dec 2025. The 2026 forum has already been held, on **17 Nov 2026** (AW-011).
2. Samsung "Best Partner" award: no Samsung Electronics award by that name was found. The semiconductor award event is the **DS 상생협력 Day** (Apr 2025, Apr 2026), run separately from the DX one since 2025 (AW-040). "Best Partner Award" is SK hynix's name for its Partners Day awards (AW-033).
3. No separate SPIL supplier award was found (NOT RETRIEVED). Its suppliers are honoured at the ASE Technology Holding ceremony, in which ASE, SPIL and USI take part (TechNews; cnyes says held jointly) (AW-055). SPIL itself is a 2026 TSMC award winner.
4. Micron: the awards are "Micron Supplier Awards" in 14 "Outstanding Performance in ..." categories. Its "Assembly & Test Capital Equipment" category went to Hanmi (a TC-bonder maker) in both years, not to a tester or inspection vendor (my classification, [I]; AW-042, AW-043).
5. Watch-list names Tokyo Electron, DISCO and Canon did win (TSMC 2026, Intel 2025, ASE 2024 and Micron for TEL; TSMC and Intel for DISCO; TSMC 2025 and ASE 2024 for Canon). The categories are production, technology-development, safety or business ones, not probers or inspection, so they are classed other.
6. The ASE 2025 Best Supplier count varies: 19 named Best Supplier winners plus 3 Sustainability (technews), 22 (cnyes), 18 (DigiTimes headline). I use the names list.

## 4. Unverified leads (not turned into [F]/[S] rows)

- Onto Innovation - "Onto Innovation Receives Best Partner Award from SK hynix for Hidden Defect Prevention in High Bandwidth Memory Production" (Business Wire, about 12 Oct 2026): https://investors.ontoinnovation.com/news/news-details/2026/Onto-Innovation-Receives-Best-Partner-Award-from-SK-hynix-for-Hidden-Defect-Prevention-in-High-Bandwidth-Memory-Production/default.aspx and https://www.businesswire.com/news/home/20261012570961/en/ . Snippets say: award for technology achievement at the 25th Anniversary Partners Day (28 Sep 2026), presented by CEO Kwak Noh-Jung, for "a defect prevention system with breakthrough measurement technology for HBM", with the Dragonfly G5 inspection system. Why it matters: it is the only award found that ties an inspection tool to HBM at one of the seven chipmakers. Save by hand.
- Intel 2026 categories from search snippets of Intel's page (not read): KLA - "Excellence in Technology Development"; Camtek - "Excellence in Business Enablement"; FormFactor - "Excellence in Sort Test Development"; Nova - "Excellence in Integrated CMP Metrology Solutions"; AEM, AGC, Applied Materials and ASM are also on the list. Why it matters: these are the categories for four process-control or test vendors. Intel 2025 snippets also give English categories (e.g. Technoprobe - "Excellence in Sort/Test Development"; Camtek - "Excellence in Affordability and Technology Development").
- TSMC 2025 English release snippets (pr.tsmc.com/english/news/3274) give English category names, e.g. "Excellent Production Support", "Excellent Technology Development and Production Support" and "Excellent Contribution in Green Manufacturing". My English renderings of the Chinese categories in AW_table follow these; the 2026 English names are my translations.
- CMTX (via search) says the Micron 2025 awards took place on 13 Nov 2025 at the Westin, San Francisco. This conflicts with Micron's blog of 31 Oct 2025 ("last week"). Unresolved.
- Samsung "Material Day 2025" (Nov 2025): Fujifilm says it received Samsung's "Most Valuable Partner Award", one of 14 companies honoured (https://www.fujifilm.com/kr/en/news/hq/13138). It is a materials-supplier event, not checked for inspection vendors.
- Samsung Foundry SAFE Forum partner awards (EDA/IP/OSAT): not pursued, because no equipment vendors are expected.
- ASMPT: "ASMPT Honoured with Amkor Supplier Excellence Award 2025" (https://smt.asmpt.com/en/news-center/news/asmpt-honoured-with-amkor-supplier-excellence-award-2025/). A second Amkor 2025 winner (SMT equipment, other class); the page was fetched, then removed as not needed.
- Synopsys also reports a 2025 TSMC OIP award in "3DFabric Testing" (https://www.synopsys.com/blogs/chip-design/tsmc-awards-semiconductor-design-innovation.html). This is an EDA vendor; it shows Teradyne was not the only 3DFabric Testing awardee.
- Qnity Electronics - "Qnity named ASE 2025 Best Supplier in Advanced Packaging Materials" (Business Wire, 28 May 2026). Materials; it matches the ASE list.
- Liberty Times (ec.ltn.com.tw/article/paper/1778949) reportedly calls V5 Technologies a repeat TSMC winner (再度得獎), while managertoday marks it new versus 2025. V5 may have won in 2024; not checked.
- TechInsights "Global Semiconductor Supplier Awards" (Advantest, FormFactor) are customer-survey rankings, not chipmaker supplier awards, so they are excluded.
- SK hynix 기술혁신기업 (Technology Innovation Company) cohort selections (e.g. 8th cohort, Aug 2025) are a supplier-development programme, not an award, so they are excluded. The cohort lists may include Korean inspection vendors; not checked.

## Corrections after verification (2026-11-21)

- AW-009 re-tagged [F] -> [C] (Onto's paraphrase of TSMC's rationale; no TSMC wording).
- AW-018 claim: 'new' reworded to 'not on the 2025 list' (the article's 新面孔 definition).
- AW-033 split: award receipt stays [F]; ENTRON POR adoption claim moved to new row AW-059 [C].
- AW-042, AW-043 claims: only 'no category named for inspection or metrology' stays [F]; 'no inspection/metrology/test vendor' moved to an [I] note.
- AW-049, AW-055: 'co-hosted'/'held jointly' softened to TechNews' 共襄盛舉 (took part); cnyes' 共同舉辦 cited separately.
- AW-057: claim cut to Senju's account of the award and date (vendor release, not Amkor's); '3,000 suppliers' moved to new row AW-060 [C].
