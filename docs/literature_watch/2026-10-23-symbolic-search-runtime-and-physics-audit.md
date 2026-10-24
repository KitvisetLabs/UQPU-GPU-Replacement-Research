# Literature watch — 2026-10-23: symbolic-search runtime and per-candidate physics audit

**Accessed:** 2026-10-23  
**Primary owner:** Lane H — literature synthesis  
**Implementation owner:** Lane A; integration/evidence owner: Lane F  
**Evidence class:** LITERATURE_ONLY / EXTERNAL METHODS  
**UQPU evidence promotion:** none

## Sources and dates

1. Zihan Yu, Shixuan Zhou, Hao Huang, Jingtao Ding and Yong Li, *SRHarness: A Harness for Agentic Symbolic Regression*, arXiv:2609.35501, submitted 2026-09-28. Official preprint: https://arxiv.org/abs/2609.35501.
2. Diab W. Abueidda, Bilal Ahmed, Panos Pantidis and Mostafa E. Mobasher, *Physics-Audited Agentic Discovery in Scientific Machine Learning*, arXiv:2607.07379, submitted 2026-07-08. Official preprint: https://arxiv.org/abs/2607.07379.

These papers are new to this cycle's repository crosswalk, not papers first published on 23 October. The 15 October UQPU watch already covers RISR (arXiv:2610.11387); this article does not duplicate its residual-informed equation-repair claims.

## Genuine methodological deltas

### SRHarness: the search runtime is part of the method

SRHarness exposes scientific actions through a common interface, retains evaluated hypotheses as persistent scientific state, and manages trajectory continuation, branching, restart and termination. Its authors report improved symbolic recovery and numerical generalization on LLM-SRBench under matched backbones, including 93.69% versus 62.16% symbolic accuracy on LSR-Transform for one reported backbone/configuration.

For UQPU, the actionable idea is to version and audit the search harness separately from the language model and candidate equation. Candidate history, experiment-design history, resource budget, splits and restarts should be reproducible inputs rather than hidden prompt memory.

### PA-SciML: candidate-level physics checks beat error-only promotion

PA-SciML fixes its evaluator before search, turns mechanics requirements into reviewable checks, tests candidate outputs against those checks, and searches prescribed input/history ranges for high-violation cases without requiring reference solution fields for every probe. In its reported transient elastodynamics example, an error-only baseline with similar mean error violates a causality check by responding to future loading history, while the selected model passes the stated check.

For UQPU, the actionable idea is to retain counterexample and physics-constraint results per candidate instead of allowing a low aggregate fit score to erase a conservation, symmetry, dimensional or causality failure.

## Limitations and evidence boundaries

- Both are method papers/preprints, not independent UQPU reproductions.
- SRHarness's reported benchmark results are tied to its benchmark, model backbones, splits and tool configuration; they do not establish physical-law discovery or lower total energy/cost.
- PA-SciML's examples are scoped to the stated solid-mechanics models and checks. Passing selected checks does not establish that all relevant physics has been encoded.
- A machine-checkable proof validates a derivation relative to formal assumptions; physical adequacy still requires discriminating observations.
- Neither paper provides QPU performance, accepted useful-task economics, critical-material substitution, saleable bio-oil, net fusion electricity, lower project WACC, or Data-Center-to-One-Phone evidence.

## Exact UQPU relevance and falsifiable follow-up

- FND-006 / EQN-001–006 / INV-035: preserve the candidate, harness, evaluator, normalization, training/selection/test splits and counterexample-search versions as separate immutable identifiers.
- Lane A: compare fixed versus branched/restarted hypothesis trajectories under equal candidate-evaluation budgets; prevent the test split from selecting the equation.
- Lane F: report wall time, evaluator calls, host compute, memory, energy where measurable, false-discovery count and cost per independently accepted candidate, not just best fit.
- Lane C: no inference from symbolic-state size to readable classical memory capacity.
- Lanes D/E/G: apply physics-audit checks only after a concrete device/material/energy model and its measured observables are specified.
- INV-029–033: these methods are upstream research tools only; no mission-level capability, material, fuel, electricity or finance claim follows.

Proposed falsifier: on a frozen synthetic ODE suite with one confounded parameter pair and one causality-violating surrogate, compare a fixed harness against a stateful/branching harness with identical compute and evaluation budgets. The proposed system fails if it (a) promotes the causality-violating model, (b) reports experiment-class exhaustion despite a declared full-rank design, (c) selects on held-out test data, or (d) reduces fit error only by violating dimensional/constraint checks. Repeat on a withheld law family before any physical use.

## Project evidence status

This is literature surveillance only. No new UQPU experiment, equation, theorem, physical law, QPU result, material/fuel/electricity result or economic advantage is established.
