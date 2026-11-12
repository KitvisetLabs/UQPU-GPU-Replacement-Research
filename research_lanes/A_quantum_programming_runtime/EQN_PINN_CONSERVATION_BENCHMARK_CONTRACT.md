# EQN-PINN-CONSERVATION-001 — matched benchmark contract

**Primary owner:** Lane A — quantum programming/workloads/compiler/runtime  
**Integration owners:** Lane C — memory/state/data movement; Lane F — evidence/economics  
**Publication owner:** Lane H  
**Date:** 2026-10-26  
**Status:** DESIGN_ONLY; no UQPU reproduction or performance claim  
**Related gap:** `docs/RESEARCH_GAP_EQN_PINN_CONSERVATION_001.md`

## Hypothesis

For at least one source-pinned PDE reconstruction task, a candidate model with mathematically justified hard conservation/admissibility constraints and an explicit model-discrepancy term may improve held-out accepted-output quality or reliability compared with an unconstrained PINN, without exceeding a matched compute budget or losing to a conventional numerical solver.

This is a falsifiable method hypothesis, not a claim that PINNs are generally superior or that the cited articles introduce new physical laws.

## Arms

1. `FINITE_VOLUME_REFERENCE`: source-appropriate conventional solver (Kurganov–Tadmor for the BDNK paper's reported comparison, or a source-justified finite-volume baseline for another case).
2. `PINN_UNCONSTRAINED`: same PDE and observations, no added hard constraint beyond the baseline formulation.
3. `PINN_CONSTRAINT_AWARE`: conservation/flux and admissibility enforced exactly where mathematically justified, with all transformations and tolerances logged.
4. `PINN_CONSTRAINT_PLUS_DISCREPANCY`: arm 3 plus an explicit inadequacy term for unclosed/model-mismatch contributions where the source equations justify it.

Do not treat the four arms as comparable until the exact problem and output contract make the comparison meaningful. The BDNK and RANS papers describe different physical models; their results must not be pooled as if they were one dataset.

## Frozen inputs and controls

- Exact governing equations, dimensional units, constants and source version.
- Dataset DOI/URL, content hash, data license, boundary/initial conditions and measurement provenance.
- Train/validation/held-out split hashes and record-level disjointness certificate.
- Fixed seeds, optimizer, discretization, precision, stopping rules, parameter count and wall-clock/host-resource budgets.
- Smooth and discontinuous/sharp-gradient regimes, plus parameter-shift or out-of-distribution cases.
- A quality threshold defined from the task's useful output, not chosen after observing test results.

If any input is missing or cannot be reconstructed, mark the case `BLOCKED_SOURCE_PROVENANCE` and do not report a reproduction.

## Required metrics

- Accepted-output fraction and quality/error on held-out data.
- Conservation/flux residual and admissibility/realizability violations.
- Separate smooth, discontinuous, shifted-parameter and OOD results.
- Calibration/uncertainty and numerical convergence sensitivity.
- Trainable parameter count, iterations, wall time, peak physical memory bytes, reads/writes and transfers where measured.
- Host CPU/GPU usage and energy only when measured with a stated instrument/boundary.
- Retries, failed runs, missing data and total resource budget.
- Cost per accepted useful output only with a comparable billing/amortization basis; otherwise `null`.

Logical state count, residual magnitude and estimated operation count are not physical bytes, joules or cost.

## Acceptance and falsification

A candidate is eligible for further study only if it passes source provenance, output-quality, constraint, held-out and counterexample checks. Reject a method-level advantage if it does not improve pre-registered accepted-output quality/reliability within the matched budget, violates hard constraints, fails on sharp-gradient cases, or cannot be independently replayed.

A result on one PDE class does not transfer automatically to quantum workloads, biomass conversion, fusion plant models or another physical domain. For each transfer, state the shared mathematical interface and run a new matched test.

## Evidence promotion

- `DESIGN_ONLY`: contract authored, no run.
- `MODEL_ONLY`: numerical experiment with pinned code/data; not physical energy or commercial evidence.
- `INDEPENDENTLY_REPRODUCED_MODEL`: separate implementation reproduces the reference within preregistered tolerances.
- `PHYSICAL_MEASUREMENT`: calibrated instrument and physical boundary recorded.
- `ECONOMICALLY_VALIDATED`: accepted output and full comparable lifecycle cost measured.

No generated equation becomes a physical law by fitting. Promotion requires explicit incumbent assumption, alternative equation, dimensions, symmetry/conservation/causality checks, limiting cases, falsifier, discriminating observable, held-out prediction, proof/simulation as applicable, experiment and independent validation.
