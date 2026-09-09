# UQPU Open Research Roadmap

## Phase 0 — Research foundation
- [x] Define functional GPU replacement
- [x] Establish GPU workload coverage matrix
- [x] Define semantic compilation approach
- [x] Record physical and architectural barriers
- [x] Define cost-supremacy target
- [x] Open repository for public collaboration

## Phase 1 — Formal specification
- [ ] Complete UQPU Semantic IR specification
- [ ] Define workload/output contracts
- [ ] Define resource-estimation schema
- [ ] Define total-cost-per-task schema
- [ ] Expand GPU functional coverage to detailed sub-workloads

## Phase 2 — Software prototype
- [ ] Semantic workload parser
- [ ] Mathematical IR
- [ ] backend interface
- [ ] reversible-circuit fallback
- [ ] quantum simulator backend
- [ ] cost/resource estimator
- [ ] benchmark harness

## Phase 3 — First quantum-native mappings
- [ ] search
- [ ] Monte Carlo / amplitude estimation
- [ ] optimization
- [ ] linear systems
- [ ] eigenvalue workloads
- [ ] graph workloads
- [ ] quantum simulation

## Phase 4 — AI
- [ ] inference microbenchmarks
- [ ] attention experiments
- [ ] quantum model representations
- [ ] whole-graph compilation
- [ ] training experiments
- [ ] state-preparation cost analysis

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

## Phase 7 — Cost supremacy
For each workload determine whether it reaches:

- [ ] 100×
- [ ] 1,000×
- [ ] 10,000×
- [ ] 100,000×
- [ ] 1,000,000×
- [ ] 10,000,000×
- [ ] 100,000,000× moonshot

## Phase 8 — Real QPU experiments
- [ ] select available hardware
- [ ] run reproducible workloads
- [ ] compare simulator/resource model with hardware
- [ ] publish negative and positive results

## Community research tracks

Contributors can independently lead a track:

- UQPU-Compiler
- UQPU-AI
- UQPU-Graphics
- UQPU-HPC
- UQPU-Memory
- UQPU-QEC
- UQPU-Hardware
- UQPU-Cost
- UQPU-Benchmarks
- UQPU-Theory

Pull Requests that improve or challenge this roadmap are welcome.
