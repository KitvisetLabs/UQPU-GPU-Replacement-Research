# Lane A gate — pinned-SDK reconstruction of signed Max-Cut Hamiltonian

**Gate ID:** A-GATE-SIGNED-MAXCUT-SDK-001  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Interfaces:** B (provider/SDK and target identity), C (state/output and reconstruction accounting), D/G (Hamiltonian/device mapping), F (reference certificates and economics), H (cold-start publication)  
**Status:** PINNED-SDK SEMANTIC SUBGATE PASSED ON MAIN; TARGET-AWARE SIMULATION OPEN  
**Evidence class:** PINNED_SDK_ALGEBRAIC_CROSSCHECK / SOFTWARE_CONTRACT_ONLY  
**Starting main:** 42e6614db390db7b3e248bc6b383d67e9d00dd3b

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


## Execution record — 2026-10-28

The pinned SDK semantic subgate was executed on main `42e6614db390db7b3e248bc6b383d67e9d00dd3b` in [GitHub Actions run 40693966482](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40693966482), job [qiskit-verification](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40693966482/job/122836265874). Environment: Python 3.12.15, Qiskit 2.5.2. Four SDK-specific tests passed. Six fixtures and 74 computational-basis assignments were checked; maximum absolute score error was 0.0 at tolerance (10^{-12}). The complete direct-score and SDK argmax sets matched, including the minimize-negative-score convention. The full core/invariant matrix and [cold-start audit](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40693966594) also passed on that exact head.

The machine-readable certificate is `benchmarks/results/2026-10-28-signed-maxcut-qiskit-crosscheck-42e6614.json`. The original semantic plan above remains binding; the current result closes only the finite SDK/operator subgate. It does not establish QAOA quality, target-aware simulation, real-QPU behavior, quantum advantage, physical limits, energy savings or economics.

**Next gate:** provider-neutral lowering and target-aware simulation for a frozen workload/target snapshot, with exact reference values, full argmax, circuit/transpiler hashes, explicit noise/shots, state/I/O/transfer/memory/reconstruction/host-compute accounting and cost per accepted useful task only when measured. Real QPU remains NO-SUBMIT without credentials, bounded budget and explicit consent.
