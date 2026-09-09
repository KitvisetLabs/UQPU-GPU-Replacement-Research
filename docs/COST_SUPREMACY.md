# Cost Supremacy Objective

## Mission

Beyond functional GPU replacement, UQPU targets **100× lower total cost per completed useful workload** as the minimum economic-success threshold, with a moonshot target extending to **100,000,000×** on workloads where quantum structure permits it.

This is a falsifiable research target, not a guaranteed claim.

## Cost tiers

| Tier | Reduction vs GPU | Meaning |
|---|---:|---|
| C1 | 100× | Minimum target |
| C2 | 1,000× | Strong advantage |
| C3 | 10,000× | Transformative advantage |
| C4 | 100,000× | Extreme advantage |
| C5 | 1,000,000× | Million-fold advantage |
| C6 | 10,000,000× | Ultra-advantage |
| C7 | 100,000,000× | Moonshot target |

## Metric

[
C_{task} =
rac{
C_{capex,amortized}+C_{energy}+C_{cooling}+C_{control}+C_{QEC}
+C_{memory}+C_{network}+C_{maintenance}+C_{software}
}{
N_{accepted tasks}
}
]

[
A_C = rac{C_{GPU/task}}{C_{UQPU/task}}
]

Minimum economic success:

[
A_C ge 100
]

Moonshot:

[
A_C ge 10^8
]

## Mandatory accounting

Include hardware amortization, cryogenics/optics, control electronics, QEC, host CPU, memory, networking, electricity, cooling, calibration, maintenance, state preparation, shots, measurement, decoding, output reconstruction, software overhead, and retry/failure rates.

## Possible multiplicative sources of advantage

[
A_C=A_{algorithm}A_{data}A_{hardware}A_{energy}A_{utilization}A_{lifetime}
]

The 10^8× target is expected to require multiple stacked advantages rather than a single optimization.

## Candidate domains for extreme advantage

- structured search
- amplitude-estimation-compatible Monte Carlo
- selected optimization problems
- quantum simulation
- sparse linear-algebra observables
- graph/combinatorial workloads with efficient oracles
- whole-program AI where large classical intermediates can be avoided

## Least plausible domains for extreme advantage

- raw framebuffer emission
- decoded raw video
- dense tensor materialization
- full sorting of classical records
- memory-copy dominated kernels
- simple arithmetic without a quantum shortcut

## Architecture strategy

1. Avoid instruction-by-instruction classical emulation except as fallback.
2. Use whole-graph semantic compilation.
3. Reuse prepared states and fuse operations.
4. Minimize measurement and shots.
5. Optimize QEC for cost per accepted result.
6. Select the cheapest viable quantum modality per workload.
7. Study reduced-cooling and room-temperature technologies long-term.
8. Design for manufacturability and modular replacement.
9. Maximize hardware utilization through batching and scheduling.

## Benchmark rule

Every benchmark must report both GPU and UQPU total cost/task, including all data movement and quantum overheads.

## Honesty rule

Never convert an asymptotic speedup directly into a cost-savings claim. State preparation, oracle construction, QEC, measurement and output can dominate.

## Ultimate target

- 100% functional GPU workload coverage
- ≥100× lower cost/task as the primary economic goal
- up to 100,000,000× lower cost/task on exceptional workloads where physically and algorithmically possible
