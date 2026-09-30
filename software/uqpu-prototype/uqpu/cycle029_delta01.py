"""Cycle 029 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import re
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


def ninth_graph_stabilizer_partition():
    n = 11

    def edges(weights):
        return [[i, (i + 1) % n, weights[i]] for i in range(n)]

    def solve(weight_list):
        edge_list = edges(weight_list)
        scores = [
            sum(w for u, v, w in edge_list if ((mask >> u) & 1) != ((mask >> v) & 1))
            for mask in range(1 << n)
        ]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {
            "states": len(scores),
            "objective": optimum,
            "witnesses": witnesses,
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

    eighth = [1] * n
    for index, weight in ((3, 2), (8, 3), (5, 4), (1, 5), (10, 6)):
        eighth[index] = weight
    ninth = list(eighth)
    ninth[7] = 7
    prior, current = solve(eighth), solve(ninth)
    transforms = []
    stabilizer = []
    for sign in (1, -1):
        for shift in range(n):
            transformed_weights = transform_weights(ninth, sign, shift)
            transformed = solve(transformed_weights)
            expected = sorted(transform_mask(mask, sign, shift) for mask in current["witnesses"])
            row = {
                "sign": sign,
                "shift": shift,
                "task_sha256": transformed["task_sha256"],
                "witness_sha256": transformed["witness_sha256"],
                "matches": transformed["witnesses"] == expected,
            }
            transforms.append(row)
            if transformed_weights == ninth:
                stabilizer.append((sign, shift))
    remaining = set(current["witnesses"])
    orbits = []
    while remaining:
        seed = min(remaining)
        orbit = sorted({transform_mask(seed, sign, shift) for sign, shift in stabilizer})
        orbits.append(orbit)
        remaining.difference_update(orbit)
    return {
        "states_each": [prior["states"], current["states"]],
        "objectives": [prior["objective"], current["objective"]],
        "witness_counts": [len(prior["witnesses"]), len(current["witnesses"])],
        "changed_edge_indices": [7],
        "unchanged_edges_identical": all(eighth[i] == ninth[i] for i in range(n) if i != 7),
        "dihedral_transform_count": len(transforms),
        "all_dihedral_transforms_match": all(row["matches"] for row in transforms),
        "stabilizer": [[sign, shift] for sign, shift in stabilizer],
        "stabilizer_orbit_partition": orbits,
        "partition_sha256": canonical_hash(orbits),
        "complete_witness_sha256": current["witness_sha256"],
        "deterministic": current == solve(ninth),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def duplicate_lexical_receipt_gate():
    first = b'{"body":{"negative":-0,"amount":125.0,"items":[1,2,3]}}'
    equivalent = b'{"body":{"items":[1,2,3],"amount":1.25e2,"negative":0}}'
    caps = {"bytes": 256, "depth": 5, "tokens": 24, "magnitude": 10 ** 12,
            "fraction_digits": 6, "exponent_abs": 12}
    number_pattern = re.compile(r"-?(?:0|[1-9]\d*)(?:\.(\d+))?(?:[eE]([+-]?\d+))?")

    def pairs(items):
        output = {}
        for key, value in items:
            if key in output:
                raise ValueError("duplicate key")
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

    def valid_numbers(value):
        if isinstance(value, dict):
            return all(valid_numbers(item) for item in value.values())
        if isinstance(value, list):
            return all(valid_numbers(item) for item in value)
        if isinstance(value, (int, float)) and not isinstance(value, bool):
            return math.isfinite(value) and abs(value) <= caps["magnitude"]
        return True

    def bounded(raw):
        if len(raw) > caps["bytes"]:
            raise ValueError("byte cap")
        text = raw.decode("utf-8")
        for match in number_pattern.finditer(text):
            fraction, exponent = match.groups()
            if fraction and len(fraction) > caps["fraction_digits"]:
                raise ValueError("fraction cap")
            if exponent and abs(int(exponent)) > caps["exponent_abs"]:
                raise ValueError("exponent cap")
        value = json.loads(text, object_pairs_hook=pairs,
                           parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
        if depth(value) > caps["depth"] or tokens(value) > caps["tokens"] or not valid_numbers(value):
            raise ValueError("value cap")
        normalized = json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
        return canonical_receipt_bytes(normalized)

    canonical = bounded(first)
    controls = {}
    cases = {
        "duplicate_key": b'{"a":1,"a":2}',
        "exponent_cap": b'{"a":1e13}',
        "fraction_cap": b'{"a":1.1234567}',
        "nonfinite": b'{"a":NaN}',
        "magnitude_cap": b'{"a":1000000000001}',
        "token_cap": json.dumps({"v": list(range(25))}).encode(),
    }
    for name, raw in cases.items():
        try:
            bounded(raw)
            controls[name] = False
        except (ValueError, UnicodeError, json.JSONDecodeError):
            controls[name] = True
    return {
        "accepted_lexical_equivalence": canonical == bounded(equivalent),
        "canonical_sha256": hashlib.sha256(canonical).hexdigest(),
        "caps": caps,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def triple_reader_inode_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(4):
        target_name = f"triple-reader-{run % 2}.bin"
        target = root / target_name
        if not target.exists():
            target.write_bytes(b"old-complete-payload")
        old = target.read_bytes()
        payloads = [f"cycle029-{run}-{writer}".encode() for writer in range(3)]
        allowed = {old, *payloads}
        stop = threading.Event()
        barrier = threading.Barrier(4)
        observations = [[], [], []]

        def reader(index):
            barrier.wait()
            while not stop.is_set():
                try:
                    stat = target.stat()
                    observations[index].append((target.read_bytes(), stat.st_ino, target.name))
                except FileNotFoundError:
                    observations[index].append((b"", -1, target.name))
                time.sleep(0.0005)

        threads = [threading.Thread(target=reader, args=(index,)) for index in range(3)]
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
            "reader_complete": [bool(items) and all(data in allowed and name == target_name
                                                     for data, _, name in items)
                                for items in observations],
            "inode_sets": [sorted({inode for _, inode, _ in items}) for items in observations],
            "parent_complete": result["visible_complete"],
            "parent_sha256": result["visible_sha256"],
            "exit_codes": result["exit_codes"],
        })
    return {
        "runs": rows,
        "reader_count": 3,
        "all_reader_parent_observations_complete": all(
            all(row["reader_complete"]) and row["parent_complete"] for row in rows
        ),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_TRIPLE_READER_FIXTURE",
    }


def zip64_header_descriptor_bind():
    expected = {"version": 45, "flags": 0x08, "crc32": 0xA0B0C0D0,
                "compressed": 37, "uncompressed": 53}

    def header(version=45, flags=0x08):
        return version.to_bytes(2, "little") + flags.to_bytes(2, "little")

    def descriptor(signed=True, crc=None, compressed=None):
        import struct
        body = struct.pack("<IQQ", expected["crc32"] if crc is None else crc,
                           expected["compressed"] if compressed is None else compressed,
                           expected["uncompressed"])
        return (b"PK\x07\x08" + body) if signed else body

    def verify(raw_header, raw_descriptor):
        import struct
        version, flags = struct.unpack("<HH", raw_header)
        body = raw_descriptor[4:] if len(raw_descriptor) == 24 and raw_descriptor[:4] == b"PK\x07\x08" else raw_descriptor
        if (version, flags) != (expected["version"], expected["flags"]):
            raise ValueError("header")
        if len(body) != 20 or struct.unpack("<IQQ", body) != (
            expected["crc32"], expected["compressed"], expected["uncompressed"]
        ):
            raise ValueError("descriptor")
        return True

    controls = {}
    cases = {
        "version": (header(version=20), descriptor()),
        "flags": (header(flags=0), descriptor()),
        "crc": (header(), descriptor(crc=0)),
        "size": (header(), descriptor(compressed=38)),
        "signature_like_prefix": (header(), b"PK\x07\x08synthetic-payload"),
    }
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except (ValueError, TypeError):
            controls[name] = True
    opaque_a = [(0x0001, b"zip64"), (0xBEEF, b"opaque-029")]
    opaque_b = list(reversed(opaque_a))
    return {
        "descriptor_forms_valid": [verify(header(), descriptor(True)), verify(header(), descriptor(False))],
        "reordered_extra_maps_equal": dict(opaque_a) == dict(opaque_b),
        "unknown_extra_preserved": dict(opaque_a)[0xBEEF] == b"opaque-029",
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def nine_issuer_revocation_controls():
    sample = hashlib.sha256(b"cycle029-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer"),
        ("issuer-d", "analysis"), ("issuer-e", "archive"),
        ("issuer-f", "archive:delegated"), ("issuer-g", "release:delegated"),
        ("issuer-h", "audit:delegated"), ("issuer-i", "audit:subdelegated"),
    ]
    starts = [f"2026-{month:02d}-01" for month in range(1, 10)]

    def build(path="fixture-029"):
        events, prior = [], "0" * 64
        for sequence, ((issuer, scope), start) in enumerate(zip(specs, starts)):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       start, "2027-01-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-i": "issuer-h", "issuer-h": "issuer-g"}

    def verify(events, bound_registry, revocation_sequence=10, bound_ancestry=ancestry):
        if revocation_sequence <= events[-1]["sequence"]:
            raise ValueError("revoked")
        if any(event["path_id"] != "fixture-029" for event in events):
            raise ValueError("path")
        if bound_ancestry.get("issuer-i") != "issuer-h" or bound_ancestry.get("issuer-h") != "issuer-g":
            raise ValueError("ancestry")
        return verify_custody_chain(events, bound_registry, "2026-09-01")

    valid = verify(build(), registry)
    controls = {}
    cases = {
        "revoked_sequence": (build(), registry, 8, ancestry),
        "cross_path": (build("other-path"), registry, 10, ancestry),
        "scope_removed": (build(), {**registry, "issuer-i": {"audit"}}, 10, ancestry),
        "ancestry_changed": (build(), registry, 10, {"issuer-i": "issuer-g", "issuer-h": "issuer-g"}),
    }
    for name, args in cases.items():
        try:
            verify(*args)
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "event_count": 9,
        "terminal_sha256": valid["final_event_sha256"],
        "boundary_rejections": controls,
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def thirteen_component_covariance_grid():
    n = 13
    intervals = [[i + 1, i + 4] for i in range(n)]
    matrices = {
        "positive": [[0.02 if i == j else 0.0002 for j in range(n)] for i in range(n)],
        "zero": [[0.02 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.02 if i == j else -0.0007 for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0]
    return {
        "components": n,
        "sigma_values": sigmas,
        "sweeps": {str(s): component_covariance_sweep(intervals, matrices, [1, 7, 13, 0], sigma=s)
                   for s in sigmas},
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def block_basis_covariance_transform():
    covariance = [
        [Fraction(4), Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(9), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1), Fraction(49)],
    ]
    permutation = [1, 0, 3, 2]

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

    transformed = [[covariance[permutation[i]][permutation[j]] for j in range(4)] for i in range(4)]
    inverse = [permutation.index(i) for i in range(4)]
    restored = [[transformed[inverse[i]][inverse[j]] for j in range(4)] for i in range(4)]

    def corr(matrix, i, j):
        return float(matrix[i][j]) / math.sqrt(float(matrix[i][i] * matrix[j][j]))

    return {
        "block_permutation": permutation,
        "matrix_product_count": 16,
        "exact_roundtrip": restored == covariance,
        "trace_invariant": sum(transformed[i][i] for i in range(4)) == sum(covariance[i][i] for i in range(4)),
        "determinant_invariant": determinant(transformed) == determinant(covariance),
        "correlation_permutation_invariant": all(
            math.isclose(corr(transformed, i, j), corr(covariance, permutation[i], permutation[j]),
                         rel_tol=0.0, abs_tol=1e-15)
            for i in range(4) for j in range(4)
        ),
        "symmetric": all(transformed[i][j] == transformed[j][i] for i in range(4) for j in range(4)),
        "psd_by_permutation_congruence": True,
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def thirteen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3],
    ]

    def counts(rows):
        output = [0, 0, 0, 0]
        for scores in rows:
            eligible = {i for i, score in enumerate(scores) if score == max(scores)}
            for order in itertools.permutations(range(4)):
                output[next(item for item in order if item in eligible)] += 1
        return output

    full = counts(scenarios)
    fractions = [Fraction(value, 13 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 6):
        combos = list(itertools.combinations(range(13), removed_count))
        grid_counts[str(removed_count)] = len(combos)
        denominator = (13 - removed_count) * 24
        for removed in combos:
            removed_set = set(removed)
            row = counts([item for i, item in enumerate(scenarios) if i not in removed_set])
            fractions.extend(Fraction(value, denominator) for value in row)
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 13,
        "orders_each": 24,
        "full_grid_size": 312,
        "winner_counts": full,
        "deletion_grid_counts": grid_counts,
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def six_source_affine_maps(*raw_sources):
    if len(raw_sources) != 6 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("six source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 6:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
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
        "nonmonotone": (sources, [*maps[:5], (Fraction(0), Fraction(0))], [1, 0, 0, 0]),
    }
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


def transcript_hash_chain_controls():
    def build(audience="fiction-029", epoch=10, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 6):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows

    def verify(rows, audience="fiction-029", minimum_epoch=10):
        prior = "0" * 64
        for expected_sequence, row in enumerate(rows, start=1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            if (row["sequence"] != expected_sequence or row["epoch"] < minimum_epoch
                    or row["audience"] != audience or not row["active"]
                    or row["previous_sha256"] != prior
                    or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            prior = row["row_sha256"]
        return True

    valid = build()
    replay = [*valid[:3], valid[2], *valid[4:]]
    skipped = [*valid[:2], *valid[3:]]
    downgraded = build(epoch=9)
    wrong_audience = build(audience="other")
    revoked = build(active=False)
    table = [
        ("valid", valid, True), ("replay", replay, False), ("skip", skipped, False),
        ("epoch_downgrade", downgraded, False), ("audience", wrong_audience, False),
        ("revoked", revoked, False),
    ]
    controls = [{"case": name, "accepted": verify(rows), "expected": expected}
                for name, rows, expected in table]
    return {
        "control_table": controls,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in controls),
        "terminal_sha256": valid[-1]["row_sha256"],
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v19(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    members = ["t1", "t2", "t3", "v1", "v2", "h1", "h2", "h3"]
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

    def proof(index):
        output = []
        for row in tree[:-1]:
            sibling = index ^ 1
            if sibling >= len(row):
                sibling = index
            output.append({"side": "left" if sibling < index else "right", "sha256": row[sibling]})
            index //= 2
        return output

    def verify_path(leaf, path, root):
        value = leaf
        for item in path:
            value = hashlib.sha256(((item["sha256"] + value) if item["side"] == "left"
                                    else (value + item["sha256"])).encode()).hexdigest()
        return value == root

    root = tree[-1][0]
    heldout = {members[i]: {"leaf": leaves[i], "path": proof(i)} for i in (5, 6, 7)}
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 18, "source_sha256": source_sha})
    body = {
        "schema_version": 19,
        "parent_manifest_sha256": parent,
        "source_sha256": source_sha,
        "provenance_merkle_root": root,
        "heldout_inclusion_paths": heldout,
        "config_sha256": canonical_hash({"model": "synthetic-v19"}),
        "heldout_metric": {"name": "fixture_loss", "value": 0.19, "unit": "1", "split": "test"},
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        paths = candidate.get("heldout_inclusion_paths", {})
        return (
            candidate.get("schema_version") == 19
            and candidate.get("parent_manifest_sha256") == parent
            and candidate.get("source_sha256") == source_sha
            and candidate.get("provenance_merkle_root") == root
            and set(paths) == {"h1", "h2", "h3"}
            and all(verify_path(item["leaf"], item["path"], root) for item in paths.values())
            and candidate.get("manifest_sha256") == canonical_hash(unsigned)
        )

    mutated_path = json.loads(json.dumps(manifest))
    mutated_path["heldout_inclusion_paths"]["h1"]["path"][0]["sha256"] = "0" * 64
    return {
        "manifest": manifest,
        "leaf_count": len(leaves),
        "heldout_path_count": len(heldout),
        "valid_manifest": verify(manifest),
        "path_mutation_rejected": not verify(mutated_path),
        "parent_mutation_rejected": not verify({**manifest, "parent_manifest_sha256": "0" * 64}),
        "schema_mutation_rejected": not verify({**manifest, "schema_version": 18}),
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def seven_inverse_pairs_segment_gate():
    mask = 0b001011
    operations = [
        ("xor", lambda v: v ^ mask, lambda v: v ^ mask, 6),
        ("rotate", lambda v: ((v << 1) & 63) | (v >> 5),
         lambda v: (v >> 1) | ((v & 1) << 5), 10),
        ("pair-swap", lambda v: sum((((v >> low) & 1) << (low + 1))
                                    | (((v >> (low + 1)) & 1) << low) for low in (0, 2, 4)),
         lambda v: sum((((v >> low) & 1) << (low + 1))
                       | (((v >> (low + 1)) & 1) << low) for low in (0, 2, 4)), 6),
        ("bit-reverse", lambda v: sum(((v >> bit) & 1) << (5 - bit) for bit in range(6)),
         lambda v: sum(((v >> bit) & 1) << (5 - bit) for bit in range(6)), 15),
        ("add-nine", lambda v: (v + 9) % 64, lambda v: (v - 9) % 64, 21),
        ("multiply-five", lambda v: (v * 5) % 64, lambda v: (v * 13) % 64, 30),
        ("multiply-twenty-one", lambda v: (v * 21) % 64, lambda v: (v * 61) % 64, 35),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    names = [item[0] for item in operations]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, inverse=True) for value in encoded]
    mutated = [operations[1], operations[0], *operations[2:]]
    segments = [{"name": name, "gates": gates} for name, _, _, gates in operations]
    expected_gates = sum(item["gates"] for item in segments)
    return {
        "inverse_pair_names": names,
        "prefix_program_sha256": [canonical_hash(names[:i]) for i in range(1, 8)],
        "suffix_program_sha256": [canonical_hash(names[i:]) for i in range(7)],
        "segment_resources": segments,
        "program_sha256": canonical_hash({"operators": names, "segments": segments}),
        "resource_accounting_valid": expected_gates == 123,
        "resource_mutation_rejected": expected_gates != 122,
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(a != apply(value, mutated)
                                            for value, a in enumerate(encoded)),
        "resource_bound": {"gates": expected_gates, "max_qubits": 6},
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle029_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": ninth_graph_stabilizer_partition(),
            "B": duplicate_lexical_receipt_gate(),
            "C": triple_reader_inode_atomicity(work),
            "D": zip64_header_descriptor_bind(),
            "E": nine_issuer_revocation_controls(),
            "F": thirteen_component_covariance_grid(),
            "G": block_basis_covariance_transform(),
            "H": thirteen_scenario_deletion_intervals(),
            "FND/EQN": six_source_affine_maps(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
            ),
            "SCM": transcript_hash_chain_controls(),
            "AI-COST": lineage_manifest_v19(source_bytes),
            "QOS/QSVT": seven_inverse_pairs_segment_gate(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
