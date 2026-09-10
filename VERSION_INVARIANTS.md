# Version Invariants

Every UQPU release must preserve the following project-level guarantees in its documentation and architecture.

| ID | Invariant | Required in every version |
|---|---|---|
| INV-001 | Provider-agnostic UQPU core | Yes |
| INV-002 | Extensible quantum-cloud adapters | Yes |
| INV-003 | Full GPU functional-domain research scope | Yes |
| INV-004 | End-to-end cost accounting | Yes |
| INV-005 | >=100× cost/task research target | Yes |
| INV-006 | Up to 100,000,000× workload-specific moonshot | Yes |
| INV-007 | No unsupported quantum-advantage claims | Yes |
| INV-008 | Develop-test-inspect-improve loop | Yes |
| INV-009 | External-user usability and documentation | Yes |
| INV-010 | Continuous provider-market surveillance | Yes |
| INV-011 | VRAM/HBM and host-memory/data-movement replacement scope | Yes |
| INV-012 | CPU/NPU/storage/network/full-system research scope in addition to GPU/accelerator scope | Yes |
| INV-013 | Hardware/photonics/device-physics research scope | Yes |
| INV-014 | Biomass/agricultural-residue advanced-materials strategy | Yes |

## Release rule

A version should not be considered compliant if it removes or weakens these invariants without an explicit research decision documenting why.

## CI enforcement

The repository includes automated policy tests that check permanent mission markers, the eight-lane directory architecture and the maximum directory-depth rule.

| INV-015 | Complete chip-fabrication equipment/process research scope | Yes |
| INV-016 | Parallel fab workstreams with cross-system integration | Yes |
| INV-017 | Preserve multilingual Ketskaew Chulamani / Kanusanan Pongpanna strategic plan links and integrate the plan as permanent research context | Yes |
| INV-018 | Cross-chat/session continuity: load and follow the canonical current eight-lane Research Operating System from GitHub | Yes |
| INV-019 | Software/programming-first use of current cloud QPUs is the primary execution strategy | Yes |
| INV-020 | Replace CPU/GPU/NPU/RAM/VRAM/storage by application outcome, not classical internal mechanism | Yes |
| INV-021 | Attempt software/cloud path to >=100x economics before escalating to new hardware | Yes |
| INV-022 | Quantum programming is Priority #1 while all established research lanes continue progressing in parallel | Yes |
| INV-023 | Historical seven-lane architecture milestone preserved as project history; superseded operationally by INV-024 | Yes |
| INV-024 | Permanent eight-lane architecture A–H; Lane H continuously researches/publishes the Ketskaew Chulamani / Kanusanan Pongpanna Model strategic plan | Yes |
| INV-025 | Single-QPU ~100,000,000-GPU useful-work replacement + >=100,000,000x cost moonshot; evidence-gated | Yes |
| INV-026 | Universal ~100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage functional replacement + >=100,000,000x cost moonshot; subsystem-specific equivalence contracts required | Yes |
| INV-027 | Open-frontier search across all scientifically/mathematically plausible depths, including fundamental physics, with falsifiability and evidence gates | Yes |
| INV-028 | Dedicated GitHub folders for lanes A–H, maximum 16 directory levels from repository root, primary artifact ownership, and integration-first cross-lane interfaces through the shared integration hub | Yes |
| INV-029 | Ultimate North Star: compress a user-defined $10T–$100T data-center-scale capability envelope into one future phone-class device costing only tens of thousands of THB, judged by equivalent useful service contracts rather than dollar-value analogy | Yes |

## INV-028 operational definition

The canonical lane-oriented workspace is `research_lanes/`, containing one clearly separated folder for each permanent lane A–H. Future special projects may create nested subfolders under the owning lane or under `integration/`, but repository paths must never exceed **16 directory levels from repository root**. Every substantive artifact has one primary owning lane; shared work uses cross-lane contracts and stable references rather than unnecessary duplication. Existing canonical code/docs may migrate incrementally when moving them can be done without breaking imports, links, reproducibility identifiers, tests or CI. Research direction must maximize scientifically defensible integration among all eight lanes around common useful-output, feasibility and total-cost objectives. See `research_lanes/README.md`, `research_lanes/LANE_DIRECTORY_POLICY.md` and `integration/LANE_INTERFACE_CONTRACT.md`.

## NPU scope clarification

NPU is a permanent accelerator-replacement target alongside GPU and CPU. NPU claims must use neural-workload equivalence contracts—model/checkpoint, precision/quantization, task quality, batch/sequence/input shape, latency, throughput, memory/data movement and total cost—not headline TOPS alone. The permanent detailed tracks are `research_lanes/A_quantum_programming_runtime/NPU_REPLACEMENT_TRACK.md` and `research_lanes/F_economics_benchmark_evidence/NPU_EQUIVALENCE_AND_COST_CONTRACT.md`.

## INV-029 operational definition — Data Center to Phone

The project owner's highest long-term mission is to investigate whether the useful computing/service capability associated with an extraordinarily large hypothetical data-center envelope—expressed by the owner as roughly **US$10 trillion to US$100 trillion of present-era conventional infrastructure value**—can ultimately be compressed into **one phone-class physical device** with a future device price in the **tens of thousands of Thai baht**.

The US$10T–US$100T range is a **user-defined ambition/scale proxy, not a claim that a present-day individual data center has that market value**. Success must be established through concrete capability contracts: GPU/CPU/NPU compute, RAM/VRAM/HBM/storage/state services, networking/I/O, AI/HPC/application throughput, latency, reliability, persistence where required, energy/thermal constraints, device form factor and total lifecycle cost. Cloud dependence, external classical infrastructure, cryogenics and control hardware must be counted honestly rather than hidden outside the phone boundary.

All earlier 100× and 100,000,000× research targets, subsystem-replacement tracks, quantum programming, cloud-QPU experiments, device/material/manufacturing work and Lane H strategy are subordinate stepping stones toward this ultimate North Star. It remains a long-horizon falsifiable research objective, not a demonstrated capability or promised delivery date.
