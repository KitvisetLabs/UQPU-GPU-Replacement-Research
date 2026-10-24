# INT-20261023-003 — RG-034 identifiability interface

**Primary implementation owner:** Lane A  
**Evidence/integration owner:** Lane F  
**Method intake owner:** Lane H  
**Status:** proposed, MODEL_ONLY; review required before main synchronization

## Stable input contract

- design_id: unique, stable identifier for one declared observation protocol.
- dimensionless_sensitivity_matrix: finite rectangular Jacobian after documented observation and parameter scaling.
- normalization_provenance: nonempty record of the scales and units used.
- solver_converged: explicit boolean; false forces NOT_YET_SOLVED.
- alternative_designs: versioned list of alternative protocols with the same parameter basis.
- experiment_class_complete: caller attestation that a finite declared class has been enumerated; this field is not independently proved by the helper.
- tolerance: explicit numerical rank tolerance in (0, 1).

## Stable output contract

- verdict: NOT_YET_SOLVED, IDENTIFIABLE, LOCALLY_NON_IDENTIFIABLE, or EXPERIMENT_CLASS_EXHAUSTED.
- primary rank and parameter_count;
- primary nullspace_basis;
- design_ranks for every declared design;
- convergence, class-completeness and tolerance provenance.

## Promotion rules

1. Do not call a candidate physically true because it is locally identifiable.
2. Do not call it globally identifiable from a single local Jacobian.
3. Never emit EXPERIMENT_CLASS_EXHAUSTED unless at least two unique declared designs are all rank deficient and the bounded class is explicitly marked complete.
4. A newly declared full-rank alternative falsifies the class-exhaustion verdict.
5. Before real-data use, compare analytic and finite-difference Jacobians, perturb the candidate parameter point and rank tolerance, and freeze train/selection/test splits.
6. For physical hypotheses, continue with dimensional/symmetry/conservation/causality checks, limiting cases, held-out prediction, counterexample search and independent validation.

## Lane links

A owns deterministic implementation and tests; B is not invoked; C receives no state-capacity inference; D/G remain downstream of measured device observables; E receives no material/fuel/fusion result; F owns provenance and evidence boundaries; H owns literature and scientific-method review.
