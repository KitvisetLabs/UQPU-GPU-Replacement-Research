# INT-20261024-001 — QFI-aware reservoir optimization follow-up

**Status:** PROPOSED / LITERATURE_ONLY  
**Primary artifact owner:** Lane A  
**Integration/evidence owner:** Lane F  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Lane-A source commit:** `9cbf85596dce7699b8bea9f997c1d2ddec37503f`  
**Primary artifact blob SHA:** `9ac7d078da95044dbce49f9005c2eb49a4fdc979`  
**Source:** Nguyen & Soh, arXiv:2610.14454v1 (2026-10-10), read 2026-10-24  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`

## Causal hypothesis

For a small parameterized quantum reservoir with a retrained linear readout, a QFI-aware natural-gradient stage may locate useful parameter updates that equal-budget scalar-loss search misses. The hypothesized mechanism is improved use of pre-measurement state distinguishability; it is not assumed to imply quantum advantage, lower energy, or lower lifecycle cost.

## Required comparison contract

- **Accepted useful output:** a forecast on a frozen held-out time-series window meeting a preregistered NRMSE threshold.
- **Matched data:** identical training windows, held-out windows, seeds and selection rules for all methods.
- **Matched optimization budget:** equal objective/gradient evaluations and reported host compute; separately report costs intrinsic to QFI estimation and finite-shot measurement.
- **Baselines:** grid+Bayesian search, equal-budget continuation of black-box search, classical-parameter gradients with quantum parameters frozen, and a stronger parameter-trained classical reservoir.
- **Required outputs:** held-out error and uncertainty; QFI/gradient-bound residual; QFI conditioning/regularization; evaluation counts; wall time; host memory; measurement shots; state preparation; noise sensitivity; energy when measurable; total cost per accepted forecast.
- **Falsifier:** the proposed useful optimization effect fails if the derived bound is not numerically reproduced, the gain vanishes under stronger matched controls or held-out distribution shift, or full accepted-task cost is not improved.

## Cross-lane edges

| From | To | Candidate interface | Current evidence / status |
|---|---|---|---|
| A | F | Forecast acceptance + full-cost benchmark contract | PROPOSED; literature-only |
| A | D | Parameterized reservoir design variables and controllable observables | PROPOSED; no device evidence |
| A | C | Feature, state, I/O and reconstruction accounting | PROPOSED; no memory-replacement claim |
| FND-006 / INV-035 | A/F | Derivation and falsification gate for optimization relations | Method input only; no physical-law promotion |
| A/F | B | Later provider-neutral target protocol | BLOCKED until offline reproduction and authorization gates pass |
| D/G | H | Manufacturing/finance impact only after device requirement and cost data exist | BLOCKED; no present consequence |

## Lane disposition A–H

- **A:** offline QFI-RESERVOIR-001 proposed; no implementation result yet.
- **B:** no provider call, credentials, snapshot or QPU job.
- **C:** QFI and feature count are not readable classical memory capacity.
- **D:** no physical device, process or packaging evidence.
- **E:** no Pangola, biomass, bio-oil, fusion or cooling evidence.
- **F:** full-cost and matched-output contract required before economic promotion.
- **G:** no factory/equipment consequence until a device-level requirement is established.
- **H:** preserve the dated source watch and route the result into the strategic ledger only after evidence gates.

## Invariant boundary

- **INV-029:** no phone-class physical-compression or data-center-equivalence evidence.
- **INV-030/031/032:** no materials, fuel or fusion evidence.
- **INV-033:** no principal, interest, financing-rate or WACC evidence.
- **INV-034:** no new physical limit; small-system mathematics remains a proposed reproduction task.
- **INV-035:** candidate relations remain hypotheses until dimensional/structural checks, counterexamples, held-out tests, independent reproduction and appropriate physical validation pass.
- **INV-025/026/027:** universal and 100,000,000-unit targets remain unproven.

## Next action

Implement the offline exact/simulation fixture and matched-budget controls only after pinning the paper version and test data. Keep the current Lane-A provider route/native-conformance gate separate. No paid execution or purchase is authorized by this artifact.
