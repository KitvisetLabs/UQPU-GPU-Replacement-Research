# Research gap — FND-003 matched control / quantum-speed-limit contract

**Opened:** 2026-10-27  
**Primary owner:** Lane A — workload and comparison contract  
**Measurement owner:** Lane D — device/control/Hamiltonian provenance  
**Evidence and economics owner:** Lane F  
**Publication owner:** Lane H  
**Related:** FND-001, FND-003, FND-006, EQN-001–006, INV-029, INV-034/035  
**Status:** OPEN — contract implemented; no matched physical experiment or independent theorem reconstruction

## Objective

Make it impossible for the research stack to compare unmatched classical and quantum task timings, use a generic gate duration as a quantum-speed-limit denominator, or infer wall-plug energy from intrinsic energy/entropy terms.

## Current evidence

The existing control-duration diagnostic deliberately reports only the inverse Margolus–Levitin energy scale implied by a duration. The 2026-10-27 literature watch for Kobashi, “Thermodynamic speed limits in isolated quantum systems,” *Physical Review Research*, accepted 2026-10-06 (DOI 10.1103/k16k-nx74; arXiv:2609.12520), adds a candidate theoretical comparator whose coarse-graining and entropy-production definitions are part of its scope.

The new contract binds one useful-output task to control and quantum records, checks quality acceptance before exposing time ratios, binds the theorem to a hashed quantum-evolution record, and keeps measured wall-plug energy separate with an explicit boundary identifier. It is metadata validation only. It does not derive the theorem, run an experiment, or establish that the assumptions are true.

## Blocking unknowns

- No UQPU workload has been measured with a shared input/output hash, matched acceptance threshold, identical timing boundary and independently audited quantum-evolution record.
- No independent derivation of the Kobashi theorem or reproduction of its distance/entropy quantities has been performed by this repository.
- No same-evolution mean energy above ground has been measured for the standard Margolus–Levitin form.
- No matched whole-system wall-plug energy, uncertainty, retries, host work or cost per accepted task has been recorded.
- The latest software contract has not passed exact-head hosted CI until the new commit's workflows complete.

## Acceptance gate

1. Freeze the workload/input/output contract and a disjoint held-out case.
2. Bind both control and quantum runs to the same contract hash and require both to pass the same quality threshold before calculating descriptive elapsed-time ratios.
3. For a quantum-speed-limit comparison, pin the theorem version, assumptions audit, initial/final state hashes, Hamiltonian/dynamics model, state-distance definition, coarse-graining and entropy-production definitions.
4. Keep the bound null unless its applicability assumptions and derivation are explicitly audited and hash-bound. The contract never derives the bound itself.
5. Measure the same elapsed-time boundary and separately measure wall-plug energy with matched system boundaries. Do not substitute intrinsic energy or entropy for wall-plug joules.
6. Independently reproduce the theorem calculation and workload result; retain failed, inconclusive and counterexample cases.
7. Propagate accepted measurements into cost per accepted useful task only after resource boundaries, retries, host compute, memory/I/O, provider charges and energy are all accounted for.

## Falsifiers and stop rules

- Different workload/input/output hashes, acceptance metrics, thresholds, held-out cases or timing boundaries invalidate the comparison.
- A failed output-quality gate suppresses the time comparison even if a circuit or program executed successfully.
- Missing theorem assumptions, mismatched evolution hashes or missing derivation/audit artifacts suppress the speed-limit ratio.
- Missing or mismatched wall-plug energy boundaries suppress energy ratios.
- A valid descriptive time ratio does not itself establish quantum advantage, physical-limit proximity, cost reduction or a new physical law.

## Explicit nonclaims

No quantum advantage, phone-class physical compression, readable-memory equivalence, critical-material substitution, accepted bio-oil, net fusion electricity, lower absolute interest, lower WACC or new physical law is established by this gap or its contract tests.
