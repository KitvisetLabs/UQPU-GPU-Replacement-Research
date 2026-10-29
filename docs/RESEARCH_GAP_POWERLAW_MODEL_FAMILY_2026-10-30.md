# Research gap RG-A-EQN-POWERLAW-FAMILY-001 — fit score versus model-family validity

**Opened:** 2026-10-30  
**Primary owner:** Lane A  
**Evidence owner:** Lane F  
**Publication owner:** Lane H  
**Status:** SYNTHETIC COUNTEREXAMPLE ADDED / REPOSITORY CI UNVERIFIED / MODEL_ONLY  
**Related:** Batch 137, Batch 138, FND-006, EQN-001–EQN-006, INV-034/035  
**Source context:** https://proceedings.mlr.press/v306/n-guessan26a.html

## Evidence added

A pure-power-law log-linear reference was challenged using synthetic data from (y=1+x^2), which is not a pure power law. For training points (x=(1,2,4,8,16)), the restricted model achieved log-space (R^2\approx0.99445), yet predicted about 776.576 at held-out (x=32), versus the true 1025 (24.24% relative error). This deterministic counterexample is designed to show that high in-sample fit does not identify the correct model family.

A regression test was added to `software/uqpu-prototype/tests/test_scaling_exponent_baseline.py`. The numeric counterexample was independently checked in an isolated arithmetic calculation; the repository suite and exact-head hosted CI remain unverified.

## Interpretation

- The fitted exponent is a parameter of the assumed model family, not automatically a physical scaling law.
- A small residual on a narrow observed range is not a uniqueness proof, a causal mechanism, or evidence of a new constitutive law.
- Parameter identifiability conditional on a family and discrimination among competing families are separate gates.
- Held-out prediction must be evaluated beyond the fit range and by regime, with noise and measurement uncertainty controlled.

## Remaining blockers

1. Full repository tests and exact-head Actions.
2. Noise, outlier, sensor uncertainty, piecewise and multiscale fixtures.
3. Group-disjoint fit/selection/test splits; preregistered ranges and repeated seeds.
4. Comparison against conventional symbolic regression and MSN-PINN with matched time/CPU/memory/candidate budgets.
5. Uncertainty intervals, failed runs, counterexamples and false-discovery rate.
6. Dimensional/symmetry/conservation/causality checks and domain-specific measurement before any D/E/G technology consequence.
7. No transfer of this synthetic result to BIO-001, FUS-001, material performance, QPU advantage, financing economics or a physical law.

## Unlock criteria

The next gate passes only if the competing model family is explicitly included, held-out tests are untouched during selection, uncertainty and failure rates are reported, resource budgets are matched, and independent reproduction is available. Any claim of a changed physical law additionally requires a distinct observable and discriminating experiment.
