# Lane A gate — pinned-SDK reconstruction of signed Max-Cut Hamiltonian

**Gate ID:** A-GATE-SIGNED-MAXCUT-SDK-001  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** B (provider/SDK and target identity), C (state/output and reconstruction accounting), D/G (Hamiltonian/device mapping), F (reference certificates and economics), H (cold-start publication)  
**Status:** SPECIFIED / NOT EXECUTED  
**Evidence class:** TEST PLAN ONLY  
**Starting main:** 0970a70b0045ca79291550ef619cbfa850716996

## Frozen semantic objective

For a simple undirected weighted graph and bit assignment x_v in {0,1},

C(x) = sum over edges (u,v) of w_uv (x_u XOR x_v).

The signed weight is preserved as supplied; a negative weight remains a negative contribution when cut. With spins s_v = 1 - 2x_v, the exact score operator is

C_hat = (1/2) sum_edges w_uv I - (1/2) sum_edges w_uv Z_u Z_v.

Its computational-basis eigenvalue for bitstring x must equal C(x). If an SDK optimizer minimizes energy, it must receive -C_hat (or another explicitly documented equivalent convention); it must not silently optimize the opposite objective.

## Procedure

1. Pin the exact SDK and version, Python version, source SHA, graph serialization, Pauli/qubit ordering convention, numeric precision and objective convention. No provider target or price may be borrowed from another provider's record.
2. Implement the operator from the frozen contract using the selected SDK's native symbolic/operator type. Keep identity/constant terms in the reported score even if an optimizer can omit constants internally.
3. For every graph in the tiny-instance fixture set, enumerate every bitstring and compare (a) the existing pure-Python direct score, (b) QUBO score, (c) Ising score, and (d) the SDK operator's computational-basis expectation/eigenvalue.
4. Include negative, positive and zero edge weights; disconnected and empty graphs; vertex/edge ordering permutations; tied optima; and malformed-input controls. Preserve the complete argmax set, not only one best bitstring.
5. Verify the optimizer-sign adapter separately: maximize C and minimize -C must yield the same complete maximizer set. Include a counterexample fixture that would expose a sign reversal or omitted constant.
6. Run existing numeric-range tests. Non-finite coefficients, conversion overflow, non-finite scores, exceptions and unresolved SDK semantics fail closed.
7. Only after the independent SDK oracle passes may target-aware simulation begin. Record exact target/provider, circuit and transpiler hashes, shots, optimizer evaluations, quality/approximation ratio, latency, host compute, state/I/O, retries, reconstruction, memory, energy if measurable and total cost per accepted useful task.

## Acceptance criteria

- Exact agreement within a predeclared tolerance for all enumerated tiny-instance scores.
- Exact agreement of complete argmax sets under the frozen tie tolerance.
- Correct optimizer sign, qubit ordering and constant handling.
- Independent test author/reviewer and reproducible environment.
- No NaN/Inf, overflow, or silent fallback.
- Every failure is preserved with source/version and a minimal counterexample.

## Nonclaims and authorization boundary

This contract is a test plan, not evidence that an SDK implementation or target has been tested. Passing it would establish only objective/SDK semantic equivalence on the tested finite fixtures. It would not establish QAOA quality, speedup, quantum advantage, physical lower-bound violation, readable classical-memory equivalence, or economic superiority. Real QPU submission remains prohibited unless credentials, a bounded budget and explicit user consent are present.
