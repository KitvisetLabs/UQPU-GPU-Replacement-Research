# Research gap — RG-QAOA-PARITY-001: matched higher-order parity QAOA evidence

**Opened:** 2026-10-27  
**Primary owner:** Lane A  
**Evidence/integration owner:** Lane F  
**Status:** OPEN — PREREGISTERED_MANIFEST_AND_EXACT_REFERENCES; MATCHED_RUN_NOT_EXECUTED.  
**Related:** INV-025/026/027, INV-029, INV-034/035, RG-026, RG-EQN-008.

## Objective

Determine whether higher-order parity constraints improve accepted useful-solution probability for a declared sparse-graph optimization workload after accounting for extra physical qubits, two-qubit depth/gates, routing, parameter training/transfer, mitigation/decoding, host compute, I/O, energy and total cost per accepted solution.

## Current evidence

Weidinger et al., arXiv:2610.26381 (2026-10-19 submission; manuscript dated 2026-10-21), report simulation and IBM Heron experiments for signed Max-Cut on selected sparse graphs. The external study reports useful signals on its tested instances but also documents higher two-qubit depth and roughly 1.5 physical qubits per logical vertex for its 3-regular parity representation. UQPU has not independently reproduced the result. The current reviewed UQPU QAOA implementation converts QUBO to Ising and compiles direct QAOA; the present change adds a matched evidence contract, not a parity circuit.

## Blocking unknowns

- A 10-instance pilot manifest and exact logical reference file now exist; no matched algorithm run, independent SDK validation or target-aware simulation has been executed.
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


## 2026-10-30 update — preregistered held-out pilot manifest and exact logical references

The pilot artifacts are now committed:

- Manifest: ../benchmarks/manifests/qaoa-parity-heldout-2026-10-30.json
- Exact logical references: ../benchmarks/references/qaoa-parity-exact-references-2026-10-30.json
- Manifest regression test: ../software/uqpu-prototype/tests/test_qaoa_parity_heldout_manifest.py
- Batch and integration records: BATCH_143_PARITY_QAOA_HELDOUT_MANIFEST_AND_REFERENCE_AUDIT.md and ../integration/DAILY_CYCLE_2026-10-30_PARITY_QAOA_HELDOUT_MANIFEST.md

The 10 signed-weight fixtures are split 4/3/3 across train, validation and test, with disjoint graph families. The reference file exhaustively enumerates all logical vertex assignments (688 states in total) and preserves the complete argmax set for each instance. The manifest fixes one decoded logical output contract, parity-cycle feasibility, normalized regret, and equal proposed p=1 budgets of 8,192 shots, 32 optimizer evaluations and 10 repetitions per instance/method.

The public test references are available for audit and final scoring; they are not a secret holdout. Method and hyperparameter selection must not use test optima or reference certificates. Six isolated local tests passed for manifest/reference integrity and exhaustive recomputation. This is a MODEL_ONLY exact small-instance reference plus software contract, not a QAOA run, SDK validation, target-aware simulation, QPU result or advantage claim.

The matched direct-versus-parity comparison remains OPEN. Next gate: implement the paired runner, independently verify the SDK/operator and decoder semantics, then run target-aware simulation under the same target/configuration and budgets. Record all state, I/O, routing, host, retry, reconstruction, energy and total cost fields. Paid QPU execution still requires explicit authorization, credentials and a bounded budget.


## 2026-10-30 — RG-QAOA-PARITY-001 exact mapping audit update (Batch 144)

**Status:** OPEN / EXACT_MAPPING_AUDIT_ADDED / MATCHED_QAOA_NOT_EXECUTED. **Primary owner:** Lane A; evidence/integration owner Lane F. **Evidence:** SOFTWARE_CONTRACT + MODEL_ONLY_EXACT_SMALL_INSTANCE_REFERENCE. The new test `software/uqpu-prototype/tests/test_qaoa_parity_heldout_mapping.py` independently reconstructs the direct signed-Max-Cut QUBO and edge-parity encoding for all ten frozen fixtures. It exhaustively checks 688 logical assignments, all 7,072 parity basis strings, cycle constraints, fail-closed decoding, exact optima and complete argmax-to-ground-state correspondence. This closes a mapping/certificate audit only; it does not run QAOA, tune angles, validate an SDK, transpile to a target, measure memory/energy or demonstrate advantage. Next: paired direct-versus-parity p=1 execution under the frozen equal budget, with exact references used for scoring only.
