# Research gap — physical-semantic faithfulness of formally checked equation candidates

**Gap ID:** RG-EQN-PHYSICS-SEMANTIC-FAITHFULNESS-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane F — evidence contracts and integration  
**Cross-lane owners:** Lane H (formalization literature), Lane A (workload semantics), Lane D/E (physical-model dictionary)  
**Status:** OPEN / CONTRACT_HARDENED_ON_BRANCH / EXACT_HEAD_CI_PENDING  
**Related:** INV-034–035, FND-006, EQN-001–EQN-006  
**Sources:** docs/literature_watch/2026-10-28-ai-assisted-physics-formalization-axqm.md

## Problem

A proof checker can establish a formal conclusion while the formal statement does not faithfully encode the intended physical claim. Examples include defining the conclusion by construction, weakening quantifiers, assuming a critical step, or omitting the physical mechanism whose behavior is supposedly derived. This is distinct from an invalid proof and distinct from a candidate that fails an empirical test.

The current EquationHypothesis contract already binds proof evidence to the exact claim ID, status, checker, source revision, artifact, environment and run log. Batch 097 adds a separate physical_interpretation_review_status and auditable notes. A formal proof alone cannot satisfy that review gate. The code and tests are on branch research/2026-10-28-physics-formalization-and-qaoa-contract; exact-head CI has not yet been observed.

## Required contract

1. Keep proof discovery, kernel verification, semantic interpretation review, held-out prediction, counterexample search, independent replication, device/system consequence and economics as separate evidence dimensions.
2. Require an independent reviewer to check that each formal variable, unit, assumption, domain and observable maps to the intended physical system and that no conclusion is smuggled into a definition or hypothesis.
3. Permit explicit FAILED and INCONCLUSIVE review states with notes; never erase disagreement or convert it into approval.
4. Do not promote a candidate relation merely because formal proof status is CHECKED, KERNEL_CHECKED or INDEPENDENTLY_REPRODUCED.
5. Keep empirical evidence requirements unchanged: a semantic review does not replace real data, held-out improvement, counterexample search or independent physical validation.

## Unlock criteria

- Batch 097 equation-discovery unit tests pass on exact branch head.
- A deliberately vacuous formal statement and a faithful known-law statement are reviewed against the same checklist.
- An independent physics reviewer signs off the model-to-observable dictionary and records assumptions/validity regime.
- The evidence ledger records false discoveries, failed review, reviewer disagreement and undecided outcomes.
- A subsequent independently reproduced physical relation passes its own data/device/economics gates before any technology claim is advanced.

## Nonclaims

No equation is promoted by this gap record. Formal correctness is not physical truth; model fit is not a new law; an external benchmark is not UQPU evidence. This gap contributes to INV-035 by preventing proof metadata from silently bypassing the physical-meaning gate.
