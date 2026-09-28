# Synchronized Cycle 020 — Execution Delta 01

| Field | Value |
|---|---|
| Date | 2026-09-28 |
| Branch | `research/cycle-020-delta-01-2026-09-28` |
| Base | Verified Cycle 019 closeout `a4e4dbfdc0c88d35e96dda0ec7aa2dc470cf48f7` |
| Code/evidence SHA | `86b529395dd7fbd00360839c745c9e7496aa6d20` |
| State | Cycle 020 closed; exact-SHA GitHub Actions passed 8/8; external gates remain open |

Cycle 020 advanced all twelve lanes under the [canonical parallel research portfolio](PARALLEL_RESEARCH_PORTFOLIO_2026-09-28.md). Code/evidence SHA: `86b529395dd7fbd00360839c745c9e7496aa6d20`. Exact-SHA Actions run: [36458180939](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/36458180939), **passed 8/8**. Executable acceptance artifact: [cycle020-delta01-executable-acceptance.json](../benchmarks/results/cycle020-delta01-executable-acceptance.json), SHA-256 `d9f077dee4b759958c92ca7ec42c40ca6dca467ae022732cc06face625c236ce`.

## Lane deltas

| Lane | Result | Evidence class | Remaining gate |
|---|---|---|---|
| A | Exhaustive 11-node odd-cycle fixture enumerates 2,048 states at the cap with objective 10 and deterministic task/witness hashes. Scaling remains null. | Local exact classical fixture | Matched QPU/GPU workload and independent baseline. |
| B | Nested receipt serialization is canonical; nested duplicate keys reject and key-id rotation changes fixture bytes. External authority, job, invoice and provider claim remain null. | Synthetic receipt fixture | External provider authorization and verifiable execution/billing. |
| C | Two subprocess sets each exit `[0, 23, 23]`; visible targets remain complete old/new payloads. | Local process fixture | Crash consistency, cache/flush behavior and power-loss durability. |
| D | ZIP64 local/central fields cross-bind; signed and unsigned descriptors pass, and central offset mutation rejects before payload access. | Synthetic ZIP64 fixture | Independent archive-producer corpus and complete metadata interoperability. |
| E | Synthetic custody is valid before expiry; the half-open expiry boundary and revoked issuer reject. Physical sample is null. | Synthetic custody | Operational issuers, independent custody review and physical sample. |
| F | Five-component covariance stress covers independent/correlated, missing, indefinite and non-finite cases at output counts 1/2/4/0. Invalid covariance and zero denominator return null. | Model only | Sourced measurements/covariance and accepted-output definition. |
| G | kg/g, m/cm, s/ms and A/mA rescaling propagates through ten pairwise product units; symmetry and positive semidefiniteness under positive diagonal congruence hold. Calibration is null. | Synthetic typed covariance | Traceable calibration and measured covariance. |
| H | Five ranking scenarios each enumerate 24 candidate orders (120 outcomes); winner counts 54/30/18/18 yield interval `[0.15, 0.45]`. No probability or capital claim. | Finite illustrative scenario | Owner-approved priorities, sourced distributions and validated outcome model. |
| FND/EQN | Exact path converts `1 m → 100 cm → 1,000 mm → 1 m`; source-digest mismatch and incompatible-dimension conversion reject. Sort remains `RealModel/Model`. | Source-typed rational model | Independent derivation and broader source-backed unit tests; no law claim. |
| SCM | Fiction-only revocation before use rejects; empirical coupling remains null. | Fiction only | No empirical claim is supported here. |
| AI-COST | Synthetic manifest v10 binds parent v9 and source/split/metric/config hashes; parent corruption and held-out leakage controls reject. Candidate/equivalence remain null. | Synthetic lineage | Real lineage, held-out evaluation, independent baseline and equivalence test. |
| QOS/QSVT | Second non-identity six-bit operator/inverse reconstructs 64 basis states at residual 0; resource-bound mutation rejects. Hardware is null. | Synthetic inverse operator | Independent target-specific synthesis/reconstruction and hardware resource/error evidence. |

## Validation and limits

- Focused Cycle 020 suite: 13 passed, 0 failed.
- Available local workspace discovery: 110 passed, 0 failed.
- Compilation and 12-lane acceptance runner: passed locally.
- Exact-SHA GitHub Actions status: **8/8 passed**.

Primary-source review dated 2026-09-28 used PKWARE APPNOTE v6.3.10 FINAL (revised 2022-11-01), §§4.3.7, 4.3.9 and 4.3.12, and official Python `os.replace` documentation. ZIP vectors are synthetic and payload is never read. Process exits do not establish crash durability; covariance and ranking are model grids; exact unit conversions are not calibration. No hardware, advantage, provider, invoice, commercial, capital, physical-sample, AI-equivalence or new-law claim is made.

All twelve lanes have concrete local acceptance results; all external gates remain open. See the [machine-readable lane ledger](../benchmarks/results/cycle020-delta01-synchronized-lane-ledger.json) and [Cycle 021 handoff](SYNCHRONIZED_CYCLE_021_HANDOFF_2026-09-28.md).
