# Literature watch — 2026-10-24: conjecture-guided equation discovery and experimental closure

**Observed:** 2026-10-24  
**Primary owner:** Lane H — foundational research and strategic publication  
**Feeds:** A, E, F, H; FND-006; EQN-001–006; BIO-001; FUS-001; FIN-001; INV-029, INV-030, INV-031, INV-032, INV-033, INV-034, INV-035  
**Evidence class:** LITERATURE_ONLY / THIRD_PARTY_PREPRINT  
**Project evidence promotion:** none

## Primary source and novelty

Yuxiao Hu et al., “Beyond Equation Search: Conjecture-Guided Discovery with SCOPE and ClosureBench,” arXiv:2610.18938, submitted 2026-10-13: https://arxiv.org/abs/2610.18938

The paper argues that improving equation fit is not enough to decide whether the underlying scientific conjecture should be retained, revised or rejected. SCOPE runs multiple conjecture-driven research trajectories with model construction, question formulation and active experimentation; ClosureBench supplies 60 closure-discovery tasks across five scientific domains. Each task embeds an unknown algebraic relation in a known PDE system and lets agents choose experimental conditions in OpenFOAM. The authors propose evaluating evidence faithfulness, mechanism insight and experimental effectiveness in addition to equation accuracy.

Related source already recorded in the project: “Learning to Design SR Solvers: Harness Optimization for Symbolic Regression,” arXiv:2610.16966, submitted 2026-10-12: https://arxiv.org/abs/2610.16966. HarnessSR treats the solver workflow and prompts as optimization variables. The new-to-this-cycle distinction is that SCOPE emphasizes the conjecture and the evidence-producing investigation, not only the solver harness or final expression.

## Limitations and evidence boundary

- SCOPE is an unrefereed preprint at the time of this review; reported results are third-party claims pending independent reproduction.
- ClosureBench uses simulated PDE systems and hidden closure relations. This is a useful controlled benchmark, not a demonstration that a generated relation is a unique causal law of nature.
- A good equation fit or successful active experiment does not by itself establish dimensional consistency, conservation, symmetry, causality, uniqueness, a proof, or validity outside the sampled regime.
- No result here is UQPU hardware execution, material qualification, Pangola fuel yield, fusion electricity, financing evidence, or a new physical law.

## Exact UQPU relevance

- EQN-001 and EQN-006: keep multiple competing conjectures alive when several equations fit the same observations; log why a conjecture is retained, revised or rejected.
- EQN-002 and EQN-003: freeze held-out regimes and experiment budgets before search; treat experiment selection and data acquisition as costed actions.
- EQN-004 and EQN-005 / FND-006: apply physical constraints and counterexample searches before any candidate can be promoted; formal proof checks a mathematical statement relative to its assumptions, not whether the assumptions describe nature.
- BIO-001 / INV-031: a future biomass conversion dataset could test candidate yield or quality relations only after feedstock identity, moisture, ash, process conditions, mass/energy balance and final accepted-product assays are traceable.
- INV-030: candidate carbon-material constitutive or adsorption relations must be tested against function-specific data, purity, contamination, regeneration and lifecycle cost; carbon processing is not elemental transmutation.
- FUS-001 / INV-032: any candidate relation between material exposure, component lifetime, availability or net output must be tested against independently measured conditions and cannot substitute for integrated net-electric evidence.
- FIN-001 / INV-033: report the compute, experiment, time-to-evidence and capital budget of the discovery process. A more efficient search algorithm does not itself demonstrate a lower project WACC.
- INV-029: only a verified device/system consequence that passes the service, energy, physical and lifecycle-cost contracts can contribute to Data-Center-to-Phone; this paper contributes methodology only.

## Proposed falsifiable follow-up: EQN-SCOPE-001

1. Select a synthetic constitutive/closure family with a known ground-truth relation and freeze the generator, data and code hashes before discovery.
2. Split by entire equation family and operating regime, not random rows. Hold out at least one scale/regime and one family of perturbations.
3. Compare a fixed symbolic-regression baseline, a harness-optimized baseline and a conjecture-guided/active-experiment variant under matched wall-clock, host-compute, token and simulated-experiment budgets.
4. Enforce dimensional checks and the relevant symmetry, conservation and causality constraints; run counterexample search after fitting.
5. Score structure recovery, held-out prediction, evidence faithfulness, mechanism discrimination, experiment effectiveness, false discoveries, counterexample survival and total search/experiment cost.
6. Include deliberately misspecified conjectures and observationally indistinguishable alternatives as negative controls. A candidate fails if its claimed mechanism is not discriminated by the preregistered observations.
7. Only after the synthetic gate passes, seek an open, provenance-rich real dataset for a specific biomass/material or fusion subproblem. Do not transfer a synthetic pass into a physical claim.

## Surveillance notes

The 2026-10-20 Nature Machine Intelligence News & Views on physics-informed machine learning and fluid dynamics is contextual, not a new physical law: https://www.nature.com/articles/s42256-026-01319-4. The recent IRENA 2025 renewable-cost report and DOE 2026 fusion roadmap remain external economic/roadmap context, not commercial fusion or project-specific financing evidence: https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025 and https://www.energy.gov/fusion/fusion-energy.

## Decision

**Material methodological delta:** yes — evaluate the conjecture/evidence/experiment trajectory, not only the recovered expression.  
**Physical-law status:** unchanged.  
**Project evidence promotion:** none.  
**Next gate:** preregister EQN-SCOPE-001 and obtain traceable real datasets before attempting domain claims.
