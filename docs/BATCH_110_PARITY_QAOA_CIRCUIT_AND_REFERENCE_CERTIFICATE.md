# Batch 110 — higher-order parity-QAOA prototype and exact reference certificate

**Date:** 2026-10-29  
**Starting main SHA:** 6eafdd40f73c4db40fc78ec553bb8eb426c156ff  
**Primary lane:** A — quantum programming/workloads/compiler/runtime  
**Cross-cutting:** B/C/F/H and D/G co-design; INV-025–027, INV-029–035; FND-001–006; EQN-001–EQN-010  
**Evidence class:** PROTOTYPE / EXACT SMALL-INSTANCE CLASSICAL CERTIFICATE / NO QPU EXECUTION  
**Paid QPU execution:** not authorized or attempted

## 1. Implementation

Added software/uqpu-prototype/uqpu/parity_qaoa.py. It builds a higher-order parity objective over edge bits, assigns a penalty to every odd-parity fundamental cycle, converts cycle penalties into higher-order Z strings, and lowers those strings into provider-neutral CNOT/RZ phase gadgets with an RX mixer. It records the objective offset, edge ordering, cycle constraints, penalty, bit order and evidence level in program metadata.

The penalty is fail-closed: when cycles exist, penalty_weight must exceed twice the sum of absolute edge costs. Under the declared objective this ensures that an infeasible assignment cannot beat all feasible assignments. The product-RX mixer does not preserve cycle feasibility, so sampled outputs must be checked for cycle parity and decoded; this limitation is explicit in metadata.

Added software/uqpu-prototype/tests/test_parity_qaoa.py. The triangle test enumerates all 8 physical assignments, checks the exact optimum against the feasible optimum and confirms that optimal edge assignments decode/re-encode canonically. An independent dense-statevector test compares the compiled CNOT/RZ higher-order phase gadget against the direct objective definition for two QAOA layers. Malformed inputs and insufficient penalties are rejected.

## 2. Evidence boundary

This is a provider-neutral circuit prototype plus an exact bounded classical reference. It is not a real-QPU result, not a matched performance benchmark and not a quantum-advantage claim. The triangle's 3 physical edge qubits are not a scalable-resource estimate. Larger instances need exact certificates or rigorous bounds, matched CPU/GPU/NPU baselines, target-aware simulation and full output/energy/cost accounting.

The circuit has a standard RX mixer, not a feasibility-preserving mixer. Its penalty strength may affect trainability and spectral scale. Future comparisons must freeze the same workload, acceptance predicate, total shots, optimizer evaluations, held-out graph families and reference certificates for direct and parity-encoded methods.

## 3. A–H integration

- **A:** first higher-order parity-QAOA circuit and exact small-instance certificate are now present; real matched simulation and objective acceptance remain open.
- **B:** portable instructions only; no provider job submitted. Adapters need independent SDK/lowering checks before target-aware simulation.
- **C:** physical edge-qubit count, state representation, measurement output and reconstruction are explicit; no readable classical-memory equivalence is inferred.
- **D:** no device result; target-native gate synthesis and noise/resource estimates remain future gates.
- **E:** BIO-001 and FUS-001 remain independent full-system cost gates; no material/fuel/electricity result.
- **F:** exact objective and feasible-ground-state predicates are added; total cost/energy per accepted useful task remains unmeasured.
- **G:** D/G co-design continues; no chip/fab/yield evidence.
- **H:** canonical batch and integration record preserve the open-source research handoff and permanent strategic context.

## 4. Foundational and permanent invariants

FND-001–006 and EQN-001–EQN-010 remain active. The cycle penalty is a mathematical modeling choice, not a new physical law. INV-029 remains an ultimate physical-compression goal; INV-030–033 receive no new material/fuel/fusion/finance evidence; INV-034/035 retain proof, falsification and physical-validation requirements. INV-025/026/027 remain falsifiable moonshots, not achieved claims.

## 5. Next gate

Run the new unit tests and exact-head CI, then independently verify the parity-QAOA output distribution against the direct dense reference (already specified as a regression test). Next compare parity and direct QAOA on a frozen graph suite with equal shots and optimizer evaluations, held-out graph families, decoded objective certificates, target-aware simulation, and complete host/state/I/O/memory/energy/cost accounting. No paid QPU job without explicit consent and a bounded budget.
