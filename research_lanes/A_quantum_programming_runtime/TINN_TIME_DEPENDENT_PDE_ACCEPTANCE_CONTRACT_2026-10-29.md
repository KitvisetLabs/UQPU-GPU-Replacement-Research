# Lane A contract — time-dependent PDE surrogate acceptance (TINNs)

**Date:** 2026-10-29  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** C, D, E, F, G, H; INV-034/035  
**Status:** PREREGISTERED DESIGN / MODEL_ONLY UNTIL EXECUTED  
**Source:** https://proceedings.mlr.press/v306/dai26a.html  
**Focused gap:** ../../docs/RESEARCH_GAP_TINN_TIME_DEPENDENT_PDE_GENERALIZATION_2026-10-29.md

## Purpose

Evaluate time-conditioned neural networks for time-dependent PDE prediction without mistaking a surrogate fit for a changed physical law or an accepted system result. This contract is reusable for future thermal-fluid, material/process and cooling models only when an appropriate dataset and validated reference exist.

## Frozen comparison arms

1. Conventional space-time PINN with shared weights across time.
2. TINN with time-conditioned weights and the source's stated nonlinear least-squares/Levenberg–Marquardt procedure, if its implementation can be pinned and legally reused.
3. A neural-operator-splitting comparator, only if a compatible pinned implementation/data path is available.
4. A trusted numerical solver/reference with documented discretization, convergence and tolerances.

Do not silently substitute a different architecture, solver, optimizer, or compute budget after seeing held-out results.

## Preregistration and split integrity

Record immutable source revision, license/access state, environment/dependency hashes, dataset/provenance hash, preprocessing hash, PDE/units schema, solver/reference revision, initial/boundary conditions, geometry, coefficient and forcing ranges, seeds, optimizer-evaluation budget, stopping rule and acceptance-rule hash.

Split by complete trajectory or physical regime. Keep all points from a trajectory and all near-duplicate states in the same partition. Hold out at least one regime axis (for example coefficient range, initial/boundary condition, forcing or geometry); publish split manifests and check overlap before fitting. If no independent reference exists, label the case DATA_BLOCKED rather than manufacturing ground truth.

## Required outputs

- Median and worst-case held-out relative L2 error, with exact aggregation rule.
- PDE residual and dimensional/unit checks.
- Conservation drift and declared lower/upper-bound or positivity violation counts/rates/maxima.
- Solver-reference convergence and sensitivity to discretization/tolerance.
- Seed-level results, failures, timeouts and all attempted variants.
- Training/search and inference wall time separately; optimizer evaluations; peak host/device memory; checkpoint size; data/transfer bytes; energy only when instrumented; estimated cost only with disclosed assumptions.
- Cost per independently accepted result and uncertainty interval, including failed attempts and model-selection overhead.

Reuse software/uqpu-prototype/uqpu/pde_surrogate_metrics.py for declared discrete conservation/bound metrics when its interface matches the dataset. Reuse the existing grouped-holdout and matched-error contracts rather than creating a second generic metric system.

## Acceptance / rejection

Accept only if (a) the held-out split and provenance checks pass, (b) the predeclared physical tolerances pass, and (c) a predeclared quality or cost objective improves over the matched baseline without worst-case regression beyond the predeclared tolerance. Report effect sizes and uncertainty; do not choose a winning seed after the fact. If metrics conflict, report the conflict and keep the candidate OPEN.

Reject or mark INCONCLUSIVE if split leakage, missing reference convergence, unreported tuning, incompatible resource budgets, non-finite results, physical-constraint violations or unreproducible dependencies occur.

## Evidence boundary

Passing this contract is model/software evidence only. It does not establish a new physical law, validated reactor/device behavior, critical-material substitution, accepted bio-oil, net fusion electricity, QPU advantage, lower WACC or Data-Center-to-One-Phone physical compression.
