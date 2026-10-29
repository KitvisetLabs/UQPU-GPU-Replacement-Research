# Research gap RG-FND001-MEASUREMENT-ONLY-HEAT-ENGINE-001 — theorem assumptions and energy-boundary reproduction

**Opened:** 2026-10-29  
**Primary owner:** Lane E — energy/thermodynamic model interface  
**Cross-lane owners:** Lane H literature provenance; Lane A formal model; Lane F energy/evidence accounting  
**Status:** SOURCE WATCHED / INDEPENDENT THEOREM RECONSTRUCTION NOT RUN  
**Source:** https://journals.aps.org/pra/accepted/10.1103/4kmf-nzsm  
**Related:** INV-034/035, FND-001, FND-004, FUS-001

## Objective

Determine exactly which finite-dimensional, steady-regime, bare-measurement assumptions support the accepted paper's no-go theorem for measurement-only quantum heat engines, and prevent project models from treating measurement backaction as a free net-work source.

## Current evidence

The APS accepted-paper page dated 2026-10-26 summarizes a Poincaré-like recurrence argument for general quantum channels. Under the stated setup—finite-dimensional working substance, bare quantum measurements, no feedback control or thermal contact, steady regime—the authors report that measurements become nondisturbing and do not inject energy, precluding work extraction in that regime.

This is a publisher-hosted accepted-paper summary, not an independent UQPU proof reconstruction. The full theorem assumptions, proof details and operational definitions must be checked before reuse.

## Required unlock criteria

1. Pin and read the accepted manuscript and exact theorem statement; preserve version and source hashes.
2. Formalize the channel, steady-state, measurement and work definitions and list all assumptions.
3. Independently verify the recurrence/no-go argument or construct a proof-checkable reduction.
4. Reproduce a finite-dimensional toy example within the theorem's scope.
5. Model feedback, thermal contact, controller work, measurement apparatus, memory/reset and heat flows as distinct changed-assumption cases.
6. For any physical test, preregister the complete-cycle energy balance and a discriminating observable.

## Non-claims

This does not rule out all quantum computing, feedback-controlled systems or heat engines with thermal contact. It is not a fusion-economic result, a measurement of device energy, or a new UQPU physical law. FUS-001 and FIN-001 remain open.
