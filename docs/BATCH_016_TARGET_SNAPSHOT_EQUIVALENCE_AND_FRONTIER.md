# Eight-Lane Batch 016 — Target Snapshot, Subsystem Equivalence and Open-Frontier Search

Date: 2026-09-10

## Executive result

Batch 016 advances three independent gates without making a quantum-advantage claim:

1. **Lane A/B/F — target-aware snapshot simulation:** the existing 3-qubit QAOA correctness fixture was transpiled against IBM Runtime `FakeKingston` and simulated with `AerSimulator.from_backend`, which constructs an approximate device noise model from the saved backend snapshot.
2. **Lane C/F — subsystem equivalence contracts:** compute and state/memory/storage functions now have executable service-level contracts, preventing capacity-only or qubit-count-only replacement claims.
3. **INV-027 / A–H — open-frontier opportunity map:** the repository now separates established algorithmic routes, architecture/material routes, hard information-theoretic constraints and speculative/fundamental-physics hypotheses.

## Target-snapshot experiment

GitHub Actions run: `34436202336`  
Job: `target-snapshot-noise`  
Environment: Python 3.12.14, Qiskit 2.5.2, Qiskit Aer 0.17.1, Qiskit IBM Runtime 0.48.0.

Target model: `FakeKingston` (`fake_kingston`), a 156-qubit IBM fake backend stored in Qiskit IBM Runtime. IBM documents fake backends as system snapshots containing coupling maps, basis gates and qubit/system properties useful for transpilation and noisy simulation. Qiskit Aer documents `AerSimulator.from_backend()` as an approximate backend-derived noise simulation route.

### Measured bounded result

| Metric | Result |
|---|---:|
| Logical qubits | 3 |
| Logical depth | 12 |
| Routed depth | 36 |
| Logical CX count | 6 |
| Routed CZ count | 9 |
| Routed SX count | 21 |
| Routed RZ count | 19 |
| Shots | 4096 |
| Ideal optimum probability | 0.9942078994 |
| Snapshot-noisy optimum hits | 4018 |
| Snapshot-noisy optimum probability | 0.98095703125 |
| Transpile runtime on CI host | ~0.0266 s |
| Aer simulation runtime on CI host | ~1.961 s |

Snapshot summary recorded by the job included a median CZ error of about `0.00183159` and a median measurement error of about `0.00952148` across snapshot entries. The snapshot also contains extreme outliers, so global maxima are not treated as typical active-qubit performance.

### Evidence interpretation

This is **CALIBRATION_SNAPSHOT_SIMULATION**, not `REAL_QPU` evidence. `FakeKingston` is a saved system snapshot, not a statement of live calibration at execution time. Aer noise is approximate. No queue time, provider billing, drift, QEC, mitigation, network cost or real hardware energy was measured.

Therefore this batch does **not** demonstrate quantum advantage, GPU/CPU replacement, memory/storage replacement, >=100x economics, or the 100M-unit moonshot.

## Subsystem-equivalence advance

New executable contracts distinguish compute from state-service replacement:

- compute: minimum accepted tasks/second, maximum latency and minimum output quality;
- state/memory/storage: capacity, read/write bandwidth, read/write latency, retention, random-access semantics, persistence and recovery probability.

This explicitly rejects the invalid shortcut `large Hilbert space = equivalent RAM/VRAM/HDD capacity`. A candidate with sufficient nominal capacity but inadequate access, persistence, retention or recovery fails the contract.

## Open-frontier research result

`docs/OPEN_FRONTIER_OPPORTUNITY_MAP.md` now ranks routes by scientific status.

Highest-value established routes include structured quantum algorithms with strong asymptotic advantage, quantum simulation, amplitude estimation, search/walks, and compressed-output linear algebra. The same map records early-kill constraints: classical input loading, full-output materialization, QEC/shot overhead, weak baseline comparisons and inaccessible quantum-state information.

The fundamental-physics frontier remains open under INV-027, but any proposed new mechanism must supply a causal information-processing primitive, scaling law, compatibility with known physical constraints and a falsifiable experiment or bound. Speculative mathematical models such as free postselection remain separated from engineering claims.

## References

- IBM Quantum fake-provider documentation: https://quantum.cloud.ibm.com/docs/en/api/qiskit-ibm-runtime/fake-provider
- IBM Quantum noise-model guide: https://quantum.cloud.ibm.com/docs/en/guides/build-noise-models
- Qiskit Aer `AerSimulator`: https://qiskit.github.io/qiskit-aer/stubs/qiskit_aer.AerSimulator.html
- P. W. Shor, FOCS 1994, DOI 10.1109/SFCS.1994.365700
- L. K. Grover, arXiv:quant-ph/9605043
- Bennett, Bernstein, Brassard, Vazirani, DOI 10.1137/S0097539796300933
- Harrow, Hassidim, Lloyd, DOI 10.1103/PhysRevLett.103.150502
- Wootters, Zurek, DOI 10.1038/299802a0
- S. Aaronson, DOI 10.1098/rspa.2005.1546

## Next highest-value gates

1. freeze the exact physical layout/active qubits used by the snapshot transpilation and record only their calibration properties rather than global medians;
2. repeat target-snapshot simulation for ER6/ER8 only when simulation cost remains bounded;
3. compare target-aware noisy quality to the exact useful-output contract and calculate required shots per accepted solution;
4. add a competitive GPU/CPU baseline for the same accepted-output contract;
5. obtain an authorized bounded real-QPU job and actual billed-cost evidence;
6. apply the new compute/state equivalence contracts to the INV-025/026 100M-unit evidence gate.
