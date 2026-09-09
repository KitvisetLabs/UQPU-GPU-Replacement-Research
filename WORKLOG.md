# UQPU Work Log

## 2026-09-09

### Project conception
Defined the core objective: design a QPU-like architecture that can replace the **functional goals** of GPUs without requiring the same internal process.

### Functional scope established
Identified target domains including graphics, rendering, AI, matrix/tensor workloads, HPC, simulation, analytics, signal processing, media, optimization and general-purpose parallel compute.

### Architecture direction
Proposed the Universal Quantum Processing Unit (UQPU) as a quantum-first heterogeneous accelerator with semantic compilation, quantum-native execution, reversible fallback, measurement/decoding, memory/I/O and QEC as first-class components.

### Compiler direction
Established a semantic compiler model:
application intent -> mathematical IR -> backend selection -> quantum/reversible execution.

### Feasibility framing
Recorded major barriers: state preparation, classical input/output lower bounds, measurement, reversible arithmetic overhead, latency, fault tolerance and cost.

### Repository creation
Research repository established at:
https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research

Repository verified public.

### Authorship
Lead Researcher: Kanutsanan Pongpanna  
AI Research Collaborator: OpenAI GPT-5.6 Sol

### Economic objective added
Added a primary target of at least **100× lower total cost per useful task** than GPU and a workload-specific moonshot target of **100,000,000×**.

### Process documentation
Added project goals, research/engineering process, decision log and work log so future changes can be traced.

## Next research work

- create formal cost model spreadsheets/data structures
- build per-workload resource estimators
- add semantic IR specification
- design prototype runtime and backend interface
- implement first reversible fallback kernels
- implement first quantum-native benchmark candidates
- compare against real GPU baselines
- identify which workload classes can realistically approach 100× and which cannot


### Software prototype v0.2
Implemented the first executable UQPU software prototype under `software/uqpu-prototype/`.

Implemented:
- semantic workload IR and result contracts
- quantum-native backend estimator
- reversible deterministic fallback estimator
- end-to-end cost model
- semantic compiler/backend selection
- benchmark classifications
- 100×–100,000,000× cost tiers
- JSON workload input
- CLI
- unit tests
- GitHub Actions continuous integration

### Verification cycle
Development iteration 1:
- implemented initial prototype
- ran 6 unit tests
- result: 6/6 passed
- inspected benchmark output

Issue discovered:
- hypothetical cost estimates could be misread as experimentally demonstrated advantage.

Development iteration 2:
- added mandatory `MODEL_ONLY` evidence labels
- added confidence values
- added explicit cost-supremacy tiers
- added JSON workload ingestion
- expanded tests

Verification:
- ran 9 unit tests
- result: 9/9 passed
- CLI smoke test passed

Scientific note:
A demonstration Monte Carlo model produced a hypothetical >100× cost ratio, but this remains a low-confidence MODEL_ONLY result. It is not accepted as physical quantum advantage until resource assumptions are calibrated against literature and hardware.

### Continuous verification
Added GitHub Actions CI to test Python 3.10, 3.11 and 3.12 on prototype changes and Pull Requests.

Next development iteration:
- replace heuristic QPU resource assumptions with configurable hardware profiles
- add surface-code/QEC model
- add measured GPU-baseline schema
- add sensitivity/uncertainty analysis
- add first literature-backed quantum algorithm estimator


### Software prototype v0.3 — hardware/QEC/economic modeling
Implemented the next development layer:

- configurable quantum hardware profiles
- generic GPU hardware/economic profiles
- phenomenological surface-code QEC estimator
- physical-qubit accounting
- GPU cost-per-task baseline model
- sensitivity sweep engine
- inverse cost-target solver for 100× through 100,000,000×
- MODEL_ONLY reference profiles

Verification:
- 11 new local tests passed
- cumulative repository test inventory: 20 tests
- GitHub Actions remains configured for Python 3.10/3.11/3.12 integration testing

Scientific guardrails:
- reference hardware profiles are explicitly MODEL_ONLY
- QEC model is phenomenological and not vendor-calibrated
- cost-target solver computes required UQPU budget; it does not claim the target is physically achievable

Next iteration:
- inverse hardware design solver
- uncertainty distributions / Monte Carlo sensitivity
- measured GPU baseline ingestion
- literature-backed algorithm-specific resource models
- QEC model alternatives and calibration hooks


### Multi-provider quantum cloud portability becomes a core requirement
Expanded UQPU from a provider-agnostic research concept into a market-aware cloud execution architecture.

Implemented:
- provider registry
- active / preview / announced / retired lifecycle states
- paradigm classification: gate model, analog, annealing, photonic, hybrid
- capability negotiation
- provider adapter interface
- initial market registry covering IBM Quantum, Amazon Braket, Azure Quantum, IonQ, Rigetti QCS, D-Wave Leap, IQM Resonance, Quantinuum Nexus, Pasqal Cloud, QuEra/Bloqade, Quandela Cloud and OQC Cloud
- preview tracking for Quantum Circuits on Azure
- cloud-compatibility tests
- documentation defining CLOUD-L0 through CLOUD-L5 validation maturity

Market surveillance rule:
At every development cycle, check official provider/cloud documentation for new providers, hardware targets, previews, retirements, SDK/API changes and pricing/access changes. Update registry and adapter plans accordingly.

Economic rule:
A cloud connection is not considered strategically successful merely because execution works. Every real-QPU integration should progress toward a measured GPU-vs-QPU cost/task benchmark, targeting at least 100× lower cost/task and up to 100,000,000× as a workload-specific moonshot.

Current status:
Provider registry entries are architecture metadata. Real paid QPU submission adapters are not yet enabled by default and will require credentials/budget plus provider-specific validation.
