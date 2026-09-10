# Batch 019 — Equal-Budget QAOA Objective Selection

**Date:** 2026-09-10  
**Primary owner:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Integration:** A–H  
**Evidence:** SIMULATION + CALIBRATION_SNAPSHOT_SIMULATION  
**Real QPU:** No  
**Quantum advantage:** Not demonstrated

## Research question

For the existing ER6 MaxCut/QUBO contract `8efaa94bb3306d25`, can a different variational objective select a p=1 QAOA circuit with higher probability of returning the exact optimum without increasing the number of parameter-grid circuit evaluations?

The baseline selects `(gamma,beta)` by minimizing ordinary expected energy. The candidate selects from the **same 24×24 grid (576 circuit evaluations)** using lower-tail Conditional Value at Risk (CVaR). The exact optimum `-7` is used only for post-selection diagnosis; optimum probability is not used to choose the CVaR parameters.

## Reproducible ideal-statevector result

GitHub Actions run `34448205957`, Python 3.12.14, completed the new objective-selection experiment successfully.

| Selection | alpha | gamma | beta | ideal expected energy | ideal optimum probability | probability ratio vs mean |
|---|---:|---:|---:|---:|---:|---:|
| mean energy | — | 0.5235987756 | 1.3089969390 | -5.6802282764 | 0.2539173400 | 1.0000 |
| CVaR | 0.25 | 0.5235987756 | 1.3089969390 | -5.6802282764 | 0.2539173400 | 1.0000 |
| CVaR | 0.50 | 0.6544984695 | 2.7488935719 | -5.6055293424 | 0.3088642280 | 1.2163967533 |
| CVaR | 0.75 | 0.6544984695 | 2.7488935719 | -5.6055293424 | 0.3088642280 | 1.2163967533 |

Under this bounded ideal fixture, alpha=0.50 and alpha=0.75 select the same circuit and raise exact-optimum probability from about **25.39% to 30.89%**, a relative increase of about **21.64%**, while using the same shared 576-point parameter grid.

The result also shows why mean energy and useful-answer probability must not be conflated: the CVaR-selected circuit has a slightly worse ordinary expected energy but a higher probability on the exact optimum state.

## Equal-shot saved-target validation

The next falsification gate was executed in GitHub Actions run `34448884641`. Both selected circuits were transpiled to the same saved IBM `FakeKingston` target snapshot at optimization level 2 with transpiler seed 17. Each strategy then received exactly **8,192 simulator shots**: four deterministic simulator seeds × 2,048 shots.

| Selection | snapshot optimum hits | total shots | snapshot optimum probability | Wilson 95% interval* | expected shots / optimum | shots for >=99% at least one optimum | routed depth | routed 2Q gates |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| mean energy | 1,920 | 8,192 | 0.2343750000 | [0.2253241762, 0.2436597970] | 4.2666666667 | 18 | 76 | 26 CZ |
| CVaR alpha=0.50 | 2,255 | 8,192 | 0.2752685547 | [0.2657102647, 0.2850518703] | 3.6328159645 | 15 | 75 | 26 CZ |

The saved-target simulation therefore retained a positive signal:

- absolute optimum-probability increase: **0.0408935547** (~4.09 percentage points);
- relative optimum-probability ratio: **1.1744788861** (~17.45% higher);
- expected shots per optimum: **4.2667 -> 3.6328**, about **14.85% fewer** expected shots;
- integer shot threshold for >=99% chance of at least one optimum: **18 -> 15**, about **16.7% fewer** shots;
- routed two-qubit count remained **26 CZ** for both circuits and routed depth changed only 76 -> 75.

*The Wilson intervals quantify finite simulator sampling uncertainty only. They do **not** include uncertainty in the saved calibration snapshot or the noise-model approximation. Their non-overlap must not be interpreted as live-hardware statistical significance.

The ideal relative probability increase was ~21.64%; under this saved target snapshot it remained ~17.45%. Thus this particular target/noise model reduced but did not erase the CVaR-selected circuit's useful-answer-probability advantage.

## What this does and does not establish

This is a positive **algorithm/objective-selection signal** for one six-qubit fixture under both ideal exact simulation and a saved target-derived noise simulation. It is not yet a workload speedup or economic win. The parameter selection used exact statevector probabilities; a hardware CVaR optimizer would itself require finite-shot objective estimation. The saved `FakeKingston` model is not a current live backend calibration and Aer simulation is not exact hardware behavior.

No competitive CPU/GPU/NPU end-to-end runtime baseline, real QPU execution, provider billing, queue time, mitigation/QEC, energy or network cost is measured here. Therefore no >=100×, >=100,000,000×, subsystem-replacement, or Data-Center-to-Phone claim follows from this result.

## Immediate next gate

Freeze the ER6 contract and the two parameter sets above into a provider-neutral real-QPU comparison protocol. The real experiment must use the same provider/backend calibration window, identical shot budgets, identical acceptance rule, reproducible bit mapping, complete job/result provenance and measured provider billing/runtime. If paid execution is required, it must not be submitted without explicit budget authorization.

The key falsification question is now: **does the ~17.45% saved-snapshot probability gain survive a provider-matched real-QPU execution after including the optimization/measurement overhead needed to obtain the CVaR-selected parameters?**

## Eight-lane integration

| Lane | Batch 019 contribution | Next gate |
|---|---|---|
| A | CVaR selection raised accepted-answer probability under equal 576-evaluation p=1 search budget and retained the signal under saved-target simulation | finite-shot optimizer + real-QPU comparison |
| B | Same provider-neutral QAOA contract and parameter pairs are ready for bounded provider-matched execution | authorized real-QPU job |
| C | Saved-target result predicts fewer shots/readouts per accepted optimum in this fixture | measure actual I/O, retries and state/output traffic |
| D | Positive signal survived comparable routed complexity: 26 CZ for both and depth 76 vs 75 | live calibration/error sensitivity |
| E | Pangola/biomass-carbon INV-030 remains active; no new material-performance claim is made in this algorithm batch | measured functional-unit materials experiments |
| F | Equal evaluation/shot budgets and stable contract ID prevent moving-target comparisons | measured provider cost per accepted optimum and competitive classical baseline |
| G | Calibration/routing requirements inform control, metrology and device-manufacturing constraints | connect observed hardware errors to process/control requirements |
| H | Capital gate remains: stronger software/snapshot evidence precedes paid scale-up | bounded real-QPU budget after authorization |

## North-Star interpretation

The Data-Center-to-One-Phone mission requires reductions in **work required per accepted useful result**, not merely smaller hardware. Objective shaping is relevant because a higher accepted-output probability can reduce repetitions, readout/data movement, control work and potentially cost. Batch 019 demonstrates that principle only on a microscopic six-qubit simulated fixture; scaling must be measured rather than extrapolated.

**Status:** POSITIVE IDEAL + CALIBRATION_SNAPSHOT_SIMULATION / REAL_QPU VALIDATION PENDING.
