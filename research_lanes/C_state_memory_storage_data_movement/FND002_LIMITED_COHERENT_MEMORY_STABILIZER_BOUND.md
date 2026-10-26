# FND-002 extension — coherent-memory-limited testing and learning

**Primary owner:** Lane C — RAM / VRAM / HBM / storage / state / data movement  
**Status:** PROPOSED — literature-derived resource contract; not independently reproduced  
**Source:** Arunachalam & Schatzki, arXiv:2607.02444 (2026-07-02), https://arxiv.org/abs/2607.02444  
**Cross-lane consumers:** A, F, H  
**Related:** INV-026/029/034/035; FND-002; EQN-001–006

## Contract distinction

FND-002's existing output-information bound concerns the minimum information needed to distinguish and expose accepted classical outcomes. The limited-coherent-memory result is a different family of mathematical resource bounds: for a stated stabilizer-state task, the sample complexity depends on the coherent-memory budget. These bounds must not be merged into one quantity or treated as a general memory-capacity theorem.

| Field | Required record |
|---|---|
| Task | STABILIZER_TESTING, STABILIZER_LEARNING, or another explicitly defined task |
| State size | n qubits in the problem instance |
| Coherent memory | k qubits retained coherently between copies/measurements; define when memory is measured |
| Sample/copy budget | copies consumed, re-preparation and failed attempts included |
| Measurement/control | measurement count, adaptive/non-adaptive policy, reset/control overhead |
| Classical resources | host RAM, working storage, classical compute and transfer bytes |
| Accepted output | decision or reconstruction target, error/quality threshold, reference certificate |
| Operational metrics | latency, throughput, retries, energy where measured, billable usage and total cost per accepted task |
| Evidence state | paper theorem, independently checked proof, MODEL_ONLY simulation, or measured implementation — never collapse these states |

## Source-reported bounds — do not generalize beyond assumptions

The official preprint reports Θ(n − k) sample complexity for stabilizer-state testing and Θ(n²/k) for non-adaptive stabilizer-state learning in its specified k-qubit coherent-memory framework, plus an exponential purity-testing lower bound in a stated coherent protocol. These statements are literature claims pending an independent UQPU theorem audit. They do not give a wall-clock, joule, dollar, RAM-byte or phone-compression result.

## Fail-closed acceptance

1. Record the exact source revision, theorem statement, assumptions, task model and proof location.
2. Keep testing and learning as separate workload IDs and preserve the adaptive/non-adaptive distinction.
3. Reject a comparison if n, k, copy budget, noise model, output quality, or access model differs without an explicit normalization.
4. Do not convert k qubits or 2^n state-space labels into readable classical bytes.
5. Keep unsuccessful proof checks, counterexamples and simulation failures as first-class records.
6. Promote no theorem to physical law, hardware performance, material/fuel/fusion advantage or economics without the separate relevant evidence gates.

## Integration edges

- **A ↔ C:** coherent-memory constraints become explicit workload parameters before algorithm selection and provider lowering.
- **C ↔ F:** report copies and memory separately from latency, joules, provider charges and total cost.
- **C ↔ INV-029:** include measurement/control and classical reconstruction in the eventual phone-class physical boundary.
- **FND-002 ↔ INV-035:** the result is a scoped incumbent-model constraint; any proposed alternative must identify which assumption changes, a replacement equation, a discriminating observable and an independent validation path.

## Next gate

Independently reconstruct the source theorem. Only then create a small-n diagnostic and, if an executable reference exists, a preregistered matched-output test/learn benchmark. No real-QPU job is authorized by this artifact.