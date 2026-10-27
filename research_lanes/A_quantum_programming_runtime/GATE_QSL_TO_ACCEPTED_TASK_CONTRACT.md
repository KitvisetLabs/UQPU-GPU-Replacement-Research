# Lane A contract — gate-specific QSL to accepted-task runtime

**Contract ID:** A-GATE-QSL-001  
**Date:** 2026-10-28  
**Owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane interfaces:** B target/SDK identity; C state and data movement; D Hamiltonian/control provenance; F reference certificates and total-cost accounting; H evidence publication  
**Evidence class:** CONTRACT_ONLY / LITERATURE_ONLY  
**Source candidate:** Nelson & Barnes, *Physical Review A* accepted 2026-10-15, DOI 10.1103/28zn-ch8y

## Purpose

Keep a theoretical gate-time lower bound from being misreported as measured gate latency, circuit runtime, quantum advantage, or cost per accepted useful task. The source is a candidate theorem until the full statement, equations and assumptions are independently reconstructed.

## Required identity fields before a bound can be evaluated

- immutable workload/instance/input/output-contract hash and accepted-output quality threshold;
- exact target and provider, SDK/API version, native-gate and compilation configuration;
- source-paper version/hash, theorem identifier, equation transcription, proof/reconstruction artifact hash;
- target gate or unitary, endpoint-equivalence convention (including global phase), Hilbert-space dimension and declared control model;
- Hamiltonian spectral-width definition and value/provenance, admissible controls, drift assumptions and duration boundary;
- initial/final unitary or state convention, fidelity/error threshold and leakage tolerance;
- held-out-case manifest, numerical tolerances, counterexample-search result and independent reviewer/result hash.

Missing fields suppress numerical bound reporting. Do not fill unknown theorem conventions by guess.

## Separate time and resource quantities

1. **Theoretical gate lower bound:** calculated only after theorem reconstruction and assumption checks.
2. **Physical pulse/gate duration:** target-specific measurement with calibration and uncertainty.
3. **Compiled circuit critical path:** includes routing, parallelism and the target's native operations.
4. **Fault-tolerant logical runtime:** includes the declared QEC/code-cycle and logical-error requirements.
5. **End-to-end accepted-task latency:** includes preparation, compilation, queueing where applicable, execution, readout, reconstruction, retries and host-side work.

Keep energy separate from all time quantities. A lower gate bound is not a measured energy estimate. For economics, include controller and cooling power where measurable, host compute, memory/I/O, provider billing and total cost per accepted useful task.

## Matched comparison gate

A classical control, simulated circuit or hardware run is comparable only when it uses the same useful-output contract, input/instance hash, accepted-quality criterion, declared timing boundary and comparable confidence/uncertainty reporting. A successful job is not quality acceptance. A failed quality gate suppresses any speed or cost advantage claim.

For provider comparisons, probability, calibration and price must come from the same named target and compatible time window. No cross-provider probability/price mixing is permitted. Simulator/dry-run first; paid QPU jobs remain disabled without credentials, bounded budget and explicit user consent.

## Acceptance and falsification

- Reconstruct the exact source theorem and reproduce the source's small gate examples.
- Independently implement the formula and check dimensions, gate equivalence, limiting cases and the theorem's control assumptions.
- Compare with an independently coded numerical optimal-control reference on pinned and held-out small gates.
- Preserve failed derivations, counterexamples and uncertainty.
- Do not promote the theorem to a new physical law; it is an external theoretical result under stated assumptions.
- Do not promote gate-level results to algorithm speedup, hardware advantage or economics until the full accepted-task gates pass.

## Integration impact

- **B:** exposes target/SDK/calibration requirements without choosing a provider.
- **C:** keeps output-information/readable-storage contracts distinct from state-space size.
- **D/G:** exposes Hamiltonian, control and process evidence needs for device/manufacturing co-design; no yield or device result follows.
- **E:** no bio-oil, material or fusion transfer without separate domain evidence.
- **F:** provides a consistent boundary for time/energy/cost evidence and FIN-001; no financing-rate result follows.
- **H:** provides a reusable publication and handoff contract while preserving the multilingual strategic plan.

This contract changes research bookkeeping and test design only. It contains no measured QPU result and no claim of quantum advantage.
