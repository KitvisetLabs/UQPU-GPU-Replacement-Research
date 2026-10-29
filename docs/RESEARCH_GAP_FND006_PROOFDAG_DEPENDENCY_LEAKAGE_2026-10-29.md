## RG-FND006-PROOFDAG-DEPENDENCY-LEAKAGE-001 — 2026-10-29

**Status:** METADATA GUARD IMPLEMENTED / EXACT-HEAD CI PENDING  
**Primary owner:** Lane A — formal-validation tooling  
**Cross-lane owners:** Lane F — split/evidence integrity; Lane H — provenance  
**Related:** INV-034/035, FND-006, EQN-001–006, RG-FND006-PROOFEVOLVE-SCHEMA-REUSE-001

### Finding

The proof-DAG validator required referenced parents to exist and prohibited a claim family from crossing declared train/validation/test splits, but it did not constrain dependency edges by split. Consequently a train node could depend on a validation/test node, or a held-out family could import a fragment from another held-out family through a normal parent edge rather than the separately guarded schema-reuse field.

### Implemented guard

Parent dependencies may originate from training nodes. A non-training parent is permitted only for an internal edge within the same claim family and the same held-out split. This allows a proof family to contain multiple connected nodes without allowing cross-family or cross-split held-out import. Declared schema reuse remains subject to the existing verified-training-source rule.

Four synthetic regression tests cover the rejection and allowed-edge cases. This closes a metadata-level leakage path; it does not prove that datasets are genuinely disjoint, that a statement digest corresponds to semantic identity, or that a proof kernel executed.

### Required unlock

1. Run exact-head Python 3.10/3.11/3.12 and project-invariant CI.
2. Build a pinned theorem-family corpus with preregistered disjoint splits and inspect every dependency edge.
3. Compare baseline proof search and schema reuse under equal compute/time budgets.
4. Independently rerun held-out kernel-checked proof artifacts and retain failed/inconclusive attempts.
5. Report accepted-result rate, residual premises, invalid/changed statements, timeout, wall time, peak memory, energy where measurable and cost per independently accepted result.

**Non-claims:** no theorem novelty, physics result, real-QPU advantage or mission-level economic improvement is established.
