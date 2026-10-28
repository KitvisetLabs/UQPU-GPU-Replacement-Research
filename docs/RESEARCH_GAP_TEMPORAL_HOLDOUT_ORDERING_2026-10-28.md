# Research gap — chronological temporal-holdout ordering

**Gap ID:** RG-A-TEMPORAL-HOLDOUT-ORDERING-001  
**Opened:** 2026-10-28  
**Primary owner:** Lane A — benchmark/model acceptance contracts  
**Cross-lane owners:** C (state/data movement), D/G (process drift), E (physical-system models), F (evidence/economics), H (literature provenance)  
**Status:** IMPLEMENTED CERTIFICATE / REAL-DATA GENERALIZATION OPEN  
**Related:** RG-045, A-TEMPORAL-HOLDOUT-001, INV-034/035, FND-006, EQN-001–010

## Problem

A group-disjoint `TIME_BLOCK` manifest can prevent group leakage without proving that the held-out blocks occur after the training window. A random or incorrectly ordered split can therefore overstate future-time generalization.

## Implementation

`software/uqpu-prototype/uqpu/temporal_holdout.py` composes the existing raw-record-bound split-manifest validator with strict ISO-8601 timestamp parsing, UTC normalization, chronological ordering and a caller-declared embargo. It emits a deterministic certificate with dataset/manifest hashes, per-split time ranges, record/group counts and measured temporal gaps. The new test module contains 11 deterministic cases, including positive controls and fail-closed counterexamples.

## Evidence status

- The implementation and tests are committed as a software contract; exact-head GitHub Actions are required before acceptance.
- The local environment could not clone the public repository because DNS resolution failed, so this cycle does not claim a local test pass.
- No external PDE dataset, model, neural-operator splitting method, physical experiment or QPU was run.
- A PASS binds the supplied records and temporal split only. It does not authenticate an external dataset or prove physical generalization.

## Unlock criteria

1. Pass exact-head core/invariant and cold-start Actions.
2. Pin source data, license, loader, preprocessing and raw-record hashes.
3. Freeze chronological test windows and positive embargo before tuning; add parameter/geometry/law-family holdouts where relevant.
4. Run matched model/operator-splitting and trusted numerical-reference comparisons with preregistered seeds and complete compute/resource accounting.
5. Independently reproduce any claimed gain; preserve all failures and false discoveries.

## Cross-pillar non-claims

This gap does not close INV-029 phone-class physical compression, INV-030 material substitution, INV-031 accepted liquid-fuel cost, INV-032 net fusion-electricity cost, or INV-033 financing-rate reduction. No new physical law is promoted under INV-034/035.
