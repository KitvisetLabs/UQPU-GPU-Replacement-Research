# Mandatory Main-Branch Commit Detail Synchronization Policy
Date: 2026-10-16 | Owner directive | Applies to all agents, humans, branches, worktrees, forks and research lanes A–I, FND/EQN, and specialized frontiers.
## Core requirement
**Every substantive commit anywhere in the project must have its research/change details reflected in canonical `main`.** A commit on a feature branch, fork or detached worktree is NOT considered synchronized merely because it exists. `main` is the shared memory and discoverability source for all autonomous agents.
## Commit-level record contract
For each source commit record: source repository/branch and full SHA, date, author/agent (when available), lanes and work-item IDs, objective, changed files, method, assumptions, actual results and negative results, evidence class, tests/CI status, invariant impacts, cross-lane integration edges, open gaps, next action, and the `main` PR/merge/sync SHA. Clearly distinguish proposed, in-review, merged, blocked, and rejected changes.
## Reliable workflow
1. Agents read the newest `main` before starting and before publishing; never use a fixed batch.
2. Each substantive source commit carries a meaningful message and a dated summary in its branch/PR. Open/update a PR to `main` promptly. If auto-merge is authorized and checks pass, merge; otherwise request human review. Never silently force-push `main`.
3. On merge, preserve a mapping of **all source SHAs** to the resulting `main` SHA (including squash/rebase). Publish human-readable details in `main` via the merged PR, lane artifact, and dated sync ledger under `integration/`. Do not claim unmerged code exists on `main`.
4. After each merge or direct `main` commit, run a reconciliation job: enumerate commits on active registered branches and PRs since the last checkpoint; compare against recorded source-to-main mapping; identify missing records and file a sync-debt issue. Report last checked SHA and CI outcome. On forks, only registered/accessible forks can be checked.
5. For commits that cannot yet be merged, put a **clearly labeled summary of pending branch work** into `main` (via separately reviewed commit/PR) without falsely asserting that code/results are merged. Record blocker, PR, source SHA, and expected next gate.
6. Protect `main` with required CI, PR review as appropriate, and permission-limited bots. A documentation sync must not bypass code review, security, evidence gates, or branch protections.
7. Use append-only dated ledgers/unique IDs, never truncate canonical history. Handle concurrent writes with separate PRs and conflict checks.
## Recursion / impossible instantaneous atomicity
The ledger update itself is a commit. Avoid an infinite self-reporting loop: a sync/ledger-only commit is recorded automatically by Git history and may be summarized in the **next** reconciliation checkpoint. For a source commit outside `main`, no system can truthfully guarantee that it appears in `main` at the exact same instant; the enforceable target is prompt sync with explicit status and detectable debt. GitHub Actions automation must be implemented and CI-tested separately; this policy document alone does not activate a webhook or scheduler.
## Minimum daily audit
Report (a) latest `main` SHA, (b) source commits discovered, (c) merged/synchronized, (d) pending or inaccessible branches/forks, (e) sync debt, (f) CI and (g) next reconciliation action. Every agent bootstrap must read this policy and `integration/PERMANENT_CROSS_LANE_CONTINUOUS_INTEGRATION_PROTOCOL_2026-10-16.md`.
## Existing known checkpoint
Prior to this policy, `main` included `f3ebcf54c395db52c363903d14f08e7f3c0a1d1c` (Lane I research charter) and `fa5a257ccc188546f58f2f616d3886e8d0fca1e5` (continuous cross-lane integration protocol). These are main commits, not unsynchronized branch work. No claim is made that all historical branches/forks have been audited.
