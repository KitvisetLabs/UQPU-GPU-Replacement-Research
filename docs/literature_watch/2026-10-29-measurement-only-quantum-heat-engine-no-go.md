# Literature watch — steady-regime no-go for measurement-only quantum heat engines

**Date reviewed:** 2026-10-29  
**Source accepted:** 2026-10-26  
**Evidence class:** PUBLISHER-HOSTED ACCEPTED PAPER / THEOREM CLAIM / UQPU REPRODUCTION NOT RUN  
**Primary owner:** Lane H — literature provenance  
**Cross-lane owners:** Lane A formal-model tooling; Lane E energy/infrastructure; Lane F evidence and energy accounting  
**Related:** INV-034/035, FND-001, FND-004, FUS-001

## Source and stated scope

Kenta Koshihara and Kazuya Yuasa, “No-go theorem for quantum heat engines powered purely by quantum measurements in the steady regime,” Physical Review A, accepted 2026-10-26: https://journals.aps.org/pra/accepted/10.1103/4kmf-nzsm (DOI: 10.1103/4kmf-nzsm).

The publisher's accepted-paper summary states a no-go result for a finite-dimensional working substance driven by bare quantum measurements, with no feedback control and no thermal contact in the cycle. Using a Poincaré-like recurrence theorem for general quantum channels, the authors argue that in the steady regime the measurements become nondisturbing and do not inject energy into the working substance, so steady-cycle work extraction is unavailable under those assumptions.

## Genuine relevance and limitations

This is a potentially useful negative constraint for FND-001 thermodynamic-gap accounting and FND-004 alternative physical primitives: a proposal cannot count measurement backaction as a free, indefinitely reusable energy source while omitting the measurement/control boundary.

The result is not a no-go theorem for all quantum computing, all measurement-assisted control, or all heat engines. Its stated assumptions exclude feedback and thermal contact and restrict the working substance to finite dimension in the steady regime. A route that changes those assumptions must explicitly account for the resources introduced; it may not simply cite the paper as either universally decisive or irrelevant.

The UQPU project has not independently checked the proof, reconstructed the theorem's full assumptions from the manuscript, or run a physical experiment. No new physical law or measured energy result is claimed.

## Exact project consequences

- **FND-001:** retain measurement, control, feedback, memory, reset, heat exchange and extracted work as distinct terms in the thermodynamic boundary.
- **FND-004:** require alternative primitive proposals to name the changed assumption and the measurable consequence; bare measurement-only steady-cycle extraction is not an accepted free-energy mechanism.
- **FUS-001 / INV-032:** this theorem does not establish a fusion-plant cost result. It reinforces that any proposed measurement/control subsystem must include its energy and thermal boundary if it is later integrated into a plant model.
- **INV-033:** no financing or interest-rate conclusion follows from this paper.
- **INV-035:** mathematical proof review and physical/engineering validity remain separate evidence gates.

## Falsifiable follow-up

1. Pin the accepted manuscript, source version, theorem statement, assumptions and any available proof artifacts.
2. Independently formalize the finite-dimensional channel and steady-regime assumptions; check whether the recurrence argument covers the intended channel class.
3. Construct small finite-dimensional examples satisfying the assumptions and verify that repeated bare measurements do not yield positive net steady-cycle work under the paper's definitions.
4. Test altered cases with explicit feedback or thermal contact as separate models, including controller work, memory updates/reset, measurement apparatus and heat flows.
5. If any physical implementation is proposed, measure all input work and heat flows over a complete cycle and define a falsifier before interpreting the result as an energy advantage.

**Disposition:** relevant theorem lead / negative-evidence candidate for FND-001 and FND-004; independent reproduction OPEN. It does not demonstrate quantum advantage, cheaper fusion electricity, a new physical law, or any UQPU mission milestone.
