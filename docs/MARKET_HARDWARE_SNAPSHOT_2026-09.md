# Quantum Hardware Market Snapshot — September 2026

## Purpose

This snapshot provides an official-source baseline for UQPU/UQCS gap analysis.

It is deliberately **modality-aware**. Qubit counts from gate-model, analog and annealing systems are not treated as interchangeable.

## Verified current/roadmap observations

### IBM Quantum

**Nighthawk r2 / ibm_phoenix:** IBM's September 2026 Quantum Compute Service changelog reports the first Nighthawk r2 cloud QPU, `ibm_phoenix`, with 120 programmable qubits, >100,000 MCPS throughput and up to 25x higher throughput than Heron while matching fidelity. This is now included in the machine-readable snapshot.

Source: https://quantum.cloud.ibm.com/docs/en/guides/changelog-quantum-compute-service

IBM lists current Heron-family systems at 133/156 programmable qubits and Nighthawk at 120 programmable qubits. IBM's 2029 Starling roadmap target is 200 logical qubits and 100 million quantum gates.

Source: https://www.ibm.com/quantum/hardware

### Quantinuum
Helios is available through Quantinuum's cloud and is listed with 98 fully connected qubits, 50 logical qubits, 99.9975% single-qubit fidelity and 99.921% two-qubit fidelity.

Source: https://www.quantinuum.com/products-solutions/quantinuum-systems/helios

### IonQ
IonQ's roadmap lists a 2026 target of 100–256+ physical qubits, 99.99% physical-qubit fidelity, 12 logical qubits and logical error state below 1e-7.

Source: https://www.ionq.com/roadmap

### Pasqal
Pasqal reported defect-free 1024-atom registers with under 0.5% defects and 5000-second lifetimes in April 2026. Pasqal's roadmap also targets 200+ logical qubits by 2029.

Sources:
- https://www.pasqal.com/blog/defect-free-1024-atom-registers-scaling-to-1000-qubits/
- https://www.pasqal.com/technology/roadmap/

### QuEra
Amazon Braket documents QuEra Aquila as an analog neutral-atom QPU operating up to 256 qubits.

Source: https://aws.amazon.com/braket/quantum-computers/quera/

### Rigetti
Rigetti lists Cepheus-1-108Q, deployed April 7 2026, with 108 qubits, 99.9% median single-qubit-gate fidelity and 99.1% median CZ fidelity.

Source: https://www.rigetti.com/what-we-build

### D-Wave
Advantage2 is available through Leap and is documented with 4,400+ qubits and 40,000+ couplers. It is an annealing system, not a universal gate-model QPU.

Source: https://support.dwavesys.com/hc/en-us/articles/32105885880087-D-Wave-s-Advantage2-Quantum-Computer-Now-Generally-Available

### OQC
OQC Cloud provides access to the 32-qubit Toshiko system. OQC's roadmap describes Genesis as a 16-logical-qubit KiloQuOp device, commercially targeted from 2026.

Sources:
- https://oqc.tech/access/oqc-cloud/
- https://oqc.tech/tech/technical-roadmap

### Quandela
Quandela continues expanding cloud-accessible photonic quantum computing, including its September 2026 addition to Canada's Quantum Computing Sandbox.

Source: https://www.quandela.com/about-us/newsroom/

## Gap-analysis rule

Never rank systems solely by qubit count.

The machine-readable gap analyzer compares:
- paradigm;
- cloud availability;
- physical qubits when meaningful;
- logical qubits when published;
- gate fidelity where published;
- operation-scale claims;
- unknown fields.

An unknown metric is never treated as a pass.

## Current high-level conclusion

Present market systems remain far from a general UQCS that replaces the complete CPU/GPU/memory/storage stack. The most strategically useful near-term route is to use current cloud QPUs as experimental execution backends, identify narrow workload advantages, and use inverse design to quantify the hardware/software gap to 100× economic replacement.
