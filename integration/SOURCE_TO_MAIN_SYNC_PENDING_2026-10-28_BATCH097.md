# Source-to-main synchronization record — Batch 097 (clean v2 attempt)

**Recorded:** 2026-10-28  
**Canonical repository:** KitvisetLabs/UQPU-GPU-Replacement-Research  
**Base main SHA:** d04eb7987b2e3b0c82840b77e263cf2ae8e41285  
**Clean source branch:** research/2026-10-28-physics-formalization-and-qaoa-contract-v2  
**Superseded attempt:** PR #148, initial source head 013c0b10c33bf71a0d61da54870dc78df0f8466d  
**Clean PR:** pending creation  
**Status:** CLEAN BRANCH REPLAY / NOT MERGED / EXACT-HEAD CI PENDING

## Why the initial attempt is superseded

PR #148 was opened with source commits carrying Research-Sync: main on an unmerged branch. This contradicts the cold-start validator and the main-commit synchronization policy, which require Research-Sync: pending-main until the work is merged. The initial observed core workflow #1896 (run 40649592251) also failed its canonical cold-start manifest assertion because the evidence_class fields for lanes A, B, C, D, F and G were not in the validator's closed enum. The Python 3.11 run executed 796 tests with 25 skips; the new signed-Max-Cut portable-QAOA and equation-discovery tests passed, but the overall workflow failed on the manifest audit. Python 3.10 and 3.12 were cancelled after the matrix failure. No cold-start workflow run was exposed.

PR #148 must not be merged. It is being superseded by a clean replay of the same 16 changed paths from the unchanged main base SHA, with valid evidence-class labels and Research-Sync: pending-main on every recreated commit. This is a process repair, not a scientific result. The old branch remains an accessible historical failed attempt until separately reconciled.

## Current source-to-main mapping

- Main base: d04eb7987b2e3b0c82840b77e263cf2ae8e41285.
- Clean source branch: research/2026-10-28-physics-formalization-and-qaoa-contract-v2.
- Clean PR number/head: to be recorded immediately after PR creation.
- Main merge SHA: none; the work is not merged.
- Exact-head CI: pending for the clean source branch.

## Changed artifacts

Batch 097, the A–H integration report, two literature watches, two focused gaps, the signed-Max-Cut portable-QAOA test, equation-discovery code/tests, refreshed Lane A gate, README, WORKLOG, RESEARCH_GAPS, scoreboard and cold-start manifest.

## Review gate

Run exact-head core/invariant and cold-start checks. Preserve failures and fix the specific cause. Do not merge until required checks and human review are satisfied. No paid/live QPU job, physical experiment, new physical law, quantum advantage, material substitution, commercial bio-oil, net fusion electricity, lower WACC or physical Data-Center-to-Phone result is claimed.
