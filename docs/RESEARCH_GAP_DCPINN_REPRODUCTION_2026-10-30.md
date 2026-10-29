# Research gap RG-A-EQN-DCPINN-REPRO-001 — derivative-constrained PINN reproduction

**Opened:** 2026-10-30  
**Primary owner:** Lane A — PDE/equation evaluation  
**Evidence owner:** Lane F  
**Publication owner:** Lane H  
**Status:** PEER-REVIEWED METHOD IDENTIFIED / SOURCE AND DATA AUDIT NOT DONE / MODEL_ONLY  
**Source:** https://doi.org/10.1103/5bbf-p6zk  
**Related:** INV-034/035, FND-006, EQN-003, EQN-004, EQN-006; lanes A, C, E, F, H

## Current evidence

The official APS publisher page for Hoshisashi, Phelan, and Barucca, *Physical Review E* 113, 055301 (published 2026-05-04), describes derivative-constrained PINNs (DC-PINNs) for PDE problems. It reports explicit nonlinear derivative constraints (including bounds, monotonicity, convexity, and incompressibility), automatic differentiation, self-adaptive loss balancing, and selected numerical benchmarks. The paper is not indexed elsewhere in the repository as of 2026-10-30.

Only the publisher page and abstract were reviewed. The cited source-code location, data, license, dependencies, and reported results have not been independently audited or reproduced. This is a method lead, not evidence of a new governing law or engineering advantage.

## Unlock criteria

1. Pin the exact source revision, license, dependencies, benchmark data, and dataset/split hashes.
2. Reproduce one heat-diffusion-with-bounds case using the stated baselines and equal resource budgets.
3. Freeze held-out spatial/temporal regimes and include a counterexample where PDE residual is small but a derivative constraint is violated.
4. Report PDE residual and each constraint separately, plus boundary error, held-out error, uncertainty, failures, memory, runtime, and energy where measurable.
5. Compare total training/search/inference cost and require independent review before any domain transfer to biomass, cooling, materials, or fusion models.

## Nonclaims

No UQPU reproduction, new physical law, quantum advantage, device result, accepted Pangola fuel, net fusion electricity, lower WACC, or Data-Center-to-One-Phone progress is demonstrated by the external paper alone.
