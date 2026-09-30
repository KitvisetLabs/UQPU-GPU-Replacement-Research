"""Cycle 031 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

import hashlib
import itertools
import json
import math
import struct
import tempfile
import threading
import time
import unicodedata
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


def eleventh_graph_witness_quotient():
    n, full_mask = 11, (1 << 11) - 1

    def edges(weights):
        return [[i, (i + 1) % n, weights[i]] for i in range(n)]

    def solve(weights):
        edge_list = edges(weights)
        scores = [sum(w for u, v, w in edge_list if ((mask >> u) & 1) != ((mask >> v) & 1))
                  for mask in range(1 << n)]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {"states": len(scores), "objective": optimum, "witnesses": witnesses,
                "task_sha256": canonical_hash({"vertices": n, "edges": edge_list}),
                "witness_sha256": canonical_hash(witnesses)}

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

    tenth = [1] * n
    for index, weight in ((0, 8), (1, 5), (3, 2), (5, 4), (7, 7), (8, 3), (10, 6)):
        tenth[index] = weight
    eleventh = list(tenth)
    eleventh[2] = 9
    prior, current = solve(tenth), solve(eleventh)
    transforms, stabilizer = [], []
    for sign in (1, -1):
        for shift in range(n):
            transformed_weights = transform_weights(eleventh, sign, shift)
            transformed = solve(transformed_weights)
            expected = sorted(transform_mask(mask, sign, shift) for mask in current["witnesses"])
            transforms.append({"sign": sign, "shift": shift,
                               "matches": transformed["witnesses"] == expected,
                               "task_sha256": transformed["task_sha256"],
                               "witness_sha256": transformed["witness_sha256"]})
            if transformed_weights == eleventh:
                stabilizer.append((sign, shift))
    witnesses = set(current["witnesses"])
    remaining, quotient = set(witnesses), []
    while remaining:
        seed = min(remaining)
        orbit = set()
        for sign, shift in stabilizer:
            transformed = transform_mask(seed, sign, shift)
            orbit.update((transformed, transformed ^ full_mask))
        bounded = sorted(orbit & witnesses)
        quotient.append({"representative": min(bounded), "members": bounded})
        remaining.difference_update(bounded)
    return {
        "states_each": [prior["states"], current["states"]],
        "objectives": [prior["objective"], current["objective"]],
        "witness_counts": [len(prior["witnesses"]), len(current["witnesses"])],
        "changed_edge_indices": [2],
        "unchanged_edges_identical": all(tenth[i] == eleventh[i] for i in range(n) if i != 2),
        "dihedral_transform_count": len(transforms),
        "all_dihedral_transforms_match": all(row["matches"] for row in transforms),
        "stabilizer": [[sign, shift] for sign, shift in stabilizer],
        "witness_quotient": quotient,
        "quotient_sha256": canonical_hash(quotient),
        "complete_witness_sha256": current["witness_sha256"],
        "deterministic": current == solve(eleventh),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def unicode_value_receipt_gate():
    first = '{"body":{"label":"é","max_int":9007199254740991,"negative":-0}}'.encode()
    equivalent = b'{"body":{"negative":0,"max_int":9007199254740991,"label":"e\\u0301"}}'
    caps = {"bytes": 256, "depth": 5, "tokens": 24, "normalized_string_length": 16,
            "max_exact_integer": 2 ** 53 - 1, "magnitude": 10 ** 12}

    def pairs(items):
        output = {}
        for raw_key, value in items:
            key = unicodedata.normalize("NFC", raw_key)
            if key in output:
                raise ValueError("normalized duplicate key")
            output[key] = value
        return output

    def normalize(value):
        if isinstance(value, dict):
            return {key: normalize(item) for key, item in value.items()}
        if isinstance(value, list):
            return [normalize(item) for item in value]
        if isinstance(value, str):
            result = unicodedata.normalize("NFC", value)
            if len(result) > caps["normalized_string_length"]:
                raise ValueError("string cap")
            result.encode("utf-8")
            return result
        return value

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
        if isinstance(value, int) and not isinstance(value, bool):
            return abs(value) <= caps["max_exact_integer"]
        if isinstance(value, float):
            return math.isfinite(value) and abs(value) <= caps["magnitude"]
        return True

    def bounded(raw):
        if len(raw) > caps["bytes"]:
            raise ValueError("byte cap")
        value = normalize(json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                                     parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant"))))
        if depth(value) > caps["depth"] or tokens(value) > caps["tokens"] or not valid_numbers(value):
            raise ValueError("value cap")
        normalized = json.dumps(value, sort_keys=True, separators=(",", ":"),
                                ensure_ascii=False, allow_nan=False).encode("utf-8")
        return canonical_receipt_bytes(normalized)

    canonical = bounded(first)
    cases = {
        "normalized_key_collision": '{"é":1,"é":2}'.encode(),
        "literal_duplicate": b'{"a":1,"a":2}',
        "string_length": json.dumps({"v": "x" * 17}).encode(),
        "integer_precision": b'{"v":9007199254740992}',
        "nonfinite": b'{"v":NaN}',
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
        "normalized_value_equivalence": canonical == bounded(equivalent),
        "canonical_sha256": hashlib.sha256(canonical).hexdigest(),
        "caps": caps,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def five_reader_descriptor_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(4):
        target_name = f"five-reader-{run % 2}.bin"
        target = root / target_name
        if not target.exists():
            target.write_bytes(b"old-complete-payload")
        old = target.read_bytes()
        payloads = [f"cycle031-{run}-{writer}".encode() for writer in range(3)]
        allowed = {old, *payloads}
        pre_names = sorted(path.name for path in root.iterdir())
        with target.open("rb") as held:
            held_inode = target.stat().st_ino
            stop = threading.Event()
            barrier = threading.Barrier(6)
            observations = [[], [], [], [], []]

            def reader(index):
                barrier.wait()
                while not stop.is_set():
                    try:
                        observations[index].append((target.read_bytes(), target.name, target.stat().st_ino))
                    except FileNotFoundError:
                        observations[index].append((b"", target.name, -1))
                    time.sleep(0.0005)

            threads = [threading.Thread(target=reader, args=(index,)) for index in range(5)]
            for thread in threads:
                thread.start()
            barrier.wait()
            result = concurrent_subprocess_replace(root, target_name, payloads)
            time.sleep(0.003)
            stop.set()
            for thread in threads:
                thread.join(timeout=2)
            held.seek(0)
            held_bytes = held.read()
        rows.append({
            "run": run,
            "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(data in allowed and name == target_name
                                                     for data, name, _ in items)
                                for items in observations],
            "held_descriptor_old_complete": held_bytes == old,
            "held_inode": held_inode,
            "path_inode": target.stat().st_ino,
            "pre_directory_names": pre_names,
            "post_directory_names": sorted(path.name for path in root.iterdir()),
            "parent_complete": result["visible_complete"],
            "exit_codes": result["exit_codes"],
        })
    return {
        "runs": rows,
        "reader_count": 5,
        "all_reader_parent_observations_complete": all(
            all(row["reader_complete"]) and row["parent_complete"] for row in rows
        ),
        "all_held_descriptors_complete": all(row["held_descriptor_old_complete"] for row in rows),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_FIVE_READER_FIXTURE",
    }


def zip64_name_version_bind():
    expected = {"version_needed": 45, "version_extract": 45, "flags": 0x808,
                "method": 8, "crc32": 0xA0B0C0D0, "compressed": 43, "uncompressed": 61}
    name = "cycle031-Δ.bin".encode("utf-8")

    def header(version_needed=45, version_extract=45, flags=0x808, method=8, filename=name):
        return struct.pack("<HHHHH", version_needed, version_extract, flags, method, len(filename)) + filename

    def parse_header(raw):
        if len(raw) < 10:
            raise ValueError("truncated")
        needed, extract, flags, method, width = struct.unpack_from("<HHHHH", raw)
        filename = raw[10:]
        if len(filename) != width or (needed, extract, flags, method) != (
            expected["version_needed"], expected["version_extract"], expected["flags"], expected["method"]
        ):
            raise ValueError("header")
        if not (flags & 0x800) or filename.decode("utf-8") != name.decode("utf-8"):
            raise ValueError("name")
        return filename

    def extra(identifier, body):
        return struct.pack("<HH", identifier, len(body)) + body

    zip64 = extra(0x0001, struct.pack("<QQ", expected["uncompressed"], expected["compressed"]))
    opaque = extra(0xD00D, b"opaque-031")

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
        if 0x0001 not in output or struct.unpack("<QQ", output[0x0001]) != (
            expected["uncompressed"], expected["compressed"]
        ):
            raise ValueError("zip64")
        return output

    def descriptor(signed=True, crc=None):
        body = struct.pack("<IQQ", expected["crc32"] if crc is None else crc,
                           expected["compressed"], expected["uncompressed"])
        return (b"PK\x07\x08" + body) if signed else body

    def verify(local_header, central_header, raw_descriptor, local_extra, central_extra):
        if parse_header(local_header) != parse_header(central_header):
            raise ValueError("header mismatch")
        body = raw_descriptor[4:] if len(raw_descriptor) == 24 and raw_descriptor[:4] == b"PK\x07\x08" else raw_descriptor
        if len(body) != 20 or struct.unpack("<IQQ", body) != (
            expected["crc32"], expected["compressed"], expected["uncompressed"]
        ):
            raise ValueError("descriptor")
        return extras(local_extra) == extras(central_extra)

    valid = (header(), header(), descriptor(), zip64 + opaque, opaque + zip64)
    cases = {
        "version_needed": (header(version_needed=20), *valid[1:]),
        "version_extract": (header(version_extract=20), *valid[1:]),
        "utf8_flag": (header(flags=0x08), *valid[1:]),
        "method": (header(method=0), *valid[1:]),
        "name_mismatch": (header(), header(filename=b"other.bin"), *valid[2:]),
        "invalid_utf8": (header(filename=b"\xff"), *valid[1:]),
        "descriptor": (header(), header(), descriptor(crc=0), *valid[3:]),
        "duplicate_extra": (header(), header(), descriptor(), zip64 + opaque + zip64, opaque + zip64),
    }
    controls = {}
    for key, args in cases.items():
        try:
            verify(*args)
            controls[key] = False
        except (ValueError, UnicodeError, struct.error):
            controls[key] = True
    return {
        "signed_unsigned_valid": [verify(*valid), verify(header(), header(), descriptor(False), zip64 + opaque, opaque + zip64)],
        "filename_utf8": name.decode("utf-8"),
        "unknown_extra_preserved": extras(zip64 + opaque)[0xD00D] == b"opaque-031",
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def eleven_issuer_revocation_quorum():
    sample = hashlib.sha256(b"cycle031-synthetic-custody").hexdigest()
    specs = [
        ("issuer-a", "intake"), ("issuer-b", "storage"), ("issuer-c", "transfer"),
        ("issuer-d", "analysis"), ("issuer-e", "archive"), ("issuer-f", "archive:delegated"),
        ("issuer-g", "release:delegated"), ("issuer-h", "audit:delegated"),
        ("issuer-i", "audit:subdelegated"), ("issuer-j", "review:subdelegated"),
        ("issuer-k", "release-review:subdelegated"),
    ]
    starts = [f"2026-{month:02d}-01" for month in range(1, 12)]

    def build(path="fixture-031"):
        events, prior = [], "0" * 64
        for sequence, ((issuer, scope), start) in enumerate(zip(specs, starts)):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       start, "2027-01-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-k": "issuer-j", "issuer-j": "issuer-i"}

    def verify(events, bound_registry, revocation_votes=(False, False, True),
               bound_ancestry=ancestry, now="2026-11-01"):
        if sum(bool(vote) for vote in revocation_votes) >= 2:
            raise ValueError("revocation quorum")
        if any(event["path_id"] != "fixture-031" for event in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        if not (max(event["valid_from"] for event in events) <= now
                <= min(event["expires_at"] for event in events)):
            raise ValueError("window")
        return verify_custody_chain(events, bound_registry, now)

    valid = verify(build(), registry)
    cases = {
        "revocation_quorum": (build(), registry, (True, True, False), ancestry, "2026-11-01"),
        "cross_path": (build("other"), registry, (False, False, True), ancestry, "2026-11-01"),
        "scope_removed": (build(), {**registry, "issuer-k": {"release-review"}}, (False, False, True), ancestry, "2026-11-01"),
        "ancestry_changed": (build(), registry, (False, False, True), {"issuer-k": "issuer-i", "issuer-j": "issuer-i"}, "2026-11-01"),
        "before_intersection": (build(), registry, (False, False, True), ancestry, "2026-10-31"),
    }
    controls = {}
    for key, args in cases.items():
        try:
            verify(*args)
            controls[key] = False
        except ValueError:
            controls[key] = True
    return {"event_count": 11, "terminal_sha256": valid["final_event_sha256"],
            "boundary_rejections": controls, "physical_sample": None,
            "evidence_class": "SYNTHETIC_CUSTODY"}


def fifteen_component_ordered_covariance(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 15
    order = [f"component-{i:02d}" for i in range(n)]
    intervals = [[i + 1, i + 5] for i in range(n)]
    matrices = {
        "positive": [[0.02 if i == j else 0.00015 for j in range(n)] for i in range(n)],
        "zero": [[0.02 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.02 if i == j else -0.0005 for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("inf") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    identity = canonical_hash({"source_sha256": source_sha, "order": order,
                               "intervals": intervals, "matrix_names": sorted(matrices), "sigmas": sigmas})
    mutated = canonical_hash({"source_sha256": source_sha, "order": list(reversed(order)),
                              "intervals": intervals, "matrix_names": sorted(matrices), "sigmas": sigmas})
    return {
        "components": n, "source_sha256": source_sha, "component_order": order,
        "covariance_grid_sha256": identity, "order_mutation_rejected": mutated != identity,
        "sigma_values": sigmas,
        "sweeps": {str(s): component_covariance_sweep(intervals, matrices, [1, 8, 15, 0], sigma=s)
                   for s in sigmas},
        "commercial_interpretation": None, "evidence_class": "MODEL_ONLY",
    }


def composed_signed_block_transforms():
    covariance = [
        [Fraction(4), Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(9), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1), Fraction(49)],
    ]
    transforms = [([1, 0, 3, 2], [1, -1, 1, -1]), ([2, 3, 0, 1], [-1, 1, -1, 1])]

    def apply(matrix, permutation, signs):
        return [[signs[i] * signs[j] * matrix[permutation[i]][permutation[j]]
                 for j in range(4)] for i in range(4)]

    def inverse(matrix, permutation, signs):
        inv = [permutation.index(i) for i in range(4)]
        return [[signs[inv[i]] * signs[inv[j]] * matrix[inv[i]][inv[j]]
                 for j in range(4)] for i in range(4)]

    def determinant(matrix):
        work, output = [list(row) for row in matrix], Fraction(1)
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
                factor = work[row][col]
                for j in range(col, len(work)):
                    work[row][j] -= factor * work[col][j]
        return output

    first = apply(covariance, *transforms[0])
    second = apply(first, *transforms[1])
    restored = inverse(inverse(second, *transforms[1]), *transforms[0])
    return {
        "transform_count": 2, "matrix_product_count": 32,
        "exact_composition_roundtrip": restored == covariance,
        "trace_invariant": sum(second[i][i] for i in range(4)) == sum(covariance[i][i] for i in range(4)),
        "determinant_invariant": determinant(second) == determinant(covariance),
        "symmetric": all(second[i][j] == second[j][i] for i in range(4) for j in range(4)),
        "psd_by_signed_permutation_congruence": True,
        "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                "signs": [item[1] for item in transforms]}),
        "calibration": None, "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def fifteen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3],
    ]

    def counts(rows):
        output = [0, 0, 0, 0]
        for scores in rows:
            eligible = {i for i, score in enumerate(scores) if score == max(scores)}
            for order in itertools.permutations(range(4)):
                output[next(item for item in order if item in eligible)] += 1
        return output

    full = counts(scenarios)
    fractions = [Fraction(value, 15 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 8):
        combos = list(itertools.combinations(range(15), removed_count))
        grid_counts[str(removed_count)] = len(combos)
        denominator = (15 - removed_count) * 24
        for removed in combos:
            removed_set = set(removed)
            row = counts([item for i, item in enumerate(scenarios) if i not in removed_set])
            fractions.extend(Fraction(value, denominator) for value in row)
    low, high = min(fractions), max(fractions)
    return {"scenario_count": 15, "orders_each": 24, "full_grid_size": 360,
            "winner_counts": full, "deletion_grid_counts": grid_counts,
            "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
            "probability_claim": None, "capital": None,
            "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO"}


def eight_source_affine_maps(*raw_sources):
    if len(raw_sources) != 8 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("eight source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 8:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
        (Fraction(17, 16), Fraction(1, 17)), (Fraction(19, 18), Fraction(-1, 19)),
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
    cases = {"source_order": (list(reversed(sources)), maps, [1, 0, 0, 0]),
             "dimension": (sources, maps, [0, 1, 0, 0]),
             "nonmonotone": (sources, [*maps[:7], (Fraction(0), Fraction(0))], [1, 0, 0, 0])}
    controls = {}
    for key, args in cases.items():
        try:
            compose(*args)
            controls[key] = False
        except ValueError:
            controls[key] = True
    return {"source_sha256": sources, "map_count": len(maps),
            "composed_interval": [[v.numerator, v.denominator] for v in transformed],
            "roundtrip_interval": [[v.numerator, v.denominator] for v in restored],
            "exact_roundtrip": restored == (Fraction(2, 3), Fraction(5, 3)),
            "negative_controls": controls, "sort": ["RealModel", "Model"],
            "new_law_claim": None, "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL"}


def transcript_equivocation_quorum_controls():
    def build(audience="fiction-031", epoch=12, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 6):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "payload": f"row-{sequence}", "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows, prior

    def verify(rows, reports, audience="fiction-031", minimum_epoch=12):
        prior = "0" * 64
        for expected, row in enumerate(rows, start=1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            if (row["sequence"] != expected or row["epoch"] < minimum_epoch
                    or row["audience"] != audience or not row["active"]
                    or row["previous_sha256"] != prior or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            prior = row["row_sha256"]
        counts = {head: reports.count(head) for head in set(reports)}
        return len(reports) == 4 and counts.get(prior, 0) >= 3

    valid, head = build()
    fork = dict(valid[2]); fork["payload"] = "fork"
    fork["row_sha256"] = canonical_hash({k: v for k, v in fork.items() if k != "row_sha256"})
    forked = [*valid[:3], fork, *valid[3:]]
    replay = [*valid[:3], valid[2], *valid[4:]]
    downgraded, down_head = build(epoch=11)
    wrong, wrong_head = build(audience="other")
    revoked, revoked_head = build(active=False)
    table = [
        ("valid", valid, [head, head, head, head], True),
        ("equivocation", valid, [head, head, "f" * 64, "f" * 64], False),
        ("stale_quorum", valid, [valid[-2]["row_sha256"]] * 3 + [head], False),
        ("fork", forked, [head] * 4, False), ("replay", replay, [head] * 4, False),
        ("downgrade", downgraded, [down_head] * 4, False),
        ("audience", wrong, [wrong_head] * 4, False),
        ("revoked", revoked, [revoked_head] * 4, False),
    ]
    controls = [{"case": name, "accepted": verify(rows, reports), "expected": expected}
                for name, rows, reports, expected in table]
    return {"control_table": controls,
            "all_controls_match": all(row["accepted"] == row["expected"] for row in controls),
            "terminal_sha256": head, "observer_count": 4, "quorum": 3,
            "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def lineage_manifest_v21(source_bytes):
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

    tree, root = levels(leaves), levels(leaves)[-1][0]

    def proof(index):
        original, output = index, []
        for level, row in enumerate(tree[:-1]):
            sibling = index ^ 1
            if sibling >= len(row):
                sibling = index
            output.append({"level": level, "index": index, "side": "left" if sibling < index else "right",
                           "sha256": row[sibling]})
            index //= 2
        return {"leaf_index": original, "steps": output}

    def verify_path(leaf, item, expected_root):
        value, index = leaf, item["leaf_index"]
        for level, step in enumerate(item["steps"]):
            expected_side = "left" if (index ^ 1) < index else "right"
            if step["level"] != level or step["index"] != index or step["side"] != expected_side:
                return False
            value = hashlib.sha256(((step["sha256"] + value) if step["side"] == "left"
                                    else (value + step["sha256"])).encode()).hexdigest()
            index //= 2
        return value == expected_root

    inclusion = {member: {"leaf": leaves[i], "proof": proof(i)} for i, member in enumerate(members)}
    absent = [
        {"id": "h1a", "lower_id": "h1", "upper_id": "h2",
         "lower": inclusion["h1"], "upper": inclusion["h2"]},
        {"id": "t2a", "lower_id": "t2", "upper_id": "t3",
         "lower": inclusion["t2"], "upper": inclusion["t3"]},
    ]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 20, "source_sha256": source_sha})
    config = canonical_hash({"model": "synthetic-v21"})
    body = {"schema_version": 21, "parent_manifest_sha256": parent,
            "source_sha256": source_sha, "provenance_merkle_root": root,
            "inclusion": inclusion, "nonmembership_fixtures": absent,
            "config_sha256": config,
            "heldout_metric": {"name": "fixture_loss", "value": 0.17, "unit": "1", "split": "test"},
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        paths, nonmembers = candidate.get("inclusion", {}), candidate.get("nonmembership_fixtures", [])
        metric = candidate.get("heldout_metric", {})
        return (candidate.get("schema_version") == 21
                and candidate.get("parent_manifest_sha256") == parent
                and candidate.get("source_sha256") == source_sha
                and candidate.get("provenance_merkle_root") == root
                and candidate.get("config_sha256") == config
                and set(paths) == set(members)
                and all(verify_path(item["leaf"], item["proof"], root) for item in paths.values())
                and len(nonmembers) == 2
                and all(item["lower_id"] < item["id"] < item["upper_id"] and item["id"] not in members
                        and verify_path(item["lower"]["leaf"], item["lower"]["proof"], root)
                        and verify_path(item["upper"]["leaf"], item["upper"]["proof"], root)
                        for item in nonmembers)
                and set(metric) == {"name", "value", "unit", "split"} and metric.get("split") == "test"
                and candidate.get("manifest_sha256") == canonical_hash(unsigned))

    mutations = {"root": {**manifest, "provenance_merkle_root": "0" * 64},
                 "source": {**manifest, "source_sha256": "0" * 64},
                 "schema": {**manifest, "schema_version": 20},
                 "config": {**manifest, "config_sha256": "0" * 64},
                 "metric": {**manifest, "heldout_metric": {"name": "fixture_loss"}}}
    path_mutation = json.loads(json.dumps(manifest))
    path_mutation["inclusion"]["h1"]["proof"]["steps"][0]["side"] = "left"
    mutations["direction"] = path_mutation
    index_mutation = json.loads(json.dumps(manifest))
    index_mutation["inclusion"]["h1"]["proof"]["leaf_index"] = 1
    mutations["index"] = index_mutation
    return {"manifest": manifest, "leaf_count": len(leaves), "nonmembership_count": len(absent),
            "valid_manifest": verify(manifest),
            "mutation_rejections": {key: not verify(value) for key, value in mutations.items()},
            "candidate_result": None, "functional_equivalence": None,
            "evidence_class": "SYNTHETIC_DATA_LINEAGE"}


def nine_inverse_pairs_resource_merkle():
    mask = 0b001011

    def pair_swap(v):
        return sum((((v >> low) & 1) << (low + 1)) | (((v >> (low + 1)) & 1) << low)
                   for low in (0, 2, 4))

    def reverse(v):
        return sum(((v >> bit) & 1) << (5 - bit) for bit in range(6))

    operations = [
        ("xor", lambda v: v ^ mask, lambda v: v ^ mask, 6, 6),
        ("rotate", lambda v: ((v << 1) & 63) | (v >> 5), lambda v: (v >> 1) | ((v & 1) << 5), 10, 6),
        ("pair-swap", pair_swap, pair_swap, 6, 6), ("bit-reverse", reverse, reverse, 15, 6),
        ("add-nine", lambda v: (v + 9) % 64, lambda v: (v - 9) % 64, 21, 6),
        ("multiply-five", lambda v: (v * 5) % 64, lambda v: (v * 13) % 64, 30, 6),
        ("multiply-twenty-one", lambda v: (v * 21) % 64, lambda v: (v * 61) % 64, 35, 6),
        ("add-seventeen", lambda v: (v + 17) % 64, lambda v: (v - 17) % 64, 41, 6),
        ("xor-high", lambda v: v ^ 0b110000, lambda v: v ^ 0b110000, 12, 6),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    def tree(items):
        level = [{"hash": canonical_hash({"name": name, "gates": gates, "qubits": qubits}),
                  "gates": gates, "max_qubits": qubits} for name, _, _, gates, qubits in items]
        while len(level) > 1:
            if len(level) % 2:
                level.append({"hash": canonical_hash({"padding": True,
                                                        "level_width": len(level)}),
                              "gates": 0, "max_qubits": 0})
            next_level = []
            for i in range(0, len(level), 2):
                gates = level[i]["gates"] + level[i + 1]["gates"]
                qubits = max(level[i]["max_qubits"], level[i + 1]["max_qubits"])
                next_level.append({"hash": canonical_hash({"left": level[i]["hash"],
                                                           "right": level[i + 1]["hash"],
                                                           "gates": gates, "max_qubits": qubits}),
                                   "gates": gates, "max_qubits": qubits})
            level = next_level
        return level[0]

    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, inverse=True) for value in encoded]
    mutated = [operations[1], operations[0], *operations[2:]]
    root = tree(operations)
    resource_mutation = [*operations[:8], (operations[8][0], operations[8][1], operations[8][2], 11, 6)]
    return {"inverse_pair_names": [item[0] for item in operations],
            "resource_merkle_root_sha256": root["hash"], "tree_resource_sum": root["gates"],
            "tree_max_qubits": root["max_qubits"],
            "tree_mutation_rejected": tree(resource_mutation)["hash"] != root["hash"],
            "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
            "residual": sum(a != b for a, b in enumerate(reconstructed)),
            "order_mutation_witness_count": sum(a != apply(value, mutated) for value, a in enumerate(encoded)),
            "resource_bound": {"gates": root["gates"], "max_qubits": root["max_qubits"]},
            "hardware": None, "evidence_class": "SYNTHETIC_INVERSE_OPERATOR"}


def run_cycle031_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": eleventh_graph_witness_quotient(),
            "B": unicode_value_receipt_gate(),
            "C": five_reader_descriptor_atomicity(work),
            "D": zip64_name_version_bind(),
            "E": eleven_issuer_revocation_quorum(),
            "F": fifteen_component_ordered_covariance(source_bytes),
            "G": composed_signed_block_transforms(),
            "H": fifteen_scenario_deletion_intervals(),
            "FND/EQN": eight_source_affine_maps(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight"),
            "SCM": transcript_equivocation_quorum_controls(),
            "AI-COST": lineage_manifest_v21(source_bytes),
            "QOS/QSVT": nine_inverse_pairs_resource_merkle(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
