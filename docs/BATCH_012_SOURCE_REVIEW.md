# Batch 012 — Primary-source review and research decisions

Access/review date: 2026-09-09. These are targeted searches for the active programming experiment, not an exhaustive systematic literature review. Abstract-only reads are identified below. Vendor claims remain attributed; no third-party performance number is imported as a UQPU measurement.

| Source | Scope read | Relevance and decision |
|---|---|---|
| Farhi, Goldstone & Gutmann, [A Quantum Approximate Optimization Algorithm](https://arxiv.org/abs/1411.4028), 2014; DOI 10.48550/arXiv.1411.4028 | Abstract | Foundational alternating cost/mixer algorithm. Implement QAOA as an optimization candidate; do not extrapolate graph-specific guarantees to arbitrary workloads. |
| IBM, [Quantum approximate optimization algorithm](https://quantum.cloud.ibm.com/docs/en/tutorials/quantum-approximate-optimization-algorithm) | Mapping, workflow, parameter optimization, transpilation and result decoding sections | Ground the programming path in a complete workload-to-output loop. Preserve our repository's objective sign, scale and offset; do not blindly copy a tutorial Hamiltonian normalization. Backend-native compilation and measured output remain separate gates. |
| [OpenQASM standard library](https://openqasm.com/language/standard_library.html) | Gate definitions | Use RX/RZ/CX conventions and terminal measurement in portable inspection output. A valid text representation does not prove a provider supports it. |
| Zhan et al., [A Full Stack Framework for High Performance Quantum-Classical Computing](https://arxiv.org/abs/2510.20128), 2025; DOI 10.48550/arXiv.2510.20128 | Abstract | Portable quantum kernels, compilation and orchestration are relevant architecture precedents. Their hybrid demonstrations do not establish full classical-system replacement. Keep host, compilation and orchestration costs explicit. |
| Miniskar et al., [Q-IRIS: The Evolution of the IRIS Task-Based Runtime to Enable Classical-Quantum Workflows](https://arxiv.org/abs/2512.13931), 2025 | Abstract and indexed full-text conclusion | Task-based quantum/classical integration motivates a later runtime scheduling comparison. It does not remove the need to validate UQPU output, latency and data movement. |
| IBM, [Pauli correlation encoding to reduce max-cut requirements](https://quantum.cloud.ibm.com/docs/en/tutorials/pauli-correlation-encoding-for-qaoa) | Encoding, capacity formula, measurement and reference sections | Candidate software approach to the direct-encoding qubit bottleneck. Compare original decoded objective, total measurements and optimization effort before claiming savings. |
| IBM, [Nighthawk r2—more circuits, faster](https://www.ibm.com/quantum/blog/nighthawk-r2), 31 Aug 2026 | Device, reset, throughput and application sections | Reconfirms an existing project source: 120 programmable qubits and vendor-reported >100,000 circuits/s. This is not new UQPU performance. Direct 128/512-qubit mappings exceed this device's programmable count; small still requires topology and quality checks. |

## Candidate: correlation encoding as a Lane A/C experiment

IBM's tutorial points to Sciorilli et al., [Towards large-scale quantum optimization solvers with few qubits](https://arxiv.org/abs/2401.09421). Track the primary paper for a full method review before implementation.

For the tutorial's two-body construction, capacity is \(m\leq3\binom n2\). A capacity calculation gives:

| Original binary variables | Direct encoding qubits | Correlation-capacity qubits (model) |
|---:|---:|---:|
| 32 | 32 | 6 |
| 128 | 128 | 10 |
| 512 | 512 | 19 |

These are **encoding-capacity calculations**, not successful solution demonstrations or arbitrary-data memory capacities. The nonlinear loss, reachable states, measurement uncertainty and decoding can change performance and attainable quality. Three measurement settings do not mean three total shots. This project's inference is that a small equal-budget comparison is worth testing; no speedup or quantum RAM result follows from the table.

## Source freshness and continuity

The shared [Continue UQPU Development conversation](https://chatgpt.com/share/6aa176fe-7114-83ec-a6ba-bb970db3e9c2?ogimg=plain) was retrieved from its public HTML and decoded message data. Its instructions confirm software/cloud-first execution, CPU/GPU/RAM/VRAM/storage functional scope, A–H continuity and publication at each meaningful milestone. The repository at `58d0e0220221c1f10fcb59d387bd0f92e626e348` is newer than the share's latest recorded batch and remains canonical.

The initial checkout contained 208 tracked files. Repository-wide path, document-heading and code-entry-point inventory was combined with detailed reads of the charter, invariants, master strategy, references, worklog, decisions, gaps, scoreboard, active benchmark/compiler/provider code and tests. This is not a claim that every historical economic or physical assumption has been independently revalidated. The six-language strategy links are preserved; their full external documents were not independently re-audited in this batch.

The newest sampled Gmail failure notification referred to an older public [workflow run](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/34371863973). The latest available code-triggered [baseline CI run](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/34374036120) was successful. Later documentation-only commits did not trigger that workflow. This distinction avoids mistaking an old notification for current failure or assuming that a successful older run tested a newer commit.

Future cycles must repeat targeted primary-source searches, record the query/topic and review depth, and connect new evidence to an experiment, decision or explicit no-change finding. Do not turn an unavailable source into an assumed fact.
