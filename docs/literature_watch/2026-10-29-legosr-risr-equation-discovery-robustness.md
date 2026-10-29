# Literature watch — LegoSR and residual-informed equation discovery

**Date checked:** 2026-10-29  
**Primary owner:** Lane H / INV-035 and FND-006; Lane A owns the matched-metric harness  
**Stable ID:** LIT-2026-EQN-LEGOSR-RISR-ROBUSTNESS  
**Evidence class:** official arXiv preprint plus previously indexed preprint; third-party benchmark claims; not reproduced by UQPU

## Source accounting

**New-to-repository source:** Hao Mao, Xu T. Liu, Peng Zhao, Shuai Lu and Yuntian Chen, “LegoSR: A Unified Framework for Self-improving Agent-Guided Scientific Discovery,” arXiv:2610.33465, posted 2026-10-24: https://arxiv.org/abs/2610.33465

**Previously indexed prior art, not a new delta:** Haobo Li et al., “RISR: Residual-Informed Scientific Equation Discovery with Large Language Models,” arXiv:2610.11387, posted 2026-10-08: https://arxiv.org/abs/2610.11387. UQPU already covered RISR in the 2026-10-15 equation-discovery identifiability watch and 2026-10-28 residual/conjecture watch. It is retained here only as a comparator for the new LegoSR result.

These are official preprints, not peer-reviewed UQPU validation. Reported benchmark results remain author claims until independently reproduced.

## Genuine novelty of LegoSR

LegoSR standardizes seven heterogeneous equation-discovery solvers through a shared Equation Intermediate Representation and experiment record. Its agent uses solver knowledge and prior outcomes to select and adapt searches. The authors report recovery close to the union of seven expert-tuned solvers on noisy ODE/PDE tasks and up to 29 percentage points over a generic agent using the same model, tools and budget.

RISR's previously indexed method conditions formula proposals and refinement on pointwise residual patterns rather than only aggregate loss. Its source-reported in-distribution and out-of-distribution scores are not new project evidence and are not repeated here as a new finding.

The method-level lesson is that shared candidate representation and immutable experiment records enable cross-solver comparisons; residual-guided search can propose where a candidate needs correction; deterministic metrics and held-out data—not the agent—must decide whether a candidate survives.

## Limitations and failure modes

- UQPU has not reproduced LegoSR or RISR implementations, checkpoints, datasets, training recipes, benchmark scores or runtime/energy results.
- Benchmark recovery does not establish that a candidate is a physical law, causally correct or valid outside sampled regimes.
- Residual-guided correction can overfit noise, derivative-estimation errors, leakage or a narrow regime.
- A shared representation does not make native solver scores interchangeable. Units, coefficient fitting, derivative estimation, candidate budget and resource use must remain recorded.
- A transformation certificate hash is a provenance pointer, not proof that a transformation preserves semantics. Equivalence needs a checked derivation, proof or independently reviewed mapping.
- Better fit, a kernel-checked proof and physical validation are distinct gates.

## Exact project relevance

- **INV-035 / EQN-001–006 / FND-006:** motivate multi-method search where residuals generate hypotheses, explicit constraints filter them, and held-out/counterexample/formal/experimental checks govern promotion.
- **Lane A:** use a matched held-out metric helper before comparing discovery backends or downstream resource estimates.
- **Lane C / INV-029:** group splits by equation family, physical system, specimen or source to prevent related samples leaking across train/validation/test. Data, memory and reconstruction cost remain explicit.
- **Lane D/G:** no fabrication or device claim follows from a discovered formula; a device consequence requires a causal mechanism, process window, yield and reliability data.
- **Lane E / INV-030–032:** possible future method analogues for materials, biomass conversion and fusion models only after domain-specific data and accepted-function accounting exist. No Pangola substitution, accepted bio-oil or net fusion-electricity result is implied.
- **Lane F / INV-033:** include candidate-evaluation count, CPU/GPU time, memory, measured energy if available, validation cost and time-to-evidence. No WACC effect is measured.
- **Lane H:** retain strategic-finance and multilingual links as context, not scientific evidence.

## Proposed falsifiable follow-up

1. Pin source revisions, code/checkpoints, licenses, dependencies and benchmark provenance.
2. Start with synthetic known equations and exact ground truth; add domain datasets only after units, sampling and measurement uncertainty are documented.
3. Freeze grouped train/validation/test splits by equation family or physical system. Keep equivalent algebraic/unit/coordinate transformations explicitly identified.
4. Compare static symbolic regression, search-controller, residual-guided search and shared-representation multi-solver workflows under equal candidate, wall-time and compute budgets.
5. Pre-register pointwise relative-error tolerances, complexity, interval coverage, OOD criteria and counterexample rules. Preserve failures and false discoveries.
6. Require checked transformation equivalence, independent re-run and a discriminating physical observable before an equation supports an engineering claim.

**Falsifiers:** gains disappear on held-out equation families/regimes; candidate complexity grows without stable predictive improvement; transformations alter meaning; results fail under equal budgets or independent re-run; or the physical interpretation violates units, symmetry, conservation, causality or measurements.

## Non-claims

No new physical law, theorem about nature, QPU advantage, 100x / 100,000,000x advantage, RAM/VRAM/storage equivalence, material substitution, commercial bio-oil, net fusion electricity, reduced financing rate/WACC or Data-Center-to-One-Phone milestone is established.
