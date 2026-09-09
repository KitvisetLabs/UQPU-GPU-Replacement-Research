# Batch 012 — Executable QUBO-to-QAOA programming and bounded verification

Date: 2026-09-09. Priority #1: quantum programming. Evidence: **PROTOTYPE / SIMULATION / DRY_RUN_ONLY**.

## Result

The existing QUBO optimization contract now has an executable gate-model path:

QUBO objective → exact Ising mapping → portable QAOA circuit → ideal CPU simulation → sampled assignment → exact-fixture quality assessment.

The same compiler also generates inspection payloads for the existing 32/128/512-variable benchmark tiers, without allocating an exponential statevector. IBM, Braket and Azure inspection adapters receive these circuits. This closes a local compiler-verification gap; target SDK parsing, backend ISA mapping, noise and real-QPU execution remain open.

Code: [qaoa.py](../software/uqpu-prototype/uqpu/qaoa.py), [small_statevector.py](../software/uqpu-prototype/uqpu/small_statevector.py), [runner](../software/uqpu-prototype/examples/run_qaoa_verification.py), [tests](../software/uqpu-prototype/tests/test_qaoa.py).

Data: [complete experiment artifact](../benchmarks/results/batch012-qaoa-verification.json), including every grid evaluation, selected circuits, probability vectors, seeded shot counts, original QUBOs, instance digests, certificates, provider payloads, environment and executed-source hashes.

## Mathematical convention

The repository minimizes

\[
E(x)=c+\sum_i a_i x_i+\sum_{i,j}b_{ij}x_i x_j,\quad x_i\in\{0,1\}.
\]

Diagonal quadratic terms are folded into linear terms because \(x_i^2=x_i\). Opposite pair orientations are summed. For the resulting unique off-diagonal pairs, \(x_i=(1-Z_i)/2\) gives

\[
H=C+\sum_i h_i Z_i+\sum_{i<j}J_{ij}Z_iZ_j,
\quad J_{ij}=b_{ij}/4,
\]

\[
h_i=-a_i/2-\sum_{j\ne i}b_{ij}/4,
\qquad C=c+\sum_i a_i/2+\sum_{i<j}b_{ij}/4.
\]

Here the coefficient in the sum defining \(h_i\) denotes the unique incident-pair weight. The offset is retained for objective evaluation. Its global phase is omitted from the circuit. Each layer applies cost evolution followed by an X mixer, with RZ(2γh), CX–RZ(2γJ)–CX, and RX(2β). Sparse variable IDs map to ascending qubit indices; qubit 0 is the least significant bit of integer outcomes. These choices preserve the original objective's sign and scale. Background: [Farhi, Goldstone and Gutmann](https://arxiv.org/abs/1411.4028), [OpenQASM standard gates](https://openqasm.com/language/standard_library.html).

## Reproducible experiment

Three unit-weight MaxCut fixtures use p=1 and a 24×24 grid: γ=πi/24 and β=πj/24 for i,j=0..23. This is a bounded coarse search, not a certified global parameter optimization. An ideal statevector computes each candidate expectation; 4,096 pseudorandom shots are drawn only from the selected circuit. The classical oracle exhaustively evaluates each fixture. It is a correctness reference, not a competitive runtime baseline.

| Fixture | Qubits | Uniform expected objective | Selected expected objective | Exact optimum | Best sampled objective | Ideal optimum probability per shot |
|---|---:|---:|---:|---:|---:|---:|
| triangle | 3 | -1.5 | -1.988416 | -2 | -2 | 0.994208 |
| ER, seed 42, p(edge)=0.5 | 6 | -4.5 | -5.680228 | -7 | -7 | 0.253917 |
| ER, seed 73, p(edge)=0.4 | 8 | -4.5 | -6.116055 | -8 | -8 | 0.129883 |

Lower is better. All three runs contain an optimal sampled bitstring, but the expected objective is not equal to the optimum. The artifact's `sampled_quality.verified_quality` applies only to the best sampled assignment against its fixture certificate. It does not certify the QAOA parameter optimum, performance advantage, hardware behavior or another workload.

The local run used Python 3.12.14 on x86_64 Linux. The full regression suite ran 142 tests: 141 passed, one optional OR-Tools availability test skipped. Ten new tests cover exhaustive signed/noncontiguous/diagonal QUBO mappings, a separate dense mathematical QAOA oracle across two layers, global-phase invariance, normalization, sample totals, provider inspection and bounded allocation. No vendor SDK cross-check has yet run.

```bash
cd software/uqpu-prototype
python -m pip install -e .
python -m unittest discover -s tests -v
python examples/run_qaoa_verification.py --output /tmp/qaoa-verification.json
```

Seeds, objectives and circuit payloads should reproduce; timestamps and host timing vary. Source hashes identify the executed implementation even though `source_checkout_head` records the pre-publication base commit.

## Existing-tier lowering and memory limits

The original contract IDs are unchanged. These rows are compilation/inspection results only; the angles are fixed and unoptimized.

| Tier | Contract ID | Qubits | Edges / ZZ terms | CX before routing | RZ | H | RX |
|---|---|---:|---:|---:|---:|---:|---:|
| small | 8e478d5edde63daa | 32 | 83 | 166 | 83 | 32 | 32 |
| medium | 2ec80fa696739a17 | 128 | 636 | 1,272 | 636 | 128 | 128 |
| large | f0668da7d4ee8464 | 512 | 3,850 | 7,700 | 3,850 | 512 | 512 |

Each circuit also has terminal measurement. Routing may add gates and depth. The direct encoding uses one qubit per variable. Merely fitting a qubit count does not establish connectivity, fidelity, device availability or acceptable cost.

A dense complex128 state payload requires \(16\,2^n\) bytes: **64 GiB at 32 qubits**, before overhead. This is a mathematical storage model, not measured peak RAM. The verification simulator is capped at 12 qubits before allocating state. The 128/512-variable tiers were not simulated. This result does not implement persistent quantum storage or replace classical RAM. QUBOs, parameter records, outcomes and certificates still require classical storage.

## Cross-lane integration

| Lane | Concrete outcome / reviewed blocker | Next acceptance gate |
|---|---|---|
| A — priority #1 | Objective-preserving compiler and complete small-fixture simulation loop | Independent SDK circuit equivalence and finite-shot/noise study |
| B | IBM/Braket/Azure inspection payloads; current IBM documentation reviewed | Selected target SDK, transpilation, physical layout and execution provenance |
| C | Explicit variable/bit mapping, serialized byte counts and exponential simulation cap | Measure peak RAM and decoding/transfer overhead; compare alternative encodings |
| D | Workload-derived requirements: 32 qubits, 83 interactions, at least 166 logical CX for small p=1 | Calibrated connectivity, gate/readout error and routed duration, rather than a new chip claim |
| E | Infrastructure accounting reviewed: energy, cooling, material reliability and lifecycle cost remain unmeasured | Equal-quality energy/useful-task and qualified functional-unit material comparison |
| F | Raw grids/counts, exact-fixture certificates and execution hashes | Preserve RG-024: small/medium production-tier bounds remain unproven |
| G | Routing/calibration/metrology dependency tied to concrete D requirements | Tool/process capability distributions and device calibration evidence; no fabrication result |
| H | [Article 009](LANE_H_ARTICLE_009_COMPILER_EVIDENCE_AND_CAPITAL.md) links this result to staged research spending | Close software/target evidence gaps before hardware capital escalation |

All lanes were integrated sequentially in this session. No parallel-agent execution is claimed. The [master strategy](KANUSANAN_PONGPANNA_MODEL.md) and [all multilingual references](../STRATEGIC_PLAN_REFERENCES.md) remain preserved.

## Literature decisions and next experiments

The [source review](BATCH_012_SOURCE_REVIEW.md) connects primary research and official documentation to implementation decisions. A useful next candidate is Pauli correlation encoding: research whether reduced qubit requirements outweigh optimization, shot and decoding costs. This is a different optimization formulation, not a drop-in replacement for the exact diagonal Hamiltonian above. It must be judged against the same original MaxCut objective after decoding.

1. Cross-check generated circuits with an independent SDK and add explicit provider bit-order decoding.
2. Obtain rigorous lower bounds for existing small/medium contracts (RG-024), preserving their identity.
3. Compare direct QAOA with a small Pauli-correlation experiment under an equal total evaluation/shot budget.
4. Run noisy simulation with recorded calibration assumptions; then use an authorized QPU target and competitive classical solver.

No REAL_QPU experiment, quantum advantage, 100× cost reduction, GPU replacement or persistent-memory replacement is demonstrated by Batch 012.
