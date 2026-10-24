# Research Batch 057 — multi-oracle M-QSP boundary and physics-informed equation discovery

**Date:** 2026-10-25  
**Primary owner:** Lane A  
**Integration owner:** Lane F  
**Base main SHA:** `6af8ce896368ed993fe2b8278afa6082e1ecc916`  
**Status:** literature analysis and preregistered follow-up; not implementation evidence  
**Evidence label:** `LITERATURE_ONLY`

## Objective

Advance Lane A from the newest canonical Batch 056 state without confusing a static single-matrix QSVT numerical fixture with a multi-oracle algorithm. Add a typed preflight contract for the recently found M-QSP transfer-function paper, while cross-linking a peer-reviewed physics-informed symbolic-regression result to INV-035/FND-006.

Primary literature article: `docs/literature_watch/2026-10-25-mqsp-and-physics-informed-symbolic-regression.md`.

## Canonical control: Batch 056

Batch 056 remains the latest merged bounded QSVT matrix fixture found on main. Its result is a simulation of a 2×2 Hermitian contraction embedded in a 4×4 one-ancilla block encoding: degree 81, 81 signal queries, 82 phase rotations, one signal ancilla, zero provider jobs/shots, no native-gate decomposition, and energy/cost not measured. Its residual tests and phase perturbation negative control remain valid for that specific numerical contract.

This batch does not replace Batch 056, and the new multi-oracle paper is not required to validate the existing univariate fixture.

## New work contract: QOS-MQSP-001

**Purpose:** determine whether a small multi-oracle workload has a valid M-QSP transfer-function construction and whether its weighted oracle cost can be measured fairly against matched alternatives.

### Required frozen inputs

- Exact source/theorem and pinned implementation/dependency provenance.
- Oracle IDs, access model, block-encoding normalizations and per-oracle cost units.
- Matrix family, including noncommuting/nonnormal cases where covered by the source.
- Transfer-function/polynomial target, domain/promise, approximation metric and error tolerance.
- Input/state preparation, classical preprocessing, output reconstruction and accepted useful-output semantics.
- Classical reference, sequential/univariate control, held-out cases and counterexample set.
- Matched total resource budget: host time/compute, memory/I/O, query count by oracle, weighted query cost, retries, native-gate estimate and energy/cost where measurable.

### Fail-closed gates

1. **Source-scope gate:** the selected construction and all assumptions match the cited theorem.
2. **Feasibility gate:** no synthesis attempt is counted as successful unless the formal/algorithmic admissibility test passes.
3. **Numerical gate:** independent classical reference and held-out instances satisfy the preregistered error threshold.
4. **Counterexample gate:** degenerate, boundary, noncommuting and normalization perturbations are retained; any unexplained failure blocks promotion.
5. **Target gate:** provider-neutral lowering and target-aware resources are separate from mathematical feasibility.
6. **Economics gate:** compare same accepted useful output, with all per-oracle, input, host, readout, retry and reconstruction costs. Never combine a probability from one provider with another provider's price.
7. **Authorization gate:** simulator/dry-run first; no paid QPU execution without credentials, a bounded budget and explicit user consent.

### Falsifier

Reject or defer the M-QSP path if the theorem assumptions do not hold, the independent reference fails, held-out error exceeds tolerance, the oracle is unavailable under the declared interface, or weighted end-to-end cost per accepted task is not better than the matched control. Query-complexity improvement alone is not an end-to-end win.

## Equation-discovery cross-link: EQN-PISR-001

The September 8 peer-reviewed particle-interface study is retained as a method example only. Its delayed damped oscillatory force closure is specific to the reported fluid-interface experiments. A future transfer to material/energy modeling must freeze the incumbent, units, allowed operators, physical constraints, held-out conditions, resource budget and counterexamples before search. Independent material/energy data are mandatory.

## A–H lane status for this batch

| Lane | Reviewed advancement | Open gate |
|---|---|---|
| A | M-QSP multi-oracle contract separated from Batch 056 univariate control. | Implement QOS-QSVT-FEAS-001 first; then reproduce the full M-QSP source conditions before coding a solver. |
| B | Oracle identity/access/price is now explicit in the proposed contract. | No credentials or provider-matched run; no QPU jobs/shots. |
| C | State/input/output/reconstruction and data movement required in the resource ledger. | No readable-memory/storage equivalence; physical transfer not measured. |
| D | Native gate/depth/ancilla/control requirements remain downstream. | No target decomposition or device requirement yet. |
| E | Physics-constrained model-discovery method cross-linked. | No Pangola material, saleable bio-oil, net fusion-electricity or cooling evidence. |
| F | Weighted oracle costs and full accepted-task economics are specified. | No competitive end-to-end measured baseline; RG-028 remains data/credential blocked. |
| G | D/G co-design consumes only later validated device requirements. | No process window, yield or factory-cost evidence. |
| H | Literature publication and strategic context preserved. | No financing, principal, interest or WACC effect. |

## Foundational and invariant contribution

- **FND-001:** no wall-plug energy or irreversible-erasure measurement; no thermodynamic-gap result added.
- **FND-002:** explicitly preserve state-preparation/output-information accounting; no readable-memory inference.
- **FND-003:** no matched control-vs-quantum-speed-limit timing or energy experiment.
- **FND-004:** no alternative physical primitive validated by this literature.
- **FND-005:** no particle/QFT mechanism or credible anomaly established.
- **FND-006:** physics-informed symbolic regression is a candidate model-generation method; it must climb through held-out prediction, falsification, experiment and engineering.
- **EQN-001–006:** this batch proposes no new physical equation and promotes no AI-generated expression to a law.
- **INV-029:** physical Data-Center-to-One-Phone compression remains unproven; remote infrastructure and lifecycle costs cannot be hidden.
- **INV-030:** no elemental transmutation or critical-material substitution claim.
- **INV-031:** BIO-001 remains model/data limited; no accepted liquid-energy cost result.
- **INV-032:** FUS-001 remains model/data limited; no reliable net delivered electricity cost result.
- **INV-033:** FIN-001 remains unmeasured; no lower WACC or macro-rate claim.
- **INV-034/035:** strengthens the mathematics-first and equation-discovery gate while retaining established physics as binding for present engineering claims.
- **INV-025/026/027:** 100M targets remain falsifiable goals with subsystem-specific equivalent-useful-output contracts.

## Sync and CI notes

The main-branch `RESEARCH_GAPS.md` is a large living ledger and already contains RG-035 for autonomous handoff reconciliation. This batch does not overwrite that file or assign a new RG number without a canonical append-only sync. **Sync debt:** incorporate the QOS-MQSP-001 and EQN-PISR-001 blockers into the next safe `RESEARCH_GAPS.md` append/update, retaining existing RG IDs. Main SHA `6af8ce8` had no status entries and the connector returned no workflow runs for that SHA at audit time; that is **CI not observed**, not a pass or failure. Check exact-head PR CI before considering this batch integrated.

No paid provider job, material experiment, fuel production, fusion test or financial action was performed.
