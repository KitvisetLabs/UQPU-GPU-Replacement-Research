# RG-044 — Task-resolved Fisher information versus finite-shot feature compression

**Status:** `LITERATURE_ONLY / PREREGISTRATION_REQUIRED / MODEL_ONLY`  
**Date:** 2026-10-24  
**Primary owner:** Lane C — state, memory, storage and data movement  
**Cross-lane owners:** Lane A (workload/runtime), Lane F (benchmark economics), Lane H (literature provenance)  
**Source:** Yang Peng, arXiv:2609.29570, submitted 2026-08-26  
**Related:** INV-025–027, INV-029, INV-034–035, FND-001–003, FND-006, EQN-001–006

## Objective

Test whether task-resolved Fisher diagnostics can predict the minimum measurement/feature representation needed to achieve an identical accepted prediction task, and whether any feature compression survives finite-shot, reconstruction, host-compute and end-to-end cost accounting.

## External evidence

The preprint proposes a hierarchy connecting task-score-basis QFI, Fisher information in the complete measurement record, and moment matrices retained through feature order (r). It numerically studies a five-spin open reservoir and reports that low-order compression can demand substantially more samples for higher-order temporal targets.

Evidence remains `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`. No UQPU reproduction, hardware execution, energy measurement, provider price, or end-to-end economics is available. The paper does not establish a universal result for all tasks or devices.

## Hypothesis and competing explanations

**Hypothesis:** for a frozen task and stationary operating distribution, the information retained by measured feature order (r), combined with finite-shot uncertainty, can predict the resource budget required to meet a preregistered held-out quality threshold.

**Competing explanations:** the observed trade-off is target-specific; the feature-order metric is not predictive under correlated or shifted inputs; finite-shot estimates are too noisy; data reconstruction and classical readout dominate; or a classical reservoir reaches the same quality with less total resource.

## Required experiment contract

- Freeze task ID, model/version, target-score basis, washout, data-generation protocol, precision, forecast horizon, quality metric/threshold and seed schedule.
- Store independent SHA-256 digests for train, validation and blind held-out splits; held-out histories must not influence feature-order selection, stopping or repair.
- First reproduce the source's five-spin numerical example from pinned source artifacts and licensing. No reproduction has yet been performed.
- Compare complete measured bit-string records with feature-order truncations (r=1,2,ldots) under at least two finite-shot budgets on identical histories.
- Compare exact/analytic matrices separately from estimated matrices. The analytic hierarchy must be checked in a common score basis; estimated violations are warnings requiring uncertainty analysis, not automatic evidence of a new law.
- Include a tuned classical reservoir and a simple non-reservoir baseline under matched total evaluation and data budgets.
- Record QFI, complete-record and retained-feature Fisher matrices; matrix uncertainty; shots/history; measurement settings; raw record and feature bytes; host compute; reconstruction; latency/throughput; accepted prediction windows; energy when measured; total run cost; and cost per accepted window.
- Keep provider/target identity and pricing in a single record. No cross-target mixing of probabilities and prices. No paid QPU jobs without credentials, bounded budget and explicit user consent.

## Acceptance and falsification

Accept only if independent replay matches the preregistered numerical tolerance, the same held-out quality predicate is met, uncertainty is reported, and total resources are measured or explicitly unknown. A smaller feature vector alone is not an accepted win.

Retain a negative result if feature order fails to predict held-out quality, the apparent hierarchy depends on leakage or score-basis mismatch, finite-shot overhead dominates, a tuned classical baseline is cheaper at the same quality, or the source cannot be reproduced. Do not change thresholds after observing held-out outcomes.

## Software interface

`software/uqpu-prototype/uqpu/task_resolved_fisher.py` provides a schema/consistency gate for one workload, one model, one immutable task-score basis, one split digest and one provider/target context. It validates matrix dimensions/symmetry/positive semidefiniteness, optionally enforces the analytic information hierarchy, reports estimated-hierarchy warnings, and leaves unknown energy/cost as `None`. The unit tests are schema tests, not scientific reproduction.

## Cross-lane impact

- **A:** workload/output acceptance and model-selection freeze.
- **B:** provider-neutral interface; no calls made.
- **C:** primary ownership of record/feature bytes, feature order, shots and reconstruction.
- **D/G:** no device or manufacturing change until target-specific behavior is independently established; preserve D/G co-design.
- **E:** no BIO-001/FUS-001 or material claim; only future resource-accounting inputs.
- **F:** matched baseline, quality uncertainty and total cost per accepted task.
- **H:** source provenance and publication.
- **I:** no demonstrated relation to the specialist vehicle-lift lane.

## Mission and evidence boundary

This gap does not establish quantum advantage, GPU/NPU/CPU replacement, readable classical memory from Hilbert-space dimension, Data-Center-to-Phone feasibility, Pangola-material substitution, commercial bio-oil, commercial fusion electricity, lower project WACC, or a new physical law. INV-029 through INV-035 and the root 00–06 directives remain binding. The multilingual Thai/English/Chinese/Japanese/Korean/German strategic links remain preserved.
