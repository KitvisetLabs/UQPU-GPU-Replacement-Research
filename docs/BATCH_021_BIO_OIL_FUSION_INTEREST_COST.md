# Batch 021 — Bio-Oil, Fusion Electricity and Interest-Cost Compression

**Date:** 2026-09-10  
**Primary owners:** Lane E + Lane F + Lane H  
**Integration:** A–H  
**Evidence:** LITERATURE_REVIEW + MODEL_ONLY + TESTABLE_SOFTWARE  
**Commercial low-cost bio-oil demonstrated:** No  
**Commercial low-cost fusion electricity demonstrated:** No

## Why this batch exists

The Ketskaew Chulamani plan already contained biomass-to-bio-oil, energy development and fusion as parts of the long industrial ladder. This batch elevates three relationships to permanent, highly visible research pillars:

1. **INV-031:** make biomass-derived bio-oil/biofuel as inexpensive as defensibly possible;
2. **INV-032:** make future fusion electricity as inexpensive as defensibly possible;
3. **INV-033:** explicitly minimize the financing and interest burden of R&D/industrial development by reducing required principal, construction duration, operating cost and project risk.

These are integrated with the existing INV-029 Data-Center-to-One-Phone North Star and INV-030 Pangola/biomass-carbon critical-material strategy.

## Public evidence reviewed

### Biomass liquids

NREL techno-economic analysis of fast pyrolysis and upgrading shows that feedstock cost, fuel yield, hydrogen configuration and capital cost are important economic variables. An older NREL study reported materially different modeled fuel values as feedstock price and upgrading assumptions changed; those historical values are treated only as evidence of **sensitivity**, not as present Pangola costs.

NREL's later catalytic-fast-pyrolysis work reported improved carbon efficiency and lower calculated blendstock production cost from catalyst/reactor changes, despite use of an expensive catalyst. This supports a core optimization rule: optimize **total delivered fuel cost**, not the purchase price of one input.

NREL/PNNL public TEA model catalogs also include refinery co-processing pathways explicitly intended to test whether existing refinery infrastructure can reduce new biorefinery capital and production cost.

### Fusion

The U.S. DOE finalized a Fusion Science & Technology Roadmap in 2026 aimed at supporting fusion pilot plants and commercial-sector scale-up in the mid-2030s. This is roadmap evidence, not evidence of commercial cheap fusion electricity. DOE continues to state that major scientific and engineering challenges remain before fusion can reliably provide commercial electricity.

For a competitive reality check, IRENA's July 2026 *Renewable Power Generation Costs in 2025* reports global weighted-average LCOE around USD 33/MWh for new onshore wind and USD 44/MWh for solar PV. These are plant-level generation benchmarks rather than universal firm delivered-system costs, but they prevent the project from calling an expensive future fusion plant “cheap” merely because it produces net power.

### Financing / interest

IRENA identifies cost of capital as a major determinant of renewable-electricity cost. Its 2023 financing study gives an illustrative solar/wind result in which electricity cost increases about 80% when cost of capital is 10% rather than 2% under the report's assumptions.

IEA Cost of Capital Observatory work in Southeast Asia reports that financing conditions differ materially across markets and gives survey ranges around 6–8% nominal post-tax local-currency WACC for utility-scale solar projects in Thailand for 2024. This is context only; it is not a financing quote for this project, biomass plants or fusion.

## New executable model

Batch 021 adds `software/uqpu-prototype/uqpu/energy_finance.py` with standard-library-only functions for:

- capital recovery factor;
- levelized saleable bio-oil/liquid cost per liter;
- liquid-fuel energy normalization to cost/GJ;
- net-electric fusion LCOE-like cost per MWh;
- fixed-rate amortizing loan payment/total interest;
- direct interest savings from lower financed principal at unchanged financing terms.

The model deliberately does **not** infer that cheaper technology lowers the market interest rate. That requires a separately measured risk-premium/WACC mechanism.

## Research equations

### Bio-oil

```text
saleable liquid/year = dry feedstock/year × final saleable-liquid yield

cost/liter =
 (annualized CAPEX + feedstock + fixed O&M) / saleable liters
 + variable processing/upgrading cost
 - defensible coproduct credit
```

Future measured versions must separately include collection, preprocessing, hydrogen, catalysts, utilities, logistics, compliance, storage and product-quality losses where relevant.

### Fusion electricity

```text
net MWh/year = net MW × 8760 × capacity factor

cost/MWh =
 (annualized CAPEX + fixed O&M) / net MWh
 + variable O&M
 + fuel-cycle cost
 + component-replacement reserve
```

`net MW` must already subtract recirculating plant power. A gross-fusion-output number cannot be inserted into this denominator and presented as cheap electricity.

### Interest

For identical loan rate and tenor, amortizing-loan interest scales linearly with principal. Therefore reducing a required financed principal from P to kP directly reduces absolute interest to k times the original amount under unchanged terms.

This direct project-level relationship is distinct from any claim about a lower central-bank rate, sovereign yield or market WACC.

## Initial testable findings

The new unit tests verify the following mathematical properties:

- higher final saleable bio-oil yield lowers modeled unit cost when other inputs are fixed;
- fuel cost can be normalized by heating value rather than comparing unlike liters;
- lower fusion CAPEX lowers modeled electricity cost when net output and other assumptions are fixed;
- lower financing/discount rate lowers modeled cost for a capital-intensive fusion plant;
- lower debt principal lowers absolute total loan interest at unchanged rate/tenor;
- physically impossible capacity factor >1 is rejected.

These are model-consistency findings, not measured technology performance.

## Three highest-value experimental programs opened

### BIO-001 — Pangola-to-saleable-liquid mass/energy balance
Measure dry feedstock composition, moisture/ash, conversion yields, crude-liquid quality, stabilization/upgrading losses, hydrogen demand and final saleable energy yield. The first useful certificate is cost per GJ and cost per accepted fuel-equivalent function, not crude condensate mass.

### FUS-001 — Net-electric cost-driver envelope
For each serious fusion architecture, populate wide evidence-bounded ranges for net electric gain, recirculating power, capacity factor, CAPEX, construction time, component lifetime/replacement, remote maintenance and financing. Rank which variables dominate modeled electricity cost before selecting expensive experiments.

### FIN-001 — Interest burden per validated milestone
For each large R&D/factory program, record capital committed, debt principal, financing rate/tenor, time-to-evidence, total interest and evidence outcome. Optimize `interest paid per validated useful milestone` and preserve failed/high-cost experiments as negative evidence.

## Eight-lane integration

| Lane | Batch 021 role | Next gate |
|---|---|---|
| A | Keep compute/software Priority #1; expose energy cost as part of total accepted-task economics | couple workload energy demand to delivered-energy price |
| B | Cloud-QPU path remains active; provider power/cost evidence eventually enters total-system economics | measured provider energy/cost provenance where available |
| C | State/data movement determines electricity and infrastructure demand | quantify energy per accepted state/output movement |
| D | Fusion/component physics and low-cost device/material requirements | architecture-specific lifetime/heat/neutron/magnet requirements |
| E | Own bio-oil, fusion-energy, biomass/material and infrastructure research | BIO-001 + FUS-001 evidence tables |
| F | Own LCOE, fuel cost, financing, uncertainty and accepted-output economics | integrate energy_finance.py into evidence pipeline |
| G | Manufacturing cost/throughput/construction time strongly affects fusion and biorefinery CAPEX | manufacturing BOM/process/cycle-time models |
| H | Make cheap fuel, cheap electricity and low interest burden explicit capital-development pillars | FIN-001 stage-gated financing model |

## Evidence boundary

Nothing in this batch proves that Pangola bio-oil beats petroleum products, that fusion already produces commercial cheap electricity, that either technology will reach a particular THB/kWh or THB/liter target, or that cheaper energy will mechanically lower national policy interest rates.

The advance is that these goals are now permanent, visible, measurable and connected by explicit causal/economic contracts rather than being buried as secondary text.

## Public source anchors

- NREL fast-pyrolysis TEA: https://www.nrel.gov/docs/fy11osti/46586.pdf
- NREL catalytic fast pyrolysis: https://www.nrel.gov/manufacturing/news/program/2019/advancements-in-catalytic-fast-pyrolysis-give-biofuels-a-boost
- NREL Conversion TEA Models: https://bioenergymodels.nrel.gov/models/146/
- NREL/PNNL refinery co-processing models: https://bioenergymodels.nrel.gov/models/78/
- U.S. DOE Fusion Energy portal: https://www.energy.gov/fusion/fusion-energy
- U.S. DOE Office of Fusion / 2026 Roadmap: https://www.energy.gov/fusion/office-fusion
- IRENA Renewable Power Generation Costs in 2025: https://www.irena.org/Publications/2026/Jul/Renewable-Power-Generation-Costs-in-2025
- IRENA Cost of Financing for Renewable Power: https://www.irena.org/Publications/2023/May/The-cost-of-financing-for-renewable-power
- IEA Southeast Asia Cost of Capital Observatory update: https://www.iea.org/commentaries/high-cost-of-capital-and-limited-project-pipeline-hinder-clean-energy-investment-in-southeast-asia

**Status:** THREE PERMANENT PILLARS ELEVATED / EXECUTABLE ECONOMIC MODEL ADDED / PHYSICAL COST TARGETS NOT YET DEMONSTRATED.