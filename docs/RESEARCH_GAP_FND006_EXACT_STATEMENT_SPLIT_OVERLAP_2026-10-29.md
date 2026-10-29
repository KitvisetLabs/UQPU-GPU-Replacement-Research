# Research gap RG-FND006-EXACT-STATEMENT-SPLIT-OVERLAP-001 — exact statement identity across held-out splits

**Opened:** 2026-10-29  
**Primary owner:** Lane A — formal-validation tooling  
**Cross-lane owners:** Lane F — evidence/split integrity; Lane H — provenance  
**Status:** EXACT-DIGEST GUARD ADDED / EXACT-HEAD CI UNVERIFIED / SEMANTIC OVERLAP OPEN  
**Related:** INV-034/035, FND-006, EQN-001–006, RG-FND006-PROOFEVOLVE-SCHEMA-REUSE-001, Batch 123/124

## Finding

The Batch 123 dependency-edge guard prevents training nodes from depending on held-out nodes and blocks cross-family/cross-split held-out parent edges. A separate gap remained: two different `claim_family` identifiers could carry the same exact `statement_sha256` under different splits. The family-to-split map alone does not detect that case.

## Implemented narrow guard

The validator now rejects an identical statement digest appearing in more than one of `train`, `validation`, and `test`. A synthetic regression case uses distinct claim-family IDs but the same digest for a train and test node.

## What remains open

- Exact-byte digest identity is not semantic equivalence. Alpha-renamed, normalized, or otherwise differently serialized copies may have different hashes.
- Split manifests may be contaminated or misdeclared; hashes alone do not authenticate source data or chronology.
- Legitimate shared background lemmas must be represented as a training-split dependency, not silently duplicated as a held-out node.
- Exact-head repository CI is not yet confirmed. The local full test suite was not run because a fresh GitHub clone could not resolve DNS in the current runtime.

## Acceptance protocol

1. Require exact-head Python 3.10/3.11/3.12 and project-invariant CI.
2. Pin the source revision, license, theorem corpus, prover/kernel, dependencies and environment.
3. Freeze theorem-family-disjoint splits and audit both exact hashes and normalized/semantic statement identity where feasible.
4. Compare baseline proof search and proof-DAG schema reuse under equal compute/time budgets.
5. Independently rerun a held-out subset; preserve failed/inconclusive proofs, residual premises, timeouts and changed statements.
6. Report wall time, peak memory, energy where measurable and cost per independently accepted result.

## Evidence boundary

This is a software metadata guard, not proof-kernel execution. It does not establish theorem novelty, semantic equivalence, a new physical law, UQPU advantage, or any materials, fuel, fusion, finance or Data-Center-to-One-Phone outcome.

**Next gate:** exact-head CI, followed by pinned corpus/kernel and equal-budget independent held-out reproduction.
