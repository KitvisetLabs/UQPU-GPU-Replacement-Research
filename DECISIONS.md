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
