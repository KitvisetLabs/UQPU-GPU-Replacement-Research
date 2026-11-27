# AI-Assisted Quantum Gravity Research (QGR)

**Status:** Research program established; initial literature and mathematical audit pending.  
**Canonical repository:** https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research  
**Evidence policy:** No claim is promoted beyond its documented evidence class.

## Mission

Build a reproducible, open research program to examine candidate approaches to quantum gravity, understand where general relativity and quantum theory resist unification, and evaluate AI-assisted mathematical discovery methods. The goal is not to assume that a particular theory is correct. The goal is to make claims precise, test them against established results, and identify discriminating mathematical or observational tests.

## Start here

A new contributor should follow this sequence:

1. Read the repository root [README](../../README.md) and [PROJECT_CHARTER](../../PROJECT_CHARTER.md).
2. Read [Foundational Physics & Mathematics Deep Frontier](../../05_FOUNDATIONAL_PHYSICS_MATHEMATICS_DEEP_FRONTIER.md).
3. Read [AI-Assisted Physics Equation Discovery](../../06_AI_ASSISTED_PHYSICS_EQUATION_DISCOVERY.md).
4. Read the [Research Gaps register](../../RESEARCH_GAPS.md) and [Worklog](../../WORKLOG.md).
5. Read the [contributor handoff and reproducibility guide](../../docs/RESEARCH_HANDOFF_GUIDE.md).
6. Review the source paper or dataset directly before summarizing or extending it.
7. Select one bounded task from the work queue below; record assumptions and evidence before coding or proposing a new theory.

Do not rely on chat history. This repository is the canonical project memory. If an instruction in an old chat conflicts with the current repository, open a documented issue rather than silently choosing one.

## Research tracks

| Track | Scope | First deliverable |
|---|---|---|
| QGR-A: Literature and claim audit | Review candidate quantum-gravity approaches and AI-assisted discovery claims | Annotated source register with claim-level evidence |
| QGR-B: Mathematical foundations | Differential geometry, GR, QFT, operator algebras, canonical/path-integral methods | Definitions, assumptions, derivations and known-limit checks |
| QGR-C: Candidate-framework comparison | Effective field theory, asymptotic safety, loop approaches, string/holographic approaches, causal/discrete approaches and other sourced candidates | Neutral comparison matrix; no premature ranking |
| QGR-D: Black holes and information | Black-hole thermodynamics, entropy, information, semiclassical limits | Reproduce one published derivation or identify a precise gap |
| QGR-E: AI-assisted equation discovery | Symbolic regression, theorem/proof assistance, counterexample search | Benchmark on known equations before novel claims |
| QGR-F: Observational and experimental tests | Gravitational waves, cosmology, precision tests and feasible discriminators | Observable, uncertainty, competing predictions and feasibility |
| QGR-G: Simulation and computation | Reproducible symbolic/numerical calculations | Versioned code, tests, environment and data provenance |

Tracks may proceed in parallel, but interfaces and shared assumptions must be recorded so their results can be integrated.

## Initial work queue

- **QGR-001 — Source verification:** establish a verified bibliography of primary papers, publication status, versions, authorship and independent commentary. Separate peer-reviewed papers from preprints and media reports.
- **QGR-002 — Baseline map:** summarize what GR, quantum theory and quantum field theory each describe, where their domains overlap, and the specific mathematical/physical incompatibilities that motivate quantum-gravity research.
- **QGR-003 — Framework comparison:** compare candidate approaches using common criteria: mathematical definition, recovered low-energy GR, quantum consistency, unitarity/causality where applicable, known-limit recovery, observables, open problems and evidence.
- **QGR-004 — AI claim audit:** independently inspect any claim that an OpenAI model or other AI system helped derive a result. Identify exact model/version, human authorship, contribution, reproducibility and independent validation. Do not infer discovery from publicity.
- **QGR-005 — Reproduction benchmark:** reproduce selected known calculations and known equations before testing AI-generated candidates.
- **QGR-006 — Falsifiable hypothesis protocol:** require each novel candidate to specify equations, variables/units, assumptions, domain, limiting cases, conservation/symmetry checks, observable, baseline, uncertainty and a falsifier.

## Evidence labels

Use the repository's evidence taxonomy. At minimum distinguish:

- **CONCEPT:** an idea without a validated derivation.
- **THEORY:** a mathematically specified framework or derivation, not necessarily empirically confirmed.
- **MODEL_ONLY:** a model fits or computes selected cases; predictive validation is incomplete.
- **SIMULATION:** a computational result with code, inputs and reproducibility information.
- **LAB_RESULT / PUBLISHED_EXPERIMENT:** measured evidence, with method, uncertainty and provenance.
- **REPRODUCED:** an independent reproduction of a specified result; state exactly what was reproduced.

A preprint is not peer reviewed merely because it is on arXiv. A peer-reviewed publication is not automatically correct. An AI-generated equation is not a physical law.

## Mandatory research record

Every task must include: question; owner/contributor; date; source URLs and access/version date; exact claim; assumptions; mathematical definitions; method; code/data hashes where applicable; baseline; checks and tests; results; uncertainty; limitations; falsifier; evidence label; next action; and reviewer status.

## Collaboration and handoff

- Use focused branches and pull requests. Do not commit speculative conclusions directly to the main branch.
- Every PR must explain what changed, why, how to reproduce it, what evidence supports it, what remains unknown, and how it affects other tracks.
- Preserve negative results and failed attempts with enough detail to prevent repeated dead ends.
- Update the root README, this QGR index, relevant research-gap entries and WORKLOG when a material milestone is integrated into main.
- A successor must be able to continue from the repository alone: no private chat context, unstated assumptions or undocumented credentials.
- Never include secrets, access tokens, private personal data or unlicensed source material.

## Immediate next step

Begin with QGR-001 and QGR-002. Do not claim that the project has independently verified a new quantum-gravity discovery until the source audit and mathematical reproduction have actually been completed.

## How to contribute

Fork the repository, create a focused branch, follow [RESEARCH_HANDOFF_GUIDE.md](../../docs/RESEARCH_HANDOFF_GUIDE.md), and submit a pull request. Questions and proposed tasks should be opened as GitHub Issues with the relevant QGR track and evidence label.
