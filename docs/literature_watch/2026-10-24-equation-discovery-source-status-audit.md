# Literature source-status audit — 2026-10-24: CoSR manuscript provenance

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy / future-industry research and publication  
**Related pending research:** PR #56 (progressive symbolic discovery), PR #71 (agentic scientific discovery), PR #55 (thermodynamic speed limits), PR #76 (EQN-OPT-001 evaluator)  
**Evidence class:** LITERATURE_ONLY / source-provenance audit  
**Project evidence promotion:** none

## Question audited

Can CoSR, “Data-driven progressive discovery of physical laws” (Mingkun Xia and Weiwei Zhang), be treated as a trusted baseline for the project's equation-discovery comparisons?

## Primary records checked

- The [Physical Review Research accepted-paper page](https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q) lists acceptance on 2026-10-06, DOI 10.1103/f2kp-pp4q.
- The [official arXiv HTML record](https://arxiv.org/abs/2603.13727), dated 2026-03-14, currently displays a CoSR abstract and full HTML methods/results body consistent with the title.
- A [third-party Pith review](https://pith.science/paper/2603.13727) reports that the supplied version-2 PDF/full text appears to be an unrelated CHI paper, “It Became My Buddy, But I'm Not Afraid to Disagree” (arXiv:2603.13717), so the empirical claims cannot be checked from that PDF.

## Correct status and limitation

The current official arXiv HTML page shows CoSR content and no withdrawal notice. The third-party review is a provenance warning, not an official withdrawal or retraction notice. During this cycle, the actual PDF bytes and final journal version were not independently retrieved; the PDF/body mismatch is therefore **reported but unresolved**, not confirmed.

This distinction matters: neither the accepted-journal abstract nor a third-party review alone establishes that the downloadable PDF, accepted version, code and data are mutually consistent. Do not label CoSR withdrawn/retracted, and do not treat its reported benchmark performance as independently verified until the artifact mismatch is resolved.

## Next falsifiable provenance gate

1. Retrieve the actual arXiv version-2 PDF and the final journal version of record.
2. Compare title, authors, body, equations, figures, tables, references, version history and DOI metadata.
3. Check the official journal/arXiv records for any correction, replacement, or editorial notice.
4. Compare the article's code and dataset version with the manuscript that describes them.
5. Record hashes of the retrieved PDF, HTML snapshot, code commit and dataset manifest.
6. If the mismatch is confirmed but cannot be resolved, keep CoSR excluded from scored baselines. Do not infer misconduct or withdrawal from a third-party review alone.

## Cross-lane integration

- **Lane A / EQN-OPT-001:** the finite-grid candidate screen is method-agnostic; CoSR must not be assigned a trusted score until provenance is resolved.
- **RG-034:** source provenance is separate from identifiability. Even a verified paper cannot replace the confounded-ODE/null-direction experiment.
- **RG-045:** numeric-grid disjointness checks in EQN-OPT-001 do not establish raw-data split membership or provenance.
- **INV-034/035:** keep the search open to progressive equation discovery while maintaining evidence, falsification, independent replication and source-integrity gates.
- **No claim promotion:** no CoSR result is a UQPU discovery, a new physical law, or evidence of a material, energy, quantum, financing, or Data-Center-to-Phone advantage.

The detailed CoSR comparison contract and LLM-PySR method watch remain in the pending [PR #56](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/56); thermodynamic speed-limit analysis remains in [PR #55](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/55); the broader agentic-discovery watch remains in [PR #71](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/71). This file records only the source-status correction so the literature methods are not unnecessarily duplicated.
