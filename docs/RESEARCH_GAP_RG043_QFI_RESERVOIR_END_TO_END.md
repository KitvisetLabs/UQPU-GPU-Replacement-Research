# RG-043 — QFI-aware reservoir optimization under an end-to-end accepted-task contract

**Status:** `LITERATURE_ONLY / REPRODUCTION_NOT_RUN / MODEL_ONLY`  
**Date:** 2026-10-24  
**Primary owner:** Lane A — quantum programming / workloads / compiler / runtime  
**Cross-lane owners:** Lane H (literature provenance), Lane F (benchmark and economics)  
**Related:** INV-025–027, INV-029, INV-034–035, FND-001–004, FND-006, EQN-001–006

## Objective

Determine whether QFI-aware physical-parameter optimization improves a quantum-reservoir predictor over the strongest search-only and classical baselines after matching the complete training, inference and measurement budget—not merely readout size—and whether any quality improvement survives conversion into accepted-task cost.

## External signal

Nguyen and Soh, “Quantum-Fisher-information-aware optimization yields a quantum reservoir advantage over tuned classical reservoirs,” arXiv:2610.14454 (10 October 2026), reports lower held-out error on five-step Mackey–Glass forecasting for a small driven Jaynes–Cummings reservoir, including gains attributed to a QFI-aware optimization stage. The paper identifies code/configuration/seed artifacts at DOI 10.5281/zenodo.23272046.

Evidence class: `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`. The reported result has not been independently reproduced by UQPU and is not a hardware, energy, total-cost or physical-law result.

## Current blockers

- The Zenodo payload has not yet been downloaded, hashed, license-checked or reproduced by UQPU.
- No UQPU workload contract or held-out data manifest is frozen for this experiment.
- No QFI-estimation shot/control overhead or total training-resource ledger exists.
- No equal-end-to-end-budget comparison against the strongest tuned classical baseline exists.
- No hardware/provider execution or energy measurement is authorized or performed.

## Unlock criteria

1. Pin source artifacts, environment, data-generation rules, split hashes, seeds and numerical conventions.
2. Reproduce the published numerical result within a preregistered tolerance; preserve any failed figure/table.
3. Freeze train/validation/held-out separation, forecast horizon, normalization, precision, quality threshold, and accepted prediction-window definition.
4. Compare QFI-aware optimization, the source paper's simple optimizer, continued search with the same added evaluation budget, and a tuned classical reservoir. Add a second classical temporal/neural baseline if its budget can be frozen.
5. Keep all held-out data blind until model selection and stopping are frozen; include shuffled/no-signal, no-QFI, multiple-seed, shifted-window and equivalent-parameter-scaling controls.
6. Report quality and economics separately: NRMSE and uncertainty; accepted predictions/s; training/inference latency; parameter and trajectory evaluations; QFI-estimation method/shots; preparation/measurement/readout; retries/reconstruction; host compute; memory/data movement; calibration; energy where measured; and total cost per accepted prediction window.
7. Require independent replay. A simulation-only result remains `SIMULATION`; a schema or preregistration pass remains `MODEL_ONLY`. No method result establishes a physical law.
8. Do not schedule a paid QPU job without credentials, bounded budget and explicit user consent.

## Failure outcomes to preserve

- QFI-aware improvement vanishes under equal total training budget.
- Improvement is limited to one seed, one time window or the source's chosen task.
- A gain in NRMSE costs more in state preparation, measurement, optimizer evaluations, host compute or wall time.
- Classical tuning catches up under the same budget.
- The public reproduction deposit is incomplete, unlicensed for the intended reuse, or fails to reproduce the reported result.

Each outcome is a useful negative result; none permits relaxing the preregistered acceptance rule after seeing held-out data.

## Mission boundary

This gap is a candidate workload-method study only. It does not demonstrate quantum advantage, 100x/100,000,000x cost reduction, GPU/NPU replacement, Data-Center-to-Phone feasibility, RAM/VRAM/storage equivalence, Pangola material substitution, commercial bio-oil, commercial fusion electricity, reduced project WACC or new physical law.
