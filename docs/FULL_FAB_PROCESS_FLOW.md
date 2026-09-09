# UQCS Full Fab Process-Flow Model

## Purpose

Move fabrication research beyond lithography-only analysis and model the complete wafer/device manufacturing chain.

## Verified process-chain basis

ASML's semiconductor-manufacturing overview identifies deposition, photoresist/lithography, etch, ionization and packaging as critical manufacturing steps. Applied Materials groups wafer fabrication around deposition, material removal/etch/CMP, ion implantation and thermal modification, metrology/inspection, and heterogeneous integration. Applied also notes that advanced chips can require hundreds of process steps. citeturn261559search8turn261559search1turn261559search36

Applied describes ALD/CVD/PVD/selective deposition as major routes for creating films, and describes dry/plasma etch, selective removal and CMP as central material-shaping operations. citeturn261559search13turn261559search7

ASML documents optical and e-beam metrology/inspection as part of yield control, with feedback to lithography and process control. citeturn261559search10

## Model implemented

`uqpu.fab_flow` represents a process as a sequence of steps with:

- cost/wafer
- step yield
- cycle time
- energy/wafer
- evidence level
- process category

The model calculates:

[
Y_{process}=prod_i y_i
]

[
GoodDies = GrossDies 	imes Y_{process} 	imes Y_{random-defect}
]

[
Cost/GoodDie = TotalProcessCost/Wafer div GoodDies
]

The random-defect term currently uses a simple Poisson approximation and is therefore MODEL_ONLY.

## Bottleneck analysis

`uqpu.fab_bottleneck` ranks steps by normalized contributions from:

- cost share
- yield loss
- cycle-time share
- energy share

This allows the research program to optimize the largest full-stack fabrication penalty rather than focusing only on lithography.

## Current generic flow

The first architecture-study flow includes:

1. deposition
2. lithography
3. etch
4. implant/doping
5. thermal activation
6. CMP
7. cleaning
8. metrology
9. inspection
10. wafer test/package allocation

All cost/yield/time/energy values in the reference flow are MODEL_ONLY placeholders.

## Research gaps

- real foundry process flows
- calibrated cost/wafer per step
- layer counts
- rework/scrap probabilities
- tool utilization and downtime
- queueing/WIP
- mask amortization
- chemical/gas consumption
- water and abatement
- facility power
- defect-density distributions
- packaging and test yield
- quantum/photonics-specific process modules
- biomass-derived material compatibility with purity/reliability requirements

## Strategic use

This model will connect directly to the UQCS inverse-cost budget. If a device cannot fit the fabrication budget needed for 100×, the system must either:

- use a cheaper fabrication route;
- relax feature requirements through architecture;
- reduce die area;
- improve yield;
- reduce process steps;
- use chiplets/heterogeneous integration;
- externalize fabrication;
- or classify the design as economically blocked under current assumptions.
