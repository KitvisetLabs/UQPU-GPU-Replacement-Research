# Batch 075 — SISSO materials-gene sensitivity and equation identifiability

**Date:** 2026-10-27  
**Starting main SHA:** 83e5ba81ea32d739ae5d191b48e78e8bb2e4fc42  
**Primary owner:** Lane H — literature synthesis/publication  
**Technical owner:** Lane D — device/material physics  
**Integration owner:** Lane F — evidence/benchmark/economics  
**Evidence class:** LITERATURE_ONLY; no code or physical experiment reproduced

## Research question

Can analytical sensitivity and equivalent-descriptor analysis improve UQPU's equation-discovery gates by separating robust model behavior from non-identifiable symbolic terms, without promoting a fitted expression to a causal law?

## Fresh literature delta

The APS version of record for Foppa and Scheffler, “How SISSO-derived materials genes shape materials properties: An analytical sensitivity analysis,” *Physical Review Materials* 10, 093601, was published 2026-09-08 (DOI 10.1103/gk23-cfh1). It derives a sensitivity-analysis method for SISSO descriptors and discusses equally accurate feature combinations that encode equivalent information, with a perovskite lattice-constant example. The article links a public code repository. This source was not present under a dedicated SISSO sensitivity watch in the current literature-watch directory.

The novelty for this project is methodological: equation evaluation should include sensitivity and identifiability under equivalent parameterizations, not just training fit or expression recovery. This is a research lead, not a new physical law and not UQPU reproduction.

## A–H review

- **A — Workloads/compiler/runtime:** no quantum workload or QAOA implementation changed; EQN-002/003/004 gain a concrete candidate evaluation protocol for sensitivity stability and equivalence classes.
- **B — Cloud/QPU integration:** no provider adapter or QPU job used; provider-neutral execution path unchanged.
- **C — Memory/state/data movement:** no memory-capacity result; descriptor count or symbolic compactness is not readable classical storage or subsystem equivalence.
- **D — Device/material physics:** opened RG-MAT-SISSO-SENSITIVITY-001 with a pinned-source and independent-reproduction gate.
- **E — Biomass/materials/bio-oil/fusion/cooling:** perovskite results do not transfer to Pangola carbon; BIO-001 and FUS-001 remain unchanged and commercially unproven.
- **F — Economics/evidence/integration:** added held-out, matched-budget, uncertainty, sensitivity-stability and stop-rule requirements; no cost or energy measurement.
- **G — Manufacturing/factory systems:** no fabrication, process-window, yield or cost-per-good-device result; D/G co-design remains required for any later component claim.
- **H — Strategy/publication:** published a dated primary-source watch and linked gap while preserving the Kanusanan Pongpanna Model and multilingual master-plan references.

## Foundation and invariants

- **FND-001–005:** no change in evidence level; no physical thermodynamic, information, speed-limit, primitive or QFT/particle result.
- **FND-006:** advances only the mathematics-first model-evaluation method; no physical equation discovered by UQPU.
- **EQN-001–006:** adds sensitivity/identifiability checks to the generator → constraints → evaluator → held-out test → counterexample → proof/simulation → discriminating experiment → independent replication → system consequence → economics ladder.
- **INV-029:** no physical-compression or phone-boundary result.
- **INV-030:** no elemental transmutation or Pangola material substitution; this is a candidate screening method only.
- **INV-031/032/033:** no accepted bio-oil, net fusion-electricity or financing/interest evidence.
- **INV-034/035:** deep-frontier exploration remains open; current physics is binding and candidate equations remain hypotheses.
- **INV-025/026/027:** 100,000,000-GPU and universal subsystem targets remain falsifiable moonshots.

The root directives 00, 00A and 01–06, all A–H lane workspaces, the integration hub, and Thai/English/Chinese/Japanese/Korean/German strategic-plan links remain preserved. No paid/live QPU job was submitted.

## Next highest-value gate

Pin the public code/data and reproduce the perovskite example; cross-check analytical sensitivities with finite differences, then test equivalent descriptor sets on frozen held-out property families under matched total resource budgets. Only an independent reproduction should unlock any separate carbon-specific study.
