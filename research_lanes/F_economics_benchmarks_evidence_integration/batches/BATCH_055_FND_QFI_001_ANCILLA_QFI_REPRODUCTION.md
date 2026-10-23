# Batch 055 — FND-QFI-001 exact-rational ancilla-QFI reproduction

**Date:** 2026-10-23  
**Primary owner:** Lane F — economics, benchmarks, evidence and integration  
**Source main SHA:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Related lanes:** A, C, F, H; D/G and E reviewed as downstream blockers  
**Evidence class:** MODEL_ONLY exact-rational fixture  
**Real QPU:** No; provider jobs/shots = 0

## Question and incumbent assumptions

The 2026-10-21 arXiv v1 preprint, *Evaluation of the quantum Fisher information for large systems via an ancilla* (arXiv:2610.29146v1), studies a finite-dimensional ancilla transfer protocol. Its Theorem 2 states a no-go condition when the number m of distinct nonzero local scores q_i = (partial_x p_i)/p_i exceeds ancilla dimension n, assuming the system measurement is already optimal and the conditional ancilla states are parameter-independent.

The protocol condition in the paper also states that every pair with unequal q_i and q_j must have orthogonal conditional ancilla states. The exact-rational fixture checks this rank/orthogonality condition and the associated classical Fisher information. It does not optimize arbitrary controlled unitaries or reproduce the full quantum theorem.

## Exact method

For a strictly positive finite distribution, define q_i = p_i'/p_i and I = sum_i (p_i')^2/p_i = sum_i p_i q_i^2. Group outcomes with identical q values. For each group k, P_k' = q_k P_k, so the grouped classical Fisher information equals I exactly. Such an orthogonal score-class encoding requires at least as many ancilla dimensions as distinct score classes.

The implementation accepts exact rational inputs only. It rejects floating-point inputs so near-equal scores cannot be silently merged, and rejects zero-probability/rank-boundary cases because those require a separate support-change contract.

## Results

- Two score classes, n=2: exact grouped Fisher information 1 equals the system classical Fisher information 1. This is a constructed finite classical score model, not a physical QFI-transfer or device result.
- Three distinct nonzero score classes, n=2: m=3>2, so the preprint's stated Theorem-2 condition is triggered. The exact classical Fisher information is 37/50.
- Zero-score boundary, n=2: the two distinct nonzero scores are -1 and +1, so m_nonzero=2 does not trigger Theorem 2. But the full score set is {-1,0,+1}, requiring three mutually orthogonal conditional states under the paper's pairwise condition. A two-dimensional ancilla cannot satisfy that orthogonality condition. This does not falsify Theorem 2; it shows that any sufficiency interpretation of m_nonzero<=n needs clarification when q=0 occurs.
- Near-degenerate scores: exact rationals keep 1 and 1+10^-12 distinct. The case has three nonzero score classes and n=2; the stated no-go condition is triggered.
- Zero probabilities are rejected, not patched by an arbitrary epsilon.

The machine-readable result is benchmarks/results/fnd-qfi-001-exact-fixture-2026-10-23.json. Nine unit tests cover exact-match, no-go, zero-score, near-degenerate, support-boundary, float-input, artifact consistency, the frontier-hypothesis contract, and the equation-discovery no-promotion gate.

## Fresh literature surveillance

The primary source is the official arXiv record and full v1 HTML: https://arxiv.org/abs/2610.29146v1. It was submitted 2026-10-21 and remains an unrefereed preprint in this review. The 2026-10-23 repository literature watch already records OptScientist (arXiv:2610.28562, submitted 2026-10-20) as a distinct optimization-law generator and preserves its limitations. The 2026-10-15 equation-discovery watch already includes Coupled Harness–Model Evolution (arXiv:2610.17740, submitted 2026-10-13); this cycle did not create a duplicate article. A separate 2026-10-23 GOLLuM literature watch adds a peer-reviewed uncertainty-calibrated experiment-selection hypothesis. It changes the method backlog, not any current UQPU hardware, material, bio-oil, fusion, finance or provider-execution evidence gate.

## A–I status

| Lane | Status this cycle | Evidence boundary / next gate |
|---|---|---|
| A | Priority #1 retained; QOS-AUDIT-010B25 remains the leading execution gate | QFI is not a workload win; keep identical useful-output, independent SDK and total-cost gates |
| B | Reviewed; no provider call or job | No credentials, submission, shots or billable usage |
| C | QFI/state-service distinction reinforced | No Hilbert-space or QFI-to-readable-memory equivalence |
| D | Reviewed, downstream blocked | No device requirement follows until a physical primitive and accepted workload are specified |
| E | Reviewed, no new measurements | BIO-001/FUS-001 remain unmeasured commercial gates; no material claim |
| F | Exact-rational fixture, result JSON and tests added | MODEL_ONLY; exact-commit CI and independent numerical follow-up required |
| G | D/G co-design reviewed, no device input yet | No manufacturing-equipment/process-window consequence |
| H | Literature context integrated with falsifiable follow-up | Preprint remains third-party evidence, not a new law or economic result |
| I | Reviewed, unrelated to this QFI gate | Contactless vehicle lift remains MODEL_ONLY; no field/gravity claim |

## Integration and invariants

The integration contract records all 36 A–I pairs. Active edges are A–C (state/output semantics), A–F (acceptance and evidence), A–H (EQN-OPT-001/EQN-001–006 follow-up), B–F (zero-provider accounting), C–F (no memory-equivalence promotion), D–G (co-design reviewed but blocked), E–F/E–H (BIO/FUS/finance evidence unchanged), and F–H (literature-to-falsifier workflow). Other pairs are explicitly marked N/A with rationale rather than forced coupling.

- INV-029: no physical data-center-to-phone compression demonstrated; QFI is not general compute or memory equivalence.
- INV-030: no Pangola-carbon substitution or elemental-transmutation claim.
- INV-031: no accepted-liquid fuel, yield or commercial cost evidence.
- INV-032: no net delivered fusion electricity evidence.
- INV-033: no interest/WACC change evidence; no finance-rate inference.
- INV-034: adds an exact-rational, assumption-scoped theorem-reproduction checkpoint.
- INV-035: exact arithmetic, explicit assumptions, falsifier, counterexample and independent-validation gates are preserved.
- INV-025/026/027 remain moonshots/open-frontier objectives, not achieved results.

## Next highest-value gate

Build an independent numerical QFI evaluator for small parameterized distributions and optimize the allowed controlled-unitary states for cases with m_nonzero<=n, m_nonzero>n, and q=0. Check rank changes and near-degenerate scores, independently derive the exact orthogonality condition, and resolve the zero-score interpretation before using this result in any UQPU state-service contract. Keep RG-033's read-only target snapshot and QOS-AUDIT-010B25 separate; no paid QPU execution is authorized by this artifact.

## Sync and CI

This work is being prepared on branch research/fnd-qfi-001-20261023 from main SHA c7b5958af58fad04a101ef5c6abf6a29293c867e. The PR and exact-commit CI are pending. The historical RESEARCH_GAPS, WORKLOG, DECISIONS and cold-start handoff are appended/updated in the same branch without deleting earlier history. Source-to-main merge mapping must be reconciled after review; inaccessible branches/forks are not claimed audited.
