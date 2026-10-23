# PISR-AUDIT-001 — source-data and generalization gap

**Date opened:** 2026-10-24  
**Owner:** Lane H, with Lane A/F support  
**Status:** PROPOSED / DATA_BLOCKED FOR SOURCE REPRODUCTION  
**Evidence class:** LITERATURE_ONLY + PROTOCOL_PROPOSAL

## Why this gap exists

Lazebnik, Mortenfeld and Liberzon (Machine Learning: Science and Technology 7, 055004, 2026-09-08; DOI 10.1088/2632-2153/ae9c8b) report a physics-informed symbolic-regression closure for particles crossing density interfaces. Their paper states that the underlying commercially sensitive data are available from the authors upon reasonable request and cannot be made publicly available at publication. The current UQPU cycle has reviewed the paper but has not obtained the data or reproduced the result.

## Required unlock

1. Request the source dataset, exact trajectory labels, preprocessing, operator configuration, random seeds, baseline implementation and scoring details.
2. If access is denied or incomplete, retain source reproduction as DATA_BLOCKED and do not infer missing data from plots.
3. Separately implement a synthetic benchmark with a known delayed/damped/oscillatory term, frozen whole-trajectory and parameter-group splits, repeated seeds, operator ablations and shuffled/no-signal controls.
4. Score equation-family recovery, held-out prediction, constraint compliance and full resource cost separately.
5. Require blind validation on new parameter groups and independent replay before any empirical or model-generalization claim.
6. For a physical mechanism claim, require an observable that distinguishes the proposed wake/recoil interpretation from alternatives, ideally simultaneous flow-field measurement; trajectory fit alone is insufficient.

## Falsification and failure retention

Reject the candidate if it fails on untouched held-out groups, if its structure is unstable under seeds/operator ablations, if shuffled data produce comparable discovery rates, if physical constraints fail, or if independent replay cannot reproduce the result. Record negative outcomes as first-class evidence.

## Mission boundary

This is a method-validation gap only. It does not establish a new physical law, UQPU advantage, device requirement, Pangola material substitution, saleable bio-oil, fusion-electricity cost reduction or financing effect.
