# UQCS Research Operating System — Parallel Simple Mode

## One mission
All work serves one measurable mission: maximize useful-computing functional coverage while pursuing provider portability and >=100x lower total cost/useful-task; 100,000,000x remains a workload-specific moonshot, never a guaranteed claim.

The permanent Kanusanan Pongpanna Model and multilingual references remain strategic context for every cycle.

## Operating principle: many lanes, one scoreboard
Do not run the project as dozens of unrelated projects. Run **6 parallel lanes** that share one input contract, one result contract, one priority queue and one integration gate.

### Lane A — Workloads & software
Owns GPU/CPU workload contracts, Semantic IR, compiler/runtime, algorithms, benchmarks and output correctness.

### Lane B — Quantum & cloud
Owns QPU modalities, QEC, logical/physical resources, provider adapters, provider surveillance and real/simulated execution evidence.

### Lane C — Memory, photonics & interconnect
Owns VRAM/HBM/RAM/storage replacement or avoidance, photonics, networking, chiplet/interconnect bandwidth and data-movement reduction.

### Lane D — Devices, fabrication & packaging
Owns quantum/photonic/semiconductor devices, lithography, complete fab flow, yield, packaging, reliability and manufacturability.

### Lane E — Biomass, materials, energy & infrastructure
Owns Pangola/agricultural-residue feedstocks, functional material substitution/minimization/recovery, power, cooling and data-center infrastructure.

### Lane F — Economics, evidence & integration
Owns GPU/full-stack baselines, inverse cost budgets, financing/commercialization context, evidence labels, research gaps, cross-lane dependency resolution and release gating.

## Single work-item contract
Every task in every lane uses exactly this compact record:

- **ID / lane**
- **Objective / workload or component**
- **Input requirement**
- **Output / acceptance metric**
- **Evidence level**
- **Cost impact / target budget**
- **Dependencies**
- **Status:** READY | ACTIVE | BLOCKED | DONE | REJECTED_CURRENT_ASSUMPTIONS
- **Blocker + unlock criterion** if blocked
- **Next experiment/action**
- **Artifact:** code/model/doc/data/test

No work item may disappear because it failed. BLOCKED/REJECTED_CURRENT_ASSUMPTIONS items move to RESEARCH_GAPS.md with an unlock path.

## Parallel execution cycle

```text
                 MASTER MISSION + MASTER STRATEGY
                            |
                    PRIORITY / SCOREBOARD
                            |
       +---------+----------+----------+----------+----------+
       |         |          |          |          |          |
       A         B          C          D          E          F
   Software   Quantum    Memory     Fab/Pack   Materials  Economics/
  Workloads    Cloud    Photonics              Energy    Integration
       |         |          |          |          |          |
       +---------+----------+----------+----------+----------+
                            |
                     INTEGRATION GATE
                            |
                 TEST -> EVIDENCE -> COST
                            |
             MERGE / GAP / NEXT PRIORITY
                            |
                       GITHUB SYNC
```

When independent agents are available, assign one or more lanes to agents concurrently. When they are unavailable, execute the same six-lane batch sequentially without changing the contracts. Never claim parallel execution when it did not occur.

## Priority score
Lane F ranks candidate work before each cycle. Prefer the item with the highest expected mission impact:

```text
Priority ~= (functional-coverage gain
           + expected cost-reduction leverage
           + blocker/uncertainty reduction
           + cross-lane enabling value)
           / estimated effort
```

Do not pretend this heuristic is a measured scientific quantity. It is a project-management rule.

### P0 — integration blockers
Anything preventing a complete workload path, test, evidence classification or cost calculation.

### P1 — economic bottlenecks
Largest contributors preventing >=100x cost/task.

### P2 — functional-coverage gaps
GPU/CPU/memory/storage functions without an accepted path.

### P3 — enabling research
Fabrication, materials, photonics, provider or infrastructure work that unlocks P0-P2.

### P4 — speculative exploration
Long-horizon ideas that do not yet unblock the measurable core mission.

## Integration gate — only five questions
Before accepting a result, answer:

1. **Function:** does it satisfy a defined workload/component contract?
2. **Evidence:** what is actually demonstrated versus MODEL_ONLY/SIMULATION/ROADMAP?
3. **System:** are memory/I/O, control/QEC, fabrication/package and power/cooling dependencies represented where applicable?
4. **Economics:** what does it do to total cost/useful-task and the >=100x budget?
5. **Reproducibility:** is there an artifact/test/source sufficient for another contributor to inspect or reproduce it?

If any required answer is missing, the result is not integrated; it becomes ACTIVE or BLOCKED.

## Minimal daily batch
A productive daily cycle does not require touching every lane equally.

1. Verify master strategy/invariants and inspect GitHub/CI.
2. Refresh only time-sensitive evidence that affects active tasks (especially quantum-cloud/provider changes).
3. Select **1-3 P0/P1 tasks** plus at most one enabling task per relevant lane.
4. Work lanes independently against the shared contract.
5. Integrate once at the end of the batch instead of repeatedly cross-checking after every tiny edit.
6. Run tests/evidence checks/cost accounting.
7. Record negative results and unlock paths.
8. Update WORKLOG/DECISIONS only for meaningful changes.
9. Preserve master-plan references and sync GitHub.

## Weekly integration review
Once per week, or after a major architectural result:
- recompute the end-to-end workload coverage map;
- recompute the full-stack cost bottleneck ranking;
- reconcile lane dependencies;
- retire duplicated tasks;
- promote/demote priorities;
- review RESEARCH_GAPS unlock triggers;
- review provider/fabrication/material evidence freshness;
- select the next week's top P0/P1 targets.

## Shared scoreboard
Track only the metrics that decide whether the project is moving:

1. **Functional coverage:** accepted workload contracts / target workload contracts.
2. **Evidence maturity:** fraction at PROTOTYPE/PUBLISHED_EXPERIMENT/PRODUCTION_DATA versus MODEL_ONLY.
3. **Economic ratio:** GPU/full-stack cost per useful task divided by UQCS cost per useful task, with uncertainty.
4. **Cloud portability:** providers/adapters at each CLOUD validation level.
5. **Data movement:** bytes/materializations avoided versus baseline where meaningful.
6. **Manufacturing:** modeled/measured cost per good die/device/package and yield.
7. **Blockers:** open P0/P1 gaps and time-to-unlock evidence.
8. **Reproducibility:** tests/benchmarks passing and artifacts available.

## Anti-complexity rules
- One canonical document per concept; other files link to it rather than duplicate it.
- One canonical task/gap ID; never maintain competing copies.
- One integration review per batch.
- Prefer machine-readable data for provider/cost/coverage matrices.
- Separate current evidence from roadmap/speculation.
- Do not optimize a subsystem without showing its end-to-end impact.
- Do not run paid QPU jobs silently.
- Do not physically attempt hazardous fab processes outside proper professional facilities.
- Preserve negative results.
- Preserve the permanent strategic master plan and multilingual links.

## Definition of a completed cycle
A cycle is complete only when:
- selected tasks have DONE/BLOCKED outcomes;
- tests/checks were run where applicable;
- evidence labels are explicit;
- cost/system impact is recorded;
- blockers have unlock criteria;
- master strategy/invariants remain intact;
- WORKLOG captures meaningful progress;
- GitHub is synchronized.

This operating system replaces ad-hoc expansion with coordinated parallel research: **six lanes, one contract, one scoreboard, one integration gate, one mission.**
