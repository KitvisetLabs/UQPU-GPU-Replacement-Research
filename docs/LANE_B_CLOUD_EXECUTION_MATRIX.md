# Lane B — Quantum Cloud Execution Matrix

Lane B turns the provider registry/adapters into a workload-execution decision surface.

| Route | Modality | Primary UQPU path | Current software status | Next evidence gate |
|---|---|---|---|---|
| IBM Quantum | gate model | direct adapter | submit code + dry-run | simulator/real-QPU smoke |
| Amazon Braket | gate/analog aggregator | direct aggregator adapter | submit code + dry-run | target-specific smoke |
| Azure Quantum | multi-provider aggregator | direct aggregator adapter | submit code + dry-run | target-specific smoke |
| IonQ | gate model | direct API + aggregators | submit code + dry-run | simulator/real-QPU smoke |
| Rigetti QCS | gate model | pyQuil/QCS | submit code + dry-run | QCS smoke |
| D-Wave Leap | annealing/hybrid | Ocean | submit code + dry-run | bounded QUBO smoke |
| Quantinuum Nexus | gate model | qnexus | submit code + dry-run | emulator/real target |
| IQM | gate model | Braket / direct SDK research | aggregator-routed | target smoke |
| Pasqal | neutral atom analog | Azure / Pulser research | aggregator-routed | target smoke |
| QuEra | neutral atom analog/digital | Braket / Bloqade | aggregator-routed | target smoke |
| Quandela | photonic | Perceval | serialization/dry-run | configured remote RPC |
| OQC | gate model | account/runtime route | serialization/dry-run | configured runtime |

## Selection rule

For each Lane A workload contract:

1. determine mathematical/semantic modality;
2. identify providers that can express that modality;
3. estimate state-loading/output and billing implications;
4. prefer simulator/free-tier validation;
5. require explicit consent/budget for paid QPU execution;
6. record job ID, output-quality result and actual cost for real-QPU evidence.

Provider connection alone is not mission progress. The connection must eventually carry a useful workload contract.
