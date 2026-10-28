# Research gap RG-EQN-009 — independent audit of high-impact external AI theorem claims

**Opened:** 2026-10-28  
**Status:** OPEN / EXTERNAL_CLAIMS_PENDING_INDEPENDENT_REVIEW  
**Primary owner:** Lane H — source provenance and literature publication  
**Cross-lane owners:** Lane A — formal artifacts/tooling; Lane F — evidence, resource and decision gates  
**Related:** INV-034–035, FND-006, EQN-007, RG-EQN-008, INV-029–033  
**Source watch:** [2026-10-28 external AI mathematics, complexity and QFT claims](literature_watch/2026-10-28-openai-math-complexity-qft-claims-verification-boundary.md)

## Objective

Create a reproducible, claim-by-claim audit path for the mathematics, computational-complexity and constructive-quantum-field-theory claims announced by OpenAI on 2026-10-26. Keep the source's claims, exact formal statements, proof-checker results, independent expert validation, physical correspondence and downstream technology consequences as distinct evidence objects.

This gap is an instance-specific application of [RG-EQN-007](RESEARCH_GAP_EQN007_FORMAL_VERIFICATION_AND_PHYSICAL_PREDICTION.md), not a replacement for its schema-level requirements.

## Current evidence

- The official announcement links a natural-language mathematics write-up and Lean formalization for a claimed local-smoothing result, and a natural-language computer-science write-up and Lean formalization for a claimed ETH refutation.
- Public scope pages identify formalized mathematical statements. UQPU has not independently cloned, hash-pinned, compiled or reviewed the artifacts in this cycle.
- The announcement says the constructive-QFT artifacts are being withheld while an external group examines the result. The QFT claim is therefore artifact-blocked for independent reproduction.
- Exact-head CI was green on the cycle's starting commit, but those checks validate the repository state, not these external claims.

## Blocking unknowns

- Exact source commit, manuscript bytes, licenses, dependency locks and toolchain versions for the two public developments.
- Proof-checker build logs, imported axioms, admitted goals, dependency graph, and the relationship between each formal theorem and its natural-language claim.
- Independent assessment of novelty, prior work, theorem assumptions and statement fidelity.
- For ETH: independent reconstruction of the algorithm and asymptotic resource bounds under the declared encoding; the precise consequences for conditional lower bounds and finite workloads remain unknown.
- For QFT: public definitions, proof source, assumptions, dependency/environment data and an independently reviewable statement are not yet available.
- No discriminating physical experiment or UQPU workload result follows from the announcement.

## Acceptance contract

1. **Provenance:** freeze repository commit, all relevant manuscript/proof bytes, license, toolchain, dependencies and build instructions; compute hashes before execution.
2. **Formal check:** build in a clean pinned environment and record exact command, logs, imported axioms/admissions and dependency graph. Compilation is necessary but not sufficient for independent validation.
3. **Statement audit:** an independent reviewer maps each natural-language claim to the exact formal statement and checks hypotheses, definitions, prior results and scope. Include intentionally mutated/invalid controls where feasible.
4. **ETH audit:** reconstruct the counting algorithm, input encoding, time/space bounds and proof dependencies. Record the exact lower-bound consequences that follow if accepted; do not infer a practical UQPU speedup without a separate benchmark.
5. **QFT audit:** keep status DATA_BLOCKED until reviewable public artifacts exist; then require independent mathematical-physics review before any change to the project model.
6. **Physical promotion:** any candidate equation intended to change an engineering claim must additionally pass dimensional, symmetry, conservation, causality, limiting-case, held-out-prediction, counterexample, experiment and independent-replication gates required by INV-035.
7. **Economics:** any later technology consequence must use an identical accepted-useful-output contract and full resource accounting. No cross-provider price/probability mixing and no inferred WACC reduction.

## Required outcome labels

Use separate labels for SOURCE_CLAIM, ARTIFACT_AVAILABLE, KERNEL_CHECKED, INDEPENDENTLY_REPRODUCED, EXPERT_REVIEWED, PHYSICALLY_VALIDATED, and ENGINEERING_ADVANTAGE_DEMONSTRATED. A later stage never follows automatically from an earlier one.

## Cross-pillar status

- **INV-029:** no Data-Center-to-One-Phone capability, energy, physical-compression or lifecycle-cost gate is closed.
- **INV-030/031:** no Pangola functional-material substitution or accepted saleable-liquid result is supplied.
- **INV-032:** no reliable net delivered fusion electricity or lifecycle-cost result is supplied.
- **INV-033:** no financing rate/WACC result; absolute interest changes only through measured principal/time/terms.
- **INV-034/035:** advances the formal-evidence audit path while leaving present physical constraints binding.
- **INV-025/026/027:** the universal subsystem moonshots and broad research frontier remain preserved and unproven.

**Next gate:** freeze and independently compile the public math/ETH artifacts; record QFT as blocked until public proof artifacts are released. No paid QPU execution is needed or authorized for this task.
