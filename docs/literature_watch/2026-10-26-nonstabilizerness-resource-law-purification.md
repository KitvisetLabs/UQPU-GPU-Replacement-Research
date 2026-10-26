# Literature watch — 2026-10-26: quantitative nonstabilizer resources for universal state purification

**Observed / recorded:** 2026-10-26  
**Primary source:** Keming He, Enji Xiong and Xin Wang, “A Nonstabilizerness Resource Law for Universal Quantum State Purification,” arXiv:2607.08626 (submitted 2026-07-09).  
**Official preprint:** https://arxiv.org/abs/2607.08626  
**Related peer-reviewed primary source:** Keming He et al., “No-Go Theorems for Universal Quantum State Purification via Classically Simulable Operations,” *Physical Review Letters* 136, 090204 (published 2026-03-04), DOI: 10.1103/bdw8-k91v.  
**Official journal record:** https://journals.aps.org/prl/abstract/10.1103/bdw8-k91v  
**Primary owner:** Lane A — quantum programming, workloads, compiler/runtime  
**Publication support:** Lane H — strategic research and publication  
**Integration owner:** Lane F — evidence, benchmark and economics  
**Evidence class:** ARXIV_PREPRINT + RELATED_PEER_REVIEWED_THEOREM; LITERATURE_ONLY_FOR_UQPU  
**Promotion:** no UQPU implementation, quantum advantage, new physical law, energy/material/fuel/fusion/finance result, or Data-Center-to-Phone result promoted

## Why this result matters

The related March 2026 *Physical Review Letters* paper proves that deterministic and probabilistic protocols restricted to classically simulable operations cannot achieve universal two-to-one quantum-state purification for qubits or systems of any odd dimension. Its three- and four-copy extensions are described as semidefinite-programming/numerical evidence, so those extensions must not be silently upgraded to the same theorem status.

The July 2026 preprint adds a quantitative resource-theory result: it reports an exact linear mana law for universal two-copy purification in odd dimensions, a two-sided linear robustness law for multi-qubit systems (exact for a single qubit), and an explicit successful purification map. This is a useful new literature lead because it moves from a qualitative no-go boundary toward a resource-versus-fidelity/success-probability accounting problem.

This watch was found by fresh public-literature surveillance and is newly recorded for this repository; it is not a claim that the work was published today. The July result is an arXiv preprint, and the project has not independently reproduced its theorem or calculations.

## Genuine novelty and evidence class

- **Published theorem boundary:** the related peer-reviewed no-go result excludes universal two-to-one purification under the paper's classically simulable-operation assumptions for qubits and odd dimensions.
- **Preprint contribution:** the newer work reports quantitative lower/resource tradeoffs using nonstabilizerness measures (mana and robustness) and supplies a constructive purification map.
- **Project value:** it suggests a way to turn an abstract state-quality target into an explicit resource requirement before estimating circuit depth, repetitions, host work or cost per accepted output.
- **What it is not:** neither paper demonstrates a general quantum speedup, an end-to-end cheaper workload, or that all error correction/error mitigation fails. The theorem is scoped to specified purification tasks and operation/resource classes.

## Limitations and interpretation boundary

1. The July 2026 source is a preprint, not an independent UQPU reproduction.
2. The exact theorem statements, definitions of mana/robustness, dimensional assumptions, success-probability conventions and proof dependencies must be checked against the full source before coding a reproduction.
3. A resource monotone is not automatically a count of physical T gates, magic states, shots, joules, dollars or device time. Any mapping to hardware resources requires a separately justified compilation/resource model.
4. Purification fidelity alone is not an accepted useful output. A future workload contract must also freeze the target state/task, success criterion, output reconstruction, failure handling, copies consumed, latency and total cost.
5. Numerical semidefinite-program results for three/four copies must remain distinct from proved statements; numerical feasibility or infeasibility is not a proof without a certified bound.
6. No claim about RAM/VRAM/storage replacement follows. Quantum-state dimension is not equivalent to readable classical storage, and the source does not measure data movement or persistence.
7. No implication follows for Pangola carbon/material substitution, saleable bio-oil, net delivered fusion electricity, project interest/WACC, or phone-class physical compression.

## Exact UQPU relevance

- **Lane A / INV-019–021:** add a scoped resource-bound check before treating a purification primitive as a provider-neutral algorithmic building block. Any candidate must be evaluated on the same accepted-output contract as a competitive classical/hybrid baseline.
- **Lane B:** future provider comparisons must pin the target, circuit, calibration, shots and success-probability provenance. No provider job is authorized by this watch.
- **Lane C:** include input-copy count, intermediate state materialization, output reconstruction and host memory/I/O in any eventual system boundary; do not convert a resource-theory quantity into storage bytes.
- **Lanes D/G:** no device/process change is justified unless an independently validated resource tradeoff changes a concrete gate, control, readout or packaging requirement.
- **Lane E / INV-030–032:** no direct biomass, accepted-fuel, materials or fusion-electricity consequence is established.
- **Lane F / INV-033:** cost must be reported per accepted output with repetitions, failed attempts, host processing, energy where measurable and provider-matched billing. No principal, interest, risk-premium or WACC effect is measured.
- **Lane H:** integrate the result into the long-term plan as a constrained quantum-resource frontier, not a promise of general-purpose replacement.
- **FND-006 / EQN-001, EQN-004, EQN-005 and EQN-006 / INV-034–035:** retain the no-go assumptions and resource law as source-bounded mathematics; test proofs/counterexamples and trace any validated resource change to device, system and economics. No AI-generated equation or literature claim is promoted to a new physical law.

## Proposed falsifiable follow-up — EQN-PURIFY-001

1. **Source freeze:** archive exact arXiv version, paper PDF/source hash, theorem statements, definitions, proof dependencies, and all solver/library versions before implementation.
2. **Formal boundary reproduction:** independently encode the two-copy qubit and odd-dimension theorem assumptions. Separate proof-checked conclusions from numerical SDP observations for three/four copies.
3. **Known-case controls:** test explicit source-provided purification maps and stabilizer/classically simulable baselines on a preregistered set of noisy input states. Freeze state generation, dimensions, target fidelity, success-probability convention and random seeds.
4. **Held-out/counterexample phase:** reserve state families and parameter regimes not used to develop the implementation; search for counterexamples to any broader statement the project proposes. Reject accidental promotion of a theorem scoped to one resource class into a universal statement about all quantum operations.
5. **Resource ledger:** report mana/robustness separately from physical gate counts, nonstabilizer-state consumption, copies, repetitions, success probability, fidelity, depth, host compute, memory/I/O, energy if measurable and total cost per accepted output. Never infer one resource from another without a cited, versioned mapping.
6. **Independent check:** have a separate implementation or proof review verify the theorem boundary and all claimed numerical certificates. Preserve failures and solver instability.
7. **Technology gate:** only if a reproducible resource tradeoff survives these checks, compile a bounded protocol through a provider-neutral path and compare it with the best competitive baseline under the same useful-output contract. Simulator/dry-run first; no paid QPU job without credentials, a bounded budget and explicit user consent.
8. **Falsifiers:** stop or narrow the claim if the source assumptions were misread, a counterexample violates a proposed generalization, numerical bounds lack certification, the independent implementation disagrees, or any resource reduction fails to lower end-to-end cost per accepted useful output.

## Current status

**LITERATURE_ONLY / READY_FOR_INDEPENDENT_REPRODUCTION.** No implementation, formal proof assistant run, SDP solve, provider call, QPU job or physical experiment was executed in this watch. No project evidence level is promoted. The permanent root directives, INV-025/026/027 and INV-029–035, and the Thai/English/Chinese/Japanese/Korean/German strategic references remain unchanged.
