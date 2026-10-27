# Research gap RG-MAT-SISSO-SENSITIVITY-001 — symbolic materials-gene sensitivity and identifiability

**Opened:** 2026-10-27  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Primary owner:** Lane D — device/material physics  
**Cross-lane consumers:** E (biomass/carbon), F (evidence/economics), G (manufacturing), H (publication)  
**Stable links:** FND-006; EQN-001–006; INV-030; INV-034/035

## Objective

Determine whether derivative-based sensitivity analysis can distinguish stable, physically interpretable material descriptors from non-identifiable or reparameterization-sensitive symbolic models under held-out validation and matched resource budgets.

## Source and current evidence

Foppa and Scheffler, *Physical Review Materials* 10, 093601 (published 2026-09-08), DOI https://doi.org/10.1103/gk23-cfh1. The peer-reviewed APS article studies analytical sensitivity of SISSO-derived materials genes and reports equivalent information in distinct gene combinations for a perovskite lattice-constant example. The paper links public code at https://github.com/lfoppa/sensitivity_analysis_sisso.

This is external published methodology. UQPU has not reproduced the code, dataset or sensitivity values. No descriptor, causal mechanism, physical law or material substitution is accepted by this gap.

## Blocking unknowns

- Exact repository revision, data/supplement checksums and software environment have not been pinned by UQPU.
- No independent rebuild or finite-difference cross-check has been run.
- No perturbation study establishes robustness under correlated features, reparameterization, noise or held-out material families.
- No carbon-specific or Pangola-specific dataset, application functional unit, independent material qualification or lifecycle-cost evidence exists.

## Unlock criteria

1. Pin source revision, code/data/supplement hashes, feature grammar, units, domain and compute budget.
2. Freeze train/validation/test splits and held-out composition/property families before model selection.
3. Reproduce the perovskite example; compare analytical derivatives against finite differences and retain failed/counterexample cases.
4. Compare equivalent or near-equivalent symbolic descriptor sets under matched candidate evaluations, seeds, wall/CPU time and memory.
5. Evaluate held-out prediction, sensitivity stability, uncertainty, model complexity and robustness to correlated-feature perturbations and unit-preserving reparameterization.
6. Treat feature importance as model sensitivity, not causal identification. Require independent physical evidence for causal or law claims.
7. Any later Pangola-carbon route must use a distinct carbon dataset and an application-specific functional benchmark; perovskite results do not transfer automatically.

## Falsification / stop rules

The proposed method transfer fails if sensitivity rankings change materially under equivalent reparameterizations, the apparent insight disappears on held-out families, or the model violates domain/units/symmetry constraints. A better fit or derivative plot alone is insufficient. Preserve failed seeds and false discoveries.

## Mission boundary

This gap advances the method-design part of FND-006 and EQN-002/003/004/006 only. It supplies no UQPU performance, new physical law, Pangola-carbon substitution, bio-oil yield/cost, net fusion electricity, financing-rate change or Data-Center-to-Phone result. INV-029–035 and INV-025–027 remain evidence-gated.
