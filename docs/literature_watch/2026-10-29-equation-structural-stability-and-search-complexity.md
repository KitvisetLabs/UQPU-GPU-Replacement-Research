# Literature watch — structural stability and the computational limits of symbolic regression

**Watch date:** 2026-10-29  
**Primary owner:** Lane H; interfaces A/C/F; INV-034/035  
**Evidence class:** OFFICIAL ICML 2026 / PMLR PAPERS; THIRD-PARTY RESULTS; UQPU REPRODUCTION NOT RUN

## Sources

- Yu et al., “Beyond Accuracy and Complexity: The Effective Information Criterion for Structurally Stable Symbolic Regression,” PMLR 306 (ICML 2026): https://proceedings.mlr.press/v306/yu26az.html. Authors' implementation: https://github.com/tsinghua-fib-lab/EIC.
- Soubki and Cranmer, “How Hard Is Science?”, PMLR 306 (ICML 2026): https://proceedings.mlr.press/v306/soubki26a.html.

Neither paper title nor the EIC repository was present in the starting repository tree. These are new-to-repository sources, not papers claimed to be published today.

## Genuine delta

EIC argues that fit error and expression complexity can favor compact but numerically ill-conditioned formulas. It treats recursive evaluation as an information channel and measures rounding-noise amplification. The authors report 2–4x pretraining sample efficiency, a 22.4% improvement in generalization R-squared under EIC filtering, and 70% alignment with preferences in a study of 108 experts. These are source-reported results, not UQPU measurements; expert preference is not physical truth.

Soubki and Cranmer report fixed-parameter tractability for search parameterized by expression depth/tree size when the primitive set is fixed, while parameterizing by variable count or primitive-set size is W[1]-hard. They also report ETH-based lower bounds and approximation hardness. UQPU should declare depth/tree size, variable/primitive counts, candidate budget and compute limits; bounded search does not prove a globally correct law was found.

## Exact UQPU relevance

- INV-035 / FND-006 / EQN-001–006: numerical stability supplements but never replaces dimensional, symmetry, conservation, causality, limiting-case, held-out, counterexample, proof/experiment and independent-replication gates.
- Lane A: added a normalized finite-perturbation diagnostic with predeclared scales. It is not EIC or a physical-law score.
- Lane C: numeric scales/precision must be recorded; ratios are comparable only with the same scale definitions and perturbation design.
- Lanes D/G: device/process model equations need robustness checks; no device or factory claim follows.
- Lane E: future biomass, bio-oil or fusion surrogates require validated reference data; no commercial result is inferred.
- Lane F: equal-budget comparisons include candidate generation, failures, CPU, memory, precision and evaluation time.
- Lane H: source provenance is preserved without promoting third-party claims.

## Falsifiable follow-up

Pin EIC revision, license, dependencies, data and evaluation scripts. Freeze known-law equation families and disjoint splits. Compare fit-plus-complexity, EIC and the UQPU proxy under equal candidate/time/CPU/memory/precision budgets, including exact-recovery, null and ill-conditioned controls. Sweep precision and preregistered perturbations; report held-out error, constraint violations, numerical failures, sensitivity, false discoveries and cost per accepted candidate. Repeat on an independent equation family. If rankings change across scales, perturbations, precision or held-out families, report the instability.

**Non-claims:** no physical law, QPU advantage, memory equivalence, material substitution, accepted bio-oil, net fusion electricity, lower WACC or mission compression is established.
