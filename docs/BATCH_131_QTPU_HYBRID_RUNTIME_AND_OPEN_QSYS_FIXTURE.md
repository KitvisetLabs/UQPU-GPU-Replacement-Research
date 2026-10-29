# Batch 131 — open-system invariant toy oracle and qTPU hybrid-runtime surveillance

**Date:** 2026-10-29  
**Starting main SHA:** `ff2fbb5ea3fad629666a4407fe59942b86015592` (Batch 130)  
**Main at artifact authoring:** `22e7e2b11fdab7c56af3baadf2178a6faaed62e2`  
**Primary owner:** Lane A — exact toy oracle and workload acceptance  
**Interfaces:** Lane B open-system/provider measurement; Lane C state/memory/transfer; Lane F evidence/economics; Lane H literature/provenance  
**Evidence class:** MODEL_ONLY SOFTWARE FIXTURE + PEER-REVIEWED SYSTEMS LITERATURE / PUBLIC ARTIFACT INSPECTION; NO UQPU HARDWARE REPRODUCTION

## 1. Canonical start and governance

Resolved the latest `main` dynamically; did not infer state from a fixed batch number or prior conversation. Read the charter, version invariants, goals, README, A–H Research Operating System, open-frontier directive, Kanusanan Pongpan na Model, strategic references, root directives 00/00A/01–06, main-commit sync policy, cross-lane continuous-integration protocol, Batch 130/129/128, current invariant-structure and equation-stability gaps, lane scoreboard and work-log/research-gap context. The canonical multilingual Thai, English, Chinese, Japanese, Korean and German plan links and strategic AI-agent/funding references remain preserved.

The starting combined-status query returned no status contexts for `ff2fbb5ea3fad629666a4407fe59942b86015592`. The repository connector's status response remains the available CI signal; no green result is inferred from an empty response. The container could not resolve GitHub for a fresh clone, so the committed repository test suite has not been run locally in this session. No paid QPU job was submitted.

## 2. Lane A implementation: separate invariance from algebra closure

Batch 130's highest-value next gate was to implement an exact small-model oracle before attempting noisy inference. Added:

- `software/uqpu-prototype/uqpu/open_quantum_invariant_toy.py`
- `software/uqpu-prototype/tests/test_open_quantum_invariant_toy.py`
- `research_lanes/A_quantum_programming_runtime/OPEN_QSYS_TOY_FIXTURE_2026-10-29.md`

The toy model declares a single-qubit pure-dephasing Heisenberg generator in Pauli basis `(I,X,Y,Z)): (I,Z\mapsto0), (X,Y\mapsto-\gamma(X,Y)), for finite `gamma >= 0`. A standard-library evaluator separately tests whether each generator image remains in the candidate span and whether pairwise operator products remain in that span. It validates finite coefficients, basis dimensions, linear independence, rate and tolerance inputs.

The reference harness ran nine deterministic synthetic test methods and passed **9/9**. The committed repository test file still needs exact-head Actions confirmation. The tests include a positive invariant/algebra-closed case, an invariant but non-algebra counterexample, a closed but non-invariant counterexample, zero-rate behavior, and malformed/non-finite/dependent-input rejection. These are model/software checks only; they do not infer a structure from measurements, establish decoherence-free behavior, or demonstrate any physical/engineering advantage.

## 3. Fresh literature surveillance — qTPU

Fresh public searches covered symbolic regression and staged equation discovery, neural-symbolic/formal proof discovery, physics-informed and time-dependent modeling, automated experiment design, quantum/open-system methods, material inverse design, biomass conversion, fusion cost, and R&D financing. The recent CoSR, AI-mathematics corpus, formal-proof and other equation-discovery leads were already indexed in the repository; no new physical-law or lower-bound evidence was promoted.

A new-to-repository systems source was identified: Tornow, Giortamis, Sprokholt, Mendl and Bhatotia, “qTPU: Hybrid Tensor Networks for Quantum-Classical Acceleration,” USENIX OSDI 2026, pp. 2367–2388. Official page: https://www.usenix.org/conference/osdi26/presentation/tornow. Public artifact: https://github.com/TUM-DSE/qtpu, inspected revision `3f68fc96e5de9c336c96e82d4af0a2f7a96b5a22`. The paper introduces a hybrid tensor-network representation with compiler/runtime optimization across classical contraction overhead and quantum error. The authors report substantial gains on their selected workloads; these remain attributed external claims, not UQPU results.

The public README and reproduction guide were inspected, along with the dependency manifest and root Apache-2.0 licence. The guide describes reproducing plots from pre-collected logs and identifies IBM Marrakesh as a hardware arm requiring IBM credentials. This cycle did not execute qTPU, audit every raw log row, or independently reproduce the paper. A dated literature watch and a focused matched-resource gap record source/date, method novelty, limitations, exact A–H relevance and a falsifiable follow-up. UQPU copied no external code.

## 4. A–H status

| Lane | Current status | Evidence boundary / next gate |
|---|---|---|
| **A — Quantum programming/workloads/compiler/runtime** | Added exact Pauli-basis invariance/algebra-closure oracle and nine tests; qTPU hTN is a new optional lowering candidate. | Verify exact-head CI; extend the toy oracle to a second known generator; then freeze matched-output classical/QPU/hTN arms and family-disjoint holdouts. |
| **B — Cloud/QPU/provider integration** | Provider-neutral measurement boundary retained; qTPU artifact includes an IBM hardware arm. | No provider execution. Keep probabilities, noise, usage and price tied to the same target/run; simulator/dry-run first. |
| **C — RAM/VRAM/HBM/storage/state/data movement** | Explicitly separates observable subspace, Pauli-basis dimension, tensor intermediates and readable classical memory. | Measure contraction peak memory, state/I/O, transfers and reconstruction; no storage equivalence inferred. |
| **D — Quantum/photonic/semiconductor device/chip/process/packaging** | No new device result. Measurement/control requirements remain downstream of reproducible workload results. | Derive target-specific tolerances only after independent reproduction. |
| **E — Biomass/materials/bio-oil/fusion/cooling/infrastructure** | Batch 129 BIO-001 flash-Joule/Pangola gap and FUS-001 cost-driver work remain open. | No new fuel, material substitution, net fusion electricity or cooling/energy result; obtain primary data and matched balances. |
| **F — Economics/benchmarks/evidence/integration** | Added a testable structural oracle and a qTPU matched-resource gap. | Count compilation, shots, host compute, memory, transfers, retries, reconstruction, billable usage, energy and total cost per accepted useful task. |
| **G — Quantum-chip manufacturing equipment/software/factory systems** | D/G co-design remains active; no equipment, yield or cost-per-good-device evidence. | Convert only replicated device/runtime needs into metrology and process specs. |
| **H — Strategic/financial/future-industry research and publication** | Added qTPU source watch and reproduction gap; strategic master plan remains preserved. | Keep author-reported performance, strategy, project finance and measured economics as separate evidence classes. |

INV-034 and INV-035 remain upstream cross-cutting layers feeding A–H. The lane A fixture lives under the lane-oriented workspace; cross-lane interfaces and source provenance are recorded in `integration/`.

## 5. Foundational and equation-discovery progress

- **FND-001:** no new thermodynamic-gap measurement.
- **FND-002:** no output-information lower-bound change; observable or tensor dimension is not readable storage.
- **FND-003:** no matched control-versus-quantum-speed-limit measurement.
- **FND-004:** known pure-dephasing toy model only; no alternative physical primitive.
- **FND-005:** no new QFT/elementary-particle mechanism or discriminating observable.
- **FND-006:** strengthened exact known-model oracle and counterexample retention; no theorem or new physics claim.
- **EQN-001:** qTPU is a systems-method source, not a new equation.
- **EQN-002:** generator invariance and algebra closure are now separate executable checks.
- **EQN-003:** model, basis, generator rate and numerical tolerance are declared before acceptance.
- **EQN-004:** invariant/non-algebra and closed/non-invariant counterexamples reject false acceptance; measurement-identifiability, noise and family-holdout gates remain open.
- **EQN-005:** no anomaly, altered physical assumption or replacement law proposed.
- **EQN-006:** technology and economics promotion remains blocked pending independent reproduction and end-to-end resource accounting.

The existing `fundamental_limits.py`, `frontier_hypothesis.py`, `equation_discovery.py`, equation-candidate gate and Batch 130 benchmark contract remain in place. Present physics and known bounds remain binding for engineering claims.

## 6. Contribution to INV-029 through INV-035 and INV-025/026/027

- **INV-029:** adds a reusable, explicit model-checking step for one possible computational primitive; no handset physical-compression or external-resource closure.
- **INV-030:** no new material result; carbon remains functional substitution, minimization, recovery/recycling, hybridization or redesign, never elemental transmutation.
- **INV-031:** no accepted Pangola liquid-energy yield or full delivered-fuel cost.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle cost evidence.
- **INV-033:** no UQPU financed-principal, absolute-interest, project WACC or macro-rate effect measured; time-to-evidence remains a separate finance gate.
- **INV-034:** the toy oracle connects an explicit mathematical model to falsifiable software checks; qTPU offers a testable systems/compiler direction.
- **INV-035:** candidate claims remain subordinate to dimensions/model assumptions, held-out behavior, counterexamples, proof/simulation, experiments and independent replication.
- **INV-025/026/027:** the 100,000,000-GPU and universal 100,000,000-unit targets remain falsifiable goals; neither qubit count nor tensor/state-space dimension is classical memory or accepted useful work by itself.

All eight high-visibility root directives, `docs/KANUSANAN_PONGPANNA_MODEL.md`, `STRATEGIC_PLAN_REFERENCES.md`, multilingual public master-plan links and recorded strategic AI-agent/funding references were preserved. No new physical law, real-QPU advantage, critical-material substitution, commercial low-cost bio-oil/fusion, lower WACC or North-Star closure is claimed.

## 7. GitHub commits, synchronization and CI

The following main-branch commits are part of this cycle and are now described in this Batch record:

| Artifact | Main commit |
|---|---|
| Toy evaluator | `d6f644563aa8ab583efefe3b152c27b10cacb83d` |
| Nine unit tests | `e2de78b4652b26e881d89a19d15f1b8cd0ce5cae` |
| qTPU literature watch | `f0ce34676133a25b93c56fc3d955af72420aad64` |
| qTPU focused gap | `5934c79663e47b81828e819417499dd71662f8e2` |
| Daily integration report | `ca09a3bb795b89dcbb87cf6a3ef9e0312fbcf638` |
| Machine-readable integration record | `00ccab89835ddd5915c7acaa385aaba8e17de8ac` |
| Lane A contract | `22e7e2b11fdab7c56af3baadf2178a6faaed62e2` |

All these commits were written to canonical `main` with `Research-Sync: main` trailers. This Batch is the human-readable source-to-main detail record. Its own commit and subsequent navigation/ledger bookkeeping commits are self-referential bookkeeping and must be reconciled at the next audit. No unmerged branch work is represented as merged.

**CI status:** combined-status endpoint returned no status contexts for the starting head. No green status is claimed for the new commits; exact-head Actions remains the acceptance gate. The local reference harness passed 9/9 equivalent synthetic checks, but repository CI and full-suite status are **unverified**. No paid QPU job or credentials were used.

## 8. Next highest-value gate

1. Inspect exact-head GitHub Actions for the current `main`; repair feasible failures and record actual workflow/run IDs.
2. Extend the toy oracle to a second analytically known generator and add a generator-invariance residual/certificate to the benchmark contract.
3. Implement blind family/regime-held-out open-system identification with >=30 preregistered seeds, shuffled-label and non-Markovian controls, abstention, failed-candidate retention and false-discovery accounting.
4. Freeze a qTPU-inspired matched-output comparison manifest against UQPU and a strong classical tensor-network baseline before implementation; run simulator/dry-run first.
5. Continue BIO-001, FUS-001 and FIN-001 gaps in parallel; do not let A suppress D/G or E/F/H.
6. Preserve append-only history, root directives, multilingual strategic context and all INV-025–035 on every subsequent cycle.

Research-Sync: main
