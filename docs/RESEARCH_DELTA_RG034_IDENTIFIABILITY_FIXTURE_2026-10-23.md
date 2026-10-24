# Research delta — RG-034 local identifiability fixture (2026-10-23)

**Primary owner:** Lane A — equation-discovery tooling  
**Integration/evidence owner:** Lane F  
**Cross-cutting:** FND-006, EQN-001–006, INV-034, INV-035  
**Evidence:** MODEL_ONLY / SYNTHETIC_FIXTURE  
**Canonical starting commit:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Main synchronization:** pending review/merge; no canonical-main update is claimed.

## Why this gate

The main-branch RG-034 gap requires a deterministic distinction between an unsolved candidate, a locally non-identifiable candidate, and a genuinely exhausted bounded, declared experiment class. The 15 October equation-discovery watch also requires rank/null-space output and a complete design ledger before a candidate advances.

This delta implements a small dependency-free rank/null-space auditor in software/uqpu-prototype/uqpu/equation_identifiability.py. It accepts only finite rectangular sensitivity matrices and requires explicit normalization provenance. The matrix must already be dimensionless and scaled using documented observation and parameter scales; a raw dimensional Jacobian is not silently treated as comparable.

## Deterministic verdict contract

- NOT_YET_SOLVED: the candidate fit/solver has not converged. This verdict takes precedence even if the supplied matrix is full rank.
- IDENTIFIABLE: the converged primary design has full column rank in the local sensitivity test. This is not global identifiability and does not establish physical truth.
- LOCALLY_NON_IDENTIFIABLE: the primary design has a nontrivial local null direction, but the declared experiment class is not proven exhausted.
- EXPERIMENT_CLASS_EXHAUSTED: only when the caller declares the bounded class complete, at least two unique designs are supplied, and every design remains rank deficient. This does not claim that every imaginable experiment has been exhausted.

The implementation computes reduced row-echelon form and a right-null-space basis with a caller-visible relative tolerance. The bounded class-complete flag is provenance from the experiment designer; the helper cannot independently certify that the designer enumerated nature's entire possible experiment space.

## Synthetic scenarios and falsifiers

Machine-readable fixture: benchmarks/results/rg034-sens-001-identifiability.json.

- Two linear protocols with proportional sensitivity columns retain a one-dimensional null space; a declared complete two-design class receives EXPERIMENT_CLASS_EXHAUSTED.
- Adding a quadratic protocol with full rank changes the class verdict to LOCALLY_NON_IDENTIFIABLE, falsifying the exhaustion claim.
- A full-rank matrix paired with solver_converged=false remains NOT_YET_SOLVED.
- A converged full-rank primary design passes only the local rank gate.

Tests are in software/uqpu-prototype/tests/test_equation_identifiability.py. The intended next gate is to compare the analytic Jacobian against finite-difference estimates on a deliberately confounded synthetic ODE, perturb the parameter point and tolerance, and test a withheld design. Only after that should a physical model be evaluated with held-out data and an independently designed discriminating experiment.

## Literature crosswalk

This fixture is methodologically compatible with two public sources reviewed in the same cycle:

- SRHarness (arXiv:2609.35501, submitted 2026-09-28) suggests treating scientific actions, persistent candidate state, and search-trajectory branching/restart as explicit runtime objects.
- Physics-Audited Agentic SciML (arXiv:2607.07379, submitted 2026-07-08) motivates candidate-level constraint checks and counterexample searches beyond aggregate fit error.

Both are external method evidence, not UQPU results. The separate dated literature watch records their novelty, limitations and proposed tests.

## A–H integration review

| Lane | Status / dependency |
|---|---|
| A | Implements local rank/null-space audit and negative tests; next is analytic-vs-finite-difference ODE fixture. |
| B | No provider calls or target capability claims. |
| C | No classical-memory/state-capacity inference from mathematical parameter count or Hilbert-space dimension. |
| D | No device claim; a later physical experiment must expose measured observables and calibration. |
| E | No Pangola material, accepted bio-oil, fusion-electricity or cooling evidence. |
| F | Stable JSON result, tolerance, design ranks, null-space dimension and non-claim boundary; hosted CI is the acceptance gate. |
| G | No fabrication/process-window claim; D/G co-design remains downstream of measured device requirements. |
| H | Adds a falsifiable discovery-method path while preserving the Kanusanan Pongpanna Model and multilingual strategy references on main. |

## INV-029–INV-035 impact

- INV-029: improves a mathematical gate that may eventually constrain a useful workload; no physical phone compression.
- INV-030: no carbon/material substitution or transmutation claim.
- INV-031: no accepted saleable-liquid or fuel-cost result.
- INV-032: no net delivered fusion-electricity result.
- INV-033: no financed-principal, interest, risk-premium or WACC result.
- INV-034: operationalizes one bounded falsifiability gate for foundational hypotheses.
- INV-035: candidate equations remain hypotheses; dimensional, held-out, counterexample, proof/experiment and independent-validation requirements remain binding.

## Synchronization and evidence debt

The canonical RESEARCH_GAPS.md and append-only WORKLOG.md were not rewritten from partial history. This dated artifact records the RG-034 advancement and explicit sync debt. The PR must be reviewed against the current main and the existing Cycle 008 Delta 25 / Batches 057–059 branch before merge; no batch number is used as a substitute for inspecting current refs.

No provider credentials, paid QPU job, shot, funding action, material experiment, fuel/electricity measurement or new physical law was used.
