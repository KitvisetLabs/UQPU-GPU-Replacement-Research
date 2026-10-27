# EQN-PCSR-TURB-001 — physics-constrained symbolic regression reproduction gate

**Primary owner:** Lane A — workloads/software/equation-discovery interface  
**Cross-lane reviewers:** Lane E (thermal-fluid/cooling relevance), Lane F (evidence/economics), Lane H (publication)  
**Status:** OPEN / OFFICIAL_PREPRINT / REPRODUCTION_NOT_RUN  
**Opened:** 2026-10-28  
**Source:** Shan & Zhang, arXiv:2610.35276, https://arxiv.org/abs/2610.35276

## Question

Can the paper's staged physics-constrained symbolic-regression (PCSR) relations for incompressible smooth-wall zero-pressure-gradient turbulent-boundary-layer mean velocity and effective mixing length be independently reconstructed and generalize to genuinely held-out profiles while preserving declared asymptotic constraints?

**Competing explanation:** reported agreement may depend on fitted profiles, model-selection choices, prescribed high-Reynolds-number targets, correlated datasets or a narrow geometry/flow regime. Out-of-fit profiles in the preprint are not necessarily a statistically independent test set.

## Contract and equations

Pin the preprint version, code/data/license, preprocessing, profile IDs, wall units, operator set, symbolic-search budget/seeds, coefficient-fit procedure, selected expression and residuals. Variables (U^+), (y^+), (eta=y/\delta) and (Re_\tau) are dimensionless by the source definitions. Reconstruct the exact reported formulas before coding alternatives.

Required checks include:
- no-slip and linear near-wall (U^+\sim y^+);
- recovery of the logarithmic overlap baseline in its stated regime;
- wake correction that vanishes sufficiently rapidly as (eta\to0);
- declared high-(Re_\tau) limits, clearly marked as imposed priors when they are not independently inferred;
- positivity/domain checks for logarithms, fractional powers and square roots;
- residuals by profile, region and Reynolds number, not only pooled averages.

## Falsifiable protocol

1. Freeze hashes, preprocessing, train/fit IDs and symbolic-search settings.
2. Independently reconstruct the source equations and in-fit results; retain unsuccessful seeds and counterexamples.
3. Use profiles/conditions excluded from expression and coefficient selection as a sealed holdout. If no independent data are available, mark validation BLOCKED rather than calling out-of-fit points independent.
4. Compare with classical log-law/Coles-wake and van-Driest baselines using identical profiles, metrics, evaluation points and uncertainty treatment.
5. Stress low-Re, near-wall, outer-layer and measurement-sensitive regions; test whether asymptotic behavior survives parameter changes.
6. Record search CPU/GPU time, memory, model complexity and energy where measurable. A shorter equation is not automatically cheaper to evaluate or more accurate.

**Fail criteria:** source artifacts cannot be pinned; the exact formula cannot be reproduced; constraints are violated; performance disappears on independent holdout; model selection leaks test profiles; or a domain-specific fit is described as a new universal physical law.

## Integration boundary

This preprint may inform the equation-discovery method and, later, domain-matched fluid/cooling model tests. It does not directly validate data-centre cooling, fusion blanket/divertor, plasma, biomass conversion or any UQPU mission advantage. Current physical laws remain binding for engineering claims.
