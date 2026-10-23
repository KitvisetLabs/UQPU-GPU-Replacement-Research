# Literature watch — 2026-10-24: progressive symbolic discovery of physical laws

**Accessed:** 2026-10-24 (Asia/Bangkok)  
**Primary owner:** Lane H — strategy / foundational-method surveillance  
**Integration owner:** Lane F — evidence and reproducibility  
**Feeds:** Lane A, FND-006, EQN-001–006, INV-034, INV-035; conditional downstream links to C, D/G, E and F  
**Evidence class:** PEER-REVIEWED ACCEPTED PAPER / THIRD-PARTY METHOD RESULT  
**UQPU evidence promotion:** none

## Source and freshness decision

Mingkun Xia and Weiwei Zhang, “Data-driven progressive discovery of physical laws,” *Physical Review Research*, accepted 6 October 2026, DOI 10.1103/f2kp-pp4q. Official American Physical Society accepted-paper record:

https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q

The APS page was checked during this cycle. The repository's 2026-10-23 literature watch covered optimization-law discovery and an ancilla-QFI theorem, but did not record this distinct progressive-chain method. The paper is not newly dated 24 October; today's delta is its first identified and documented inclusion in this repository's current literature-watch sequence.

## Genuine methodological delta

The paper proposes Chain of Symbolic Regression (CoSR): instead of fitting one large end-to-end expression, it composes interpretable intermediate knowledge units into a chain. The APS record reports a reconstruction of the Kepler-third-law-to-universal-gravitation discovery path and applications to Rayleigh–Bénard convection, pipe flow, laser–metal interaction and aircraft aerodynamic-coefficient scaling.

This differs from the already reviewed search-controller and optimization-law methods. It raises a concrete design question for EQN-001–006: can progressive decomposition improve recovery and held-out generalization when the data contain genuinely identifiable intermediate structure, or does it merely add model flexibility and extra degrees of freedom?

## Limits and audit flags

- This is an external method result, not a UQPU experiment. The paper's reported cases do not establish a new law for UQPU, quantum devices, biomass, fuel, fusion or finance.
- The accepted-paper landing page is the source checked here; this watch does not claim an independent reproduction of the complete paper or its supplementary material.
- A chain can overfit by selecting intermediate variables after inspecting the held-out set. The benchmark must freeze the candidate grammar, split hashes and stage order before evaluation.
- If multiple chains or a compact one-step expression make indistinguishable held-out predictions, the data do not identify a unique mechanism. Structural elegance is not evidence of physical truth.
- More intermediate measurements, more search time or more compute can explain an apparent gain. They must be budget-matched rather than credited to “progressive discovery.”
- Any physical-law challenge must still state the incumbent assumption, alternative equation, dimensional/symmetry/conservation/causality checks, scaling and limiting cases, falsifier, discriminating observable, held-out prediction, proof or experiment, and independent validation path.

## Falsifiable follow-up: EQN-PROGRESSIVE-001

An offline benchmark preregistration is added under integration/batches/cycle010. It remains PROPOSED / NOT_EXECUTED until exact dataset and split hashes are committed.

1. Compare a one-step symbolic-regression baseline with a progressive-chain candidate on synthetic composite laws with known intermediate quantities. Use identical raw observations, operator grammar, coefficient-fitting budget, wall-clock limit and host-resource accounting.
2. Split by complete law family and parameter regime, not random rows alone. Keep at least one whole family blind until all candidates and thresholds are frozen.
3. Include an identifiability negative control where a chain and a compact one-step expression are observationally equivalent. The correct result for that control is “mechanism not identified,” not a forced winner.
4. Include noisy observations, correlated distractors, dimensionally invalid candidates, and a law family for which the assumed chain is wrong. Preserve all failed runs and invalid proposals.
5. Score held-out error, exact structure recovery where identifiable, expression complexity, unit consistency, declared symmetry/conservation checks, counterexample survival, parameter identifiability, false-discovery count, runtime, peak memory, tokens if used, and energy only where measured.
6. Accept a method improvement only if it improves preregistered held-out performance or identifiable structure over the strongest baseline under matched budgets without worsening constraint violations or calibration. Otherwise record a null/negative result.

A pass would be MODEL_ONLY evidence about a discovery workflow. It would not establish a physical law or technology advantage. Any downstream use for device design, accepted liquid fuel, net fusion electricity or financing must separately pass the relevant physical and economic gates.

## Exact UQPU relevance

- **Lane A / software:** a staged generator can propose compiler/runtime cost models or algorithmic resource relations, but only after semantic equivalence and held-out validation.
- **FND-006 / INV-034:** mathematics-first invention gains a candidate decomposition strategy; present physical limits remain binding.
- **INV-035 / EQN-001–006:** add progressive composition as a generator family, while retaining deterministic evaluation, counterexample search and independent validation.
- **Lane C:** complexity and memory/I/O accounting belong in the benchmark; no Hilbert-space or equation-state count is readable RAM/VRAM/storage.
- **Lanes D/G:** no device or factory requirement follows unless a validated relation changes a concrete control, timing, material or process specification.
- **Lane E / INV-030–032:** possible future modeling method only; no Pangola material, accepted bio-oil, fusion-electricity or cooling evidence.
- **Lane F / INV-033:** include discovery compute and time-to-evidence in future cost comparisons; no interest-rate or WACC claim follows.
- **Lane H:** preserves the strategic plan as context without importing third-party results as project evidence.

## Decision

**Material method delta: yes. Evidence promotion: no.** Add EQN-PROGRESSIVE-001 as an offline falsifiable benchmark. Do not duplicate the existing EQN-CTRL-001, EQN-PROOF-001, FND-QFI-001 or QALG-CTRL-001 tasks; they test different claims. No provider call, QPU job, shot, purchase, physical experiment or capital action was performed.