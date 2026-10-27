# Research gap RG-MAT-SYMBOLIC-ENSEMBLE-001 — symbolic interatomic-potential reproduction and carbon transfer

**Opened:** 2026-10-27  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Primary owner:** Lane D — device/material physics  
**Cross-lane consumers:** E (biomass/carbon materials), G (manufacturing/process), F (evidence/economics), H (publication)  
**Stable IDs:** RG-MAT-SYMBOLIC-ENSEMBLE-001; EQN-MAT-001; INV-030; INV-034/035

## Objective

Test whether a physically structured symbolic-ensemble workflow improves held-out interatomic-potential predictions and robustness under matched data/resource budgets, then decide whether a separate carbon-specific study is justified. The first reproduction target is aluminum because that is the material reported in the source; Pangola-derived carbon is a separate, later target and cannot inherit aluminum results.

## Source and current evidence

Varughese et al., “Symbolic ensemble learning enables discovery of fast accurate physics-based interatomic potentials,” *Physical Review Materials* 10, 103802, published 2026-10-09, DOI https://doi.org/10.1103/gkpd-gtzp; public preprint https://arxiv.org/abs/2609.16526.

The paper reports physically structured EqNN/EAM symbolic potentials trained on DFT data for aluminum, with multiple optimization/transfer routes and a weighted ensemble. The reported evidence is a third-party computational materials study. UQPU has not reproduced its code/data, checked its reported errors, synthesized material or validated a component.

## Blocking unknowns

- Exact code/data availability and version-of-record supplementary material must be pinned; APS full text was access-restricted during the 2026-10-27 surveillance.
- No UQPU reproduction environment, frozen dataset manifest, held-out split or independent baseline run exists.
- The source's energy-training objective and separate force evaluation must not be collapsed into one metric.
- No carbon-specific dataset, material characterization, independent experiment or application functional-unit contract exists for a Pangola-derived candidate.
- No device-level or lifecycle cost model is supported by this literature alone.

## Unlock criteria

1. Pin source revision, source code/data (or explicitly document unavailability), DFT settings, element/configuration coverage, cutoff, seeds, software versions and resource limits.
2. Freeze train/validation/test partitions before tuning; reserve held-out structures and property families.
3. Compare incumbent EAM, each reproducible symbolic candidate, weighted ensemble and a declared ML-interatomic-potential baseline with matched training data and total resource budgets.
4. Report energy and force errors separately, uncertainty, equation-of-state curvature, phonon dispersion, elastic/surface/defect/melting metrics where reference data exist, model complexity, wall-clock, host compute, energy where measurable and all failed seeds.
5. Apply dimensional, invariance, stability, cutoff and domain checks; run adversarial counterexample search over strained and non-equilibrium configurations.
6. Require an independent rebuild before concluding the ensemble transfer is reproduced.
7. Only then open a carbon-specific experiment with a distinct carbon dataset and explicit target function. For INV-030, compare the material's measured function against the incumbent component and include manufacturing, lifetime, recovery/recycling and lifecycle cost.
8. Do not claim Pangola carbon can replace elemental metals/minerals. Where chemistry or function forbids direct substitution, test minimization, hybridization, recovery or architecture-level elimination instead.

## Falsifier / stop rule

Stop the proposed transfer if the weighted ensemble fails to improve the preregistered held-out metrics over the declared incumbent, fails stability/invariance/domain checks, or increases total model-development and inference cost without compensating utility. If the source's artifacts cannot be recovered, mark reproduction BLOCKED and use a separately documented, non-identical benchmark rather than claiming replication.

## Mission boundary

This gap advances the *method-selection* part of INV-034/035 and provides a possible screening path for INV-030. It is not evidence of a Pangola material, bio-oil, fusion, chip-manufacturing, UQPU, financing or Data-Center-to-Phone advantage. Present physical laws and element identity remain binding.
