# Research gap RG-EQN-007 — formal verification metadata and physical prediction are distinct gates

**Date opened:** 2026-10-26  
**Primary owner:** Lane A — quantum programming/runtime equation-discovery contract  
**Cross-lane owners:** Lane F — evidence and benchmark policy; Lane H — literature publication  
**Status:** OPEN — schema/test change is not yet CI-verified and no candidate equation has been physically validated  
**Related:** INV-034/035, FND-006, EQN-001–006, RG039, RG040

## Observed gap

The prior `EquationHypothesis` contract captured a baseline model, proposed equation, units, domain, constraints, limiting cases, falsifier, observables, held-out errors, provenance and independent-validation plan. It did not require dedicated typed fields for the incumbent assumption, dimensional/symmetry/conservation/causality checks, counterexample-search status, explicit held-out prediction, proof/experiment path, formal-proof status, or false-discovery status.

The gap matters because AI-generated mathematical manuscripts, proof-assistant-checked theorems, symbolic-regression fits, simulations and physical experiments establish different things. A valid proof only certifies the frozen formal statement under its declared imports and axioms. It does not establish that the statement is a physical law.

## Change in this batch

The candidate schema now records those missing items separately. The physical-candidate discussion guard requires an allowed empirical evidence class, independent validation, held-out improvement, a completed counterexample search with no counterexample found, and no unresolved false-discovery flag. Formal proof status is separately recorded; it does not substitute for a physical experiment.

## Unlock criteria

1. GitHub Actions passes the updated equation-discovery tests and repository invariants.
2. A test fixture confirms that a missing gate, unrun/inconclusive counterexample search, counterexample finding, false-discovery flag, or absent formal-proof provenance is handled as specified.
3. One frozen mathematical obligation is checked in a pinned proof environment with theorem-statement/import hashes and an explicit axiom/admission policy; a mutated invalid control is rejected.
4. For any physical claim, preregister a discriminating observable and held-out prediction, then obtain independent experimental evidence and report uncertainty, counterexamples, failures, and total resource cost.
5. Do not use formal verification alone to promote a physical law or claim UQPU, material, fuel, fusion, finance, or Data-Center-to-Phone advantage.

## Current non-claims

No AI-generated equation is promoted. No proof checker was run in this batch. No physical experiment, real-QPU job, accepted-task cost measurement, material qualification, saleable bio-oil result, net fusion-electricity result, or financing-rate result is added.

## Sync debt

This standalone gap is not yet merged into the append-heavy aggregate `RESEARCH_GAPS.md`. Preserve both records until a safe append-only reconciliation can be made.
