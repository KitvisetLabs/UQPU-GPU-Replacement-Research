# Cycle 008 Delta 23 — cold-start CI closure

Date: 2026-10-21

## Scope

This closure records a provenance-gate failure and its remediation. It does not
change the scientific evidence class of QOS-AUDIT-010B25 or authorize provider
execution.

## Observed failure

Cold-start workflow runs on commits `aa7ed8edf1ff1e42535adc15875d855f8108fc38`
and `ff76ff1fe4f37225ea3e113dd26b2403570c61a1` reached the handoff audit but
failed because the canonical commit message omitted the required trailer:

`Research-Sync: main`

The audit still checked all A-I lanes and 36 integration pairs. The failure was
therefore a commit-provenance defect, not a scientific, target-feasibility,
provider, credential, or dependency result.

## Remediation

The repair commit and its merge commit carry the required trailer. All evidence
and authorization boundaries remain fail-closed:

- no credentials or authenticated provider snapshot;
- no service/session initialization;
- no QPU jobs or shots;
- no cost, energy, quality, or advantage measurement;
- no promotion of MODEL_ONLY, FND-001–006, EQN-001–006, BIO-001, FUS-001,
  FIN-001, or INV-029–035 claims.

## Next gate

Implement QOS-AUDIT-010B25 in an authorized read-only environment, capture a
redacted fresh `ibm_kingston` target snapshot, validate all preregistered
counterexamples, and only then build an exact route/native-conformance
certificate. QPU submission remains separately blocked.
