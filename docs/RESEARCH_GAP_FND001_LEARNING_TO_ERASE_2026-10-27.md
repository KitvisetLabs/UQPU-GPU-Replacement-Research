# Research gap RG-FND001-LEARNING-TO-ERASE-001 — reversible learning and thermodynamic work

**Opened:** 2026-10-27  
**Status:** OPEN / THEORY_ONLY / REPRODUCTION_NOT_RUN  
**Primary owner:** Lane F — thermodynamic accounting and evidence  
**Source/publication owner:** Lane H  
**Implementation owner if unlocked:** Lane A  
**Cross-lane consumers:** C, F, H; FND-001, FND-002, FND-006, EQN-001–006, INV-034/035

## Objective

Determine whether a pinned, independently reconstructed learning-to-erase theorem can provide a useful and correctly scoped model for UQPU's information-erasure accounting, while separating ideal logical work from actual circuit, memory, control, error-correction, refrigeration and wall-plug energy.

## Source and evidence class

Haimeng Zhao, Yuzhen Zhang and John Preskill, “Learning to erase quantum states: thermodynamic implications of quantum learning theory,” npj Quantum Information 12, Article 137 (published 2026-05-27; version of record 2026-08-20), DOI https://doi.org/10.1038/s41534-026-01273-4.

The peer-reviewed theoretical paper constructs reversible learning-to-erase protocols for scoped classes of distinguishable quantum states when the learning algorithm outputs a state-preparation circuit description. It gives efficient protocols attaining an information-theoretic Landauer work cost for certain efficiently learnable state classes and a computational no-go result for some classes under explicit cryptographic assumptions. The source states that it generated or analyzed no experimental dataset. UQPU has not independently reconstructed the proof or reproduced a protocol.

## Current blockers

- Exact theorem and supplementary-information assumptions have not been independently transcribed into a machine-checkable UQPU record.
- No selected finite state family, frozen input manifest, independent learning implementation or reversible-uncomputation test exists in UQPU.
- No measured work, wall-plug energy, refrigeration/control overhead or device-maintenance cost is available.
- The paper's idealized accounting isolates logical irreversibility; some results assume a trivial Hamiltonian and leave implementation overhead to future work.
- Cryptographic assumptions in the no-go result are conditional mathematical assumptions, not empirical observations.

## Unlock criteria

1. Pin the version-of-record article and supplementary information; extract the state-class definition, distinguishability requirement, preparation-circuit description, sample complexity, work expression, ancilla conditions and cryptographic assumption.
2. Independently reconstruct the theorem/proof and its scope before translating any result into a software contract.
3. Preregister a finite, efficiently described state family with known preparation circuits and disjoint held-out states. Include both a structured learnable family and an explicitly assumption-scoped hard-family model.
4. Implement the learning and inverse/uncomputation path; test failure branches and verify that all ancillas/workspace are returned to the declared state.
5. Compare the theorem's ideal work expression and Landauer reference with a deliberately under-informed baseline. Record state-class size m, copies N, sample count s, circuit description bytes, classical runtime, circuit depth/gates, workspace, error-correction assumptions, uncertainty and failures.
6. Keep logical work, intrinsic energy, device energy and whole-system wall-plug energy as separate fields with explicit boundaries. No physical-energy claim is allowed without a separate instrumented experiment.
7. Independently rebuild the result and retain failed, inconclusive and out-of-scope cases.

## Falsifier and stop rules

Stop or downgrade the claim if the chosen states do not satisfy the source's distinguishability assumptions, the learner does not output the required circuit description, ancillas are not restored, the proof relies on an unrecorded prior or cryptographic assumption, the independent proof reconstruction fails, or an apparent benefit depends on omitting learning/runtime/workspace costs. A mismatch in scope is not proof that the source theorem is false; it means the proposed UQPU application is unsupported.

## Mission relevance and non-claims

- **FND-001:** improves the accounting model for active memory and logical erasure only after reproduction.
- **FND-002:** keeps state-class information distinct from readable classical output/storage.
- **FND-006 / EQN-001–006:** supplies a theorem-led, falsifiable path for formal reconstruction and counterexample search.
- **INV-034/035:** mathematics may suggest new methods, but current thermodynamic constraints remain binding until a precise, discriminating result justifies a scoped revision.

This gap is not evidence of a better Landauer bound, quantum speedup, UQPU energy advantage, readable-memory equivalence, commercial energy/fuel/fusion result, financing benefit, or Data-Center-to-One-Phone compression. No QPU job is authorized by this record.
