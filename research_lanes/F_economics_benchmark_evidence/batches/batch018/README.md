# Lane F — Batch 018

ER6 snapshot-noisy optimum probability is 956/4096 = 0.2333984375. Under the independent-shot model this gives 4.2845188284518825 expected shots per optimum sample; 18 shots provide >=99% probability of observing at least one optimum sample.

This is a quality-adjusted shot burden, not a dollar cost. `provider_dollar_cost_calculated=false` remains correct because FakeKingston snapshot performance is not a live provider-matched measurement and the GitHub simulation runtime is not billable QPU time.

Next: obtain provider-matched real-QPU success probability + billable usage/actual charge and a competitive classical CPU/GPU baseline for the same accepted-output contract. RG-028 remains open.
