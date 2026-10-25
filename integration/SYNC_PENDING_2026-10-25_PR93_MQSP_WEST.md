# Pending-main sync record — PR #93 (M-QSP order invariance + WEST reliability)

**Record date:** 2026-10-25  
**Status:** PENDING REVIEW; SOURCE WORK IS NOT ON MAIN  
**Canonical main at source-cycle start:** `70796ef8b918fe2e95382bc49cd7016a825db7e1`  
**Source PR:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/93  
**Source branch:** `research/2026-10-25-mqsp-order-invariance-west-wall-watch`  
**Source head at sync preparation:** `79a50fe6e04c4a68b1e5632bd55b48d30130245b`

## Source change manifest

| Path | Purpose | Primary owner |
|---|---|---|
| `software/uqpu-prototype/tests/test_mqsp_constructivity.py` | Order-permutation regression for the published M-QSP nonconstructible fixture at three tolerances | Lane A |
| `docs/literature_watch/2026-10-25-west-wall-protection-long-pulse-reliability.md` | Source-bounded analysis of WEST wall protection and falsifiable reliability follow-up | Lane E |
| `docs/BATCH_064_MQSP_ORDER_INVARIANCE_AND_WEST_RELIABILITY_WATCH.md` | Dated A–H research cycle, invariant assessment, evidence boundaries and next gates | Lane H publication; Lane A primary |
| `integration/INT-20261025-021-MQSP-ORDER-INVARIANCE-WEST-RELIABILITY.json` | Cross-lane evidence/contract record and explicit sync debt | Lane F |
| `README.md` | Current canonical checkpoint pointer and evidence/CI caveat | Shared navigation |

The source branch's commit sequence includes the code test (`0844d49fb475bffe55e94e0c60b8908dd828c154`), dated literature/batch/integration artifacts and README checkpoint update. Source PR #93 is open and unmerged. Do not describe these files as already present on main.

## Method and evidence

- The M-QSP regression reorders dictionary entries only; it does not change polynomial coefficients. It expects the published nonconstructible pair to remain rejected with no witness across four deterministic orderings and tolerances (10^{-12},10^{-9},10^{-6}).
- The numerical decision is not an exact proof, a second independent implementation, or a hardware/workload result.
- The WEST preprint (arXiv:2610.11871, submitted 2026-10-08) describes long-pulse wall-protection diagnostics/ML workflows. It does not establish that active protection caused the duration record or that plant net electricity/cost improved.
- No paid QPU jobs, credentials, wet-lab work, fabrication, fusion experiment, funding or external financial action occurred.
- INV-025/026/027 and INV-029–035 are preserved; root directives 00/00A/01–06, the Kanusanan Pongpanna Model, strategic references and Thai/English/Chinese/Japanese/Korean/German public master-plan links remain unchanged.

## Exact-head CI observation

GitHub Actions run `40171773729` was associated with source head `06fdac2af2286fbc081492ad708aef6f8f3b13f8`, which contained the code/test change and all five changed paths before the later CI-status text updates. Python 3.10, 3.11 and 3.12 unit/invariant tests and CLI smoke tests passed. The finite-shot sensitivity and equal-budget QAOA steps were skipped on Python 3.10/3.11 and passed on Python 3.12. Extended QSP/QSVT jobs were still in progress or queued at last observation; no full-workflow pass is claimed. Later commits on the source branch changed only documentation/JSON/README status text; no test code changed after the successful matrix.

The starting-main combined-status endpoint returned no status contexts. The commit-workflow lookup is PR-filtered and may return no run for documentation-only commits.

## Synchronization debt and required next action

- This record itself is a separate pending-main sync proposal; it does not merge PR #93.
- Do not overwrite large append-only `WORKLOG.md`, `RESEARCH_GAPS.md` or historical scoreboards from partial reads.
- Review PR #93 under normal branch protection; verify its latest head and all required checks. If merged, record the exact source-head-to-main-SHA mapping in the next reconciliation checkpoint.
- Continue the independent M-QSP-CDA/exact-algebraic gate and FUS-001 source-data/held-out wall-event reliability gate.
