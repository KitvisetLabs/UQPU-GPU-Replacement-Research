# Pending-main synchronization record — formal-proof binding and equation-discovery literature

**Date:** 2026-10-27  
**Status:** PENDING REVIEW / NOT YET CANONICAL  
**Canonical main SHA at start:** `c60594ad8a02f20e2908c53640b66f9062479002`  
**Source PR:** [#132 — Bind formal proof artifacts and add fresh equation-discovery watch (RG-047)](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/132)  
**Source branch:** `research/2026-10-27-rg047-equation-proof-binding`  
**Source branch head:** `d7e04470f3267fbb6bc5de323d915ddb30958b96`  
**Owner lanes:** A (primary), F (evidence/integration), H (publication), with D/E consumers for symbolic material-potential literature

## Pending source commits

All of these commits are on the source branch and **are not yet merged into main**:

| Source SHA | Role |
|---|---|
| `ff00d14da856437eccc0c249de1c2180e9b1dbcb` | Batch 071 research record |
| `4aa9f5e92a95834d4daa8dfb3253f6e1009034e8` | Bind EquationHypothesis to FormalProofEvidence |
| `5f4109ed1491ebceb565a4cd7d35049bb3ba0a7c` | Initial proof identity/status regression tests |
| `75246a00e221a7c5b481e4a27aab8a9ec21b7705` | Exact theorem statement binding |
| `8c87e33346df45659d7747d0a440494d432e62a7` | Statement/status-only fail-closed tests |
| `8695b341c7f6771fa5e0ba06318022a29a92d727` | Initial daily integration report |
| `e8792a1ec7a94f41dfbb85b3580008b13b055a0c` | Initial machine-readable integration record |
| `c9577308ac889e714accd1395d924b7b1c7b4c98` | Batch 071 literature delta update |
| `83b58dbfb01253e5e1bc2318c27bef81ca18144e` | Daily report source-map update |
| `00ff03080eb996c95e4019b42e56e70a7cc6ea81` | Integration manifest source-map update |
| `f7847782e86e6a929b9917852f15e32cf7f70ac8` | Fresh literature watch: AI-Newton, symbolic material potentials, AIProver and Duffing |
| `38a0e73e097e72311c7cb9af2605efb554165658` | Batch 071 updated with new watch |
| `73130a63763c67088a892a2572e806d556a57d13` | Daily report updated with new watch |
| `02379ad33f9f705ca1ad1983f3601d0e69255dc6` | Final source branch integration-manifest update |
| `151d0288eb08fd1d16f1fe6a4f70b2af026932b6` | Update RG-047 gap with pending EquationHypothesis binding |
| `483fe362765d102b1c0511b18827e86da19f7f5b` | Update daily report with RG-047 gap status |
| `3ca85ac284278fe770136ac6a348bea5b8fe5c8c` | Link RG-047 gap update in integration manifest |
| `c1f814a387921263490b0a2143b661afa5ff260f` | Remove duplicated AI-Newton source summary; cross-link pending PR #111 |
| `e52120fd1d4cdc64240098b56c884610dfa00bca` | Update Batch 071 literature deduplication note |
| `ffd114ab189ab475df18e1589fac439917a869e5` | Update daily report with pending AI-Newton source PR |
| `d7e04470f3267fbb6bc5de323d915ddb30958b96` | Update integration manifest literature provenance |

## What the pending work changes

- Equation hypotheses with a recorded formal-proof attempt must carry a typed `FormalProofEvidence` record, bind the exact theorem statement to `formal_proof_statement`, and match equation ID, claim kind and status.
- The legacy `CHECKED` spelling cannot stand alone; it aliases only a bound kernel-checked or independently reproduced record.
- Regression tests cover status-only records, identity/status/statement mismatches, independent-reproduction metadata and non-promotion to physical-candidate readiness.
- A new literature watch records symbolic ensemble interatomic potentials, AIProver and Duffing symbolic rediscovery with limitations and falsifiable follow-ups. AI-Newton is already covered by open PR #111 and is linked rather than duplicated.
- The standalone RG-047 gap now explicitly records the proposed equation-record binding and remains partially open until exact-head CI, a pinned theorem run and independent reproduction.

## Exact-head CI status at this checkpoint

- Workflow run #1681 on code-bearing head `00ff03080eb996c95e4019b42e56e70a7cc6ea81`: Python 3.10/3.11/3.12 unit/invariant and CLI smoke steps passed; QSP/QSVT, Qiskit and reference-benchmark jobs were still in progress/queued at the last poll.
- Workflow run #1685 on final documentation head `02379ad33f9f705ca1ad1983f3601d0e69255dc6`: Python 3.10/3.11/3.12 jobs were queued at the last poll.
- The combined commit-status endpoint returned no legacy status rows. Do not report either run as fully passed until all relevant jobs complete.
- The regression tests were not executed in the connector-only local environment; hosted Actions is the test evidence path.

## Evidence boundaries and next gate

RG-047 is only partially addressed. A real theorem must still be checked using a pinned proof assistant/toolchain with exact statement, assumptions/imports, source revision, proof bytes, environment and log hashes, followed by independent reproduction. RG-046 remains open until the raw SRSD-Feynman train/validation/test files are acquired, hashed and independently reconstructed into a group-aware split manifest.

This work establishes no new physical law, QPU advantage, memory/storage replacement, Pangola-derived material substitution, accepted biomass fuel, net delivered fusion electricity, financing-rate reduction or Data-Center-to-Phone result. INV-025/026/027 and INV-029–035 remain preserved. All A–H lanes remain active; the repository's specialized Lane I program is additional.

Large append-only `RESEARCH_GAPS.md` and `WORKLOG.md` were not rewritten from partial reads. The source-to-main mapping remains pending until PR #132 is reviewed/merged and reconciled.
