# Literature watch — progressive symbolic regression status and formal theorem discovery

**Date checked:** 2026-10-28  
**Primary owner:** Lane H — literature surveillance/publication  
**Cross-lane interfaces:** Lane A (equation/workload contracts), Lane E (constitutive and multiphysics models), Lane F (reproducibility/evidence/economics)  
**Evidence class:** LITERATURE_ONLY; the CoSR source has a publication-status conflict  
**Related:** INV-034, INV-035, FND-006, EQN-001–EQN-006

## 1. Chain of Symbolic Regression (CoSR): method idea, but not validated here

**Sources**

- Xia, Mingkun and Zhang, Weiwei, “Data-driven progressive discovery of physical laws,” Physical Review Research accepted-paper record, marked accepted 2026-10-06, DOI https://doi.org/10.1103/f2kp-pp4q. Official record: https://journals.aps.org/prresearch/accepted/10.1103/f2kp-pp4q
- Same-title arXiv record arXiv:2603.13727, checked 2026-10-28: https://arxiv.org/abs/2603.13727. The current arXiv page explicitly says the paper was withdrawn by Mingkun Xia; version 2 is dated 2026-05-29 and the author comment says it needs retraction because of methodological flaws found in the Rayleigh–Bénard convection (RBC) case.

**Genuine methodological idea reported by the publisher record**

The proposed Chain of Symbolic Regression (CoSR) organizes discovery as a progression of interpretable physical knowledge units instead of a single end-to-end expression search. The APS abstract describes applications to RBC convection, circular-pipe viscous flow, laser–metal interaction and aerodynamic coefficient scaling. Staged discovery is a potentially useful candidate-generation design pattern: propose a simple relation, test it, then add a physically interpretable unit only when held-out evidence warrants it.

**Critical limitation / status conflict**

The APS accepted-paper record and current withdrawn arXiv record coexist. This watch does not infer that the accepted record is invalid, nor assume that acceptance resolves the stated RBC flaw; the exact version, correction and review status need reconciliation. Until that is resolved, CoSR is not treated as a positive validated-method result. Do not reuse the RBC claim as a successful benchmark or cite the method as independently verified. No UQPU reproduction, source-code audit or independent dataset analysis was performed in this cycle.

**Exact UQPU relevance**

- EQN-001–EQN-006 / FND-006: motivates staged, semantically labelled candidate generation, but every candidate still needs explicit units, symmetries, conservation/causality checks, limiting cases, held-out tests, counterexample search and independent proof/simulation/experiment as applicable.
- Lane E / BIO-001 / FUS-001: a symbolic surrogate is only potentially relevant if its governing equations and parameter domain match a specific biomass, upgrading, thermal-fluid, fusion-auxiliary or cooling process. The paper does not establish bio-oil yield/cost, material substitution, fusion net-electricity or commercial benefit.
- Lane F / FIN-001: staged discovery may reduce wasted search effort only if measured in a reproducible workflow; no cost, energy, financing or time-to-evidence improvement has been measured here.

**Falsifiable follow-up**

1. Reconcile the exact APS manuscript/version with the withdrawn arXiv version and the RBC methodological flaw before selecting a paper benchmark.
2. If a lawful, pinned source/data implementation is available, preregister one known-law synthetic benchmark plus one unrelated physical benchmark; hash source, data, split and solver.
3. Compare one-shot symbolic regression with a staged candidate chain under equal search/evaluation budgets. Freeze grouped/parameter-held-out splits before tuning.
4. Record every candidate, failure, dimensional/symmetry violation, counterexample and undecided result. Compare predictive error, expression complexity and uncertainty against a fixed incumbent and simple baselines.
5. Reject any candidate whose apparent gain disappears under held-out or adversarial cases. A better fit alone is not a new physical law without a discriminating observable and independent validation.

## 2. Self-supervised formal theorem discovery: proof-search lead, not physics discovery

**Source:** Ota, Kazuki; Osa, Takayuki; Harada, Tatsuya, “Self-Supervised Theorem Discovery in a Formal Axiomatic System,” arXiv:2606.28747, submitted 2026-06-27: https://arxiv.org/abs/2606.28747

The preprint describes an agent that alternates formal proof search and useful-theorem extraction, then reuses extracted lemmas in later search. Its demonstrated domain is a small Hilbert axiomatization of classical propositional logic, where proofs can be machine checked. This is a useful external lead for proof-artifact binding and a failed-conjecture ledger, but it is not evidence that AI has discovered a new physical law or a theorem about quantum advantage.

**UQPU follow-up:** test whether formally verified lemmas can reduce proof-search effort for a bounded, already formalized software contract or mathematical subclaim. Bind every result to the exact formal statement, axioms, proof kernel/version and artifact hash. Report unsuccessful searches and resource limits. Any application to physical claims must formalize assumptions and must not skip dimensional, empirical or engineering gates.

## Decision

No equation, physical law, QPU advantage, material substitution, accepted fuel, fusion-electricity, cost/task or financing claim is promoted. The useful result is a source-status warning plus a testable methodology lead. Current physical constraints remain binding. Evidence class remains LITERATURE_ONLY.
