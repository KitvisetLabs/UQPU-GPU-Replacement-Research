# Permanent Continuous Cross-Lane Research Integration Protocol
Date: 2026-10-16 | Status: operating directive | Scope: A–I plus FND/EQN and specialized frontiers
## Intent
All research lanes remain independently productive in parallel, while continuously searching for scientifically and economically defensible combinations that improve useful outcomes. GitHub main is canonical memory. This document supplements, never replaces, PROJECT_CHARTER.md, VERSION_INVARIANTS.md (especially INV-025–035), GOALS.md, the root 00–06 directives, multilingual strategic references, and the Research Operating System. A remains Priority #1, but no lane is silently paused.
## Integration is a continuous process, not a final assembly phase
At **every meaningful new commit, result, failed experiment, literature discovery, constraint change or daily cycle**, each agent must:
1. Read newest main and inspect changes since its last integrated SHA; never use a fixed batch.
2. Publish its own lane-owned reproducible artifact and machine-readable result contract.
3. Scan every other lane A–I and FND/EQN for potential shared inputs, bottlenecks, conflicts and synergies; also scan SCM, AI-COST, QOS/QSVT when relevant.
4. Record a candidate integration edge even if its value is negative or uncertain. Rank by expected measurable gain, feasibility, dependency readiness, safety and cost of evidence.
5. Run compatible components together in a **controlled matched baseline vs combined system** with same accepted useful output, quality, boundary conditions and accounting. A plausible mechanism alone is not a demonstrated improvement.
6. Commit a dated integration artifact and link the exact component SHAs; avoid copying canonical lane-owned content. Notify dependent lane owners via PR/issue as permissions allow.
7. Re-evaluate previous integrations when an upstream interface, result, uncertainty or assumption changes. Fail closed on stale/incompatible evidence.
## Required stable integration record
ID (INT-YYYYMMDD-NNN); owners and lanes; input artifact path+commit SHA; hypothesis and causal mechanism; interface/version; physical units/dimensions; baseline/combined output contract; quality and safety constraints; expected vs measured gain; runtime/energy/materials/CAPEX/OPEX/finance and lifecycle boundaries; negative effects/tradeoffs; uncertainty and evidence class; falsifier; rollback; status PROPOSED/READY/TESTING/REJECTED/ACCEPTED_WITH_EVIDENCE/BLOCKED; next experiment; reviewers; integration commit. Never multiply speculative savings or double-count coproduct credits. Preserve provenance for each measurement.
## Shared interface
Use `integration/` for integration edges and scoreboard, `research_lanes/` for primary lane ownership. Prefer JSON or YAML alongside human-readable markdown; unique IDs and SHA-pinned dependencies. Maximum directory depth 16. Conflicts resolved by evidence, not agent authority. Parallel agents use separate branches/PRs and rebase/refresh before merge; no concurrent overwriting of append-only canonical files.
## Mandatory cross-lane opportunity scan
- A+B+C: workload semantics, provider-neutral lowering, target execution, classical memory/transfer and cost/accepted task.
- A+D+G: compiler logical gate demand -> target-aware device controls -> manufacturable process, with calibration and uncertainty.
- C+D+E+I: storage/power electronics, magnetic materials, superconducting cooling, propulsion/levitation and thermal budgets.
- E+F+H: Pangola carbon functional materials, bio-oil accepted liquid-energy, fusion **net** electricity, logistics, financing, industrial deployment.
- A+E+F+I: control optimization, propulsion energy, acoustic constraints, system-level lifecycle economics.
- FND/EQN + every lane: alternate hypotheses must pass incumbent-assumption, dimensions, symmetry, conservation, limiting-case, falsifier, held-out prediction, independent replication and system-economics gates.
- INV-029: all combinations must eventually be assessed against actual phone-class *physical* compression, counting external infrastructure.
## Daily deliverables and agent bootstrap
On every run, inspect A–I individually, run an all-pairs candidate scan (36 possible pairs) plus selected 3+ lane combinations, prioritize high-value cross-lane experiments, report at least one tested integration or explicit BLOCKED reason with an unblock experiment. Maintain an integration opportunity backlog with both successes and failures. Publish integration scoreboard delta, links to provenance, CI status and next gate. No automatic claim promotion from MODEL_ONLY, no paid jobs or hazardous experiments without authorization.
## Acceptance
This file creates the operating contract only. Automated enforcement, scheduled agent dispatch, all-pairs scan implementation, and empirical improvements remain **NOT_YET_IMPLEMENTED** until independently committed and CI-verified.
