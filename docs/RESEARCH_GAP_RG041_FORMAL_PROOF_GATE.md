# RG-041 — Formal theorem-discovery provenance and independent replay

**Date:** 2026-10-23  
**Status:** IMPLEMENTED_METADATA_GATE / LOCAL_TESTS_14_OF_14 / EXACT_HEAD_CI_PENDING / THEOREM_BENCHMARK_OPEN  
**Primary owner:** Lane A; evidence governance and integration: Lane F; publication: Lane H  
**Related:** FND-006, EQN-001–006, INV-034, INV-035  
**Canonical starting main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Integration record:** INT-20261023-005  
**Sync state:** standalone gap artifact on PR #50 branch; canonical RESEARCH_GAPS.md append is deferred until the concurrent PR #48 RG-036–040 suffix is reconciled.

## Objective

Prevent AI-assisted theorem discovery from being treated as verified mathematics or physical law without reproducible proof-check provenance and independent replay.

## Current evidence

The metadata gate is implemented in `software/uqpu-prototype/uqpu/formal_proof_gate.py`, with focused tests in `software/uqpu-prototype/tests/test_formal_proof_gate.py`. The isolated local test run passed **14/14** cases on the revised module/test contents. It checks runtime field types, canonical lowercase SHA-256 digests, result/exit-code consistency, matching theorem/axiom/proof digests, and distinct primary/independent checker identities/build digests.

Evidence class: **LOCAL_FOCUSED_UNIT_TESTS_ONLY**. The exact branch-head hosted CI is pending. This module validates metadata only: it does not parse proof objects, run a proof assistant, authenticate logs, prove a theorem, or connect axioms to nature.

## Blockers

- Exact-head GitHub Actions CI after the latest code and reconciliation commits.
- A bounded theorem-discovery benchmark with known theorems, false claims, inconsistent premises, altered proof bytes and held-out theorem families.
- Two genuinely independent proof-checker backends and an independently reviewed replay record.
- Measured proof-search/checker runtime, memory, proof-artifact size, energy and cost where available.
- Safe canonical append-only synchronization after PR #48's RG-036–040 update is reconciled.

## Best current alternative

Keep the gate metadata-only and fail closed on malformed records. Do not claim proof verification or physical truth until the actual named checker is run on the exact proof object and independent replay is independently audited.

## Unlock criteria

1. Exact-head CI passes.
2. All malformed and mismatched metadata controls fail closed.
3. A known-theorem/false-claim benchmark is frozen before execution.
4. Two independent checkers validate the same theorem statement, axiom set and proof-object bytes with distinct checker builds and separate logs.
5. Proof validity is reviewed separately from the question of whether axioms model nature.
6. Any physics challenge states the incumbent assumptions, alternative equation, dimensions, symmetries, conservation, causality, limits, falsifier, discriminating observable, held-out prediction, experiment/proof and independent validation.
7. Append this record to canonical RESEARCH_GAPS.md only after the conflicting PR suffixes are reconciled.

## Next experiment

Implement FND6-PROOF-001 using a small set of trusted known theorems, intentionally false claims, changed axiom sets, modified proof bytes and two independent proof-checker backends. Record false positives, false negatives, wall time, memory and artifact sizes. Keep theorem verification, physical-law promotion, device/system consequence and economics as separate gates.

## Non-claims and safety

No new theorem, physical law, QPU advantage, material substitution, saleable bio-oil, net fusion electricity, financing-rate reduction, or Data-Center-to-One-Phone capability is established. No provider session, QPU job, shot, payment, material purchase, or capital deployment occurred.
