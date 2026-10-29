# Literature watch — LegoSR and residual-informed equation discovery

**Date checked:** 2026-10-29  
**Primary owner:** Lane H / INV-035 and FND-006; Lane A owns the matched-metric harness  
**Stable ID:** LIT-2026-EQN-LEGOSR-RISR-ROBUSTNESS  
**Evidence class:** official arXiv preprints; third-party benchmark claims; not reproduced by UQPU

## Primary sources and source dates

1. Hao Mao, Xu T. Liu, Peng Zhao, Shuai Lu and Yuntian Chen, “LegoSR: A Unified Framework for Self-improving Agent-Guided Scientific Discovery,” arXiv:2610.33465, posted 2026-10-24: https://arxiv.org/abs/2610.33465
2. Haobo Li, Wenshuo Zhang, Wenxiao Zhao, Eunseo Jung, Rui Sheng, Yushi Sun, Peiqin Zhuang, Hao Chen and Fenghua Ling, “RISR: Residual-Informed Scientific Equation Discovery with Large Language Models,” arXiv:2610.11387, posted 2026-10-08: https://arxiv.org/abs/2610.11387

These are official preprints, not peer-reviewed project validation. Their reported results remain author claims until independently reproduced.

## Genuine novelty

LegoSR standardizes seven heterogeneous equation-discovery solvers through a shared Equation Intermediate Representation and experiment record, while its agent uses solver knowledge and prior outcomes to choose and adapt searches. The authors report recovery close to the union of seven expert-tuned solvers on noisy ODE/PDE tasks and up to 29 percentage points over a generic agent using the same model, tools and budget.

RISR conditions formula proposals and refinement on pointwise residual patterns rather than only aggregate loss. Its paper reports in-distribution accuracy of 63.57% / 38.50% and out-of-distribution accuracy of 56.07% / 38.24% at 1% / 0.1% pointwise relative-error tolerances on its benchmark suite. These are source-reported values, not UQPU measurements.

The combined methodological lesson is that a common candidate representation and immutable experiment record enable cross-solver comparisons; residual-guided search can propose where a candidate needs correction; deterministic metrics and held-out data—not the agent—must decide whether a candidate survives.

## Limitations and failure modes

- UQPU has not reproduced either implementation, checkpoint, dataset, training recipe, benchmark score or runtime/energy result.
- Benchmark recovery does not establish that a candidate is a physical law, causally correct, or valid outside sampled regimes.
- Residual-guided correction can overfit noise, derivative-estimation errors, leakage or a narrow regime. OOD scores remain benchmark-specific.
- A shared representation does not make solver scores interchangeable. Native scores, units, coefficient fitting, derivative estimation and search budgets must be recorded separately.
- A transformation certificate hash is a provenance pointer, not proof that a transformation preserves semantics. Equivalence needs a checked derivation, proof or independently reviewed mapping.
- Better fit, a kernel-checked proof, and physical validation are distinct gates. A proof certifies the encoded statement under its assumptions.

## Exact project relevance

- **INV-035 / EQN-001–006 / FND-006:** motivate multi-method search where residuals generate hypotheses, explicit constraints filter them, and held-out/counterexample/formal/experimental checks govern promotion.
- **Lane A:** use a matched held-out metric helper before comparing discovery backends or downstream resource estimates.
- **Lane C / INV-029:** group splits by equation family, physical system, specimen or source to prevent related samples leaking across train/validation/test. Data, memory and reconstruction cost remain explicit.
- **Lane D/G:** no fabrication or device claim follows from a discovered formula; a device consequence requires causal mechanism, process window, yield and reliability data.
- **Lane E / INV-030–032:** possible future method analogues for materials, biomass conversion and fusion-plant models only after domain-specific data and accepted-function accounting exist. No Pangola substitution, accepted bio-oil or net fusion-electricity result is implied.
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
