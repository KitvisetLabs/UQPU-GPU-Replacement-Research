# Batch 040 — AI-COST-003 VQC Reproduction and Hybrid Readout Repair

**Gate:** `AI-COST-003`  
**Classification:** `VQC_XOR_ACCEPTED_CAPABILITY_REACHED_BY_HYBRID_READOUT_REPAIR_NO_COST_ADVANTAGE`  
**Evidence level:** `IDEAL_STATEVECTOR_REPRODUCTION_PLUS_ANALYTIC_RESOURCE_LEDGER`  
**Primary lane:** Lane A — Quantum Programming / Workloads / Compiler / Runtime  
**Cross-lane dependencies:** Lane B (future provider/QPU execution), Lane C (data/memory traffic), Lane F (benchmark/economics/evidence)

## Research Attribution

- **Research Owner / Principal Investigator / Research Direction:** Kanutsanan Pongpanna
- **Facebook:** https://www.facebook.com/LoveMoneyTH
- **YouTube:** https://www.youtube.com/@LoveMoneyTHOfficial
- **AI Research Agent:** OpenAI GPT-5.6 Sol
- **AI-assisted contribution:** public VQC literature/code triage, reproduction-interface design, ideal-statevector implementation, exact-gradient audit, resource-ledger derivation, hybrid readout repair, tests/results and research documentation.

Attribution reflects roles in this batch only.

## Why this gate exists

Batch 039 froze a deterministic classical accepted-capability contract instead of allowing an isolated quantum-kernel comparison. The quantum/hybrid candidate must therefore use the same 256 training and 256 held-out examples and pass both:

- held-out accuracy `>= 0.98`;
- held-out BCE `< 0.19`.

The public comparator selected for maximum information gain is:

- Miras Seilkhan and Adilbek Taizhanov, *Comparing Classical and Quantum Variational Classifiers on the XOR Problem*, `arXiv:2602.24220v1`;
- public reproducibility repository `mseilkhan/XOR-research-Quantum-ML-vs-Classic`;
- repository pin used here: `d7dd995db6a19295235c48483fe1abb108d9022d`.

The paper reports that a depth-2 VQC can match XOR accuracy in representative settings, while the MLP is substantially faster and no clear efficiency advantage is observed. Its public code implements a two-qubit circuit with `RX(pi*x_i)` encoding, `6L` trainable parameters, each layer containing two `Rot` gates plus `CNOT(0->1)`, and `<Z0>` readout.

UQPU retains Batch 039's task semantics. Because the frozen data are in `[-1,1]^2`, they are affinely mapped to `[0,1]^2` before the public `RX(pi*x)` encoding. Batch 039 labels **same-sign quadrants** as class 1 (XNOR), whereas the paper Dataset-C convention labels XOR as class 1, so the probability convention is complemented without adding a trainable resource.

## Independent executable reproduction

`software/uqpu-prototype/uqpu/ai_training_vqc_reproduction.py` implements the two-qubit statevector directly in pure Python. It does not import PennyLane. The implementation propagates exact derivatives of every trainable `RZ/RY/RZ` rotation through the statevector, providing a second implementation route rather than simply calling the source repository.

Frozen public-route settings:

- qubits: `2`;
- depth: `2`;
- nominal trainable parameters: `12`;
- full-batch epochs: `250`;
- learning rate: `0.2`;
- initialization: the exact 12 values produced by the public NumPy seed-0 `N(0,0.1)` initialization, frozen as literals;
- readout: `<Z0>`;
- task data and quality thresholds: Batch 039 unchanged.

Result:

| Metric | train | held-out |
|---|---:|---:|
| accuracy | `0.96484375` | `0.95703125` |
| BCE | `0.3809695833065735` | `0.37888043300038676` |

Therefore the public architecture route **does not pass** the frozen Batch-039 accepted-capability contract in this reproduction.

This is a scoped negative result. It does not refute the paper, because the paper studies multiple XOR datasets/settings and reports representative results rather than this exact UQPU dataset/quality threshold.

## Interface finding: nominal 12 parameters are not all active under `<Z0>`

For the final depth-2 layer, parameters `[8, 9, 10, 11]` have exactly zero derivative for the `<Z0>` observable in this architecture:

1. the final `CNOT(0->1)` leaves `Z0` invariant;
2. every final-layer operation acting only on target wire 1 is therefore invisible to the final `Z0` expectation;
3. the final `RZ` on wire 0 commutes with the `Z0` readout.

Thus four of the nominal twelve parameters are structurally inactive at the output interface, not merely small-gradient parameters for one initialization. Executable tests verify the zero derivatives directly.

This is an interface/expressivity result, not a claim that the architecture can never solve every XOR dataset.

## UQPU readout repair

The highest-information minimal repair was to preserve the same feature encoding and variational layers but replace the single-wire readout with parity:

`m(x) = <Z0 Z1>`.

With this change the exactly inactive final-layer tail drops from four parameters to two (`[8,11]`), because the parity observable exposes target-wire information that `<Z0>` discarded.

After the same 250-epoch quantum-parameter training, before any classical calibration:

| Metric | train | held-out |
|---|---:|---:|
| accuracy | `1.0` | `0.9921875` |
| BCE | `0.3835357370819664` | `0.3774990388898494` |

The parity route therefore clears the accuracy gate but still fails the BCE gate: its decision boundary is good, but the raw expectation-to-probability mapping is under-confident.

A two-scalar classical readout calibration was then fitted on the frozen training expectations only:

`p(y=1|x) = sigmoid(a*m(x) + b)`

with:

- `a = 10.603102052547635`;
- `b = -0.08930314977146993`;
- 2 trainable classical scalars;
- 2,000 full-batch scalar calibration steps at learning rate `0.2`.

After calibration:

| Metric | train | held-out |
|---|---:|---:|
| accuracy | `0.9921875` | `0.984375` |
| BCE | `0.1320469933712274` | `0.12508869380594245` |

The repaired hybrid model therefore **passes both Batch-039 quality thresholds in ideal simulation**.

This result is deliberately narrow: it demonstrates that the frozen toy accepted-capability target can be reached after repairing the measurement/readout interface. It does **not** show that quantum computation makes the task faster or cheaper.

## Resource pressure — quality success is not economic success

For a straightforward hardware-style parameter-shift implementation with 12 parameters, one full training example/epoch requires one base circuit plus two shifted circuits per parameter:

`1 + 2*12 = 25 circuit evaluations`.

Across `256 * 250 = 64,000` training-example visits this gives:

- `1,600,000` training circuit evaluations;
- `22,400,000` single-qubit rotation applications using the decomposed gate count;
- `3,200,000` CNOT applications;
- `25,600,000` elementary gate applications under this logical counting convention;
- `204,800,000` shots if every circuit used 128 shots;
- `1,638,400,000` shots if every circuit used 1,024 shots.

These are **parameter-shift deployment equivalents**, not operations physically executed by this ideal simulator, not a fault-tolerant resource estimate, and not proof that parameter-shift is the optimal gradient method.

For intuition only, dividing the Batch-039 environment-specific median classical time `1.1564624219998905 s` by `1.6 million` serialized training circuits gives about `0.722789 microseconds/circuit` before counting state preparation, measurement, reset, classical control, queueing or calibration. At 128 serialized shots this corresponds to about `5.65 ns/shot`; at 1,024 shots about `0.706 ns/shot`. This is a **pressure envelope**, not a hardware impossibility theorem, because batching, parallelism, advanced gradients and hardware concurrency can change the accounting.

The main research result is therefore two-sided:

1. **quality barrier repaired:** the toy accepted-capability contract is reachable by a parity-readout + 2-scalar hybrid repair in ideal simulation;
2. **cost barrier remains open:** a naive shot-based training realization has a very large circuit/readout burden relative to the tiny classical baseline.

## Reproducible artifacts

- `software/uqpu-prototype/uqpu/ai_training_vqc_reproduction.py`
- `software/uqpu-prototype/tests/test_ai_training_vqc_reproduction.py`
- `software/uqpu-prototype/examples/run_ai_cost_vqc_reproduction.py`
- `benchmarks/results/batch040-ai-cost-003-vqc-reproduction.json`
- `benchmarks/external/xor-vqc-provenance-2026-09-13.json`

The unit test suite runs the full 250-epoch Z0 and ZZ routes and verifies the frozen metrics, structural zero-gradient indices and resource ledger.

## Next gates

### `AI-COST-003B` — independent SDK + finite-shot/noise cross-check

Reconstruct the parity-readout candidate in an independent SDK (Qiskit and/or PennyLane), verify the ideal expectation surface, then add finite-shot and target-derived noise. The quality claim must be downgraded immediately if `>=0.98` accuracy and `<0.19` BCE are not retained.

### `AI-COST-003C` — destroy the 1.6M-circuit training burden

Search for lower-evaluation methods under the same accepted-capability contract, including adjoint gradients where physically meaningful, simultaneous-perturbation methods, analytic structure exploitation, parameter tying, data re-uploading with fewer effective parameters, quantum-kernel alternatives, and new UQPU ansatz/readout designs. Every method must expose loading/readout and classical residual work.

### `AI-COST-004` — residual-cost destruction map

Map every remaining cost component: data/state preparation, shots, reset/readout, QEC/error mitigation, host optimization, memory, communication, control electronics, energy/cooling, hardware amortization, maintenance and lifecycle cost. The moonshot cannot advance on quantum-kernel quality alone.

## Evidence boundaries / non-claims

Batch 040 does **not** establish:

- real-QPU AI training;
- quantum advantage or a practical quantum speedup;
- cheaper training than the Batch-039 classical baseline;
- measured quantum energy or end-to-end TCO;
- GPU/NPU/RAM/DRAM/HBM replacement;
- `100,000,000x`, billion-fold or tens-of-billions-fold savings;
- US$10–100T-equivalent capability for tens of thousands of Thai baht;
- a fault-tolerant implementation;
- a new physical law.

Passing the toy quality contract is a necessary experimental milestone only. The economic moonshot remains unproven.
