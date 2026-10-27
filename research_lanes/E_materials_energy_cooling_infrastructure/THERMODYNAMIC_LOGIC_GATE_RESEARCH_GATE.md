# Lane E gate — thermodynamic logic computation with complete energy boundary

**Primary owner:** Lane E — energy/cooling/infrastructure research  
**Co-design:** Lane D devices and Lane G manufacturing equipment; Lane A workload contract; Lane F evidence/economics  
**Evidence status:** LITERATURE_ONLY; no UQPU model reproduction or physical test  
**Date:** 2026-10-28

## Source and candidate

Whitelam, “Evolutionary design of thermodynamic logic gates and their heat emission,” *Physical Review E* 114, 034135 (published 2026-09-21), https://doi.org/10.1103/9lv8-drtp. The publisher abstract reports simulation results. Treat it as an alternative-primitive lead, not a demonstrated hardware efficiency result.

## Experiment contract

Freeze the exact Boolean function/truth table, input distribution, output-error threshold, throughput or operation-time target, environmental temperature, initialization, reset policy and accepted-task predicate before optimization. Compare candidate and baseline under the same contract.

Record separately:
- heat emitted by information-bearing degrees of freedom;
- heat emitted by control degrees of freedom;
- actuation and power-supply energy;
- measurement, feedback and readout;
- initialization and reset;
- thermal management/cooling;
- failed or rejected outputs, retries and recovery;
- wall-plug energy, only if measured or supported by a validated model;
- accepted useful tasks, latency, throughput, memory/I/O and full lifecycle cost.

## Pass criteria

A reproduction must pin the source revision and model, pass a source-faithfulness review, preserve the truth table on preregistered held-out states, match the baseline's declared error/throughput boundary, and account for every material energy channel. A lower heat number in one subsystem is insufficient. Independent replication is required before any device or economic claim.

## Stop criteria

Stop or classify as inconclusive if the source model cannot be reconstructed, controller energy is unbounded, the output contract differs, the effect disappears on held-out states/composed gates, or the measured/modelled total energy is not lower under the matched contract.

## Mission boundary

The work can inform FND-001 and future D/G co-design. It does not establish a new physical law, a working UQPU primitive, material substitution, accepted bio-oil, net fusion electricity, lower WACC or Data-Center-to-One-Phone capability. Pangola and fusion applications require separate process-specific models and measurements.
