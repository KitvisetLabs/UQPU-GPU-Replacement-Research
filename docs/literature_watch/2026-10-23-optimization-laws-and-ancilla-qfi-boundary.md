# Literature watch — 2026-10-23: optimization-law discovery and ancilla-QFI no-go boundary

**Accessed:** 2026-10-23  
**Primary owner:** Lane H — strategy / future-industry research  
**Feeds:** A, B, C, F, FND-002, FND-003, FND-006, EQN-001–006, INV-029, INV-034, INV-035  
**Evidence class:** `LITERATURE_ONLY / THIRD_PARTY_PREPRINT`  
**Project evidence promotion:** none

## Sources reviewed

1. Ma ZhenYao, Yue Liang and Jian-Qiao Zhu, *OptScientist: Automated
   Discovery of Optimization Laws*, arXiv:2610.28562v1, submitted 2026-10-20:
   https://arxiv.org/abs/2610.28562
2. Qi Liu, Xin-Yu Hao and Jing Liu, *Evaluation of the quantum Fisher
   information for large systems via an ancilla*, arXiv:2610.29146v1,
   submitted 2026-10-21: https://arxiv.org/abs/2610.29146

Both are unrefereed preprints as observed. Neither is project execution
evidence, a demonstrated physical law, a device result, or an economic result.

## Material delta 1 — optimization laws are a distinct discovery target

OptScientist searches for compact symbolic **optimization problems**, rather
than only input-output equations. Its synthetic OptFeynman evaluation converts
99 analytic-physics equations into latent objective landscapes and separates
training, validation and test contexts. The paper reports perfect exact-order
recovery on 88/99 discrete problems and 78/99 continuous problems on held-out
contexts. It also reports two observational-data case studies and a lower
LLM-output-token count than its selected LLM baselines.

The relevant novelty for UQPU is methodological: EQN candidates may encode an
objective and constraints, not only a closed-form response equation. This adds
a useful generator family for control, compilation and architecture search.

### Limits that block promotion

- OptFeynman is derived from known equations; it is not blind discovery of new
  physics.
- Real-world case-study laws have unknown ground truth. Held-out prediction
  does not establish causal mechanism, uniqueness, or physical truth.
- The authors state that the method is likely to fail when the true structure
  differs substantially from an optimization formulation.
- The reported token comparison excludes training and symbolic-search compute.
  It therefore cannot be treated as total energy, time, or cost efficiency.
- The work does not supply UQPU-specific counterexample search, proof,
  independent replication, device consequence, or accepted-task economics.

### Falsifiable project follow-up

Create an `EQN-OPT-001` benchmark from an existing project model whose
objective and constraints are known but hidden from the generator.

1. Freeze train/validation/test context hashes before discovery.
2. Compare direct equation discovery against optimization-law discovery under
   matched wall-clock, host-energy and token budgets.
3. Score exact structure, dimension/symmetry/conservation checks, constraint
   recovery, out-of-distribution objective ordering, and counterexamples.
4. Include a deliberately non-optimization generator family as a negative
   control.
5. Reject the candidate if an equally predictive, materially different
   objective survives the identifiability test.

Passing this benchmark would be internal computational evidence only. It would
not make a generated expression a physical law.

## Material delta 2 — an assumption-scoped QFI transfer no-go theorem

The ancilla-QFI preprint studies transferring a large system's quantum Fisher
information (QFI) to a lower-dimensional ancilla through a controlled unitary.
Under an already-optimal projective measurement and the paper's protocol class,
let `m` be the number of distinct nonzero values of
`partial_x log(p_i)` and `n` the ancilla dimension. Its Theorem 2 states
that no “perfect” protocol in this class exists when `m > n`, where perfect
means equality between the reduced ancilla QFI and the system QFI.

This is a useful capacity boundary for claims that a small observable subsystem
can losslessly expose all parameter information of a larger system. It is not
a general no-go theorem for quantum compression, readable memory, computation,
or the Data-Center-to-One-Phone mission.

### Limits and audit flags

- The theorem is scoped to the stated controlled-unitary/measurement model and
  assumes an optimal system measurement basis.
- It concerns QFI for a parameterized state, not arbitrary useful output,
  classical state recovery, RAM/VRAM capacity, or computational advantage.
- The paper demonstrates a GHZ circuit example but no UQPU target execution,
  accepted-task economics, or end-to-end provider measurement.
- The conclusion describes a count of distinct `p_i` values, whereas the
  theorem statement uses distinct nonzero `partial_x log(p_i)` values. This
  notation mismatch must be resolved from the derivation before reuse.
- The proof and attainability conditions require independent mathematical and
  numerical reproduction.

### Falsifiable project follow-up

Create `FND-QFI-001` with small exactly solvable parameterized states:

1. Enumerate cases with `m <= n` and `m > n`.
2. Optimize the allowed controlled unitaries numerically and compare system QFI,
   ancilla QFI and sub-QFI with high precision.
3. Search for counterexamples at rank changes, zero probabilities and
   near-degenerate log-derivatives.
4. Formalize the theorem assumptions and the `m` definition in the certificate.
5. Only after analytic/numerical agreement, evaluate whether the boundary
   constrains any specific UQPU measurement contract.

Failure would be recorded as a theorem-reproduction discrepancy, not hidden.

## A–H integration status

| Lane | Delta or retained boundary |
|---|---|
| A | Adds `EQN-OPT-001` as a possible objective/constraint discovery benchmark; no compiler/runtime advantage. |
| B | No provider call, credential use, snapshot, job, shot or billable usage. |
| C | QFI transfer is not readable classical memory or storage; no capacity equivalence. |
| D | No device, process, fabrication or packaging evidence. |
| E | No new Pangola/material, BIO-001, FUS-001, cooling or infrastructure evidence. |
| F | Token counts are not total cost; no accepted-task economics or WACC evidence. |
| G | No manufacturing-equipment or factory-system consequence before a device requirement exists. |
| H | Literature surveillance and falsifiable follow-up design are the substantive advance. |

D/G co-design remains unchanged and fail-closed. BIO-001, FUS-001 and FIN-001
were inspected but receive no evidence-class promotion.

## Invariant contribution

- **INV-029:** the QFI result is recorded only as a possible small-interface
  information boundary; it does not demonstrate physical data-center
  compression into one phone.
- **INV-030:** no material substitution or elemental-transmutation claim.
- **INV-031:** no commercial bio-oil evidence.
- **INV-032:** no net delivered fusion-electricity evidence.
- **INV-033:** no financing-rate or interest-cost evidence.
- **INV-034:** adds a precise, assumption-scoped theorem-reproduction target.
- **INV-035:** broadens the generator class to optimization laws while retaining
  dimensional, symmetry, conservation, causality, limiting-case, falsifier,
  held-out, counterexample, proof/experiment and independent-validation gates.

INV-025/026/027 and the 100x/100,000,000x moonshots remain unproven. No
Hilbert-space dimension is equated with readable memory, and no NPU comparison
is inferred from TOPS or QFI.

## Surveillance boundary

The fresh scan also screened agentic domain-specific symbolic-regression work,
but found no additional result that changed UQPU evidence gates for materials,
bio-oil, fusion electricity, financing, manufacturing or provider execution.
Absence from this watch is not evidence that those fields are static.

## Next highest-value gate

The project execution gate remains the authorized read-only `ibm_kingston`
snapshot and exact route/native-conformance certificate preregistered by
QOS-AUDIT-010B25. The literature-derived next research gate is smaller and
offline: reproduce the ancilla-QFI theorem on exactly solvable cases before
allowing it to constrain any architecture claim.
