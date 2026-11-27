# QGR Parallel Research Task Board

**Status:** OPEN / UNASSIGNED. This board assigns bounded work; it does not claim research completion.
**Program index:** [QGR README](README.md)  
**Handoff protocol:** [Research Handoff Guide](../../docs/RESEARCH_HANDOFF_GUIDE.md)  
**Repository split plan:** [Repository Boundaries and Split Plan](../../docs/REPOSITORY_BOUNDARIES_AND_SPLIT_PLAN.md)

## Work packages

| ID | Workstream | Assignment | Deliverable | Dependencies |
|---|---|---|---|---|
| QGR-001 | Literature and claim audit | Verify primary sources, versions, publication status and exact claims for foundational QG papers and AI-physics claims. | Annotated bibliography and claim/evidence matrix. | None |
| QGR-002 | Mathematical foundations | Map GR, differential geometry, quantum theory/QFT and precise incompatibility/consistency questions. | Definitions, notation, sourced derivations, assumptions, units and limit checks. | Independent start; align with QGR-001 |
| QGR-003 | Candidate-framework comparison | Compare established approaches using neutral, common criteria. | Matrix of formulation, GR/QFT limits, consistency, observables, open problems and evidence. | QGR-001/002 |
| QGR-004 | AI-assisted discovery audit | Evaluate symbolic regression, theorem assistance and AI-generated equations against known results. | Benchmark protocol, leakage/counterexample checks and reproducibility report. | QGR-001/002 |
| QGR-005 | Reproduction benchmark | Independently reproduce one well-specified published derivation/calculation. | Versioned notebook/code, pinned sources/environment, tests and discrepancy report. | QGR-001/002 |
| QGR-006 | Observational/experimental tests | Identify discriminating, falsifiable tests for candidate predictions. | Observable/prediction table, uncertainty, confounders, feasibility and falsifiers. | QGR-003 |
| QGR-007 | Black holes and quantum information | Audit or reproduce one bounded result in black-hole thermodynamics, entropy, information or semiclassical gravity. | Sourced derivation, assumptions, boundary conditions, limit checks and unresolved steps. | QGR-001/002 |

## Contributor procedure

1. Read this board, the QGR index and the handoff guide.
2. Claim one task in a focused branch; include its ID in branch, commits and PR.
3. Check repository history and current literature before duplicating work.
4. Record primary sources with DOI/arXiv ID, version/date and publication status.
5. State definitions, assumptions, units, method, commands, dependencies and tests.
6. Separate results from interpretation; record negative results, uncertainty, limits and a falsifier.
7. Open a PR with reproducible artifacts. Do not self-promote unreviewed results to established findings.
8. After integration, update this board, QGR index, root README and WORKLOG.

## Evidence and status controls

Use the project's evidence taxonomy. A preprint is not automatically peer reviewed; an AI-generated equation is not a physical law; a simulation is not an experiment. No task is complete based only on a chat summary.

Allowed statuses: **OPEN**, **IN_PROGRESS**, **BLOCKED**, **IN_REVIEW**, **INTEGRATED**, **CLOSED_NOT_SUPPORTED**. Every status transition must cite a PR/commit or state the blocker.

No paid compute, external spending, credential changes, destructive actions or hazardous physical experiments are authorized by task assignment. Obtain explicit human authorization and professional safety review where applicable.

## Session handoff

Report task ID, branch/commit/PR, source versions, completed work, exact commands and test outcomes, evidence class, what was not done, blockers, and the next reproducible action.
