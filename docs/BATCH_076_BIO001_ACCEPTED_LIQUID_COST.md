# Batch 076 — BIO-001 accepted-liquid cost and upgrading boundary

**Date:** 2026-10-27  
**Starting main SHA:** bc6140d667168d4d210961bea5c9122777b0c744  
**Primary owner:** Lane E — biomass/materials/energy/infrastructure  
**Evidence/integration owner:** Lane F  
**Publication/strategy owner:** Lane H  
**Evidence class:** MODEL_ONLY contract implementation + peer-reviewed literature; no Pangola reproduction

## Research question

Can UQPU prevent crude bio-oil yield from being misreported as accepted-fuel economics by binding batch mass, product acceptance, upgrading inputs, plant capital recovery, R&D lock-up interest and non-overlapping coproduct credits into one fail-closed cost contract?

## Implementation

The shared energy-finance module now contains a batch-level accepted-liquid calculator and focused tests. Accepted energy is accepted liquid mass times the declared lower heating value only when the frozen acceptance gate passes. Cost is reported per accepted MJ/GJ and per litre only when density is available. Inputs include moisture/dry-feed basis, feedstock/preprocessing/logistics, hydrogen, catalyst, utilities, other OPEX, annualized CAPEX, capacity factor/lifetime, separate R&D principal-lockup interest and disjoint net coproduct credits. Rejected batches cannot report accepted-fuel cost; outputs are always MODEL_ONLY.

## Literature delta

The HTL upgrading review and wheat-straw hydrotreatment batch study show why upgrading and acceptance cannot be omitted from the cost boundary. They do not provide Pangola-specific yield, closed energy balance or commercial minimum selling price.

## A–H and cross-cutting status

A–C remain provider-neutral/software-first; no quantum workload, cloud job or memory-equivalence claim is added. D/G have no device/manufacturing result. E receives the cost-contract implementation but still lacks Pangola batch data. F receives explicit cost and finance boundaries. H receives the dated watch and strategic linkage. FND-001–005 remain at prior evidence levels; FND-006 advances at accounting-method level only. EQN-001–006 remain evidence-gated.

INV-029 remains an unmet physical-compression mission. INV-030 receives no material substitution. INV-031 remains not demonstrated at target cost. INV-032 has no net-electricity result. INV-033 gains a model for separate principal-lockup interest only; no lower WACC/risk premium is claimed. INV-034/035 remain upstream research principles. INV-025/026/027 and all 100,000,000-unit goals remain falsifiable targets. Root directives 00, 00A and 01–06 and all multilingual master-plan references remain preserved.

## Next gate

Freeze one Pangola/residue lot and acceptance specification, measure all mass/energy/output streams and upgrading inputs, close ledgers within a preregistered tolerance, and independently repeat the batch. Only then may cost per accepted MJ be estimated from project data. Do not label MODEL_ONLY output as commercial evidence.
