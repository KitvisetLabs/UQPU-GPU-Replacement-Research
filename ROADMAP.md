# UQPU Open Research Roadmap

## Ultimate destination — Data Center to One Phone

All phases in this roadmap are stepping stones toward the permanent long-term objective defined in `00_ULTIMATE_NORTH_STAR_DATA_CENTER_TO_PHONE.md`: investigate whether an extreme conventional data-center-scale useful-capability envelope can ultimately be compressed into **one phone-class physical device** costing only **tens of thousands of Thai baht**.

The project owner uses roughly **US$10 trillion to US$100 trillion** of present-era conventional infrastructure value as an ambition-scale proxy. This is not asserted as the valuation of one real data center. Progress must be measured by concrete service/capability contracts rather than dollar value alone.

Because the necessary breakthroughs are unknown, this roadmap is **evidence-gated rather than calendar-promised**. Each phase unlocks the next only when its acceptance criteria are supported by reproducible evidence.

## Phase 0 — Research foundation
- [x] Define functional GPU replacement
- [x] Establish GPU workload coverage matrix
- [x] Define semantic compilation approach
- [x] Record physical and architectural barriers
- [x] Define cost-supremacy target
- [x] Open repository for public collaboration
- [x] Expand permanent target scope to CPU, NPU, RAM, VRAM/HBM and persistent storage
- [x] Publish ultimate data-center-to-phone North Star

## Phase 1 — Formal specification
- [ ] Complete UQPU Semantic IR specification
- [ ] Define workload/output contracts
- [ ] Define CPU/GPU/NPU equivalence contracts
- [ ] Define RAM/VRAM/HBM/storage state-service contracts
- [ ] Define resource-estimation schema
- [ ] Define total-cost-per-task schema
- [ ] Define integrated data-center useful-service contract families

## Phase 2 — Software prototype
- [ ] Semantic workload parser
- [ ] Mathematical IR
- [ ] backend interface
- [ ] reversible-circuit fallback
- [ ] quantum simulator backend
- [ ] cost/resource estimator
- [ ] benchmark harness
- [ ] subsystem-elimination/materialization-avoidance optimizer

## Phase 3 — First quantum-native mappings
- [ ] search
- [ ] Monte Carlo / amplitude estimation
- [ ] optimization
- [ ] linear systems
- [ ] eigenvalue workloads
- [ ] graph workloads
- [ ] quantum simulation

## Phase 4 — AI / NPU replacement research
- [ ] inference microbenchmarks
- [ ] attention experiments
- [ ] quantum model representations
- [ ] whole-graph compilation
- [ ] training experiments
- [ ] state-preparation cost analysis
- [ ] competitive NPU baseline contracts
- [ ] accepted-output latency/throughput/quality comparison

## Phase 5 — Graphics and media
- [ ] quantum ray/path sampling
- [ ] light-transport experiments
- [ ] framebuffer-output analysis
- [ ] quantum-assisted reconstruction
- [ ] codec search/optimization
- [ ] deterministic standards-compliant fallback

## Phase 6 — Fault-tolerant resource study
- [ ] logical qubit estimates
- [ ] non-Clifford resource estimates
- [ ] QEC models
- [ ] physical-qubit estimates
- [ ] runtime estimates
- [ ] energy estimates
- [ ] control/cryogenic/form-factor budget

## Phase 7 — Cost supremacy and 100-million-unit compression
For each workload/subsystem determine whether it reaches:

- [ ] 100×
- [ ] 1,000×
- [ ] 10,000×
- [ ] 100,000×
- [ ] 1,000,000×
- [ ] 10,000,000×
- [ ] 100,000,000× moonshot
- [ ] approximately 100,000,000-unit GPU/CPU/NPU/RAM/VRAM/storage useful-function replacement where a defensible contract exists

## Phase 8 — Real QPU experiments
- [ ] select available hardware
- [ ] run reproducible workloads
- [ ] compare simulator/resource model with hardware
- [ ] publish negative and positive results
- [ ] capture job IDs, quality, retries, billed cost and classical support requirements

## Phase 9 — Integrated node/rack replacement
- [ ] integrate compute + memory/state + storage + network/I/O contracts
- [ ] demonstrate useful multi-service workloads
- [ ] measure external classical dependencies
- [ ] measure total energy/thermal/lifecycle cost

## Phase 10 — Data-center-class service compression
- [ ] define representative data-center service portfolios
- [ ] demonstrate increasing service coverage under identical accepted-output contracts
- [ ] measure throughput, latency, reliability, persistence and recovery
- [ ] quantify physical-volume and infrastructure compression

## Phase 11 — Extreme data-center-scale envelope
- [ ] translate the owner-defined US$10T–US$100T ambition proxy into concrete hardware/service/capability baselines
- [ ] test whether integrated UQPU/UQCS architecture can cover those capability classes
- [ ] preserve rigorous impossibility/negative results where physical limits prevent a target

## Phase 12 — Phone-class physical integration
- [ ] complete compute/state/storage/control/interconnect device boundary
- [ ] eliminate hidden remote-data-center dependence for the ultimate physical-compression claim
- [ ] satisfy phone-class volume/mass/thermal/power constraints
- [ ] validate reliability, persistence and recovery contracts

## Phase 13 — Affordable end-user economics
- [ ] target a future device price in the tens of thousands of Thai baht
- [ ] include manufacturing yield, packaging, maintenance, energy and lifecycle cost
- [ ] independently reproduce capability and economic claims

## Community research tracks

Contributors can independently lead a track:

- UQPU-Compiler
- UQPU-AI / NPU Replacement
- UQPU-Graphics
- UQPU-HPC
- UQPU-Memory / Storage
- UQPU-QEC
- UQPU-Hardware
- UQPU-Cost
- UQPU-Benchmarks
- UQPU-Theory
- UQPU-Data-Center-to-Phone Integration

Pull Requests that improve or challenge this roadmap are welcome.
