# Lane A contract — conservative and bounded PDE-surrogate metrics

**Contract ID:** A-PDE-SURROGATE-METRICS-001  
**Primary owner:** Lane A — workload/model acceptance contracts  
**Evidence owner:** Lane F — benchmarks, reproducibility and economics  
**Publication owner:** Lane H — source/literature provenance  
**Consumers:** Lane C (state/data movement), D/G (device/process), E (materials/energy/cooling)  
**Evidence class:** SOFTWARE_CONTRACT + SYNTHETIC_UNIT_FIXTURES  
**Status:** IMPLEMENTED METRIC / SCIENTIFIC BENCHMARK NOT RUN  
**Related gap:** RG-PDE-SURROGATE-001 in docs/BATCH_102_CONSERVATION_AND_TEMPORAL_PDE_EVALUATION.md

## Purpose

Prevent a low mean prediction error from hiding drift in a quantity that the selected PDE is supposed to conserve, or predictions outside a physically justified admissible range. This contract complements (but does not replace) the existing split-disjointness, source-provenance and matched-resource contracts.

## Interface

Implementation: software/uqpu-prototype/uqpu/pde_surrogate_metrics.py  
Tests: software/uqpu-prototype/tests/test_pde_surrogate_metrics.py

The public function is score_conservative_bounded_trajectory. Inputs are:

- initial_field: finite numeric values for the reference field at the initial time;
- predicted_fields: nonempty finite fields at successive prediction times, each matching the initial field length;
- cell_weights: optional positive spatial cell measures; unit weights are used only when explicitly omitted;
- lower_bound / upper_bound: optional physical bounds, supplied only when justified for the actual model;
- conservation_scale: a positive scale with the same units as the discrete conserved total; if omitted, it is derived only from the initial weighted field;
- normalized_conservation_tolerance: a dimensionless acceptance threshold;
- bound_tolerance: a tolerance in field-value units.

Outputs report the initial and predicted weighted totals, absolute and normalized drift, drift pass/fail, bound violation count/rate/maximum, and whether bounds were applicable. A zero-magnitude initial field requires an explicit positive conservation scale. If no bounds are supplied, bounds_pass is None, not True.

## Mandatory use conditions

1. The caller must name the PDE, conserved quantity, units, boundary conditions, discretization, cell weights, valid domain and reason that conservation/bounds apply. The helper cannot infer these from numbers.
2. A metric pass means only that the supplied discrete trajectory meets the caller-declared tolerance. It does not prove the PDE is solved, the reference model is correct, or nature obeys the assumed model.
3. The metric is not a PDE residual, boundary/initial-condition error, calibration test, equation-discovery score, material property, QPU benchmark or cost model.
4. Pair it with held-out relative error against an independent reference, PDE residual, initial/boundary errors, temporal and parameter/geometry holdouts, stability checks, uncertainty/interval scores where applicable, and full compute/resource accounting.
5. Keep the evaluation task class distinct from symbolic equation discovery. Do not pool solver scores with EQN-008 method rankings or claim a discovered physical law.
6. Preserve all failed seeds, counterexamples and out-of-range predictions. A single average metric cannot erase catastrophic failures.

## Acceptance sequence

- **Gate 0 — synthetic known solution:** hand-check cell weights, conserved totals, bounds and normalized tolerance.
- **Gate 1 — reference solver:** pin source/data/license, PDE and initial/boundary conditions; compare to a trusted numerical or analytic reference.
- **Gate 2 — blind holdout:** freeze time-block and parameter/geometry splits before tuning; prohibit test leakage.
- **Gate 3 — matched methods:** use the same task, data, preprocessing, seed set, hardware class and hard resource envelope. Keep separate task strata if methods solve different problems.
- **Gate 4 — useful output/economics:** include wall time, CPU/accelerator time, peak memory, field bytes, retries, failures, energy if measurable and total cost per accepted output.
- **Gate 5 — independent reproduction:** no method advantage or physical-law claim until source artifacts and results are independently checked.

## Non-claims

This contract does not implement FluxNet, TINNs or Heavy-tailed PINNs. The external papers remain LITERATURE_ONLY; the current helper has only synthetic unit fixtures. It does not change current physical equations or establish any benefit for Pangola materials, bio-oil, fusion, finance or Data-Center-to-One-Phone.
