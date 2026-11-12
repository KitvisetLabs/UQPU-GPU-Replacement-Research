# Integration handoff — INT-20261024-019 FUS-001 cost-account adapter

**Date:** 2026-10-24  
**Primary owner:** integration hub for cross-lane routing; Lane E owns the literature artifact  
**Source artifact:** research_lanes/E_materials_energy_cooling_infrastructure/LITERATURE_WATCH_2026-10-24_FUSION_COST_ESTIMATION.md  
**Canonical main at cycle start:** c7b5958af58fad04a101ef5c6abf6a29293c867e  
**Status:** PROPOSED / PR REVIEW REQUIRED  
**Evidence class:** external cost-model methodology; no UQPU plant or economic result promoted

## Integrated delta

The September 2026 ACCERT adaptation supplies a potential common cost-account interface for multiple magnetic-confinement concepts and exposes sensitivity to magnets, breeding blankets and material choices. FUS-001 should reuse the traceability idea, not copy absolute cost outputs across incompatible architectures or treat sensitivity rankings as proof of net-electric performance.

## Shared contract

- Versioned architecture, geometry, power balance, cost year/currency, lifetime and financing assumptions.
- Subsystem quantities linked to their source physics/design model and evidence class.
- Declared COA with fail-closed missing-account handling.
- Separate cost sensitivity, uncertainty, net-electric output, capacity factor and lifecycle-cost outputs.
- Independent subsystem cross-check and held-out scenario before model promotion.
- No double-counted credits, no silent zero assumptions and no conversion of model output to commercial evidence.

## A–H integration edges

| Lane | Handoff |
|---|---|
| A | Any algorithmic optimizer must be compared with classical optimization on the same architecture, objective, uncertainty and budget. |
| B | No cloud/provider/QPU job is needed; provider-neutral interfaces remain dry-run only. |
| C | Keep model input/output bytes and state materialization separate from physical storage claims. |
| D | Define device/material specifications, lifetime, irradiation damage and manufacturability. |
| E | Own the plant physics, materials, cooling and net-electric boundary. |
| F | Own COA reconciliation, uncertainty, CAPEX/OPEX, financing and lifecycle cost per net MWh. |
| G | Supply process/tooling/yield/inspection evidence for dominant components in continuous D/G co-design. |
| H | Use the cost-of-information and time-to-evidence gate before committing irreversible capital. |

## Invariants and non-claims

- INV-032: no reliable net-electric fusion or commercial low-cost plant is demonstrated.
- INV-033: no project WACC/risk-premium reduction is demonstrated; principal and capital lock-up remain separate measurable channels.
- INV-030/031: no Pangola critical-material substitution or saleable bio-oil result follows.
- INV-034/035: model fitting and sensitivity do not change physical laws; all hypotheses remain subject to constraints, falsification and independent validation.
- INV-029: no Data-Center-to-One-Phone physical-compression evidence follows.

## Next gate

Implement FUS-001-COA-ADAPTER-001 for one explicitly bounded architecture, validate account completeness, run uncertainty/sensitivity and independent subsystem checks, then add net-electric and lifecycle terms before any LCOE conclusion. Keep the adapter MODEL_ONLY until the required engineering evidence exists.
