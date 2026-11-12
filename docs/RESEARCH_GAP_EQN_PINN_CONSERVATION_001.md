# Research gap — EQN-PINN-CONSERVATION-001: conservation-constrained equation discovery

**Opened:** 2026-10-26  
**Primary owner:** Lane A — equation/workload evaluation contract  
**Publication owner:** Lane H  
**Integration owners:** Lanes C, D, E, F and G  
**Evidence state:** LITERATURE_ONLY / REPRODUCTION_NOT_STARTED  
**Canonical base:** c9880f2bcca274ed36fe19f83b91e7c91e41b400

## Objective

Determine whether hard enforcement of conservation/admissibility constraints plus explicit model-discrepancy representation improves held-out equation-model acceptance over an unconstrained physics-informed baseline and a conventional numerical solver, under matched data and compute budgets.

## Evidence motivating the gap

- Chomalí-Castro et al., *Physical Review D* 114, 076013 (published 2026-10-07), DOI 10.1103/shpm-ksq9, report flux-conservative BDNK diffusion solved by Kurganov–Tadmor finite volumes and SA-PINN-ACTO. Their abstract reports agreement on smooth profiles and increased errors on discontinuous profiles. The accepted manuscript is not available from the publisher until 2027-10-07; this gap therefore does not claim exact reproduction.
- Zhang, *Physical Review Fluids* 11, 104602 (published 2026-10-06), DOI 10.1103/rn1j-32n4, reports boundary-data RANS reconstruction using exact advection/production terms, an explicit inadequacy term for unclosed terms and a realizability mechanism. This is a method paper in one fluid-model domain, not a general law-discovery result.

## Missing evidence

1. Source-pinned equations, units, boundary/initial conditions and data hashes for a reproducible case.
2. A conventional solver reference plus an unconstrained PINN control and a constraint-aware variant.
3. Separate smooth, discontinuous/sharp-gradient, parameter-shifted and held-out regimes.
4. Quantified conservation/flux residuals, admissibility violations, error and uncertainty, compute budget and negative controls.
5. Independent implementation and replay; actual wall-plug energy and lifecycle cost only if separately measured.

## Preregistered acceptance boundary

- Freeze the equation and dataset before training; do not choose the equation after observing the holdout.
- Use hard constraints only where their mathematical applicability is established; log every soft penalty, tolerance and auxiliary transform.
- Model discrepancy explicitly and test whether it absorbs a real signal or hides model misspecification.
- Compare all arms under the same accepted-output contract, data volume, training budget and hardware/software boundary.
- Keep solver error, physical model error, measurement error and numerical optimization error distinct.
- A lower residual is insufficient. Require held-out acceptance, counterexample search and independent validation.

## Stop / falsification rules

Stop promotion if the exact equation or data provenance is incomplete; conservation or admissibility checks fail; held-out performance degrades; discontinuity errors dominate; compute budgets are unmatched; or independent replay fails. A failed PINN result is not a falsification of the established governing equation. Do not infer physical joules, quantum advantage, material performance or economics from a model fit.

## Mission disposition

- **INV-029:** no physical-compression result; external support and all memory/I/O costs remain in the system boundary.
- **INV-030 / INV-031:** no carbon substitution or accepted liquid-fuel result.
- **INV-032:** no net fusion-electricity result.
- **INV-033:** no financing, principal, interest or WACC result.
- **INV-034:** contributes a falsifiable mathematics-first numerical-method test.
- **INV-035:** keeps generated/reformulated equations subordinate to dimensional, conservation, held-out, counterexample and independent-validation gates.
