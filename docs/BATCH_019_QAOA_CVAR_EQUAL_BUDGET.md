# Batch 019 — Equal-Budget QAOA Objective Selection

**Date:** 2026-09-10  
**Primary owner:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Integration:** A–H  
**Evidence:** SIMULATION  
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

## What this does and does not establish

This is a positive **algorithm/objective-selection signal** for this one six-qubit ideal fixture. It is not yet a workload speedup or economic win. The search uses exact statevector probabilities; a hardware CVaR optimizer would itself require finite shots. No competitive CPU/GPU/NPU runtime baseline, QPU execution, provider billing, queue time, mitigation/QEC, energy or network cost is measured here.

Therefore no >=100×, >=100,000,000×, subsystem-replacement, or Data-Center-to-Phone claim follows from this result.

## Immediate falsification gate

A target-aware comparison is now being added using the same ER6 contract and the same mean-vs-CVaR selected circuits. Both circuits must be transpiled against the same saved IBM FakeKingston target snapshot and receive the same total simulator-shot budget and deterministic seed set.

The key test is whether the ideal +21.64% optimum-probability gain survives target routing and the saved calibration-derived noise model. If it disappears or reverses, the negative result must be retained.

## Eight-lane integration

| Lane | Batch 019 contribution | Next gate |
|---|---|---|
| A | Added CVaR objective selection under equal 576-evaluation p=1 search budget | noisy target comparison; then hardware-feasible optimizer |
| B | Same provider-neutral QAOA contract remains lowerable to cloud gate-model paths | authorized provider-matched real-QPU run |
| C | Higher useful-answer probability may reduce shot/readout/output traffic per accepted answer | measure target-aware shot and I/O reduction |
| D | Physical routing/noise may erase software-level probability gain | quantify mapped circuit depth/error sensitivity |
| E | Pangola/biomass-carbon INV-030 remains active; no new material-performance claim is made in this algorithm batch | measured functional-unit materials experiments |
| F | Equal evaluation budget and stable contract ID prevent moving-target comparisons | connect probability gain to accepted-solution cost only after provider matching |
| G | Target calibration/routing requirements inform control/metrology/manufacturing constraints | map sensitivity to device/process requirements |
| H | Capital stage gate remains: improve software evidence before paid scale-up | bounded real-QPU budget only after target-aware evidence |

## North-Star interpretation

The Data-Center-to-One-Phone mission requires reductions in **work required per accepted useful result**, not merely smaller hardware. Objective shaping is relevant because a higher accepted-output probability can reduce repetitions, data movement, control work and cost. Batch 019 is only a microscopic six-qubit test of that principle.

**Status:** POSITIVE SIMULATION RESULT / TARGET-SNAPSHOT VALIDATION PENDING.
