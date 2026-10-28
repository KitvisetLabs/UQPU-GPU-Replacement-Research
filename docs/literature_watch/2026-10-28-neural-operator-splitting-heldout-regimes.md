# Literature watch — test-time neural-operator splitting for unseen physics regimes

**Date checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance/publication  
**Implementation interface:** Lane A — split certificates and model-evaluation contracts  
**Cross-lane consumers:** C (state and data movement), D/G (process models), E (thermal-fluid/material/energy models), F (evidence and economics)  
**Evidence class:** LITERATURE_ONLY  
**Related:** INV-034, INV-035, FND-006, EQN-001–010, RG-045, RG-A-TEMPORAL-HOLDOUT-ORDERING-001

## Primary source

Louis Serrano, Jiequn Han, Edouard Oyallon, Shirley Ho and Rudy Morel, “Test-time Generalization for Physics through Neural Operator Splitting,” *Proceedings of the 43rd International Conference on Machine Learning*, PMLR 306 (2026), pp. 109205–109235. Official record: https://proceedings.mlr.press/v306/serrano26a.html.

## Reported method and genuine novelty

The paper targets neural-operator failure on inputs outside training distributions, including new initial conditions, unseen PDE coefficients or unseen physics. It composes operators from a pretrained dictionary at test time to approximate unseen dynamics without changing the pretrained weights. This is a method for constructing a candidate solution operator, not a claim that the governing equations have changed.

The useful project-level distinction is that “no weight update” is not the same as “no adaptation or extra cost”: test-time operator selection/composition can still consume observations, search time and compute. UQPU evaluation should measure that complete inference/adaptation budget.

## Limitations and evidence boundary

- The paper's results are external author-reported results on its stated tasks; this cycle did not download its code/data, verify licensing, or reproduce a benchmark.
- Generalization is conditional on the pretrained operator dictionary, candidate-composition search, observed test context and tested PDE families. It is not a universal guarantee for arbitrary unseen physics.
- A small prediction error alone does not establish conservation, admissible state bounds, a correct physical model or an accepted engineering result.
- The method does not discover a new physical law by declaration and cannot replace present physics in engineering claims.

## Exact UQPU relevance

- **Lane A / INV-035:** add strict chronological and group-disjoint holdouts so temporal interpolation is not misreported as future-time extrapolation. Keep equation discovery, solution-operator approximation and physical-law validation as separate tasks.
- **Lane C:** record field bytes, state preparation, transfers, peak memory and reconstruction when comparing model composition against direct numerical solvers.
- **Lanes D/G:** process-control and manufacturing models may have time-dependent drift; any transfer needs measured process data and yield/defect outcomes.
- **Lane E / INV-030–032:** operator surrogates may support exploratory heat/fluid, biomass-conversion or fusion-component models, but cannot establish Pangola-material performance, saleable bio-oil economics or net delivered fusion electricity.
- **Lane F / INV-033:** count model training amortization, test-time search, inference and failed runs in the same cost basis; no WACC or interest-rate effect follows from this method.

## Falsifiable follow-up

1. Pin source revision, code/data hashes, license and environment before execution.
2. Freeze a chronological future-time test window plus separate coefficient/geometry holdouts before model selection; validate the raw-record split manifest and a positive embargo.
3. Compare operator splitting, a direct pretrained operator, a matched fine-tuned model and a trusted numerical reference on the same PDE tasks.
4. Preregister at least 30 seeds per stochastic arm and identical total resource ceilings. Report relative error, PDE residual, boundary/initial error, conservation/bounds, long-rollout stability, uncertainty, wall time, CPU/GPU time, peak memory, retries and energy where measurable.
5. Preserve all failed seeds and counterexamples. If gains disappear on future-time or coefficient/geometry holdouts, reject the broad generalization claim.
6. Do not transfer a surrogate result to materials, fuel, fusion or device claims without independent physical validation and full economics.

**Disposition:** relevant new method lead; no UQPU reproduction, new equation, physical law, QPU advantage or economic advantage established.
