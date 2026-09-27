# SCM-P2-CAL-001 — Known-Interference Calibration Benchmark Specification

**Date:** 2026-09-28  
**Status:** PREREGISTERED-DESIGN CANDIDATE / SYNTHETIC-FIRST / NO PARANORMAL TEST

## Table of Contents — สารบัญ
1. [Objective](#1-objective)
2. [Hypotheses](#2-hypotheses)
3. [Conditions](#3-conditions)
4. [Sensor channels](#4-sensor-channels)
5. [Primary metrics](#5-primary-metrics)
6. [Randomization and blinding](#6-randomization-and-blinding)
7. [Calibration provenance](#7-calibration-provenance)
8. [Failure and exclusion rules](#8-failure-and-exclusion-rules)
9. [Synthetic benchmark first](#9-synthetic-benchmark-first)
10. [Promotion rule](#10-promotion-rule)

## 1. Objective
Measure how often an SCM-style multimodal detector generates threshold/coincidence events under ordinary conditions and known injected disturbances. Ground truth is mundane by construction.

## 2. Hypotheses
Primary H1: known interference changes the precommitted detector event rate relative to control.
H0: condition does not change the precommitted event rate.
This study does not contain a spirit-source hypothesis.

## 3. Conditions
- control: ordinary background after calibration;
- known-interference: traceable injected disturbance;
- optional future subclasses: RF, magnetic, acoustic, vibration, thermal, optical.

Subclasses must be declared before analysis.

## 4. Sensor channels
Candidate synchronized channels: magnetic, electric/RF, acoustic, vibration, thermal, visible/near-IR and photon counting where justified. Every channel requires sensor ID, units, sampling rate, calibration record and clock provenance.

## 5. Primary metrics
- per-channel threshold exceedance rate;
- multimodal coincidence false-positive rate;
- sensitivity to known injection;
- specificity under control;
- detection latency;
- missing/corrupt data fraction.

For binary ground-truth injection:
`sensitivity = TP/(TP+FN)`
`specificity = TN/(TN+FP)`
`FPR = FP/(FP+TN)`

Thresholds and coincidence windows must be frozen before benchmark scoring.

## 6. Randomization and blinding
Blocked randomization determines control vs injection schedule. The primary analyst receives coded conditions until event extraction is frozen. Injection operator and analyst are separate roles where practical.

## 7. Calibration provenance
Each trial points to calibration IDs and raw-data SHA-256 using `scm_trial_ledger.py`. Pre/post-run reference injections test sensor drift. Environmental RF/acoustic/thermal/power logs accompany the replication manifest.

## 8. Failure and exclusion rules
Exclude only predeclared hardware/data-integrity failures. Do not exclude “ugly” null trials or inconvenient false positives. Missing calibration, broken raw hash or undisclosed schedule leakage blocks the run.

## 9. Synthetic benchmark first
Before physical acquisition, generate a frozen synthetic fixture with seeded Gaussian/background noise and common-mode interference using SCM-GATE-001. The goal is to validate the analysis pipeline, not to estimate real detector performance.

## 10. Promotion rule
Passing CAL-001 means the system's response to known ordinary causes is characterized. It does **not** promote evidence toward spirits or cross-realm communication. Its output becomes the null/adversary library for later SCM-P2-DEC-001 and INF-001.
