# Literature watch — 2026-10-24: Gaussian quantum-repeater no-go theorem

**Accessed:** 2026-10-24  
**Primary owner:** Lane H — strategy, finance, future-industry research and publication  
**Feeds:** Lane B provider/network capabilities; Lane C photonic interconnect and data movement; Lane F system economics; FND-002/FND-004; EQN-005; INV-029/INV-034  
**Evidence class:** LITERATURE_ONLY — peer-reviewed Physical Review Letters theorem; official publisher abstract reviewed, full-text scope audit not yet completed  
**Project evidence promotion:** none

## Source and date

Rabsan Galib Ahmed and Graeme Smith, “No-Go Theorem for Gaussian Quantum Repeaters from Fractional Extendibility,” *Physical Review Letters* 137, 170804, published **2026-10-23**, DOI: https://doi.org/10.1103/5cyh-2mqf. Official publisher record: https://journals.aps.org/prl/abstract/10.1103/5cyh-2mqf. The article was received 2026-06-30, revised 2026-08-25 and accepted 2026-09-28.

The publisher abstract states that, for a pure-loss bosonic attenuation channel, a repeater chain using Gaussian operations, homodyne measurements and arbitrary classical communication cannot increase quantum or private capacity beyond direct transmission. It also reports that Gaussian local operations and classical communication among repeater nodes cannot enhance the two-way capacities. The proof introduces fractional extendibility for Gaussian states.

## Genuine delta for UQPU

This is a newly published, model-scoped **no-go theorem**, not a new physical law. Its practical value is to constrain architecture assumptions: a future photonic/distributed-QPU design must not count a Gaussian-only repeater layer as a capacity improvement over direct transmission for the channel and operation class covered by the theorem.

The relevant distinction is capacity-level communication theory versus a particular finite workload's throughput, latency, reliability, energy or price. Even a proven capacity no-go does not by itself provide a cost number for a deployed network; those system metrics still require a separate end-to-end contract.

## Scope limits and non-claims

- This watch reviewed the official publisher abstract, not the full article text; the exact theorem hypotheses and proof details require a full-text audit before implementation-specific use.
- The result is scoped to pure-loss attenuation channels and Gaussian repeater operations/measurements/classical communication as described by the source.
- It does **not** establish that all quantum repeaters fail, that photonic computing is impossible, or that non-Gaussian, memory-assisted, error-corrected or otherwise assumption-changing architectures can or cannot improve a specified workload.
- It does not revise thermodynamics, quantum mechanics or a physical law; it is a mathematical constraint under a stated model.
- No UQPU network, provider, device, photonic interconnect or real QPU was tested.

## Falsifiable follow-up — QNET-GAUSS-001

1. Obtain and review the full paper; freeze the exact pure-loss channel definition, capacity quantity, Gaussian-operation class, allowed classical communication and all theorem assumptions.
2. Encode a model-scoped architecture guard: a proposed design within those assumptions may not claim a capacity increase over direct transmission.
3. Build a small analytic/numerical reference comparing direct transmission with a Gaussian repeater under identical channel transmissivity and capacity definition. This is a consistency check of the model, not a replacement for the proof.
4. If a proposed architecture claims an advantage, require it to name the assumption that changes (for example, a non-Gaussian operation or a different channel/resource model), derive the distinct observable/capacity prediction, and compare under the changed model without silently mixing the two regimes.
5. For any system-level proposal, separately account for end-to-end accepted-task rate, latency, loss/retry, memory, classical control/data movement, energy and lifecycle cost.
6. Retain counterexamples, null results and failures. No provider call or hardware experiment is part of this literature follow-up.

**Falsifier of an architecture-level capacity claim:** under the theorem's stated assumptions, a claimed capacity improvement over direct transmission is inconsistent with the cited result unless a reviewed theorem premise or capacity definition differs. A different assumption requires its own explicit model and evidence path.

## A–H relevance

- **A — quantum programming/runtime:** no compiler change follows directly; any distributed-workload contract must specify the communication channel and accepted useful output.
- **B — cloud/QPU/provider integration:** provider-neutral architecture must distinguish ordinary connectivity from a proven capacity gain from a repeater.
- **C — memory/state/storage/data movement:** network capacity and quantum-state transmission are not equivalent to readable classical storage; count classical output and reconstruction separately.
- **D — device/chip/process/fabrication:** no photonic-device performance or fabrication result is established.
- **E — biomass/materials/energy/cooling:** no material, fuel, electricity or cooling measurement follows from this theorem.
- **F — economics/evidence:** a capacity bound is not a measured cost; any comparison must use matched service and resource boundaries.
- **G — manufacturing equipment/software/factory:** no process-window, yield or factory consequence is established.
- **H — strategy/publication:** record the theorem as a scoped constraint and keep alternative architectures tied to explicit changed assumptions.

## Foundational and permanent-mission boundary

- **FND-002:** capacity limits inform information-flow accounting, but do not replace application-visible output-information and reconstruction contracts.
- **FND-004:** no new physical primitive is established; the result constrains one operation/channel class.
- **EQN-005:** formal no-go results must be mapped to their exact premises before a technology claim is evaluated.
- **INV-029:** no Data-Center-to-One-Phone physical-compression result; network and external infrastructure still count inside the system boundary.
- **INV-030:** no Pangola material substitution or elemental transmutation claim.
- **INV-031:** no accepted bio-oil or fuel-cost result.
- **INV-032:** no net reliable delivered fusion-electricity result.
- **INV-033:** no financed-principal, interest or WACC effect.
- **INV-034/035:** the search remains open to alternative mathematical structures, but present physical constraints remain binding; any proposed escape must state the changed assumption and a discriminating prediction.

No new physical law, UQPU advantage or mission-level economic result is claimed.
