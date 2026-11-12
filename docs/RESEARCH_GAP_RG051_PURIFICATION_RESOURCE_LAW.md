# Research Gap RG-051 — independent reproduction of the nonstabilizerness purification resource law

**Opened:** 2026-10-26  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owner:** Lane F — evidence, benchmarks and economics  
**Publication support:** Lane H  
**Related work item:** EQN-PURIFY-001  
**Status:** LITERATURE_ONLY / READY_FOR_REPRODUCTION / SOURCE_ASSUMPTIONS_NOT_YET_VERIFIED  
**Evidence class:** PREPRINT + RELATED_PEER_REVIEWED_THEOREM; no UQPU result

## Objective

Determine whether the reported quantitative resource relations for universal quantum-state purification can be independently reproduced under their exact mathematical assumptions, and whether they can be translated into a defensible resource/cost bound for an explicitly defined useful task.

## Current evidence

- He, Xiong and Wang, “A Nonstabilizerness Resource Law for Universal Quantum State Purification,” arXiv:2607.08626 (2026-07-09), reports an exact linear mana law for universal two-copy purification in odd dimensions, a two-sided linear robustness law for multi-qubit systems (exact for one qubit), and a constructive purification map.
- The related peer-reviewed *Physical Review Letters* paper 136, 090204 (2026-03-04) proves a scoped two-copy no-go result for classically simulable operations. Its three/four-copy extensions are numerical SDP evidence unless independently certified.
- The source is newly recorded from literature surveillance, not newly published today. UQPU has not reproduced the preprint's theorem, resource relation or numerical calculations.

## Blockers

1. The exact arXiv version, theorem statements, quantifiers, definitions of mana/robustness, success-probability convention and proof dependencies are not yet frozen in a source-to-claim manifest.
2. No independent proof assistant or second implementation has reproduced the two-copy boundary.
3. No certified SDP reproduction, held-out state-family test or counterexample search has been run.
4. Mana/robustness have no validated mapping here to physical gate count, nonstabilizer-state consumption, shots, energy, provider billing or total cost per accepted useful output.
5. No provider credentials, budget or explicit consent exists for any real-QPU experiment; no job is authorized.

## Best current alternative

Treat the theorem/resource relation as a literature-only constraint on future algorithm design. Continue the existing provider-neutral QUBO/QAOA/QSVT and accepted-useful-output path without assuming that state purification is necessary or that resource monotones are hardware costs.

## Unlock criteria

1. Freeze source version, paper/source hashes, theorem statements, assumptions and proof/solver dependencies.
2. Independently reproduce the two-copy qubit and odd-dimension boundary; separate proof-level conclusions from numerical SDP evidence for three/four copies.
3. Test source-provided maps on preregistered known cases and held-out state families; retain counterexamples and solver instability.
4. Have an independent implementation or proof reviewer verify the results.
5. Create a versioned resource mapping only if the mathematical reproduction passes; keep mana, robustness, physical resources, energy and currency as distinct quantities.
6. Compare any candidate against a competitive baseline with identical accepted output, fidelity threshold, success probability, copy count, reconstruction, host work, I/O, latency, energy where measurable and cost per accepted output.
7. Keep all paid QPU execution disabled until credentials, bounded budget and explicit user consent are separately present.

## Invariant and mission boundary

- **INV-029:** no Data-Center-to-One-Phone physical-compression, service, energy or lifecycle-cost closure.
- **INV-030/031:** no Pangola-carbon substitution, accepted bio-oil or full liquid-energy cost result.
- **INV-032:** no net delivered fusion-electricity or lifecycle-cost result.
- **INV-033:** no project principal, absolute-interest, time-to-evidence or WACC effect.
- **INV-034/035:** present limits remain binding; the preprint is not a new physical law and is not UQPU-validated mathematics.
- **INV-025/026/027:** 100,000,000-unit targets and open-frontier claims remain falsifiable and unproven.

## Canonical gap-ledger sync debt

The large append-only `RESEARCH_GAPS.md` history was inspected but not replaced from a partial or stale extract. Its latest visible canonical detailed gates include RG-033/RG-034 (2026-10-18/19); this new RG-051 is a dated supplemental gap artifact and remains pending until its source PR is reviewed and merged. Do not treat this file as already synchronized to the canonical living ledger.
