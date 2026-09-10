# AI Equation Discovery Literature Watch — 2026-09-10

**Lane:** H — Strategic Development / Future-Industry Research  
**Feeds:** INV-034, INV-035, EQN-001  
**Evidence type:** third-party published research / literature surveillance

## Purpose

Maintain a dated public record of developments that may improve the project's ability to generate, constrain, test or falsify new mathematical/physical equations. Inclusion here does not endorse a paper's claims as project evidence.

## Current high-signal papers and systems

### Ruan et al. — parallel symbolic enumeration
**Title:** Discovering physical laws with parallel symbolic enumeration  
**Venue:** Nature Computational Science  
**Published:** 21 November 2025  
**URL:** https://www.nature.com/articles/s43588-025-00904-8

The work frames symbolic-law discovery as efficient search over mathematical expressions with parsimony/generalization pressure and evaluates the method across more than 200 synthetic and experimental problem sets. For UQPU, the important architectural lesson is to separate candidate generation from a measurable evaluator rather than rely on unconstrained natural-language equation proposals.

### Taskin, Xie & Lazebnik — LLM-guided physics-informed symbolic regression
**Title:** Knowledge integration for physics-informed symbolic regression using pre-trained large language models  
**Venue:** Scientific Reports  
**Published:** 13 January 2026  
**URL:** https://www.nature.com/articles/s41598-026-35327-6

The paper integrates LLM-based guidance into symbolic regression while emphasizing that the LLM is not itself a guarantee of physical understanding. This maps closely to INV-035: AI may guide search, while dimensional consistency, constraints and predictive validation remain explicit gates.

### Lazebnik & Liberzon — spatio-temporal symbolic regression
**Title:** Moving from table to graph in physics-informed spatio-temporal symbolic regression  
**Venue:** Scientific Reports  
**Published:** 23 May 2026  
**URL:** https://www.nature.com/articles/s41598-026-53882-w

The work extends equation discovery to systems with spatio-temporal structure relevant to ODE/PDE-governed physics. This is directly relevant to fusion, materials, transport, fields and device dynamics, where scalar table-fitting is insufficient.

### Ying et al. — PhyE2E
**Title:** A neural symbolic model for space physics  
**Venue:** Nature Machine Intelligence  
**Published:** 15 October 2025  
**DOI:** https://doi.org/10.1038/s42256-025-01126-3

PhyE2E combines neural and symbolic techniques to infer interpretable space-physics formulas from observations. The project should study its unit-handling, decomposition and refinement pattern as a candidate design reference for EQN-002/EQN-003.

### Google DeepMind — AlphaEvolve
**Title/system:** AlphaEvolve: a Gemini-powered coding agent for designing advanced algorithms  
**Published:** 14 May 2025  
**URL:** https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/

AlphaEvolve demonstrates a generator–evaluator–evolution loop for mathematical and algorithmic search. Its relevance is methodological: candidate novelty should be coupled to executable evaluation and retention of only measured improvements.

### Georgiev, Gómez-Serrano, Tao & Wagner — mathematical exploration at scale
**Title:** Mathematical exploration and discovery at scale  
**Preprint:** arXiv:2511.02864 (2025)  
**URL:** https://arxiv.org/abs/2511.02864

The work reports LLM-guided evolutionary exploration across many mathematical problems and combines the search loop with proof-oriented systems. It supports a distinct mathematics-first route in FND-006, but mathematical success alone does not imply new physical law.

### Krenn et al. — AI-designed physics experiments
**Title:** Designing physics experiments with artificial intelligence  
**Venue:** Nature 657, 47–58 (2026)  
**URL:** https://www.nature.com/articles/s41586-026-10898-6

The review surveys AI-based search for experimental configurations and stresses search-space design, simulators, objectives and practical constraints. EQN-004/EQN-005 should couple equation proposals to experiments that distinguish the candidate from incumbent physics.

## Research interpretation

The literature supports an increasingly strong toolchain for **scientific equation discovery**, but none of these sources establishes that AI can freely override experimentally supported physical laws. The recurring successful pattern is:

```text
candidate generation
-> physics/math constraints
-> evaluator
-> held-out/generalization test
-> interpretable expression or construction
-> experimental/proof validation
```

This pattern is now the default architecture for INV-035.

## Watch criteria for future updates

Add a new entry when a paper or result materially advances one of:

- equation recovery accuracy or extrapolation;
- unit/symmetry/conservation-aware generation;
- automated theorem/proof/counterexample search;
- discovery of new experimentally validated constitutive/effective laws;
- discriminating experiment design;
- new no-go theorem or lower bound relevant to UQPU;
- credible anomaly that motivates a modified physical model;
- an AI-generated scientific relation that survives independent validation.

For every future item record publication date, source, evidence class, novelty, limitations, exact project bottleneck, and whether a new GitHub experiment should be opened.