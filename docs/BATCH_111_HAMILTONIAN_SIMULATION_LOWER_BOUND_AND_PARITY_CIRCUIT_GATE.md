# Batch 111 — Hamiltonian-simulation lower bound and multi-cycle parity-QAOA gate

**Date:** 2026-10-29  
**Starting main SHA:** a3de2ef67dc8a487bcdab5b2b19d4a87e3302b46  
**Primary lane:** A — quantum programming/workloads/compiler/runtime  
**Secondary owner:** H — literature surveillance/publication  
**Cross-cutting:** A–H, D/G co-design, INV-025–027, INV-029–035, FND-001–006, EQN-001–EQN-010, BIO-001, FUS-001, FIN-001  
**Evidence class:** REGRESSION-TEST-ADDITION / OFFICIAL PREPRINT / REPRODUCTION GAP  
**Paid QPU execution:** not authorized or attempted

## 1. Canonical state and CI

Main was resolved dynamically at the starting SHA above. Starting-head UQPU Prototype and Project Invariants run #1976 and Autonomous Cold-Start Handoff Audit #1237 both succeeded. Those results validate only the starting head; this commit requires exact-head Actions.

The charter, invariants, goals, README, operating system, open-frontier directive, Kanusanan Pongpanna Model, strategic references, root directives 00/00A/01–06, Batches 109–110, current gaps/worklog, parity-QAOA source/tests and foundational/equation-discovery modules were inspected. The Thai, English, Chinese, Japanese, Korean and German public editions were not modified.

## 2. Lane A implementation delta

Extended software/uqpu-prototype/tests/test_parity_qaoa.py with a five-vertex/six-edge graph whose spanning-forest cycle basis contains overlapping cycles of lengths four and five. The regression checks the cycle-basis shape, enumerates all 64 physical assignments, requires the certified ground states to be feasible, compares a two-layer compiled CNOT/RZ circuit with a direct dense-statevector objective, and checks the expected 28 CNOTs for the two cycle gadgets across two layers.

The local environment could not resolve github.com during a fresh clone attempt. No local test pass is claimed. Exact-head GitHub Actions is the acceptance gate.

## 3. Literature delta and focused gap

Added the [literature watch](literature_watch/2026-10-29-hamiltonian-simulation-lower-bound.md) for Zlokapa, Allen and Harrow, “Optimal Lower Bounds for Hamiltonian Simulation,” arXiv:2607.19852, submitted 2026-07-22. The official preprint reports asymptotically tight gate and classical-query lower bounds for specified local bounded-degree Hamiltonian hard-instance families, with a coefficient-tail trade-off matching composite qDRIFT up to subpolynomial factors.

The watch records the limits: this is not a measured device result, does not directly apply to every Hamiltonian, and its classical-oracle query model is not a coherent block-encoding oracle. Additional Hamiltonian/input-state structure may permit specialized algorithms. The result does not validate the parity-QAOA circuit.

Added [RG-A-FND002-HAMILTONIAN-SIM-LOWER-BOUND-001](RESEARCH_GAP_HAMILTONIAN_SIMULATION_LOWER_BOUND_2026-10-29.md) to preregister theorem-assumption mapping, frozen coefficient profiles, exact small-instance reference, matched direct/qDRIFT/composite-qDRIFT comparisons, held-out profiles and full task-boundary accounting.

The CoSR publisher/arXiv status conflict was rechecked and remains unresolved. The existing gap stays open; no CoSR result is adopted. No new physical law or UQPU reproduction is claimed.

## 4. Explicit A–H status

- **A:** multi-cycle parity-QAOA regression added; exact-head CI pending; matched direct/parity benchmark remains open.
- **B:** provider-neutral lowering remains; no independent SDK or cloud target was run.
- **C:** bounded 64-amplitude statevector is a correctness reference only, not readable memory/storage or a scalable resource estimate.
- **D:** no new device/chip/process evidence; target-native compilation and noise/resource mapping remain open.
- **E:** BIO-001 and FUS-001 remain independent open cost gates; no material, fuel, electricity or cooling measurement.
- **F:** theorem applicability and complete oracle/state/I/O/host/energy/cost accounting remain required; no cost advantage inferred.
- **G:** continuous D/G co-design preserved; no factory/yield evidence.
- **H:** literature watch, gap, batch and integration entry published; multilingual master-plan and strategic AI-agent/funding references preserved.

## 5. Foundations, invariants and non-claims

FND-001–006 and EQN-001–EQN-010 remain active. The lower-bound paper is a mathematical algorithmic result, not a new physical law. INV-029 remains a long-horizon physical-compression goal; INV-030 remains functional material substitution/minimization/recovery/recycling/hybridization/redesign without elemental transmutation; INV-031 remains accepted-liquid-energy cost optimization; INV-032 remains net reliable delivered fusion electricity; INV-033 keeps principal/time/risk distinct from WACC/rate evidence; INV-034/035 require proof, counterexample, held-out, experiment and independent-validation gates. INV-025/026/027 remain falsifiable goals.

No QPU advantage, GPU replacement, readable-memory equivalence, 100x/100,000,000x economics, Pangola material substitution, commercial bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone milestone is established.

## 6. Next gate

Obtain exact-head CI for the multi-cycle parity-QAOA test. If green, independently review the penalty proof and circuit semantics, then run a frozen direct-versus-parity comparison with exact references, held-out graph families, equal shots/optimizer budgets, target-aware simulation and full accepted-task resource/cost accounting. In parallel, preregister bounded Hamiltonian-simulation lower-bound reproduction. No paid QPU job without explicit consent, credentials and bounded budget.
