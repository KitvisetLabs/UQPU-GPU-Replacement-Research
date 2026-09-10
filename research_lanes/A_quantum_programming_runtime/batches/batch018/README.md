# Lane A — Batch 018

Priority #1 advance: generalized the target-snapshot QAOA runner from a hard-coded triangle to a named-fixture contract and executed the 6-qubit ER6 fixture without changing its workload identity.

ER6 ideal optimum probability is 0.25391734004004546 and snapshot-noisy probability is 0.2333984375. The next algorithm experiment is an equal-budget comparison of the current p=1 baseline with warm-start QAOA and/or an evolutionary/CVaR optimizer route. Any improvement must be judged on the same contract, accepted-output definition, total evaluation budget and target-aware pipeline.

Evidence: CALIBRATION_SNAPSHOT_SIMULATION, not REAL_QPU.
