# Batch 013 — Independent SDK verification and routing overhead

Date: 2026-09-09. Priority #1: quantum programming. Status: **SIMULATION / DRY_RUN_ONLY**.

## Findings

Qiskit 2.5.2 with qiskit-qasm3-import 0.6.0 independently parsed the OpenQASM emitted in [Batch 012](BATCH_012_QAOA_PROGRAMMING_AND_SIMULATION.md). For each of the three 3/6/8-qubit fixtures and all three provider-labelled inspection payloads, its statevector probabilities agreed with UQPU's own simulator. These are nine SDK comparisons of three distinct circuits, not nine independent workload experiments.

- Maximum absolute probability difference before routing: **1.1102230246251565e-16**.
- Maximum difference after synthetic routing and explicit readout permutation decoding: **1.3877787807814457e-16**.
- All nine 32/128/512-qubit provider-labelled payloads parsed successfully; none was statevector simulated or run on a QPU.

The agreement closes the independent-SDK part of RG-026 for these fixtures. It is an independent implementation check, not third-party research replication. Parsing an Azure/Braket-labelled payload in Qiskit does not establish acceptance by Azure or Braket.

## Synthetic routing experiment

Use a bidirectional nearest-neighbor line, basis `rz,sx,x,cx`, optimization level 2 and transpiler seed 17. This is a controlled synthetic topology, not a current provider device or calibration snapshot.

| Circuit | Qubits | CX before routing | CX after routing | Depth before | Depth after |
|---|---:|---:|---:|---:|---:|
| triangle | 3 | 6 | 9 | 12 | 25 |
| ER seed 42 | 6 | 18 | 31 | 24 | 43 |
| ER seed 73 | 8 | 18 | 32 | 27 | 55 |
| existing small tier | 32 | 166 | 1,043 | 66 | 352 |

The 32-qubit study increases CX count by about **6.28×** under this routing configuration. The lower-level basis also changes depth, so this table must not be interpreted as physical-duration or energy ratios. The larger circuit was parsed and transpiled only. In the bounded fixtures, measurement maps were used to reconstruct classical result order after routing and preserve the original variable assignment semantics.

The engineering consequence is concrete: qubit count alone cannot select a provider or justify hardware expenditure. D/G need the routed interaction graph, native gate decomposition, calibration and a quality budget. E/F need measured energy and total cost at accepted output quality. No generic 6.28× overhead is assumed for other topologies or optimizers.

## Reproduce and inspect

Code: [SDK verifier](../software/uqpu-prototype/uqpu/sdk_verification.py), [runner](../software/uqpu-prototype/examples/run_qiskit_crosscheck.py), [readout tests](../software/uqpu-prototype/tests/test_sdk_verification.py).

Data: [Batch 013 artifact](../benchmarks/results/batch013-qiskit-crosscheck.json). It records environment versions, input-artifact and source hashes, per-payload errors, routing counts, readout maps and limitations. Input is the unchanged published Batch 012 artifact.

Use an isolated **Python 3.12** environment; the optional dependency lock is the actually tested environment and is not a cross-version core requirement.

```bash
cd software/uqpu-prototype
python -m pip install -e .
python -m pip install -r verification-optional-requirements.txt
python -m unittest discover -s tests -q
python examples/run_qiskit_crosscheck.py --output /tmp/qiskit-crosscheck.json
```

The SDK environment ran **145 tests: 144 passed, one optional OR-Tools test skipped**. The dependency-free environment ran 145 tests with 141 passed and four optional tests skipped. A dedicated Python 3.12 CI job now reruns the decoder tests and SDK experiment. The core runtime retains no Qiskit dependency.

## Source review

Reviewed the official [Qiskit OpenQASM 3 API](https://quantum.cloud.ibm.com/docs/en/api/qiskit/qasm3), the [IBM QAOA workflow](https://quantum.cloud.ibm.com/docs/en/tutorials/quantum-approximate-optimization-algorithm), and installed SDK behavior. The API specifies conversion between OpenQASM and QuantumCircuit; the QAOA workflow makes target transpilation and result interpretation explicit. This batch tests both concepts locally rather than assuming a serialization success is an execution success.

The [correlation-encoding primary paper](https://arxiv.org/abs/2401.09421) abstract and journal metadata were also reviewed: the record links to Nature Communications 16, 476 (2025), DOI [10.1038/s41467-024-55346-z](https://doi.org/10.1038/s41467-024-55346-z). RG-027 remains a candidate pending full method review and an equal-budget experiment; reported external results are not UQPU results.

## A–H integration and next gate

| Lane | Outcome | Remaining gate |
|---|---|---|
| A | Independent parser/simulator agreement | Finite-shot and noisy correctness at matched output quality |
| B | SDK-parsed circuits with explicit readout mapping | Actual provider SDK/ISA, target access and recorded job results |
| C | Routing permutation decoded to original classical bits | Hardware result schema, measured memory/transfer overhead |
| D | Topology sensitivity quantified for a synthetic model | Source real coupling maps and gate/readout calibration |
| E | Gate overhead identified as an energy-accounting input | Measure energy/useful-task; no material or cooling result claimed |
| F | Input/source hashes, pinned environment and automatic SDK gate | Competitive classical baseline and tier reference bounds |
| G | Routing demand connected to D calibration/metrology needs | Measured device/process capability; no factory result claimed |
| H | [Article 009 follow-up](LANE_H_ARTICLE_009_COMPILER_EVIDENCE_AND_CAPITAL.md) updates the software gate | Prioritize noisy/target integration before hardware capital escalation |

The next highest-value experiment is a finite-shot/noise sensitivity comparison of the frozen circuits, followed by calibrated target routing. All stages must preserve the original workload objective and include parameter-search, readout, retries, host, I/O and cost. RG-024 remains open. Priority #1, all eight lanes, the [master strategy](KANUSANAN_PONGPANNA_MODEL.md) and [multilingual references](../STRATEGIC_PLAN_REFERENCES.md) are preserved.

No cloud job was submitted. No quantum advantage, ≥100× economic win or CPU/GPU/RAM/storage replacement is demonstrated.
