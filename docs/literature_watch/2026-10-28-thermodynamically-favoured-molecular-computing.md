# Literature watch — thermodynamically favoured molecular computation

**Watch date:** 2026-10-28  
**Primary source:** Stérin et al., “A thermodynamically favoured molecular computer,” *Nature* 657, 646–652 (version of record 2026-09-16).  
**DOI:** https://doi.org/10.1038/s41586-026-10996-5  
**Open full text:** https://pmc.ncbi.nlm.nih.gov/articles/PMC13581610/  
**Evidence:** peer-reviewed external experiment; **UQPU reproduction NOT RUN**.

## Novelty

The paper demonstrates a Scaffolded DNA Computer (SDC) whose designed molecular binding-energy landscape favours target configurations as the system relaxes. It reports ten programs and more than 700 computations, including parity detection and binary arithmetic. A large addition example counts two 25-bit inputs plus carry/output bits as 100 computed bits; small instances can run in under a minute, while larger instances require longer anneals.

This is a published alternative *physical implementation of computation*, not a UQPU result or a quantum-QPU result.

## Limits

- “Thermodynamically favoured” does **not** establish minimum wall-plug joules, low lifecycle cost, high throughput, general-purpose CPU/GPU replacement or a Landauer-limit approach.
- UQPU has not reproduced sequences, protocols, source data, fluorescence decoding, failures or uncertainty.
- Strand/scaffold inventory and concentration, preparation, labels/reporting, annealing/heating, fluorescence readout, operator/instrument time, failures, waste, reuse and output transfer must be counted.
- Scale-up involves strand number/length and heating/annealing; molecular equilibrium does not automatically transfer to quantum circuits, semiconductor fabrication, Pangola conversion or fusion.
- The authors disclose pending patents covering aspects of the core principles/reporting mechanism; future licensing diligence is required.

## UQPU relevance and falsifiable follow-up

FND-004/INV-034: a concrete alternative primitive for narrow tasks. FND-001/INV-035: measure energy per accepted output and use a Landauer floor only with a matched, declared irreversible-erasure count. Lane A: exact parity/arithmetic truth tables and an optimized CPU baseline. Lane C: count inputs, scaffold/strand inventory, reporting/readout, readable output, persistence and transfer. D/G: consider assembly/metrology/yield/automation only after reproducibility. Lane E: no Pangola, bio-oil or fusion evidence. F/H: all-in cost and capital lock-up per accepted output.

1. Pin article version, data, sequences/protocol, software, licenses and hashes.
2. Freeze one small program, truth table, decoder, acceptance threshold and CPU reference before tuning.
3. Retain failures, invalid outputs, missing reads and exclusions. Start with at least 30 independent preparations per program/control across three batches and a predeclared uncertainty method.
4. Test blind inputs, controls, concentration/temperature/anneal sensitivity, reuse and generalization.
5. Measure wall-plug energy, time, accepted-output rate, reagent/strand costs, instrument amortization, labour, waste and retries; compare identical outputs with an optimized CPU.
6. Preserve negative results if preparation/readout dominates, quality fails or generalization collapses.

**Promotion gate:** independent reproduction plus matched resource/economic measurements. No external result or ideal bound is promoted to UQPU advantage or new physical law.
