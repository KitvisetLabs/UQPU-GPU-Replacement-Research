"""Cycle 030 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
import struct
import tempfile
import threading
import time
from fractions import Fraction
from pathlib import Path

from uqpu.cycle013_delta01 import canonical_hash
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


def tenth_graph_double_orbits():
    n = 11
    full_mask = (1 << n) - 1

    def edges(weights):
        return [[i, (i + 1) % n, weights[i]] for i in range(n)]

    def solve(weights):
        edge_list = edges(weights)
        scores = [
            sum(w for u, v, w in edge_list if ((mask >> u) & 1) != ((mask >> v) & 1))
            for mask in range(1 << n)
        ]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {
            "states": len(scores), "objective": optimum, "witnesses": witnesses,
            "task_sha256": canonical_hash({"vertices": n, "edges": edge_list}),
            "witness_sha256": canonical_hash(witnesses),
        }

    def transform_weights(weights, sign, shift):
        transformed = [0] * n
        for index, value in enumerate(weights):
            u, v = (sign * index + shift) % n, (sign * (index + 1) + shift) % n
            transformed[min(u, v) if abs(u - v) == 1 else max(u, v)] = value
        return transformed

    def transform_mask(mask, sign, shift):
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output

    ninth = [1] * n
    for index, weight in ((0, 1), (1, 5), (3, 2), (5, 4), (7, 7), (8, 3), (10, 6)):
        ninth[index] = weight
    tenth = list(ninth)
    tenth[0] = 8
    prior, current = solve(ninth), solve(tenth)
    transforms, stabilizer = [], []
    for sign in (1, -1):
        for shift in range(n):
            transformed_weights = transform_weights(tenth, sign, shift)
            transformed = solve(transformed_weights)
            expected = sorted(transform_mask(mask, sign, shift) for mask in current["witnesses"])
            transforms.append({"sign": sign, "shift": shift, "matches": transformed["witnesses"] == expected,
                               "task_sha256": transformed["task_sha256"],
                               "witness_sha256": transformed["witness_sha256"]})
            if transformed_weights == tenth:
                stabilizer.append((sign, shift))
    remaining = set(current["witnesses"])
    double_orbits = []
    while remaining:
        seed = min(remaining)
        orbit = set()
        for sign, shift in stabilizer:
            transformed = transform_mask(seed, sign, shift)
            orbit.update((transformed, transformed ^ full_mask))
        bounded = sorted(orbit & set(current["witnesses"]))
        double_orbits.append(bounded)
        remaining.difference_update(bounded)
    return {
        "states_each": [prior["states"], current["states"]],
        "objectives": [prior["objective"], current["objective"]],
        "witness_counts": [len(prior["witnesses"]), len(current["witnesses"])],
        "changed_edge_indices": [0],
        "unchanged_edges_identical": all(ninth[i] == tenth[i] for i in range(n) if i != 0),
        "dihedral_transform_count": len(transforms),
        "all_dihedral_transforms_match": all(row["matches"] for row in transforms),
        "stabilizer": [[sign, shift] for sign, shift in stabilizer],
        "complement_stabilizer_double_orbits": double_orbits,
        "double_orbit_sha256": canonical_hash(double_orbits),
        "complete_witness_sha256": current["witness_sha256"],
        "deterministic": current == solve(tenth),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def integer_escaped_key_receipt_gate():
    first = b'{"body":{"a":1,"max_int":9007199254740991,"negative":-0}}'
    equivalent = b'{"body":{"negative":0,"max_int":9007199254740991,"\\u0061":1}}'
    caps = {"bytes": 256, "depth": 5, "tokens": 24,
            "max_exact_integer": 2 ** 53 - 1, "magnitude": 10 ** 12}

    def pairs(items):
        output = {}
        for key, value in items:
            if key in output:
                raise ValueError("duplicate decoded key")
            output[key] = value
        return output

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

    def numbers(value):
        if isinstance(value, dict):
            return all(numbers(item) for item in value.values())
        if isinstance(value, list):
            return all(numbers(item) for item in value)
        if isinstance(value, int) and not isinstance(value, bool):
            return abs(value) <= caps["max_exact_integer"]
        if isinstance(value, float):
            return math.isfinite(value) and abs(value) <= caps["magnitude"]
        return True

    def bounded(raw):
        if len(raw) > caps["bytes"]:
            raise ValueError("byte cap")
        value = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                           parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
        if depth(value) > caps["depth"] or tokens(value) > caps["tokens"] or not numbers(value):
            raise ValueError("value cap")
        normalized = json.dumps(value, sort_keys=True, separators=(",", ":"),
                                ensure_ascii=False, allow_nan=False).encode("utf-8")
        return canonical_receipt_bytes(normalized)

    canonical = bounded(first)
    cases = {
        "integer_precision": b'{"a":9007199254740992}',
        "escaped_duplicate": b'{"a":1,"\\u0061":2}',
        "literal_duplicate": b'{"a":1,"a":2}',
        "nonfinite": b'{"a":Infinity}',
        "float_magnitude": b'{"a":1e13}',
        "token_cap": json.dumps({"v": list(range(25))}).encode(),
    }
    controls = {}
    for name, raw in cases.items():
        try:
            bounded(raw)
            controls[name] = False
        except (ValueError, UnicodeError, json.JSONDecodeError):
            controls[name] = True
    return {
        "escaped_key_equivalence": canonical == bounded(equivalent),
        "canonical_sha256": hashlib.sha256(canonical).hexdigest(),
        "caps": caps,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def four_reader_directory_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(4):
        target_name = f"four-reader-{run % 2}.bin"
        target = root / target_name
        if not target.exists():
            target.write_bytes(b"old-complete-payload")
        old = target.read_bytes()
        payloads = [f"cycle030-{run}-{writer}".encode() for writer in range(3)]
        allowed = {old, *payloads}
        pre_names = sorted(path.name for path in root.iterdir())
        pre_inode = target.stat().st_ino
        stop = threading.Event()
        barrier = threading.Barrier(5)
        observations = [[], [], [], []]

        def reader(index):
            barrier.wait()
            while not stop.is_set():
                try:
                    observations[index].append((target.read_bytes(), target.name, target.stat().st_ino))
                except FileNotFoundError:
                    observations[index].append((b"", target.name, -1))
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,)) for index in range(4)]
        for thread in threads:
            thread.start()
        barrier.wait()
        result = concurrent_subprocess_replace(root, target_name, payloads)
        time.sleep(0.003)
        stop.set()
        for thread in threads:
            thread.join(timeout=2)
        post_names = sorted(path.name for path in root.iterdir())
        rows.append({
            "run": run,
            "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(data in allowed and name == target_name
                                                     for data, name, _ in items)
                                for items in observations],
            "pre_directory_names": pre_names,
            "post_directory_names": post_names,
            "pre_inode": pre_inode,
            "post_inode": target.stat().st_ino,
            "parent_complete": result["visible_complete"],
            "parent_sha256": result["visible_sha256"],
            "exit_codes": result["exit_codes"],
        })
    return {
        "runs": rows,
        "reader_count": 4,
        "all_reader_parent_observations_complete": all(
            all(row["reader_complete"]) and row["parent_complete"] for row in rows
        ),
        "all_targets_declared": all(
            f"four-reader-{row['run'] % 2}.bin" in row["pre_directory_names"]
            and f"four-reader-{row['run'] % 2}.bin" in row["post_directory_names"]
            for row in rows
        ),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_FOUR_READER_FIXTURE",
    }


def zip64_local_central_full_bind():
    expected = {"version": 45, "flags": 0x08, "method": 8,
                "crc32": 0xA0B0C0D0, "compressed": 41, "uncompressed": 59}

    def header(version=45, flags=0x08, method=8):
        return struct.pack("<HHH", version, flags, method)

    def extra(identifier, body):
        return struct.pack("<HH", identifier, len(body)) + body

    zip64 = extra(0x0001, struct.pack("<QQ", expected["uncompressed"], expected["compressed"]))
    opaque = extra(0xCAFE, b"opaque-030")

    def extras(raw):
        offset, output = 0, {}
        while offset < len(raw):
            if offset + 4 > len(raw):
                raise ValueError("truncated")
            identifier, width = struct.unpack_from("<HH", raw, offset)
            offset += 4
            if identifier in output or offset + width > len(raw):
                raise ValueError("duplicate/truncated")
            output[identifier] = raw[offset:offset + width]
            offset += width
        if 0x0001 not in output or len(output[0x0001]) != 16:
            raise ValueError("zip64")
        if struct.unpack("<QQ", output[0x0001]) != (expected["uncompressed"], expected["compressed"]):
            raise ValueError("sizes")
        return output

    def descriptor(signed=True, crc=None, compressed=None):
        body = struct.pack("<IQQ", expected["crc32"] if crc is None else crc,
                           expected["compressed"] if compressed is None else compressed,
                           expected["uncompressed"])
        return (b"PK\x07\x08" + body) if signed else body

    def verify(local_header, central_header, raw_descriptor, local_extra, central_extra):
        local_fields = struct.unpack("<HHH", local_header)
        central_fields = struct.unpack("<HHH", central_header)
        if local_fields != central_fields or local_fields != (
            expected["version"], expected["flags"], expected["method"]
        ):
            raise ValueError("header")
        body = raw_descriptor[4:] if len(raw_descriptor) == 24 and raw_descriptor[:4] == b"PK\x07\x08" else raw_descriptor
        if len(body) != 20 or struct.unpack("<IQQ", body) != (
            expected["crc32"], expected["compressed"], expected["uncompressed"]
        ):
            raise ValueError("descriptor")
        return extras(local_extra) == extras(central_extra)

    valid_args = (header(), header(), descriptor(), zip64 + opaque, opaque + zip64)
    cases = {
        "version": (header(version=20), *valid_args[1:]),
        "flags": (header(flags=0), *valid_args[1:]),
        "method": (header(method=0), *valid_args[1:]),
        "central_mismatch": (header(), header(method=0), *valid_args[2:]),
        "descriptor_crc": (header(), header(), descriptor(crc=0), *valid_args[3:]),
        "descriptor_size": (header(), header(), descriptor(compressed=42), *valid_args[3:]),
        "duplicate_extra": (header(), header(), descriptor(), zip64 + opaque + zip64, opaque + zip64),
        "truncated_extra": (header(), header(), descriptor(), zip64 + opaque[:-1], opaque + zip64),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, struct.error):
            controls[name] = True
    return {
        "signed_unsigned_valid": [verify(*valid_args), verify(header(), header(), descriptor(False), zip64 + opaque, opaque + zip64)],
        "unknown_extra_preserved": extras(zip64 + opaque)[0xCAFE] == b"opaque-030",
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def ten_issuer_two_level_revocation():
    sample = hashlib.sha256(b"cycle030-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer"),
        ("issuer-d", "analysis"), ("issuer-e", "archive"),
        ("issuer-f", "archive:delegated"), ("issuer-g", "release:delegated"),
        ("issuer-h", "audit:delegated"), ("issuer-i", "audit:subdelegated"),
        ("issuer-j", "review:subdelegated"),
    ]
    starts = [f"2026-{month:02d}-01" for month in range(1, 11)]

    def build(path="fixture-030", expiry="2027-01-01"):
        events, prior = [], "0" * 64
        for sequence, ((issuer, scope), start) in enumerate(zip(specs, starts)):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       start, expiry, prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-j": "issuer-i", "issuer-i": "issuer-h"}

    def verify(events, bound_registry, primary_revocation=11, ancestor_revocation=12,
               bound_ancestry=ancestry, now="2026-10-01"):
        if primary_revocation <= events[-1]["sequence"] or ancestor_revocation <= events[-1]["sequence"]:
            raise ValueError("revoked")
        if any(event["path_id"] != "fixture-030" for event in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        if not (max(event["valid_from"] for event in events) <= now
                <= min(event["expires_at"] for event in events)):
            raise ValueError("window")
        return verify_custody_chain(events, bound_registry, now)

    valid = verify(build(), registry)
    cases = {
        "primary_revoked": (build(), registry, 9, 12, ancestry, "2026-10-01"),
        "ancestor_revoked": (build(), registry, 11, 9, ancestry, "2026-10-01"),
        "cross_path": (build("other"), registry, 11, 12, ancestry, "2026-10-01"),
        "scope_removed": (build(), {**registry, "issuer-j": {"review"}}, 11, 12, ancestry, "2026-10-01"),
        "ancestry_changed": (build(), registry, 11, 12, {"issuer-j": "issuer-h", "issuer-i": "issuer-h"}, "2026-10-01"),
        "outside_intersection": (build(), registry, 11, 12, ancestry, "2026-09-30"),
    }
    controls = {}
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "event_count": 10,
        "terminal_sha256": valid["final_event_sha256"],
        "boundary_rejections": controls,
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def fourteen_component_covariance_grid(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 14
    intervals = [[i + 1, i + 4] for i in range(n)]
    matrices = {
        "positive": [[0.02 if i == j else 0.0002 for j in range(n)] for i in range(n)],
        "zero": [[0.02 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.02 if i == j else -0.0006 for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    identity = canonical_hash({"source_sha256": source_sha, "components": n,
                               "intervals": intervals, "matrix_names": sorted(matrices),
                               "sigmas": sigmas})
    return {
        "components": n,
        "source_sha256": source_sha,
        "covariance_grid_sha256": identity,
        "sigma_values": sigmas,
        "sweeps": {str(s): component_covariance_sweep(intervals, matrices, [1, 7, 14, 0], sigma=s)
                   for s in sigmas},
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def signed_block_covariance_transform():
    covariance = [
        [Fraction(4), Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(9), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1), Fraction(49)],
    ]
    permutation = [1, 0, 3, 2]
    signs = [1, -1, 1, -1]

    def determinant(matrix):
        work = [list(row) for row in matrix]
        output = Fraction(1)
        for col in range(len(work)):
            pivot = next((row for row in range(col, len(work)) if work[row][col]), None)
            if pivot is None:
                return Fraction(0)
            if pivot != col:
                work[col], work[pivot] = work[pivot], work[col]
                output *= -1
            value = work[col][col]
            output *= value
            for j in range(col, len(work)):
                work[col][j] /= value
            for row in range(col + 1, len(work)):
                scale = work[row][col]
                for j in range(col, len(work)):
                    work[row][j] -= scale * work[col][j]
        return output

    transformed = [[signs[i] * signs[j] * covariance[permutation[i]][permutation[j]]
                    for j in range(4)] for i in range(4)]
    inverse = [permutation.index(i) for i in range(4)]
    restored = [[signs[inverse[i]] * signs[inverse[j]] * transformed[inverse[i]][inverse[j]]
                 for j in range(4)] for i in range(4)]

    def corr(matrix, i, j):
        return float(matrix[i][j]) / math.sqrt(float(matrix[i][i] * matrix[j][j]))

    return {
        "block_permutation": permutation,
        "signs": signs,
        "matrix_product_count": 16,
        "exact_roundtrip": restored == covariance,
        "trace_invariant": sum(transformed[i][i] for i in range(4)) == sum(covariance[i][i] for i in range(4)),
        "determinant_invariant": determinant(transformed) == determinant(covariance),
        "signed_correlation_index_invariant": all(
            math.isclose(corr(transformed, i, j),
                         signs[i] * signs[j] * corr(covariance, permutation[i], permutation[j]),
                         rel_tol=0.0, abs_tol=1e-15)
            for i in range(4) for j in range(4)
        ),
        "symmetric": all(transformed[i][j] == transformed[j][i] for i in range(4) for j in range(4)),
        "psd_by_signed_permutation_congruence": True,
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def fourteen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2],
    ]

    def counts(rows):
        output = [0, 0, 0, 0]
        for scores in rows:
            eligible = {i for i, score in enumerate(scores) if score == max(scores)}
            for order in itertools.permutations(range(4)):
                output[next(item for item in order if item in eligible)] += 1
        return output

    full = counts(scenarios)
    fractions = [Fraction(value, 14 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 7):
        combos = list(itertools.combinations(range(14), removed_count))
        grid_counts[str(removed_count)] = len(combos)
        denominator = (14 - removed_count) * 24
        for removed in combos:
            removed_set = set(removed)
            row = counts([item for i, item in enumerate(scenarios) if i not in removed_set])
            fractions.extend(Fraction(value, denominator) for value in row)
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 14,
        "orders_each": 24,
        "full_grid_size": 336,
        "winner_counts": full,
        "deletion_grid_counts": grid_counts,
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def seven_source_affine_maps(*raw_sources):
    if len(raw_sources) != 7 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("seven source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 7:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
        (Fraction(17, 16), Fraction(1, 17)),
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
    cases = {
        "source_order": (list(reversed(sources)), maps, [1, 0, 0, 0]),
        "dimension": (sources, maps, [0, 1, 0, 0]),
        "nonmonotone": (sources, [*maps[:6], (Fraction(-1), Fraction(0))], [1, 0, 0, 0]),
    }
    controls = {}
    for name, args in cases.items():
        try:
            compose(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "source_sha256": sources,
        "map_count": len(maps),
        "composed_interval": [[value.numerator, value.denominator] for value in transformed],
        "roundtrip_interval": [[value.numerator, value.denominator] for value in restored],
        "exact_roundtrip": restored == (Fraction(2, 3), Fraction(5, 3)),
        "negative_controls": controls,
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def transcript_fork_stale_controls():
    def build(audience="fiction-030", epoch=11, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 6):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "payload": f"row-{sequence}", "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows, prior

    def verify(rows, declared_head, audience="fiction-030", minimum_epoch=11):
        prior, seen_parents = "0" * 64, set()
        for expected_sequence, row in enumerate(rows, start=1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            parent_key = (row["sequence"], row["previous_sha256"])
            if (parent_key in seen_parents or row["sequence"] != expected_sequence
                    or row["epoch"] < minimum_epoch or row["audience"] != audience
                    or not row["active"] or row["previous_sha256"] != prior
                    or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            seen_parents.add(parent_key)
            prior = row["row_sha256"]
        return prior == declared_head

    valid, head = build()
    fork_row = dict(valid[2])
    fork_row["payload"] = "fork"
    fork_row["row_sha256"] = canonical_hash({k: v for k, v in fork_row.items() if k != "row_sha256"})
    forked = [*valid[:3], fork_row, *valid[3:]]
    replay = [*valid[:3], valid[2], *valid[4:]]
    skipped = [*valid[:2], *valid[3:]]
    downgraded, downgraded_head = build(epoch=10)
    wrong_audience, wrong_head = build(audience="other")
    revoked, revoked_head = build(active=False)
    table = [
        ("valid", valid, head, True), ("fork", forked, head, False),
        ("stale_head", valid, valid[-2]["row_sha256"], False),
        ("replay", replay, head, False), ("skip", skipped, head, False),
        ("epoch_downgrade", downgraded, downgraded_head, False),
        ("audience", wrong_audience, wrong_head, False),
        ("revoked", revoked, revoked_head, False),
    ]
    controls = [{"case": name, "accepted": verify(rows, declared_head), "expected": expected}
                for name, rows, declared_head, expected in table]
    return {
        "control_table": controls,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in controls),
        "terminal_sha256": head,
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v20(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    members = ["h1", "h2", "h3", "t1", "t2", "t3", "v1", "v2"]
    leaves = [canonical_hash({"id": member}) for member in members]

    def levels(items):
        output = [list(items)]
        while len(output[-1]) > 1:
            row = list(output[-1])
            if len(row) % 2:
                row.append(row[-1])
            output.append([hashlib.sha256((row[i] + row[i + 1]).encode()).hexdigest()
                           for i in range(0, len(row), 2)])
        return output

    tree = levels(leaves)
    root = tree[-1][0]

    def proof(index):
        output = []
        for row in tree[:-1]:
            sibling = index ^ 1
            if sibling >= len(row):
                sibling = index
            output.append({"side": "left" if sibling < index else "right", "sha256": row[sibling]})
            index //= 2
        return output

    def verify_path(leaf, path, expected_root):
        value = leaf
        for item in path:
            value = hashlib.sha256(((item["sha256"] + value) if item["side"] == "left"
                                    else (value + item["sha256"])).encode()).hexdigest()
        return value == expected_root

    inclusion = {member: {"leaf": leaves[i], "path": proof(i)}
                 for i, member in enumerate(members[:3])}
    nonmember = {
        "id": "h2a", "lower_id": "h2", "upper_id": "h3",
        "lower": inclusion["h2"], "upper": inclusion["h3"],
    }
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 19, "source_sha256": source_sha})
    config = canonical_hash({"model": "synthetic-v20"})
    body = {
        "schema_version": 20, "parent_manifest_sha256": parent,
        "source_sha256": source_sha, "provenance_merkle_root": root,
        "heldout_inclusion_paths": inclusion, "nonmembership_fixture": nonmember,
        "config_sha256": config,
        "heldout_metric": {"name": "fixture_loss", "value": 0.18, "unit": "1", "split": "test"},
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        paths = candidate.get("heldout_inclusion_paths", {})
        absent = candidate.get("nonmembership_fixture", {})
        metric = candidate.get("heldout_metric", {})
        return (
            candidate.get("schema_version") == 20
            and candidate.get("parent_manifest_sha256") == parent
            and candidate.get("source_sha256") == source_sha
            and candidate.get("provenance_merkle_root") == root
            and candidate.get("config_sha256") == config
            and set(paths) == {"h1", "h2", "h3"}
            and all(verify_path(item["leaf"], item["path"], root) for item in paths.values())
            and absent.get("lower_id") < absent.get("id") < absent.get("upper_id")
            and absent.get("id") not in members
            and verify_path(absent["lower"]["leaf"], absent["lower"]["path"], root)
            and verify_path(absent["upper"]["leaf"], absent["upper"]["path"], root)
            and set(metric) == {"name", "value", "unit", "split"} and metric.get("split") == "test"
            and candidate.get("manifest_sha256") == canonical_hash(unsigned)
        )

    mutations = {
        "root": {**manifest, "provenance_merkle_root": "0" * 64},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "schema_version": 19},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "heldout_metric": {"name": "fixture_loss", "value": 0.18}},
    }
    path_mutation = json.loads(json.dumps(manifest))
    path_mutation["heldout_inclusion_paths"]["h1"]["path"][0]["sha256"] = "0" * 64
    mutations["path"] = path_mutation
    return {
        "manifest": manifest,
        "leaf_count": len(leaves),
        "heldout_path_count": len(inclusion),
        "valid_manifest": verify(manifest),
        "mutation_rejections": {name: not verify(candidate) for name, candidate in mutations.items()},
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def eight_inverse_pairs_program_tree():
    mask = 0b001011

    def pair_swap(value):
        return sum((((value >> low) & 1) << (low + 1))
                   | (((value >> (low + 1)) & 1) << low) for low in (0, 2, 4))

    def reverse(value):
        return sum(((value >> bit) & 1) << (5 - bit) for bit in range(6))

    operations = [
        ("xor", lambda v: v ^ mask, lambda v: v ^ mask, 6),
        ("rotate", lambda v: ((v << 1) & 63) | (v >> 5), lambda v: (v >> 1) | ((v & 1) << 5), 10),
        ("pair-swap", pair_swap, pair_swap, 6),
        ("bit-reverse", reverse, reverse, 15),
        ("add-nine", lambda v: (v + 9) % 64, lambda v: (v - 9) % 64, 21),
        ("multiply-five", lambda v: (v * 5) % 64, lambda v: (v * 13) % 64, 30),
        ("multiply-twenty-one", lambda v: (v * 21) % 64, lambda v: (v * 61) % 64, 35),
        ("add-seventeen", lambda v: (v + 17) % 64, lambda v: (v - 17) % 64, 41),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    def tree(items):
        level = [{"hash": canonical_hash({"name": name, "gates": gates}), "gates": gates}
                 for name, _, _, gates in items]
        while len(level) > 1:
            level = [{"hash": canonical_hash({"left": level[i]["hash"], "right": level[i + 1]["hash"],
                                               "gates": level[i]["gates"] + level[i + 1]["gates"]}),
                      "gates": level[i]["gates"] + level[i + 1]["gates"]}
                     for i in range(0, len(level), 2)]
        return level[0]

    names = [item[0] for item in operations]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, inverse=True) for value in encoded]
    mutated = [operations[1], operations[0], *operations[2:]]
    program_tree = tree(operations)
    mutated_tree = tree([*operations[:7], (operations[7][0], operations[7][1], operations[7][2], 40)])
    return {
        "inverse_pair_names": names,
        "program_tree_root_sha256": program_tree["hash"],
        "tree_resource_sum": program_tree["gates"],
        "tree_mutation_rejected": mutated_tree["hash"] != program_tree["hash"],
        "resource_accounting_valid": program_tree["gates"] == sum(item[3] for item in operations),
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(a != apply(value, mutated)
                                            for value, a in enumerate(encoded)),
        "resource_bound": {"gates": program_tree["gates"], "max_qubits": 6},
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle030_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": tenth_graph_double_orbits(),
            "B": integer_escaped_key_receipt_gate(),
            "C": four_reader_directory_atomicity(work),
            "D": zip64_local_central_full_bind(),
            "E": ten_issuer_two_level_revocation(),
            "F": fourteen_component_covariance_grid(source_bytes),
            "G": signed_block_covariance_transform(),
            "H": fourteen_scenario_deletion_intervals(),
            "FND/EQN": seven_source_affine_maps(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five",
                source_bytes + b":six", source_bytes + b":seven",
            ),
            "SCM": transcript_fork_stale_controls(),
            "AI-COST": lineage_manifest_v20(source_bytes),
            "QOS/QSVT": eight_inverse_pairs_program_tree(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
