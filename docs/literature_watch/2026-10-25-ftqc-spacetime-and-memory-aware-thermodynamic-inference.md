# Literature watch — 2026-10-25: fault-tolerance spacetime bounds and memory-aware thermodynamic inference

**Accessed:** 2026-10-25  
**Primary owner:** Lane H — foundational research publication and strategic integration  
**Implementation owner:** Lane A — workload/resource contracts  
**Integration owners:** Lanes C and F — state/memory accounting and evidence/economics  
**Feeds:** A–H; FND-001–006; EQN-001–006; INV-025–027; INV-029–035  
**Evidence class:** one arXiv theory preprint plus one Physical Review Letters accepted paper  
**Project evidence promotion:** none

## Executive delta

Two relevant sources were absent from the current repository's literature index. They sharpen different parts of the project's accounting discipline:

1. A quantum-memory theorem quantifies a width–duration tradeoff in fault-tolerant spacetime resources under a stated independent-erasure model.
2. A PRL-accepted thermodynamic-inference result shows why memory depth in observed trajectories matters when inferring entropy production in strongly non-Markovian systems.

Neither result establishes a UQPU advantage, a new physical law, lower energy use, or commercial fusion/bio-oil performance. The first is a theory result under explicit assumptions; the second is a method/theory result for inference, not a project experiment.

## Source 1 — fault-tolerance spacetime lower bound

Kishor Bharti, Tobias Haug and Andrew Tanggara, “Fault-tolerant quantum computation cannot be achieved with constant spacetime overhead,” arXiv:2608.26272v1, submitted 2026-08-26. Official preprint: https://arxiv.org/abs/2608.26272 ; HTML full text: https://arxiv.org/html/2608.26272v1.

For the stated independent-erasure quantum-memory model, ideal recovery, and the paper's specified noise and diamond-norm error conditions, the authors derive

`C_min(K,S,epsilon) = Theta(S * (K + log(S/epsilon)))`,

where `K` is the number of logical qubits, `S` the number of storage time steps, and `epsilon` the target memory-channel error. The relative-overhead scaling is `Theta(1 + log(S/epsilon)/K)`. The additional reliability term is important for a narrow register stored for a long time; sufficiently wide registers can amortize it. The paper also states broader results under additional conditions, but its tight expression must not be applied indiscriminately to every noise model or architecture.

**Genuine novelty for UQPU:** this gives a concrete, dimensionless screening term for the width–duration tradeoff that should accompany QSP/QSVT, iterative phase-estimation, long-time simulation and other long-lived coherent-register estimates. It reinforces that peak qubit count alone is not a complete resource contract.

**Limitations:** the asymptotic `Theta` statement hides constants; the ideal-recovery memory model is not a hardware bill of materials; actual devices add gate, syndrome extraction, decoding, feed-forward, communication, leakage, calibration, state-preparation, cooling and control costs. It does not say all wide computations have growing relative overhead, and it does not imply an exact resource count from the logarithmic term alone.

## Source 2 — thermodynamic inference with memory

Tassilo Schwarz, Anatoly B. Kolomeisky and Aljaž Godec, “Consistent time reversal and reliable and accurate inference in the presence of memory,” *Physical Review Letters*, accepted 2026-09-25, DOI https://doi.org/10.1103/gwf7-6kvr. Official APS accepted-paper page: https://journals.aps.org/prl/accepted/10.1103/gwf7-6kvr.

The authors derive a (k)-th-order estimator for entropy-production rate and prove necessary and sufficient conditions for guaranteed lower bounds on dissipation in strongly non-Markovian observations. Their analysis warns that a Markov estimator without a justified time-scale separation can create artifacts, while an estimator that does not account for sufficient memory order can overestimate dissipation.

**Genuine novelty for UQPU:** FND-001 should not infer a thermodynamic gap from coarse trajectories using an assumed first-order Markov model unless that assumption is independently justified. Memory order, observation window, estimator coverage and uncertainty must be recorded alongside the physical energy boundary.

**Limitations:** the paper does not measure UQPU wall-plug energy, Landauer erasure heat, fusion-plant energy, or biomass conversion. The result supplies an inference method and conditions, not a substitute for calibrated energy meters, complete process boundaries or experimental replication.

## Exact project relevance

- **Lane A / INV-025–027:** add the width–duration scaling term to long-lived coherent-workload resource estimates; keep it separate from M-QSP feasibility, oracle query counts and target-native gate counts.
- **Lane B:** provider estimates must distinguish physical/logical width, coherent duration, error target and the actual correction/control model. No provider's pricing may be combined with another target's error or success probability.
- **Lane C / INV-029:** account for quantum state retention over time separately from readable classical memory, persistent storage, classical output and data movement. Qubits and Hilbert-space dimension are not automatically equivalent to readable bytes.
- **Lanes D/G:** the theorem can motivate later device/process requirements only after an architecture-specific noise model and control stack are supplied. It does not directly determine fabrication or packaging costs.
- **Lane E / INV-030–032:** the thermodynamic-inference paper is a methodological caution for trajectory-based process studies, not evidence of biomass-material substitution, accepted bio-oil yield, lithium/tritium recovery, fusion availability or net electricity.
- **Lane F / FIN-001 / INV-033:** reliability overhead and observation time can affect the cost/time-to-evidence budget, but no interest saving, lower principal, WACC reduction or commercial cost result follows from these papers.
- **INV-034/035:** use the theorem as a model-scoped resource constraint and the inference paper as a warning about hidden-memory assumptions. Neither permits bypassing known physics or promoting an AI-generated equation to law.

## Falsifiable follow-up

1. Keep the exact theorem statement, version, assumptions and source hash frozen in the fixture manifest.
2. Calculate `log(S/epsilon)/K` for preregistered `K,S,epsilon` grids and verify the paper's published illustrative values. Label this output `MODEL_ONLY_SCALING_DIAGNOSTIC`; do not fit hidden constants or report an exact overhead.
3. For a future target-specific estimate, require explicit noise model, physical/logical width, duration, recovery/decoding assumptions, gates, measurements, feed-forward, host compute, I/O, energy and total cost.
4. Separately build synthetic trajectories with known entropy production and controlled memory order. Compare order-(k) estimators with first-order Markov inference under equal sample budgets; preregister lower-bound coverage, bias, uncertainty and failure criteria. A failed coverage test is a negative result, not a candidate physical law.
5. Only then consider authorized physical measurements. No paid QPU job, material experiment, fusion test or financing action is authorized by this article.

## Next highest-value gate

Continue the still-open Lane A M-QSP constructive decision algorithm and independently reconstructed feasible/infeasible fixtures. The new scaling helper is only a resource-screening aid and does not replace that gate. Keep FND-001/002 assumptions explicit and carry any accepted result into device/system economics only after independent validation.
