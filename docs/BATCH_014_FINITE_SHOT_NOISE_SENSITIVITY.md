# Batch 014 — Finite-shot and Synthetic Readout Sensitivity

Date: 2026-09-10. Priority #1: quantum programming.

## Why this batch exists
Batch 013 independently verified the portable QAOA circuit with Qiskit and exposed routing overhead. The next software gate was to quantify how finite shots and a simple measurement-error channel change useful-output probability before spending on real QPU jobs.

This experiment applies an **independent symmetric classical bit-flip channel after ideal circuit measurement**. It is deliberately narrow. It is not a calibrated hardware noise model.

## CI verification
GitHub Actions run 34432243877 executed the experiment on the Python 3.12 test job. The full core suite reported **149 tests passed**. The Qiskit verification job also succeeded.

## Exact probability results
Using the same p=1, 24×24 parameter-grid fixtures from Batch 012:

| Fixture | Qubits | Exact optimum | Ideal optimum probability | At 1% readout flip | At 2% | At 5% |
|---|---:|---:|---:|---:|---:|---:|
| triangle | 3 | -2 | 0.994208 | 0.984537 | 0.975062 | 0.947808 |
| ER6 | 6 | -7 | 0.253917 | 0.242292 | 0.231271 | 0.201560 |
| ER8 | 8 | -8 | 0.129883 | 0.123490 | 0.117382 | 0.100666 |

These values are exact under the stated synthetic post-measurement channel. Finite-shot samples at 128/512/2048/8192 shots were also generated with deterministic pseudorandom seeds and show the expected sampling variation.

## Interpretation
The larger fixtures are much more sensitive in useful-output probability than the triangle even before realistic gate/routing noise is introduced. At a synthetic 5% independent readout-bit error, ER8's optimum probability falls from about 12.99% to 10.07%.

This does **not** predict a particular QPU. Real execution must include target-specific readout assignment matrices, one-/two-qubit errors, coherence, crosstalk, leakage, routing, calibration drift, queue/retry behavior and mitigation overhead.

## Next gate
1. freeze a selected target/circuit;
2. ingest an official/calibrated backend snapshot rather than inventing hardware parameters;
3. run target-aware noisy simulation/transpilation;
4. preserve output-quality and total-shot contracts;
5. only then submit a bounded authorized QPU job and record job ID, billed cost, runtime and accepted-output quality.

No quantum advantage, GPU replacement, RAM/VRAM/storage replacement, or >=100× cost reduction is demonstrated here.
