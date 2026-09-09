# Cloud QPU vs Owned UQCS Hardware Economics

## Purpose

Compare two deployment strategies using the same denominator: **cost per useful completed task**.

1. Rent quantum computation from a cloud provider.
2. Build/own UQCS hardware and amortize CAPEX over useful lifetime work.

## Official pricing anchors — September 2026

### IBM Quantum
IBM lists:
- Open Plan: free, limited monthly runtime;
- Pay-As-You-Go: starts at USD96/minute;
- Flex: starts at USD72/minute;
- Premium: starts at USD48/minute.

Source: https://www.ibm.com/quantum/products

### Amazon Braket
On-demand QPU pricing uses a USD0.30 per-task charge plus device-specific per-shot pricing. Current official pricing includes:
- Rigetti Cepheus: USD0.000425/shot
- IQM Garnet: USD0.00145/shot
- IQM Emerald: USD0.00160/shot
- QuEra Aquila: USD0.01000/shot
- AQT IBEX-Q1: USD0.02350/shot
- IonQ Forte: USD0.08000/shot

Source: https://aws.amazon.com/braket/pricing/

### Azure Quantum
Microsoft's provider pricing page lists provider-specific models including:
- IonQ gate-shot pricing with program minimums;
- Pasqal Fresnel: EUR3000/QPU-hour;
- Rigetti Cepheus: USD0.02 per 10 ms execution increment;
- Quantinuum usage/subscription pricing.

Microsoft explicitly warns that provider prices can change and users should verify the current workspace pricing before execution.

Source: https://learn.microsoft.com/en-us/azure/quantum/pricing

## Implementation

`uqpu.cloud_economics` supports:
- per-second
- per-task + per-shot
- per-gate-shot + minimum program price
- per-QPU-hour
- per-time-increment

`uqpu.cloud_pricing_snapshot` stores a dated official-source snapshot rather than pretending prices are permanent.

`uqpu.cloud_vs_owned` compares cloud cost/task to an owned-hardware model containing:
- CAPEX
- lifetime
- utilization
- power
- electricity
- maintenance

## Important boundaries

- Provider pricing changes over time.
- Azure and some providers add infrastructure/storage costs beyond headline QPU pricing.
- Currency differences are preserved; EUR and USD must not be numerically combined without an explicit exchange-rate conversion.
- Queue time is not automatically a billed runtime metric, but can affect useful throughput and economics.
- Real owned UQCS CAPEX is unknown today and remains MODEL_ONLY.
- Cloud pricing does not prove workload capability or output quality.

## Strategic interpretation

Cloud is likely to dominate early research because it avoids fabrication CAPEX and provides immediate access.

Owned hardware can become economically superior only when utilization, useful lifetime workload volume, maintenance, power and fabrication economics amortize below cloud price/task.

The crossover must be calculated per workload and architecture; it is not a universal constant.
