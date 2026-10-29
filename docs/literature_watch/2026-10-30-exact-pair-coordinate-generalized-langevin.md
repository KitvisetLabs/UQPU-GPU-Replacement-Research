# Literature watch — exact pair-coordinate generalized Langevin dynamics

**Review date:** 2026-10-30  
**Source:** Shunsuke Ando, Tomoya Urashita, Soya Shinkai and Tomoshige Miyaguchi, “Exact generalized Langevin dynamics of pair coordinates in elastic networks,” *Physical Review E* 114, L042108, published 2026-10-22. DOI: https://doi.org/10.1103/v5zx-93k9  
**Publisher:** https://journals.aps.org/pre/abstract/10.1103/v5zx-93k9  
**Evidence class:** PEER-REVIEWED PRIMARY PAPER; ABSTRACT REVIEWED; FULL TEXT/SUPPLEMENT NOT REPRODUCED  
**Primary owner:** Lane H; implementation owner: Lane A. Interfaces: C, E, F; INV-034/035.

## Novelty

The authors analytically derive an exact coupled GLE for two tagged beads in arbitrary harmonic elastic networks and an exact GLE for their relative coordinate. The publisher abstract says the memory kernel and effective restoring force are explicit functions of network matrices. A GLE for interbead distance additionally uses a small-displacement approximation.

## Limitations

The publisher page confirms publication 2026-10-22, receipt 2026-04-14 and acceptance 2026-09-29. Article text and supplement were subscription-gated in this review; UQPU has not reconstructed the equations or assumptions. Exactness is limited to the stated overdamped harmonic-network model; the distance result has an additional approximation. This does not cover arbitrary nonlinear or inertial systems. A physical memory kernel is not RAM, VRAM, HBM, storage or quantum memory.

## UQPU relevance and follow-up

FND-006/EQN-001/003/004: a peer-reviewed effective-equation reproduction target. Lane A should obtain the full source, independently derive a small network case and compare the reduced pair GLE against a direct full-network solver. Hold out topology, size, edge weights and tagged pairs. Check units, causality, symmetry, stability/passivity, fluctuation-dissipation consistency, equilibrium limits and near-zero/degenerate modes. Treat nonlinear springs and underdamped dynamics as out-of-domain controls unless source-covered. Lane C must measure kernel bytes/convolution history without conflating physical memory with computer memory. Lane F must compare precomputation/convolution/storage against full-solver cost per accepted trajectory. No device, biomass, bio-oil, fusion, new-law or economic benefit follows.

**Decision:** source-attributed exact effective-equation lead under restricted assumptions; no independent UQPU reproduction.