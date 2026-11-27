# Research Handoff Guide — Cold-Start Contributor Protocol

**Purpose:** Any researcher, developer, AI assistant or future conversation must be able to continue this project from the repository alone.

## 1. Canonical source of truth

- The GitHub repository is the durable project memory.
- Read the root README and the required-reading list before doing work.
- Treat current committed files, open issues and accepted decisions as authoritative.
- Chat transcripts, generated summaries and verbal plans are not canonical until documented and reviewed in GitHub.
- If two repository documents conflict, record the conflict in an issue and do not silently overwrite either position.

## 2. Cold-start sequence

1. Read root README and PROJECT_CHARTER.
2. Read VERSION_INVARIANTS and RESEARCH_OPERATING_SYSTEM.
3. Read the relevant foundational, lane and technical documents.
4. Read RESEARCH_GAPS, DECISIONS and the latest WORKLOG entries.
5. Inspect the latest commits, open pull requests, CI results and unresolved review comments.
6. Identify the next explicitly unblocked task. Do not repeat completed work without a reason.
7. Before implementation, state the task, expected artifact, acceptance criteria, dependencies and risk.

## 3. Required task record

Every research task must state:

- Unique task ID and title
- Research question and why it matters
- Current accepted baseline and source
- Hypothesis or claim, clearly labeled
- Definitions, variables, units, assumptions and domain
- Method and exact steps
- Data/source provenance, version, license and hashes where relevant
- Code, environment and dependency versions where relevant
- Tests, controls, known-limit checks and independent cross-checks
- Results, including null/negative results
- Uncertainty, limitations and possible confounders
- Falsifier or condition that would reject the claim
- Evidence class and reviewer status
- Next action, dependencies and handoff notes

## 4. Evidence and language discipline

Never present a proposal, preprint, simulation, fitted model or AI-generated result as an experimentally established discovery. Distinguish mathematical consistency from physical truth, numerical success from independent reproduction, and a paper's claims from the evidence actually shown.

Use dated primary sources where possible. Verify title, authors, version, publication venue and DOI/arXiv identifier. Record disagreements and credible criticism. Do not fabricate citations, model names, experiments, peer review or tool results.

## 5. Branch, test and integration protocol

- Work on a focused branch; keep changes small and reviewable.
- Run the relevant tests and report exact commands and outcomes. If tests cannot be run, say why and mark them NOT RUN.
- Open a pull request with a concise summary, evidence, reproduction steps, limitations and cross-lane impact.
- Do not merge around failing or missing required checks.
- Integrate only after review and required CI. Update root README and WORKLOG after integration.
- Preserve history; do not rewrite or truncate unrelated records.

## 6. AI assistant operating contract

An AI successor must:
- Begin by reading repository documents rather than asking the user to repeat project context.
- Never claim it has performed a search, simulation, experiment, commit or verification unless the corresponding tool result or artifact exists.
- Separate sourced facts, calculations, assumptions, hypotheses and speculation.
- Ask the user only for decisions that cannot be resolved from repository policy or evidence.
- Avoid paid compute, external spending, public announcements, credential changes or destructive operations without explicit authorization.
- Keep research reproducible and make handoffs understandable to a human newcomer.

## 7. End-of-session handoff template

At the end of each work session, update the relevant log with:

```text
Task ID:
Date (UTC):
Contributor / agent:
Branch / commit / PR:
Question:
Work completed:
Artifacts changed:
Sources and versions:
Commands / tests and exact outcomes:
Evidence class:
What was not done:
Open blockers / risks:
Next recommended action:
Instructions for the next contributor:
```

## 8. Definition of a successful handoff

A handoff succeeds only when a new contributor with repository access—but no access to the prior chat—can identify the project goal, current state, evidence, unfinished work, exact next step and how to reproduce the preceding result.
