# Synchronized Cycle 026 — Execution Delta 01

| Field | Value |
|---|---|
| Prepared | 2026-09-30 Asia/Bangkok |
| Branch | `research/cycle-026-delta-01-2026-09-28` |
| Base | Verified Cycle 025 metadata closeout `033aec71256e9ee89e0f3d882180407db925429f` |
| Preregistration | `607ab6d0e2276c19c583ae8420f887fd044dfd47` |
| Code/test/runner SHA | `fb184b6bd31b67ea3a3d7fd69ddf19c024b8687d` |
| Acceptance-artifact SHA | `490ff89cd0983bbeda164a3d852a7112db417958` |
| GitHub Actions | [Run 36658478948](https://github.com/KitvisetLabs/UQPU-GPU-Replacement-Research/actions/runs/36658478948) on exact code SHA `fb184b6bd31b67ea3a3d7fd69ddf19c024b8687d`: 8/8 jobs passed |
| State | Cycle 026 closed; exact-SHA GitHub Actions passed; external gates remain open |

Cycle 026 advances all twelve lanes under the [canonical parallel research portfolio](PARALLEL_RESEARCH_PORTFOLIO_2026-09-28.md). The executable acceptance artifact is [`cycle026-delta01-executable-acceptance.json`](../benchmarks/results/cycle026-delta01-executable-acceptance.json), file SHA-256 `4202441be35e1f14adaffec91d31e0d75f2aecbca8dca863ec43cf7e549e436b`, payload SHA-256 `ca149c47b3b99024f474caf09e2baf276debbe2bbe48d1b1f625737ae782e9b4`.

## Lane deltas

| Lane | Result | Evidence class | Remaining gate |
|---|---|---|---|
| A | Fifth/sixth 11-node fixtures each enumerate 2,048 states; changing only edge 5 changes objective 13→16 and complete witness count 18→16. All 16 sixth-fixture witnesses form eight bound complement pairs. | Local exact classical fixture | Matched QPU/GPU workload, accepted-output contract and independent classical baseline. |
| B | Equivalent exponent/sign numeric receipts canonicalize identically; byte, depth, non-finite, NFC-collision and invalid-surrogate controls reject. | Synthetic receipt canonicalization | Externally authorized provider key plus independently verifiable job and billing evidence. |
| C | Four alternating-target process runs record parent-directory before/after hashes, returned target digests and exit codes; every observation maps to a complete payload. | Local process-termination fixture | Crash consistency, cache/flush behavior and power-loss durability. |
| D | Permuted permitted ZIP64 extra fields parse identically; duplicate, missing and mismatched-size controls reject before payload access, with signed/unsigned descriptors cross-bound. | Synthetic ZIP64 metadata | Independent real-producer archive corpus and full interoperability. |
| E | A six-issuer synthetic custody chain adds delegated scope; removed delegation plus two overlapping issuer-revocation controls reject. | Synthetic custody | Operational issuer keys, independent custody review and a physical sample. |
| F | A ten-component covariance model sweeps sigma 0/0.5/1/2/3/4 while missing, indefinite, non-finite and zero-output cases remain null. | Model only | Sourced measured components/covariance and an accepted-output definition. |
| G | Exact rational covariance computed from a centered Gram construction is invariant under declared translations; prior rescale/permutation inverse remains exact across all 16 products. | Synthetic typed covariance | Traceable calibration and measured covariance for declared measurands. |
| H | Ten declared scenarios enumerate 240 full-grid outcomes, 10 leave-one-out grids and 45 leave-two-out grids; the exact finite winner interval is 3/32–13/32. | Finite illustrative scenario | Owner-approved priorities, sourced distributions and a validated outcome model. |
| FND/EQN | Three independently source-bound rational maps compose to [35/24, 175/48] and invert exactly; source-order and dimension mutations reject. | Source-typed rational model | Independent derivation, registered-unit coverage and source-backed falsifiers. |
| SCM | A five-row fictional consent table adds context mismatch and revocation-after-challenge controls; only the valid transcript accepts. | Fiction only | No empirical inference without separate authorization and external evidence. |
| AI-COST | Synthetic manifest v16 binds disjoint split memberships and metric direction; overlap, invalid direction and parent mutations reject. | Synthetic data lineage | Real source lineage, held-out evaluation, independent baseline and equivalence test. |
| QOS/QSVT | Four declared inverse pairs reconstruct all 64 basis states with residual 0; swapping the first two operators changes all 64 encoded states under a 40-gate/6-qubit cap. | Synthetic inverse operator | Independent synthesis/reconstruction and target-specific resource/error evidence. |

## Validation and limits

- Focused Cycle 026 tests: 13 passed, 0 failed.
- Selected regression set (Cycles 018, 020, 024, 025 and 026): 65 passed, 0 failed.
- Compilation and reproducible acceptance runner: passed locally.
- Remote file verification: all four implementation/test/runner/artifact Git blob IDs exactly match the validated local files.
- Exact-SHA GitHub Actions: 8 passed, 0 failed on run `36658478948`. Passing jobs were Python 3.10, 3.11 and 3.12 tests, reference benchmark, Qiskit verification, QSP phase synthesis, QSPPACK 0.4.0 reconstruction and target-snapshot noise.

Primary-source boundaries are recorded in the preregistration and executable artifact: PKWARE APPNOTE v6.3.10 FINAL (revised 2022-11-01) for ZIP64 metadata, and official Python `os.replace` documentation for process replacement. The archive records are synthetic and payload bytes are not inspected. Process exits and directory observations do not establish crash durability. All other inputs are fixture, model, typed-rational or fiction-only data.

No measured QPU/GPU performance, scaling, quantum advantage, provider execution/invoice, commercial economics, capital result, crash durability, calibration, physical sample, AI equivalence, new physical law or empirical SCM result is claimed.
