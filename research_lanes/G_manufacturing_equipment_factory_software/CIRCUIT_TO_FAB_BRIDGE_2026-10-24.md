# Circuit-to-device/fabrication/economics bridge — 2026-10-24

**Work ID:** QALG-FAB-001  
**Primary owner:** Lane G — manufacturing equipment, factory software and production systems  
**Cross-lane consumers:** A (circuit/workload semantics), B (target identity and routing), C (state/I/O/host memory), D (device/process/package requirements), E (power/cooling/materials), F (benchmark/economics/evidence), H (strategy and financing)  
**Base main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Evidence class:** MODEL_ONLY_SOFTWARE_CONTRACT + LITERATURE_ONLY_RESOURCE_REPORT  
**Status:** IMPLEMENTED_CONTRACT / exact-head GitHub CI pending  
**Project evidence promotion:** none

## Why this bridge exists

The 2026-10-15 arXiv preprint “Discovering state-of-the-art quantum circuits with large language models” reports improvements in circuit-level Toffoli and peak-qubit counts on several benchmark tasks. For one Reed–Solomon decoding subroutine, the authors report a baseline of 5.1 million Toffoli gates and 1,938 peak qubits, versus 440,000 Toffolis and 1,837 peak qubits for a discovered circuit; the paper reports an approximately 12-fold Toffoli-count × peak-qubit improvement for that case.

Source: https://arxiv.org/abs/2610.22367

These are third-party preprint results. They are not UQPU measurements, a target-specific circuit certificate, physical-qubit requirements, process/yield data, lifecycle economics, or proof of quantum advantage. The bridge prevents circuit-resource reductions from being silently converted into device/factory/cost claims.

## Executable contract

Primary implementation: software/uqpu-prototype/uqpu/circuit_fab_bridge.py  
Tests: software/uqpu-prototype/tests/test_circuit_fab_bridge.py  
Frozen literature fixture: benchmarks/experiments/cycle010/qalg-fab-interface-001-literature-fixture.json

The validator is dependency-free and fail-closed. It validates completeness and input sanity only. It never calculates or promotes a quantum-advantage claim.

### Stage 1 — circuit and accepted-output certificate

Require the exact workload and quality contract IDs, candidate/reference circuit SHA-256 digests, evidence class, independently checked output-equivalence certificate, logical qubits, native gate histogram, routed depth, and shots per accepted task.

A Toffoli count, qubit count, successful compilation, or same-implementation comparison alone cannot pass this stage. Equivalence must be independently checked against the same useful-output semantics and failure budget.

### Stage 2 — target mapping

Require target ID and redacted target-snapshot digest, calibration snapshot ID, native gate-set ID, routing profile, QEC profile, physical-qubit count, readout profile, latency, control power and cryogenic load.

A saved calibration snapshot is not live calibration. A generic SDK circuit or simulator result does not supply missing target schedules, fidelity, queue, energy or billing.

### Stage 3 — device/process response (D/G co-design)

Require device architecture, process-window ID, measured or explicitly modeled yield fraction, fab cost per good die, package/test cost per device and useful accepted-task lifetime per device.

Lane D specifies device, wiring, control/readout, cryogenic, parasitic, reliability and package requirements. Lane G must return the corresponding equipment/process-control capability, metrology, throughput, yield, cost and blocker record. Neither lane may fill missing fields with an assumed advanced-lithography requirement or a vendor headline.

### Stage 4 — lifecycle economics

Require the same UQPU target, workload contract, quality contract and measurement window across the relevant records. Include provider cost, host/orchestration cost, energy, maintenance, output reconstruction, accepted-output count, baseline-stack identity, UQPU and baseline cost per accepted task, and an uncertainty manifest.

The bridge rejects cross-target price/result combinations and mismatched baseline workload, quality or measurement-window IDs. It does not combine one provider's probability or target performance with another provider's price. A ready assessment means “ready for integration review,” not “advantage achieved.”

## Reproducible negative control

The persisted arXiv resource-count fixture contains only the source-reported Toffoli/peak-qubit figures and is expected to stop at BLOCKED_CIRCUIT_CERTIFICATE. The unit tests also check:

- independent-equivalence requirement;
- missing target snapshot and process-window blockers;
- target/workload/quality/measurement-window mismatch rejection;
- malformed hashes, impossible yield fractions, negative/non-finite costs, invalid gate counts and physical-qubit counts below logical-qubit counts;
- the rule that a complete contract is only READY_FOR_INTEGRATION_REVIEW.

Local isolated validation on the exact module/test logic: 12 unittest methods pass. This is software-contract evidence only; full repository CI on the exact PR head remains authoritative.

## Eight-lane integration status

| Lane | Status this cycle | Evidence boundary / next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Circuit-resource reductions are treated as candidates only. | Freeze the same useful-output contract and independent semantic-equivalence certificate before target/resource translation. |
| B — cloud/QPU/provider integration | Provider-neutral target fields are defined; no credentials or service initialization used. | Obtain an authorized read-only target snapshot; paid jobs remain separately disabled. |
| C — RAM/VRAM/HBM/storage/state/data movement | Host, transfer, reconstruction and memory fields remain explicit downstream requirements. | Measure actual state/I/O/transfer/memory; never infer readable storage from Hilbert-space size. |
| D — devices/chip/process/fabrication/packaging | Receives target-specific routed gate, physical-qubit, readout, control and cryogenic requirements. | No device requirement is accepted until a target/resource certificate exists. |
| E — biomass/materials/energy/cooling/infrastructure | Cooling/control power and material/process dependencies are named, not inferred. | No Pangola-material, fuel, net-electricity or infrastructure measurement was added. |
| F — economics/benchmarks/evidence/integration | Adds fail-closed same-context accounting requirements. | Competitive baseline and total cost per accepted useful task remain absent. |
| G — manufacturing equipment/software/factory systems | Primary owner; adds a circuit-to-process/yield/cost bridge. | Require a device-specific process-window and yield response before fab economics are accepted. |
| H — Kanusanan Pongpanna Model strategy/finance/future industries | Keeps the software-first path connected to capital and lifecycle economics. | No funding, principal, interest, WACC or commercialization result is claimed. |

The current canonical AGENTS.md also preserves Lane I as an additional parallel extension. This artifact does not replace, merge away, or suspend any A–H lane; the user's permanent A–H review remains intact.

## Foundational/equation-discovery cross-cutting review

FND-001 through FND-006 and EQN-001 through EQN-006 remain active. This bridge is an engineering/accounting interface, not a new equation of physics. Any future proposed physical-law change must retain the incumbent assumption, dimensional/symmetry/conservation/causality checks, limiting cases, falsifier, held-out prediction, discriminating observable, experiment/proof and independent-validation path.

BIO-001, FUS-001 and FIN-001 were reviewed but receive no evidence-class promotion. The bridge can later pass validated manufacturing cost/yield inputs into Lane F/H models; it supplies no Pangola feedstock/yield/upgrading data, fusion net-electric cost, or financing terms by itself.

## INV-029 through INV-035 impact

- **INV-029:** advances a staged route toward complete physical-system accounting; no phone-class physical compression is demonstrated.
- **INV-030:** no material substitution or elemental transmutation claim.
- **INV-031:** no accepted bio-oil/fuel or commercial cost result.
- **INV-032:** no reliable net delivered fusion-electricity result.
- **INV-033:** no measured principal, absolute-interest, project-WACC or macro-rate reduction.
- **INV-034:** preserves the mathematics-to-device/economics path with explicit constraints and falsifiers; no foundational physical discovery.
- **INV-035:** circuit and equation candidates remain hypotheses until independent predictive/experimental evidence; no AI-generated physical law is promoted.

INV-025/026/027 and the 100× / 100,000,000× goals remain unproven. The 100-million-GPU and universal 100-million-unit subsystem moonshots are not supported by this bridge.

## Synchronization and next gate

This work is on source branch research/2026-10-24-dg-resource-cost-bridge and is **pending PR review/main synchronization**. Each source commit carries the required Research-Sync: pending-main trailer. The append-only RESEARCH_GAPS.md, WORKLOG.md and DECISIONS.md were not rewritten from a connector snapshot; the dated lane artifact and integration record retain this cycle's detail until a safe canonical reconciliation.

The latest main SHA at startup was c7b5958af58fad04a101ef5c6abf6a29293c867e. The connector returned no commit-status entries for that SHA; the last run recorded in the main cold-start manifest is historical and is not exact-current-head CI evidence.

**Next highest-value gate:** require exact-head UQPU Prototype and Project Invariants CI, then apply this bridge to an independently verified circuit/resource certificate with a same-target read-only snapshot. Only after target mapping passes should Lane D/G populate device/process/yield inputs and Lane F compute same-window cost per accepted useful task. No paid QPU job is authorized or submitted.
