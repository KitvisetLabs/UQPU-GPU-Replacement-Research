# BIO-001 — component-resolved accepted-liquid cost ledger

**Date:** 2026-10-24  
**Primary owner:** Lane E — materials, energy and infrastructure  
**Consumers:** Lane F economics; Lane H finance; integration hub  
**Evidence class:** MODEL_ONLY + SYNTHETIC_UNIT_TESTS  
**Physical/commercial evidence promoted:** No

## Purpose

The existing aggregate bio-oil cost model is useful for sensitivity work but can hide omitted components when one variable-cost field is populated from incomplete estimates. This addition introduces a separate, explicit ledger for the final accepted liquid-energy function. It does not replace the existing API and must not be mixed with the aggregate model's variable-cost total.

## Functional unit and boundary

The denominator is one litre of final accepted, stabilized/upgraded liquid meeting a named product specification. Report its measured lower heating value (LHV) and accepted yield per dry tonne. Crude condensate is not the saleable-product denominator.

The ledger exposes:

- dry feedstock purchase;
- collection and transport to the process gate;
- preprocessing, including drying and size reduction where applicable;
- annualized CAPEX using an explicit discount rate and plant life;
- fixed operating and maintenance cost;
- conversion-only variable cost;
- upgrading and stabilization;
- hydrogen;
- catalysts;
- utilities;
- downstream logistics;
- compliance and storage;
- working-capital carrying cost per accepted litre;
- qualified coproduct credit, separately reported and subtracted once.

All monetary fields must use one currency and consistent price year. Do not enter the same cost in both conversion and a separately named component. The working-capital carrying-cost input is an explicit scenario or measured value; FIN-001 must separately retain principal, financing terms and capital lock-up duration.

## Accounting equations

Annual accepted liquid (L/year) = dry feedstock (dry t/year) × final accepted yield (L/dry t).

Per-litre contribution for each per-dry-tonne input = that input divided by accepted yield.

Annualized CAPEX per litre = CAPEX × capital-recovery factor(discount rate, plant life) / annual accepted litres.

Gross accepted-liquid cost per litre = annualized CAPEX + feedstock + collection/transport + preprocessing + fixed O&M, each normalized to accepted litres, plus conversion + upgrading + hydrogen + catalyst + utilities + logistics + compliance/storage + working-capital carrying cost.

Net accounting cost per litre = gross cost per litre − qualified coproduct credit per dry tonne / accepted yield.

Cost per GJ of LHV = cost per litre × 1000 / LHV in MJ/L.

The output retains gross cost and coproduct credit separately. If the credit exceeds gross cost, a negative net accounting cost is mathematically reported rather than clamped; it is not evidence that the liquid's energy is physically free. Credit eligibility, marketability, handling cost and allocation must be independently justified.

## Validation added

A standard-library unit-test fixture checks component reconciliation, per-dry-tonne normalization, energy-unit conversion, credit subtraction exactly once, and fail-closed behavior for zero yield, negative cost/credit and non-finite inputs. The fixture values are synthetic and must never be cited as Pangola measurements or commercial TEA.

## Missing evidence / next gate

BIO-001 remains blocked on a Pangola-specific, lot-traceable mass and energy balance. The next accepted dataset must identify feedstock lot, moisture, ash/composition, pretreatment energy, conversion conditions, liquid/char/gas yields, final liquid assay, LHV, accepted saleable yield, hydrogen/catalyst consumption, utilities, process losses, logistics, CAPEX/OPEX basis, price year and uncertainty. Coproduct credits require independent quality, quantity, market and allocation evidence.

Do not claim a lowest-cost route until competing routes are compared on the same accepted-liquid specification, functional unit, system boundary, financing assumptions and uncertainty treatment. Negative or failed yield/quality results remain part of the evidence record.

## Cross-lane interface

- Lane F receives the component ledger and cost-per-accepted-litre / cost-per-GJ outputs; all source inputs retain evidence labels and provenance.
- Lane H receives financed-principal and time-to-evidence fields through FIN-001; no lower WACC is inferred from lower modeled cost.
- Lane D/G receive future qualified carbon/material streams only after process yield, purity, contamination, component-function and manufacturing gates.
- INV-029 receives only measured contributions to energy, material, mass, volume and lifecycle-cost contracts; this model alone does not compress a data center into a phone.
