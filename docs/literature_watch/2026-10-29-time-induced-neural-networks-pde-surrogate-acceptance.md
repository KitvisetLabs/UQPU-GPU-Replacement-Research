# Literature watch — time-induced neural networks for time-dependent PDEs

**Date checked:** 2026-10-29  
**Primary owner:** Lane H — literature surveillance and publication  
**Implementation interface:** Lane A — model/workload acceptance contracts  
**Cross-lane consumers:** C (state/memory/data movement), D/G (device and manufacturing thermal/process models), E (materials, reactors, cooling and energy systems), F (evidence and economics)  
**Evidence class:** LITERATURE_ONLY; UQPU reproduction not performed  
**Related:** INV-034, INV-035, FND-006, EQN-001–006, RG-A-TINN-TIME-DEPENDENT-PDE-001

## Primary source

Chen-Yang Dai, Che-Chia Chang, Te-Sheng Lin, Ming-Chih Lai and Chieh-Hsin Lai, “TINNs: Time-Induced Neural Networks for Solving Time-Dependent PDEs,” Proceedings of the 43rd International Conference on Machine Learning, Proceedings of Machine Learning Research 306 (2026), pp. 22358–22384. Official publisher record: https://proceedings.mlr.press/v306/dai26a.html.

## Reported method and genuine novelty

The paper targets a known weakness of conventional space-time physics-informed neural networks (PINNs): a single network with shared weights across all time points can struggle when the dynamics change substantially over time. TINNs parameterize the network weights as a learned function of time and formulate optimization as nonlinear least squares, using a Levenberg–Marquardt method. The publisher record reports up to 4× lower relative L2 error and up to 10× faster convergence than the compared PINN/strong baselines on the paper's tested tasks.

The actionable novelty for UQPU is a distinct time-conditioned model architecture plus solver choice, not a new governing equation. It complements, but is not the same as, neural-operator splitting that composes a pretrained operator dictionary at test time. The source deserves a pinned, grouped-holdout comparison rather than adopting its headline metrics as project evidence.

## Limitations and evidence boundary

- These are author-reported results in the source's experimental settings. UQPU has not downloaded and pinned the code/data, checked all dependencies/licensing, or reproduced the reported metrics.
- “Up to” improvements are not guaranteed for arbitrary PDEs, parameter regimes, geometries or initial/boundary conditions.
- Relative L2 error alone does not guarantee conservation, positivity, stability, correct boundary behavior, calibrated uncertainty or an accepted engineering output.
- Training, time-conditioning, nonlinear least-squares iterations, test-time inference, memory traffic and failed runs all consume resources. Faster convergence is not automatically lower total energy or lifecycle cost.
- A model that fits a known PDE is not evidence of a new physical law; an AI-generated equation still requires the full INV-035 validation ladder.

## Exact UQPU relevance

1. Lane A / FND-006 / EQN-001–006: add TINNs as a candidate baseline in a known-law benchmark, alongside a conventional PINN, the existing neural-operator-splitting family when available, and a trusted numerical solver.
2. Lane C: record peak host/device memory, state representation, data movement, checkpoint size and reconstruction. Do not treat fewer optimizer steps as lower bytes moved without measurement.
3. Lanes D/G: later evaluate held-out thermal/transient device and process regimes only after a validated model and suitable data exist. No device, yield or packaging claim follows from this paper.
4. Lane E: a possible future surrogate for heat-transfer, reactor or cooling transients; Pangola kinetics, saleable bio-oil, fusion net-electricity and cooling performance require their own calibrated inputs and evidence.
5. Lane F: compare cost per independently accepted held-out prediction under matched resource budgets, including training/search, failed runs, uncertainty, wall time, memory and energy where measurable.
6. Lane H: preserve the distinction between an external ML-method result and evidence for the strategic industrial/finance plan.

## Proposed falsifiable follow-up

Freeze source revision, dataset and provenance hashes, PDE family, preprocessing, numerical reference/tolerance, code/dependency environment, random seeds, optimizer-evaluation budget and acceptance predicate before running. Split by entire physical regimes or trajectories—including coefficients, initial/boundary conditions, forcing or geometry—not random points from the same trajectory. Use at least 30 preregistered seeds where the selected benchmark permits meaningful stochastic repetition.

Report median and worst-case held-out relative error, PDE residual, conservation drift, bound/positivity violations, solver-reference convergence, uncertainty calibration if claimed, failure/timeout rate, training and inference wall time, peak memory, bytes transferred, energy if instrumented, and total cost per accepted result. Reject any apparent gain that depends on leakage, extra unreported optimization budget, a changed solver tolerance or a relaxed physical constraint. Preserve negative and inconclusive runs.

**Decision:** literature is sufficient to justify a benchmark gate, not adoption as a default model. No UQPU reproduction, new physical equation, physical law, material/fuel/electricity result, QPU advantage or economic advantage is established.
