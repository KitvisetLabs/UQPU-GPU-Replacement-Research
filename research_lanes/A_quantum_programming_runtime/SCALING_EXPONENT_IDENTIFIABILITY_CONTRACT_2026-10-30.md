# Lane A contract — scaling-exponent identifiability and known-law baseline

**Date:** 2026-10-30  
**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Evidence/accounting owner:** Lane F  
**Publication owner:** Lane H  
**Cross-lane interfaces:** B, C, D, E, F, G, H; INV-034/035  
**Status:** SYNTHETIC REFERENCE BASELINE / MODEL_ONLY / EXTERNAL METHOD NOT REPRODUCED  
**Source:** https://proceedings.mlr.press/v306/n-guessan26a.html  
**Focused gap:** ../../docs/RESEARCH_GAP_SCALING_EXPONENT_IDENTIFIABILITY_2026-10-30.md

## Objective

Create a transparent classical reference for a narrow known-law family before attempting to reproduce physics-informed trainable-exponent methods. Keep parameter identifiability separate from model-family validity and from any claim of physical discovery.

## Restricted model and implementation

For positive finite observations under the predeclared model y = a x^mu, with a > 0 and x > 0, the reference fits log(y) = log(a) + mu log(x) using ordinary least squares. A declared minimum log-x span rejects degenerate or nearly degenerate designs. The returned R-squared is a fit diagnostic only.

Implementation: software/uqpu-prototype/uqpu/scaling_exponent_baseline.py  
Tests: software/uqpu-prototype/tests/test_scaling_exponent_baseline.py

The isolated local test harness passed 7/7 synthetic test methods. Exact-head GitHub Actions for the resulting repository commit still require observation. The implementation does not reproduce the MSN-PINN architecture or its identifiability theorem.

## Acceptance contract

1. Recover a known amplitude and exponent on an exact synthetic fixture.
2. Predict a predeclared held-out scale without refitting.
3. Preserve exponent estimates under a change of x-unit scale while allowing amplitude to transform.
4. Reject constant/near-constant log-x designs, nonpositive/nonfinite data, boolean inputs and shape mismatch.
5. Keep training/selection/test groups disjoint in the future external-method comparison.
6. Record equation form, units, regime, data/source hashes, noise model, residuals, held-out error, failed candidates, counterexamples and false-discovery state.
7. Compare methods at equal candidate, wall-clock, CPU, memory and precision ceilings; record GPU/energy only when actually measured.
8. Do not infer a physical law from synthetic recovery or a high R-squared.

## Cross-lane consequences

- **B:** no provider calls are needed for this CPU reference; cloud/QPU evaluation remains dry-run first.
- **C:** record input arrays and output artifacts in bytes; do not equate a model's mathematical dimension with readable memory.
- **D/G:** any eventual scaling relation used for device/process decisions needs measured quantities and validated process regimes.
- **E:** BIO-001 and FUS-001 remain separate domain-specific data/economic gates; this helper supplies no fuel or electricity evidence.
- **F:** future comparisons must include total search/evaluation resource use and cost per accepted model.
- **H:** publish source-specific conclusions without turning a roadmap or fit into a technology or financing claim.

## Next gate

Pin and audit the paper's code/data/license/environment, then preregister a matched comparison against the classical baseline and conventional symbolic regression on known-law and misspecified fixtures. Require held-out regime performance, physical-constraint checks, counterexample search, false-discovery accounting and independent review. No real-QPU execution is needed or authorized for this gate.
