# UQPU Hardware Requirements Matrix

| Layer | Requirement | Metric | Why it matters |
|---|---|---|---|
| Qubit/device | Low physical error | error/gate or operation | QEC cost |
| Qubit/device | High coherence | T1/T2 or modality equivalent | circuit depth |
| Control | Low energy/control channel | J/op or W/channel | data-center power |
| Control | High fanout/multiplexing | qubits/channel | wiring/ASIC cost |
| Readout | Low latency | s/measurement | feedback/QEC |
| Readout | High fidelity | error probability | result quality |
| QEC | Low physical/logical ratio | physical qubits/logical | hardware cost |
| Photonics | Low loss | dB/component/link | scalability |
| Photonics | High detector efficiency | % | photonic fault tolerance |
| Photonics | High source quality | indistinguishability/purity | gate success |
| Interconnect | High bandwidth | bit/s or qubit-links/s | scale-out |
| Interconnect | Low energy/bit | J/bit | data-center cost |
| Memory | Long logical-state lifetime | seconds | state reuse |
| Memory | High usable bandwidth | state ops/s | GPU-memory replacement |
| Packaging | High die/chiplet yield | % | cost |
| Packaging | Low thermal burden | W | cooling |
| Fabrication | High wafer yield | % | CAPEX amortization |
| Calibration | Low calibration overhead | time/day | utilization |
| System | High uptime | % | cost/task |
| System | High utilization | % | amortization |
| System | Low total cost/task | USD/task | economic target |

## Target derivation rule

Do not set arbitrary hardware specifications.

For each workload:

1. measure GPU+HBM+RAM baseline;
2. solve maximum allowed UQPU cost for target 100× / 1M× / 100M×;
3. propagate this cost budget backward through hardware layers;
4. derive required yield, power, fidelity, bandwidth, QEC overhead and utilization;
5. mark impossible requirements as falsification evidence.
