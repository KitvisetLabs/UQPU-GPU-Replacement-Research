# Literature watch — 2026-10-24: thermodynamic speed limits for isolated quantum systems

**Accessed:** 2026-10-24 (Asia/Bangkok)  
**Primary owner:** Lane H — strategy / foundational-method surveillance  
**Integration owner:** Lane F — evidence, benchmarks and reproducibility  
**Feeds:** FND-001, FND-003, FND-006, EQN-001–006; conditional downstream links to A–C and F  
**Evidence class:** PEER-REVIEWED ACCEPTED PAPER / THIRD-PARTY METHOD RESULT  
**UQPU evidence promotion:** none

## Source and freshness

Rikuya Kobashi, “Thermodynamic speed limits in isolated quantum systems,” *Physical Review Research*, accepted 6 October 2026, DOI [10.1103/k16k-nx74](https://doi.org/10.1103/k16k-nx74). The official APS accepted-paper record was checked during this cycle: [APS source](https://journals.aps.org/prresearch/accepted/10.1103/k16k-nx74). The author's public preprint is [arXiv:2609.12520](https://arxiv.org/abs/2609.12520), submitted 11 September 2026.

A search of canonical main found no existing watch for this title/DOI. This is a newly recorded literature delta for the project, not a claim that the paper was published on 24 October.

## Genuine technical delta

The paper derives thermodynamic speed-limit inequalities for finite-time unitary driving of isolated quantum systems. It relates entropy production defined at a chosen thermodynamic coarse-graining to the Vu–Saito quantum Wasserstein distance between coarse-grained initial/final states. Dividing the entropy-production lower bound by the average entropy-production rate yields a lower bound on protocol duration.

For the paper's Gibbs-entropy setting, the stated results include a quadratic distance bound and a finite-dimensional linear bound. In the paper's units and definitions, their time-limit forms are:

- `tau >= ln(2) * (W_q^G)^2 / <sigma_G>`;
- `tau >= ln(d/(d-1)) * W_q^G / <sigma_G>` for finite dimension `d`.

These are not universal gate-time constants: `W_q`, the entropy-production quantity, coarse-graining, initial-state conditions and Hamiltonian protocol must match the theorem. The paper also treats observational-entropy coarse-grainings for system–bath, local-energy and energy-basis/diagonal-entropy settings. Its quantum Wasserstein quantity is a pseudo-metric depending on state spectra; zero distance can mean unitary equivalence rather than identical density operators.

## Why this matters to UQPU

- **FND-003 (quantum-speed-limit gap):** adds a candidate thermodynamic/coarse-grained lower-bound family to compare with the incumbent Margolus–Levitin and Mandelstam–Tamm bounds under the *same* Hamiltonian, initial/final state, energy convention and accepted task. It may tighten some bounds, be redundant, or be too loose to affect an engineering decision; that is the experiment.
- **FND-001 (thermodynamic-gap accounting):** supplies a possible state-transformation/entropy-production accounting term. It does not replace the Landauer erasure floor and does not establish achievable wall-plug efficiency.
- **FND-002 / Lane C:** coarse-grained distinguishability and a quantum Wasserstein distance are not readable classical output bits, RAM/VRAM/HBM capacity, storage, or lossless arbitrary-state compression.
- **Lane A / F:** a bound can constrain a proposed workload only after the workload's accepted-output contract, target dynamics and measured resource boundary are fixed. A lower bound is not an expected runtime or a measured speedup.
- **Lanes D/G and E:** the paper supplies no device, fabrication, material, Pangola, bio-oil, fusion, cooling or factory result.
- **Lane H / INV-033:** the paper gives no project-finance, interest or WACC evidence. A useful bound might reduce wasted experiment time only if a future, separately measured protocol shows that effect.

## Limitations and evidence boundary

1. This is a third-party theoretical-method result, not an experiment on UQPU or a present cloud-QPU target.
2. The result is tied to the selected entropy functional, coarse-graining, initial-state conditions and unitary protocol. It must not be transplanted unchanged to noisy/open hardware or arbitrary algorithms.
3. The Vu–Saito distance depends only on spectra and is a pseudo-metric. A zero value need not mean the underlying states are equal.
4. The entropy-production rate may be zero, ill-conditioned or estimated from incomplete observables; division by it requires explicit domain checks and uncertainty treatment.
5. A tighter mathematical lower bound does not prove a device can attain it, does not establish quantum advantage, and does not imply physical data-center-to-phone compression.
6. No UQPU code, device experiment, provider execution, accepted-task cost, or new physical law was validated by the paper.

## Proposed falsifiable follow-up: FND-003-TSL-001

**Status:** PROPOSED / NOT EXECUTED  
**Evidence class:** future MODEL_ONLY analytic reproduction until independently checked

1. Freeze a deterministic suite of exactly solvable two- and three-level unitary protocols with known `H(t)`, initial state, final state, protocol duration, and explicit Gibbs/observational coarse-grainings.
2. Include passive initial states satisfying the relevant theorem assumptions, and negative controls for non-passive initial states, changed coarse-graining, degeneracies, rank/support changes, zero entropy-production rate, and unitarily equivalent states with zero pseudo-distance.
3. Compute the paper's `W_q`, entropy production and average rate directly from its definitions. Verify dimensional consistency and the inequality on every in-domain case; retain every counterexample or numerical-conditioning failure.
4. Compare the new bound with Margolus–Levitin and Mandelstam–Tamm bounds using identical energy and state-transition conventions. Report which bound is strongest per case, the gap to exact protocol time, numerical precision, runtime and memory.
5. Freeze train/validation/test Hamiltonian families and seeds before evaluating any fitted or learned estimator; do not tune on held-out cases.
6. Independently rederive the inequality and implement the small-system calculation separately before allowing the result to influence FND-003 architecture decisions.
7. Reject the proposed engineering relevance if valid cases violate the theorem, if the result depends on an unstated assumption, or if it never tightens an incumbent bound on any mission-relevant contract. A successful finite fixture remains MODEL_ONLY and does not establish physical law or device performance.

The critical question is whether this bound changes a matched-control measurement or experiment-selection decision—not whether another inequality can be added to a catalogue.

## A–H and invariant contribution

| Lane / invariant | Consequence of this watch |
|---|---|
| A — workloads/compiler/runtime | Candidate bound for a later same-task timing/resource contract; no compiler or runtime advantage. |
| B — cloud/QPU integration | No provider, credentials, service, job, shot or billable usage. |
| C — state/memory/storage | No readable-memory or state-compression equivalence. |
| D — device/chip/fabrication | No device requirement or fabrication result until a measured protocol identifies one. |
| E — materials/energy/infrastructure | No Pangola, accepted liquid fuel, net delivered fusion electricity or cooling evidence. |
| F — economics/evidence | Future comparisons must include time-to-evidence and full cost; no economic result now. |
| G — manufacturing systems | No equipment/factory consequence without a validated device requirement. |
| H — strategy/foundations | Records a falsifiable FND-003 candidate and primary-source trail. |
| INV-029 | Does not demonstrate physical Data-Center-to-One-Phone compression. |
| INV-030–033 | No material substitution, commercial bio-oil, net reliable fusion electricity, principal/interest reduction or WACC effect. |
| INV-034 | Extends the foundational search with an assumption-scoped thermodynamic-bound candidate. |
| INV-035 | Keeps incumbent physics binding and requires explicit assumptions, units, limiting cases, falsifiers, held-out tests and independent validation. |

The permanent root directives 00–06, the Kanusanan Pongpanna Model, strategic AI-agent/funding references, and Thai/English/Chinese/Japanese/Korean/German master-plan links remain unchanged. INV-025/026/027 and the 100×/100,000,000× objectives remain evidence-gated goals.

## Next highest-value gate

Implement the exact small-system FND-003-TSL-001 fixture and compare it with the incumbent QSL bounds under matched assumptions. Do not use it to authorize QPU submission; QOS-AUDIT-010B25 still requires an authorized, redacted, fresh read-only target snapshot, and any paid execution requires separate explicit user consent and a bounded budget.
