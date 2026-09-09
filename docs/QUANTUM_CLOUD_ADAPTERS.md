# UQPU Quantum Cloud Adapter Layer — September 2026

## Goal

Prepare one provider-neutral software boundary for every major cloud quantum route in the UQPU/UQCS registry.

The core compiler never imports vendor SDKs. Vendor packages are imported only inside concrete adapters.

## Adapter coverage

| Provider/route | UQPU adapter | Current readiness | Primary path |
|---|---|---|---|
| IBM Quantum | IBMQuantumAdapter | real-submit implemented | qiskit-ibm-runtime |
| Amazon Braket | AWSBraketAdapter | real-submit implemented | amazon-braket-sdk |
| Azure Quantum | AzureQuantumAdapter | real-submit implemented | Azure/QDK workspace target |
| IonQ direct | IonQDirectAdapter | real-submit implemented | IonQ API v0.4 |
| Rigetti QCS | RigettiQCSAdapter | real-submit implemented | pyQuil/QCS |
| D-Wave Leap | DWaveLeapAdapter | real-submit implemented | Ocean/DWaveSampler |
| IQM | IQMAdapter | aggregator-routed | Amazon Braket |
| Quantinuum Nexus | QuantinuumNexusAdapter | real-submit implemented | qnexus |
| Pasqal | PasqalAdapter | aggregator-routed | Azure Quantum |
| QuEra | QuEraAdapter | aggregator-routed | Amazon Braket |
| Quandela | QuandelaAdapter | serialization/dry-run ready | Perceval remote config pending |
| OQC | OQCAdapter | serialization/dry-run ready | account-specific runtime config pending |

## Why aggregator routing counts as a prepared connection path

Amazon Braket and Azure Quantum are first-class quantum-cloud aggregators. A provider does not need a separate UQPU core path if it can be selected as a target through an aggregator adapter while preserving the provider-neutral execution contract.

This reduces duplicated credential, billing and result-management logic.

## Current official API anchors

IBM's current client is `qiskit-ibm-runtime` / IBM Quantum Compute Service. IBM's July 2026 rename from Qiskit Runtime to IBM Quantum Compute did not require code changes. The service exposes backends, jobs and Qiskit primitives.

Amazon Braket's Python SDK uses `AwsDevice(...).run(...)` and returns an asynchronous quantum task with task ID/state/result.

Azure Quantum's current QDK supports Python/CLI job submission to provider targets; provider-native formats and QIR are supported depending on target.

IonQ API v0.4 uses `POST https://api.ionq.co/v0.4/jobs`, API-key auth, simulator/QPU backend selection, job status/results and dedicated cost endpoints.

Rigetti QCS uses pyQuil/Quil plus QCS/QVM.

D-Wave Leap uses Ocean SDK samplers such as `DWaveSampler` for QUBO/Ising workloads.

Quantinuum Nexus exposes the `qnexus` API for circuits, compilation, devices, execution and jobs.

## Safety/economic execution guard

Real paid QPU submission is **never implicit**.

Concrete adapters require a `SubmissionGuard` with explicit consent when an execution is marked paid. Dry-run requires no credentials or vendor SDKs.

The software therefore supports three safe steps:

```text
portable program
 -> adapter.lower()
 -> adapter.dry_run()
 -> explicit consent/budget
 -> adapter.submit()
```

## Credential conventions

Typical credential/config inputs include:

- IBM: `QISKIT_IBM_TOKEN` / saved Qiskit Runtime account
- AWS: standard AWS credentials/profile
- Azure: `AZURE_QUANTUM_CONNECTION_STRING` or Azure identity/workspace
- IonQ: `IONQ_API_KEY`
- D-Wave: `DWAVE_API_TOKEN`
- Quantinuum: Nexus authentication
- Rigetti: QCS configuration

No secret is stored in the repository.

## Remaining validation work

“Implemented” does not mean “real-QPU verified.”

Current evidence levels:

- adapter interface + dry-run: testable without credentials;
- simulator: must be validated provider-by-provider;
- real QPU: requires account access, credentials, target availability and explicit execution consent/budget;
- paid execution must record actual provider cost and useful-output contract.

Quandela and OQC direct account APIs remain the principal direct-route gaps; their serialization/dry-run paths are ready and their official/partner access routes must be configured per account.

## Future provider rule

Adding a new cloud provider requires only:

1. add/update `ProviderProfile`;
2. implement `BaseConcreteAdapter`;
3. register it in `ADAPTERS`;
4. add dry-run and health tests;
5. document credentials/program formats;
6. validate simulator and real-QPU levels when access exists.

No compiler/core rewrite should be necessary.
