# Lane A contract — exact pair-coordinate GLE reproduction

**Date:** 2026-10-30 · **Work item:** RG-EQN-GLE-PAIR-001  
**Source:** DOI 10.1103/v5zx-93k9 · **Status:** FULL TEXT REQUIRED / NOT REPRODUCED

Obtain the full paper and pin equations, units, network-matrix conventions, mobility/friction, thermal-noise covariance, initial conditions and kernel definitions. The APS abstract alone is insufficient.

Independently derive a small harmonic-network case and compare the reduced pair GLE with a direct full-network solver under identical parameters, noise conventions and initial conditions. Hold out topology, network size, edge-weight distribution and tagged-pair choices. Check dimensional consistency, causality, symmetry, stability/passivity, fluctuation-dissipation consistency, equilibrium limits and near-zero/degenerate modes. Treat nonlinear springs and underdamped dynamics as out-of-domain controls unless the source explicitly covers them.

Record pair trajectory/correlation error, kernel residual, precomputation, convolution, kernel storage bytes, peak memory, full-solver time, host work, retries and energy where measured. Compare cost per accepted trajectory. A physical memory kernel is not RAM/VRAM/HBM or readable storage. No new law, device, material, fuel, fusion, QPU or economic benefit is implied.