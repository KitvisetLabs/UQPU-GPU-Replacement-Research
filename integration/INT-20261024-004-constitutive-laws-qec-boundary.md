# INT-20261024-004 — constitutive-law discovery and continuous-QEC scope

**Date:** 2026-10-24  
**Primary owner:** Lane H — research synthesis and publication  
**Cross-lane owners:** A/B (runtime/provider capability), D/G (device/process co-design), E (materials/energy), F (evidence/economics)  
**Source main SHA:** `c7b5958af58fad04a101ef5c6abf6a29293c867e`  
**Source branch:** `research/2026-10-24-equation-discovery-audit-v2`  
**Work IDs:** `CONSTITUTIVE-LAW-001`, `QEC-MEAS-001`  
**Status:** PROPOSED  
**Evidence class:** `LITERATURE_ONLY`; no project evidence promotion

## Hypotheses

1. Graph-based and physics-informed symbolic regression can be evaluated as candidate generators for model-specific constitutive equations when data provenance, constraints, identifiability and held-out regimes are frozen.
2. Runtime/provider capability contracts should distinguish mid-circuit measurement/reset/conditional operations from continuous syndrome-measurement/QEC requirements.
3. These methods and limitations can improve research design, but do not themselves establish a new fundamental law, UQPU performance, material substitution or economic advantage.

## Source artifacts and assumptions

- Lane-H literature article: `research_lanes/H_strategy_finance_future_industries/LITERATURE_WATCH_2026-10-24_CONSTITUTIVE_LAWS_AND_QEC.md`
- GraphED: Xu et al., *Science Advances*, DOI 10.1126/sciadv.aec0989, studied steel/lithium/rubber datasets.
- Physics-informed symbolic regression: Lazebnik et al., *Machine Learning: Science and Technology*, DOI 10.1088/2632-2153/ae9c8b, studied spheres crossing water–salt/water–glycerol interfaces.
- Continuous QEC: Halaski & Koch, *Physical Review Applied* 26, 034074 (2026), DOI 10.1103/8bkm-b48b; conclusions remain model/protocol scoped.
- Related lower-bound preprint arXiv:2608.26272 is already described in pending PR #50; it is not treated as merged.

## Interface and acceptance gates

**Constitutive-law route:** freeze source data/splits, model domain, units, baseline model, candidate complexity budget and held-out regimes. Require residual/counterexample analysis, parameter identifiability and independent replay. Report failed regimes and uncertainty. A fit or compact formula alone cannot pass.

**Continuous-QEC route:** record exact protocol, interaction terms, measurement model, noise assumptions, logical/error subspaces, readout/decoder, target-specific capability evidence and predicted observable. Do not infer continuous QEC from mid-circuit measurement support. Any alternative primitive must change a named assumption and predict a discriminating observable.

## Falsifiers

- Reject a constitutive candidate if the published result cannot be reproduced, units/limits fail, held-out performance does not beat the frozen baseline, or independent data contradict the relation.
- Reject a claimed continuous-QEC capability if the declared target cannot implement the required interaction/measurement sequence or if independent simulation/experiment reproduces logical corruption under the same assumptions.
- Reject any cross-lane economic claim if candidate generation, fitting, failed runs, decoding, transfer, independent replication or system-level costs are omitted.

## Cross-lane consequence

A/B receive a capability-schema requirement; C/F receive readout/decoder/resource accounting requirements; D/G receive a future measurable interaction/process gate; E receives a candidate method only, not Pangola-specific evidence; H retains the source and strategic mapping. No lane is granted a technology conclusion from literature alone.

## Current result and next gate

The article and this integration record are literature-only. No paper was independently reproduced in this cycle; no QPU, physical instrument, material or fuel test was run. Next, reproduce GraphED or PISR on the source dataset with frozen splits and a baseline, while separately keeping QEC capability as a model-scoped requirement. Continue to require exact-head CI and keep the main-branch synchronization status explicit.
