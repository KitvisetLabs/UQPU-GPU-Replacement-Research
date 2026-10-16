# Literature Watch — Dense QROM encoding under workspace constraints

**Access date:** 2026-10-16

## Source and evidence class

- Danial Motlagh, *Halving the cost of QROM again via dense encoding*,
  arXiv:2610.02321, submitted 2026-10-01.
  <https://arxiv.org/abs/2610.02321>
- Project classification: `LITERATURE_ONLY`.

## Genuine novelty

The preprint proposes storing two classical information bits per dirty qubit by
using both X and Z bases. In the stated qubit-constrained table-loading regime,
the construction reports leading Toffoli count `N/lambda`, half the leading
SelectSwap value, and a combined sequential-packet construction with leading
count `0.5(1+1/b)N/lambda`.

## Limits and non-transfer

These are fault-tolerant asymptotic/resource-model results, not measurements on
the ER6 circuit or a provider. The claimed factors depend on table size,
message width, available dirty qubits, restoration, precision and which cost
term dominates. The project therefore does not record 2x or approximately 4x
as an achieved reduction and does not combine the paper's cost with project
success probability, cloud pricing, energy or accepted-task economics.

## Concrete project decision

QOS-AUDIT-010B7 uses direct generic PREP/SELECT synthesis for the frozen 10-term
ER6 LCU and measures its decomposition first. Dense QROM becomes a candidate
alternative only after a follow-up freezes:

1. the same coefficient/branch table and approximation precision;
2. workspace and dirty-qubit budgets, including restoration;
3. a baseline SelectSwap/sequential implementation under the same basis;
4. total T/Toffoli, Clifford, depth, logical-qubit and serialization ledgers;
5. projected-operator agreement and the unchanged accepted-output contract.

## Falsifiable follow-up

Implement both ordinary and dense table-loading layouts for a scaled family of
the same LCU contract. The dense route advances only if independent
reconstruction stays within the frozen error budget and its complete resource
ledger improves under the same workspace cap. A leading-term improvement that
is erased by restoration, state preparation or downstream QSVT is a recorded
negative result, not an advantage.
