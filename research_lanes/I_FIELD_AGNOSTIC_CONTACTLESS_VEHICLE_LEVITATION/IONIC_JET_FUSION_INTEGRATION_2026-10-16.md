# Lane I extension: Ionic Jet / EHD Propulsion + Fusion Energy Integration
Date: 2026-10-16 | Status: RESEARCH_PLAN / MODEL_ONLY
Canonical base: RESEARCH_PROGRAM_2026-10-16.md; main sync: integration/MAIN_COMMIT_SYNC_POLICY_2026-10-16.md; cross-lane: integration/PERMANENT_CROSS_LANE_CONTINUOUS_INTEGRATION_PROTOCOL_2026-10-16.md.

## Mission
Research whether ionic jet / electrohydrodynamic (EHD) propulsion and fusion-sourced electricity could contribute to quiet, efficient, high-thrust, **fully contactless** automobile and motorcycle lift, propulsion and stabilization. Keep this work **parallel** with I-001..007, all A–H, FND/EQN. Nothing here asserts feasibility of human-scale ionic lift or vehicle-mounted fusion.

## Distinguish physical mechanisms
- Atmospheric ionic wind/EHD: electrodes ionize air; electric fields accelerate charged particles, transferring momentum to neutral air. The reaction medium is atmosphere, **not Earth's magnetic field or gravity**. Account for thrust, voltage/current, ionization, corona loss, electrode erosion, ozone/NOx, acoustic noise and human exposure.
- Space ion thruster: expels propellant in vacuum with high exhaust velocity and usually low thrust. It is **not** a direct practical atmospheric hovering solution. Do not mix its specific impulse with EHD thrust-to-electric-power.
- Fusion electricity: distinguish an **offboard grid supplied by a fusion plant** from an **onboard fusion power source**. Grid fusion does not imply self-contained vehicle levitation; onboard fusion must include shielding, fuel, reactor, conversion, recirculating power, cooling, mass, reliability and regulatory requirements. Current onboard vehicle-scale fusion is a speculative target, not an available product.

## New parallel work packets
**I-008 EHD ionic jet thrust and lift** — Build reproducible measured-literature baseline and dimensional models of thrust-to-electrical-power N/W, thrust-to-mass N/kg, hover power W/kg gross mass, propulsive efficiency, thrust vectoring, electrode spacing, voltage, current, ambient pressure/humidity and stability. Compare with distributed electric rotors at identical payload, hover height, speed and noise distance. Start with passive models; any energized high-voltage experiment requires human safety review and approval.

**I-009 Fusion-to-propulsion energy chain** — Model fusion heat -> net delivered electricity -> grid/transmission or onboard power conditioning -> EHD power electronics -> thrust -> accepted passenger-km. Account for fusion recirculation, conversion losses, storage, cooling, mass, downtime, lifecycle cost and finance. Reuse FUS-001 net-electric envelope from Lane E/F. Never substitute gross reactor power for net delivered energy.

**I-010 Hybrid contactless vehicle architecture** — Compare EHD-only, rotor-only, EHD+rotor, superconducting guideway+EHD, and offboard fusion electricity + battery + EHD/rotor. Evaluate controllability, lift stability, redundancy, terrain clearance, passenger exposure, acoustic signatures, range, weather sensitivity, mass and cost. No-contact is required; guideway-only systems must be explicitly scoped, not sold as arbitrary-terrain.

**I-011 Physics/frontier alternative** — If hypothesizing magnetic-gravitational coupling or radically new EHD enhancement, apply INV-035 incumbent-model, dimensional/symmetry/conservation, falsifier, held-out prediction and independent-replication requirements before any performance claim.

## Acceptance gates
G0: traceable primary sources and equations, realistic mass and electrical-power budget, no double-counting.
G1: matched-baseline simulations and uncertainty sweeps across ambient conditions.
G2: independently replicated calibrated low-energy EHD thrust evidence and byproduct/exposure checks (subject to approval).
G3: demonstrable safe unmanned hover and stable thrust control, with energy/noise benchmarks.
G4: net fusion electricity and propulsion chain demonstrated separately, with lifecycle and finance accounting.
G5: combined system independently validated against baseline per **accepted useful passenger-km**, including all external infrastructure.
No gate is passed by publishing this plan.

## Agent-ready execution and integration interfaces
Every AI agent reads AGENTS.md and newest main, then creates lane-owned dated artifacts. Publish machine-readable interface:
`{work_id, source_sha, hypothesis, evidence_class, vehicle_mass_kg, payload_kg, lift_N, thrust_N, electric_input_W, fusion_net_delivered_W, conversion_losses_W, range_km, Wh_per_passenger_km, noise_dBA_at_m, ozone_NOx_exposure, uncertainty, baseline_id, blockers, next_test}`.
Leave unmeasured fields null. Primary cross-lane links: A (control/optimization), C (power/data/thermal), D/G (electrodes, power electronics and manufacturability), E (fusion/cooling/materials), F (net energy/economics), H (funding), FND/EQN (falsifiable models). After every source commit, update the main sync record according to the policy, including pending branch work and CI status. No high-voltage prototype, plasma reactor, human test, procurement or paid compute without explicit authorization.
