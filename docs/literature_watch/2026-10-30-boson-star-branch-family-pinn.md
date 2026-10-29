# Literature watch — physics-informed boson-star branch-family surrogates

**Review date:** 2026-10-30  
**Source:** Ao Liu, Chen-Hao Hao, Cuihong Wen, Shao-Jiang Wang and Jieci Wang, “Learning boson star solution families with physics-informed neural networks,” *Physical Review D* 114, 083537, published 2026-10-26; accepted 2026-10-05. DOI: https://doi.org/10.1103/gnwy-2szh  
**Publisher:** https://journals.aps.org/prd/abstract/10.1103/gnwy-2szh  
**Evidence class:** PEER-REVIEWED PRIMARY PAPER; ABSTRACT REVIEWED; FULL TEXT NOT REPRODUCED  
**Primary owner:** Lane H; implementation owner: Lane A. Interfaces: F; INV-034/035.

## Novelty

The authors report a PINN mapping physical parameters and radial coordinate to scalar and metric fields over a boson-star equilibrium solution manifold. The abstract describes regularity/asymptotic boundary conditions embedded in the output and a training objective combining pointwise supervision, Einstein-Klein-Gordon residuals, ADM mass and Noether charge. Representative one-, two- and three-branch families, including inner branches, are reported.

## Limitations

The publisher confirms publication 2026-10-26, acceptance 2026-10-05 and receipt 2026-08-22. Full text was subscription-gated; equations, potential, architecture, data, code and tolerances were not audited. The abstract does not establish universal extrapolation, stability, dynamical formation or uniqueness. The source uses established Einstein-Klein-Gordon equations; it does not report a new field equation or particle.

## UQPU relevance and falsifiable follow-up

FND-006/EQN-003/004/006: use as a known-equation surrogate benchmark, not new physics. Obtain the full source; pin equations, potential, units, boundary conditions and branch labels. Reproduce a small family with an independent high-accuracy boundary-value solver and numerical continuation. Hold out parameter intervals and complete branch families. Measure field errors, equation residuals, regularity/asymptotic errors, ADM mass and Noether charge separately. Search for branch collapse, turning-point interpolation and inner-branch failures. Compare data-generation/training/search/inference/memory/energy costs against repeated continuation. A branch-label ambiguity is a potential failure mode to test, not a failure attributed to the authors.

**Decision:** constrained-surrogate method lead only; no UQPU reproduction, new physical law, particle, QPU advantage or material/energy/economic result.