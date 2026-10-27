# Literature watch — 2026-10-27: analytical sensitivity and non-identifiability in SISSO materials genes

**Accessed:** 2026-10-27  
**Primary owner:** Lane H — literature synthesis and strategic publication  
**Technical owner:** Lane D — device/material physics; Lane E is the biomass/materials consumer  
**Integration owner:** Lane F — benchmark/evidence/economics  
**Feeds:** FND-006, EQN-001–006, INV-030, INV-034/035  
**Evidence class:** LITERATURE_ONLY — peer-reviewed primary article  
**Project evidence promotion:** none

## Source and genuine novelty

Lucas Foppa and Matthias Scheffler, “How SISSO-derived materials genes shape materials properties: An analytical sensitivity analysis,” *Physical Review Materials* 10, 093601, published 8 September 2026. DOI: https://doi.org/10.1103/gk23-cfh1. The APS article is open access; it links supplementary material and the authors' reproducibility code at https://github.com/lfoppa/sensitivity_analysis_sisso.

The useful methodological delta is an analytical-derivative sensitivity analysis for SISSO symbolic-regression descriptors (“materials genes”). The authors explicitly examine the fact that multiple gene combinations can produce similarly accurate models, and use sensitivity analysis to expose how distinct combinations can encode equivalent information. Their worked physical example concerns the equilibrium lattice constant of perovskites; the article highlights valence-orbital radii, nuclear charges and products of those quantities as influential descriptors. This is a method for interrogating candidate models, not proof that one expression is the unique causal law.

## Limitations and evidence boundary

- The result is a domain-specific materials-model study, not a universal theorem of symbolic-regression identifiability.
- Derivatives describe local or domain-conditioned model sensitivity; correlated features, reparameterization, extrapolation and dataset choice can change interpretation.
- A model may have stable predictions while individual symbolic terms are non-identifiable; conversely, a high sensitivity score is not by itself causal evidence.
- UQPU has not run the authors' code, rebuilt the paper's dataset, reproduced the numerical sensitivity analysis or independently validated any material.
- No new physical law, Pangola-carbon property, chip/device benefit, fuel/fusion result, energy saving or economic advantage follows from this source.

## Exact project relevance

- **EQN-002 / EQN-003:** extend equation-discovery evaluation beyond fit and expression recovery to sensitivity stability, equivalent-feature classes and parameter/feature perturbation.
- **EQN-004:** use unstable or counterexample-sensitive descriptors to prioritize adversarial tests and preserve false discoveries.
- **EQN-006 / INV-037:** distinguish an interpretable fitted formula from an identifiable mechanism; report uncertainty and equivalence classes rather than selecting a unique expression by appearance.
- **INV-030 / D–E–G:** the method may eventually help screen material-property models, but the perovskite result cannot be transferred to Pangola carbon, graphite, diamond or a semiconductor without separate datasets and functional tests.
- **INV-029 / F:** any eventual materials-model speedup must be measured as a component of an end-to-end accepted-service and lifecycle-cost contract, not as a proxy for phone-class physical compression.

## Falsifiable follow-up: RG-MAT-SISSO-SENSITIVITY-001

1. Pin the paper version, repository commit, dataset/supplement checksums, software environment, feature-generation grammar and split protocol. Record missing artifacts explicitly.
2. Reproduce the perovskite example before transferring the method to any other material. Compare analytical derivatives with independently computed finite-difference checks over a declared valid domain.
3. Refit multiple equally accurate or near-equivalent descriptor sets under matched candidate-evaluation and compute budgets. Report held-out prediction, feature/sensitivity stability, uncertainty and model complexity.
4. Stress the result under correlated-feature perturbations, unit-preserving reparameterizations, noise, alternative train/test splits and held-out composition/property families.
5. Use counterexamples and domain-boundary checks; retain failed seeds and descriptors. A sensitivity narrative is rejected if it changes materially under equivalent reparameterization or fails on held-out material families.
6. Only after independent reproduction may a separate material-specific dataset be considered. Pangola-carbon work must identify an application function and cannot inherit perovskite evidence.

**Stop rule:** do not promote a descriptor to a physical law or causal mechanism from fit, derivative magnitude or interpretability alone. Promotion requires dimensional/symmetry/domain checks, held-out prediction, counterexample search and independent evidence appropriate to the claim.
