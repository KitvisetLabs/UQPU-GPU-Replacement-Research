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

## Repeated-seed finite-sample calibration — 2026-10-25

The reproducibility module is software/uqpu-prototype/uqpu/fnd001_cmi_bias_calibration.py. Run it with python -m uqpu.fnd001_cmi_bias_calibration. The fixed-seed summary is benchmarks/results/fnd001-cmi-bias-calibration-2026-10-25.json.

Thirty independent seeds per family/sample length were evaluated at n=500, 2,000 and 10,000. Analytic truth is 1-H_b(0.1)=0.5310044 bits for k=0 in the first-order chain, 1-H_b(0.03)=0.8056081 bits for k=1 in the noisy XOR chain, and zero for the stated null orders.

| Generator | n | Mean k=0 (bits) | Mean k=1 (empirical p95) | Mean k=2 (empirical p95) |
|---|---:|---:|---:|---:|
| First-order Markov | 500 | 0.520434 | 0.002773 (0.009020) | 0.005730 (0.016953) |
| First-order Markov | 2,000 | 0.528709 | 0.000960 (0.002712) | 0.001714 (0.003911) |
| First-order Markov | 10,000 | 0.528437 | 0.000128 (0.000319) | 0.000327 (0.000710) |
| Second-order noisy XOR | 500 | 0.025759 | 0.768583 (0.859503) | 0.002437 (0.008130) |
| Second-order noisy XOR | 2,000 | 0.003476 | 0.794071 (0.842708) | 0.001411 (0.002173) |
| Second-order noisy XOR | 10,000 | 0.001055 | 0.801779 (0.818154) | 0.000395 (0.000964) |

Null-order empirical p95 values fall with increasing sample length in these two fixtures; signal estimates approach analytic values. The empirical p95 is a descriptive nearest-rank statistic over 30 replicates, not a confidence interval or decision threshold. This calibration is MODEL_ONLY and does not estimate entropy production, heat or energy.

## Required next gate

Calibrate finite-sample bias and uncertainty across frozen known-truth process families, then compare a preregistered entropy-production estimator with known-truth values and an independent implementation. See gap RG-038. Failed classifications must be retained rather than discarded.
