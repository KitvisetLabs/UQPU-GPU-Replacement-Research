# SCM-P2-DEC-001 — Blinded Human/AI Ambiguous-Signal Decoder Protocol

**Date:** 2026-09-28  
**Status:** DESIGN ONLY / NO HUMAN DATA / NO AI ANOMALOUS-EVIDENCE CLAIM

## Table of Contents — สารบัญ
1. [Objective](#1-objective)
2. [Stimulus families](#2-stimulus-families)
3. [Blinding](#3-blinding)
4. [Human and AI arms](#4-human-and-ai-arms)
5. [Primary outcomes](#5-primary-outcomes)
6. [Priming experiment](#6-priming-experiment)
7. [Anti-hallucination rules](#7-anti-hallucination-rules)
8. [Promotion boundary](#8-promotion-boundary)
9. [Canon use](#9-canon-use)

## 1. Objective
Quantify how often humans and AI assign meaningful labels to noise/ambiguous audio or imagery when ground truth is known and hidden.

## 2. Stimulus families
A: pure/null noise; B: weak known injected target; C: ordinary environmental artifact; D: held-out synthetic mixture. Exact generation and labels are frozen before decoding.

## 3. Blinding
Stimulus filenames/metadata contain no target labels. Decoder sees randomized IDs only. Ground truth remains inaccessible until responses and confidence are frozen.

## 4. Human and AI arms
Human participants require appropriate ethics/consent. AI models are version-pinned with prompt, model identifier, decoding settings and retrieval/network policy recorded. Human and AI results are reported separately; neither substitutes for the other.

## 5. Primary outcomes
Exact label accuracy, false-positive rate on nulls, calibration of confidence, abstention rate, confusion matrix and performance on held-out stimuli. Free-text resemblance is secondary and cannot override primary scoring.

## 6. Priming experiment
A preregistered arm may expose a suggestive label before decoding while an unprimed arm receives neutral instructions. The question is whether expectation changes reported perception, not whether priming creates a real source channel.

## 7. Anti-hallucination rules
No repeated prompting until a desired answer appears; no target-dependent prompt editing; no post-hoc label merging; no discarding nulls; no training on held-out targets; record every model response.

## 8. Promotion boundary
DEC-001 characterizes interpreters and false positives. Even exceptional accuracy on known injected signals does not establish a spiritual source. A later INF-001 trial must test prospective source-dependent information.

## 9. Canon use
Vol 2 turns the first apparent ghost image/voice into a decoder-control crisis. Vol 3 weaponizes priming, deepfakes and model hallucination. By Vol 5, SCM-3 displays confidence/provenance and can abstain rather than manufacture a face/voice.
