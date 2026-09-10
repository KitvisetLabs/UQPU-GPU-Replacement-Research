# Batch 025 — AI-Assisted Physics Equation Discovery

**Date:** 2026-09-10  
**Primary foundation:** INV-034 + new INV-035  
**Programs:** FND-006 / EQN-001…EQN-006  
**Evidence:** THEORY + SOFTWARE CONTRACT + LITERATURE REVIEW  
**REAL_QPU:** No  
**Paid QPU job:** No

## Research question

Can the project preserve present-day physics as the binding engineering baseline while also creating a permanent, AI-assisted process for proposing and testing new equations, effective laws and mathematical structures when current models leave a reproducible bottleneck or anomaly?

## Result

Yes—as a scientific-method program, not as permission to ignore known physics.

The permanent rule introduced in this batch is:

> **Imagination is unconstrained at the equation-hypothesis generation stage; technology claims remain constrained by knowledge, experiment, reproducibility and end-to-end evidence.**

This is operationalized in `06_AI_ASSISTED_PHYSICS_EQUATION_DISCOVERY.md` and `uqpu/equation_discovery.py`.

## Why the distinction matters

The project has already encountered a concrete example in Batch 023: a saved quantum-backend gate duration did not provide the matched energy quantity required to compute a defensible Margolus–Levitin speed-limit gap. INV-035 does not allow us to declare that the speed limit can simply be changed. Instead it turns the blocker into a structured research question:

1. which assumptions define the current theorem;
2. which observations would invalidate or restrict those assumptions;
3. what alternative mathematical relation is proposed;
4. what new observable differs between the incumbent and candidate;
5. which experiment or proof can decide between them;
6. only after validation, what device/algorithm consequence follows.

## Fresh literature surveillance — 2025–2026

### 1. Parallel symbolic enumeration

Ruan et al., **"Discovering physical laws with parallel symbolic enumeration"**, Nature Computational Science, published 21 November 2025 (volume 6, 2026), proposes parallel symbolic enumeration for discovering parsimonious mathematical expressions from synthetic and experimental datasets. The paper reports improved recovery accuracy and lower runtime versus evaluated baselines across more than 200 problem sets.

Source: https://www.nature.com/articles/s43588-025-00904-8

**Project relevance:** equation search can be treated as a computational search problem with explicit parsimony/generalization objectives rather than free-form formula generation.

### 2. LLM-guided physics-informed symbolic regression

Taskin, Xie and Lazebnik, **"Knowledge integration for physics-informed symbolic regression using pre-trained large language models"**, Scientific Reports, 13 January 2026, combines symbolic regression with LLM guidance to incorporate domain constraints. Importantly, the authors explicitly do not claim that the LLM itself inherently understands physics.

Source: https://www.nature.com/articles/s41598-026-35327-6

**Project relevance:** supports our decision that AI can guide hypothesis search while dimensional, symmetry and scientific-validity gates remain external and explicit.

### 3. Spatio-temporal equation discovery

Lazebnik and Liberzon, **"Moving from table to graph in physics-informed spatio-temporal symbolic regression"**, Scientific Reports, 23 May 2026, extends symbolic-regression approaches toward spatio-temporal systems where ODE/PDE structure matters.

Source: https://www.nature.com/articles/s41598-026-53882-w

**Project relevance:** future UQPU/device/fusion/material research will frequently involve dynamics and fields rather than static tabular relations; equation search must therefore support differential structure.

### 4. Neural-symbolic discovery in space physics

Ying et al., **"A neural symbolic model for space physics"**, Nature Machine Intelligence, 15 October 2025, introduces PhyE2E, a neural-symbolic system for discovering interpretable physics formulas from observational data and reports improvements on evaluated space-physics relations.

DOI: https://doi.org/10.1038/s42256-025-01126-3

**Project relevance:** provides a concrete precedent for combining learned priors, symbolic formula generation and observational validation in a real scientific domain.

### 5. AI-guided mathematical/algorithmic search

Google DeepMind's **AlphaEvolve** (May 2025) combines LLM generation with automated evaluators and evolutionary search for algorithmic and mathematical discovery. Subsequent mathematical exploration work reported systematic use across a broad portfolio of open mathematical problems.

Sources:  
https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/  
https://arxiv.org/abs/2511.02864

**Project relevance:** the useful pattern is generator -> evaluator -> retain/improve, not "LLM says equation therefore equation is true".

### 6. AI-designed physics experiments

Krenn and collaborators, **"Designing physics experiments with artificial intelligence"**, Nature, 2026, surveys AI methods that search experimental configurations and emphasizes the need for expressive search spaces, reliable simulators, computable objectives and practical constraints.

Source: https://www.nature.com/articles/s41586-026-10898-6

**Project relevance:** equation discovery should be coupled to discriminating experiment design so that new mathematical candidates can be falsified quickly.

## Software contract

`software/uqpu-prototype/uqpu/equation_discovery.py` introduces `EquationHypothesis` with mandatory fields for:

- baseline model;
- proposed equation;
- variables/units;
- assumptions/domain;
- known constraints;
- limiting cases/scaling;
- falsifier;
- discriminating observables;
- evidence level;
- provenance;
- independent-validation plan.

The promotion guard explicitly rejects a fabricated evidence label such as `AI_DISCOVERED_LAW`. Even a candidate with good held-out error cannot be promoted to a physically supported candidate unless it has evidence at an experimental/prototype tier plus independent validation. A positive gate still does not declare a universal law.

## New permanent research ladder

`EQN-001` literature surveillance  
`EQN-002` equation-recovery benchmark  
`EQN-003` constraint-aware equation generator  
`EQN-004` counterexample/falsification engine  
`EQN-005` new-physics escalation gate  
`EQN-006` equation-to-technology traceability

## Eight-lane integration

| Lane | INV-035 role |
|---|---|
| A | discover alternative computational formulations and mathematical operators, then compile only validated candidates |
| B | use cloud QPUs as experimental platforms when an equation hypothesis yields a testable quantum prediction |
| C | test information/readout/memory claims against information theory and measured output semantics |
| D | convert candidate equations into Hamiltonian/device/control observables and discriminating experiments |
| E | search constitutive/transport/reaction/energy models for materials, bio-oil, fusion and thermal systems |
| F | compare candidate vs incumbent predictive accuracy, uncertainty, resource cost and economic consequence |
| G | translate validated physical relations into manufacturing/process/metrology requirements |
| H | maintain scientific-literature surveillance, article publication and stage-gated capital allocation |

## New blocker discipline

A present physical limit is never bypassed by saying "future physics may change it." A credible challenge requires:

`assumption to challenge -> new equation -> changed prediction -> discriminating observable -> experiment/proof -> independent validation`.

Without this chain the incumbent physical constraint remains binding.

## Next experiment

**EQN-002A:** build a hidden-law benchmark from known physics equations with train/holdout regimes, noise and unit metadata. Compare at least a conventional symbolic-regression baseline and an AI-assisted candidate generator under the same expression-complexity budget. Measure exact recovery, dimensional consistency, held-out error, extrapolation failure and false-discovery rate.

A successful benchmark will validate only the *equation-discovery workflow*, not any new law of nature.

No quantum advantage, new fundamental law, 100x/100,000,000x advantage, or Data-Center-to-Phone feasibility is demonstrated by this batch.