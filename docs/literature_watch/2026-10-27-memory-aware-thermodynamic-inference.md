# Literature watch — 2026-10-27: memory-aware thermodynamic inference

**Source version date:** arXiv v5 revised 2026-10-01  
**Journal status:** accepted for publication in Physical Review Letters on 2026-09-25  
**Accessed:** 2026-10-27  
**Primary source:** Tassilo Schwarz, Anatoly B. Kolomeisky and Aljaž Godec, “Consistent time reversal and reliable and accurate inference in the presence of memory.” [Official arXiv record, v5](https://arxiv.org/abs/2410.11819v5) · [APS accepted-paper record, DOI 10.1103/gwf7-6kvr](https://doi.org/10.1103/gwf7-6kvr)  
**Evidence class:** PEER-REVIEWED ACCEPTED PAPER + OFFICIAL PREPRINT; not reproduced by UQPU  
**Primary owner:** Lane H — literature publication  
**Implementation/evaluation owners:** Lane F — thermodynamic accounting and evidence; Lane A — reproducible estimator tooling if the gate is funded  
**Feeds:** FND-001, FND-003, EQN-001–006, INV-034/035; lanes A/C/E/F/H  
**UQPU advantage promoted:** none

## Executive delta

The paper derives an experimentally accessible k-th-order estimator for entropy-production rate from coarse observations. Its stated result supplies necessary and sufficient conditions for a guaranteed dissipation lower bound in strongly non-Markovian settings. The authors emphasize that the estimator order must be sufficient to resolve the relevant memory duration: a Markovian estimator without a valid time-scale separation can produce artifacts, while an estimator whose order does not saturate the memory duration can overestimate dissipation.

The project-relevant novelty is a stricter measurement-model warning: a thermodynamic inference pipeline cannot silently replace an unresolved memory process with a first-order Markov model and then treat its inferred dissipation as a reliable bound. This is especially relevant to FND-001's thermodynamic-gap accounting and to active-memory/state-reset measurements. It is not a new general quantum speed limit or a new Landauer bound.

## Limitations and evidence boundary

- The source is a theoretical/methodological result with a peer-reviewed accepted-paper record; this cycle did not independently reconstruct the proof or reproduce the estimator.
- The paper's assumptions and exact estimator must be extracted from the pinned v5 text before implementation. The abstract alone is insufficient to reproduce its theorem.
- The result does not establish a general quantum thermodynamic law, a device energy floor, or the energy cost of a UQPU workload.
- Entropy-production inference from coarse trajectories is not a substitute for direct wall-plug energy, cooling, control, transfer, reset, and facility-boundary measurements.
- It does not establish accepted bio-oil, net delivered fusion electricity, material substitution, lower financing cost, or Data-Center-to-Phone compression.

## Exact UQPU relevance

- **FND-001:** add memory-order and estimator-assumption provenance before interpreting an inferred thermodynamic gap. Report the measured boundary separately from model-inferred dissipation.
- **FND-002:** no direct change to output-information lower bounds; keep state-space size distinct from readable classical output.
- **FND-003:** matched control/quantum runs should preserve sampling resolution, observation history, hidden-state assumptions, and energy boundary. This paper is not itself a quantum-versus-classical speed-limit measurement.
- **Lane C:** active memory, retained state, observation history, and readable memory are different quantities; do not infer one from another.
- **Lanes E/F:** BIO-001 and FUS-001 must continue to use accepted-liquid and net-reliable-electricity boundaries. A more defensible entropy estimator may improve analysis, but cannot create missing plant energy or cost data.
- **Lane H / FIN-001:** reduced uncertainty could shorten time-to-evidence only if independently measured; it is not a financing-rate or WACC result.
- **INV-034/035:** use the paper as a source-grounded measurement hypothesis, not a declaration of new physics. Existing physical constraints remain binding.

## Falsifiable follow-up

1. Freeze the exact arXiv v5 source, theorem statement, assumptions, estimator equations, and any author-provided code/data before implementation.
2. Independently implement the estimator and a reference calculation for finite-state processes with known transition structure and entropy production.
3. Preregister synthetic process families with known memory lengths, observation coarse-graining, sample lengths, and held-out trajectories. Include cases with and without a justified time-scale separation.
4. Compare the paper's required estimator order against first-order and deliberately under-saturated estimators. Report bias, interval coverage, lower-bound violations, overestimation frequency, uncertainty, runtime, and failures across at least 30 fixed seeds.
5. Search for counterexamples to the claimed conditions and have an independent researcher rebuild the calculations from the frozen source.
6. Only after the synthetic gate passes should a lab-trace study be proposed; keep direct energy measurements separate and do not generalize a classical trajectory result to quantum hardware without a distinct derivation.

**Decision rule:** reject any claimed method improvement that disappears on held-out process families, violates the stated lower-bound conditions, depends on unreported memory order, or cannot be reproduced from the pinned source. Retain failed and inconclusive runs.

## Non-claims

No UQPU measurement, physical-law discovery, quantum advantage, QPU result, device energy saving, commercial fuel/electricity result, financing benefit, or Data-Center-to-Phone achievement is established by this watch.
