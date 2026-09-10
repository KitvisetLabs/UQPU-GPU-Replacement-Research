# UQPU Project Charter

## Permanent Mission

The UQPU project exists to develop an open, provider-portable quantum computing software and research stack that can ultimately make cloud quantum computers perform the practical workload goals currently served by GPUs, CPUs, NPUs and associated memory/storage systems, while progressing toward the project's highest long-term objective: **compressing extreme data-center-scale useful capability into one affordable phone-class physical device**.

The internal process does **not** need to imitate conventional GPU/CPU/NPU/memory/storage microarchitecture.

The permanent target is:

1. **Conventional Compute + Memory/Storage Functional Replacement** — cover useful application-level roles of GPU, CPU and NPU while targeting the functional/economic roles of VRAM/HBM, RAM and persistent storage where physically meaningful.
2. **Quantum Cloud Portability** — users of this repository should be able to connect UQPU software to the broadest practical set of quantum cloud providers through provider adapters.
3. **Economic Supremacy Research Target** — pursue at least **100× lower total cost per useful completed task** than a competitive conventional baseline, with a workload-specific moonshot target at and beyond **100,000,000×**.
4. **Ultimate Data-Center-to-Phone North Star** — investigate whether the useful capability associated with the owner's user-defined US$10T–US$100T conventional-infrastructure ambition envelope can ultimately be compressed into one phone-class device costing only tens of thousands of Thai baht.
5. **Ultra-Low-Cost Materials / Fuel / Electricity** — permanently research Pangola/biomass-carbon critical-material reduction, ultra-low-cost biomass bio-oil/biofuel and ultra-low-cost fusion electricity as enabling industrial pillars.
6. **Interest-Cost / R&D-Finance Compression** — reduce financed principal, capital lock-up time, project risk and absolute interest expense; treat any claimed reduction in financing rate/WACC as a separately evidenced effect.
7. **Open Development** — anyone may study, fork, adapt, extend and contribute according to the repository license and contribution rules.
8. **Continuous Provider Discovery** — every development cycle must inspect whether new quantum cloud providers, devices, SDKs, APIs, access routes or pricing models have appeared.
9. **Evidence Discipline** — cost/capability multipliers and extreme-compression objectives are research targets, not guaranteed results. All claims must be supported by end-to-end measurements or clearly labeled models.

The detailed ultimate mission is published at `00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md`. The permanent enabling strategies are `01_PANGOLA_BIOMASS_CARBON_TECHNOLOGY_STRATEGY.md`, `02_ULTRA_LOW_COST_BIOMASS_BIO_OIL_STRATEGY.md`, `03_FUSION_ELECTRICITY_COST_STRATEGY.md` and `04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md`.

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
C_{conventional/task}/C_{UQPU/task} ge 100
]

### INV-006 — 100,000,000× moonshot
The project may pursue:

[
C_{conventional/task}/C_{UQPU/task} ge 10^8
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
The project must treat accelerator-local VRAM/HBM and associated host-RAM/data-movement costs as part of the system-level replacement target. UQPU research must seek to reduce or eliminate large classical intermediate materialization where possible, while honestly retaining classical memory where required by input/output and control.

## Definition of Success

The long-term project succeeds only when all required dimensions converge:

```text
GPU + CPU + NPU functional coverage
        +
RAM / VRAM-HBM / storage functional coverage or semantic elimination
        +
Reduced data-movement / infrastructure burden
        +
Quantum-cloud portability during the development path
        +
Measured economic advantage
        +
Low-cost materials / fuel / electricity / financing burden
        +
Progressive physical integration
        +
Ultimate phone-class system boundary
```

A connection to a QPU alone is not success.
A simulated speedup alone is not success.
A narrow quantum algorithm alone is not success.
A fusion-gain milestone alone is not cheap electricity.
A low raw biomass price alone is not cheap saleable fuel or advanced material.
A phone acting only as a remote terminal to an external data center is not final data-center-to-phone physical replacement.

The target is an open system that can progressively execute useful conventional-computing workloads through quantum/UQPU methods and demonstrate end-to-end economic and physical value against competitive conventional stacks.

### INV-012 — Universal computing-stack scope
The long-term research scope includes CPU/general compute, NPU/AI acceleration, persistent storage, networking/interconnect and system orchestration in addition to GPU, VRAM/HBM and RAM. The project may replace, semantically eliminate or reduce conventional subsystems while preserving useful application behavior.

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
The project's PRIMARY execution objective is software/programming-first: use compiler transformations, semantic IR, quantum algorithms, runtime orchestration, state/data representations, provider adapters and cloud-QPU execution to make CURRENT cloud quantum computers perform the useful application-level roles served today by CPU, GPU, NPU, RAM, VRAM/HBM and persistent storage wherever physically possible. New custom quantum hardware is NOT the primary first path. Hardware/device/fabrication/materials research remains important and progresses in parallel, with escalation driven by documented software/cloud blockers and the ultimate physical-integration mission.

### INV-020 — Cloud-first functional emulation by outcome, not classical mechanism
For CPU/GPU/NPU/RAM/VRAM/storage replacement, UQPU is judged by useful workload behavior and economics, not by reproducing classical instructions, memory cells or disk mechanisms internally. Software may transform, eliminate, compress, defer or encode state differently as long as the required application contract is satisfied and all I/O/state-recovery constraints are accounted for.

### INV-021 — Software-first economic supremacy target
The first path toward >=100x and >=100,000,000x lower total cost/useful-task must prioritize software techniques on existing cloud quantum infrastructure before proposing new hardware for the same experiment. Each workload study should first attempt: semantic reformulation -> provider-neutral lowering -> cloud execution/simulation -> output validation -> total cost/task measurement -> optimization. Hardware redesign is escalated when the software/cloud path reveals a documented blocker or when later physical miniaturization gates require it.

### INV-022 — Priority #1 does not suspend parallel research
Quantum programming/software-first cloud-QPU execution is Priority #1, but it is NOT the only active research stream. Every established project lane must continue producing measurable research progress in parallel on every ongoing research horizon: workloads/software; quantum/cloud; memory/state/data movement; devices/fabrication/packaging; materials/biomass/power/cooling/infrastructure; economics/evidence/integration; and approved strategic domains. Priority #1 determines ordering, emphasis and conflict resolution, not cancellation or suspension of the other lanes. Cross-lane results must be integrated continuously toward the common ultimate mission.

### INV-023 — Historical seven-lane research architecture
The project previously operated as seven concurrent lanes before Lane H was added. This seven-lane definition remains preserved as project history and is superseded operationally by INV-024.

### INV-024 — Permanent eight-lane research architecture and Lane H strategic-plan research
The project permanently operates as EIGHT concurrent research lanes A–H. Lane A remains Priority #1, but all eight lanes must remain known, active, reviewed, progressively advanced and publicly documented in this repository.

**Lane A — Quantum Programming / Workloads / Compiler / Runtime (Priority #1):** semantic reformulation, algorithms, IR, compiler/runtime, application contracts and software-first CPU/GPU/NPU functional replacement.

**Lane B — Quantum Cloud / QPU / Provider Integration:** provider-neutral adapters, capability negotiation, execution, cloud portability and provider surveillance.

**Lane C — RAM / VRAM / HBM / Storage / State & Data Movement:** memory/state semantics, persistence, caching, recomputation, compression, bandwidth, I/O and data movement.

**Lane D — Quantum / Photonic / Semiconductor Devices, Chip Architecture, Fabrication & Packaging:** device physics, qubit/photonic/semiconductor architectures, chip processes, packaging, reliability and manufacturability.

**Lane E — Biomass / Advanced Materials / Energy / Cooling / Infrastructure:** Pangola/biomass-derived materials, carbon/graphene and material substitution, ultra-low-cost bio-oil/biofuel, fusion electricity, power, cooling, facilities, sustainability and infrastructure.

**Lane F — Economics / Benchmark / Evidence / Integration:** total cost/useful-task, baselines, benchmarks, energy/fuel economics, financing/interest burden, evidence classification, reproducibility, cross-lane integration and mission scorekeeping.

**Lane G — Quantum Chip Manufacturing Equipment & Software:** research and design of the hardware, software, tooling and factory-production systems needed to manufacture relevant quantum-processing chips and integrated future systems, including DUV/EUV and alternative lithography, deposition, etch, implantation/doping where applicable, cleaning, wafer handling, metrology/inspection, masks, process control, EDA/TCAD/process simulation, automation/robotics, cryogenic/electrical/optical characterization, photonic fabrication, assembly, bonding, packaging and test.

**Lane H — Ketskaew Chulamani / Kanusanan Pongpanna Model Strategic Development, Finance & Future-Industry Research:** continuously research, deepen, test, structure and expand the user's master development/financial plan and related articles from agriculture/Pangola/biomass and cash-flow foundations through bio-oil, materials, cheap energy/fusion, financing/interest compression, semiconductor/photonics/quantum, AI/robotics, biotechnology/health, food/water/agriculture, future cities/infrastructure, global economic networks, space industry and explicitly labeled speculative/far-future concepts, toward the Ketskaew Chulamani social-development vision.

Lane H must continuously produce research notes/articles/roadmaps/feasibility analyses and publish verified progress to GitHub. Preserve multilingual master-plan references and public links as canonical reference material. Clearly distinguish factual evidence, forecasts, hypotheses, personal/religious vision and speculative technology; do not convert targets or beliefs into scientific claims.

**Permanent rule:** Lane A is Priority #1, but A–H all progress concurrently. Every research cycle must explicitly recognize all eight lanes and must not silently delete, merge away, suspend or forget any lane.

### INV-025 — Single-QPU 100-million-GPU replacement moonshot
The project must maintain a parallel research direction testing whether one quantum computer, or one logically unified UQPU execution system, can deliver the accepted useful-work output otherwise requiring approximately **100,000,000 competitive GPUs** for a defined workload class, while targeting **>=100,000,000× lower total financial cost per accepted useful task**.

This is a permanent **moonshot research objective and falsifiable hypothesis**, not an assertion about present quantum computers. Evidence must compare equivalent useful output and account for throughput, latency, state preparation, repetitions/shots, QEC/error mitigation, retries, classical orchestration, RAM/VRAM/data movement, network/interconnect, energy/cooling, utilization, provider charges or hardware amortization, maintenance and reconstruction/verification. Simulation, asymptotic complexity or qubit-count arguments alone cannot establish this invariant as achieved.

Research cycles should develop algorithmic, architectural, cloud-QPU, memory/state, hardware, manufacturing and economic routes toward this target in parallel with the other A–H lanes, while preserving negative results and lower-multiplier intermediate evidence.

### INV-026 — Universal 100-million-unit subsystem replacement moonshot
In parallel with INV-025, the project must investigate whether one quantum computer / logically unified UQPU system can replace the accepted useful function or useful-work capacity of approximately **100,000,000 units** of each relevant conventional subsystem: GPU, CPU, NPU, RAM, VRAM/HBM and persistent storage (HDD/SSD or equivalent), while targeting **>=100,000,000x lower total financial cost** for the same accepted useful function.

This invariant is a research objective, not a statement of current quantum capability. Each subsystem requires its own equivalence contract. Compute requires equivalent workload/output quality, throughput and latency. NPU comparisons additionally require model/checkpoint, precision/quantization, task quality and neural-workload semantics rather than TOPS alone. Memory/storage requires equivalent application-visible capacity, bandwidth, latency, access semantics, persistence/retention, durability and recovery where applicable. Qubits/amplitudes must never be counted as RAM/VRAM/disk capacity merely by dimensional comparison.

Achievement requires measured end-to-end evidence including all required classical hardware and orchestration, state preparation, QEC/error mitigation, repetitions/shots, I/O, network/interconnect, energy/cooling, utilization, provider charges or amortization, maintenance, verification and output reconstruction. Negative results are retained and may show that semantic elimination/recomputation/hybrid architecture is superior to literal subsystem replacement.

### INV-027 — Open-frontier scientific search
The project must investigate all scientifically and mathematically plausible routes toward the North-Star mission, and may expand research as deeply as required into algorithms, mathematics, information theory, materials, chemistry, condensed-matter/AMO/nuclear/particle physics, quantum field theory, fundamental physics and other relevant sciences. This breadth does not weaken evidence discipline: speculative or beyond-established-physics ideas must be labeled, tied to a causal mechanism, checked against known constraints and assigned a falsifiable experiment/proof/bound. Negative and impossibility results must be preserved. Software-first quantum programming remains Priority #1 and all eight lanes A–H continue concurrently. See `docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md`.

### INV-028 — Lane-oriented repository architecture and integration-first research
The canonical lane-oriented workspace is `research_lanes/`, containing one clearly separated folder for each permanent lane A–H, with `integration/` as the cross-lane integration hub. Future nested projects must respect the repository's maximum 16 directory levels from root. Every substantive artifact has one primary owning lane; shared work uses stable interfaces/references rather than unnecessary duplicate sources of truth. Existing canonical code/docs may migrate incrementally only when imports, links, hashes, reproducibility and CI remain intact.

### INV-029 — Ultimate Data-Center-to-Phone North Star
The project's **highest long-term objective** is to investigate whether the useful computing and service capability associated with an extraordinarily large conventional data-center-scale system can ultimately be compressed into **one phone-class physical device** whose future end-user price is only **tens of thousands of Thai baht**.

The project owner expresses the ambition scale as conventional present-era infrastructure valued on the order of **US$10 trillion to US$100 trillion**. This range is a **user-defined scale/ambition proxy and must not be presented as evidence that an individual current data center actually has such a valuation**. Research must translate the scale into defensible service/capability baselines rather than treating dollars as a computational unit.

A qualifying end-state must address, where required by the target service portfolio: GPU/CPU/NPU compute, RAM, VRAM/HBM, persistent storage, state/data movement, networking/I/O, orchestration, AI/HPC/application throughput, latency, output quality, reliability, recovery/persistence, energy, cooling/thermal constraints, manufacturing, device volume/mass and total lifecycle cost.

The final phone-class physical-compression claim may not hide essential infrastructure outside the comparison boundary. Remote cloud/QPU dependence, server-side CPU/GPU/NPU, external memory/storage, cryogenic plants, control electronics, networking, power/cooling and reconstruction/verification resources must be explicitly included. A handset that merely serves as a terminal to a remote data center does not satisfy INV-029.

All earlier project targets—including >=100× economic advantage, >=100,000,000× moonshots, approximately 100-million-unit subsystem replacement, quantum-cloud programming, memory/storage transformation, device/material/manufacturing research and the Lane H financial-development strategy—are to be treated as staged research pathways toward INV-029.

INV-029 is **LONG-HORIZON / NOT_YET_DEMONSTRATED**. It is a falsifiable mission direction, not a claim of current physical feasibility and not a promised calendar delivery date. The canonical detailed milestone schedule is `00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md`.

### INV-030 — Pangola/Biomass Carbon Strategic Pillar
The project permanently prioritizes Pangola/biomass-derived carbon and advanced-material research for functional substitution, material minimization, recovery/recycling, hybridization and system redesign to reduce dependence on expensive or supply-constrained technology materials. Ordinary biomass-carbon processing does not create Au, Cu, Ag, Li, Co, Ni or rare-earth atoms, so every claim is judged on the required function and lifecycle economics. Canonical strategy: `01_PANGOLA_BIOMASS_CARBON_TECHNOLOGY_STRATEGY.md`.

### INV-031 — Ultra-Low-Cost Biomass Bio-Oil / Biofuel
The project permanently researches the lowest defensible cost for useful biomass-derived liquid fuel or refinery-compatible intermediate, with Pangola grass and other agricultural residues as candidate feedstocks. Evidence must include final accepted product quality, feedstock/preprocessing, physical yield, upgrading/hydrogen/catalysts, utilities, CAPEX/OPEX, uptime, logistics, financing and defensible non-double-counted coproduct credits. Crude liquid yield alone is not a commercial fuel-cost result. Canonical strategy: `02_ULTRA_LOW_COST_BIOMASS_BIO_OIL_STRATEGY.md`.

### INV-032 — Fusion Electricity Cost Minimization
Fusion is a permanent cheap-electricity research pillar. Success is measured by reliable **net delivered electricity cost**, not ignition, plasma gain or gross heat alone. Required economics include recirculating power, capacity factor, CAPEX/construction time, component lifetime, fuel cycle, materials damage, maintenance/remote handling, conversion/cooling, grid interfaces, financing and decommissioning. Commercial ultra-low-cost fusion electricity remains NOT_YET_DEMONSTRATED. Canonical strategy: `03_FUSION_ELECTRICITY_COST_STRATEGY.md`.

### INV-033 — Interest-Cost and R&D-Finance Compression
The project permanently minimizes financing burden by reducing underlying technology/material/fuel/electricity costs, required CAPEX/OPEX/working capital, financed principal, capital lock-up time and project risk. Lower principal directly lowers absolute interest expense at unchanged terms. Any claim that a lower-cost technology also lowers the financing rate, project WACC, policy rate or economy-wide interest rate must be separately evidenced rather than assumed. Canonical strategy: `04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md`.
