# Research gap RG-047 — formal-proof artifact binding and verification state

**Date opened:** 2026-10-27  
**Status:** PARTIALLY ADDRESSED — standalone byte-binding contract and tests added; integration into equation-discovery records and a real pinned proof run remain OPEN  
**Primary owner:** Lane A — equation-discovery/formal evidence tooling  
**Evidence owner:** Lane F — reproducibility and evidence classification  
**Publication owner:** Lane H  
**Related:** RG-046, FND-006, EQN-001–006, INV-034/035

## Observed gap

An equation candidate can carry a formal proof status, but a status string alone does not bind the exact theorem statement, proof artifact, checker version, execution environment or log. Recent AI-mathematics literature also illustrates why “formalized” must not be read as “kernel-checked”: a survey can extract candidate proof instruments while explicitly not compiling or kernel-checking the associated Lean development.

## Change made

Added software/uqpu-prototype/uqpu/formal_proof_evidence.py with an explicit proof-state taxonomy: NOT_RUN, PROOF_TEXT_ONLY, FORMAL_STATEMENT, KERNEL_CHECKED, INDEPENDENTLY_REPRODUCED, FAILED and INCONCLUSIVE. Checked/failed attempts require an immutable source revision, statement digest, proof-artifact digest, checker name/version/command, environment digest, run-log digest and exit code. The exact-byte verifier rejects a changed proof or log. A kernel-checked record and an independently reproduced record remain distinct; failed attempts are retained.

Nine focused unit tests pass locally, including byte tampering, missing checker identity, statement-hash mismatch, and false promotion of a formal statement to a kernel-checked result.

## Scope boundary

This is a metadata and byte-integrity preflight, not a prover. It does not execute a checker, authenticate who ran it, prove that the declared log is honest, settle mathematical novelty, validate imported axioms, or establish empirical physics. A hash match establishes only that supplied bytes match a record. The empirical-physics-established field remains false for every proof state.

## Remaining blockers

1. Wire this record into the existing EquationHypothesis/discovery manifest without weakening current validation.
2. Pin a real checker and toolchain, immutable repository revision, theorem statement, imports/axioms, proof artifact and reproducible command.
3. Run the checker and independently rebuild the result; preserve failed, timeout and inconclusive states.
4. Keep mathematical theorem verification separate from physical-equation acceptance, which still needs dimensional/symmetry/conservation/causality checks, held-out prediction, falsification, experiment and independent replication.
5. RG-046 remains open: the pinned SRSD-Feynman candidate still lacks acquired raw files and computed SHA-256 values; no preregistered 30-seed matched comparison has run.

## Falsification and stop rules

Reject a KERNEL_CHECKED or INDEPENDENTLY_REPRODUCED record if required checker/environment/source metadata is missing, the checker exit code is not zero, or exact statement/proof/log bytes do not match their declared hashes. A failed proof must not be overwritten by a later success; retain both with their source revisions. Do not promote a mathematical proof to a physical law or a technology/economic claim without the separate empirical gates.

## Synchronization debt

Synchronization debt was resolved on 2026-10-27: the RG-047 summary and cycle update were appended to RESEARCH_GAPS.md and WORKLOG.md using complete fetched files as exact prefixes. This focused file remains the canonical detailed record. Root directives, INV-025/026/027 and INV-029–035, and the multilingual strategic-plan references remain unchanged.
