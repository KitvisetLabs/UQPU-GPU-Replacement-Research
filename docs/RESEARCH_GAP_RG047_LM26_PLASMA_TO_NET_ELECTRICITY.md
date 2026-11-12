# Research Gap RG-047 — LM26 plasma milestone to net delivered electricity

**Opened:** 2026-10-25  
**Primary owner:** Lane E — materials, energy, cooling and infrastructure  
**Integration owner:** Lane F — evidence and lifecycle economics  
**Co-design:** Lanes D/G — device, liner, diagnostics and manufacturing  
**Related invariants:** INV-032, INV-033; enabling context INV-029  
**Status:** LITERATURE_ONLY / DATA_BLOCKED_FOR_NET_ELECTRICITY

## Objective

Determine whether source-reported magnetized-target-fusion plasma milestones can be connected through a measured, repeatable energy and electrical boundary to positive reliable net delivered electricity and lifecycle cost per net MWh.

## Current evidence

The 2026-10-08 LM26 preprints report electron-temperature measurements of 1180 ± 65 eV from filtered X-ray diodes and 1090 ± 40 eV from Thomson scattering; ion temperature of 459 ± 33 eV is inferred from neutron yield. The UKAEA announcement describes this as a plasma-compression milestone and states that progress toward the Lawson criterion remains ahead. See `docs/literature_watch/2026-10-25-lm26-compressional-heating-to-net-electricity.md`.

These are source-reported external measurements, not UQPU measurements and not plant net-electricity evidence.

## Blockers

- No complete shot-level energy balance has been independently reconstructed here.
- Temperature and neutron diagnostics do not by themselves provide driver energy, recoverable pulse energy, fusion/thermal energy, conversion efficiency or grid-delivered electricity.
- No plant-boundary measurements of gross generation, recirculating loads, parasitic loads and grid-delivery losses are supplied by this watch.
- No repeated-pulse operating distribution, availability/capacity factor, component lifetime, maintenance/replacement interval or fuel-cycle closure is established.
- No verified CAPEX/OPEX, construction-time, financing, decommissioning or lifecycle cost per net MWh is established.

## Required evidence contract

Use `software/uqpu-prototype/uqpu/fusion_evidence.py` to classify only the completeness and internal consistency of a supplied electric-power record. The gate requires a stated meter boundary and averaging duration, and checks:

`net delivered electric power = gross electric power - recirculating power - other parasitic power - grid-delivery losses`.

The helper's `NET_ELECTRICITY_ACCOUNTING_CONSISTENT` class is not a reliability, safety, commercial or lifecycle-cost acceptance. Independent measurement provenance and repeated-operation evidence remain mandatory.

## Unlock criteria and falsifiers

1. Pin the primary paper versions, shot identifiers, diagnostics, calibration, uncertainty and available raw/supplementary data.
2. Reconstruct the plasma and energy diagnostics independently, keeping directly measured and inferred quantities separate.
3. Publish a source-bound driver/compression and energy-recovery balance with uncertainty.
4. Obtain a time-aligned electric meter record that includes gross generation, all recirculating/parasitic terms, grid losses, boundary and averaging interval.
5. Demonstrate repeatability and characterize pulse repetition, availability, outages, component replacement and fuel-cycle recovery.
6. Propagate the measured envelopes through architecture-neutral FUS-001 lifecycle economics, including CAPEX, construction time, cooling/conversion, maintenance, remote handling, financing and decommissioning.
7. Independently replicate critical measurements and preserve failed shots.

The net-electricity hypothesis is falsified for the tested configuration if the uncertainty-bounded delivered balance is non-positive, or if repeat operation and required auxiliary loads eliminate the apparent positive balance. No future-physics assumption can bypass these gates.
