# Integration handoff — INT-20261024-017 BIO-001 upgrading/acceptance gate

**Date:** 2026-10-24  
**Primary owner:** integration hub for cross-lane routing; Lane E owns the source literature artifact  
**Source artifact:** research_lanes/E_materials_energy_cooling_infrastructure/LITERATURE_WATCH_2026-10-24_BIO_OIL_UPGRADING.md  
**Canonical main at cycle start:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Evidence class:** external peer-reviewed experiment + external TEA model; no UQPU project evidence promotion  
**Status:** PROPOSED / PR REVIEW REQUIRED
**Supplementary surveillance update:** 2026-10-25
**Supplementary source commit:** 5b08f0293d3651ec6abcbc8a1d1568e863a02135

## Integrated delta

The two primary studies reinforce a measurable boundary for BIO-001: optimize the final accepted liquid-energy function, not crude bio-oil yield. The straw study supplies process variables and quality hazards for hydrotreating; the microalgae HTL study shows that cost-optimal settings can differ from yield-optimal settings and change with scale. Their numerical results are feedstock- and route-specific and must not be applied to Pangola without new measurements.

## 2026-10-25 supplementary coproduct delta

A peer-reviewed *Biomass and Bioenergy* 2026 study (DOI: https://doi.org/10.1016/j.biombioe.2026.109296) reports catalytic co-pyrolysis of a 1:1 microalgae–hardwood blend, bio-oil yields of 22.1 wt% without catalysis, 23.9 wt% in-situ and 23.5 wt% ex-situ at 500 °C, and a catalyst-loaded biochar tested for methylene-blue adsorption. This is a **candidate coproduct function only**: it does not establish Pangola fuel economics, a commercial adsorbent market, safe reuse, or an incremental net credit.

Before any BIO-001 credit is allowed, require a frozen functional unit, verified off-take or avoided-treatment cost, regeneration and disposal costs, leaching/contaminant qualification, uncertainty, and an explicit allocation rule. Do not assign the same char mass full credits for fuel, adsorption, soil amendment, carbon storage and material precursor simultaneously. Evidence class remains external literature; no project evidence is promoted.

## Shared interface

- **Input contract:** characterized dry feedstock lot, feedstock ID/hash, moisture/ash/composition, route/process window, product specification and frozen experimental design.
- **Output contract:** mass/energy closure; accepted-liquid yield; LHV and accepted MJ; hydrogen/catalyst/utilities; off-spec fractions; lifecycle cost per accepted litre and accepted MJ; uncertainty and independent replication status.
- **Evidence:** external literature is context only. Pangola measurements start at MODEL_ONLY/LAB_RESULT according to actual provenance and may not be promoted without the relevant test.
- **Accounting:** no double counting of coproduct credits; no combining of process cost with incompatible price years/currencies; unknown energy/cost remains null rather than zero.

## A–H integration edges

| Lane | Required handoff |
|---|---|
| A — quantum programming/runtime | If used for equation discovery or optimization, compare with classical process-optimization baselines on the same objective and budget; no quantum advantage inferred. |
| B — cloud/QPU | No provider calls or QPU jobs required for this gate. |
| C — state/memory/data movement | Preserve raw experimental records and hashes; count storage/data movement only if measured. |
| D — device/process/materials | Translate catalyst, reactor pressure/mixing, heat-transfer, corrosion and material compatibility into a testable process-window contract. |
| E — biomass/energy | Own feedstock qualification, conversion/upgrading experiment and accepted-product measurement. |
| F — economics/evidence | Own accepted-litre/MJ cost ledger, sensitivity, uncertainty and non-double-counted coproduct audit. |
| G — manufacturing equipment/factory | Co-design scale-up, continuous reactor, metrology and process-control equipment with D only after bench-scale evidence. |
| H — strategy/finance | Gate capital on the cheapest decisive experiment; measure financed principal and time-to-evidence, not speculative WACC savings. |

## Invariants and non-claims

- **INV-029:** no physical compression or phone-class capability evidence.
- **INV-030:** no elemental transmutation or Pangola critical-material substitution result.
- **INV-031:** no commercial ultra-low-cost bio-oil/biofuel result.
- **INV-032:** no fusion-electricity result; separate FUS-001 remains its own architecture-neutral net-electric accounting path.
- **INV-033:** no financing-rate/WACC result; only a future measured principal/time-to-evidence effect could support an absolute-interest calculation.
- **INV-034/035:** existing physical laws remain binding; equation discovery must include dimensions, conservation, limits, falsifier, held-out prediction, counterexamples and independent validation.

## Next gate

Run BIO-001-UPGRADE-ACCEPTANCE-001 on a characterized Pangola/residue lot only when a safe, appropriate laboratory protocol and measurements are available. First freeze the product specification and accounting boundary; then measure mass/energy closure, upgrading requirements and accepted yield. Do not scale or claim commercial economics from literature values alone.
