# Daily Eight-Lane integration — 2026-10-28 — signed Max-Cut SDK and proof-failure feedback

**Starting main SHA:** e74aa14978391209909814eb8f067131b41d9712  
**Batch:** [094 — pinned-Qiskit signed-Max-Cut reconstruction and proof-failure feedback](../docs/BATCH_094_PINNED_QISKIT_SIGNED_MAXCUT_AND_PROOF_FAILURE_CLASSIFICATION.md)  
**Primary owner:** Lane A — implementation; Lane H — literature surveillance  
**Cross-cutting:** A–H, INV-025–035, FND-001–006, EQN-001–006, BIO-001, FUS-001, FIN-001  
**Evidence class:** IMPLEMENTATION_ADDED / LITERATURE_ONLY / EXACT_HEAD_CI_PENDING_AT_AUTHORING

## What changed

1. Added a Qiskit 2.5.2 signed-Max-Cut operator builder that preserves the constant term and maps qubit 0 to the rightmost Pauli-label character.
2. Added exhaustive small-graph tests across direct, QUBO, Ising and SDK operator-diagonal scores, including complete tied argmax and optimizer-sign equivalence.
3. Added a JSON certificate runner and wired it into the existing pinned-Qiskit CI job. It is simulator/operator-only and cannot submit a paid job.
4. Added a dated literature watch for the 2026-10-27 v2 revision of Maestro (arXiv:2610.25920), focusing on failure classification, counterexamples and global replanning. The paper remains an external method claim.

## Integration gate

- **Accepted output:** every assignment in each frozen fixture has matching direct/QUBO/Ising/SDK score within the declared tolerance; complete argmax sets agree; minimizing the negative operator agrees with maximizing the declared score.
- **Failure behavior:** wrong Pauli order, missing constant, sign reversal, non-Hermitian/off-diagonal operator, non-real score, overflow or tolerance violations fail closed. Exhaustive allocation is capped at eight vertices.
- **Evidence separation:** passing unit tests is semantic SDK verification only. It is not QAOA performance, target acceptance, hardware calibration, physics validation, accepted-task cost, energy advantage or commercial evidence.
- **Literature follow-up:** pin source/toolchain; compare failure-aware replanning with a fixed baseline under identical total budgets and held-out theorem families; count false acceptance and all failures.
- **Mission/economics:** INV-029 remains a long-horizon physical-compression goal; INV-030/031/032 remain material/fuel/fusion evidence gates; INV-033 separates principal/duration effects from rate/WACC claims.

## A–H review

A receives the executable priority gate. B remains provider-neutral and no-submit. C preserves state/memory/I-O accounting. D/G remain co-designed without fabrication claims. E preserves full thermodynamic and accepted-liquid/net-electric boundaries. F controls score correctness, provenance and end-to-end economics. H preserves the multilingual strategic plan and publishes the fresh source watch.

## CI and sync

The core/invariant workflow and cold-start audit passed on the starting SHA. The new Qiskit job must be read from the new commit's exact-head Actions run. No result is inferred from the parent. README.md was updated without deleting historical sections. The large append-only WORKLOG.md and RESEARCH_GAPS.md remain unsynchronized by this commit; this report is the durable, dated handoff artifact.

**Next gate:** exact-head Qiskit verification, then inspect every assignment-level certificate row before enabling target-aware simulation. Real QPU execution remains unapproved.


## CI failure diagnosis and correction — 2026-10-28

The first exact-head run passed all three core Python matrices and failed only in the new Qiskit test's assignment ordering. Qiskit's operator diagonal is indexed by computational-basis integer with q0 as the least-significant bit; itertools.product yields a different order when zipped against the diagonal. The SDK helper's internal per-index direct-score assertion passed, and the separate nonadjacent-edge/constant check passed. The test now generates tuples from each basis index explicitly. A new exact-head Actions run is required; the original failure remains preserved as a regression finding, not silently overwritten.


## Second CI diagnosis — 2026-10-28

The second exact-head run passed all four new Qiskit unit tests. It failed at the next step because the JSON certificate runner had an unterminated string caused by a newline escape during source generation. The runner is corrected to write a literal newline using an escaped source string. This is a reproducibility-runner syntax defect, not an SDK/operator mismatch; a third exact-head run is required before acceptance.


## Post-authoring CI reconciliation — 2026-10-28

Main SHA b3252a556b61b7e566d5e057606c1f2e917d79e8 passed the exact-head prototype/invariant workflow [#1872](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40625789742) and cold-start audit [#1094](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/40625789684). The pinned Qiskit verification step is green for the frozen tiny-instance algebraic contract. The result does not promote the workload to QAOA accepted-output quality, real-QPU execution, energy or economic evidence.
