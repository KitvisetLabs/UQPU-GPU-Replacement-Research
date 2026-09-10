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


### INV-014 — Biomass and agricultural-residue materials strategy
Pangola grass and broadly available agricultural residues remain a permanent low-cost renewable-feedstock research track for UQCS and future-technology supply chains. The project must investigate functional substitution, critical-material minimization, recovery/recycling and hybrid-material routes that can reduce dependence on expensive minerals/metals while preserving scientific constraints on elemental identity.


### INV-015 — Complete chip-fabrication equipment and process scope
UQCS research includes fabrication equipment and factory/process integration required for candidate semiconductor, photonic, quantum, memory, control and packaging devices. Lithography research may include mature optical, DUV, immersion, EUV at system/economic level, direct-write, e-beam, nanoimprint and future routes. The project must co-optimize device architecture and fabrication economics rather than assume the most advanced lithography is required.

### INV-016 — Parallel fabrication workstreams and integration review
Fabrication research must maintain separable lithography, deposition, etch, doping, metrology, cleaning, photonics, quantum-device, packaging, materials, economics and automation workstreams with explicit interfaces. Findings must be integrated against the permanent end-to-end functional and economic objective.


### INV-017 — Permanent multilingual strategic-plan preservation
The user-provided **Ketskaew Chulamani / Kanusanan Pongpanna Model** multilingual plan and the public source links recorded in `STRATEGIC_PLAN_REFERENCES.md` are permanent project context. Every meaningful project update/release must preserve a visible repository reference to that document and must not silently remove its links. The plan must be considered during research integration while scientific/economic claims remain subject to independent evidence verification.


### INV-018 — Cross-chat research operating system continuity
The canonical operating method in `docs/RESEARCH_OPERATING_SYSTEM.md` is a permanent project invariant. Every AI agent, contributor, new chat/session, automation or development environment working on this repository must begin by reading the repository's current charter, version invariants, research operating system, master strategy, decisions, worklog and living research gaps rather than relying on prior-chat memory. The current eight-lane A–H Research Operating System, shared work-item contract, P0–P4 priorities, single scoreboard, integration gate, evidence discipline, negative-result preservation and GitHub synchronization rule must remain the default workflow unless an explicit documented decision replaces it.


### INV-019 — Software-first cloud-QPU replacement priority
The project's PRIMARY execution objective is software/programming-first: use compiler transformations, semantic IR, quantum algorithms, runtime orchestration, state/data representations, provider adapters and cloud-QPU execution to make CURRENT cloud quantum computers perform the useful application-level roles served today by CPU, GPU, RAM, VRAM/HBM and persistent storage wherever physically possible. New custom quantum hardware is NOT the primary path. Hardware/device/fabrication/materials research remains important but is secondary unless a documented software/cloud blocker proves that existing cloud hardware cannot satisfy a required function or economic target.

### INV-020 — Cloud-first functional emulation by outcome, not classical mechanism
For CPU/GPU/RAM/VRAM/storage replacement, UQPU is judged by useful workload behavior and economics, not by reproducing classical instructions, memory cells or disk mechanisms internally. Software may transform, eliminate, compress, defer or encode state differently as long as the required application contract is satisfied and all I/O/state-recovery constraints are accounted for.

### INV-021 — Software-first economic supremacy target
The first path toward >=100x and up to 100,000,000x lower total cost/useful-task must prioritize software techniques on existing cloud quantum infrastructure before proposing new hardware. Each workload study should first attempt: semantic reformulation -> provider-neutral lowering -> cloud execution/simulation -> output validation -> total cost/task measurement -> optimization. Hardware redesign is escalated only when this path is blocked and the blocker is documented.


### INV-022 — Priority #1 does not suspend parallel research
Quantum programming/software-first cloud-QPU execution is Priority #1, but it is NOT the only active research stream. Every established project lane must continue producing measurable research progress in parallel on every ongoing research horizon: workloads/software; quantum/cloud; memory/state/data movement; devices/fabrication/packaging; materials/biomass/power/cooling/infrastructure; economics/evidence/integration; and any additional approved project domains. Priority #1 determines ordering, emphasis and conflict resolution, not cancellation or suspension of the other lanes. Cross-lane results must be integrated continuously toward the common North-Star mission.


### INV-023 — Permanent seven-lane research architecture
The project permanently operates as SEVEN concurrent research lanes. Lane A is Priority #1, but all seven lanes must remain known, active, reviewed and progressively advanced:
1. **Lane A — Quantum Programming / Workloads / Compiler / Runtime (Priority #1):** semantic reformulation, algorithms, IR, compiler/runtime, application contracts and software-first CPU/GPU functional replacement.
2. **Lane B — Quantum Cloud / QPU / Provider Integration:** provider-neutral adapters, capability negotiation, execution, cloud portability, QPU/photonic/annealing/analog access and provider surveillance.
3. **Lane C — RAM / VRAM / HBM / Storage / State & Data Movement:** memory/state semantics, persistence, caching, recomputation, compression, bandwidth, I/O and data movement.
4. **Lane D — Quantum / Photonic / Semiconductor Devices, Chip Architecture, Fabrication & Packaging:** device physics, qubit/photonic/semiconductor architectures, chip processes, packaging, reliability and manufacturability.
5. **Lane E — Biomass / Advanced Materials / Energy / Cooling / Infrastructure:** Pangola/biomass-derived materials, carbon/graphene and material substitution, power, cooling, facilities, sustainability and infrastructure.
6. **Lane F — Economics / Benchmark / Evidence / Integration:** total cost/useful-task, baselines, benchmarks, evidence classification, reproducibility, cross-lane integration and mission scorekeeping.
7. **Lane G — Quantum Chip Manufacturing Equipment & Software:** research and design of ALL hardware, software, control systems and production equipment required to manufacture every relevant form of quantum-processing chip, including lithography (DUV/EUV and alternatives), deposition, etch, implantation/doping where applicable, cleaning, wafer handling, metrology/inspection, masks, process control, EDA/TCAD/process simulation, automation/robotics, cryogenic/electrical/optical characterization, photonic fabrication, assembly, bonding, packaging, test and future manufacturing methods.

Lane G is distinct from Lane D: Lane D owns the chips/devices/process architecture and manufacturability requirements; Lane G owns the machines, tooling, software and factory-production systems that realize those requirements. The two lanes must co-design continuously.

**Permanent rule:** Priority #1 means emphasis, not exclusivity. Every research cycle must explicitly recognize A–G and must not silently delete, merge away or suspend a lane. All seven feed the same North-Star mission.


### INV-024 — Permanent eight-lane research architecture and Lane H strategic-plan research
The project permanently operates as EIGHT concurrent research lanes A–H. Lane A remains Priority #1, but all eight lanes must remain known, active, reviewed, progressively advanced and publicly documented in this repository.

**Lane H — Ketskaew Chulamani / Kanusanan Pongpanna Model Strategic Development, Finance & Future-Industry Research:** continuously research, deepen, test, structure and expand the user's master development/financial plan and its related articles. This includes the progression from agriculture/Pangola grass/biomass and cash-flow foundations through carbon/materials, energy, semiconductor/photonics/quantum, AI/robotics, biotechnology/health, food/water/agriculture, future cities/infrastructure, global economic networks, space industry and explicitly labeled speculative/far-future concepts, toward the Ketskaew Chulamani social-development vision. It also includes financial engineering, startup/funding pathways, One Person Business Company, Local AI, Local Deep Agents, agent-swarm operations, business automation and integration with the technical A–G research program.

Lane H must continuously produce research notes/articles/roadmaps/feasibility analyses and publish verified progress to GitHub. Preserve the multilingual master-plan references and public links as canonical reference material. Clearly distinguish factual evidence, forecasts, hypotheses, personal/religious vision and speculative technology; do not convert targets or beliefs into scientific claims.

**Permanent rule:** Lane A is Priority #1, but A–H all progress concurrently. Every research cycle must explicitly recognize all eight lanes and must not silently delete, merge away, suspend or forget Lane H or any other lane.


### INV-025 — Single-QPU 100-million-GPU replacement moonshot
The project must maintain a parallel research direction testing whether one quantum computer, or one logically unified UQPU execution system, can deliver the accepted useful-work output otherwise requiring approximately **100,000,000 competitive GPUs** for a defined workload class, while targeting **>=100,000,000× lower total financial cost per accepted useful task**.

This is a permanent **moonshot research objective and falsifiable hypothesis**, not an assertion about present quantum computers. Evidence must compare equivalent useful output and account for throughput, latency, state preparation, repetitions/shots, QEC/error mitigation, retries, classical orchestration, RAM/VRAM/data movement, network/interconnect, energy/cooling, utilization, provider charges or hardware amortization, maintenance and reconstruction/verification. Simulation, asymptotic complexity or qubit-count arguments alone cannot establish this invariant as achieved.

Research cycles should develop algorithmic, architectural, cloud-QPU, memory/state, hardware, manufacturing and economic routes toward this target in parallel with the other A–H lanes, while preserving negative results and lower-multiplier intermediate evidence.


### INV-026 — Universal 100-million-unit subsystem replacement moonshot
In parallel with INV-025, the project must investigate whether one quantum computer / logically unified UQPU system can replace the accepted useful function or useful-work capacity of approximately **100,000,000 units** of each relevant conventional subsystem: GPU, CPU, RAM, VRAM/HBM and persistent storage (HDD/SSD or equivalent), while targeting **>=100,000,000x lower total financial cost** for the same accepted useful function.

This invariant is a research objective, not a statement of current quantum capability. Each subsystem requires its own equivalence contract. Compute requires equivalent workload/output quality, throughput and latency. Memory/storage requires equivalent application-visible capacity, bandwidth, latency, access semantics, persistence/retention, durability and recovery where applicable. Qubits/amplitudes must never be counted as RAM/VRAM/disk capacity merely by dimensional comparison.

Achievement requires measured end-to-end evidence including all required classical hardware and orchestration, state preparation, QEC/error mitigation, repetitions/shots, I/O, network/interconnect, energy/cooling, utilization, provider charges or amortization, maintenance, verification and output reconstruction. Negative results are retained and may show that semantic elimination/recomputation/hybrid architecture is superior to literal subsystem replacement.
