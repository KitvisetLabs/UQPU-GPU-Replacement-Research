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
| INV-030 | Pangola/biomass carbon innovation is a permanent strategic pillar for replacing, minimizing or recovering expensive technology minerals/materials across the full industrial stack | Yes |
| INV-031 | Ultra-low-cost biomass-derived bio-oil/biofuel is a permanent strategic pillar; compare accepted liquid-energy/fuel function with full process, upgrading, logistics, coproduct and financing cost | Yes |
| INV-032 | Ultra-low-cost fusion electricity is a permanent strategic pillar; judge success by net reliable delivered electricity and full lifecycle/financing cost, not fusion gain alone | Yes |
| INV-033 | Interest-cost/R&D-finance compression is a permanent strategic pillar: reduce required principal, financing duration and project risk; any reduction in financing rate/WACC itself requires separate evidence | Yes |
| INV-034 | Foundational Physics & Mathematics Deep-Frontier Agenda: research may descend from logic/mathematics through information theory, quantum foundations, QFT/elementary-particle physics and other sciences, then climb to devices/engineering/systems under explicit mechanism, constraints, scaling and falsification gates | Yes |
| INV-035 | AI-Assisted Physics Equation Discovery: maximize imagination for candidate equations/models while requiring dimensional, symmetry/conservation/causality, held-out-prediction, falsification and independent-evidence gates before physical-law or technology claims | Yes |
| INV-036 | Difference-to-Technology Particle/Spacetime Principle: systematically search controllable/readable differences across particle, antiparticle, dark-sector, spacetime/gravity and material-defect scales; preserve the Pangola/biomass-carbon -> synthetic-diamond hypothesis under explicit material/device/economic falsifiers | Yes |

## INV-028 operational definition

The canonical lane-oriented workspace is `research_lanes/`, containing one clearly separated folder for each permanent lane A–H. Future special projects may create nested subfolders under the owning lane or under `integration/`, but repository paths must never exceed **16 directory levels from repository root**. Every substantive artifact has one primary owning lane; shared work uses cross-lane contracts and stable references rather than unnecessary duplication. Existing canonical code/docs may migrate incrementally when moving them can be done without breaking imports, links, reproducibility identifiers, tests or CI. Research direction must maximize scientifically defensible integration among all eight lanes around common useful-output, feasibility and total-cost objectives. See `research_lanes/README.md`, `research_lanes/LANE_DIRECTORY_POLICY.md` and `integration/LANE_INTERFACE_CONTRACT.md`.

## NPU scope clarification

NPU is a permanent accelerator-replacement target alongside GPU and CPU. NPU claims must use neural-workload equivalence contracts—model/checkpoint, precision/quantization, task quality, batch/sequence/input shape, latency, throughput, memory/data movement and total cost—not headline TOPS alone. The permanent detailed tracks are `research_lanes/A_quantum_programming_runtime/NPU_REPLACEMENT_TRACK.md` and `research_lanes/F_economics_benchmark_evidence/NPU_EQUIVALENCE_AND_COST_CONTRACT.md`.

## INV-029 operational definition — Data Center to Phone

The project owner's highest long-term mission is to investigate whether the useful computing/service capability associated with an extraordinarily large hypothetical data-center envelope—expressed by the owner as roughly **US$10 trillion to US$100 trillion of present-era conventional infrastructure value**—can ultimately be compressed into **one phone-class physical device** with a future device price in the **tens of thousands of Thai baht**.

The US$10T–US$100T range is a **user-defined ambition/scale proxy, not a claim that a present-day individual data center has that market value**. Success must be established through concrete capability contracts: GPU/CPU/NPU compute, RAM/VRAM/HBM/storage/state services, networking/I/O, AI/HPC/application throughput, latency, reliability, persistence where required, energy/thermal constraints, device form factor and total lifecycle cost. Cloud dependence, external classical infrastructure, cryogenics and control hardware must be counted honestly rather than hidden outside the phone boundary.

All earlier 100× and 100,000,000× research targets, subsystem-replacement tracks, quantum programming, cloud-QPU experiments, device/material/manufacturing work and Lane H strategy are subordinate stepping stones toward this ultimate North Star. It remains a long-horizon falsifiable research objective, not a demonstrated capability or promised delivery date.

## INV-030 operational definition — Pangola/Biomass Carbon Strategic Pillar

The project permanently prioritizes research into **carbon-rich materials and carbon powders derived from Pangola grass and diverse agricultural residues**, including solid-carbon/char streams produced through thermochemical conversion and carbonaceous streams associated with bio-oil production, upgrading and distillation/refining where scientifically applicable.

The strategic objective is to use purification, activation, graphitization, heteroatom doping, nanostructuring, composites, coatings, membranes and other carbon-material innovations to **replace the required function, minimize the required loading, enable recovery/recycling, or redesign away dependence** on expensive or supply-constrained technology materials. Priority comparison families include gold (Au), copper (Cu), silver (Ag), lithium (Li), cobalt (Co), nickel (Ni), rare-earth elements and other high-value/critical minerals used across electronics, semiconductors, quantum/photonics, batteries, power systems, AI/data centers, robotics, aerospace and future infrastructure.

This invariant does not assert elemental transmutation or universal one-for-one substitution. Ordinary carbon processing does not create Au, Cu, Ag, Li, Co, Ni or rare-earth atoms. For every target material the project must identify the **specific incumbent function**—for example electrical conduction/contact, electrochemical ion carrier, catalytic activity, magnetic/optical behavior, thermal spreading, structural support or adsorption—and test the biomass-carbon route against that functional unit. When direct carbon substitution is physically unsuitable, the required research route is critical-material minimization, hybridization, recovery/recycling, chemistry/architecture substitution or system-level elimination.

The canonical public strategy is `01_PANGOLA_BIOMASS_CARBON_TECHNOLOGY_STRATEGY.md`. INV-030 is a central enabling strategy for INV-029 because extreme data-center-to-phone compression also requires radical reductions in material cost, supply-chain burden, energy, cooling, packaging and manufacturability.

## INV-031 operational definition — Ultra-Low-Cost Biomass Bio-Oil / Biofuel

The project permanently researches how Pangola grass and other abundant biomass/agricultural residues can be converted into **the lowest-cost defensible useful liquid-energy product or refinery-compatible intermediate**. Candidate pathways include fast/catalytic pyrolysis, hydrothermal liquefaction where suitable, gasification-derived liquids, refinery co-processing and integrated liquid-plus-carbon coproduct systems.

Cost must be normalized to accepted product quality and energy/service function. Required accounting includes feedstock collection and moisture/preprocessing, conversion yield, upgrading/hydrogen/catalyst demand, utilities, CAPEX/OPEX, uptime, storage/logistics/distribution, financing and defensible non-double-counted coproduct credits. Crude pyrolysis liquid volume alone is not equivalent to finished diesel/gasoline/jet fuel or refinery feedstock.

The canonical public strategy is `02_ULTRA_LOW_COST_BIOMASS_BIO_OIL_STRATEGY.md`. INV-031 is **ACTIVE RESEARCH / NOT_YET_DEMONSTRATED_AT_TARGET_COST**.

## INV-032 operational definition — Fusion Electricity Cost Minimization

Fusion is a permanent strategic energy pillar. The objective is not merely ignition, plasma gain or gross thermal output; it is to minimize **net reliable delivered electricity cost** while meeting safety, reliability, maintainability and manufacturability requirements.

Every serious fusion-economic comparison must account for net output after recirculating power, capacity factor, plant CAPEX, construction duration, magnets/lasers/pulsed-power systems, fuel cycle, blanket/divertor/chamber lifetime, neutron/material damage where applicable, component replacement, remote maintenance, power conversion, cooling, grid/interconnect, decommissioning, financing and uncertainty. Present roadmaps or simulations cannot be represented as commercial cheap electricity.

The canonical public strategy is `03_FUSION_ELECTRICITY_COST_STRATEGY.md`. INV-032 is **ACTIVE LONG-HORIZON RESEARCH / COMMERCIAL LOW-COST FUSION NOT_YET_DEMONSTRATED**.

## INV-033 operational definition — Interest-Cost and R&D-Finance Compression

The project permanently treats financing burden as a first-class engineering/economic objective. Reducing technology, material, fuel, electricity, factory and infrastructure costs can directly reduce required **CAPEX, OPEX, working capital and financed principal**, and therefore reduce absolute interest expense when borrowing terms are otherwise unchanged. Shorter construction and evidence cycles can also reduce the time capital remains tied up.

Lower technical/commercial risk and stronger cash-flow coverage may reduce a project's risk premium or WACC if lenders/investors recognize the improvement, but this second-order effect requires separate evidence. The repository must never claim that cheaper technology or energy automatically lowers central-bank policy rates or economy-wide interest rates, which also depend on inflation, monetary policy, sovereign/currency risk, market structure and credit conditions.

The canonical public strategy is `04_INTEREST_COST_AND_RND_FINANCE_STRATEGY.md`. Every large future research/industrial program should progressively measure financed principal, rate/WACC assumptions, tenor, construction/evidence duration, total interest, capital-at-risk per evidence milestone and lifecycle financing cost per accepted useful service.

## INV-034 operational definition — Foundational Physics & Mathematics Deep-Frontier Agenda

The project permanently treats **foundational mathematics and fundamental physics as an active upstream research layer**, not as an emergency appendix. Research may descend from formal logic, proof, computability and advanced mathematics through information/complexity theory, quantum information, quantum thermodynamics, QFT and elementary-particle physics, AMO/condensed-matter/many-body/photonics, materials and chemistry, then climb through device physics, fabrication, control, algorithms, architecture, systems, energy and economics toward every project target.

Every deep-frontier hypothesis must provide a mathematical formulation, causal physical mechanism, mission bottleneck, known-constraint analysis, scaling law, falsifier, observable, baseline, resource accounting and governed evidence label. Established constraints such as thermodynamics, causality, no-cloning, measurement/readout limits, state preparation and energy-time bounds may not be hand-waved away. A mathematical possibility is not automatically physical realizability; physical realizability is not automatically engineering feasibility; engineering feasibility is not automatically economic advantage.

The canonical public directive is `05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md`. This operationalizes and makes highly visible the broader open-frontier mandate of INV-027. It is **ACTIVE PERMANENT RESEARCH**, while any individual beyond-established-physics hypothesis remains CONCEPT/THEORY until discriminating evidence supports it.

## INV-035 operational definition — AI-Assisted Physics Equation Discovery

The project permanently uses mathematics, scientific literature, computation and AI to generate, recover, stress-test and falsify candidate equations and effective models. Imagination may be broad during hypothesis generation, but every candidate must identify which incumbent assumption changes and must pass the applicable dimensional, symmetry, conservation, causality, limiting-case, scaling, held-out-prediction, counterexample and discriminating-experiment/proof checks before promotion.

A human- or AI-generated equation is not a new physical law because it is elegant or fits a training dataset. Independent evidence is required. The canonical public directive is `06_AI_ASSISTED_PHYSICS_EQUATION_DISCOVERY.md`, with the highest-visibility companion `00A_PERMANENT_AI_EQUATION_DISCOVERY_PRINCIPLE.md`.

## INV-036 operational definition — Difference-to-Technology Particle/Spacetime Principle

The project permanently treats a **reproducible measurable difference** as a technology-search starting point. Binary 0/1 states motivate the heuristic, which is extended to spin, charge, flavour, particle/antiparticle structure, matter/antimatter comparison, field amplitude, phase/frequency, energy level, spacetime/gravity, symmetry sector, material defect and other measurable differences.

The required engineering chain is:

```text
ΔX
-> distinguishability
-> preparation
-> control
-> retention / coherence / stability
-> readout
-> useful function
-> scaling/resources
-> falsifier
-> independent reproduction
```

When `ΔX` is an energy difference, the project uses `ΔE = E_final - E_initial`; INV-036 does not claim that all abstract differences are literally energy or establish a new physical law.

Mandatory research coverage includes quark/gluon spin and QCD structure, antiparticles/antimatter, dark-matter detector technology, dark-energy/cosmology measurement technology, spacetime/gravity and relativistic clock differences, extra-dimension/quantum-gravity falsifiable searches, diamond/color-center spin defects, and other credible particle/quantum-state routes. Detector technology must not be confused with control of the detected phenomenon.

INV-036 also permanently links INV-030's Pangola/agricultural-residue carbon program to a falsifiable synthetic-diamond route: defined biomass carbon stream -> characterization/purification -> suitable HPHT/CVD precursor -> verified diamond phase/crystal quality -> intentional defect engineering -> ODMR/accepted state readout -> coherence/sensitivity/device metric -> lifecycle energy and cost comparison. The exact Pangola-residue-to-device-grade-diamond chain remains an unproven material hypothesis until experimentally demonstrated.

Canonical documents:
- `00C_DIFFERENCE_TO_TECHNOLOGY_PARTICLE_SPACETIME_PRINCIPLE.md`
- `research_lanes/D_device_chip_fabrication/batches/BATCH_045_FND_008_DIFFERENCE_PARTICLE_SPACETIME_TECHNOLOGY.md`
- `research_lanes/E_materials_energy_cooling/PANGOLA_BIOMASS_TO_SYNTHETIC_DIAMOND_RESEARCH_ROUTE.md`

INV-036 is **ACTIVE PERMANENT RESEARCH / NO PARTICLE-SPACETIME OR PANGOLA-DIAMOND TECHNOLOGY ADVANTAGE YET DEMONSTRATED**.
