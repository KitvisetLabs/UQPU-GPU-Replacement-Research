# Literature watch — 2026-10-26: thermodynamic bounds with quantum feedback

**Accessed:** 2026-10-26  
**Primary owner:** Lane H — strategic research and publication  
**Integration owner:** Lane F — evidence, benchmarks and economics  
**Implementation consumer:** Lane A — quantum programming/workloads/compiler/runtime  
**Cross-cutting programs:** FND-001, FND-002, FND-003, EQN-001, EQN-006  
**Evidence class:** `LITERATURE_ONLY` / author-reported theoretical bounds  
**Project evidence promoted:** no  
**Canonical starting main:** `5fbe3d295ad6ca5b7c701f05c64899829910cbe8`

## Source and publication state

- Kaiyuan Ji, Gilad Gour and Mark M. Wilde, “Fundamental limits for thermodynamic control with quantum feedback,” *Physical Review Letters*, accepted 6 October 2026, DOI [10.1103/x67n-33gr](https://doi.org/10.1103/x67n-33gr). Official APS accepted-paper record: https://journals.aps.org/prl/accepted/10.1103/x67n-33gr
- Authors’ arXiv manuscript: [arXiv:2503.09012](https://arxiv.org/abs/2503.09012); the indexed v4 was revised 9 October 2026.

The authors derive single-shot bounds on work of formation and extractable work when a controller holds quantum side information and feeds it back coherently. In the asymptotic regime they formulate a generalized second law using conditional Helmholtz free energy. Their stated consistency result explicitly accounts for acquisition, processing and reset of side information.

## Genuine UQPU-relevant delta

The useful contribution is a sharper **accounting boundary**, not a claim that quantum feedback is free or that UQPU has an energy advantage. A quantum side-information register is not interchangeable with an uncharged classical record. Any proposed feedback-enabled workload must declare how the side information is prepared/acquired, retained, processed, coupled back to the system, read out if needed, and reset or otherwise disposed of.

This is directly relevant to:

- **FND-001 — thermodynamic-gap accounting:** keep thermodynamic work bounds separate from wall-plug energy per accepted useful task. A conditional free-energy expression is not a meter reading.
- **FND-002 — output-information lower bounds:** identify what information is output, retained, or consumed as side information; do not hide the controller's memory and readout boundary.
- **FND-003 — matched speed-limit measurement:** use the new work-accounting result alongside, not as a substitute for, gate-level or state-evolution time bounds. A work bound and a time bound are different contracts.
- **Lane A/B/C:** a future runtime/provider experiment would need a same-target state-transition contract plus controller memory, transfer, control, measurement and reset records. No provider-independent numerical result can be inferred from this paper alone.
- **Lane F/H and INV-033:** include control-side resources in lifecycle and financing models; this result does not demonstrate lower CAPEX, OPEX, principal, interest or WACC.
- **INV-029–032:** no data-center-to-phone, biomass-material, accepted-fuel or net-fusion-electricity gate is closed. At most, the paper improves the list of terms a future system boundary must not omit.

## Limitations and non-claims

1. This is a theoretical result reported in an accepted paper and public manuscript, not an UQPU reproduction or an experiment on a UQPU device.
2. The work quantity in a thermodynamic resource theory is not automatically equal to wall-plug electrical energy, cloud-provider billing, lifecycle cost or useful-work throughput.
3. The result does not remove Landauer, causality, measurement, memory, control or reset requirements; it formalizes bounds under stated operational assumptions.
4. No new physical law is proposed here. No symbolic-regression result, simulation, literature result or mathematical state-space size is promoted to physical evidence.
5. The paper does not show that quantum feedback beats a competitive classical controller after all acquisition, processing, storage, reset and implementation costs are included.

## Falsifiable follow-up — FND-QFB-001 (proposed, not implemented)

**Question:** Under a frozen finite-dimensional state-transition contract, does an independently reproduced quantum-side-information work bound change the *allowed thermodynamic work interval* relative to classical/dephased side information and no side information, after all three cases use the same declared boundary?

1. Transcribe the paper’s exact theorem and assumptions from arXiv v4; record notation, units, Hamiltonians, allowed operations and the work-reservoir model. Do not infer formulas from the abstract.
2. Freeze small qubit-level fixtures with known states and Hamiltonians. Include (a) quantum side information, (b) a classical/dephased record with matched accessible information, and (c) a no-side-information negative control.
3. Independently implement the stated single-shot bounds and the asymptotic conditional-free-energy limit; compare symbolic/algebraic checks where available and numerical values on held-out parameter combinations.
4. Record side-information preparation/acquisition, storage/coherence retention, controller processing, transfer/coupling, measurement, reset/disposal and all omitted-resource flags. If an apparent advantage depends on an uncharged resource or a changed boundary, fail closed.
5. Keep **thermodynamic work**, **measured wall-plug energy**, **provider charges**, and **cost per accepted useful task** in separate fields. A model-only result must not be promoted to any of the latter.
6. Require independent review/reproduction before any laboratory proposal. Any paid QPU execution still requires credentials, a bounded budget and explicit user consent.

**Pass condition:** the theorem and implementation agree on frozen and held-out fixtures, assumptions are explicit, and the full controller-side resource ledger is complete.  
**Fail condition:** disagreement with the source theorem, hidden side-information resources, unhandled reset/acquisition terms, or a conclusion that depends on silently changing the system boundary.  
**Evidence expected at first pass:** `MODEL_ONLY` mathematical reproduction, not a physical measurement or economic advantage.

## A–H integration review

| Lane | Relevance now | Evidence boundary / next gate |
|---|---|---|
| A — quantum programming/workloads/compiler/runtime | Extend accepted-task resource contracts to expose controller-side quantum information and reset costs if a feedback workload is proposed. | No code change or workload result in this watch; integrate only after the exact theorem is independently transcribed. |
| B — cloud/QPU/provider integration | Any future test must keep target identity, calibration, provider price and output probability matched. | No credentials used; no QPU job submitted. |
| C — memory/state/data movement | Side information is a state/memory and transfer resource, not free readable classical storage. | No memory-capacity or transfer measurement. |
| D — device/chip/process/fabrication/packaging | Future coherent feedback may impose control, retention and reset requirements. | No device or fabrication consequence yet. |
| E — biomass/materials/bio-oil/fusion/cooling | No direct materials, fuel or net-electricity result; full-boundary accounting is the only transferable method principle. | BIO-001 and FUS-001 remain open. |
| F — economics/benchmarks/evidence/integration | Separate thermodynamic work from electrical energy, provider billing and lifecycle cost. | No measured economic delta. |
| G — chip manufacturing equipment/software/factory systems | Translate a validated control/memory requirement into manufacturable requirements only after Lane A/B evidence exists. | No manufacturing result. |
| H — strategy/finance/publication | Publish the source-bounded literature delta and explicit falsifier while preserving strategic context. | No funding, principal, interest or WACC result. |

## Mission and invariant disposition

INV-025/026 remain evidence-gated subsystem-equivalence moonshots; Hilbert-space dimension is not readable classical storage. INV-027 and INV-034 remain open to foundational mathematics under explicit falsification. INV-035 is followed: candidate mathematical interpretations remain subordinate to the incumbent theorem, declared assumptions, independent checks and physical evidence.

INV-029 through INV-033 remain **unclosed**: this literature watch does not demonstrate phone-class physical compression, Pangola material substitution, saleable ultra-low-cost fuel, reliable net fusion electricity, lower project principal/interest, or lower financing rates. The US$10T–US$100T figure remains an ambition-scale proxy only.

**Next gate:** implement the source-exact, three-control FND-QFB-001 mathematical reproduction and resource-boundary validator; compare its inputs with the existing FND-001 accepted-task ledger before any experiment is proposed.
