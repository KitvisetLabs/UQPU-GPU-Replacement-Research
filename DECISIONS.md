# Decision Log

## 2026-09-09 — D001: Define replacement at the functional level
**Decision:** UQPU does not need to reproduce GPU internal architecture or execution. It must satisfy the same end-use goals and output contracts.

**Reason:** Instruction-level emulation would unnecessarily inherit GPU computation patterns and likely erase quantum advantages.

## 2026-09-09 — D002: Require complete GPU functional-domain coverage
**Decision:** The research target includes graphics, AI, HPC, simulation, media, analytics and general parallel compute.

**Reason:** The objective is GPU replacement, not a narrow quantum accelerator.

## 2026-09-09 — D003: Permit classical control electronics but no GPU dependency
**Decision:** CPU, controllers, memory interfaces, QEC decoders and display/network I/O are allowed. A qualifying UQPU workload must not require a GPU.

**Reason:** Quantum hardware requires classical control; eliminating all classical electronics is not part of the research objective.

## 2026-09-09 — D004: Use semantic compilation
**Decision:** Compile application intent and mathematical structure to a UQPU execution plan rather than translating GPU instructions one-for-one.

**Reason:** Whole-program transformations can avoid unnecessary classical intermediates and expose quantum-native algorithms.

## 2026-09-09 — D005: Add economic supremacy as a core objective
**Decision:** Target ≥100× lower total cost per useful task versus GPU, with a moonshot target up to 100,000,000× where physically possible.

**Reason:** Functional replacement alone is insufficient for disruptive adoption.

## 2026-09-09 — D006: Treat 100,000,000× as a moonshot, not a guaranteed result
**Decision:** Extreme cost claims must be workload-specific and include full system cost.

**Reason:** Quantum advantage is problem-specific and can be erased by data loading, QEC, measurement and classical output.

## 2026-09-09 — D007: Preserve negative results
**Decision:** Failed mappings, no-advantage results and unresolved barriers remain part of the repository.

**Reason:** The project is a research program and must remain falsifiable.


## 2026-09-09 — D008: Introduce inverse design from economic targets
**Decision:** Treat 100×–100,000,000× cost goals as constraints to solve backward from measured GPU cost/task into maximum UQPU cost/task and, later, required hardware parameters.

**Reason:** This turns economic ambition into falsifiable engineering requirements instead of treating cost advantage as a narrative claim.

## 2026-09-09 — D009: Keep hardware and QEC reference profiles explicitly MODEL_ONLY
**Decision:** Generic hardware profiles and the first surface-code estimator are modeling tools only until calibrated against literature and hardware measurements.

**Reason:** Prevents hypothetical parameters from being confused with vendor specifications or demonstrated quantum advantage.


## 2026-09-09 — D010: Multi-provider quantum cloud portability is mandatory
**Decision:** All UQPU software architecture must support multiple quantum cloud providers through adapters and capability negotiation.

**Reason:** The research objective is to use available cloud QPUs as execution hardware without provider lock-in and to compare which cloud/device can best satisfy GPU-replacement workloads.

## 2026-09-09 — D011: Continuously discover new quantum cloud providers
**Decision:** Provider discovery is repeated during every development cycle. New, preview, announced and retired services are recorded rather than relying on a static provider list.

**Reason:** Quantum cloud offerings change rapidly, and new hardware/providers may alter feasibility or economics.

## 2026-09-09 — D012: Cloud execution must remain tied to the 100×–100M× economic objective
**Decision:** A successful adapter connection alone is insufficient. Real cloud-QPU execution must ultimately be benchmarked against competitive GPU cost/task using complete provider and system costs.

**Reason:** The primary project goal is functional GPU replacement with dramatic cost reduction, not merely quantum-cloud interoperability.


## 2026-09-09 — D013: Treat project mission as version invariants enforced by CI
**Decision:** Preserve cloud portability, full GPU functional scope, 100× minimum economic target, 100,000,000× moonshot, evidence discipline and provider surveillance in every version through explicit charter/invariant documents and automated tests.

**Reason:** The core mission should not silently disappear or weaken as code and community contributions evolve.


## 2026-09-09 — D014: Treat VRAM/HBM and host-memory pressure as part of GPU replacement
**Decision:** UQPU must target not only GPU compute but also the functional/economic role of accelerator-local VRAM/HBM and, where possible, reduce host-RAM and data-movement requirements.

**Reason:** Modern accelerator workloads depend heavily on memory capacity and bandwidth; excluding memory would understate the real cost and architectural burden of data-center GPU systems.

## 2026-09-09 — D015: Prefer avoiding classical materialization over one-for-one memory emulation
**Decision:** The primary memory research direction is whole-graph semantic execution that avoids large intermediate tensors/frames/states when possible, rather than assuming quantum memory must imitate HBM or DRAM exactly.

**Reason:** A quantum system is most likely to gain a system-level advantage by changing the computation/data representation, not by reproducing every classical memory transaction.


## 2026-09-09 — D016: Compare complete computing stacks, not isolated accelerator chips
**Decision:** Economic benchmarking will expand to CPU+GPU+VRAM/HBM+RAM+storage+fabric+power/cooling/operations versus the complete UQCS stack.

**Reason:** Component-only comparisons can hide costs that dominate real data-center workloads.

## 2026-09-09 — D017: Allocate economic targets backward to subsystem budgets
**Decision:** Use inverse design to divide the maximum UQCS cost/task allowed by each target tier among compute, memory, storage, fabric, control/QEC and power/operations.

**Reason:** A 100×–100M× goal becomes an actionable engineering constraint only when every subsystem has a measurable budget.


## 2026-09-09 — D018: Use inverse economic targets to drive hardware specifications
**Decision:** Hardware requirements should be derived backward from end-to-end cost/task targets rather than chosen independently.

**Reason:** This connects fidelity, power, bandwidth, yield, photonic loss and QEC resources directly to the 100×–100M× economic objective.

## 2026-09-09 — D019: Require monotonic target tightening in inverse-design models
**Decision:** As economic target tiers become more demanding, inverse-design constraints must tighten monotonically unless a model explicitly explains a non-monotonic physical effect.

**Reason:** This is a useful software invariant and exposed a defect in the first utilization/yield implementation.


## 2026-09-09 — D020: Make hardware gap analysis paradigm-aware
**Decision:** Compare provider hardware only after matching computational paradigm and workload contract. Do not rank gate-model, analog, annealing or photonic systems by raw qubit count alone.

**Reason:** A qubit count has different operational meaning across modalities and can create invalid conclusions about capability.

## 2026-09-09 — D021: Unknown provider metrics must not be treated as success
**Decision:** If a requirement needs a metric that a provider has not published or the snapshot has not verified, classify the field as unknown rather than passing the requirement.

**Reason:** This prevents missing data from being converted into fabricated capability.

## 2026-09-09 — D022: Separate roadmap targets from current hardware
**Decision:** Future announced/roadmap systems can inform inverse design and strategic planning but cannot be used as evidence of currently executable cloud capability.

**Reason:** Economic and functional claims must reflect hardware that actually exists and is accessible at the time of benchmarking.


## 2026-09-09 — D023: Add biomass as a strategic UQCS materials feedstock
**Decision:** Pangola grass and agricultural residues become a permanent materials research track for reducing UQCS/future-technology supply-chain cost.

**Reason:** Low-cost renewable carbon, cellulose, lignin and selected inorganic fractions can potentially supply electrodes, adsorbents, composites, membranes, packaging and other functional materials.

## 2026-09-09 — D024: Replace expensive elements by function, minimization, recovery or hybridization—not chemical transmutation
**Decision:** Biomass research must not claim ordinary processing creates Au, Cu, Ag, rare-earths or other absent elements. Valid pathways are functional substitution, reduced loading, recovery/recycling and hybrid structures.

**Reason:** Chemical processing rearranges atoms but does not change elemental identity. Maintaining this boundary keeps the cost-reduction program physically credible.


## 2026-09-09 — D025: Co-design UQCS devices with fabrication equipment
**Decision:** Treat chip-fabrication equipment/process architecture as part of UQCS, including DUV/EUV and alternative lithography plus deposition, etch, doping, metrology, cleaning, test and packaging.
**Reason:** A computing architecture cannot meet aggressive system economics if its manufacturing route is ignored.

## 2026-09-09 — D026: Do not default to the most advanced lithography
**Decision:** Select the least-cost fabrication route that satisfies device requirements; EUV is an option, not an invariant.
**Reason:** Quantum, photonic and heterogeneous devices may achieve system goals on mature or specialized processes with lower total cost.

## 2026-09-09 — D027: Integrate parallel fab research through shared interfaces
**Decision:** Maintain separate fab workstreams and periodically reconcile evidence, dependencies, bottlenecks, negative results and cost impact.
**Reason:** Lithography alone cannot determine manufacturability; yield and system economics emerge from the integrated process.


## 2026-09-09 — D028: Make unresolved limitations permanent research objects
**Decision:** Every blocked, failed, infeasible or unsupported research path must be represented in a living research-gap backlog with an unlock path and next experiment.
**Reason:** The project should accumulate negative knowledge instead of repeatedly rediscovering the same limitations.

## 2026-09-09 — D029: Coordinate the project through explicit workstream interfaces
**Decision:** Organize UQCS into compute/compiler, quantum/QEC, cloud, memory/storage, photonics, fabrication, packaging, biomass/materials, power/cooling, economics and evidence/integration workstreams.
**Reason:** The mission is too cross-disciplinary for isolated optimization; each workstream must expose requirements, cost, dependencies and blockers to system integration.


## 2026-09-09 — D030: Select lithography by device requirement and total economics
**Decision:** UQCS fabrication planning should choose the least-modeled-cost route that satisfies feature-size, overlay, yield, throughput and mask requirements rather than defaulting to EUV.
**Reason:** Mature DUV, nanoimprint or specialized/direct-write processes may be economically superior for quantum, photonic, control, power or packaging devices that do not need leading-edge CMOS geometry.

## 2026-09-09 — D031: Treat lithography as one element of an integrated patterning/fab system
**Decision:** No lithography route may be evaluated without eventually including resist/materials, etch, deposition, metrology, defects, yield, masks, cleaning, packaging and facility costs.
**Reason:** Published tool resolution alone is not a manufacturing-cost metric and cannot establish the project's 100× economic objective.


## 2026-09-09 — D032: Optimize fabrication by cost per good die, not tool resolution alone
**Decision:** UQCS fabrication economics will use cumulative yield and total process cost to estimate cost per good die.
**Reason:** A nominally cheaper or higher-resolution process can lose economically through low yield, excessive steps, long cycle time or high facility/process overhead.

## 2026-09-09 — D033: Rank fab bottlenecks across cost, yield, time and energy
**Decision:** Fabrication optimization should identify the highest combined process penalties rather than assuming lithography is always dominant.
**Reason:** Deposition, etch, CMP, cleaning, metrology, test or packaging may dominate a specific quantum/photonic/semiconductor process flow.


## 2026-09-09 — D034: Preserve the complete Kanusanan Pongpanna Model as a master project artifact
**Decision:** Maintain `docs/KANUSANAN_PONGPANNA_MODEL.md` as the canonical strategic master document containing the staged investment/future-industry vision, public multilingual source links, AI-agent/business-automation context, biomass strategy and UQCS integration.
**Reason:** The user's strategic plan must remain durable, public and available to every future research cycle rather than relying on chat history alone.

## 2026-09-09 — D035: Enforce strategic-plan preservation in CI and daily workflow
**Decision:** Every meaningful project version/progress cycle must preserve the master plan, all multilingual source links and README visibility; CI and daily automation will verify/require this.
**Reason:** This prevents later refactoring, contributions or long-running development from silently losing the project's strategic foundation.

## 2026-09-09 — D036: Preserve strategic intent while independently verifying evidence
**Decision:** The master plan guides research priorities and integration, but scientific, technical, financial, legal, market and vendor claims require current independent primary-source verification before being treated as verified findings.
**Reason:** Long-term strategic continuity and scientific/economic credibility must be maintained simultaneously.


## 2026-09-09 — D037: Consolidate research into six parallel lanes
**Decision:** Replace fine-grained day-to-day coordination across many independent workstreams with six stable lanes sharing one work-item contract, scoreboard and integration gate.
**Reason:** The project scope is broad enough that excessive coordination can become a bottleneck. Six lanes preserve domain separation while reducing duplicated planning and integration overhead.

## 2026-09-09 — D038: Prioritize integration/economic blockers before feature breadth
**Decision:** Rank P0 integration blockers and P1 economic bottlenecks ahead of general feature expansion, while retaining lower-priority enabling and speculative research.
**Reason:** The permanent mission is determined by end-to-end functional coverage, evidence and cost/useful-task; subsystem progress that cannot integrate should not dominate resources.

## 2026-09-09 — D039: Integrate once per research batch
**Decision:** Allow lanes to work independently against stable contracts, then perform one cross-lane integration gate at the end of a batch unless a dependency requires earlier coordination.
**Reason:** Repeated cross-checking after every small change creates avoidable overhead and makes parallel work less efficient.


## 2026-09-09 — D040: Make GitHub the canonical cross-chat project memory
**Decision:** New chats, agents, automations and contributors must reconstruct project context from the repository's canonical documents rather than depending on conversational memory.
**Reason:** Chat/session context is not a reliable permanent storage mechanism; version-controlled repository state is inspectable, shareable and auditable.

## 2026-09-09 — D041: Make the six-lane operating system a permanent invariant
**Decision:** Preserve the Parallel Simple Mode defined in `docs/RESEARCH_OPERATING_SYSTEM.md` as INV-018 and require explicit documented decisions for any future replacement.
**Reason:** The workflow must survive new chats, different AI agents, community contributions and long-running development without silently reverting to ad-hoc coordination.


## 2026-09-09 — D042: Gate fabrication by amortized cost per useful task
**Decision:** A UQCS fabrication route must be evaluated by manufacturing cost amortized over useful lifetime workload tasks, not by cost/wafer or cost/die alone.
**Reason:** The permanent economic objective is total cost/useful-task. Device count, lifetime, utilization and packaging/test can reverse conclusions drawn from raw die cost.

## 2026-09-09 — D043: Keep manufacturing-budget allocation explicit and scenario-dependent
**Decision:** Do not hard-code a universal fraction of compute budget for fabrication. Require each architecture/economic scenario to state and sensitivity-test its manufacturing allocation.
**Reason:** Quantum, photonic, semiconductor and hybrid architectures distribute cost differently across fabrication, package/test, QEC/control, memory, photonics and operations.


## 2026-09-09 — D044: Compare cloud and owned hardware using cost per useful task
**Decision:** Cloud-QPU rental and owned-UQCS deployment must use the same useful-task denominator before economic conclusions are drawn.
**Reason:** Headline per-minute, per-shot or CAPEX values are not directly comparable without workload normalization and amortization.

## 2026-09-09 — D045: Preserve dated provider pricing snapshots
**Decision:** Store quantum-cloud pricing with snapshot date and official source rather than treating provider prices as permanent constants.
**Reason:** Quantum-cloud prices and plans change; reproducible historical economics require provenance.

## 2026-09-09 — D046: Reject cross-currency comparisons without explicit FX conversion
**Decision:** Do not compare EUR and USD pricing numerically unless a dated, explicit currency conversion is supplied.
**Reason:** Silent cross-currency arithmetic can produce false cost rankings.


## 2026-09-09 — D047: Treat cloud-vs-owned deployment as a crossover under uncertainty
**Decision:** Deployment economics must be sensitivity-tested across utilization, CAPEX, runtime and other major variables rather than decided from one central scenario.
**Reason:** Small changes in utilization or lifecycle assumptions can reverse which route is cheaper.

## 2026-09-09 — D048: Use robust interval classification before deployment claims
**Decision:** Classify a route as robustly cheaper only when its high-cost estimate remains below the competing route's low-cost estimate; otherwise report uncertainty overlap.
**Reason:** This prevents fragile MODEL_ONLY assumptions from becoming false strategic conclusions.

## 2026-09-09 — D049: Require dated provenance for FX conversion
**Decision:** Currency conversion used in provider economics must carry source currency, target currency, rate, as-of date and source provenance.
**Reason:** FX is time-dependent and must be reproducible in historical cost comparisons.


## 2026-09-09 — D050: Require every integrated change to advance the original mission
**Decision:** A subsystem result should not count as integrated mission progress unless it improves functional coverage, cost/useful-task, evidence maturity, provider portability, data movement, manufacturability or removes a documented blocker.
**Reason:** The project has expanded into many disciplines; an explicit mission gate prevents scope growth from displacing the original objective.

## 2026-09-09 — D051: Use mission-impact scoring to prioritize research effort
**Decision:** Candidate work should be ranked by expected mission benefit divided by estimated effort, with P0/P1 blockers taking precedence.
**Reason:** The fastest route to the original objective is reducing the highest-value uncertainty and cost/functional bottlenecks rather than maximizing raw activity.


## 2026-09-09 — D052: Make vendor SDKs a strict adapter-only boundary
**Decision:** Provider-specific SDK/API imports must remain inside concrete adapter modules; the semantic compiler and core execution model remain provider-neutral.
**Reason:** This is required for broad cloud portability and prevents vendor SDK churn from propagating through UQCS core architecture.

## 2026-09-09 — D053: Prefer aggregator routing when it reduces duplicated provider integration
**Decision:** Hardware providers accessible through Amazon Braket or Azure Quantum may use the aggregator adapter as the primary UQPU production path, while direct adapters can be added when they provide meaningful capability/economic benefits.
**Reason:** Shared authentication, billing and job lifecycle reduce duplicated integration code without changing the underlying target hardware.

## 2026-09-09 — D054: Distinguish software readiness from real-QPU verification
**Decision:** Adapter readiness must explicitly distinguish serialization/dry-run, simulator verification, implemented real-submit code, aggregator routing and real-QPU verified execution.
**Reason:** A correct-looking integration cannot be claimed as verified hardware access without credentials, target availability, job evidence and result/cost validation.


## 2026-09-09 — D055: Make programming on existing cloud QPUs the primary project strategy
**Decision:** The first and highest-priority path is to program currently available cloud quantum computers to perform application-level CPU/GPU/RAM/VRAM/storage roles through semantic transformation, quantum algorithms and runtime orchestration.
**Reason:** The user's original intent is software-driven functional replacement using market-available cloud quantum hardware, not hardware invention as the primary prerequisite.

## 2026-09-09 — D056: Escalate to custom hardware only after a documented software/cloud blocker
**Decision:** Hardware, device physics, lithography and fabrication remain active research but are secondary unless software/cloud execution produces a measurable blocker that existing hardware cannot overcome.
**Reason:** This prevents hardware research from consuming priority before the software-first hypothesis has been tested.

## 2026-09-09 — D057: Treat memory/storage replacement as semantic state-service replacement
**Decision:** RAM, VRAM/HBM and persistent-storage goals should first be attacked by changing representation, materialization, access and persistence semantics rather than trying to recreate DRAM/HBM/disk cells inside a QPU.
**Reason:** The internal mechanism may differ; the acceptance criterion is the useful application/state contract plus end-to-end economics.


## 2026-09-09 — D058: Priority #1 means emphasis, not exclusivity
**Decision:** Quantum programming/software-first cloud-QPU execution remains Priority #1, while all established research lanes continue concurrently and must make ongoing progress.
**Reason:** The project is intentionally multidisciplinary. Priority determines scheduling emphasis and resolves resource conflicts; it must never be interpreted as permission to stop hardware, photonics, fabrication, memory/storage, biomass/materials, infrastructure or economics/evidence research.


## 2026-09-09 — D059: Expand the permanent operating architecture to seven research lanes
**Decision:** Add Lane G — Quantum Chip Manufacturing Equipment & Software — and make A–G the permanent project operating architecture.
**Reason:** Designing a manufacturable quantum chip and designing the machines/software/factory stack that can produce it are related but distinct engineering problems and require separate ownership.

## 2026-09-09 — D060: Separate chip/process design from manufacturing-equipment design
**Decision:** Lane D owns quantum/photonic/semiconductor device and chip architecture, process requirements, fabrication/packaging and manufacturability. Lane G owns manufacturing machines, tooling, production software, process-control/EDA systems, metrology, automation, characterization and factory systems. D and G co-design continuously.
**Reason:** The separation improves research accountability while retaining cross-lane integration.

## 2026-09-09 — D061: Every cycle must explicitly recognize all seven lanes
**Decision:** Every research/daily cycle must inspect A–G. Lane A receives Priority #1 emphasis, while B–G continue research and progress in parallel.
**Reason:** The seven-lane structure is project memory and must remain stable across chats, agents and scheduled runs.


## 2026-09-09 — D062: Expand the permanent operating architecture to eight research lanes
**Decision:** Add Lane H — Ketskaew Chulamani / Kanusanan Pongpanna Model Strategic Development, Finance & Future-Industry Research — making A–H the permanent project architecture.
**Reason:** The master development/financial plan is not merely a reference document; it is an independent living research program requiring continuous deepening, feasibility analysis, article expansion and public GitHub publication.

## 2026-09-09 — D063: Lane H continuously publishes research while preserving evidence boundaries
**Decision:** Lane H must progressively publish research notes/articles/roadmaps derived from the plan, preserve multilingual source references, and distinguish evidence, forecasts, hypotheses, speculative technologies, personal/religious vision and targets.
**Reason:** Continuous publication supports open collaboration while evidence labels prevent aspirational or belief-based material from being mistaken for demonstrated scientific results.

## 2026-09-09 — D064: Every cycle explicitly recognizes A–H
**Decision:** Every research/daily cycle must inspect all eight lanes. Lane A remains Priority #1; B–H continue progress in parallel.


## 2026-09-09 — D065: Require an artifact or explicit reviewed status from every lane in integrated batches
**Decision:** Integrated A–H research batches should produce a concrete artifact, tested model, evidence update or explicit blocker/review result for every lane.
**Reason:** The eight-lane architecture should create measurable progress rather than merely exist as an organizational diagram.

## 2026-09-09 — D066: Make the first verified cloud-QPU workload win the primary cross-lane milestone
**Decision:** The highest-value near-term integration milestone is a reproducible workload contract carried from classical baseline through current cloud-QPU/hybrid execution to validated output and total cost/useful-task.
**Reason:** This is the shortest evidence path from software architecture toward the original functional/economic mission.


## 2026-09-09 — D067: Require REAL_QPU evidence before calling a workload a verified quantum win
**Decision:** MODEL_ONLY, SIMULATION and DRY_RUN results may guide research but cannot satisfy the verified-win gate. A verified win requires real-QPU execution, accepted output quality and measured end-to-end economics.
**Reason:** This prevents software models or simulator performance from being confused with demonstrated cloud-QPU advantage.

## 2026-09-09 — D068: Add provider throughput as a first-class routing/economics variable
**Decision:** Provider selection should eventually include circuit/reset/repetition throughput in addition to qubit count, fidelity, modality and headline price.
**Reason:** IBM's Nighthawk r2 illustrates that a system with similar/smaller qubit scale can materially change useful-work economics through much higher throughput.

## 2026-09-09 — D069: Lane H uses stage gates instead of assuming automatic industrial progression
**Decision:** Transitions in the Kanusanan Pongpanna Model should be analyzed through explicit technical, market, cash-flow and financing gates.
**Reason:** Success in agriculture/biomass does not automatically make semiconductor/quantum investment economically feasible; each transition requires evidence.


## 2026-09-09 — D070: Benchmark the useful workload contract, not an isolated quantum kernel
**Decision:** A First Verified Win benchmark must include workload semantics, provider modality fit, state/I/O accounting, output quality and total cost/useful-task.
**Reason:** Kernel-only quantum performance can hide input preparation, state movement, retries and reconstruction costs.

## 2026-09-09 — D071: Make device/factory co-design use a measurable shared contract
**Decision:** Lane D must supply critical device/process/test requirements to Lane G, and Lane G must return equipment capability, throughput, yield, cost and blocker information.
**Reason:** Separating chip architecture from equipment research without a formal interface creates unusable manufacturing studies.

## 2026-09-09 — D072: Derive Lane E material research from system functions
**Decision:** Biomass/advanced-material candidates must map to defined computing/fabrication/infrastructure functions and qualification requirements.
**Reason:** Functional requirements make substitution research economically and scientifically testable.

## 2026-09-09 — D073: Scale research capital by evidence and uncertainty reduction
**Decision:** Lane H capital-allocation research should preserve all eight lanes while giving larger marginal funding to experiments that reduce mission-critical uncertainty most efficiently.
**Reason:** Equal funding by organizational lane is not automatically optimal.


## 2026-09-09 — D074: Use a baseline ladder and prohibit toy-baseline advantage claims
**Decision:** Classical benchmarking progresses from correctness fixture to optimized CPU and competitive multicore/GPU baselines before serious economic comparison.
**Reason:** A quantum system compared only against naive Python would create a meaningless advantage ratio.

## 2026-09-09 — D075: Capture classical-baseline provenance before cost claims
**Decision:** Runtime evidence must record implementation, platform/hardware context, workload objective and cost methodology.
**Reason:** Cost/useful-task cannot be reproduced from an unlabeled timing number.

## 2026-09-09 — D076: Convert cross-lane interfaces into reusable schemas
**Decision:** D/G and E research must use structured requirement/qualification templates when moving from concept to measurable engineering.
**Reason:** Templates reduce ambiguity and make later automation/agent parallelization safer.


## 2026-09-09 — D077: Freeze benchmark semantics with stable contract IDs
**Decision:** Classical and quantum comparisons must share a canonical workload contract whose identity changes when benchmark semantics change.
**Reason:** This prevents accidental advantage claims caused by comparing different instances, quality tolerances or objective definitions.

## 2026-09-09 — D078: Use scalable seeded instances before provider execution
**Decision:** Candidate optimization workloads require reproducible scalable instance generation before simulator or real-QPU economic comparisons.
**Reason:** Tiny fixtures validate correctness but cannot establish realistic scaling or economics.


## 2026-09-09 — D079: Treat benchmark tiers as revisable research hypotheses
**Decision:** Batch tier sizes/densities are versioned research starting points and may change when measured CPU/GPU/QPU scaling evidence warrants it.
**Reason:** Freezing arbitrary early sizes as permanent benchmarks would optimize the project around an unvalidated workload envelope.

## 2026-09-09 — D080: Preserve unknown measurement fields as unknown
**Decision:** Missing energy, transfer, memory or cost measurements must remain null/unknown rather than being silently imputed in measured benchmark artifacts.
**Reason:** Separating measurement from modeling is necessary for credible end-to-end advantage claims.


## 2026-09-09 — D081: Make invariant CI compare canonical documents rather than hard-code project age
**Decision:** Project invariant tests should derive the current invariant set from canonical repository documents and verify required minimum/current markers instead of assuming the project permanently stops at a fixed invariant number.
**Reason:** The previous hard-coded INV-018/six-lane assumptions became a false failure after documented evolution to INV-024/eight lanes.

## 2026-09-09 — D082: Keep competitive solver dependencies optional
**Decision:** Established benchmark solvers such as OR-Tools belong in an optional benchmark dependency set rather than the UQPU core runtime.
**Reason:** Provider/runtime portability should not require heavyweight classical benchmark packages, while evidence work still needs credible competitor solvers.


## 2026-09-09 — D083: Execution success is not output-quality acceptance
**Decision:** A benchmark runner may record that execution completed, but accepted=true must ultimately be derived from a contract quality check against a defensible reference/bound.
**Reason:** Conflating process success with solution quality would create false benchmark wins.


## 2026-09-09 — D084: Require a reference certificate before benchmark acceptance
**Decision:** Tier runner artifacts default to accepted=false unless the workload contract is paired with a matching objective reference certificate.
**Reason:** This implements D083 in code and prevents execution success from being mistaken for solution-quality success.

## 2026-09-09 — D085: Distinguish best-known feasible values from proof-quality references
**Decision:** BEST_KNOWN_FEASIBLE may support comparison but cannot produce verified-quality status; EXACT_OPTIMUM or a valid PROVEN_LOWER_BOUND is required for certified minimization-gap evidence.
**Reason:** A feasible incumbent is not a proof of distance from the true optimum.

## 2026-09-09 — D086: Compare materials on functional units
**Decision:** Lane E cost comparisons must normalize to the delivered function and reliability requirement rather than feedstock mass price alone.
**Reason:** Processing, loading, durability and replacement frequency can reverse apparent raw-material savings.


## 2026-09-09 — D087: Solver status controls reference proof strength
**Decision:** The reference generator emits EXACT_OPTIMUM only from an optimized solver result explicitly reporting proven optimality. A feasible time-limited result is recorded as BEST_KNOWN_FEASIBLE.
**Reason:** A strong incumbent is useful but is not proof of the global optimum.

## 2026-09-09 — D088: Reference manifests must carry execution provenance
**Decision:** Reference artifacts record stable certificate/contract IDs, method, evidence level, source, runtime, solver status and proven-optimal flag.
**Reason:** QPU quality comparisons must be reproducible against the same reference evidence rather than an undocumented objective number.
