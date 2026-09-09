# UQPU Project Charter

## Permanent Mission

The UQPU project exists to develop an open, provider-portable quantum computing software and research stack that can ultimately make cloud quantum computers perform the practical workload goals currently served by GPUs.

The internal process does **not** need to imitate GPU microarchitecture.

The permanent target is:

1. **GPU + Accelerator-Memory Functional Replacement** — cover the full application-level workload domain of GPUs while also targeting the functional/economic roles of VRAM/HBM and reducing dependence on large host RAM where possible.
2. **Quantum Cloud Portability** — users of this repository should be able to connect UQPU software to the broadest practical set of quantum cloud providers through provider adapters.
3. **Economic Supremacy Research Target** — pursue at least **100× lower total cost per useful completed task** than a competitive market GPU baseline, with a workload-specific moonshot target up to **100,000,000×**.
4. **Open Development** — anyone may study, fork, adapt, extend and contribute according to the repository license and contribution rules.
5. **Continuous Provider Discovery** — every development cycle must inspect whether new quantum cloud providers, devices, SDKs, APIs, access routes or pricing models have appeared.
6. **Evidence Discipline** — these cost multipliers are research objectives, not guaranteed results. All claims must be supported by end-to-end measurements or clearly labeled models.

## Permanent Invariants

These requirements must be preserved in every released version.

### INV-001 — Multi-cloud portability
The UQPU core must remain provider-agnostic. Vendor-specific SDKs belong behind adapters.

### INV-002 — Broad cloud usability
The architecture must support adding old and new quantum-cloud providers without redesigning the semantic compiler.

### INV-003 — GPU functional scope
Every major workload goal currently served by GPUs remains in project scope, including graphics, AI, HPC, simulation, signal/image/video processing, analytics, optimization and general programmable compute.

### INV-004 — End-to-end economic comparison
Cost claims must include provider billing, hardware amortization where relevant, host orchestration, state preparation, data movement, shots, QEC/error mitigation, retries, measurement, decoding, output reconstruction, energy, cooling and maintenance as applicable.

### INV-005 — 100× minimum target
The primary economic research target is at least:

[
C_{GPU/task}/C_{UQPU/task} ge 100
]

### INV-006 — 100,000,000× moonshot
The project may pursue:

[
C_{GPU/task}/C_{UQPU/task} ge 10^8
]

for workload classes where physical and algorithmic conditions make it possible.

### INV-007 — No fabricated advantage
The repository must never present MODEL_ONLY, simulated or theoretical estimates as demonstrated cloud-QPU economic advantage.

### INV-008 — Continuous development
The project follows an iterative loop:

```text
research -> implement -> test -> inspect -> improve -> retest
-> cloud-compatibility check -> benchmark -> document -> repeat
```

### INV-009 — Community usability
Documentation, examples, provider adapters and setup instructions should be sufficient for external users to run supported workloads without modifying UQPU core internals.

### INV-010 — Provider-market surveillance
Every major development/release cycle must check both existing and newly appearing quantum-cloud providers and record meaningful changes.

### INV-011 — Memory-system replacement scope
The project must treat GPU-local VRAM/HBM and associated host-RAM/data-movement costs as part of the system-level replacement target. UQPU research must seek to reduce or eliminate large classical intermediate materialization where possible, while honestly retaining classical memory where required by input/output and control.

## Definition of Success

The long-term project succeeds only when all three dimensions converge:

```text
GPU + VRAM/HBM functional coverage
        +
Reduced host-RAM/data-movement burden
        +
Quantum-cloud portability
        +
Measured economic advantage
```

A connection to a QPU alone is not success.
A simulated speedup alone is not success.
A narrow quantum algorithm alone is not success.

The target is an open system that can execute useful GPU-domain workloads through cloud quantum computers and demonstrate end-to-end economic value against competitive GPU+VRAM/HBM+host-memory stacks.


### INV-012 — Universal computing-stack scope
The long-term research scope includes CPU/general compute, persistent storage, networking/interconnect and system orchestration in addition to GPU, VRAM/HBM and RAM. The project may replace, semantically eliminate or reduce conventional subsystems while preserving useful application behavior.

### INV-013 — Hardware/photonics/device-physics scope
Hardware, photonic processors, semiconductor/process technology, packaging, control/readout, cryogenics, materials and goal-directed device/fundamental physics remain valid research layers whenever required to meet functional or economic targets.
