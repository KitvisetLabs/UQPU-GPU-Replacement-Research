# MAT-HYPERREDUCE-001 — constrained neural-material inverse-model reproduction contract

**Primary owner:** Lane E — materials, energy and infrastructure  
**Co-design:** Lane D device/package mechanics and Lane G manufacturing/process systems  
**Evidence owner:** Lane F  
**Status:** PREREGISTERED DESIGN ONLY — no source build or material-model reproduction completed

## Question

Can POD + energy-conserving sampling/weighting (ECSW) + adjoint sensitivities reduce the computational cost of inverse identification of a polyconvex neural hyperelastic constitutive model while retaining full-order predictive accuracy on held-out load paths and specimens?

The scope is mechanical constitutive identification only. It does not directly identify electrical conductivity, optical response, thermal transport, electrochemistry, quantum coherence or diamond defects.

## Immutable inputs

- Official preprint: arXiv:2610.31322v1, submitted 2026-10-22.
- Exact source commit, solver version, mesh, finite-element type, solver tolerances, optimizer, precision, dependencies and build flags.
- Experimental raw files, source publication, license, acquisition/preprocessing record, inclusion/exclusion rules and hashes.
- Boundary conditions, geometry, loading histories, force/displacement channels, measurement uncertainty and train/validation/held-out specimen/load-path split.
- Full-order reference implementation, polyconvex network architecture, logarithmic normalization and growth-term parameters.
- Frozen compute/time/memory/energy budget, convergence and acceptance thresholds.

## Matched comparison

Run full-order identification and POD+ECSW hyperreduction on identical source records, architecture, loss terms, optimizer, seed set, stopping criteria and machine configuration. If separate hardware is unavoidable, label it a cross-system comparison rather than a controlled same-host experiment.

Record, per seed and load path:
- source/data/mesh/configuration hashes and accepted/rejected reason;
- training and full-order verification time, solver and adjoint call counts, convergence history and failed runs;
- peak host RAM, accelerator memory if used, basis size, sampled-element count, temporary arrays and data movement;
- reaction-force and displacement errors on training and held-out specimens;
- equilibrium residuals, energy admissibility, polyconvexity/coercivity assumptions and full-order recheck error;
- energy sensor/source, calibration, boundary and uncertainty; cost only with explicit measured/modelled hardware and energy inputs.

Use repeated seeds and report the full error-versus-cost Pareto curve. A smaller reduced model is not automatically more accurate or more physically valid.

## Required falsification tests

1. **Localization:** hold out a load path with localized deformation and check whether the adaptive basis/sample updates preserve accuracy.
2. **Identifiability:** compare force-only observations with force-plus-displacement observations and multiple independent load paths. A reaction-force fit alone cannot establish a unique constitutive law.
3. **Negative control:** intentionally undersize the basis or omit relevant modes; full-order verification must expose the error.
4. **Out-of-domain:** evaluate held-out specimens and loading paths without retraining; mark any extrapolation failure.
5. **Admissibility:** independently check the stated polyconvexity, coercivity and non-negativity construction and the solver’s equilibrium residuals.
6. **Cost boundary:** include basis updates, canary/full-order checks, preprocessing, failed optimization runs and verification cost. Reject any speedup that excludes these required costs.

## Relevance to UQPU material and device work

A later application to mechanical package/substrate/fixture behavior or a qualified carbon-containing structural composite requires a separate material-specific contract and experimental data. This contract does not transfer to Pangola carbon chemistry, semiconductor/electrical properties, thermal conductivity, diamond phase/defect engineering, bio-oil yield or fusion-facing material damage without new governing models and measurements.

Even if reproduced, this result would be a validated numerical method for the stated mechanical model and data boundary. It would not itself establish material substitution, reduced manufacturing CAPEX, lower project WACC, a physical law, or Data-Center-to-One-Phone compression.
