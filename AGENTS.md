# Autonomous Research Agent Entry Point (MANDATORY)

> **HIGHEST-PRIORITY WORKING CULTURE:** Read [00_AUTONOMOUS_RESEARCH_HANDOFF_FIRST_PRINCIPLE.md](00_AUTONOMOUS_RESEARCH_HANDOFF_FIRST_PRINCIPLE.md) first. Every research result must pass the cold-start handoff test: a new chatbot with no previous conversation can independently resume from GitHub main. This rule governs all lanes, commits and integrations; preserve evidence, safety and access controls.

Repository: KitvisetLabs/UQPU-GPU-Replacement-Research | Canonical branch: **main**

## Non-negotiable: every commit must be reflected on main
Read [the full policy](integration/MAIN_COMMIT_SYNC_POLICY_2026-10-16.md) **before any work or commit**. Every substantive commit made on any branch, worktree, or accessible fork must have a traceable **main-branch research-detail record** (not merely a SHA). Do not report source-branch work as merged until actually merged. Open a PR; when blocked, publish a pending summary on main through a separately reviewed PR and mark it pending. Reconcile untracked commits; do not bypass branch protections. The sync record's own bookkeeping commit is captured in Git history and the next audit, preventing infinite recursion.

## Start of every autonomous session
1. Fetch newest main SHA and read PROJECT_CHARTER.md, VERSION_INVARIANTS.md, GOALS.md, README.md, docs/RESEARCH_OPERATING_SYSTEM.md, docs/OPEN_FRONTIER_RESEARCH_DIRECTIVE.md, docs/KANUSANAN_PONGPANNA_MODEL.md, STRATEGIC_PLAN_REFERENCES.md, root 00–06 directives, latest dated batches/gaps/CI, and both integration policies. Never assume a fixed batch.
2. Work across **A–I concurrently**, with A quantum software Priority #1; include FND-001..006, EQN-001..006, BIO-001, FUS-001, FIN-001, and specialized research where relevant. Lane I concerns no-contact vehicle lift; never claim Earth's magnetic field or gravity manipulation already supports it.
3. Each lane owns its primary artifact in research_lanes/. For every new result scan cross-lane synergies and publish evidence-gated integration edges in integration/. Use stable IDs, pinned SHA provenance and same useful-output comparisons.
4. Search fresh literature, implement/test, record positive and negative results, gaps, CI, evidence class, next falsifier. Preserve INV-025–035, multilingual master-plan links, and no unsupported physical/economic claims.
5. Before committing, create/update a descriptive change record with branch/source SHA once known. Open/update PR to main; synchronize details promptly and reconcile status after merging. No paid QPU, purchases or hazardous vehicle tests without explicit approval.
6. End each run with newest main SHA, all A–I statuses, integrations, source commits and main sync mapping, unsynced debt, CI and next gates.

## Minimum commit detail record
source repo/branch/full SHA; timestamp; agent; lane/work ID; goal; files changed; methods; baseline; actual results/negative results; evidence tier; tests/CI; cross-lane impact; open blockers; next step; PR; main SHA/status.

**Important:** This file establishes agent instructions, not a running automatic watcher. A webhook/Actions reconciler must be implemented and verified separately. If missing access to a branch/fork, report it rather than claiming complete coverage.
