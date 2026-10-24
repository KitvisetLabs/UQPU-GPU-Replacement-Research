# RG-045 — Non-finite held-out metrics in the equation-discovery promotion gate

**Date:** 2026-10-24  
**Primary owner:** Lane A — quantum programming / equation-discovery runtime  
**Integration owner:** Lane F — evidence and acceptance  
**Cross-lane publication:** Lane H  
**Status:** `CODE_FIX_COMMITTED / HOSTED_CI_PENDING / NO_SCIENTIFIC_PROMOTION`  
**Canonical base:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`

## Finding

A code audit of `software/uqpu-prototype/uqpu/equation_discovery.py` found that held-out errors were rejected only when negative. IEEE-754 `NaN` and positive infinity can pass a simple `value < 0` test. In particular, an infinite baseline error paired with a finite candidate error can make `has_heldout_improvement` return true. With the other metadata satisfied, this could incorrectly open the `ready_for_physical_candidate_claim` gate.

This is a **software validation defect**, not evidence about a physical system or about the correctness of any external paper. The invalid record must fail closed before it can influence EQN-002/003/004/005/006 or a downstream device/economic decision.

## Repair committed on the research branch

The validator now requires each supplied held-out error to be a finite, non-negative real number or `None`. Booleans and non-numeric values are rejected rather than implicitly treated as metrics. `independent_validation_count` must be a non-negative integer and cannot be a boolean. The `has_heldout_improvement` property validates its record and returns false for invalid metadata, so callers cannot bypass the guard by reading the property before explicitly calling `validate()`.

Four focused regression-test methods cover NaN/infinity in either metric, the infinite-baseline false-promotion counterexample, boolean/string/arbitrary-object metrics, and invalid validation counts. The exact-head hosted test result is **pending**; no test pass is claimed until GitHub Actions reports it.

## Minimal counterexample and falsifier

- **Incumbent assumption in code:** a negative-only check is sufficient to validate an error metric.
- **Counterexample:** `baseline_error = +inf`, `candidate_error = 0.1`, with otherwise qualifying evidence metadata.
- **Expected repaired behavior:** validation raises a finite-value error; `has_heldout_improvement` and `ready_for_physical_candidate_claim` are both false.
- **Additional falsifiers:** NaN, negative infinity, positive infinity, booleans, strings and non-real objects are all rejected.
- **Held-out/scientific boundary:** these tests establish only software guard behavior. They do not reproduce an equation-discovery paper, establish predictive generalization, or validate a physical law.

## Literature surveillance (2026-10-24)

The initial public-source scan found no additional primary result that changed the current UQPU evidence gates beyond the results already represented by the 2026-10-23 main-branch optimization-law/ancilla-QFI watch and current pending research branches. A subsequent expanded arXiv scan in this same cycle identified Zhong et al., arXiv:2610.29170 (submitted 2026-10-21), on top-down joint quantum target/compiler configuration selection. It was absent from main and the inspected PR #53/#56–#58 changed-file patches; a separate Lane-H watch and Lane-A benchmark contract were published on PR #62. This literature delta does not change the software defect finding or promote any scientific evidence. Relevant sources screened:

- AI-Newton, APS accepted-paper record dated 2026-10-09: https://journals.aps.org/prresearch/accepted/10.1103/dvvc-4rsr
- Data-driven progressive discovery of physical laws / CoSR, APS accepted-paper record dated 2026-10-06: https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q
- Evaluation of quantum Fisher information for large systems via an ancilla, arXiv:2610.29146, submitted 2026-10-21: https://arxiv.org/abs/2610.29146
- Graph sparsification/decomposition for QAOA, *Quantum* (2026-08-07): https://doi.org/10.22331/q-2026-08-07-2185

The sources motivate disciplined equation-search, information and workload accounting, but remain third-party literature. No UQPU paper reproduction, real-QPU run, energy measurement, materials test, fuel test, fusion-electricity measurement or project-finance measurement was performed in this cycle. CoSR-specific preregistration is already proposed in open PR #56; this artifact avoids duplicating its literature watch.

## Next gate

1. Wait for exact-head GitHub Actions on this branch.
2. If CI passes, review the change and merge through the repository's normal integration path.
3. Add a compact property-based or table-driven audit for non-finite values in adjacent equation/benchmark result schemas without weakening any evidence gate.
4. Resume the EQN-COSR-001 synthetic known-law benchmark only under its frozen grammar, evaluator, equal resource caps, blind held-out split and retained-failure contract.

## Non-claims

This repair does not demonstrate quantum advantage, GPU/CPU/NPU/RAM/VRAM/storage replacement, a new physical law, Data-Center-to-One-Phone compression, Pangola-material substitution, ultra-low-cost commercial bio-oil, commercial low-cost fusion electricity, or lower financing rates/WACC. INV-025/026/027 and INV-029 through INV-035 remain unchanged. All root directives 00–06, the Kanusanan Pongpan­na Model, strategic references and Thai/English/Chinese/Japanese/Korean/German master-plan links remain canonical and untouched.
