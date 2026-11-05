# EQN-STRUCTURE-001 — structural-guidance calibration work item

**Primary owner:** Lane F — economics, benchmarks, evidence and integration  
**Implementation support:** Lane A — quantum programming / equation-discovery tooling  
**Publication support:** Lane H  
**Opened:** 2026-10-25  
**Evidence class:** LITERATURE_ONLY + SOFTWARE_DIAGNOSTIC  
**Status:** OPEN / EXACT-HEAD-CI-PENDING

## Decision question

Does a structural signal improve the number of correctly recovered, constraint-valid equations per unit of total search cost beyond numerical fit and standard model-selection baselines?

## Source and non-reproduction statement

L2G-SR (Huang et al., arXiv:2610.20685, submitted 2026-10-14) reports a learned structural verifier that complements numerical error. This work item does not reproduce the model, verifier training, benchmark, or paper's exact tree-edit metric. The current `uqpu.equation_structure` helper is a deterministic transparent baseline only.

## Preregistered experiment

1. Freeze known-law families with (K=1,2,3), explicit variables/units, symmetries, conservation/causality expectations, limiting cases and a restricted operator grammar.
2. Generate multiple noisy/correlated observations and distractor variables; reserve law-family-disjoint validation and scale-shift holdout partitions.
3. Declare equivalence rules before evaluation: commutative/associative rewrites, coefficient abstraction policy, unit rescaling, and optional exponent preservation.
4. Compare residual-only selection, BIC, blocked held-out error, the transparent structure metric as post-hoc known-truth diagnostic, and a learned verifier only if its training and evaluation code can be pinned and audited.
5. Match candidate slots, wall-clock, host compute/memory and model-training/inference budgets. Count failed runs and retries; report energy only if measured.
6. Never provide the true target formula or true structural distance to a runtime selector. Ground truth is used only for synthetic fixture construction and post-hoc scoring.

## Required metrics

- exact structural recovery and normalized structural distance;
- held-out predictive error and scale-shift/extrapolation error;
- false-discovery rate and false multi-law rate;
- unit/equivalence invariance and constraint violations;
- counterexample survival and replicate stability;
- candidates evaluated, rejected candidates, failures/retries;
- wall-clock, tokens, host memory/compute, energy where measurable;
- total cost per accepted formula, including training amortization once per pinned model hash.

## Acceptance / falsification

**Pass:** preregistered improvement in accepted, held-out-valid equation yield under matched budgets, with no increase in false discoveries or physical-constraint violations and stable results across declared equivalences.

**Fail / disable:** advantage disappears on law-family or scale-shift holdouts; rankings change under equivalent rewrites or unit rescaling; or false-discovery/constraint-violation rates rise. Preserve null and failed cases.

## Cross-lane handoff

- A: use the helper only as an evaluator-side diagnostic; do not feed hidden ground truth to the candidate ranker.
- B: no provider execution is part of this experiment.
- C: account for candidate/data memory and I/O only if measured; no classical-storage replacement claim.
- D/G: do not infer material or device validity from structural similarity.
- E: process-specific material, biomass and fusion laws need separate measurements and domain constraints.
- F: own preregistration, matched-budget accounting, false-discovery analysis and acceptance decision.
- H: publish method and negative results without promoting third-party claims.

No QPU job, wet-lab experiment, fabrication, purchase or funding action is authorized by this work item.
