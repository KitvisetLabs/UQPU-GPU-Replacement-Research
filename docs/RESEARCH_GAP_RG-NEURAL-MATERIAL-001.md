# Research gap RG-NEURAL-MATERIAL-001 — full-order validation and identifiability in hyperreduced neural-material discovery

**Opened:** 2026-10-27  
**Primary owner:** Lane E — materials/energy/infrastructure  
**Cross-lane owners:** Lane D/G — device/package/manufacturing co-design; Lane F — evidence and economics; Lane H — literature provenance  
**Related work item:** MAT-HYPERREDUCE-001  
**Status:** OPEN — source preprint located; no UQPU source-exact reproduction

## Observed result

Holthusen, Knipper and Linka’s arXiv preprint 2610.31322 (submitted 2026-10-22) combines proper orthogonal decomposition, energy-conserving sampling and weighting, adjoint sensitivities, and adaptive reduced-basis/sample updates for inverse identification of polyconvex neural hyperelastic materials. The authors report lower training cost on two experimental datasets and a synthetic 3D example.

## Gap

No source-exact code/data/solver bundle has been pinned and independently reproduced by UQPU. The published results do not yet show that the same reduction will retain accuracy on UQPU-relevant materials, localized deformation, additional loading paths or package/substrate structures. The paper itself reports weaker efficiency under localized deformation and states that the information content of the experimental data limits material identifiability.

## Unlock criteria

1. Pin the exact preprint, code/solver revisions, datasets, licenses, meshes, boundary conditions, raw-data hashes and preprocessing.
2. Reproduce a small full-order reference before comparing reduction methods.
3. Run matched full-order and POD+ECSW+adjoint training with the same data, architecture, optimizer, seeds and resource boundary.
4. Freeze held-out specimens/load paths and localization tests before tuning; preserve all failures and timeouts.
5. Independently verify full-order reaction-force/displacement predictions, equilibrium residuals, admissibility and energy accounting.
6. Quantify identifiability under force-only versus force-plus-displacement data; do not infer a unique law from a single reaction-force curve.
7. If a device/package or biomass-derived composite is proposed, first measure its actual material properties and validate the governing constitutive model on that material.

## Falsifier and non-claims

Reject promotion if held-out full-order errors exceed preregistered tolerances, localization defeats the reduction, physical admissibility checks fail, the model is not identifiable for the intended task, or the speedup disappears after basis adaptation and full-order checks. No Pangola material substitution, electrical/optical/thermal performance, device yield, commercial fuel, fusion result, financing effect or new physical law is claimed.

The append-heavy RESEARCH_GAPS.md and WORKLOG.md remain untouched until safe full-file reconciliation.
