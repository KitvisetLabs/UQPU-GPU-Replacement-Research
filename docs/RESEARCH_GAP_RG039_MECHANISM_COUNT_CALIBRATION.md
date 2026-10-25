# Research Gap RG-039 — calibrated model-count selection before equation discovery

**Date opened:** 2026-10-25  
**Primary owner:** Lane F — evidence and benchmark integration  
**Implementation owner:** FND-006 / EQN-001–006; Lane A contributes executable test contracts  
**Evidence state:** LITERATURE_ONLY + MODEL_ONLY_SYNTHETIC_REGRESSION_TESTS  
**UQPU project evidence promoted:** none

## Objective

Determine when a multi-equation candidate pool is justified by data rather than by search flexibility. The preprint Physical Law Ecology (arXiv:2609.08536) motivates making candidate count K explicit before equation fitting, but does not remove the need to calibrate model selection, data dependence and extrapolation.

## Current implementation delta

software/uqpu-prototype/uqpu/equation_discovery.py now contains select_bic_candidate_count, a generic Gaussian-residual BIC comparator using n*log(RSS/n)+p*log(n), plus deterministic tests for a small fit gain, a large fit gain and invalid inputs. This is a baseline helper only; it is not the paper's bespoke score, does not implement symbolic search, and does not establish the true number of physical mechanisms.

Lane A's M-QSP regression suite also adds the published nonconstructible polynomial pair from Ito et al., arXiv:2410.02332v3, Section 4, Eqs. (16)–(17), and tests both this negative fixture and a feasible fixture across tolerances 1e-12, 1e-9 and 1e-6. These tests validate a numerical software gate, not exact theorem verification or provider/hardware performance.

## Blockers

- No independent implementation of the full M-QSP recursion has been run against the same frozen fixtures.
- No exact-arithmetic certificate for the M-QSP negative fixture is implemented in UQPU.
- No independent reproduction of Physical Law Ecology has been performed.
- No calibrated false-K rates exist across noisy, correlated, overlapping-regime and unit-rescaled synthetic families.
- No selected project dataset supports a new constitutive law, quantum advantage, material substitution, bio-oil, fusion or financing claim.

## Unlock criteria

1. Freeze synthetic datasets with known candidate counts K=1, 2 and 3; preregister noise, correlations, feature distractors and held-out grouping.
2. Compare BIC, AIC and blocked held-out predictive error with the same training observations and explicit free-parameter counts.
3. Report confusion matrices, bootstrap stability, false multi-law rates and calibration across sample lengths and unit/scaling transformations.
4. Reproduce the preprint's public examples from pinned code/data and implement at least one independent baseline.
5. For M-QSP, compare the numerical decision and witness reconstruction against an independent implementation, then test boundary perturbations and exact/algebraic checks where feasible.
6. Only after these gates pass may a candidate be carried into a system-specific experiment or economics model; the experiment must have a discriminating observable and independent replication path.

## Negative-result rule

If model count is unstable or the multi-equation fit loses its held-out gain, retain the failed candidate and report the single-equation baseline. Do not reinterpret a poor fit as proof that current physics is wrong.

## Mission impact

- INV-034 / INV-035: strengthens mathematics-first invention while keeping evidence as the promotion gate.
- INV-029–033: no mission, material, accepted fuel, net-electricity or financing gate is closed by this gap artifact.
