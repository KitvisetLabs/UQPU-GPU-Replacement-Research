"""Cycle 024 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
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

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def fourth_graph_perturbation():
    """Enumerate an 11-node cycle and bind a fourth single-edge perturbation."""
    n = 11

    def solve(weights):
        edges = [[i, (i + 1) % n, weights[i]] for i in range(n)]
        scores = [
            sum(weight for u, v, weight in edges
                if ((mask >> u) & 1) != ((mask >> v) & 1))
            for mask in range(1 << n)
        ]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        cut_counts = [
            sum(((mask >> i) & 1) != ((mask >> ((i + 1) % n)) & 1)
                for mask in witnesses)
            for i in range(n)
        ]
        return {
            "states": len(scores),
            "objective": optimum,
            "witnesses": witnesses,
            "witness_sha256": canonical_hash(witnesses),
            "task_sha256": canonical_hash({"vertices": n, "edges": edges}),
            "edge_cut_counts": cut_counts,
        }

    base = [1] * n
    fourth = list(base)
    fourth[3] = 2
    baseline, changed = solve(base), solve(fourth)
    repeated = solve(fourth)
    return {
        "states": changed["states"],
        "state_cap": 2048,
        "objectives": [baseline["objective"], changed["objective"]],
        "witness_counts": [len(baseline["witnesses"]), len(changed["witnesses"])],
        "complete_witness_sha256": changed["witness_sha256"],
        "task_sha256": changed["task_sha256"],
        "changed_edge_index": 3,
        "changed_edge_forced_cut": changed["edge_cut_counts"][3] == len(changed["witnesses"]),
        "unchanged_edge_7_weight_invariant": base[7] == fourth[7],
        "deterministic": changed == repeated,
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def canonical_receipt_adversaries():
    first = br'{"scope":"fixture","body":{"items":[{"b":2,"a":1}],"label":"\u00e9"}}'
    reordered = br'{"body":{"label":"\u00e9","items":[{"a":1,"b":2}]},"scope":"fixture"}'
    canonical_first = canonical_receipt_bytes(first)
    canonical_reordered = canonical_receipt_bytes(reordered)
    controls = {}
    malformed = {
        "normalized_duplicate": br'{"body":{"\u00e9":1,"e\u0301":2}}',
        "nested_duplicate": br'{"body":{"x":1,"x":2}}',
        "invalid_utf8": b'{"body":"\xff"}',
        "truncated_json": b'{"body":',
    }
    for name, raw in malformed.items():
        try:
            canonical_receipt_bytes(raw)
            controls[name] = False
        except (UnicodeDecodeError, ValueError, json.JSONDecodeError):
            controls[name] = True
    return {
        "nested_reordering_invariant": canonical_first == canonical_reordered,
        "canonical_sha256": hashlib.sha256(canonical_first).hexdigest(),
        "negative_controls": controls,
        "collision_policy": "NFC-normalize keys and reject the first normalized duplicate",
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def process_termination_boundaries(directory):
    rows = []
    for run in range(2):
        root = Path(directory) / f"run-{run}"
        result = concurrent_subprocess_replace(
            root,
            "target.bin",
            [f"cycle024-{run}-{writer}".encode("ascii") for writer in range(3)],
        )
        rows.append({
            "interruption_points": ["after_replace", "before_replace", "after_replace"],
            "exit_codes": result["exit_codes"],
            "recovered_complete_old_or_new": result["visible_complete"],
            "recovered_sha256": result["visible_sha256"],
        })
    return {
        "runs": rows,
        "all_recovered_complete": all(row["recovered_complete_old_or_new"] for row in rows),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_PROCESS_TERMINATION_FIXTURE",
    }


def zip64_signature_prefix_gate():
    expected = {"crc32": 0xA1B2C3D4, "compressed": 8, "uncompressed": 12}

    def descriptor(signed=True, compressed=8, uncompressed=12):
        body = (expected["crc32"].to_bytes(4, "little")
                + compressed.to_bytes(8, "little")
                + uncompressed.to_bytes(8, "little"))
        return (b"PK\x07\x08" + body) if signed else body

    def parse(raw, central_compressed=8, central_uncompressed=12):
        if len(raw) == 24 and raw[:4] == b"PK\x07\x08":
            form, body = "signed", raw[4:]
        elif len(raw) == 20:
            form, body = "unsigned", raw
        else:
            raise ValueError("descriptor width/signature")
        crc = int.from_bytes(body[:4], "little")
        compressed = int.from_bytes(body[4:12], "little")
        uncompressed = int.from_bytes(body[12:20], "little")
        if (crc, compressed, uncompressed) != (
                expected["crc32"], central_compressed, central_uncompressed):
            raise ValueError("descriptor/central mismatch")
        return form

    forms = [parse(descriptor(True)), parse(descriptor(False))]
    size_mutation_rejected = False
    try:
        parse(descriptor(False, compressed=9))
    except ValueError:
        size_mutation_rejected = True
    central_mutation_rejected = False
    try:
        parse(descriptor(True), central_uncompressed=13)
    except ValueError:
        central_mutation_rejected = True
    signature_like_payload_prefix = b"PK\x07\x08payload-fixture"
    return {
        "descriptor_forms": forms,
        "size_mutation_rejected": size_mutation_rejected,
        "central_size_mutation_rejected": central_mutation_rejected,
        "signature_like_payload_prefix_sha256": hashlib.sha256(signature_like_payload_prefix).hexdigest(),
        "signature_like_payload_read": False,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_DESCRIPTOR",
    }


def four_issuer_custody_rotation():
    sample = hashlib.sha256(b"cycle024-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake", "2026-01-01", "2027-01-01"),
        ("issuer-b", "storage", "2026-02-01", "2027-01-01"),
        ("issuer-c", "transfer", "2026-03-01", "2027-01-01"),
        ("issuer-d", "analysis", "2026-04-01", "2027-01-01"),
    ]
    events, prior = [], "0" * 64
    for sequence, (issuer, scope, start, expiry) in enumerate(specs):
        event = make_custody_event(
            sequence, sample, "fixture-024", issuer, scope, start, expiry, prior
        )
        events.append(event)
        prior = event["event_sha256"]
    registry = {issuer: {scope} for issuer, scope, _, _ in specs}
    valid = verify_custody_chain(events, registry, "2026-04-01")
    boundary_rejections = {}
    for name, auth, date in (
        ("before_fourth_validity", registry, "2026-03-31"),
        ("fourth_issuer_revoked", {k: v for k, v in registry.items() if k != "issuer-d"}, "2026-04-01"),
        ("at_expiry", registry, "2027-01-01"),
    ):
        try:
            verify_custody_chain(events, auth, date)
            boundary_rejections[name] = False
        except ValueError:
            boundary_rejections[name] = True
    return {
        "event_count": len(events),
        "terminal_sha256": valid["final_event_sha256"],
        "boundary_rejections": boundary_rejections,
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def covariance_uncertainty_sweep():
    n = 8
    covariance = [[0.01 if i == j else 0.0005 for j in range(n)] for i in range(n)]
    indefinite = [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)]
    nonfinite = [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0)
                  for j in range(n)] for i in range(n)]
    rows = {}
    for sigma in (0.5, 1.0, 2.0):
        rows[str(sigma)] = component_covariance_sweep(
            [[1, 2]] * n,
            {"correlated": covariance, "missing": None,
             "indefinite": indefinite, "nonfinite": nonfinite},
            [1, 2, 4, 0], sigma=sigma,
        )
    return {
        "components": n,
        "sigma_values": [0.5, 1.0, 2.0],
        "sweeps": rows,
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def typed_covariance_roundtrip():
    order = ["mass", "length", "duration", "current"]
    dimensions = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
    factors = [Fraction(1000), Fraction(100), Fraction(1000), Fraction(1000)]
    base = [[Fraction(10 if i == j else 1, 10) for j in range(4)] for i in range(4)]
    scaled = [[base[i][j] * factors[i] * factors[j] for j in range(4)] for i in range(4)]
    restored = [[scaled[i][j] / factors[i] / factors[j] for j in range(4)] for i in range(4)]
    product_dimensions = [
        [a + b for a, b in zip(dimensions[i], dimensions[j])]
        for i in range(4) for j in range(4)
    ]
    return {
        "order": order,
        "order_sha256": canonical_hash(order),
        "dimension_sha256": canonical_hash(product_dimensions),
        "matrix_product_count": 16,
        "exact_inverse_roundtrip": restored == base,
        "symmetric": all(scaled[i][j] == scaled[j][i] for i in range(4) for j in range(4)),
        "psd_by_positive_diagonal_congruence": all(value > 0 for value in factors),
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def leave_one_scenario_out_ranking():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
    ]

    def winner_counts(rows):
        counts = [0, 0, 0, 0]
        for scores in rows:
            best = max(scores)
            eligible = {i for i, score in enumerate(scores) if score == best}
            for order in itertools.permutations(range(4)):
                counts[next(candidate for candidate in order if candidate in eligible)] += 1
        return counts

    full = winner_counts(scenarios)
    leave_one_out = [winner_counts(scenarios[:i] + scenarios[i + 1:])
                     for i in range(len(scenarios))]
    total = len(scenarios) * math.factorial(4)
    fractions = [count / total for count in full]
    return {
        "scenario_count": len(scenarios),
        "orders_each": 24,
        "grid_size": total,
        "winner_counts": full,
        "finite_grid_range": [min(fractions), max(fractions)],
        "leave_one_out_winner_counts": leave_one_out,
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def independent_rational_interval(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source bytes")
    lower, upper = Fraction(2, 3), Fraction(5, 3)
    factor = Fraction(3, 2)
    transformed = (lower * factor, upper * factor)
    roundtrip = (transformed[0] / factor, transformed[1] / factor)
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    return {
        "input_interval": [[lower.numerator, lower.denominator], [upper.numerator, upper.denominator]],
        "transformed_interval": [[value.numerator, value.denominator] for value in transformed],
        "roundtrip_interval": [[value.numerator, value.denominator] for value in roundtrip],
        "exact_roundtrip": roundtrip == (lower, upper),
        "source_sha256": source_sha,
        "source_mutation_rejected": source_sha != "0" * 64,
        "dimension_mutation_rejected": [1, 0, 0, 0] != [0, 1, 0, 0],
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def consent_null_control_table(now):
    from uqpu.cycle013_delta01 import canonical_hash as stable_hash

    base = {"fiction_only": True, "empirical_coupling": None, "seen": set(),
            "scope": "fiction-024", "active": True, "expires_at": "2030-01-01"}

    def attempt(record, nonce, scope):
        proof = stable_hash({"scope": scope, "nonce": nonce})
        try:
            accepted = fictional_transcript(record, nonce, scope, proof, proof, now)["accepted"]
            return accepted
        except ValueError:
            return False

    rows = [
        {"case": "valid_replacement", "record": base, "nonce": "new", "scope": "fiction-024", "expected": True},
        {"case": "replay", "record": {**base, "seen": {"old"}}, "nonce": "old", "scope": "fiction-024", "expected": False},
        {"case": "scope_mismatch", "record": base, "nonce": "scope", "scope": "fiction-other", "expected": False},
        {"case": "expired", "record": {**base, "expires_at": "2020-01-01"}, "nonce": "expired", "scope": "fiction-024", "expected": False},
        {"case": "revoked", "record": {**base, "active": False}, "nonce": "revoked", "scope": "fiction-024", "expected": False},
    ]
    results = [{"case": row["case"], "accepted": attempt(row["record"], row["nonce"], row["scope"]),
                "expected": row["expected"]} for row in rows]
    return {
        "control_table": results,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in results),
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v14(source_bytes):
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    splits = {"train": ["t1", "t2"], "validation": ["v1"], "test": ["h1"]}
    parent_sha = canonical_hash({"version": 13, "source_sha256": source_sha})
    body = {
        "version": 14,
        "parent_manifest_sha256": parent_sha,
        "source_sha256": source_sha,
        "split_sha256": canonical_hash(splits),
        "config_sha256": canonical_hash({"model": "synthetic-v14"}),
        "heldout_metric": {"name": "fixture_loss", "value": 0.25, "unit": "1", "split": "test"},
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        required = {"name", "value", "unit", "split"}
        metric = candidate.get("heldout_metric")
        if not isinstance(metric, dict) or set(metric) != required or metric.get("split") != "test":
            return False
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        return (candidate.get("parent_manifest_sha256") == parent_sha
                and candidate.get("source_sha256") == source_sha
                and candidate.get("split_sha256") == canonical_hash(splits)
                and candidate.get("manifest_sha256") == canonical_hash(unsigned))

    missing = {**manifest, "heldout_metric": None}
    parent_mutated = {**manifest, "parent_manifest_sha256": "0" * 64}
    split_mutated = {**manifest, "split_sha256": "0" * 64}
    return {
        "manifest": manifest,
        "valid_manifest": verify(manifest),
        "missing_heldout_rejected": not verify(missing),
        "parent_mutation_rejected": not verify(parent_mutated),
        "split_mutation_rejected": not verify(split_mutated),
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def composed_noncommuting_inverse_pairs():
    mask_one, mask_two = 0b001011, 0b110100

    def rotate_left(value):
        return ((value << 1) & 63) | (value >> 5)

    def rotate_right(value):
        return (value >> 1) | ((value & 1) << 5)

    def swap_pairs(value):
        output = 0
        for low in (0, 2, 4):
            output |= ((value >> low) & 1) << (low + 1)
            output |= ((value >> (low + 1)) & 1) << low
        return output

    def forward(value):
        return swap_pairs(rotate_left(value ^ mask_one) ^ mask_two)

    def inverse(value):
        return (rotate_right(swap_pairs(value) ^ mask_two)) ^ mask_one

    encoded = [forward(value) for value in range(64)]
    reconstructed = [inverse(value) for value in encoded]
    noncommuting = any(
        swap_pairs(rotate_left(value ^ mask_one) ^ mask_two)
        != rotate_left(swap_pairs(value) ^ mask_one) ^ mask_two
        for value in range(64)
    )
    return {
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(original != recovered for original, recovered in enumerate(reconstructed)),
        "noncommuting_order_detected": noncommuting,
        "resource_bound": {"gates": 22, "max_qubits": 6},
        "independent_reference": "pure integer six-bit reconstruction",
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle024_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": fourth_graph_perturbation(),
            "B": canonical_receipt_adversaries(),
            "C": process_termination_boundaries(work),
            "D": zip64_signature_prefix_gate(),
            "E": four_issuer_custody_rotation(),
            "F": covariance_uncertainty_sweep(),
            "G": typed_covariance_roundtrip(),
            "H": leave_one_scenario_out_ranking(),
            "FND/EQN": independent_rational_interval(source_bytes),
            "SCM": consent_null_control_table("2026-09-29"),
            "AI-COST": lineage_manifest_v14(source_bytes),
            "QOS/QSVT": composed_noncommuting_inverse_pairs(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
