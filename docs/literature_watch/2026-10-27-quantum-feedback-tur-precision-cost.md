# Literature watch — 2026-10-27: quantum-feedback thermodynamic uncertainty and precision-cost accounting

**Primary source:** Ryotaro Honma and Tan Van Vu, “Thermodynamic Uncertainty Relation with Quantum Feedback,” *Physical Review Letters* **137**, 160406, published 2026-10-16, DOI [10.1103/6d8l-94pv](https://doi.org/10.1103/6d8l-94pv).  
**Official preprint:** [arXiv:2602.22651v2](https://arxiv.org/abs/2602.22651v2), revised 2026-10-22 (PDF dated 2026-10-23).  
**Evidence class:** PEER-REVIEWED THEORETICAL RESULT + OFFICIAL PREPRINT; not independently reproduced by UQPU.  
**Owners:** Lane H (publication), Lane A (equation reconstruction/reference fixture), Lane F (measurement and economic boundary).  
**Feeds:** FND-001, FND-003, FND-006, EQN-001–006, INV-034/035; interfaces A/C/D/G/F/H.

## Material delta

This paper is distinct from Batch 080's conditional work-of-formation/extractable-work bounds. Honma and Vu study the precision of time-integrated currents in a finite-time feedback process. For open quantum systems weakly coupled to a thermal environment, with monitored quantum jumps and Markovian feedback, they derive a thermodynamic uncertainty relation (TUR) in which current fluctuations depend on both entropy production and quantum mutual information exploited by feedback.

The paper's stated model assumes a finite-dimensional system, local detailed balance for paired jump operators, a GKSL description in the no-feedback baseline, instantaneous feedback after detected jumps, and **unital** feedback maps. The authors set \(\hbar=k_B=1\) in the derivation. These assumptions are part of the result, not optional implementation details.

In the paper's notation, the information-thermodynamic cost over the interval is
\[
\Sigma = S_{\mathrm{tot}} - I \geq 0,
\]
where \(S_{\mathrm{tot}}\) is the total entropy production and \(I\) is the information exploited during feedback. Its central finite-time bound (Eq. 15) is
\[
\frac{\operatorname{Var}[J]}{\langle J\rangle^2}
\geq \frac{2(1+\delta_J)^2}{\Sigma},
\qquad
\delta_J = \frac{\langle J\rangle_\phi}{\langle J\rangle}.
\]
The correction \(\delta_J\) depends on an auxiliary traceless operator with its own dynamics (Eq. 16); it cannot be silently set to zero for arbitrary finite times. In the short-time limit the authors obtain a bound on the information-thermodynamic entropy-production rate from measured current mean and variance (Eq. 17). A stronger form also uses dynamical activity (Eq. 18). These expressions are dimensionless in the paper's \(\hbar=k_B=1\) convention; any SI conversion must be derived rather than guessed.

## Genuine novelty and limitations

- **Novelty:** a finite-time current-precision bound explicitly includes mutual information used by feedback, with a correction term for quantum/transient effects. The paper reports recovery of the original TUR without feedback and in the classical limit.
- **Model boundary:** weak thermal coupling, continuously monitored jump trajectories, Markovian instantaneous feedback, local detailed balance, and unital feedback. General non-Markovian controllers or non-unital channels are not automatically covered.
- **Not established:** no UQPU experiment, implementation, measured device-energy reduction, speedup, accepted-task cost reduction, or new physical law follows from this publication.
- **Accounting boundary:** \(\Sigma\) is not wall-plug joules, electricity price, total controller CAPEX, or cost per accepted computing task. Acquisition, controller processing, readout, feedback actuation and reset still need their own measured ledger if a physical implementation is studied.

## Exact UQPU relevance

- **FND-001:** keep entropy production and exploited information explicit; do not treat feedback information as free.
- **FND-003:** add a theory-defined precision-cost comparator alongside matched control/QSL timing, without converting a TUR into a speed-limit or compute-energy bound.
- **Lane A:** candidate finite-dimensional reference target is the paper's three-level quantum clock. Reconstruct jump operators, detailed balance, tilted generator/current cumulants, \(\delta_J\), and the bound before coding.
- **Lane C:** the jump-outcome memory \(M\), measurement record and state representation are distinct from readable classical storage capacity; count data movement separately.
- **Lanes D/G:** only if mapped to a real controller later, derive readout/control/reset metrology requirements; no device or factory claim now.
- **Lane F:** separate current mean/variance, entropy production, mutual information, wall-plug energy, and monetary costs in the common evidence contract.
- **Lanes E/H:** this is a methodology constraint only. It provides no evidence for Pangola material substitution, accepted bio-oil, net fusion electricity, lower financing rates or the Data-Center-to-One-Phone mission.

## Falsifiable follow-up

1. Pin the APS version and arXiv v2, then transcribe Eqs. 1–18 and their symbol/units table from the primary source.
2. Independently rebuild the three-level clock with a tilted Liouvillian and a separate trajectory-based current estimator; freeze source parameter values before running.
3. Verify local detailed balance, unital-map assumptions, \(\Sigma\geq0\), finite-time Eq. 15, the short-time Eq. 17 limit, the no-feedback/classical limits, and the activity-refined Eq. 18 where implemented.
4. Retain failed inequalities and counterexamples. Use held-out parameter sets and convergence tests; do not tune against only the published plot.
5. Only after independent reproduction, assess whether any experimentally realizable controller maps to a UQPU task. Measure controller/readout/reset energy at the device boundary and report cost per accepted useful task separately.

The canonical implementation gate is [RG-FND003-QUANTUM-FEEDBACK-TUR-REPRODUCTION-001](../RESEARCH_GAP_FND003_QUANTUM_FEEDBACK_TUR_2026-10-27.md). This literature watch records external theory, not project evidence.
