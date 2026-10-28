# Source-to-main synchronization record — Batch 097 clean v2 PR

**Recorded:** 2026-10-28  
**Canonical repository:** KitvisetLabs/UQPU-GPU-Replacement-Research  
**Base main SHA:** d04eb7987b2e3b0c82840b77e263cf2ae8e41285  
**Clean source branch:** research/2026-10-28-physics-formalization-and-qaoa-contract-v2  
**Initial clean PR head:** f04dbe1c1b354569cd465f7ad895fb5c217151fa  
**Clean source PR:** [#149 — Batch 097 v2: physical-semantic gate and signed-Max-Cut QAOA integration](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/pull/149)  
**Status:** OPEN / NOT MERGED / EXACT-HEAD CI PENDING

## Superseded attempt

PR #148 and its initial source head 013c0b10c33bf71a0d61da54870dc78df0f8466d are superseded and must not be merged. Core workflow #1896 failed the cold-start manifest assertion because evidence_class metadata for lanes A/B/C/D/F/G was outside the validator's fixed enum. The new Lane A and equation-discovery tests passed in Python 3.11; the overall job failed on metadata and Python 3.10/3.12 were cancelled. The first branch also used Research-Sync: main on unmerged commits, contrary to the pending-main rule. The failure is retained as a process/metadata result, not a scientific result.

## Current source-to-main mapping

- Main base: d04eb7987b2e3b0c82840b77e263cf2ae8e41285.
- Clean branch: research/2026-10-28-physics-formalization-and-qaoa-contract-v2.
- Initial PR #149 head: f04dbe1c1b354569cd465f7ad895fb5c217151fa.
- The handoff-sync update following PR creation advances the same source branch; the final PR head is exposed in PR metadata and still requires its own exact-head CI.
- Main merge SHA: none. No work from this PR is claimed to be merged.
- Current CI: no combined-status contexts or workflow runs had been exposed for the initial clean PR head at the time of this record. The final branch head must be checked again.

## Changed artifacts

Batch 097, the A–H integration report, two literature watches, two focused gaps, the signed-Max-Cut portable-QAOA test, equation-discovery code/tests, refreshed Lane A gate, README, WORKLOG, RESEARCH_GAPS, scoreboard and cold-start manifest.

## Review gate

Run exact-head core/invariant and cold-start checks on the final PR head. Preserve failures and fix the specific cause. Do not merge until required checks and human review are satisfied. No paid/live QPU job, physical experiment, new physical law, quantum advantage, material substitution, commercial bio-oil, net fusion electricity, lower WACC or physical Data-Center-to-Phone result is claimed.
