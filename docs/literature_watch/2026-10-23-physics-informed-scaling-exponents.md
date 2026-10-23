# Literature watch — 2026-10-23: physics-informed scaling-exponent discovery

**Access date:** 2026-10-23  
**Primary owner:** Lane H — literature synthesis  
**Integration:** Lane A (equation-discovery harness), Lane F (benchmark/evidence), with conditional future links to E/D/G  
**Evidence class:** LITERATURE_ONLY / PEER-REVIEWED CONFERENCE METHOD  
**UQPU evidence promotion:** none

## Primary source and publication date

Gnankan Landry Regis N’Guessan and Bum Jun Kim, “Discovering Scaling Exponents with Physics-Informed Müntz-Szász Networks,” *Proceedings of the 43rd International Conference on Machine Learning*, Proceedings of Machine Learning Research 306:91419–91445 (ICML, 2026-07-06 to 2026-07-11). Official proceedings and citation: https://proceedings.mlr.press/v306/n-guessan26a.html.

## Genuine methodological delta

The paper introduces a physics-informed power-law basis whose exponents are trainable and whose output includes both a solution and its scaling structure. It states identifiability conditions and reports recovery results for noisy/sparse sampling, Laplace corner singularities, singular Poisson problems and a 40-configuration wedge benchmark. The proceedings page reports that constraint-aware training improved accuracy over naive training on the studied benchmarks.

For UQPU’s INV-035 workflow, this suggests a useful generator/evaluator family when the target is an asymptotic exponent or scaling law, not necessarily a full symbolic governing equation. It complements rather than replaces symbolic regression, theorem checks, and the current equation-candidate contract.

## Limits and evidence boundary

- Results are scoped to the paper’s stated function classes, assumptions and benchmark problems; they do not imply general discovery of unknown causal laws.
- Identifiability is conditional and must be checked for the actual data-generating regime.
- The paper is not a UQPU workload result, real-QPU result, materials experiment, fuel/electricity result, or economic measurement.
- It does not establish an advantage for any quantum algorithm, lower total cost per accepted task, material substitution, commercial bio-oil, commercial fusion, lower project WACC, or physical compression into one phone.
- No independent UQPU reproduction has been performed in this cycle.

## Exact project relevance

- **FND-006 / EQN-001, EQN-002, EQN-006:** add a candidate method for exponent recovery and asymptotic structure, with explicit identifiability and constraint checks.
- **Lane A:** the output can be a scaling hypothesis to support resource models; it does not itself improve compiler/runtime execution.
- **Lane C:** any later memory or state scaling claim still needs an output-information contract and may not equate Hilbert-space dimension with readable classical storage.
- **Lane D/G:** any device/factory use requires measured physical variables, process limits and independent validation.
- **Lane E:** potential relevance to biomass conversion or fusion scaling is only a future benchmark possibility; no BIO-001 or FUS-001 evidence is added.
- **Lane F:** compare full training/search compute, runtime and energy where measurable; reported fit accuracy alone is not economic efficiency.
- **INV-029/033:** no Data-Center-to-One-Phone or financing/interest effect follows from this method paper.

## Proposed falsifiable follow-up — EQN-SCALE-001

1. Freeze train/validation/test splits by geometry and parameter regime before fitting.
2. Compare a Müntz-Szász-style exponent model, a generic PINN, and symbolic regression with matched data, noise and compute budgets.
3. Use known Laplace/Poisson singularity cases as controls; add held-out geometries and a separate out-of-domain regime.
4. Check dimensions, boundary-condition compatibility, known limiting cases, identifiability and adversarial counterexamples.
5. Report exponent error, solution error, calibration/uncertainty, false discoveries, runtime and energy where measurable.
6. Reject promotion if the gain vanishes on held-out geometries, violates constraints, or depends on unreported compute/data.

Passing would be MODEL_ONLY computational evidence for this benchmark, not a new physical law. Any proposed extension to biomass, fusion, device physics or economics requires domain-specific data and a separate evidence gate.

## Invariant contribution

This watch operationalizes INV-034/035’s mathematics-first but evidence-gated method. It preserves current physics as the engineering baseline, encourages alternative equation hypotheses, and requires held-out prediction, counterexamples and independent validation before any physical or technology claim.
