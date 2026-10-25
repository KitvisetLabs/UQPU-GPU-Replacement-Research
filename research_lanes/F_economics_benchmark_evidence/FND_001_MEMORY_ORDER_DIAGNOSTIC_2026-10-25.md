# FND-001 lane artifact — synthetic memory-order diagnostic

**Date:** 2026-10-25  
**Primary owner:** Lane F — economics, evidence and integration  
**Implementation:** software/uqpu-prototype/uqpu/thermodynamic_memory_order.py  
**Result artifact:** benchmarks/results/fnd001-memory-order-cmi-synthetic-2026-10-25.json  
**Evidence class:** MODEL_ONLY / SYNTHETIC_KNOWN_TRUTH

## Quantity measured by the software

For conditioning order k, the helper estimates in bits

I(X_t; X_{t-k-1} | X_{t-k}, ..., X_{t-1}).

This is an empirical adjacent-lag conditional mutual-information statistic. It is not a thermodynamic entropy-production estimate, heat flow, energy consumption, a wall-plug measurement or a proof that a process has Markov order k.

## Frozen synthetic controls

| Fixture | Known generator | Seed / length | CMI profile in bits, k=0,1,2 |
|---|---|---:|---|
| FND001-MEM-ORDER-1 | Binary first-order Markov chain, P(stay)=0.9 | 1729 / 30,000 | 0.51472338; 0.00014050; 0.00020681 |
| FND001-MEM-ORDER-2 | Second-order XOR with independent 0.03 flip probability | 2718 / 30,000 | 0.00002509; 0.80845387; 0.00010050 |

The known-truth contrast is useful: persistence in the first-order chain appears at k=0 and disappears after conditioning on the most recent symbol; the second-order XOR process has strong k=1 adjacent-lag information that disappears at k=2 for this fixture.

## Interpretation boundary

The values are plug-in estimates on selected synthetic data. There are no confidence intervals or bias corrections, and no model-selection threshold is justified by these two examples. The result does not validate an entropy-production estimator or any physical system.

## Required next gate

Calibrate finite-sample bias and uncertainty across frozen known-truth process families, then compare a preregistered entropy-production estimator with known-truth values and an independent implementation. See gap RG-038. Failed classifications must be retained rather than discarded.
