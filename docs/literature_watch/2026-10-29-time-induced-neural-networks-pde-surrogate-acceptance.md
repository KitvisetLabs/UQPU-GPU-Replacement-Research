# Literature watch — TINNs for time-dependent PDE surrogates

**Watch date:** 2026-10-29  
**Primary owner:** Lane H; interfaces A/C/F/D/G; INV-034/035  
**Evidence class:** OFFICIAL PMLR ICML 2026 PAPER; THIRD-PARTY MODEL RESULTS; UQPU REPRODUCTION NOT RUN

## Source and method

Dai et al., “TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs,” ICML 2026 / PMLR 306: https://proceedings.mlr.press/v306/dai26a.html. Code link: https://github.com/CYDai-ml/TINN. The architecture parameterizes network weights as a learned function of time and uses a nonlinear least-squares formulation optimized with Levenberg–Marquardt. The publisher reports up to 4x relative L2-error improvement and up to 10x faster convergence on evaluated tasks.

## Limitations and follow-up

These are author-reported task-specific results, not universal guarantees. Random-point error does not prove trajectory/regime generalization, conservation, positivity or correct extrapolation. UQPU has not pinned the implementation/data/license or reproduced the result.

Use the existing Lane A acceptance contract: pin source/data/license/environment; freeze a known-law PDE and converged numerical reference; split by complete trajectories and physical regimes; compare PINN, TINN and compatible operator-splitting baseline under equal budgets; report median/worst-case error, residuals, conservation/bounds, failures, wall time, memory, bytes moved, energy when instrumented and cost per accepted result. Do not start with an uncalibrated reactor or fusion-cooling model.

**Non-claims:** no UQPU reproduction, physical law, QPU advantage, commercial fuel/electricity result, lower WACC or phone-class physical compression is established.
