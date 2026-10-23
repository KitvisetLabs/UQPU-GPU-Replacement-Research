# Formal proof metadata gate — malformed-input hardening delta

**Date:** 2026-10-23  
**Work ID:** FND6-PROOF-001-METADATA-HARDENING  
**Owner:** Lane A; evidence governance Lane F  
**Canonical start SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Regression-test commit:** d33b3fb68e9c3da01e0dd35b239acf0a24de3519  
**Evidence class:** LOCAL_FOCUSED_UNIT_TESTS_ONLY  
**Main synchronization:** pending PR #50; no merge claim

## Review finding

Review of the new metadata gate found that Python type annotations alone did not prevent malformed runtime values. A non-string digest such as null could bypass the optional-field validation and then raise an uncaught attribute error in a completeness property. Uppercase digests were normalized for validation despite the documented canonical-lowercase contract. Similar malformed theorem/identity/result values could fail outside the intended fail-closed status path.

## Change

The gate now:
- requires string types for theorem statements, identities, result labels and digest fields;
- accepts only lowercase 64-character SHA-256 digests;
- reports malformed values as INVALID_METADATA rather than treating them as complete or allowing an attribute error to escape;
- preserves the distinction between metadata completeness, actual proof checking and physical truth.

Five regression tests cover a null statement, null digest, uppercase digest, null checker identity and null result label.

## Local validation

Command: `PYTHONPATH=<isolated-package> python -m unittest discover -s tests -v`  
Result: **14 passed, 0 failed** in a temporary isolated package-shaped environment using the revised module/test content. The five added cases exercise the previously missing malformed-input paths.

This is not the full repository suite or hosted GitHub Actions CI. The exact-head workflow is expected to rerun after the branch update and must pass before merge.

## Remaining limitations / next gate

The module still validates metadata only. It does not parse proof objects, run a trusted proof assistant, authenticate logs, establish mathematical truth, or connect formal axioms to physical nature. Next, add bounded known-theorem/false-claim fixtures and two genuinely independent proof-checker backends; keep theorem verification, physical-law promotion and technology/economic evidence as separate gates.


## Cross-PR reconciliation addendum

The formal-gate backlog item is RG-041 and its integration ID is INT-20261023-005. The canonical RESEARCH_GAPS.md, WORKLOG.md and scoreboard files on this branch were restored to their exact main blobs to avoid colliding with PR #48's pending RG-036–040 / Delta 24–25 suffixes. The full gap and cycle record remain in standalone dated artifacts until a conflict-aware canonical append is possible. The latest branch-head CI status must be checked separately; no main synchronization is claimed.
