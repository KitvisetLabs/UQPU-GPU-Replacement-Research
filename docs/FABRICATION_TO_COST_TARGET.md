# Fabrication Cost -> UQCS Economic Target Bridge

## Purpose

Connect Lane D (devices/fabrication/packaging) directly to Lane F (economics/evidence/integration).

A fabrication flow is not economically useful merely because it can produce a device. It must fit inside the maximum manufacturing cost allowed by the end-to-end cost-per-useful-task target.

## Inverse relationship

Given a conventional baseline cost/task and a target advantage tier, the UQCS inverse solver produces a compute budget:

[
B_{compute/task}
]

A user-selected share of that budget is allocated to manufacturing amortization:

[
B_{mfg/task} = B_{compute/task} f_{mfg}
]

For a deployment with (N) devices per system and (L) useful lifetime tasks per device:

[
C_{device,max} =
rac{B_{mfg/task} L}{N}
]

After subtracting package/test cost:

[
C_{fab-good-die,max}
=
max(0, C_{device,max}-C_{package/test})
]

The actual modeled manufacturing cost/task is:

[
C_{mfg/task}
=
rac{(C_{fab-good-die}+C_{package/test})N}{L}
]

The design passes this budget gate only when:

[
C_{mfg/task} le B_{mfg/task}
]

## Implementation

`uqpu.fabrication_budget` now connects:

- `FabFlowResult.cost_per_good_die_usd`
- `SubsystemBudget.compute_budget`
- device count/system
- useful lifetime tasks/device
- package/test cost
- explicit manufacturing fraction of the compute budget

Outputs include:

- maximum manufacturing cost/device
- maximum permitted fab cost/good die
- actual modeled manufacturing cost/task
- budget headroom
- PASS/FAIL

## Important evidence boundary

The bridge equations are deterministic accounting, but most current fab-flow input values and deployment assumptions are still **MODEL_ONLY**.

A PASS result therefore means:

> The modeled assumptions fit the selected modeled inverse budget.

It does **not** mean that a real fabricated UQCS device has achieved the 100x target.

## Why the manufacturing fraction is explicit

The software deliberately does not hard-code a universal claim that fabrication should consume a particular percentage of compute budget.

Different architectures may allocate cost differently among:
- fabrication
- packaging/test
- QEC/control
- memory
- photonics
- power/cooling
- operations

The fraction must therefore be supplied by the architecture/economic scenario and included in sensitivity analysis.

## Design implications

When fabrication fails the budget gate, the project should test:

1. smaller die/device area;
2. higher yield;
3. fewer process steps;
4. cheaper lithography/process route;
5. chiplets/heterogeneous integration;
6. lower package/test cost;
7. fewer devices/system;
8. higher utilization/lifetime useful tasks;
9. architecture changes that relax feature/overlay requirements;
10. external foundry or alternate manufacturing routes.

Failure becomes a research gap, not a hidden assumption.
