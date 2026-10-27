# Literature watch — sparse QROM, state-preparation and block-encoding lower bounds

**Date reviewed:** 2026-10-27  
**Primary source:** Tongyang Li, Fengning Ou, Xinzhao Wang, Penghui Yao, Pei Yuan and Shengyu Zhang, Optimal T Counts under Sparsity: from QROM to State Preparation and Block Encoding.  
**Source URL:** https://arxiv.org/abs/2607.28260  
**Source version:** arXiv v2 revised 2026-10-01 (v1 submitted 2026-07-30).  
**Evidence class:** mathematical circuit-complexity theorem in the Clifford+T model; no UQPU implementation or physical measurement.

## Material result

The paper studies a fixed classical data table compiled into a quantum read-only-memory (QROM) oracle in the Clifford+T circuit model. For a table with an n-bit address, m-bit data words and at most s nonzero entries, it proves a tight worst-case T-count for exact sparse QROM:

Θ(n + min{s, sqrt(s(m + log(2^(n+1)/s)))}) for the stated sparsity range and m ≥ 2.

It also gives matching T-count bounds for sparse state preparation and sparse block encoding, with applications to quantum singular-value transformation, Hamiltonian simulation, sparse linear systems and rejection sampling. The lower-bound argument uses reductions to state preparation and counting of possible output states; it continues to apply to the paper's adaptive Clifford+T model with mid-circuit measurements and classically controlled operations.

The important project implication is that coherent data loading is an algorithmic resource cost, not a free oracle. Sparsity and promises about valid addresses can change the cost, but only when the workload actually satisfies those assumptions.

## Scope and limitations

- The theorem measures T-count in a fixed-table Clifford+T circuit model. It is not a wall-clock, physical-memory, energy or dollar-cost theorem.
- The exact sparse-QROM and promised sparse-QROM models differ. A compiler cannot use the cheaper promised-address bound unless the input contract guarantees the promise.
- Gate depth, ancillas, connectivity/routing, magic-state supply/distillation, classical preprocessing, table storage/update costs, data movement and target-specific error correction remain separate resource terms.
- Worst-case asymptotic bounds do not directly predict a particular UQPU workload's measured cost.
- This result does not equate a Hilbert-space dimension or qubit count with readable classical memory or persistent storage.

## Exact UQPU relevance

- **Lane A:** the bound is a resource reference for coherent data loading, state preparation and block-encoding routes. The compiler should retain whether a QROM address promise is actually guaranteed.
- **Lane C:** sparse data can reduce coherent-access cost under explicit sparsity assumptions, but classical table storage, data movement and output information remain real system boundaries.
- **Lane B:** no provider execution or pricing claim follows from a circuit-complexity theorem.
- **Lanes D/G:** T-count is not a fabrication or factory metric; map it to native gates, depth, ancillas and fault-tolerant resource estimates before device claims.
- **Lane F:** cost comparisons must include the full circuit, memory, preprocessing, host and energy boundary; asymptotic T-count is a model input, not measured economics.
- **FND-002 / INV-034:** this is a useful external lower-bound reference for the cost of coherently accessing classical information. It does not replace the project's own output-information or thermodynamic-gap accounting.
- **INV-035:** the result is a theorem about a declared circuit model, not a new physical law.

## Falsifiable follow-up

1. Define a workload contract with explicit n, m, s, exact versus approximate error, address-promise semantics, data-update frequency and output requirement.
2. Compare a dense/direct QROM route, sparse-QROM hashing and any candidate compressed representation on the same frozen table family. Verify outputs exactly on small fixtures.
3. Record T-count, Clifford count, depth, ancillas, classical preprocessing, table storage, host memory, transfer bytes, output reconstruction and error budget. Do not infer energy or cost from T-count alone.
4. Test held-out sparsity patterns and address distributions so the result cannot be obtained only by fitting one table family.
5. Integrate the measured/modelled loading term into end-to-end accepted-task cost and keep the evidence class explicit. No real-QPU submission is required for the first gate.

## UQPU disposition

**Decision:** add as an external mathematical resource bound for Lane A/C and FND-002 follow-up. The theorem sharpens a circuit-level cost model but does not demonstrate a UQPU advantage, physical-memory replacement or any energy/material/fusion/finance result.
