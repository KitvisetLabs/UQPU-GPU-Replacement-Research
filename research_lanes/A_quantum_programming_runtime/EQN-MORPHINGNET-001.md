# EQN-MORPHINGNET-001 — matched-budget test contract for continuous-form symbolic regression

**Date:** 2026-10-26  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Publication/source owner:** Lane H — literature provenance  
**Integration owner:** Lane F — evidence and economics  
**Evidence status:** LITERATURE_ONLY / READY_FOR_PREREGISTRATION  
**Canonical starting main:** 5fbe3d295ad6ca5b7c701f05c64899829910cbe8

## Objective

Test whether a continuous-form symbolic-regression method represented by MorphingNet improves generalization or lowers total resource cost per independently accepted formula versus strong symbolic-search and neural-symbolic alternatives under matched data, evaluation and compute budgets.

This contract does not implement MorphingNet, reproduce the source paper, or assume its author-reported results transfer to UQPU workloads.

## Hypotheses

- **H1 (method hypothesis):** for at least one preregistered class of known equations, continuous-form search can improve the held-out/extrapolation accuracy–complexity trade-off at equal total compute budget.
- **H0 (null):** the advantage disappears under matched budgets, independent split checks, structure-recovery error limits, or the complete accepted-formula cost boundary.
- **H2 (physical hypothesis, separate gate):** a candidate equation may describe a physical system only if it passes domain-specific constraints and independent tests. H1 cannot imply H2.

## Input and data contract

Every method run must share:
- immutable dataset identifier, license/provenance and content hash;
- frozen train, validation, in-domain test and extrapolation split hashes, with an explicit disjointness check;
- grouped holdouts by equation family and parameter/domain regime, not only random row splits;
- declared units/types, domain, noise model and known generating equation for synthetic tasks;
- fixed seeds, software versions, model/weight hashes and environment manifest;
- declared wall-clock budget and hardware class, plus explicit CPU/GPU time, peak memory and training/inference separation.

A run with missing hashes, overlapping splits, duplicate seed identity, non-finite metrics or inconsistent resource accounting is INCOMPARABLE and cannot be silently repaired after observing results.

## Candidate method matrix

1. MorphingNet (only when its public implementation/version and dependencies can be pinned and run).
2. Transformer formula discovery (current project proposal is open PR #98, not canonical main).
3. Chain of Symbolic Regression / progressive composition (current project proposal is open PR #56, not canonical main).
4. L2G-SR / learned structural guidance (current project proposal is open PR #104, not canonical main).
5. PySR/Operon or another justified search baseline with pinned versions and reproducible configuration.
6. A simple known-form or domain-informed baseline where appropriate.

Do not compare reported numbers from separate papers as if they were a matched experiment. If a method cannot be installed or reproduced, retain it as NOT_RUN with a reason; do not substitute its published score into the experiment.

## Budget and metric contract

Use the same task set, data splits, evaluator and declared maximum wall-clock budget. Record at minimum:
- candidate and accepted-formula counts;
- exact symbolic recovery rate on known-ground-truth tasks;
- train, held-out and extrapolation error with uncertainty across preregistered seeds;
- formula complexity using a frozen metric;
- dimensional/symmetry/conservation/causality outcomes where applicable;
- counterexamples, false discoveries, failed searches, retries and rejected candidates;
- training and inference time, CPU/GPU hours, peak memory, model size and energy if directly measured;
- structure-recovery cost and error;
- cost per independently accepted formula, only when all methods share a named cost basis and the numerator includes failed-run costs.

A missing energy or price is NULL/UNAVAILABLE, not zero. Training cost may be amortized only over a declared, measured number of accepted uses; otherwise report unamortized and sensitivity scenarios separately.

## Acceptance and falsification

A method can be called a benchmark winner only if:
1. the frozen split and resource contract validates;
2. the independent evaluator confirms the reported metrics;
3. its improvement exceeds a preregistered threshold and uncertainty criterion on held-out data;
4. extrapolation results and formula complexity are reported, not hidden behind in-domain fit;
5. all failures, counterexamples and constraint violations remain in the denominator/ledger;
6. the result reproduces from pinned artifacts.

Reject the claimed advantage if it depends on split leakage, a larger effective budget, excluded failed runs, unreported training cost, unstable seeds, poor structure recovery, non-finite behavior, violated physical constraints or lack of independent reproduction.

Passing this contract establishes at most computational benchmark evidence. A physical-law claim separately requires the incumbent assumption, candidate equation, dimensional/symmetry/conservation/causality checks, limiting cases, falsifier, discriminating observable, held-out prediction, proof/simulation where appropriate, experiment and independent validation. A theorem or numerical fit is not a device result.

## Mission mapping and non-claims

- **INV-029:** only a verified system-level effect can later contribute; no physical-compression claim.
- **INV-030:** a validated constitutive model may guide carbon/material experiments, but no elemental transmutation or substitution is implied.
- **INV-031 / BIO-001:** possible later use for conversion/upgrading models; no accepted fuel, yield or cost result.
- **INV-032 / FUS-001:** possible later use for bounded plant/material models; no net delivered electricity or lifecycle-cost result.
- **INV-033 / FIN-001:** training and time-to-evidence resources belong in future finance accounting; no principal, interest or WACC change measured.
- **INV-034:** mathematics-first candidate generation is encouraged while present physics constrains engineering claims.
- **INV-035:** AI-generated equations remain hypotheses until independent evidence passes.
- **INV-025/026/027:** no 100-million-unit replacement evidence, and no inference from Hilbert-space size to readable classical memory.

## Current result and next gate

This cycle performed source review and preregistration only. No MorphingNet implementation, external benchmark, physical dataset, real-QPU job or physical experiment was run. No project advantage is claimed.

**Next gate:** review and complete exact-head CI for the existing shared comparison work; then add MorphingNet as a method to that common harness after its source, dependencies and data provenance are pinned. Do not create a second incompatible benchmark or change the project's pinned provider/runtime path on the basis of this preprint.
