# Research gap — RG-QAOA-PARITY-001: matched higher-order parity QAOA evidence

**Opened:** 2026-10-27  
**Primary owner:** Lane A  
**Evidence/integration owner:** Lane F  
**Status:** OPEN — NOT_YET_DEMONSTRATED for UQPU; external preprint motivates a reproducible candidate only.  
**Related:** INV-025/026/027, INV-029, INV-034/035, RG-026, RG-EQN-008.

## Objective

Determine whether higher-order parity constraints improve accepted useful-solution probability for a declared sparse-graph optimization workload after accounting for extra physical qubits, two-qubit depth/gates, routing, parameter training/transfer, mitigation/decoding, host compute, I/O, energy and total cost per accepted solution.

## Current evidence

Weidinger et al., arXiv:2610.26381 (2026-10-19 submission; manuscript dated 2026-10-21), report simulation and IBM Heron experiments for signed Max-Cut on selected sparse graphs. The external study reports useful signals on its tested instances but also documents higher two-qubit depth and roughly 1.5 physical qubits per logical vertex for its 3-regular parity representation. UQPU has not independently reproduced the result. The current reviewed UQPU QAOA implementation converts QUBO to Ising and compiles direct QAOA; the present change adds a matched evidence contract, not a parity circuit.

## Blocking unknowns

- No frozen UQPU parity-encoded test manifest or independent circuit implementation exists in this change.
- No method-level comparison has been run on disjoint graph families/seeds with equal total shots and optimizer evaluations.
- No live calibration, target transpilation, real-QPU execution, energy measurement or end-to-end cost result is added.
- Exact optimality is tractable only for bounded instances; larger-instance references must carry explicit certificates or approximation bounds.
- Error-mitigation and multiple-tree decoding may increase classical compute and can change the accepted-solution probability; all of that overhead must be included.
- The external preprint's results do not establish UQPU-wide advantage or a new physical law.

## Unlock criteria

1. Freeze workload, acceptance, test-manifest and reference-certificate hashes before method tuning; keep test optimum out of parameter selection.
2. Independently verify the logical-to-physical mapping and decoding against exact enumeration on small graphs.
3. Compare direct and higher-order parity methods on the same held-out instances and same target/configuration, total shots, optimizer evaluations and repetitions.
4. Record qubits, native/routed gates and depth, parameter search, retries, mitigation/decoder work, host time, memory, data movement, reconstruction, billable usage, energy where measurable and all-in cost per accepted task.
5. Use the same provider, pricing snapshot and calibration epoch for any real-QPU economic comparison. Never combine one target's success probability with another target's price.
6. Start with target-aware simulation and dry-run. Any paid/live job requires explicit user authorization, credentials and a bounded budget.
7. Require independent replication and a preregistered threshold for a useful quality/cost improvement before closing this gap.

## Sync debt

Synchronization debt was resolved on 2026-10-27 by appending the RG-QAOA-PARITY-001 summary to RESEARCH_GAPS.md from a complete fetched snapshot; prior aggregate content was preserved as an exact prefix.
