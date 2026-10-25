# Literature watch — 2026-10-26: gate-specific quantum speed limits and time-optimal control

**Accessed:** 2026-10-26  
**Primary owner:** Lane D — device, control, calibration and physical-limit applicability  
**Integration owners:** Lane A — gate scheduling / compiler; Lane F — measurement and economics  
**Publication owner:** Lane H  
**Feeds:** A–H; FND-003; FND-006; EQN-001–006; INV-025–027; INV-029–035  
**Evidence class:** `LITERATURE_ONLY / PEER_REVIEWED_ACCEPTED_PAPERS`  
**Project evidence promotion:** none

## Executive delta

Two recent American Physical Society (APS) accepted-paper records sharpen the project’s FND-003 question: the useful comparison is not a generic “quantum state space is large” argument, but a **matched physical evolution with a clearly specified target gate, Hamiltonian constraint, control boundary and timing uncertainty**.

1. Hunter Nelson and Edwin Barnes, **“Exact quantum speed limits for quantum gates from space curve geometry,”** *Physical Review A*, accepted 15 October 2026. The official APS accepted-paper page reports a tight quantum speed limit (QSL) for unitary evolution when the Hamiltonian spectral width is bounded, then derives gate-specific limits for Hadamard, CNOT and Toffoli. The page notes that limits can differ across gates even when their entangling power is the same. [Official APS record](https://journals.aps.org/pra/accepted/10.1103/28zn-ch8y), DOI: [10.1103/28zn-ch8y](https://doi.org/10.1103/28zn-ch8y).

2. Andrei A. Stepanenko, Kseniia S. Chernova, Maxim Mazanov and Maxim A. Gorlach, **“Efficient computation of quantum time-optimal control,”** *Physical Review A*, accepted 21 October 2026. The official APS accepted-paper page describes a method combining quantum-brachistochrone and Lax-pair techniques. Its examples include single-particle transfer in a nearest-neighbor-coupled qubit lattice with switchable couplings and a fixed sum-of-squares constraint, with finite systems up to 10,000 qubits and an effectively infinite ring. [Official APS record](https://journals.aps.org/pra/accepted/10.1103/rsjw-pk53), DOI: [10.1103/rsjw-pk53](https://doi.org/10.1103/rsjw-pk53).

These pages currently identify the works as **accepted papers**, not as fully available final versions of record. This watch therefore records only the scope stated by the official APS pages. The exact theorem statements, derivations, conventions and supplementary material must be checked against the full papers before any bound implementation is trusted.

## What is genuinely new for UQPU

The useful methodological delta is to make the FND-003 comparison **gate-/operator-specific** and tie each reported bound to the exact theorem version and Hamiltonian/control assumptions. A bound for a particular unitary under a bounded spectral-width assumption is not interchangeable with a bound for an arbitrary state transition, another gate, a different control envelope or an open-system trajectory.

The control-optimization paper is a second, complementary signal: for some structured transfer problems, time-optimal control may be computed through a tractable mathematical formulation. This motivates measuring both (a) the theorem-limited minimum under the stated constraints and (b) the actual solver/control implementation cost. It does not establish that a compiled UQPU circuit or physical QPU achieves that minimum.

## Limitations and evidence boundary

- These are external theory/control results. UQPU has not independently reproduced either derivation or its numerical examples.
- The available accepted-paper pages do not supply enough detail to safely implement the exact gate-QSL formula. The new UQPU contract therefore **accepts a precomputed bound only with a hash of the theorem source and a hash of the bound derivation**; it does not derive the bound from an abstract.
- A finite spectral-width assumption is not a complete hardware model. Pulse-shaping limits, leakage, decoherence, connectivity, calibration uncertainty, control electronics, error correction, scheduling/parallelism, measurement, readout, host orchestration and data movement may dominate the practical circuit.
- A theoretical lower bound is not a prediction of an achievable device time, a speedup over a matched classical task, or evidence of lower energy/cost.
- A discrepancy below a bound must first trigger a theorem-scope, Hamiltonian, calibration, timing-boundary and uncertainty audit. It is not automatically evidence of new physics.
- Neither paper supplies evidence for readable classical RAM/VRAM/storage replacement, a new physical law, Pangola-carbon substitution, accepted bio-oil, net fusion electricity, lower financing rates or Data-Center-to-Phone compression.

## Concrete UQPU follow-up — FND003-GATE-QSL-001

Use the new `uqpu.gate_speed_limit_contract.GateSpeedLimitRecord` as a fail-closed **record/interval checker**, not a theorem solver.

1. Freeze the exact gate/unitary hash, initial/final operator definition, Hamiltonian model and spectral-width units, target identity, calibration snapshot, control-resource boundary, environment/noise scope and measurement method.
2. Store the exact theorem/source hash and a separate hash for the executable derivation that produced the bound. Do not transcribe a formula from an abstract.
3. Record observed duration, timing uncertainty, bound uncertainty and repeat count in SI seconds. Keep logical gate time, physical pulse duration, circuit makespan, host time and end-to-end task latency as separate quantities.
4. Compare the observed-duration interval with the bound interval. Return one of:
   - `CONSISTENT_WITH_BOUND_INTERVAL`;
   - `OVERLAPPING_UNCERTAINTY_INTERVALS`;
   - `BELOW_BOUND_REQUIRES_THEOREM_AND_METROLOGY_AUDIT`.
5. If the final case occurs, stop promotion and audit theorem applicability, source/version, Hamiltonian spectral width, calibration, gate identity, pulse boundary and uncertainty budget. Any surviving discrepancy requires independent replication and a discriminating observable before a physical-model challenge can be considered.
6. First use deterministic synthetic records and exact small-system controls. Only later, if authorized, use target-aware no-submit compilation and then a real device with explicit credentials, bounded budget and user consent. This cycle submitted no QPU jobs.

**Falsifier:** after the theorem is fully available and independently implemented, the gate-specific bound fails to reproduce its stated small-system examples, is not stable under the declared assumptions, or provides no useful constraint beyond a correctly matched baseline. Preserve such a null result and keep the narrower existing FND-003 protocol.

## Lane A–H review

| Lane | This cycle’s contribution | Boundary / next gate |
|---|---|---|
| **A — programming, workloads, compiler/runtime** | Defines a way to attach a theorem-bound record to a frozen target unitary before using a QSL in scheduling claims. | No compiler speedup or useful-task advantage; next gate is independent theorem implementation and same-gate comparison. |
| **B — cloud/QPU/provider integration** | Requires target identity and, for any future hardware record, a provider job identifier. | No credentials, provider calls, paid jobs, shots or target pricing were used. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Keeps gate duration separate from state, output, host and transfer accounting. | No readable classical memory/storage equivalence or data-movement reduction is inferred. |
| **D — device/chip/process/fabrication/packaging** | Adds the provenance and uncertainty interval contract for gate-level QSL comparisons. | No measured device timing, calibration result or fabrication requirement is produced. |
| **E — biomass/materials/bio-oil/fusion/cooling/infrastructure** | Reviewed for cross-lane effects; none follows directly from these two theory papers. | BIO-001 and FUS-001 remain open; no material, accepted-fuel, net-electricity or cooling measurement. |
| **F — economics/benchmarks/evidence/integration** | Separates theorem bound, measured duration, uncertainty and later end-to-end accepted-task economics. | No wall-plug energy, total cost, CAPEX/OPEX or financing measurement. |
| **G — chip-manufacturing equipment/software/factory systems** | May consume validated gate/control requirements only after D’s target/calibration gates pass. | No process window, yield, tooling or factory-cost change. D/G co-design remains active. |
| **H — strategy/finance/future-industry/publication** | Publishes the literature delta and reproducible next gate while preserving the strategic plan. | No funding authorization, principal/interest reduction or WACC effect. |

Lane I exists as an auxiliary repository program, but it does not replace or suppress any permanent A–H review.

## Foundational and equation-discovery status

- **FND-001:** no erasure, heat or wall-plug energy measurement added.
- **FND-002:** no new readable-output-information lower bound; Hilbert-space dimension remains distinct from classical storage.
- **FND-003:** strengthened the matched-gate QSL measurement protocol; no new project timing or energy measurement.
- **FND-004:** no alternative physical primitive demonstrated.
- **FND-005:** no new particle/QFT mechanism or credible anomaly established.
- **FND-006:** advances mathematics-first control optimization and assumption-scoped theorem use; no new theorem proved by UQPU.
- **EQN-001:** recorded two fresh official APS accepted-paper sources.
- **EQN-002:** next benchmark should use frozen gate families, held-out parameter regimes and independent implementations.
- **EQN-003:** source/derivation hashes, explicit spectral-width scope and dimensional timing fields are mandatory.
- **EQN-004:** uncertainty-overlap and below-bound cases are explicit audit outcomes, not success labels.
- **EQN-005:** no fundamental-physics modification is justified by these papers; any discrepancy first triggers model/scope/metrology checks.
- **EQN-006:** a bound may influence compiler/device economics only after theorem, target, timing, energy and accepted-task gates pass.

## INV-029–035 impact

- **INV-029:** no physical Data-Center-to-One-Phone compression or service-contract closure.
- **INV-030:** no Pangola/agricultural-residue carbon functional substitution or critical-material reduction.
- **INV-031:** no accepted biomass-derived liquid fuel or cost-per-delivered-energy result.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle-cost result.
- **INV-033:** no measured financed principal, interest, time-to-evidence or WACC change.
- **INV-034:** adds a precise mathematics-to-control candidate path while respecting present physical constraints.
- **INV-035:** keeps AI/theory-generated candidates behind explicit theorem, assumptions, dimensional checks, falsification and independent-validation gates; no new equation is promoted to physical law.

INV-025/026/027 remain falsifiable goals. The 100× and 100,000,000× targets, universal subsystem replacement, commercial low-cost bio-oil/fusion and phone-class physical compression remain unachieved research targets. The six-language Thai, English, Chinese, Japanese, Korean and German master-plan references and root directives 00–06 remain preserved.

## Next highest-value gate

Implement the exact gate-QSL theorem only after the full accepted-paper derivation and assumptions are available. Independently reproduce its small-gate examples, then compare matched physical/control timings with calibrated uncertainty. In parallel, retain the existing FND-003 thermodynamic-speed-limit protocol and the priority-A workload path; do not substitute a gate bound for same-useful-output QPU-vs-classical evidence.
