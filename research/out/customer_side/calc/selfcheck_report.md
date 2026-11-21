- Rows checked: 618 (every row of evidence.csv at the time). First pass: {'MATCH': 510, 'PARTIAL': 106, 'MISMATCH': 2}.
- Flagged rows re-checked by a second, skeptical agent: 108; problem confirmed: 99 ({'PARTIAL': 97, 'MISMATCH': 2}); not confirmed: 9 (left unchanged).
- Confirmed issue types: {'other': 34, 'claim_overstates_source': 44, 'wrong_tag': 24, 'vendor_material_presented_as_chipmaker': 2, 'value_wrong': 2, 'chipmaker_attribution_unsupported': 5, 'page_wrong': 4, 'date_or_period_wrong': 5, 'inference_inputs_missing': 5}.
- Confirmed problems by module: {'PAPM': 28, 'PAPL': 15, 'TALK': 16, 'XR': 8, 'SMP': 24, 'AW': 8}.
- Fixes applied by module (fix agents): PAPM 28 applied, 2 noted, new rows PAPM-230, PAPM-231, PAPM-232; PAPL 16 applied, 4 noted, new rows PAPL-189; TALK 16 applied, 3 noted, new rows none; XR 8 applied, 2 noted, new rows none; SMP 24 applied, 3 noted, new rows SMP-045, SMP-046, SMP-047; AW 10 applied, 2 noted, new rows AW-059, AW-060.
- CANNOT OPEN: 0.

### The 15 most important rows (review packet claims): result of the self-check

| Id | First pass | Second check | Wording found by the checker (excerpt) | Tag after fixes |
|---|---|---|---|---|
| PAPM-049 | MATCH | - | We propose a practical but very effective method for pre-screening of these interface failures in mass production with the idea of small changes in BE | [F] |
| PAPM-222 | PARTIAL | confirmed PARTIAL | III. CONCLUSIONS: "The optimized process was successfully applied in mass production, demonstrating improved productivity and stable quality, with no  | [C] |
| PAPM-201 | MATCH | - | The results of this study have been implemented into measurement equipment and developed into a commercialized solution currently in use. | [C] |
| PAPM-206 | MATCH | - | the y-axis indicates the total time (in seconds) required to measure 600 chips. Under the given experimental conditions, the total measurement time of | [F] |
| PAPM-216 | MATCH | - | Final validation using actual HBM device wafers in a production-grade MI setup confirmed these findings. | [F] |
| PAPM-136 | MATCH | - | Micro-bump joint integrity for entire 12-layer stacks after reliability confirmed with daisy chain resistance and Confocal Scanning Acoustic Microscop | [F] |
| SMP-031 | MATCH | - | The implementation of 100% overlay measurement is needed ... to achieve high overlay metrology throughput with 100% chiplet inspection ... roadmap tow | [F] |
| PAPL-046 | MATCH | - | A test vehicle featuring a dense grid of fiducials across the chiplet is fabricated to enable near-infrared (NIR) post-bond chiplet level overlay mapp | [F] |
| PAPM-016 | MATCH | - | CSAM results are clean of voids, and X-section shows satisfactory bonding results on both bonding interfaces. | [F] |
| TALK-020 | MATCH | - | Advanced techniques, including optical inspection, X-ray microscopy, atomic force microscopy, and acoustic microscopy are examined alongside AI-powere | [F] |
| TALK-024 | MATCH | - | Samsung Electronics has begun introducing new inspection equipment for hybrid bonding, with Onto Innovation’s systems reportedly undergoing validation | [S] |
| XR-003 | MATCH | - | even after overexposure to three times the limit provided by DRAM manufacturer, no infant mortality failures were observed. However, the reliability o | [F] |
| XR-015 | MATCH | - | The public keynote abstract explicitly lists “DRAM/HBM damage concern by X-ray” among the challenges for advanced-packaging inspection. | [S] |
| PAPM-225 | MATCH | - | The 191 inspection systems used in this study are Hitachi High-Tech IS4100 patterned-wafer defect inspection tools | [F] |
| TALK-014 | MISMATCH | confirmed MISMATCH | Quote is exact, from the paragraph beginning "The W2W method has been commercialized...": "For HBM, the D2W approach is being adopted and is progressi | [S] |
