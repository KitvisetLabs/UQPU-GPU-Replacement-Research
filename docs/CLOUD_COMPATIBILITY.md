# UQPU Quantum Cloud Compatibility Architecture

## Core requirement

Every UQPU software component must be designed so workloads can be executed through multiple quantum cloud providers, not a single vendor.

The target is **functional portability plus economic optimization**:

1. express workload once in UQPU Semantic IR;
2. discover compatible quantum clouds/devices;
3. lower to provider-specific representations;
4. run on simulator and then real cloud QPU when credentials/budget are available;
5. normalize results;
6. compare end-to-end cost/task against GPU;
7. pursue at least 100× lower cost/task, with workload-specific moonshot up to 100,000,000×.

## Market-aware provider coverage

Initial target registry includes:

- IBM Quantum
- Amazon Braket
- Microsoft Azure Quantum
- IonQ direct
- Rigetti QCS
- D-Wave Leap
- IQM Resonance
- Quantinuum Nexus
- Pasqal Cloud
- QuEra / Bloqade
- Quandela Cloud
- OQC Cloud
- preview/announced providers such as Quantum Circuits on Azure

The registry is not considered complete forever. Provider discovery is an ongoing project obligation.

## Cloud aggregation routes

Amazon Braket provides access to multiple hardware vendors and paradigms. Current AWS documentation lists gate-based devices from AQT, IonQ, IQM and Rigetti, plus QuEra analog hardware.

Azure Quantum currently lists IonQ, Pasqal, Quantinuum and Rigetti, with Microsoft documentation also listing Quantum Circuits as coming soon/private preview.

## Capability negotiation

UQPU must not force all providers into a lowest-common-denominator circuit interface.

Instead:

```text
UQPU Semantic IR
    |
    v
Execution Requirements
    |
    +--> Gate model
    +--> Analog
    +--> Annealing / QUBO
    +--> Photonic
    +--> Hybrid
    |
    v
Provider Registry + live capability discovery
    |
    v
Provider-specific lowering
    |
    v
Cloud submission
```

## Required provider metadata

Each provider/device profile should expose:

- provider status: active / preview / announced / retired
- paradigm
- qubit/mode count
- native gate set
- topology/connectivity
- mid-circuit measurement
- reset
- classical feed-forward
- dynamic circuits
- pulse control
- analog Hamiltonian support
- QUBO/Ising support
- photonic/Fock support
- batch/session/reservation support
- simulator availability
- accepted program formats
- result formats
- pricing model
- queue/availability
- region
- credentials/access model

## Adapter rule

Provider SDK imports must live behind provider adapters only.

Core compiler modules must not directly import Qiskit Runtime, Braket SDK, Azure Quantum SDK, pyQuil, Ocean, Perceval, Pulser, Bloqade, qnexus, or any other vendor package.

## Compatibility validation levels

- **CLOUD-L0** — provider listed and documented
- **CLOUD-L1** — adapter serialization/dry-run works
- **CLOUD-L2** — provider simulator execution verified
- **CLOUD-L3** — real QPU smoke test verified
- **CLOUD-L4** — reproducible benchmark with normalized result
- **CLOUD-L5** — measured GPU-vs-QPU cost/task comparison

## Economic requirement

A provider connection is not considered strategically successful merely because the job runs.

The UQPU runtime must eventually compare:

[
A_C = C_{GPU/task} / C_{QPU-cloud/task}
]

Target ladder:

- 100× minimum
- 1,000×
- 10,000×
- 100,000×
- 1,000,000×
- 10,000,000×
- 100,000,000× moonshot

Costs must include provider charges, shots, queue/reservation charges, classical orchestration, retries, error mitigation/QEC, data transfer and output reconstruction where applicable.

## Continuous market surveillance

Provider discovery must be repeated continuously.

At every research/development cycle:

1. check official cloud/provider documentation;
2. identify new providers, new hardware, preview targets and retirements;
3. determine SDK/API/program format;
4. classify paradigm and capabilities;
5. add/update registry entries;
6. create or update adapter plan;
7. record changes in WORKLOG.md;
8. do not remove old providers silently — mark them retired when appropriate.

## Goal

The final UQPU software should behave as a provider-independent quantum execution system that can select the most suitable available cloud QPU for a workload while preserving the GPU-replacement and cost-supremacy objectives.
