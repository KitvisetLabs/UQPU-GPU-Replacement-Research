# Research Gap RG-041 — evaluator-verified reversible-circuit co-design

**Date opened:** 2026-10-25  
**Primary owner:** Lane A — quantum programming, workloads, compiler and runtime  
**Integration owner:** Lane F — benchmark/evidence economics  
**Publication owner:** Lane H  
**Evidence state:** LITERATURE_ONLY + SOFTWARE_CONTRACT_TESTS  
**UQPU advantage promoted:** none  
**Status:** OPEN

## Objective

Test whether evaluator-guided candidate generation can reduce logical resources for one selected reversible subroutine while preserving the exact same function, relative-phase semantics, ancilla cleanup, supported input domain and declared failure budget. The motivating source is Gu et al., arXiv:2610.22367v1 (submitted 2026-10-15); its reported circuit improvements are external author claims, not UQPU results.

## Current delta

The new software module, software/uqpu-prototype/uqpu/reversible_circuit_contract.py, records candidate and function-specification hashes, distinct generator/evaluator roles, verification artifacts, exhaustive basis-state coverage, proof/replica provenance, relative-phase status, ancilla-cleanup status, failure bounds, Toffoli count, peak qubits, T-depth, logical depth and optional target identity.

The comparator is fail-closed: it refuses unverified candidates and returns INCOMPARABLE when semantic hashes, input/output widths, failure budgets or target identities differ. It reports Pareto dominance/tradeoff across resource dimensions and explicitly treats Toffoli×qubits as a descriptive proxy, not a cost metric. Ten isolated unit tests passed in a Python 3.13 harness; exact-head project CI is required before merge.

This contract validates metadata consistency. It does not run a circuit simulator, verify the submitted evaluator, establish proof correctness, or demonstrate resource savings.

## Blockers

- No representative UQPU reversible primitive has yet been frozen for RVC-001.
- No LLM-generated candidate has been generated or independently evaluated by UQPU.
- No exact or formally checked correctness proof has been attached to a real candidate.
- Target-native decomposition, T-depth scheduling, routing, QEC, control, calibration, energy and device constraints are not represented by the logical-resource proxy.
- No real-QPU job, accepted useful-task result or matched classical economics measurement exists.

## Unlock criteria

1. Freeze a baseline and function specification with provenance/hash and a supported input domain.
2. Independently evaluate every basis state for a tractable domain, or check a proof artifact with explicit assumptions.
3. Verify relative phase and ancilla reset/uncomputation separately.
4. Apply the same declared failure budget to all candidates; hold out seeds/inputs where exhaustive evaluation is impossible and report residual risk.
5. Compare Toffoli count, peak qubits, T-depth, logical depth and failure bound as a Pareto frontier.
6. Lower only verified candidates to a target-aware simulator and provider-neutral compiler path.
7. Compare accepted useful output and full lifecycle cost with a competitive CPU/GPU/NPU baseline; never mix one target's probability with another target's price.

## Negative-result rule

Retain failed candidates and failed hypotheses. If no candidate is correct, no Pareto improvement survives, or target-native/QEC and accepted-task costs erase the logical improvement, record the result and do not claim advantage.

## Mission impact

- INV-029: possible software subroutine lead only; no phone-boundary or data-center capability result.
- INV-030/031/032: no carbon-material, accepted bio-oil or net-electric fusion evidence.
- INV-033: no principal, interest or WACC effect measured.
- INV-034/035: strengthens mathematics-first candidate generation with explicit verification; no new physical law.
