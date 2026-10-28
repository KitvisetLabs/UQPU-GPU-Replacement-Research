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

## 2026-10-27 update — exact graph-parity mapping baseline

The provider-neutral classical mapping oracle in software/uqpu-prototype/uqpu/parity_encoding.py now implements the logical-to-edge XOR map, a deterministic fundamental-cycle basis, validity checking and canonical decode. Seven focused tests passed locally, including exhaustive connected/disconnected graph enumeration and exact valid-assignment counts. The hosted Python unit/invariant matrix also passed on Python 3.10, 3.11 and 3.12 for code commit 717e580db4800e14b913038255a263b453d05844. This validates the mapping contract only; it does not implement the higher-order parity-QAOA circuit or close this gap. Signed-Max-Cut objective preservation, independent GF(2) rank cross-check, held-out equal-budget comparison and any QPU/economic claim remain open.

## Sync debt

Synchronization debt was resolved on 2026-10-27 by appending the RG-QAOA-PARITY-001 summary to RESEARCH_GAPS.md from a complete fetched snapshot; prior aggregate content was preserved as an exact prefix.


## 2026-10-29 update — higher-order parity circuit prototype

Added software/uqpu-prototype/uqpu/parity_qaoa.py and a focused regression suite. The implementation compiles each fundamental-cycle even-parity penalty as a higher-order Z string using CNOT/RZ phase gadgets, adds an RX mixer, and provides exact enumeration for bounded physical registers. A fail-closed penalty threshold is required when cycles exist. The mixer is not feasibility-preserving, so sampled outputs still need cycle validation and decoding.

The new dense-statevector test compares the compiled two-layer circuit with an independent direct objective definition. Exact-head CI remains required. The matched direct-versus-parity benchmark is still OPEN: no provider SDK has independently checked this new circuit, no real QPU was run, and no end-to-end advantage or cost result is established.
