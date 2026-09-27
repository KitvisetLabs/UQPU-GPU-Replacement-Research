# SCM-GATE-002 — Blinded Decoder and Pareidolia Control Benchmark

**Date:** 2026-09-28  
**Status:** MODEL_ONLY / SYNTHETIC BLINDED CONTROL  
**Claim boundary:** This benchmark does not test or demonstrate spirits, survival after death, or cross-realm communication.

## Table of Contents — สารบัญ

1. [Research question](#1-research-question)
2. [Null hypothesis](#2-null-hypothesis)
3. [Benchmark contract](#3-benchmark-contract)
4. [Metrics](#4-metrics)
5. [Priming control](#5-priming-control)
6. [Promotion gate](#6-promotion-gate)
7. [Failure conditions](#7-failure-conditions)
8. [Connection to the five-volume canon](#8-connection-to-the-five-volume-canon)
9. [Next gate](#9-next-gate)

## 1. Research question

Can a human or machine decoder appear to recover meaningful labels from ambiguous/noise inputs even when no information path exists from the hidden target to the response?

This is the central false-positive problem behind EVP-like audio, ambiguous imagery and unconstrained AI interpretation.

## 2. Null hypothesis

`H0: decoder response is independent of the hidden target.`

Under K equiprobable labels, exact-match chance is `p0 = 1/K`. A visually or semantically compelling response is not sufficient; scoring must be fixed before target reveal.

## 3. Benchmark contract

Implementation: `software/uqpu-prototype/uqpu/scm_blinded_decoder.py`

The synthetic benchmark:
- samples hidden targets independently;
- prevents a target-to-decoder information path by construction;
- optionally biases responses toward one label to model priming;
- stores trial IDs and blinded target/response pairs;
- supplies SHA-256 content commitments for future preregistration/provenance workflows.

Real human experiments would require ethics/consent procedures and are not performed by this software.

## 4. Metrics

For N trials and K labels:

```text
p0 = 1/K
hit_rate = exact_hits/N
excess = hit_rate - p0
z = (exact_hits - N*p0) / sqrt(N*p0*(1-p0))
```

A future empirical protocol should add confidence intervals, multiplicity control, calibration, preregistered stopping rules and effect-size requirements. Statistical significance alone does not identify a source.

## 5. Priming control

The simulator can force a high fraction of decoder responses toward a preferred label while targets remain independent. This demonstrates the distinction:

```text
strong response bias != source-dependent information
```

The same principle applies to suggestive EVP prompts, ghost-image labels and generative-AI descriptions.

## 6. Promotion gate

SCM-GATE-002 passes as a **control instrument** when:
1. deterministic seeded null trials reproduce;
2. unprimed null decoding remains near chance at scale;
3. strong response priming does not manufacture target information;
4. undeclared labels are rejected;
5. CI passes.

This does not promote the SCM program beyond E0/E1. Promotion toward SCM-E4 requires prospective real observations with leakage-resistant blinding and independent replication.

## 7. Failure conditions

- labels or scoring rules chosen after target reveal;
- target leakage through filenames, metadata, timestamps or operator behavior;
- repeated prompting until a desired AI answer appears;
- cherry-picking only recognizable noise samples;
- treating semantic resemblance as an exact precommitted hit;
- training/evaluating on the same target corpus without held-out controls.

## 8. Connection to the five-volume canon

- **Volume 1:** characters discover that compelling perception can emerge from noise.
- **Volume 2:** SCM-2 imaging team adopts blinded reconstruction after a false apparition.
- **Volume 3:** adversarial actors exploit priming, deepfakes and AI-generated interpretations.
- **Volume 4:** courts/regulators require provenance and precommitted scoring for claimed cross-realm messages.
- **Volume 5:** a fictional communicator must defeat these null controls before authenticated information exchange is accepted.

## 9. Next gate

**SCM-GATE-003:** prospective cryptographic challenge-response protocol. Generate unpredictable targets after isolation, commit targets/scoring rules, audit leakage, reveal only after responses are frozen, and measure verified information rather than narrative resemblance.
