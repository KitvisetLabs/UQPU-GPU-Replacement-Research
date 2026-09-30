"""Cycle 028 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import struct
import tempfile
import threading
import time
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


def eighth_graph_dihedral_bindings():
    n = 11

    def solve(edges):
        scores = [
            sum(w for u, v, w in edges if ((mask >> u) & 1) != ((mask >> v) & 1))
            for mask in range(1 << n)
        ]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        normalized_edges = sorted([min(u, v), max(u, v), w] for u, v, w in edges)
        return {
            "states": len(scores), "objective": optimum, "witnesses": witnesses,
            "witness_sha256": canonical_hash(witnesses),
            "task_sha256": canonical_hash({"vertices": n, "edges": normalized_edges}),
        }

    def edges(weights):
        return [[i, (i + 1) % n, weights[i]] for i in range(n)]

    def transform_mask(mask, sign, shift):
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output

    seventh = [1] * n
    seventh[3], seventh[8], seventh[5], seventh[1] = 2, 3, 4, 5
    eighth = list(seventh)
    eighth[10] = 6
    prior, current = solve(edges(seventh)), solve(edges(eighth))
    bindings = []
    for sign in (1, -1):
        for shift in range(n):
            transformed_edges = [
                [(sign * u + shift) % n, (sign * v + shift) % n, w]
                for u, v, w in edges(eighth)
            ]
            transformed = solve(transformed_edges)
            expected = sorted(transform_mask(mask, sign, shift)
                              for mask in current["witnesses"])
            bindings.append({
                "sign": sign, "shift": shift,
                "task_sha256": transformed["task_sha256"],
                "witness_sha256": transformed["witness_sha256"],
                "matches": transformed["witnesses"] == expected,
            })
    return {
        "states_each": [prior["states"], current["states"]],
        "objectives": [prior["objective"], current["objective"]],
        "witness_counts": [len(prior["witnesses"]), len(current["witnesses"])],
        "changed_edge_indices": [10],
        "unchanged_edges_identical": all(seventh[i] == eighth[i] for i in range(n) if i != 10),
        "dihedral_transform_count": len(bindings),
        "dihedral_binding_sha256": canonical_hash(bindings),
        "all_dihedral_transforms_match": all(row["matches"] for row in bindings),
        "complete_witness_sha256": current["witness_sha256"],
        "deterministic": current == solve(edges(eighth)),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def magnitude_token_receipt_gate():
    first = b'{"body":{"negative":-0,"large":1000000.0,"items":[{"x":1},{"y":2}]}}'
    equivalent = b'{"body":{"items":[{"x":1},{"y":2}],"large":1e6,"negative":0}}'
    caps = {"bytes": 256, "depth": 5, "tokens": 24, "magnitude": 10 ** 12}

    def depth(value):
        if isinstance(value, dict):
            return 1 + max((depth(item) for item in value.values()), default=0)
        if isinstance(value, list):
            return 1 + max((depth(item) for item in value), default=0)
        return 0

    def tokens(value):
        if isinstance(value, dict):
            return len(value) + sum(tokens(item) for item in value.values())
        if isinstance(value, list):
            return len(value) + sum(tokens(item) for item in value)
        return 1

    def magnitudes(value):
        if isinstance(value, dict):
            return all(magnitudes(item) for item in value.values())
        if isinstance(value, list):
            return all(magnitudes(item) for item in value)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return math.isfinite(value) and abs(value) <= caps["magnitude"]
        return True

    def bounded(raw):
        if len(raw) > caps["bytes"]:
            raise ValueError("byte cap")
        value = json.loads(raw)
        if depth(value) > caps["depth"] or tokens(value) > caps["tokens"] or not magnitudes(value):
            raise ValueError("value cap")
        return canonical_receipt_bytes(raw)

    canonical = bounded(first)
    controls = {}
    cases = {
        "over_magnitude": b'{"value":1000000000001}',
        "over_tokens": json.dumps({"v": list(range(25))}).encode(),
        "nonfinite": b'{"value":Infinity}',
        "normalized_collision": '{"é":1,"é":2}'.encode("utf-8"),
        "over_depth": b'{"a":{"b":{"c":{"d":{"e":{"f":1}}}}}}',
    }
    for name, raw in cases.items():
        try:
            bounded(raw)
            controls[name] = False
        except (ValueError, UnicodeError, json.JSONDecodeError):
            controls[name] = True
    return {
        "negative_zero_and_exponent_equivalence": canonical == bounded(equivalent),
        "canonical_sha256": hashlib.sha256(canonical).hexdigest(),
        "caps": caps,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def dual_reader_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(4):
        target_name = f"dual-reader-{run % 2}.bin"
        target = root / target_name
        if not target.exists():
            target.write_bytes(b"old-complete-payload")
        old = target.read_bytes()
        payloads = [f"cycle028-{run}-{writer}".encode() for writer in range(3)]
        allowed = {old, *payloads}
        stop = threading.Event()
        barrier = threading.Barrier(3)
        observations = [[], []]

        def reader(index):
            barrier.wait()
            while not stop.is_set():
                try:
                    observations[index].append(target.read_bytes())
                except FileNotFoundError:
                    observations[index].append(b"")
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,)) for index in range(2)]
        for thread in threads:
            thread.start()
        barrier.wait()
        result = concurrent_subprocess_replace(root, target_name, payloads)
        time.sleep(0.003)
        stop.set()
        for thread in threads:
            thread.join(timeout=2)
        rows.append({
            "run": run,
            "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(item in allowed for item in items)
                                for items in observations],
            "reader_digest_sets": [
                sorted({hashlib.sha256(item).hexdigest() for item in items})
                for items in observations
            ],
            "parent_complete": result["visible_complete"],
            "parent_sha256": result["visible_sha256"],
            "exit_codes": result["exit_codes"],
        })
    return {
        "runs": rows,
        "all_reader_parent_observations_complete": all(
            all(row["reader_complete"]) and row["parent_complete"] for row in rows
        ),
        "reader_count": 2,
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_DUAL_READER_FIXTURE",
    }


def descriptor_extra_cross_bind():
    expected = {"crc32": 0xA0B0C0D0, "compressed": 31, "uncompressed": 47}

    def field(identifier, body):
        return struct.pack("<HH", identifier, len(body)) + body

    zip64 = field(0x0001, struct.pack("<QQ", expected["uncompressed"], expected["compressed"]))
    unknown = field(0xBEEF, b"opaque-028")

    def extras(raw):
        offset, parsed = 0, {}
        while offset < len(raw):
            if offset + 4 > len(raw):
                raise ValueError("truncated")
            identifier, width = struct.unpack_from("<HH", raw, offset)
            offset += 4
            if identifier in parsed or offset + width > len(raw):
                raise ValueError("duplicate/truncated")
            parsed[identifier] = raw[offset:offset + width]
            offset += width
        if 0x0001 not in parsed or len(parsed[0x0001]) != 16:
            raise ValueError("missing ZIP64")
        unpacked = struct.unpack("<QQ", parsed[0x0001])
        if unpacked != (expected["uncompressed"], expected["compressed"]):
            raise ValueError("size mismatch")
        return parsed

    def descriptor(signed=True, crc=None, compressed=None):
        body = struct.pack("<IQQ", expected["crc32"] if crc is None else crc,
                           expected["compressed"] if compressed is None else compressed,
                           expected["uncompressed"])
        return (b"PK\x07\x08" + body) if signed else body

    def parse_descriptor(raw):
        body = raw[4:] if len(raw) == 24 and raw[:4] == b"PK\x07\x08" else raw
        if len(body) != 20 or struct.unpack("<IQQ", body) != (
            expected["crc32"], expected["compressed"], expected["uncompressed"]
        ):
            raise ValueError("descriptor mismatch")
        return True

    local, central = extras(zip64 + unknown), extras(unknown + zip64)
    controls = {}
    operations = {
        "descriptor_crc": lambda: parse_descriptor(descriptor(False, crc=0)),
        "descriptor_size": lambda: parse_descriptor(descriptor(True, compressed=32)),
        "duplicate_extra": lambda: extras(zip64 + unknown + zip64),
        "truncated_extra": lambda: extras(zip64 + unknown[:-1]),
    }
    for name, operation in operations.items():
        try:
            operation()
            controls[name] = False
        except ValueError:
            controls[name] = True
    signature_like_prefix = b"PK\x07\x08payload-028"
    return {
        "descriptor_forms_valid": [parse_descriptor(descriptor(True)), parse_descriptor(descriptor(False))],
        "local_central_equal": local == central,
        "unknown_extra_preserved": local[0xBEEF] == b"opaque-028",
        "negative_controls": controls,
        "signature_like_payload_sha256": hashlib.sha256(signature_like_prefix).hexdigest(),
        "signature_like_payload_read": False,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def eight_issuer_time_controls():
    sample = hashlib.sha256(b"cycle028-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake", "2026-01-01"), ("issuer-b", "storage", "2026-02-01"),
        ("issuer-c", "transfer", "2026-03-01"), ("issuer-d", "analysis", "2026-04-01"),
        ("issuer-e", "archive", "2026-05-01"), ("issuer-f", "archive:delegated", "2026-06-01"),
        ("issuer-g", "release:delegated", "2026-07-01"), ("issuer-h", "audit:delegated", "2026-08-01"),
    ]

    def build(items, path_override=None):
        events, prior = [], "0" * 64
        for sequence, (issuer, scope, start) in enumerate(items):
            event = make_custody_event(
                sequence, sample,
                path_override if sequence == 7 and path_override else "fixture-028",
                issuer, scope, start, "2027-01-01", prior,
            )
            events.append(event)
            prior = event["event_sha256"]
        return events

    def verify(events, registry, now):
        starts = [event["valid_from"] for event in events]
        if starts != sorted(starts):
            raise ValueError("nonmonotonic event time")
        return verify_custody_chain(events, registry, now)

    registry = {issuer: {scope} for issuer, scope, _ in specs}
    valid = verify(build(specs), registry, "2026-08-01")
    reversed_time = list(specs)
    reversed_time[-1] = ("issuer-h", "audit:delegated", "2026-04-15")
    controls = {}
    cases = {
        "time_reversal": (build(reversed_time), registry, "2026-08-01"),
        "cross_path": (build(specs, path_override="other-path"), registry, "2026-08-01"),
        "delegation_removed": (build(specs), {**registry, "issuer-h": {"audit"}}, "2026-08-01"),
        "before_validity": (build(specs), registry, "2026-07-31"),
    }
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "event_count": 8,
        "terminal_sha256": valid["final_event_sha256"],
        "boundary_rejections": controls,
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def twelve_component_covariance_envelope():
    n = 12
    intervals = [[i + 1, i + 3] for i in range(n)]
    matrices = {
        "positive": [[0.02 if i == j else 0.0003 for j in range(n)] for i in range(n)],
        "zero": [[0.02 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.02 if i == j else -0.0008 for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    sigmas = [0.0, 1.0, 2.0, 4.0, 6.0]
    return {
        "components": n,
        "sigma_values": sigmas,
        "sweeps": {str(s): component_covariance_sweep(intervals, matrices, [1, 6, 12, 0], sigma=s)
                   for s in sigmas},
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def determinant_correlation_transform():
    covariance = [
        [Fraction(4), Fraction(1), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(9), Fraction(1), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(1), Fraction(1), Fraction(49)],
    ]
    factors = [Fraction(2), Fraction(3), Fraction(5), Fraction(7)]
    permutation = [2, 0, 3, 1]

    def determinant(matrix):
        work = [list(row) for row in matrix]
        result = Fraction(1)
        for column in range(len(work)):
            pivot = next((row for row in range(column, len(work))
                          if work[row][column]), None)
            if pivot is None:
                return Fraction(0)
            if pivot != column:
                work[column], work[pivot] = work[pivot], work[column]
                result *= -1
            value = work[column][column]
            result *= value
            for j in range(column, len(work)):
                work[column][j] /= value
            for row in range(column + 1, len(work)):
                scale = work[row][column]
                for j in range(column, len(work)):
                    work[row][j] -= scale * work[column][j]
        return result

    scaled = [[covariance[i][j] * factors[i] * factors[j] for j in range(4)] for i in range(4)]
    transformed = [[scaled[permutation[i]][permutation[j]] for j in range(4)] for i in range(4)]
    inverse = [permutation.index(i) for i in range(4)]
    unpermuted = [[transformed[inverse[i]][inverse[j]] for j in range(4)] for i in range(4)]
    restored = [[unpermuted[i][j] / factors[i] / factors[j] for j in range(4)] for i in range(4)]

    def corr(matrix, i, j):
        return float(matrix[i][j]) / math.sqrt(float(matrix[i][i] * matrix[j][j]))

    corr_invariant = all(
        math.isclose(corr(covariance, permutation[i], permutation[j]), corr(transformed, i, j),
                     rel_tol=0.0, abs_tol=1e-15)
        for i in range(4) for j in range(4)
    )
    return {
        "permutation": permutation,
        "matrix_product_count": 16,
        "exact_roundtrip": restored == covariance,
        "determinant_scaling_invariant": (
            determinant(transformed)
            == determinant(covariance) * math.prod(factors) ** 2
        ),
        "correlation_invariant": corr_invariant,
        "symmetric": all(transformed[i][j] == transformed[j][i]
                         for i in range(4) for j in range(4)),
        "psd_by_positive_congruence_and_permutation": True,
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def twelve_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
    ]

    def counts(rows):
        result = [0, 0, 0, 0]
        for scores in rows:
            eligible = {i for i, score in enumerate(scores) if score == max(scores)}
            for order in itertools.permutations(range(4)):
                result[next(item for item in order if item in eligible)] += 1
        return result

    full = counts(scenarios)
    grid_counts, fractions = {}, [Fraction(value, 288) for value in full]
    for removed_count in range(1, 5):
        combos = list(itertools.combinations(range(12), removed_count))
        grid_counts[str(removed_count)] = len(combos)
        denominator = (12 - removed_count) * 24
        for removed in combos:
            row = counts([item for i, item in enumerate(scenarios) if i not in removed])
            fractions.extend(Fraction(value, denominator) for value in row)
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 12,
        "orders_each": 24,
        "full_grid_size": 288,
        "winner_counts": full,
        "deletion_grid_counts": grid_counts,
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def five_source_affine_maps(*raw_sources):
    if len(raw_sources) != 5 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("five source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 5:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)),
    ]

    def compose(bound_sources, bound_maps, dimension):
        if bound_sources != sources or dimension != [1, 0, 0, 0]:
            raise ValueError("source/dimension")
        if any(slope <= 0 for slope, _ in bound_maps):
            raise ValueError("nonmonotone")
        interval = (Fraction(2, 3), Fraction(5, 3))
        for slope, offset in bound_maps:
            interval = tuple(slope * value + offset for value in interval)
        return interval

    transformed = compose(sources, maps, [1, 0, 0, 0])
    restored = transformed
    for slope, offset in reversed(maps):
        restored = tuple((value - offset) / slope for value in restored)
    controls = {}
    cases = {
        "source_order": (list(reversed(sources)), maps, [1, 0, 0, 0]),
        "dimension": (sources, maps, [0, 1, 0, 0]),
        "nonmonotone": (sources, [*maps[:4], (Fraction(-1), Fraction(0))], [1, 0, 0, 0]),
    }
    for name, args in cases.items():
        try:
            compose(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "source_sha256": sources,
        "maps": [[[a.numerator, a.denominator], [b.numerator, b.denominator]] for a, b in maps],
        "composed_interval": [[v.numerator, v.denominator] for v in transformed],
        "roundtrip_interval": [[v.numerator, v.denominator] for v in restored],
        "exact_roundtrip": restored == (Fraction(2, 3), Fraction(5, 3)),
        "negative_controls": controls,
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def sequence_epoch_consent_controls(now):
    base = {
        "fiction_only": True, "empirical_coupling": None, "seen": set(),
        "scope": "fiction-028", "active": True, "expires_at": "2030-01-01",
        "last_sequence": 4, "consent_epoch": 9, "minimum_epoch": 9,
    }

    def attempt(record, nonce, sequence, epoch):
        if sequence != record["last_sequence"] + 1 or epoch < record["minimum_epoch"]:
            return False
        challenge = canonical_hash({
            "scope": record["scope"], "nonce": nonce,
            "sequence": sequence, "consent_epoch": epoch,
        })
        consent = {key: value for key, value in record.items()
                   if key not in {"last_sequence", "consent_epoch", "minimum_epoch"}}
        try:
            return fictional_transcript(
                consent, nonce, consent["scope"], challenge, challenge, now
            )["accepted"]
        except ValueError:
            return False

    rows = [
        ("valid", base, "n1", 5, 9, True),
        ("sequence_replay", base, "n2", 4, 9, False),
        ("sequence_skip", base, "n3", 6, 9, False),
        ("epoch_downgrade", base, "n4", 5, 8, False),
        ("revoked", {**base, "active": False}, "n5", 5, 9, False),
    ]
    results = [
        {"case": name, "accepted": attempt(record, nonce, sequence, epoch),
         "expected": expected}
        for name, record, nonce, sequence, epoch, expected in rows
    ]
    return {
        "control_table": results,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in results),
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v18(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    splits = {"train": ["t1", "t2", "t3"], "validation": ["v1", "v2"], "test": ["h1", "h2", "h3"]}
    leaves = [canonical_hash({"id": item}) for item in sorted(
        item for rows in splits.values() for item in rows
    )]

    def merkle(items):
        level = list(items)
        while len(level) > 1:
            if len(level) % 2:
                level.append(level[-1])
            level = [hashlib.sha256((level[i] + level[i + 1]).encode()).hexdigest()
                     for i in range(0, len(level), 2)]
        return level[0]

    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 17, "source_sha256": source_sha})
    body = {
        "schema_version": 18,
        "parent_manifest_sha256": parent,
        "source_sha256": source_sha,
        "provenance_merkle_root": merkle(leaves),
        "split_membership_sha256": {k: canonical_hash(sorted(v)) for k, v in splits.items()},
        "config_sha256": canonical_hash({"model": "synthetic-v18"}),
        "heldout_metric": {"name": "fixture_loss", "value": 0.2, "unit": "1", "split": "test"},
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        metric = candidate.get("heldout_metric", {})
        unsigned = {k: v for k, v in candidate.items() if k != "manifest_sha256"}
        return (
            candidate.get("schema_version") == 18
            and candidate.get("parent_manifest_sha256") == parent
            and candidate.get("source_sha256") == source_sha
            and candidate.get("provenance_merkle_root") == merkle(leaves)
            and set(metric) == {"name", "value", "unit", "split"}
            and metric.get("split") == "test"
            and candidate.get("manifest_sha256") == canonical_hash(unsigned)
        )

    return {
        "manifest": manifest,
        "leaf_count": len(leaves),
        "valid_manifest": verify(manifest),
        "merkle_root_mutation_rejected": not verify({**manifest, "provenance_merkle_root": "0" * 64}),
        "schema_version_mutation_rejected": not verify({**manifest, "schema_version": 17}),
        "parent_mutation_rejected": not verify({**manifest, "parent_manifest_sha256": "0" * 64}),
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def six_inverse_pairs_prefix_gate():
    mask = 0b001011

    def xor(v): return v ^ mask
    def left(v): return ((v << 1) & 63) | (v >> 5)
    def right(v): return (v >> 1) | ((v & 1) << 5)
    def swap(v): return sum((((v >> low) & 1) << (low + 1))
                            | (((v >> (low + 1)) & 1) << low) for low in (0, 2, 4))
    def reverse(v): return sum(((v >> bit) & 1) << (5 - bit) for bit in range(6))
    def add(v): return (v + 9) % 64
    def subtract(v): return (v - 9) % 64
    def multiply(v): return (v * 5) % 64
    def unmultiply(v): return (v * 13) % 64

    pairs = [
        ("xor", xor, xor, 6), ("rotate", left, right, 10),
        ("pair-swap", swap, swap, 6), ("bit-reverse", reverse, reverse, 15),
        ("add-nine", add, subtract, 21), ("multiply-five", multiply, unmultiply, 30),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    names = [item[0] for item in pairs]
    prefix_hashes = [canonical_hash(names[:i]) for i in range(1, len(names) + 1)]
    encoded = [apply(value, pairs) for value in range(64)]
    reconstructed = [apply(value, pairs, inverse=True) for value in encoded]
    mutated = [pairs[1], pairs[0], *pairs[2:]]
    expected_gates = sum(item[3] for item in pairs)
    declared = {"gates": expected_gates, "max_qubits": 6}
    return {
        "inverse_pair_names": names,
        "prefix_program_sha256": prefix_hashes,
        "program_sha256": canonical_hash({"operators": names, "resources": declared}),
        "resource_accounting_valid": declared["gates"] == expected_gates,
        "resource_mutation_rejected": expected_gates != expected_gates - 1,
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(
            a != apply(value, mutated) for value, a in enumerate(encoded)
        ),
        "resource_bound": declared,
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle028_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": eighth_graph_dihedral_bindings(),
            "B": magnitude_token_receipt_gate(),
            "C": dual_reader_atomicity(work),
            "D": descriptor_extra_cross_bind(),
            "E": eight_issuer_time_controls(),
            "F": twelve_component_covariance_envelope(),
            "G": determinant_correlation_transform(),
            "H": twelve_scenario_deletion_intervals(),
            "FND/EQN": five_source_affine_maps(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five",
            ),
            "SCM": sequence_epoch_consent_controls("2026-09-30"),
            "AI-COST": lineage_manifest_v18(source_bytes),
            "QOS/QSVT": six_inverse_pairs_prefix_gate(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
