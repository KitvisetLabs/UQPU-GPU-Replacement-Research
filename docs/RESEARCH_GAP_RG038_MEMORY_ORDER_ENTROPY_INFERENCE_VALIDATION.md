# Research gap RG-038 — calibrated memory-order diagnostics before entropy-production inference

**Date opened:** 2026-10-25  
**Primary owner:** Lane F — economics, evidence and integration  
**Cross-lane owners:** A — reusable diagnostic implementation; C — state/temporal data handling; H — research publication  
**Evidence state:** MODEL_ONLY_SYNTHETIC_KNOWN_TRUTH  
**Project evidence promoted:** none

## Objective

Build a falsifiable validation path for FND-001 so that finite-memory observations are not silently treated as first-order Markov data when a thermodynamic inference method requires stronger assumptions.

## Current implementation

The reusable helper in software/uqpu-prototype/uqpu/thermodynamic_memory_order.py estimates the adjacent-lag conditional mutual information

I(X_t; X_{t-k-1} | X_{t-k}, ..., X_{t-1})

from empirical frequencies. The dated result artifact benchmarks a known first-order binary Markov process and a known second-order noisy-XOR process. The tests demonstrate that this diagnostic separates those two selected synthetic cases.

This is only a finite-sample diagnostic. A small adjacent-lag CMI is not a proof of Markov order, and CMI is not entropy production. The current implementation provides no confidence intervals, bias correction, calibrated selection threshold, heat estimate, wall-plug energy measurement or physical-system inference.

## Blockers

- Plug-in CMI is biased at finite sample sizes, especially as the alphabet and conditioning order grow.
- A single adjacent-lag conditional-independence check does not establish independence from the full older history.
- No estimator-coverage study has yet been performed across known-truth processes and sample lengths.
- No project observation record, time-reversal support audit, transition-kernel estimate or independently validated entropy-production estimator is connected to this helper.
- No energy, device, bio-oil or fusion data were measured.

## Repeated-seed calibration update — 2026-10-25

The fixed-seed summary in benchmarks/results/fnd001-cmi-bias-calibration-2026-10-25.json evaluates the existing plug-in adjacent-lag CMI estimator over 30 seeds for each of two known-truth binary processes at n=500, 2,000 and 10,000. At n=500, null-order empirical p95 values reach about 0.017 bits for the first-order chain at k=2 and 0.0081 bits for the noisy-XOR chain at k=2; by n=10,000 they fall to about 0.00071 and 0.00096 bits, respectively. The true second-order XOR signal at k=1 has mean 0.7686 bits at n=500 and 0.8018 bits at n=10,000 versus analytic truth 0.8056 bits.

This is a narrow synthetic calibration, not a universal threshold. Thirty-replicate empirical percentiles are not confidence intervals, and sparse contexts, correlated observations and other alphabets/processes remain untested. No entropy-production, heat or wall-plug-energy value is inferred. The reproducibility module is software/uqpu-prototype/uqpu/fnd001_cmi_bias_calibration.py; its small deterministic smoke test is added to the unit suite.

## Unlock criteria

1. Freeze a suite of known-truth first-, second- and higher-order processes across sample lengths, alphabet sizes, transition sparsity and noise levels.
2. Preregister thresholds and report false-positive/false-negative rates, uncertainty coverage and sensitivity to observation coarse-graining.
3. Compare a selected entropy-production estimator against known-truth values on synthetic data and independent reference implementations.
4. Check the assumptions in Schwarz, Kolomeisky and Godec, PRL accepted 2026-09-25, DOI 10.1103/gwf7-6kvr, without treating the paper as UQPU measurement evidence.
5. Keep real-system thermodynamic or energy claims blocked until the observation model, estimator conditions and independent replication pass.

## Best current alternative

Use the CMI profile only as an exploratory, model-scoped warning signal. If the memory-order conditions are uncertain, report the entropy-production inference as unavailable or assumption-dependent rather than silently substituting a first-order estimator.

## Next action

Extend the frozen synthetic suite and calibrate sample-length-dependent uncertainty. Record every failed or false-positive memory-order classification as first-class evidence. Do not infer a physical law or energy advantage from this diagnostic.
