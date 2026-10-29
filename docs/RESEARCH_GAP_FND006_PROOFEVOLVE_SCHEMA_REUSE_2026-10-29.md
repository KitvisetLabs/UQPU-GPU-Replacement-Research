# Research gap RG-FND006-PROOFEVOLVE-SCHEMA-REUSE-001 — proof-DAG reuse under held-out theorem families

**Opened:** 2026-10-29  
**Primary owner:** Lane A — formal-validation tooling  
**Cross-lane owner:** Lane H — literature/provenance; Lane F — resource and evidence accounting  
**Status:** METADATA GATE + SYNTHETIC TESTS ADDED; EXTERNAL REPRODUCTION NOT RUN  
**Source:** https://arxiv.org/abs/2608.26334  
**Related:** INV-034/035, FND-006, EQN-001–006, RG-EQN-007 and the formal proof evidence contract

## Objective

Test whether reusable proof fragments improve independent proof acceptance across theorem families without leaking held-out information, hiding unresolved premises, or promoting metadata checks into proof claims.

## Current implementation

- Added software/uqpu-prototype/uqpu/proof_dag_reuse.py as a graph-level validator that complements formal_proof_evidence.py.
- Requires explicit node IDs, theorem-family IDs, train/validation/test split, exact statement digest, parent list and residual-premise list.
- Rejects duplicate IDs, invalid hashes, missing parents, dependency cycles, family leakage across splits and reuse from a non-training or unverified source.
- A reused schema must be an explicit dependency and must expose residual premises or explicitly certify that the residual set is closed.
- Checked/failed nodes must bind proof-record and checker-log digests, immutable source revision, checker identity/version and exit status. Failed and inconclusive attempts remain visible.
- Eleven synthetic unit tests pass in the isolated local test run. Repository exact-head CI is the separate acceptance gate.

## Non-claims

This helper validates metadata and graph bookkeeping only. It does not execute Lean, verify a proof kernel result, prove semantic equivalence, establish theorem novelty, validate physical semantics, or demonstrate a physical law or technology advantage. Hashes identify bytes; they do not authenticate authorship or correctness.

No external ProofEvolve code, checkpoint, dataset or benchmark was independently reproduced. No QPU was used and no paid job was submitted.

## Unlock criteria

1. Pin source commit, license, theorem corpus, dependencies, prover/kernel version and environment.
2. Freeze theorem-family-disjoint splits before tuning; verify that equivalent statement transformations preserve meaning.
3. Compare baseline proof search and schema reuse under equal compute/time budgets.
4. Report success and failure by status, residual-premise count, invalid/changed-statement rate, timeout, wall time, memory, energy where measurable and total cost per independently accepted result.
5. Bind exact statements, proof artifacts, logs and environment; independently reproduce a held-out sample.
6. For physics-facing claims, require a separate physical model, unit/symmetry/conservation/causality and limiting-case checks, falsifier, observable, held-out prediction, experiment/proof and independent validation.

## Stop/falsification conditions

The reuse hypothesis is weakened if gains vanish under equal budgets or theorem-family holdout, if generated transformations alter meaning, if proof fragments depend on hidden assumptions, if residual premises are omitted, or if independent runs fail to reproduce the claimed kernel-checked status.
