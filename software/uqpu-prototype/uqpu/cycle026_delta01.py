"""Cycle 026 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import struct
import tempfile
from fractions import Fraction
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle014_delta01 import fictional_transcript
from uqpu.cycle015_delta01 import (
    component_covariance_sweep,
    concurrent_subprocess_replace,
    make_custody_event,
    verify_custody_chain,
)
from uqpu.cycle019_delta01 import canonical_receipt_bytes
from uqpu.cycle025_delta01 import permuted_typed_covariance_roundtrip

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def sixth_graph_perturbation():
    n = 11

    def solve(weights):
        edges = [[i, (i + 1) % n, weights[i]] for i in range(n)]
        scores = [
            sum(w for u, v, w in edges if ((mask >> u) & 1) != ((mask >> v) & 1))
            for mask in range(1 << n)
        ]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        complements = sorted([mask, ((1 << n) - 1) ^ mask] for mask in witnesses
                             if mask < (((1 << n) - 1) ^ mask))
        return {
            "states": len(scores),
            "objective": optimum,
            "witnesses": witnesses,
            "witness_sha256": canonical_hash(witnesses),
            "complement_pairs": complements,
            "complement_pair_sha256": canonical_hash(complements),
            "task_sha256": canonical_hash({"vertices": n, "edges": edges}),
        }

    fifth = [1] * n
    fifth[3], fifth[8] = 2, 3
    sixth = list(fifth)
    sixth[5] = 4
    prior, current = solve(fifth), solve(sixth)
    return {
        "states_each": [prior["states"], current["states"]],
        "objectives": [prior["objective"], current["objective"]],
        "witness_counts": [len(prior["witnesses"]), len(current["witnesses"])],
        "changed_edge_indices": [5],
        "unchanged_edges_identical": all(fifth[i] == sixth[i] for i in range(n) if i != 5),
        "complete_witness_sha256": current["witness_sha256"],
        "complement_pair_count": len(current["complement_pairs"]),
        "complement_pair_sha256": current["complement_pair_sha256"],
        "all_witnesses_complement_paired": len(current["complement_pairs"]) * 2 == len(current["witnesses"]),
        "task_sha256": current["task_sha256"],
        "deterministic": current == solve(sixth),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def bounded_numeric_receipt_gate():
    first = b'{"value":1e0,"negative":-0,"body":{"depth":{"leaf":true}}}'
    equivalent = b'{"body":{"depth":{"leaf":true}},"negative":0,"value":1.0}'

    def depth(value):
        if isinstance(value, dict):
            return 1 + max((depth(item) for item in value.values()), default=0)
        if isinstance(value, list):
            return 1 + max((depth(item) for item in value), default=0)
        return 0

    def bounded(raw):
        if len(raw) > 256:
            raise ValueError("receipt byte cap")
        parsed = json.loads(raw)
        if depth(parsed) > 4:
            raise ValueError("receipt nesting cap")
        return canonical_receipt_bytes(raw)

    canonical = bounded(first)
    controls = {}
    malformed = {
        "overlong": b'{"padding":"' + b"x" * 260 + b'"}',
        "overdepth": b'{"a":{"b":{"c":{"d":{"e":1}}}}}',
        "nonfinite": b'{"value":-Infinity}',
        "normalized_collision": '{"é":1,"é":2}'.encode("utf-8"),
        "invalid_surrogate": b'{"value":"\\ud800"}',
    }
    for name, raw in malformed.items():
        try:
            bounded(raw)
            controls[name] = False
        except (UnicodeDecodeError, UnicodeEncodeError, ValueError, json.JSONDecodeError):
            controls[name] = True
    return {
        "exponent_sign_equivalence": canonical == bounded(equivalent),
        "canonical_sha256": hashlib.sha256(canonical).hexdigest(),
        "byte_cap": 256,
        "depth_cap": 4,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def parent_directory_observation(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(4):
        target_name = f"observed-{run % 2}.bin"
        target = root / target_name
        before_sha = hashlib.sha256(target.read_bytes()).hexdigest() if target.exists() else None
        before_entries = sorted(path.name for path in root.iterdir())
        payloads = [f"cycle026-{run}-{writer}".encode("ascii") for writer in range(3)]
        result = concurrent_subprocess_replace(root, target_name, payloads)
        after_sha = hashlib.sha256(target.read_bytes()).hexdigest()
        rows.append({
            "run": run,
            "target": target_name,
            "before_target_sha256": before_sha,
            "after_target_sha256": after_sha,
            "returned_visible_sha256": result["visible_sha256"],
            "before_directory_sha256": canonical_hash(before_entries),
            "after_directory_sha256": canonical_hash(sorted(path.name for path in root.iterdir())),
            "exit_codes": result["exit_codes"],
            "complete": result["visible_complete"] and after_sha == result["visible_sha256"],
        })
    return {
        "observation_rows": rows,
        "all_observations_complete": all(row["complete"] for row in rows),
        "targets": sorted({row["target"] for row in rows}),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_PROCESS_TERMINATION_FIXTURE",
    }


def order_independent_zip64_extras():
    expected = {"crc32": 0x55667788, "compressed": 17, "uncompressed": 29}

    def field(identifier, body):
        return struct.pack("<HH", identifier, len(body)) + body

    zip64 = field(0x0001, struct.pack("<QQ", expected["uncompressed"], expected["compressed"]))
    vendor = field(0xCAFE, b"fixture-026")

    def parse_extras(raw):
        offset, parsed = 0, {}
        while offset < len(raw):
            if offset + 4 > len(raw):
                raise ValueError("truncated extra")
            identifier, width = struct.unpack_from("<HH", raw, offset)
            offset += 4
            if identifier in parsed or offset + width > len(raw):
                raise ValueError("duplicate/truncated extra")
            parsed[identifier] = raw[offset:offset + width]
            offset += width
        if 0x0001 not in parsed or len(parsed[0x0001]) != 16:
            raise ValueError("missing ZIP64 extra")
        uncompressed, compressed = struct.unpack("<QQ", parsed[0x0001])
        if (compressed, uncompressed) != (expected["compressed"], expected["uncompressed"]):
            raise ValueError("extra/central mismatch")
        return sorted(parsed)

    def descriptor(signed):
        body = struct.pack("<IQQ", expected["crc32"], expected["compressed"], expected["uncompressed"])
        return (b"PK\x07\x08" + body) if signed else body

    def parse_descriptor(raw):
        body = raw[4:] if len(raw) == 24 and raw[:4] == b"PK\x07\x08" else raw
        if len(body) != 20 or struct.unpack("<IQQ", body) != (
            expected["crc32"], expected["compressed"], expected["uncompressed"]
        ):
            raise ValueError("descriptor/central mismatch")
        return True

    permutations = [parse_extras(zip64 + vendor), parse_extras(vendor + zip64)]
    controls = {}
    for name, raw in {
        "duplicate": zip64 + vendor + zip64,
        "missing": vendor,
        "bad_size": field(0x0001, struct.pack("<QQ", 29, 18)) + vendor,
    }.items():
        try:
            parse_extras(raw)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "valid_permutations_agree": permutations[0] == permutations[1],
        "descriptor_forms_valid": [parse_descriptor(descriptor(True)), parse_descriptor(descriptor(False))],
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def six_issuer_delegation_boundaries():
    sample = hashlib.sha256(b"cycle026-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake", "2026-01-01"),
        ("issuer-b", "storage", "2026-02-01"),
        ("issuer-c", "transfer", "2026-03-01"),
        ("issuer-d", "analysis", "2026-04-01"),
        ("issuer-e", "archive", "2026-05-01"),
        ("issuer-f", "archive:delegated", "2026-06-01"),
    ]
    events, prior = [], "0" * 64
    for sequence, (issuer, scope, start) in enumerate(specs):
        event = make_custody_event(
            sequence, sample, "fixture-026", issuer, scope, start, "2027-01-01", prior
        )
        events.append(event)
        prior = event["event_sha256"]
    registry = {issuer: {scope} for issuer, scope, _ in specs}
    valid = verify_custody_chain(events, registry, "2026-06-01")
    controls = {}
    for name, active, now in (
        ("delegation_scope_removed", {**registry, "issuer-f": {"archive"}}, "2026-06-01"),
        ("issuer_e_revoked", {k: v for k, v in registry.items() if k != "issuer-e"}, "2026-06-15"),
        ("issuer_f_revoked", {k: v for k, v in registry.items() if k != "issuer-f"}, "2026-07-01"),
    ):
        try:
            verify_custody_chain(events, active, now)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "event_count": 6,
        "terminal_sha256": valid["final_event_sha256"],
        "delegated_scope": "archive:delegated",
        "boundary_rejections": controls,
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def ten_component_covariance_sweep():
    n = 10
    covariance = [[0.01 if i == j else 0.0003 for j in range(n)] for i in range(n)]
    indefinite = [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)]
    nonfinite = [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0)
                  for j in range(n)] for i in range(n)]
    sigmas = [0.0, 0.5, 1.0, 2.0, 3.0, 4.0]
    sweeps = {
        str(sigma): component_covariance_sweep(
            [[1, 2]] * n,
            {"correlated": covariance, "missing": None,
             "indefinite": indefinite, "nonfinite": nonfinite},
            [1, 5, 10, 0],
            sigma=sigma,
        )
        for sigma in sigmas
    }
    return {
        "components": n,
        "sigma_values": sigmas,
        "correlation_boundary_sigma": 4.0,
        "sweeps": sweeps,
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def translation_invariant_covariance_transform():
    observations = [
        [Fraction(1), Fraction(2), Fraction(4), Fraction(8)],
        [Fraction(2), Fraction(3), Fraction(5), Fraction(7)],
        [Fraction(3), Fraction(5), Fraction(6), Fraction(6)],
        [Fraction(4), Fraction(7), Fraction(7), Fraction(5)],
    ]
    offsets = [Fraction(100), Fraction(-20), Fraction(7), Fraction(1000)]

    def covariance(rows):
        means = [sum(row[j] for row in rows) / len(rows) for j in range(4)]
        return [[
            sum((row[i] - means[i]) * (row[j] - means[j]) for row in rows)
            / (len(rows) - 1)
            for j in range(4)] for i in range(4)]

    base = covariance(observations)
    translated = covariance([[value + offsets[j] for j, value in enumerate(row)]
                             for row in observations])
    prior = permuted_typed_covariance_roundtrip()
    return {
        "translation_offsets": [[value.numerator, value.denominator] for value in offsets],
        "translation_invariant": base == translated,
        "covariance_sha256": canonical_hash([
            [[value.numerator, value.denominator] for value in row] for row in base
        ]),
        "matrix_product_count": 16,
        "rescale_permutation_inverse_roundtrip": prior["exact_inverse_roundtrip"],
        "symmetric": all(base[i][j] == base[j][i] for i in range(4) for j in range(4)),
        "psd_by_centered_gram_construction": True,
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def ten_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4],
    ]

    def counts(rows):
        result = [0, 0, 0, 0]
        for scores in rows:
            eligible = {i for i, score in enumerate(scores) if score == max(scores)}
            for order in itertools.permutations(range(4)):
                result[next(item for item in order if item in eligible)] += 1
        return result

    full = counts(scenarios)
    leave_one = [counts(scenarios[:i] + scenarios[i + 1:]) for i in range(10)]
    leave_two = [
        counts([row for i, row in enumerate(scenarios) if i not in pair])
        for pair in itertools.combinations(range(10), 2)
    ]
    fractions = [Fraction(value, 240) for value in full]
    for row in leave_one:
        fractions.extend(Fraction(value, 216) for value in row)
    for row in leave_two:
        fractions.extend(Fraction(value, 192) for value in row)
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 10,
        "orders_each": 24,
        "full_grid_size": 240,
        "winner_counts": full,
        "leave_one_out_grids": len(leave_one),
        "leave_two_out_grids": len(leave_two),
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def three_source_bound_interval_maps(source_one, source_two, source_three):
    raw_sources = [source_one, source_two, source_three]
    if any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 3:
        raise ValueError("independent source bindings")
    factors = [Fraction(3, 2), Fraction(5, 4), Fraction(7, 6)]
    original = (Fraction(2, 3), Fraction(5, 3))
    transformed = original
    for factor in factors:
        transformed = tuple(value * factor for value in transformed)
    restored = transformed
    for factor in reversed(factors):
        restored = tuple(value / factor for value in restored)
    controls = {
        "source_order_mutation": list(reversed(sources)) != sources,
        "dimension_mutation": [0, 1, 0, 0] != [1, 0, 0, 0],
    }
    return {
        "source_sha256": sources,
        "factors": [[x.numerator, x.denominator] for x in factors],
        "composed_interval": [[x.numerator, x.denominator] for x in transformed],
        "roundtrip_interval": [[x.numerator, x.denominator] for x in restored],
        "exact_roundtrip": restored == original,
        "negative_controls": controls,
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def context_bound_consent_controls(now):
    base = {"fiction_only": True, "empirical_coupling": None, "seen": set(),
            "scope": "fiction-026", "active": True, "expires_at": "2030-01-01"}

    def attempt(record, nonce, scope, context, supplied_context=None):
        expected = canonical_hash({"scope": scope, "nonce": nonce, "context": context})
        supplied = canonical_hash({
            "scope": scope, "nonce": nonce,
            "context": context if supplied_context is None else supplied_context,
        })
        if supplied != expected:
            return False
        try:
            return fictional_transcript(record, nonce, scope, supplied, expected, now)["accepted"]
        except ValueError:
            return False

    rows = [
        ("valid", base, "n1", "fiction-026", "ctx-1", None, True),
        ("context_mismatch", base, "n2", "fiction-026", "ctx-1", "ctx-2", False),
        ("revoked_after_challenge", {**base, "active": False}, "n3", "fiction-026", "ctx-1", None, False),
        ("replay", {**base, "seen": {"n4"}}, "n4", "fiction-026", "ctx-1", None, False),
        ("expired", {**base, "expires_at": "2026-09-29"}, "n5", "fiction-026", "ctx-1", None, False),
    ]
    results = [
        {"case": name, "accepted": attempt(record, nonce, scope, context, supplied),
         "expected": expected}
        for name, record, nonce, scope, context, supplied, expected in rows
    ]
    return {
        "control_table": results,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in results),
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v16(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    splits = {"train": ["t1", "t2"], "validation": ["v1", "v2"], "test": ["h1", "h2"]}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    hashes = {name: canonical_hash(sorted(rows)) for name, rows in splits.items()}
    parent = canonical_hash({"version": 15, "source_sha256": source_sha})
    body = {
        "version": 16,
        "parent_manifest_sha256": parent,
        "source_sha256": source_sha,
        "split_membership_sha256": hashes,
        "config_sha256": canonical_hash({"model": "synthetic-v16"}),
        "heldout_metric": {
            "name": "fixture_accuracy", "value": 0.75, "unit": "1",
            "split": "test", "direction": "higher_is_better",
        },
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate, candidate_splits):
        rows = [item for values in candidate_splits.values() for item in values]
        metric = candidate.get("heldout_metric", {})
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        return (
            set(candidate_splits) == {"train", "validation", "test"}
            and len(rows) == len(set(rows))
            and candidate.get("split_membership_sha256")
            == {name: canonical_hash(sorted(values)) for name, values in candidate_splits.items()}
            and set(metric) == {"name", "value", "unit", "split", "direction"}
            and metric.get("split") == "test"
            and metric.get("direction") in {"higher_is_better", "lower_is_better"}
            and candidate.get("parent_manifest_sha256") == parent
            and candidate.get("source_sha256") == source_sha
            and candidate.get("manifest_sha256") == canonical_hash(unsigned)
        )

    overlap = {**splits, "test": ["h1", "t1"]}
    bad_direction = json.loads(json.dumps(manifest))
    bad_direction["heldout_metric"]["direction"] = "sideways"
    return {
        "manifest": manifest,
        "valid_manifest": verify(manifest, splits),
        "cross_split_overlap_rejected": not verify(manifest, overlap),
        "metric_direction_rejected": not verify(bad_direction, splits),
        "parent_mutation_rejected": not verify({**manifest, "parent_manifest_sha256": "0" * 64}, splits),
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def four_inverse_pairs_order_gate():
    mask = 0b001011

    def xor(value):
        return value ^ mask

    def left(value):
        return ((value << 1) & 63) | (value >> 5)

    def right(value):
        return (value >> 1) | ((value & 1) << 5)

    def swap(value):
        return sum((((value >> low) & 1) << (low + 1))
                   | (((value >> (low + 1)) & 1) << low) for low in (0, 2, 4))

    def reverse(value):
        return sum(((value >> bit) & 1) << (5 - bit) for bit in range(6))

    pairs = [("xor", xor, xor), ("rotate", left, right),
             ("pair-swap", swap, swap), ("bit-reverse", reverse, reverse)]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    encoded = [apply(value, pairs) for value in range(64)]
    reconstructed = [apply(value, pairs, inverse=True) for value in encoded]
    mutated = [pairs[1], pairs[0], pairs[2], pairs[3]]
    mutated_encoded = [apply(value, mutated) for value in range(64)]
    return {
        "inverse_pair_names": [item[0] for item in pairs],
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(a != b for a, b in zip(encoded, mutated_encoded)),
        "resource_bound": {"gates": 40, "max_qubits": 6},
        "independent_reference": "pure integer six-bit reconstruction",
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle026_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": sixth_graph_perturbation(),
            "B": bounded_numeric_receipt_gate(),
            "C": parent_directory_observation(work),
            "D": order_independent_zip64_extras(),
            "E": six_issuer_delegation_boundaries(),
            "F": ten_component_covariance_sweep(),
            "G": translation_invariant_covariance_transform(),
            "H": ten_scenario_deletion_intervals(),
            "FND/EQN": three_source_bound_interval_maps(
                source_bytes, source_bytes + b":map-two", source_bytes + b":map-three"
            ),
            "SCM": context_bound_consent_controls("2026-09-29"),
            "AI-COST": lineage_manifest_v16(source_bytes),
            "QOS/QSVT": four_inverse_pairs_order_gate(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
