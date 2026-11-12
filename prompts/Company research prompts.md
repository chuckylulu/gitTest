# Company research prompts for the eight fields

Eight self-contained prompts, one per field. Each asks for the same things in the same order, so the results can be compared:

- a worldwide map of the field;
- a single global ranking of companies by quality;
- a check on whether each company has a coherent path forward;
- a separate assessment of the entry point for an investment.

Paste one prompt at a time into a research assistant that can search the web and read company filings.

Notes on how they were built:

- **Global scope.** Every prompt states that the examination is global and asks for companies in all regions, listed or private, with one ranking across regions.
- **Quality and entry point are kept apart.** The ranking uses quality only. Valuation and timing appear in their own section and cannot change the order.
- **Path forward.** Each prompt names the transitions that company strategies in that field have to get through, taken from the earlier analysis, and asks for a verdict of coherent, partly coherent or not coherent.
- **Background.** The background in each prompt is as of mid-November 2026 and comes from the analysis in this conversation. Each prompt tells the researcher to test it and to say where it is wrong.
- **Starting lists.** The company names mix those from the gathered material with obvious candidates added from general knowledge. They are seeds to verify, not selections, and they lean toward companies better known in English-language sources.

## 1. Measuring what cannot be seen

```text
I am exploring chip measurement, inspection and test: the tools and software that measure, inspect and electrically test chips during manufacturing, especially stacked and bonded chips whose critical features are buried and have to be inferred instead of imaged. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

In chip manufacturing, measurement is the judge: it decides whether a wafer moves on. As chips go three-dimensional (nanosheet transistors, rear-side power wiring, bonded wafers, memory stacks of 16 layers and more), the features that matter are buried. They cannot be imaged from above and have to be inferred by matching a simulated signal to a measured one. The analysis concluded that AI changes the software and economics of measurement before its physics, that demand for physical measurement rises before any later fall, and that an AI-based measurement is only as trustworthy as the reference data behind it.

Evidence gathered (dated; several items are company claims or secondary reports)

- KLA reported fiscal-2026 revenue up 12% to $13.58 billion and cited rising process-control intensity. Its process-control revenue from advanced packaging was projected to grow from about $635 million in 2025 to about $1 billion in 2026 (annual report and an earnings summary).
- Detecting buried defects after wafer bonding was described in November 2026 as one of the hardest open problems as bond pitches shrink below today's production range of 4 to 9 microns (Semiconductor Engineering). No roadmap exists for electrically probing dense bond arrays below about 25 microns (EE Times).
- Direct copper-to-copper bonding for memory stacks slipped to the 16-layer HBM4E generation at the earliest. Samsung reported that it cuts thermal resistance by only 12-13%, so stacks of 20 to 24 layers need new approaches (TrendForce; SemiAnalysis on the 2026 ECTC conference).
- Papers at SPIE Advanced Lithography 2026 fuse X-ray scattering and optical data with physics-informed machine learning, and the same volume names scarce training data as the brake. IBM Research maps optical spectra straight to reference measurements without an optical model.
- A table-top EUV microscope that forms its image by computation resolved 43.5 nm half-pitch lines on a real chip in 2026 (Light: Advanced Manufacturing).
- Reference data comes from slow, destructive electron-microscope cross-sections and sits mostly with the chipmakers.

Prior views to test (the percentages are judgments)

- Measurement steps per leading-edge wafer keep rising through 2028 (75%).
- AI agents make setting up a measurement recipe at least five times faster at leading users by 2028 (60%), and combining several signal types becomes standard for nanosheet devices (70%).
- Buried bond-interface defects are still a leading yield limiter in 2030 (60%).
- Computed methods (X-ray scattering, scatterometry, lensless imaging) take share from direct imaging between 2029 and 2033 (45%).
- The number of tools needed per wafer may fall after 2030 as inference replaces some measurement (35%).
- Learned noise removal is safe for measuring what is expected and risky for detecting what is not.

The open question that matters most: who ends up owning the reference data, and with it the value: the tool makers or the chipmakers?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: optical and electron-beam inspection; scatterometry and other optical dimension measurement; X-ray measurement; overlay; inspection of bonded wafers and advanced packaging (acoustic, infrared, X-ray); electrical test and probing of stacked chips; reference measurement by electron microscope and its automation; measurement and yield software. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): KLA, Applied Materials, ASML (measurement and electron-beam units), Hitachi High-Tech, Lasertec, Advantest, Onto Innovation, Nova, Camtek, Bruker, Thermo Fisher Scientific, Nearfield Instruments, PDF Solutions, Teradyne, FormFactor, and the Chinese domestic suppliers that have grown under export controls.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest position is owning the measurement that chipmakers rely on to release wafers, together with access to the reference data behind it. The weakest is selling recipe-engineering hours.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from imaging to measurement by inference, with a stated uncertainty; (2) from hand-built recipes to recipes built by AI agents, which removes paid application-engineering work; (3) from front-end wafers to bonded stacks and packaging, where buried interfaces and electrical test are unsolved; (4) from selling hardware to selling software and data, when the reference data sits with customers; (5) AI that must run on the chipmaker's premises because the data cannot leave; (6) a possible fall in tools per wafer after 2030. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. For equipment makers, place each in the chip-equipment spending cycle and say how exposed it is to a pause in AI spending and to export controls. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 2. Simulation that can be trusted

```text
I am exploring physical simulation software: the software that predicts how designs behave before they are built, from fluid flow, structures and electromagnetics to chip manufacturing and materials, and that industry and regulators rely on to accept a design. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

Simulation is the judge that screens designs before they reach a physical test. The analysis concluded that AI changes it in a fixed order. Speed comes first, mostly from AI rewriting existing solver codes for graphics processors with results verified equal to the original. Scale comes second, as AI agents set up and run thousands of studies. Accuracy comes last. Learned models are reliable as proposers when a conventional solver finishes and certifies the answer; they fail on long chaotic runs and outside their training data. Because agents can drive open-source tools, ease of use stops protecting commercial vendors, and what remains valuable is a solver whose results are accepted for sign-off.

Evidence gathered (dated; several items are company claims or secondary reports)

- An AI-assisted port of a 250,000-line Fortran weather code validated 162 routines element by element and ran 5.1 times faster as a whole application (arXiv 2608.13122, August 2026).
- A learned model used as the starting guess for a conventional solver cut the remaining equation error by seven orders of magnitude on cases outside its training data, and ran 15.5 times faster than conventional simulation in an airfoil optimisation (arXiv 2608.04400).
- Machine-learned models of forces between atoms make errors about ten times larger on unseen molecules (arXiv 2605.08988). Of papers claiming to beat standard solvers on fluid problems, 79% compared against a weak baseline (McGreivy and Hakim, Nature Machine Intelligence, 2024).
- The race-car maker Dallara set error thresholds in advance; a learned model met the one for exploring concepts, not the one for replacing high-fidelity runs (arXiv 2604.18491).
- AI agents already run the open-source flow solver OpenFOAM end to end (arXiv 2509.18178).
- Siemens and NVIDIA report lithography simulation 10 to 17 times faster on graphics processors (company claim, October 2026).
- In July 2026 a report that an open model had designed a chip using only open-source tools coincided with falls of about 9% in Cadence and Synopsys shares. Analysts called the threat overblown because sign-off engines are entrenched.
- New scientific supercomputers are AI machines. Japan's 2030 flagship is 'zettascale' only in 8-bit arithmetic.

Prior views to test (the percentages are judgments)

- At least half of the widely used open simulation codes that run only on ordinary processors have an AI-built graphics-processor version in use by 2028 (60%).
- Agents cut the time from question to result at least five-fold at early adopters by 2028 (65%).
- Methods in which a learned model proposes and the solver certifies become a default option in major commercial solvers by the early 2030s (55%).
- No major aviation, nuclear or medical regulator accepts a learned model as primary evidence before 2031 (80%).
- The large design-tool vendors keep growing through 2029 (70%), but seat-priced front-end tools and mid-market solvers lose pricing power after that (50%).

The open question that matters most: where does the boundary of trust sit today, industry by industry, and who is placed to certify it?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: general engineering simulation (flow, structures, electromagnetics, heat); simulation inside chip design and manufacturing (lithography, process, thermal and packaging); materials and atomic-scale simulation; weather and climate; AI-for-physics platforms and newer entrants; cloud and high-performance computing services built around simulation. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): Synopsys (including Ansys), Cadence, Siemens (including Altair), Dassault Systemes, Hexagon, Keysight, Autodesk, COMSOL, NVIDIA (physics-AI software), and newer entrants such as Neural Concept, PhysicsX, Luminary Cloud, Flexcompute and Rescale, plus the Japanese, Korean and Chinese vendors that sell mainly in their home markets.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest position is a solver whose results are accepted for sign-off or certification. The weakest is ease of use, which agents remove.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from seat licences to pricing by use or by result, as agents replace the engineers who held the seats; (2) from ordinary processors to graphics processors and the low-precision hardware built for AI; (3) from ease of use as a protection to tools that agents drive through programming interfaces; (4) open-source codes becoming faster and easier through AI; (5) learned models placed inside solvers that still certify the answer; (6) acceptance by regulators and by customers' own sign-off rules. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. For software vendors, say how much of the price rests on seat-based revenue, which the analysis expects to come under pressure after 2029. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 3. Verification and specification

```text
I am exploring verification and specification: the tools and companies that check chips and software are correct before release, and that capture what 'correct' means: sign-off and formal verification for chips, machine-checked proof for software, and the specifications both are checked against. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

AI now writes code and chip designs faster than people can review them, and machine-checked proof has become cheap. The analysis concluded that the scarce parts are the specification (what should be proved) and the trusted sign-off, that verification tools own the verdict while verification labour loses its price, and that seat-priced tools face pressure once agents can drive open-source alternatives.

Evidence gathered (dated; several items are company claims or secondary reports)

- Over 90% of the changes merged into Anthropic's core codebase are written by its model (company statement, November 2026).
- Google DeepMind's AlphaProof Code produced more than six million lines of machine-checked proof in four weeks for Signal's protocol library, resting on about 26,000 lines of specification that human experts reviewed.
- Harmonic extended its prover to C and to the chip-design language Verilog in October 2026. Anthropic predicts formal verification will become as routine as automated random testing.
- Only 5% of chip projects worked on their first manufacturing run in the 2026 Siemens/Wilson Research study, down from 14% in 2024. Custom AI chips grew about 45% in units in 2026 (TrendForce).
- At the 2026 Design Automation Conference, Synopsys claimed up to 50 times faster time to a validated design (company claim). Early results evaluated with AMD showed 25-40% shorter debugging.
- An Arm study found frontier models missed up to 300 of 806 planted bugs. Checks generated by language models were unstable when a design was rewritten without changing its meaning (arXiv 2609.05658).
- In July 2026 a report that an open model had designed a chip using only open-source tools coincided with falls of about 9% in Cadence and Synopsys shares. Analysts called the threat overblown because sign-off engines are entrenched.

Prior views to test (the percentages are judgments)

- Machine-proved regression checks are standard for AI-edited chip designs by 2028, and the 2030 edition of the study shows first-run success above 5% (60%).
- Rates for chip design and verification contractors fall at least 30% by 2030 (55%). Final sign-off stays with people.
- The three large design-tool vendors keep growing through 2029 (70%). Seat-priced front-end tools lose pricing power after that (50%).
- Value moves from writing proofs to writing specifications.

The open question that matters most: who writes and owns the specifications, and can AI write them well enough to be trusted?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: chip sign-off and formal verification tools; emulation and prototyping hardware; verification components sold as intellectual property; AI-native chip-verification entrants; companies selling machine-checked proof for software; specification and requirements tools; verification services, which the analysis expects to lose pricing power. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): Synopsys, Cadence, Siemens EDA, Harmonic, Axiom, the newer AI-verification entrants covered in the 2026 trade press, the Chinese design-tool vendors growing under export controls (for example Empyrean and Primarius), and the verification work of Google DeepMind, Microsoft and Anthropic as possible suppliers or competitors.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest position is the sign-off tool or the specification that others must pass. The weakest is verification labour.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from verification labour to verification tools; (2) from seat licences to pricing by use; (3) from simulation-based checking toward formal proof; (4) proprietary engines against open-source tools driven by capable models; (5) chip manufacturers' certification of sign-off tools as a barrier to entry; (6) whether a paying market forms for verified software, and who the buyer is; (7) model makers offering verification themselves. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. Say how much of the price rests on seat licences and on services, which the analysis expects to come under pressure. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 4. Fast power for computing

```text
I am exploring fast power for computing: the equipment and sites that get electricity to AI data centres quickly: on-site generation, transformers and switchgear, storage, high-voltage direct-current distribution inside the building, and sites that already have power. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

Power is the tightest constraint on AI computing, and the analysis expects it to stay the main limit through 2030. A data centre takes two to three years to build and its grid connection four to eight, so buyers are turning to on-site generation and paying for speed. The owners of this constraint hold their position in the base case, but orders can be cancelled in a spending pause and local opposition is growing. Some products are bridges (on-site gas) and some last beyond 2030 (grid equipment, powered sites). Most of the evidence gathered is from the United States, so test how far it holds elsewhere.

Evidence gathered (dated; several items are company claims or secondary reports)

- The International Energy Agency's 2026 update has data-centre electricity use rising from 485 TWh in 2025 to 950 TWh in 2030, with AI-focused centres up 50% in 2025 and 15 to 27 GW of on-site gas by 2030.
- Grid waits are four to seven years in the main US markets. GE Vernova's gas-turbine backlog and reservations were reported at 83 GW in early 2026, heading for 100 GW. Siemens Energy was reported sold out into the early 2030s. Transformer lead times were reported at 128 to 144 weeks (secondary sources).
- About 48 GW of on-site generation was proposed for US data centres in early 2026, about three-quarters of it gas, against roughly 2 GW operating in mid-2026 and about 3 GW expected by year-end (Cleanview).
- Between 30% and 50% of US projects planned for 2026 faced delay or cancellation, mainly for lack of power (Sightline Climate, via press). About 40% of planned capacity sits in states considering pauses (November 2026).
- An 800-volt direct-current architecture is being standardised through the Open Compute Project. NVIDIA's power rack was due in the second half of 2026 and row-level units of up to 2 MW in 2027.
- Bloom Energy and Brookfield have a $5 billion fuel-cell partnership. Constellation expects to restart the Crane reactor in the second half of 2027. Microsoft's president called the electrician shortage the '#1 problem' for US expansion.
- A gigawatt of AI data-centre capacity was estimated at about $49 billion for 2026-generation hardware, up from about $35 billion (Morgan Stanley, via press).

Prior views to test (the percentages are judgments)

- Power, not chips, remains the main limit on AI computing through 2030 (65%).
- New nuclear plants supply under 5 GW to data centres before 2032 (75%).
- One-megawatt racks are in production use by the end of 2030 (50%).
- Owners of powered sites hold their value better than owners of chips.
- In a spending pause (25%) orders are cancelled, so firm order books matter more than announced demand.

The open question that matters most: how much on-site and grid power is actually being delivered, against what is announced, and whose order books are firm?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: gas turbines and reciprocating engines; fuel cells; transformers, switchgear and other grid equipment; batteries and power conversion for flexible grid connection; power distribution inside the data centre, including 800-volt direct current and solid-state transformers; electrical contractors and prefabricated power modules; developers and utilities with powered sites; nuclear restarts, small reactors and geothermal as longer-dated options. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): GE Vernova, Siemens Energy, Mitsubishi Heavy Industries, Caterpillar, Cummins, Wartsila, Bloom Energy, Hitachi (energy unit), ABB, Schneider Electric, Eaton, Vertiv, Delta Electronics, HD Hyundai Electric, Hyosung Heavy Industries, LS Electric, Constellation, Brookfield, Kairos Power, Oklo, Fervo Energy, and the Chinese grid-equipment and battery makers.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest position is equipment or sites that stay physically scarce for years. Check whether each product is a bridge (for example on-site gas) or lasts beyond 2030.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from grid-only supply to on-site generation with storage and flexible load; (2) from on-site gas as a bridge to whatever follows after 2030; (3) from alternating-current distribution to 800-volt direct current and solid-state transformers; (4) expanding factory capacity without adding it into a pause; (5) scarce skilled labour pushing work into prefabrication; (6) local opposition and permitting, which differ by country. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. Say how much of the order book is firm and cannot be cancelled, and how much new capacity each company is adding into a possible pause. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 5. System-level hardware: stacking, heat removal and optical links

```text
I am exploring system-level hardware for AI: the hardware around the processor that now sets performance: advanced packaging and chip stacking, stacked memory, cooling, and the copper and optical links between chips and racks. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

The unit of progress in computing has moved from the transistor to the system. The analysis expects packaging, optical links, rack power and cooling to be the binding constraints in 2028-2030. Each of these areas has a bridging technology that ships today and a successor due later. The bridge benefits until the successor ships in volume, and several successor dates have already slipped.

Evidence gathered (dated; several items are company claims or secondary reports)

- TSMC's advanced-packaging capacity has grown by more than 80% a year since 2022, and lead times were estimated at 52 to 78 weeks. A larger package able to hold 12 or more memory stacks is due in 2027. Panel-sized packaging is in pilot in 2026 with volume expected in 2028-29. Glass-core substrates are targeted for 2027-28 by several makers.
- Stacked high-bandwidth memory was sold out for 2026, largely committed for 2027 and expected tight into 2028. Micron's roadmap has a new generation every year to 2030. Direct copper-to-copper bonding for these stacks slipped to the 16-layer HBM4E generation at the earliest.
- TSMC's A16 process slipped from late 2026 to 2027. NVIDIA's 600 kW rack was reported delayed to 2028, which NVIDIA disputes.
- Processors draw up to 2.3 kW each and are heading toward 4 kW. Cold plates handle about 100 to 150 kW a rack. Two-phase cooling is held up by restrictions on fluorinated coolants. Cooling channels inside the chip are unproven in production.
- Optics built into network switches began shipping in 2026, and NVIDIA and its packaging partner plan a fifteen-fold rise in optical-engine capacity by mid-2027. Optical links between processors are planned for 2028 and may slip to 2028-29. Copper is being stretched to 2027-28.

Prior views to test (the percentages are judgments)

- At least one of the three technologies planned for NVIDIA's 2028 generation (an A16-class process, panel packaging, optics between processors) misses volume that year (70%).
- The 600 kW rack ships in volume in 2028, not 2027 (65%). One-megawatt racks are in production use by the end of 2030 (50%).
- Memory stays supply-limited through 2028 (70%), and is the first area to turn in a spending pause.
- Bridging hardware (copper links, plug-in optical modules, solder-bump stacking equipment, cold plates) loses share between 2028 and 2030. Because successors slip, the bridges last longer than roadmaps say.

The open question that matters most: which successor technology ships in volume first, and do specialists or the integrated giants capture the value?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: advanced packaging at chip foundries and assembly houses; substrates, including glass; bonding equipment for solder bumps and for direct bonding; stacked memory; cooling (cold plates, coolant distribution, two-phase and immersion, thermal materials); optical components (lasers, optical engines, switch makers, connectors, photonic test); copper links (cables, connectors, signal-conditioning chips); power delivery inside the rack. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): TSMC, ASE Technology (including SPIL), Amkor, Intel, SK hynix, Samsung Electronics, Micron, Samsung Electro-Mechanics, Absolics, LG Innotek, Ibiden, Unimicron, BE Semiconductor, Hanmi Semiconductor, ASMPT, Tokyo Electron, NVIDIA, Broadcom, Marvell, Lumentum, Coherent, Innolight, Amphenol, Credo, Vertiv, Delta Electronics, Asia Vital Components, Accelsius, Rittal.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the key distinction is bridge against successor. Say on which side each product sits and when its successor is due.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) copper links to optical links between processors; (2) plug-in optical modules to optics built into the switch; (3) solder-bump stacking to direct bonding; (4) silicon interposers to panel and glass packaging; (5) cold plates to two-phase cooling; (6) today's rack power to 600 kW and one-megawatt racks on 800-volt direct current. For a company on the bridge side, ask whether it has a credible successor product. For a company on the successor side, ask whether it is funded through a slip of one to two years. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. Say whether the price assumes that the bridge lasts or that the successor arrives on schedule, since the analysis expects slips. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 6. Automated security

```text
I am exploring automated security: products that find and fix software flaws at machine speed and that shield devices which cannot be patched, as opposed to security work sold as human testing hours. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

AI has made working exploits cheap, and attackers do not need frontier models. The analysis concluded that this raises demand for security in a way that does not depend on the AI spending cycle, that value moves from human testers to automation, that owners of long-lived devices which cannot be patched carry rising liability, and that in the longer run machine-checked software could shrink the business of finding and patching flaws.

Evidence gathered (dated; several items are company claims or secondary reports)

- One OpenAI pipeline run on an unreleased security model produced 948 working Linux kernel privilege-escalation exploits, each with a candidate patch, for $1.2 million, or about $1,270 each (company report, October 2026).
- Check Point logged a criminal campaign of 400,791 agent messages across 292 objectives in two weeks of October 2026, run on cheap models for under $1,500. Reuters reported one hacker breaching more than 100 companies with commercial agents.
- XBOW built a three-bug Chrome sandbox escape that Google confirmed and paid its maximum bounty for.
- The curl project closed its bug bounty in January 2026 after a flood of machine-written reports. In May 2026 the Linux kernel's security list was described by its lead as almost unmanageable for the same reason.
- Anthropic's red team wrote that small open models may be months away from self-replicating on connected devices. Moonshot found that exploit skill follows general coding skill even after security data is removed from training.
- The most capable security models are gated: OpenAI, Google and Anthropic each release them only to approved organisations.
- Google DeepMind proved security properties of Signal's library by machine, and Anthropic expects formal verification to become routine.

Prior views to test (the percentages are judgments)

- A mass compromise of consumer or industrial devices is attributed to AI-built exploits by the end of 2027 (60%).
- Rates for human penetration testing fall first. Overall spending on finding and patching flaws shrinks only after 2030, if verified software removes whole classes of bugs (35%).
- Demand holds in a spending pause, because cheap models are enough for attackers.

The open question that matters most: do defenders or attackers gain more from the same models, and which vendors have access to the gated frontier security models?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: automated vulnerability discovery and repair; code and software-supply-chain security; exposure management; network shielding and segmentation for connected and industrial devices; detection and response platforms; penetration testing and bug-bounty platforms, which the analysis expects to lose pricing power; machine-checked verification sold for security. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): XBOW, Check Point, Palo Alto Networks, CrowdStrike, Fortinet, Zscaler, Snyk, Socket, HackerOne, Bugcrowd, Claroty, Armis, Nozomi Networks, Trend Micro, the Chinese vendors that serve their home market, and the security programmes of OpenAI, Google and Anthropic as suppliers or competitors (ownership of several of these has changed recently, so check current status).

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest position is automation that finds and fixes at machine speed, with access to the gated frontier models. The weakest is billable testing hours.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from billable testing hours to automation; (2) from human triage of reports to machine-speed finding and fixing; (3) from patching endpoints to shielding devices that cannot be patched; (4) dependence on access to gated frontier models, which may not be granted equally across countries, and the model makers' own security products; (5) liability and regulation for device makers, which differ by jurisdiction; (6) the longer-run shift to software verified when it is written. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. Demand here does not depend on the AI spending cycle, so concentrate on the growth the price assumes and on competition from the model makers themselves. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 7. Self-tuning instruments

```text
I am exploring self-tuning scientific and industrial instruments: measuring instruments whose set-up, alignment and calibration are run by AI agents instead of human experts: electron microscopes, X-ray and synchrotron equipment, spectrometers, particle accelerators, quantum processors and electronic test equipment. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

Setting up a complex instrument is expert work with a fast and unambiguous judge: the instrument's own reading on a known standard. The analysis identified this as a field that has received little attention and is likely to move, because an agent can tune against that reading directly. The same method should later keep fleets of chip-measurement tools in agreement. The obstacles are closed control interfaces and the cost of damaging hardware.

Evidence gathered (dated; several items are company claims or secondary reports)

- A Stanford and SLAC team reported an AI agent that plans, interprets feedback and issues control commands to align a sample at a synchrotron beamline (Nature Machine Intelligence, reported July 2026).
- IQM and NVIDIA reported an agent calibrating a 20-qubit chip. A language agent brought up a 112-qubit superconducting processor (arXiv 2606.22376). Google reported an AI system adjusting more than 1,000 control parameters while error correction runs (July 2026).
- Automated tuning of electron-microscope aberrations was reported in January 2026, and a 2026 conference abstract describes a planned agent framework controlling a Thermo Fisher microscope through its scripting interface.
- A preprint describes automated discovery of commissioning procedures for particle accelerators (arXiv 2608.07138; only its title and references were read).
- A table-top EUV microscope with built-in self-calibration resolved 43.5 nm half-pitch lines on a real chip in 2026.

Prior views to test (the percentages are judgments)

- At least two major instrument makers ship agent-run alignment and calibration as a standard feature by 2028 (65%).
- The method then spreads to keeping a chip fab's measurement tools matched.
- Closed control interfaces and the risk of damaging costly hardware are the main obstacles.

The open question that matters most: which makers open their control interfaces to agents, and does the value go to the instrument maker, to a software layer, or to the user?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: electron microscopy; X-ray and synchrotron instruments; mass spectrometry and magnetic resonance; chip-measurement tools; electronic test and measurement; control and calibration systems for quantum computers; laboratory-automation software; accelerator and beamline components. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): Thermo Fisher Scientific, JEOL, Hitachi High-Tech, Carl Zeiss, Bruker, Oxford Instruments, Shimadzu, Rigaku, Horiba, Agilent, Keysight, Rohde & Schwarz, Anritsu, IQM, Quantum Machines, Q-CTRL, and NVIDIA as a supplier of the models used.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest position is the instrument itself together with its installed base and the data it produces. Check whether its control interfaces are open enough for agents, and who would capture the value if they are.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from expert set-up to agent-run set-up; (2) from closed to open control interfaces; (3) from one-off hardware sales to software and subscription revenue; (4) instruments that use cheaper hardware and heavier computation; (5) instruments as data sources for customers' own AI, which raises the question of who owns the data. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. Many of these are diversified instrument groups, so say how much of the business this theme actually touches. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```

## 8. Analog and power-electronics design

```text
I am exploring analog and power-electronics design: analog, radio-frequency and power chips and boards, the tools used to design them, and the power parts that AI data centres now need. I want to know which companies in this field are of the highest quality and whether each has a coherent path forward. Separately, I want to know whether now is a sensible entry point for an investment in each.

Two things govern the whole task.

The examination is global. Cover companies in every region, including North America, Europe, Japan, South Korea, Taiwan, China, Israel and India, whether they are listed on any exchange or privately held. Do not default to companies listed in the United States. Where your coverage of a region is thin, for example because sources are not in English, say so.

Quality and entry point are separate judgments. The earlier analysis this builds on looked only at business position and gathered no valuation data, and a strong company can be a poor investment at the wrong price or the wrong point in its cycle. Rank on quality alone and report the entry point in its own section.

BACKGROUND YOU SHOULD USE AND TEST

This request builds on a longer analysis, completed in mid-November 2026, of how AI is changing technology. Its conclusions are judgments, built largely on analyst estimates and company claims. Treat the probabilities below as priors and check the facts against current sources.

- AI has made it cheap to produce candidates (code, designs, analyses). Progress and value now depend on the judge: whatever decides that a candidate is right, such as a simulation, a measurement, a verification tool or a regulator. A judge is strong when it is fast, faithful under optimisation pressure, informative when it says no, and final.
- Businesses that own a judge, or a physical constraint that AI cannot remove (power, lithography, leading-edge chip fabrication), keep their position. Businesses that sell labour by the hour, rent software per human seat, wrap someone else's model, or fill a temporary gap in what AI or its hardware can do, lose it when the gap closes.
- The binding constraint on AI computing moves: memory, power connection and financing in 2026-2028; packaging, optical links, rack power and cooling in 2028-2030; generation, transmission and transistor architecture after 2030. Hardware that bridges a gap benefits until its successor ships in volume, and those dates tend to slip.
- Three scenarios for AI spending to 2030: steady growth with computing supply roughly doubling each year (about 55%), a financing-led pause around 2028 (about 25%), and faster acceleration (about 20%).

What the analysis concluded about this field

Analog and power design is the last hand-crafted corner of chip design, and its judge is a circuit simulator plus prototypes that come back in days. AI agents have begun to design boards and circuit blocks, although no independently verified silicon result was found. At the same time AI data centres are creating new demand for power parts. The analysis concluded that design tools and new entrants may gain, and that established suppliers benefit now but may see their design-expertise advantage erode in the early 2030s. What agents cannot reproduce is process technology, reliability data and customer qualification.

Evidence gathered (dated; several items are company claims or secondary reports)

- Anthropic reported that its model designed three circuit boards that a third party manufactured and that worked without electrical modification (a single company-reported run, November 2026).
- ChipNexus announced an analog design agent that runs inside the standard Cadence tools (press release, 27 October 2026). Academic work includes RFChipAgent (arXiv 2610.10858), a long-horizon analog design benchmark (arXiv 2609.33356) and a board-routing benchmark (arXiv 2611.08175). No independently verified, silicon-proven block designed by an agent was found.
- The 800-volt direct-current architecture for AI racks has brought reference designs or parts from Texas Instruments, STMicroelectronics, Navitas and EPC, and silicon-carbide solid-state transformers promoted by Wolfspeed (company and trade sources, 2026).
- Processors draw up to 2.3 kW each, heading toward 4 kW. Row-level power units of up to 2 MW are due in 2027.

Prior views to test (the percentages are judgments)

- The first independently verified working chip block designed end to end by a language-model agent appears by the end of 2027 (60%).
- One-megawatt racks are in production use by the end of 2030 (50%).
- Margins on standard analog and power parts compress in the early 2030s as design expertise becomes reproducible (40%).

The open question that matters most: has any agent-designed analog block been independently verified in silicon, and who gains from it: tool makers, new entrants, or incumbents with process and reliability data?

WHAT I NEED

1. Map the field worldwide. Lay out its sub-segments and the companies that matter in each, in any country, listed or private. Sub-segments to cover: analog and mixed-signal chip suppliers; power semiconductors in silicon, silicon carbide and gallium nitride; power modules and power delivery close to the processor; radio-frequency chips; analog design tools and AI-native analog design entrants; circuit-board design automation. Aim for the 8 to 15 companies that matter most globally, and say whom you left out and why. A starting list to verify and extend, not a shortlist (it mixes names from the earlier research with obvious candidates, and it leans toward companies better known in English-language sources, so look beyond it): Texas Instruments, Analog Devices, Infineon, STMicroelectronics, onsemi, Renesas, Rohm, Mitsubishi Electric, Monolithic Power Systems, Vicor, Power Integrations, Navitas, EPC, Wolfspeed, Innoscience, the Chinese silicon-carbide and analog suppliers, Cadence, Synopsys, ChipNexus, Quilter.

2. Assess each company's quality, independent of its share price. Apply these five tests and give the evidence for each.
   a. Position. Does it own a judge or a constraint, or does it fill a gap that AI or the next hardware step will close? Here the strongest positions are process technology, reliability data and customer qualification, which agents cannot reproduce, and tools that own the design check. The weakest is design expertise alone.
   b. Lead. What outside evidence shows a real technical and commercial lead: market share, qualification at leading customers, published or independently confirmed results. The company's own description is not evidence.
   c. Revenue model. How much revenue depends on labour hours, human seats or one-off hardware, and how much recurs or scales with use.
   d. Financial strength. Margins, return on capital, cash generation, debt, and concentration by customer and by country.
   e. Resilience. How it fares in each of the three scenarios, where it sits in its own industry cycle, and how exposed it is to export controls or other cross-border restrictions.

3. Examine whether each company has a coherent path forward. In this field the transitions that test it are: (1) from hand design to agent-assisted design, and what that does to the value of scarce designers; (2) from breadth of catalogue as an advantage to easier copying of standard parts, including by lower-cost entrants; (3) from silicon to silicon carbide and gallium nitride; (4) from 48-volt to 800-volt distribution and power delivery beside the processor; (5) access to manufacturing process data and device models, which agents need and suppliers control. For each company, say which of these it must get through, what it has said and what it has actually done (products shipped, customers qualified, research and capital committed, acquisitions), whether the plan is funded and the timing plausible, and what would have to go right. Give a verdict of coherent, partly coherent or not coherent, with the reason. A company with no coherent path forward should not rank in the top group, whatever its current results.

4. Rank the companies by quality alone, using tests a to e and the path-forward verdict. Produce one global ranking, not one per region. Do not let valuation, recent share-price moves or company size change the order. Where two companies cannot be separated, say so instead of forcing an order.

5. Only then assess the entry point, in a separate section. For each company give: current valuation against its own history and its closest peers worldwide, the growth and margins the price already assumes, where the business is in its cycle, near-term events that could change the picture, and the conditions under which entry would look attractive. Place each in the analog and power semiconductor cycle, and separate the share of revenue tied to AI data-centre power from the rest. Label each one attractive, fair, stretched or cannot assess, as of the date you check. For private companies, and for listed companies that are hard for a foreign investor to reach, say whether and how exposure is possible. A high-quality company can be a poor entry and a weaker one a good entry, and I want to see the two judgments side by side, not blended into one score. This is analysis for my own exploration, not personal financial advice, so do not issue buy or sell instructions.

6. Say plainly where the evidence contradicts the background above. Do not defend it; I would rather know that a prior was wrong.

HOW TO WORK

Use only public, legally accessible sources. Prefer primary ones: annual and quarterly reports, stock-exchange filings in the company's home market, earnings-call transcripts, investor-day material, technical conference papers and standards bodies. Give the date of every figure and state the date of your research. Mark any company claim that no outside party has confirmed. If you cannot verify something, say so instead of filling the gap. Where a current source differs from the background, use the current figure and note the change.

WHAT TO RETURN

Open with a short verdict: the top three companies by quality, and the answer you reached on the open question. Then, in this order:
1. The field map, with the regions covered and any region where coverage was thin.
2. The quality ranking as a table: rank, company, home country and where it is listed, sub-segment, a one-line result for each of tests a to e, and the path-forward verdict.
3. A path-forward note for each company: the transition it faces, its plan, the evidence, and what must go right.
4. The entry-point table, kept separate from the ranking: valuation snapshot, cycle position, what the price assumes, label, and the conditions that would improve the entry.
5. A short list of companies where quality and entry point pull in opposite directions.
6. Contradictions with the background.
7. What you could not verify.
8. Sources, with dates.
```
