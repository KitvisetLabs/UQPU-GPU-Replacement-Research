# UQCS Cloud-vs-Owned Crossover and Sensitivity

## Goal

Avoid making a deployment decision from one guessed CAPEX/utilization/runtime number.

The economic engine now treats cloud-vs-owned choice as a **crossover problem under uncertainty**.

## Current pricing verification

The September 2026 pricing snapshot was rechecked against official sources:

- IBM Quantum Pay-As-You-Go starts at USD 96/minute, Flex at USD 72/minute, Premium at USD 48/minute.
- Amazon Braket on-demand QPUs use a per-task + per-shot model; current listed QPUs include AQT IBEX-Q1, IonQ Forte, IQM Emerald/Garnet, QuEra Aquila and Rigetti Cepheus. Braket also publishes hourly reservation rates.
- Azure Quantum documents provider-controlled pricing and warns that prices can change; its published models include IonQ token/gate-shot pricing, Pasqal QPU-hour pricing and Rigetti execution-time-increment pricing.

Primary sources:
- https://www.ibm.com/quantum/products
- https://quantum.cloud.ibm.com/docs/en/guides/plans-overview
- https://aws.amazon.com/braket/pricing/
- https://learn.microsoft.com/en-us/azure/quantum/pricing

## New solver

`uqpu.economic_sensitivity` provides:

- owned-hardware utilization sweeps;
- CAPEX sweeps;
- route-transition detection;
- explicit dated FX conversion with provenance;
- cost uncertainty envelopes;
- robust/uncertain deployment classification.

## Robust decision rule

Instead of asking only whether:

[
C_{cloud} < C_{owned}
]

the integration layer can compare uncertainty intervals:

- `ROBUST_CLOUD` if even the high cloud estimate is below the low owned estimate;
- `ROBUST_OWNED` if even the high owned estimate is below the low cloud estimate;
- `UNCERTAIN_OVERLAP` otherwise.

This prevents a fragile MODEL_ONLY central estimate from being treated as a deployment conclusion.

## FX rule

Cross-currency comparisons require:

- source currency;
- target currency;
- conversion rate;
- as-of date;
- source/provenance.

The repository does not hard-code a permanent EUR/USD rate.

## Strategic interpretation

Near-term research may rationally prefer cloud even if long-term owned hardware is the mission. Cloud reduces irreversible CAPEX while workload, QEC, I/O and device architecture remain uncertain.

Owned hardware becomes strategically attractive only after enough workload volume/utilization and manufacturability evidence exist to move the crossover decisively.

## Evidence level

The solver logic is deterministic, current provider price anchors are official-source snapshots, but owned-UQCS scenarios remain MODEL_ONLY until a real prototype/fabrication deployment exists.
