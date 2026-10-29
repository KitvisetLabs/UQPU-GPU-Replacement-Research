# Research gap RG-A-EQN-SCALING-IDENTIFIABILITY-001 — exponent recovery and model-family discrimination

**Opened:** 2026-10-30  
**Primary owner:** Lane A — equation-discovery/reference tooling  
**Evidence owner:** Lane F  
**Publication owner:** Lane H  
**Cross-lane consumers:** B, C, D, E, G, H  
**Status:** SYNTHETIC BASELINE ADDED / EXTERNAL METHOD NOT REPRODUCED / MODEL_ONLY  
**Source:** https://proceedings.mlr.press/v306/n-guessan26a.html  
**Related:** INV-034/035, FND-006, EQN-001–EQN-006.

## Current evidence

A source-specific literature watch records the ICML 2026 paper on physics-informed Müntz-Szász networks (MSN-PINN). A small log-linear reference has been implemented for the restricted positive power-law family y = a x^mu. Seven local synthetic test methods pass: exact recovery, held-out-scale prediction, unit-rescaling behavior, degenerate and near-degenerate design rejection, invalid-data rejection and zero-exponent recovery.

These results are synthetic software checks only. They neither reproduce MSN-PINN nor establish physical-law discovery, general identifiability among competing equation families, or technology advantage.

## Open blockers

- The paper's source implementation, supplementary data, license and runtime environment have not been pinned or audited.
- No independent paper reproduction or peer review has been performed.
- The baseline has not been compared against a conventional symbolic-regression method or MSN-PINN under equal hard resource budgets.
- No noisy, outlier-heavy, sensor-uncertain, piecewise, multiscale or misspecified physical dataset has been evaluated.
- The current log-span threshold is a numerical preflight, not a universal statistical identifiability theorem.
- No dimensional/symmetry/conservation/causality check or physical experiment is implied by a fit result.

## Unlock criteria

1. Pin source commit, license, environment, data and preprocessing hashes.
2. Freeze known-law and misspecified fixtures with group-disjoint fit/selection/test splits and no test leakage.
3. Preregister noise, scale-range, sample-count and failure-case sweeps.
4. Compare classical log-linear fit, conventional symbolic regression and MSN-PINN with matched candidate/time/CPU/memory/precision budgets.
5. Report exponent error, held-out error by regime, uncertainty, constraint violations, failed runs, counterexamples and false-discovery rate.
6. Account for all host/model/search resources and independent validation before any engineering/economic consequence is considered.

## Nonclaims

No new physical law, QPU advantage, readable-memory replacement, material substitution, accepted biomass fuel, net fusion electricity, lower WACC or Data-Center-to-One-Phone milestone is established. Present physical limits remain binding.
