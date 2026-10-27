# Research gap — RG-EQN-009: matched reproduction of transformer-guided symbolic regression

**Opened:** 2026-10-27  
**Primary owner:** Lane A — equation-discovery/compiler tooling  
**Cross-lane owners:** Lane F — benchmark/evidence economics; Lane H — literature/publication  
**Status:** OPEN / LITERATURE_ONLY / REPRODUCTION_NOT_RUN  
**Related:** FND-006; EQN-001–006; RG-EQN-008; INV-034/035  
**Primary source:** Zheng et al., “MOSAIC-SR: Transformer-Guided Symbolic Regression for Scientific Equation Recovery,” arXiv:2609.20997, submitted 2026-09-17; https://arxiv.org/abs/2609.20997

## Objective

Test whether transformer-generated multi-start equation sketches plus scale-aware constant fitting and local symbolic repair improve the rate of *accepted* equations under equal total resources, law-family-disjoint evaluation and the project's physics/math constraints.

## Incumbent assumption and alternative

- **Incumbent:** the existing symbolic-search baseline and other candidate methods are evaluated with the same frozen grammar, input data, held-out groups and resource budget; candidate acceptance is determined by deterministic tests, not generator confidence.
- **Alternative:** learned equation sketches may allocate search to promising regions and improve structural recovery or accepted-candidate rate after downstream checks.
- **Scope:** this is a method hypothesis about search efficiency, not an alternative physical law.

## Blocking unknowns

- UQPU has not reproduced the preprint or independently verified its headline metrics.
- Dataset/code/model hashes, exact benchmark splits, search budget, preprocessing and failure distribution have not been pinned in a UQPU experiment.
- No matched run compares MOSAIC-SR-style search with one-shot symbolic regression, progressive composition and LLM-guided search control.
- No law-family-disjoint or held-out-scale result exists in this project for this method.
- No candidate has passed the project's physical-law validation gates; no downstream device, energy or economic consequence is established.

## Unlock protocol

1. Pin code, model/checkpoint, data, dependency environment and all hashes.
2. Freeze variables/units, domain assumptions, expression grammar, preprocessing, train/validation/test groups and all acceptance metrics before tuning.
3. Run one-shot symbolic regression, transformer multi-start plus repair, progressive composition and LLM search control with equal total compute/inference budgets and at least 30 preregistered seeds where feasible.
4. Report exact structural recovery only where the target/equivalence class is known; separately report held-out prediction, scale extrapolation, sensitivity to equivalent reparameterizations, dimensional/constraint violations, counterexamples, false discoveries, failed searches, wall time, peak memory and total compute cost.
5. Preserve a baseline and negative controls; do not discard failed seeds.
6. If any candidate is proposed as physics, require incumbent assumptions, units, symmetry/conservation/causality, limiting cases, falsifier, discriminating observable, held-out prediction, proof/experiment path and independent validation under INV-035.

## Falsification and stop rules

Reject the method-advantage claim if it vanishes on held-out equation families or scale transformations, is explained by leakage or a larger compute budget, produces unstable equivalent forms, or increases cost without improving the preregistered accepted-equation metric. A proof-checked or benchmark-fitting expression remains distinct from empirical physical validity.

## Evidence/non-claims

This record is literature-only. No UQPU reproduction, local benchmark, real-QPU job, physical law, material substitution, saleable bio-oil, net fusion-electricity, WACC or Data-Center-to-Phone result is claimed.

## Sync note

The aggregate append-only `RESEARCH_GAPS.md` was not replaced because preserving its full historical prefix safely is a separate reconciliation step. This standalone gap is the primary detail record; aggregate sync debt remains OPEN.
