# Batch 089 — gate-specific quantum speed limits and matched runtime accounting

**Date:** 2026-10-28  
**Canonical starting main:** 52f68f50cb60cba3152ec3323575c7b8baab6fc8  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-lane owners:** B/C/D/E/F/G/H; FND-001/FND-003/FND-006; EQN-001–006  
**Evidence class:** CONTRACT_ONLY + ACCEPTED_THEORY_PAPER / LITERATURE_ONLY for UQPU

## Starting-state audit

The current main head was resolved dynamically from GitHub and confirmed again before writing. This cycle read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, root directives 00/00A/01–06, the latest main Batch 088, recent Batches 086/085, focused evidence/gap records, the Lane A signed-Max-Cut implementation/tests, fundamental_limits.py, frontier_hypothesis.py, equation_discovery.py, lane interface contract, handoff manifest and exact-head CI state. Batch 087 remains in open PR #144 and PR #145 remains an open pending-main summary; neither is treated as merged.

Starting-head CI passed on 52f68f50cb60cba3152ec3323575c7b8baab6fc8: prototype/invariant workflow [#1848](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40592732419) and cold-start audit [#1055](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40592732421). The new commit requires its own exact-head Actions checks.

The canonical operating policy defines exactly A–H, but the handoff manifest still contains legacy Lane I and the nine-lane schema. This cycle preserves that mismatch as an explicit governance gap rather than deleting legacy files or partially migrating the validator/manifest. Large append-only RESEARCH_GAPS.md and WORKLOG.md were not rewritten from partial snapshots; the new focused gap and integration record are the safe cycle records.

## Lane A — gate-specific lower bound to accepted-task contract

Added [A-GATE-QSL-001](../research_lanes/A_quantum_programming_runtime/GATE_QSL_TO_ACCEPTED_TASK_CONTRACT.md). It separates a theoretical gate lower bound from physical pulse time, compiled critical path, fault-tolerant logical runtime and end-to-end accepted-task latency. It requires source/version hashes, Hamiltonian spectral-width provenance, gate-equivalence convention, fidelity/leakage criteria, held-out tests and independent reconstruction before any numeric bound is used.

The current Lane A signed-Max-Cut contract remains SOFTWARE_CONTRACT_ONLY. Its existing six focused tests compare direct, QUBO and Ising scores and maximizers on small signed-weight fixtures. This cycle did not claim a new SDK check or target-aware simulation. The next Lane A implementation gate remains an independent pinned-SDK reconstruction of the signed-Max-Cut Hamiltonian against the exhaustive reference.

## Fresh literature surveillance

A fresh search of symbolic regression, neural-symbolic equation discovery, AI theorem discovery, physics-informed/differentiable models, automated experiment design, effective constitutive laws, no-go/lower-bound work, credible anomalies and quantum speed limits found a new-to-main source relevant to FND-003:

- Nelson and Barnes, “Exact quantum speed limits for quantum gates from space curve geometry,” *Physical Review A* accepted 2026-10-15, DOI [10.1103/28zn-ch8y](https://doi.org/10.1103/28zn-ch8y). The official accepted-paper record describes a tight unitary-gate speed limit under bounded Hamiltonian spectral width and gate-dependent examples including Hadamard, CNOT and Toffoli.
- The [dated watch](literature_watch/2026-10-28-exact-gate-quantum-speed-limit.md) records novelty, limits, relevance and a falsifiable follow-up. The [focused gap](RESEARCH_GAP_FND003_GATE_QSL_RECONSTRUCTION_2026-10-28.md) requires equation/proof reconstruction and independent optimal-control checks before code or device transfer.
- CoSR/progressive symbolic discovery and the OTOC speed-limit source are already recorded in main; they were checked rather than duplicated. No newly located result changes the accepted-liquid BIO-001 boundary, net-reliable-electricity FUS-001 boundary, or measured principal/interest/WACC status for FIN-001.

## A–H status ledger

- **A — Quantum programming/workloads/compiler/runtime:** added gate-QSL-to-accepted-task contract; no numeric bound implementation or new SDK check. Next: independently lower signed Max-Cut into a pinned SDK operator and compare all tiny-instance energies/argmax sets with the exact reference.
- **B — Cloud/QPU/provider integration:** provider-neutral route unchanged; no target, price or calibration change validated and no QPU job submitted. Keep IBM Quantum, Amazon Braket, Azure Quantum/providers, IonQ, Rigetti, D-Wave, IQM, Quantinuum, Pasqal, QuEra, Quandela, OQC and emerging providers separate by target and billing context.
- **C — RAM/VRAM/HBM/storage/state/data movement:** output-information, reconstruction and readable-storage boundaries remain. Hilbert-space dimension/qubit count is not classical memory capacity.
- **D — Quantum/photonic/semiconductor device/process/packaging:** the theorem highlights Hamiltonian/control provenance as a prerequisite; no device, fabrication or process-window result.
- **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure:** BIO-001 and FUS-001 remain open; no Pangola material qualification, accepted liquid fuel or net delivered fusion-electricity evidence.
- **F — Economics/benchmarks/evidence/integration:** bound, measured gate duration, accepted-task latency, wall-plug energy and provider cost remain separate fields. No cost advantage or FIN-001 financing result.
- **G — Manufacturing equipment/software/factory systems:** D/G co-design remains active; no yield, cost-per-good-device or factory result.
- **H — Ketskaew Chulamani/Kanusanan Pongpanna Model strategy/publication:** new dated watch, focused gap and integration record published. Thai/English/Chinese/Japanese/Korean/German master-plan links and strategic AI-agent/funding references remain preserved.

## Foundational and equation-discovery progress

- **FND-001:** the new gate contract reinforces total-system energy accounting; no measured work, heat or wall-plug energy is added.
- **FND-002:** unchanged; no output-information or readable-memory lower bound is inferred from the gate theorem.
- **FND-003:** new gate-specific operator-QSL candidate added to the literature frontier; full theorem reconstruction, optimal-control comparison and matched experiment remain open.
- **FND-004:** no new alternative physical primitive demonstrated.
- **FND-005:** no new validated QFT/elementary-particle mechanism or anomaly promoted.
- **FND-006:** mathematical theorem reconstruction and counterexample search are prioritized before implementation.
- **EQN-001–006:** unchanged evidence gates. The accepted theorem is a source to reconstruct, not an AI-generated equation or a new law; dimensional/symmetry/conservation/causality checks, limiting cases, held-out predictions, falsifiers, proof/simulation and independent validation remain required.

## INV-029 through INV-035

- **INV-029:** no Data-Center-to-One-Phone physical compression, service/energy boundary or lifecycle-cost closure.
- **INV-030:** no Pangola/agricultural-residue carbon functional substitution, recovery or material qualification; no transmutation claim.
- **INV-031:** no accepted liquid-energy/fuel result or full-path commercial cost.
- **INV-032:** no reliable net delivered fusion electricity or commercial lifecycle-cost result.
- **INV-033:** no reduced financed principal, absolute interest, project WACC or macro-rate effect demonstrated.
- **INV-034:** advances the mathematics-first, assumption-scoped theorem audit method only.
- **INV-035:** keeps equation/theorem provenance, falsification and independent validation mandatory; no AI-generated equation or fitted expression is promoted to physical law.

INV-025/026/027 remain active falsifiable moonshots; no qubit/state-space-to-readable-memory equivalence is asserted. No paid QPU job was authorized or attempted.

## Integration, synchronization and next gate

This cycle adds the dated literature watch, focused reproduction gap, Lane A interface contract, Batch 089 and A–H integration record; README and the cold-start manifest are synchronized to the new frontier while preserving the permanent directives and six-language strategic context. RESEARCH_GAPS.md and WORKLOG.md remain append-only sync debt rather than being replaced from incomplete reads. The A–H/A–I manifest discrepancy and open PRs #144/#145 remain explicitly unresolved.

**Next highest-value gate:** independently reconstruct the signed-Max-Cut Ising operator in the pinned Qiskit SDK and compare every assignment energy and complete maximizer set against the classical exhaustive oracle. In parallel, obtain the full gate-QSL paper, pin its exact equations and assumptions, then reproduce the Hadamard/CNOT/Toffoli examples and compare with a separate small-instance optimal-control reference. No paid QPU execution without credentials, bounded budget and explicit consent.
