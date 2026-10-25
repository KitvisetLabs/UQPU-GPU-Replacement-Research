# Lane E — Fusion Electricity Cost Research Track

**Parent:** `03_FUSION_ELECTRICITY_COST_STRATEGY.md` / INV-032  
**Status:** ACTIVE LONG-HORIZON / COMMERCIAL_LOW_COST_NOT_DEMONSTRATED  
**Owners:** Lane E with D device physics, G manufacturing, F economics and H finance

## Primary measurable contract

Every candidate architecture must translate physics milestones into this system boundary:

```text
fusion core / driver
-> gross fusion power
-> thermal/direct conversion
-> minus recirculating plant power
-> net MWh delivered
-> availability / capacity factor
-> component replacement + maintenance
-> CAPEX + construction time + OPEX + fuel cycle + financing
-> lifecycle cost per net MWh
```

A high plasma gain or target gain is not equivalent to a low electricity cost.

## Architecture-neutral evidence table

| Parameter | Why it matters economically | Evidence class required for strong claim |
|---|---|---|
| net electric gain | determines saleable output after internal load | integrated experiment/pilot |
| capacity factor | spreads fixed capital across delivered MWh | long-duration operating evidence |
| CAPEX | often dominates capital-intensive plant economics | vendor/project BOM + construction evidence |
| construction time | drives interest during construction and schedule risk | project execution evidence |
| component lifetime | controls outage and replacement reserve | irradiation/thermal-cycle/component tests |
| fuel-cycle closure | affects availability/supply/safety | integrated fuel-cycle evidence |
| remote maintenance time | affects downtime and labor/robotics cost | maintainability demonstrations |
| WACC/financing | annualizes capital and risk | real financing terms / evidenced scenario |

## FUS-001 next experiment

Build wide, source-bounded parameter envelopes for tokamak, stellarator, inertial and pulsed/magneto-inertial families. Run sensitivity analysis with `uqpu.energy_finance.fusion_lcoe_per_mwh` to identify which uncertain parameter most changes modeled cost. The result remains MODEL_ONLY until populated with measured project/component evidence.

## Fresh operational/design evidence lead — 2026-10-25

The IAEA long-pulse meeting (20–23 October 2026) provides source-bound leads on EAST dynamic lithium wall conditioning (contribution 42923), EAST LH/EC current drive (42922), and CFEDR baseline design (42919). See docs/literature_watch/2026-10-25-iaea-long-pulse-fusion-net-electricity.md and gap RG-036.

Use the EAST 1066-second pulse and reported auxiliary RF inputs only as operating-envelope data. Do not equate pulse duration or plasma Q with plant net electric output. The CFEDR prediction of >500 MWe is an integrated-model projection with unresolved fuel/material/maintenance issues, not a measured plant result. FUS-LPO-001 must reconstruct the power balance and availability boundary before any cost propagation.

## Competitive rule

Compare against the best available generation/system option at the date of analysis. Do not freeze an old high-cost fossil baseline and declare victory later.