"""Cycle 032 bounded fixtures; results remain local, synthetic, model, or fiction evidence."""
from __future__ import annotations

from decimal import Decimal, InvalidOperation
from fractions import Fraction
import hashlib
import itertools
import json
import math
from pathlib import Path
import struct
import tempfile
import threading
import time
import unicodedata

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle015_delta01 import (
    component_covariance_sweep,
    concurrent_subprocess_replace,
    make_custody_event,
    verify_custody_chain,
)

LANES = (
    "A", "B", "C", "D", "E", "F", "G", "H",
    "FND/EQN", "SCM", "AI-COST", "QOS/QSVT",
)


def twelfth_graph_burnside_quotient():
    n, full_mask = 11, (1 << 11) - 1

    def solve(weights):
        edges = [[i, (i + 1) % n, weights[i]] for i in range(n)]
        scores = [sum(weight for u, v, weight in edges
                      if ((mask >> u) & 1) != ((mask >> v) & 1))
                  for mask in range(1 << n)]
        optimum = max(scores)
        witnesses = [mask for mask, score in enumerate(scores) if score == optimum]
        return {"states": len(scores), "objective": optimum, "witnesses": witnesses,
                "task_sha256": canonical_hash(edges),
                "witness_sha256": canonical_hash(witnesses)}

    def transform_weights(weights, sign, shift):
        transformed = [0] * n
        for index, value in enumerate(weights):
            u, v = (sign * index + shift) % n, (sign * (index + 1) + shift) % n
            transformed[min(u, v) if abs(u - v) == 1 else max(u, v)] = value
        return transformed

    def transform_mask(mask, sign, shift, complement=False):
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full_mask if complement else 0)

    eleventh = [1] * n
    for index, weight in ((0, 8), (1, 5), (2, 9), (3, 2), (5, 4), (7, 7), (8, 3), (10, 6)):
        eleventh[index] = weight
    twelfth = list(eleventh)
    twelfth[4] = 11
    prior, current = solve(eleventh), solve(twelfth)
    dihedral, stabilizer = [], []
    for sign in (1, -1):
        for shift in range(n):
            transformed_weights = transform_weights(twelfth, sign, shift)
            transformed = solve(transformed_weights)
            expected = sorted(transform_mask(mask, sign, shift) for mask in current["witnesses"])
            dihedral.append(transformed["witnesses"] == expected)
            if transformed_weights == twelfth:
                stabilizer.append((sign, shift))

    actions = [(sign, shift, complement) for sign, shift in stabilizer
               for complement in (False, True)]
    witness_set, remaining, quotient = set(current["witnesses"]), set(current["witnesses"]), []
    while remaining:
        seed = min(remaining)
        orbit = sorted({transform_mask(seed, *action) for action in actions} & witness_set)
        quotient.append(orbit)
        remaining.difference_update(orbit)
    fixed_counts = [sum(transform_mask(mask, *action) == mask for mask in current["witnesses"])
                    for action in actions]
    burnside_numerator = sum(fixed_counts)
    return {
        "states_each": [prior["states"], current["states"]],
        "objectives": [prior["objective"], current["objective"]],
        "witness_counts": [len(prior["witnesses"]), len(current["witnesses"])],
        "changed_edge_indices": [4],
        "unchanged_edges_identical": all(eleventh[i] == twelfth[i] for i in range(n) if i != 4),
        "dihedral_transform_count": len(dihedral),
        "all_dihedral_transforms_match": all(dihedral),
        "stabilizer": [[sign, shift] for sign, shift in stabilizer],
        "action_count": len(actions),
        "direct_quotient": quotient,
        "fixed_point_counts": fixed_counts,
        "burnside_numerator": burnside_numerator,
        "burnside_orbit_count": burnside_numerator // len(actions),
        "burnside_matches_direct": burnside_numerator % len(actions) == 0
        and burnside_numerator // len(actions) == len(quotient),
        "quotient_sha256": canonical_hash(quotient),
        "complete_witness_sha256": current["witness_sha256"],
        "deterministic": current == solve(twelfth),
        "scaling_claim": None,
        "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def recursive_unicode_numeric_receipt_gate():
    caps = {"bytes": 384, "depth": 6, "tokens": 32, "normalized_string_length": 18,
            "max_exact_integer": 2 ** 53 - 1, "magnitude": "1e12"}

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
        if isinstance(value, Decimal):
            if not value.is_finite() or abs(value) > Decimal(caps["magnitude"]):
                raise ValueError("decimal cap")
            if value == 0:
                return {"$decimal": "0"}
            normalized = value.normalize()
            return {"$decimal": format(normalized, "f")}
        if isinstance(value, int) and not isinstance(value, bool):
            if abs(value) > caps["max_exact_integer"]:
                raise ValueError("integer cap")
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

    def bounded(raw):
        if len(raw) > caps["bytes"]:
            raise ValueError("byte cap")
        parsed = json.loads(raw.decode("utf-8"), object_pairs_hook=pairs,
                            parse_float=Decimal,
                            parse_constant=lambda _: (_ for _ in ()).throw(ValueError("constant")))
        if depth(parsed) > caps["depth"] or tokens(parsed) > caps["tokens"]:
            raise ValueError("shape cap")
        value = normalize(parsed)
        return json.dumps(value, sort_keys=True, separators=(",", ":"),
                          ensure_ascii=False, allow_nan=False).encode("utf-8")

    first = '{"outer":{"label":"é","rate":1.20e1,"z":-0.0},"max":9007199254740991}'.encode()
    equivalent = b'{"max":9007199254740991,"outer":{"z":0e3,"rate":12.0,"label":"e\\u0301"}}'
    cases = {
        "normalized_key_collision": '{"é":1,"é":2}'.encode(),
        "literal_duplicate": b'{"a":1,"a":2}',
        "depth": b'{"a":{"b":{"c":{"d":{"e":{"f":{"g":1}}}}}}}',
        "token_cap": json.dumps({"v": list(range(33))}).encode(),
        "integer_precision": b'{"v":9007199254740992}',
        "nonfinite": b'{"v":Infinity}',
        "decimal_magnitude": b'{"v":1.1e12}',
        "string_length": json.dumps({"v": "x" * 19}).encode(),
    }
    controls = {}
    for name, raw in cases.items():
        try:
            bounded(raw)
            controls[name] = False
        except (ValueError, UnicodeError, json.JSONDecodeError, InvalidOperation):
            controls[name] = True
    canonical = bounded(first)
    return {
        "recursive_numeric_equivalence": canonical == bounded(equivalent),
        "canonical_sha256": hashlib.sha256(canonical).hexdigest(),
        "caps": caps,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def six_reader_chained_atomicity(directory):
    root = Path(directory)
    root.mkdir(parents=True, exist_ok=True)
    rows = []
    for run in range(3):
        target_name = f"six-reader-{run % 2}.bin"
        target = root / target_name
        if not target.exists():
            target.write_bytes(b"old-complete-payload")
        old = target.read_bytes()
        first_payloads = [f"cycle032-first-{run}-{writer}".encode() for writer in range(3)]
        second_payloads = [f"cycle032-second-{run}-{writer}".encode() for writer in range(3)]
        allowed = {old, *first_payloads, *second_payloads}
        pre_names = sorted(path.name for path in root.iterdir())
        with target.open("rb") as held_old:
            old_inode = target.stat().st_ino
            stop = threading.Event()
            barrier = threading.Barrier(7)
            observations = [[] for _ in range(6)]

            def reader(index):
                barrier.wait()
                while not stop.is_set():
                    try:
                        observations[index].append((target.read_bytes(), target.stat().st_ino))
                    except FileNotFoundError:
                        observations[index].append((b"", -1))
                    time.sleep(0.0005)

            threads = [threading.Thread(target=reader, args=(index,)) for index in range(6)]
            for thread in threads:
                thread.start()
            barrier.wait()
            first = concurrent_subprocess_replace(root, target_name, first_payloads)
            with target.open("rb") as held_middle:
                middle = target.read_bytes()
                middle_inode = target.stat().st_ino
                second = concurrent_subprocess_replace(root, target_name, second_payloads)
                time.sleep(0.003)
                held_middle.seek(0)
                held_middle_bytes = held_middle.read()
            stop.set()
            for thread in threads:
                thread.join(timeout=2)
            held_old.seek(0)
            held_old_bytes = held_old.read()
        rows.append({
            "run": run,
            "reader_counts": [len(items) for items in observations],
            "reader_complete": [bool(items) and all(data in allowed for data, _ in items)
                                for items in observations],
            "held_old_complete": held_old_bytes == old,
            "held_middle_complete": held_middle_bytes == middle and middle in set(first_payloads),
            "old_inode": old_inode,
            "middle_inode": middle_inode,
            "final_inode": target.stat().st_ino,
            "pre_directory_names": pre_names,
            "post_directory_names": sorted(path.name for path in root.iterdir()),
            "parent_complete": first["visible_complete"] and second["visible_complete"],
            "exit_codes": [first["exit_codes"], second["exit_codes"]],
        })
    return {
        "runs": rows,
        "reader_count": 6,
        "replacement_stages": 2,
        "all_reader_parent_observations_complete": all(
            all(row["reader_complete"]) and row["parent_complete"] for row in rows
        ),
        "all_retained_descriptors_complete": all(
            row["held_old_complete"] and row["held_middle_complete"] for row in rows
        ),
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_SIX_READER_FIXTURE",
    }


def zip64_eocd_locator_bind():
    name = "cycle032-Ω.bin".encode("utf-8")
    expected = {"needed": 45, "extract": 45, "flags": 0x808, "method": 8,
                "crc": 0x10203040, "compressed": 71, "uncompressed": 97,
                "entries": 1, "central_size": 83, "central_offset": 4096,
                "eocd_offset": 4179}

    def header(needed=45, extract=45, flags=0x808, method=8, filename=name):
        return struct.pack("<HHHHH", needed, extract, flags, method, len(filename)) + filename

    def parse_header(raw):
        needed, extract, flags, method, width = struct.unpack_from("<HHHHH", raw)
        filename = raw[10:]
        if (len(filename) != width or (needed, extract, flags, method) !=
                (expected["needed"], expected["extract"], expected["flags"], expected["method"])):
            raise ValueError("header")
        if not flags & 0x800 or filename.decode("utf-8") != name.decode("utf-8"):
            raise ValueError("name")
        return filename

    def extra(identifier, body):
        return struct.pack("<HH", identifier, len(body)) + body

    zip64_extra = extra(0x0001, struct.pack("<QQ", expected["uncompressed"], expected["compressed"]))
    opaque = extra(0xD032, b"opaque-032")

    def parse_extras(raw):
        offset, output = 0, {}
        while offset < len(raw):
            identifier, width = struct.unpack_from("<HH", raw, offset)
            offset += 4
            if identifier in output or offset + width > len(raw):
                raise ValueError("extra")
            output[identifier] = raw[offset:offset + width]
            offset += width
        if 0x0001 not in output or struct.unpack("<QQ", output[0x0001]) != (
                expected["uncompressed"], expected["compressed"]):
            raise ValueError("zip64 extra")
        return output

    def descriptor(signed=True, crc=None):
        body = struct.pack("<IQQ", expected["crc"] if crc is None else crc,
                           expected["compressed"], expected["uncompressed"])
        return (b"PK\x07\x08" + body) if signed else body

    def eocd(entries=1, central_size=83, central_offset=4096):
        return struct.pack("<IQHHIIQQQQ", 0x06064B50, 44, 45, 45, 0, 0,
                           entries, entries, central_size, central_offset)

    def locator(disk=0, offset=4179, disks=1):
        return struct.pack("<IIQI", 0x07064B50, disk, offset, disks)

    def verify(local, central, raw_descriptor, local_extra, central_extra, raw_eocd, raw_locator):
        if parse_header(local) != parse_header(central):
            raise ValueError("header mismatch")
        if parse_extras(local_extra) != parse_extras(central_extra):
            raise ValueError("extra mismatch")
        body = raw_descriptor[4:] if len(raw_descriptor) == 24 and raw_descriptor[:4] == b"PK\x07\x08" else raw_descriptor
        if len(body) != 20 or struct.unpack("<IQQ", body) != (
                expected["crc"], expected["compressed"], expected["uncompressed"]):
            raise ValueError("descriptor")
        signature, size, made, needed, disk, start_disk, entries_disk, entries_total, size_cd, offset_cd = struct.unpack(
            "<IQHHIIQQQQ", raw_eocd)
        if (signature, size, needed, disk, start_disk, entries_disk, entries_total, size_cd, offset_cd) != (
                0x06064B50, 44, 45, 0, 0, expected["entries"], expected["entries"],
                expected["central_size"], expected["central_offset"]):
            raise ValueError("eocd")
        loc_signature, loc_disk, loc_offset, disks = struct.unpack("<IIQI", raw_locator)
        if (loc_signature, loc_disk, loc_offset, disks) != (
                0x07064B50, 0, expected["eocd_offset"], 1):
            raise ValueError("locator")
        return made == 45

    valid = (header(), header(), descriptor(), zip64_extra + opaque, opaque + zip64_extra, eocd(), locator())
    cases = {
        "name": (header(filename=b"other.bin"), *valid[1:]),
        "version": (header(needed=20), *valid[1:]),
        "flags": (header(flags=8), *valid[1:]),
        "descriptor": (header(), header(), descriptor(crc=0), *valid[3:]),
        "extra_duplicate": (header(), header(), descriptor(), zip64_extra * 2, *valid[4:]),
        "eocd_count": (*valid[:5], eocd(entries=2), valid[6]),
        "eocd_size": (*valid[:5], eocd(central_size=82), valid[6]),
        "eocd_offset": (*valid[:5], eocd(central_offset=4095), valid[6]),
        "locator_disk": (*valid[:6], locator(disk=1)),
        "locator_offset": (*valid[:6], locator(offset=4178)),
        "locator_disks": (*valid[:6], locator(disks=2)),
    }
    controls = {}
    for key, args in cases.items():
        try:
            verify(*args)
            controls[key] = False
        except (ValueError, UnicodeError, struct.error):
            controls[key] = True
    return {
        "signed_unsigned_valid": [verify(*valid), verify(header(), header(), descriptor(False),
                                                               zip64_extra + opaque, opaque + zip64_extra,
                                                               eocd(), locator())],
        "filename_utf8": name.decode("utf-8"),
        "eocd_record_size": len(eocd()),
        "locator_size": len(locator()),
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_METADATA",
    }


def twelve_issuer_threshold_receipts():
    sample = hashlib.sha256(b"cycle032-synthetic-custody").hexdigest()
    specs = [(f"issuer-{chr(97 + i)}", f"scope-{i:02d}") for i in range(12)]
    starts = [f"2026-{month:02d}-01" for month in range(1, 13)]
    authorities = {"rev-a": "synthetic-key-a", "rev-b": "synthetic-key-b", "rev-c": "synthetic-key-c"}

    def build(path="fixture-032"):
        events, prior = [], "0" * 64
        for sequence, ((issuer, scope), start) in enumerate(zip(specs, starts)):
            event = make_custody_event(sequence, sample, path, issuer, scope,
                                       start, "2027-02-01", prior)
            events.append(event)
            prior = event["event_sha256"]
        return events

    def receipt(signer, head, revoked=False):
        body = {"signer": signer, "head_sha256": head, "revoked": revoked, "epoch": 32}
        return {**body, "synthetic_signature": canonical_hash({**body, "key": authorities[signer]})}

    registry = {issuer: {scope} for issuer, scope in specs}
    ancestry = {"issuer-l": "issuer-k", "issuer-k": "issuer-j"}

    def verify(events, receipts, bound_registry=registry, bound_ancestry=ancestry,
               now="2026-12-01"):
        head = events[-1]["event_sha256"]
        signers = set()
        votes = []
        for item in receipts:
            signer = item.get("signer")
            unsigned = {key: value for key, value in item.items() if key != "synthetic_signature"}
            if (signer not in authorities or signer in signers or item.get("head_sha256") != head
                    or item.get("epoch") != 32
                    or item.get("synthetic_signature") != canonical_hash({**unsigned, "key": authorities[signer]})):
                raise ValueError("receipt")
            signers.add(signer)
            votes.append(bool(item["revoked"]))
        if len(signers) < 2 or sum(votes) >= 2:
            raise ValueError("revocation threshold")
        if any(event["path_id"] != "fixture-032" for event in events):
            raise ValueError("path")
        if bound_ancestry != ancestry:
            raise ValueError("ancestry")
        if not (max(event["valid_from"] for event in events) <= now
                <= min(event["expires_at"] for event in events)):
            raise ValueError("window")
        return verify_custody_chain(events, bound_registry, now)

    events = build()
    head = events[-1]["event_sha256"]
    valid_receipts = [receipt("rev-a", head), receipt("rev-b", head)]
    valid = verify(events, valid_receipts)
    cases = {
        "insufficient_quorum": (events, valid_receipts[:1], registry, ancestry, "2026-12-01"),
        "revoked_quorum": (events, [receipt("rev-a", head, True), receipt("rev-b", head, True)], registry, ancestry, "2026-12-01"),
        "duplicate_signer": (events, [receipt("rev-a", head), receipt("rev-a", head)], registry, ancestry, "2026-12-01"),
        "head_substitution": (events, [receipt("rev-a", "0" * 64), receipt("rev-b", "0" * 64)], registry, ancestry, "2026-12-01"),
        "signature": (events, [{**valid_receipts[0], "synthetic_signature": "0" * 64}, valid_receipts[1]], registry, ancestry, "2026-12-01"),
        "scope": (events, valid_receipts, {**registry, "issuer-l": {"wrong"}}, ancestry, "2026-12-01"),
        "ancestry": (events, valid_receipts, registry, {"issuer-l": "issuer-j"}, "2026-12-01"),
        "time": (events, valid_receipts, registry, ancestry, "2026-11-30"),
        "path": (build("other"), valid_receipts, registry, ancestry, "2026-12-01"),
    }
    controls = {}
    for key, args in cases.items():
        try:
            verify(*args)
            controls[key] = False
        except ValueError:
            controls[key] = True
    return {
        "event_count": 12,
        "receipt_authority_count": 3,
        "receipt_threshold": 2,
        "terminal_sha256": valid["final_event_sha256"],
        "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def sixteen_component_block_covariance(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    n = 16
    order = [f"component-{i:02d}" for i in range(n)]
    blocks = ["compute"] * 4 + ["memory"] * 4 + ["network"] * 4 + ["control"] * 4
    intervals = [[i + 1, i + 6] for i in range(n)]
    matrices = {
        "positive": [[0.025 if i == j else (0.0002 if blocks[i] == blocks[j] else 0.00005)
                      for j in range(n)] for i in range(n)],
        "zero": [[0.025 if i == j else 0.0 for j in range(n)] for i in range(n)],
        "negative": [[0.025 if i == j else -0.0004 for j in range(n)] for i in range(n)],
        "missing": None,
        "indefinite": [[1.0 if i == j else 2.0 for j in range(n)] for i in range(n)],
        "nonfinite": [[float("nan") if i == j == 0 else (1.0 if i == j else 0.0)
                       for j in range(n)] for i in range(n)],
    }
    sigmas = [0.0, 1.0, 2.0, 3.0, 5.0, 8.0, 13.0, 21.0]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    binding = {"source_sha256": source_sha, "order": order, "blocks": blocks,
               "row_labels": order, "column_labels": order,
               "matrix_names": sorted(matrices), "sigmas": sigmas}
    mutations = {
        "component_order": {**binding, "order": list(reversed(order))},
        "block_layout": {**binding, "blocks": list(reversed(blocks))},
        "row_labels": {**binding, "row_labels": [*order[1:], order[0]]},
        "column_labels": {**binding, "column_labels": [*order[-1:], *order[:-1]]},
    }
    identity = canonical_hash(binding)
    return {
        "components": n,
        "source_sha256": source_sha,
        "component_order": order,
        "block_layout": blocks,
        "covariance_grid_sha256": identity,
        "binding_mutation_rejections": {key: canonical_hash(value) != identity
                                         for key, value in mutations.items()},
        "sigma_values": sigmas,
        "sweeps": {str(s): component_covariance_sweep(intervals, matrices, [1, 8, 16, 0], sigma=s)
                   for s in sigmas},
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def three_signed_block_transforms():
    covariance = [
        [Fraction(9), Fraction(1), Fraction(2), Fraction(1)],
        [Fraction(1), Fraction(16), Fraction(1), Fraction(2)],
        [Fraction(2), Fraction(1), Fraction(25), Fraction(1)],
        [Fraction(1), Fraction(2), Fraction(1), Fraction(49)],
    ]
    transforms = [
        ([1, 0, 3, 2], [1, -1, 1, -1]),
        ([2, 3, 0, 1], [-1, 1, -1, 1]),
        ([3, 2, 1, 0], [1, 1, -1, -1]),
    ]

    def apply(matrix, transform):
        permutation, signs = transform
        return [[signs[i] * signs[j] * matrix[permutation[i]][permutation[j]]
                 for j in range(4)] for i in range(4)]

    def inverse(matrix, transform):
        permutation, signs = transform
        inv = [permutation.index(i) for i in range(4)]
        return [[signs[inv[i]] * signs[inv[j]] * matrix[inv[i]][inv[j]]
                 for j in range(4)] for i in range(4)]

    def compose(first, second):
        permutation = [first[0][second[0][i]] for i in range(4)]
        signs = [second[1][i] * first[1][second[0][i]] for i in range(4)]
        return permutation, signs

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

    sequential = covariance
    for transform in transforms:
        sequential = apply(sequential, transform)
    left = apply(covariance, compose(compose(transforms[0], transforms[1]), transforms[2]))
    right = apply(covariance, compose(transforms[0], compose(transforms[1], transforms[2])))
    restored = sequential
    for transform in reversed(transforms):
        restored = inverse(restored, transform)
    return {
        "transform_count": 3,
        "matrix_product_count": 48,
        "associative_composition": sequential == left == right,
        "exact_reverse_order_roundtrip": restored == covariance,
        "trace_invariant": sum(sequential[i][i] for i in range(4)) == sum(covariance[i][i] for i in range(4)),
        "determinant_invariant": determinant(sequential) == determinant(covariance),
        "symmetric": all(sequential[i][j] == sequential[j][i] for i in range(4) for j in range(4)),
        "psd_by_signed_permutation_congruence": True,
        "composition_sha256": canonical_hash({"permutations": [item[0] for item in transforms],
                                                "signs": [item[1] for item in transforms]}),
        "calibration": None,
        "evidence_class": "SYNTHETIC_TYPED_COVARIANCE",
    }


def sixteen_scenario_deletion_intervals():
    scenarios = [
        [4, 3, 2, 1], [2, 2, 1, 0], [2, 1, 2, 0], [1, 1, 1, 1],
        [0, 3, 2, 3], [0, 1, 2, 3], [3, 0, 3, 1], [1, 4, 0, 4],
        [2, 4, 4, 1], [4, 0, 1, 4], [3, 2, 4, 0], [0, 4, 3, 2],
        [4, 2, 0, 3], [1, 3, 4, 2], [2, 0, 4, 3], [3, 4, 1, 2],
    ]

    def contribution(scores):
        eligible = {i for i, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return output

    contributions = [contribution(scores) for scores in scenarios]
    full = [sum(row[i] for row in contributions) for i in range(4)]
    fractions = [Fraction(value, 16 * 24) for value in full]
    grid_counts = {}
    for removed_count in range(1, 9):
        count = 0
        denominator = (16 - removed_count) * 24
        for removed in itertools.combinations(range(16), removed_count):
            count += 1
            row = [full[i] - sum(contributions[index][i] for index in removed) for i in range(4)]
            fractions.extend(Fraction(value, denominator) for value in row)
        grid_counts[str(removed_count)] = count
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 16,
        "orders_each": 24,
        "full_grid_size": 384,
        "winner_counts": full,
        "deletion_grid_counts": grid_counts,
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def nine_source_affine_associativity(*raw_sources):
    if len(raw_sources) != 9 or any(not isinstance(item, bytes) or not item for item in raw_sources):
        raise ValueError("nine source bytes")
    sources = [hashlib.sha256(item).hexdigest() for item in raw_sources]
    if len(set(sources)) != 9:
        raise ValueError("independent sources")
    maps = [
        (Fraction(3, 2), Fraction(1, 3)), (Fraction(5, 4), Fraction(-1, 5)),
        (Fraction(7, 6), Fraction(2, 7)), (Fraction(9, 8), Fraction(0)),
        (Fraction(11, 10), Fraction(1, 11)), (Fraction(13, 12), Fraction(-1, 13)),
        (Fraction(17, 16), Fraction(1, 17)), (Fraction(19, 18), Fraction(-1, 19)),
        (Fraction(23, 22), Fraction(1, 23)),
    ]

    def combine(first, second):
        return second[0] * first[0], second[0] * first[1] + second[1]

    def compose(bound_sources, bound_maps, dimension, mode="left"):
        if bound_sources != sources or dimension != [1, 0, 0, 0]:
            raise ValueError("source/dimension")
        if any(slope <= 0 for slope, _ in bound_maps):
            raise ValueError("nonmonotone")
        if mode == "left":
            result = (Fraction(1), Fraction(0))
            for item in bound_maps:
                result = combine(result, item)
            return result
        if len(bound_maps) == 1:
            return bound_maps[0]
        middle = len(bound_maps) // 2
        return combine(compose(bound_sources, bound_maps[:middle], dimension, "balanced"),
                       compose(bound_sources, bound_maps[middle:], dimension, "balanced"))

    left = compose(sources, maps, [1, 0, 0, 0])
    balanced = compose(sources, maps, [1, 0, 0, 0], "balanced")
    original = (Fraction(2, 3), Fraction(5, 3))
    transformed = tuple(left[0] * value + left[1] for value in original)
    restored = tuple((value - left[1]) / left[0] for value in transformed)
    cases = {
        "source_order": (list(reversed(sources)), maps, [1, 0, 0, 0]),
        "dimension": (sources, maps, [0, 1, 0, 0]),
        "nonmonotone": (sources, [*maps[:8], (Fraction(0), Fraction(0))], [1, 0, 0, 0]),
    }
    controls = {}
    for key, args in cases.items():
        try:
            compose(*args)
            controls[key] = False
        except ValueError:
            controls[key] = True
    return {
        "source_sha256": sources,
        "map_count": len(maps),
        "associative_composition": left == balanced,
        "composed_interval": [[value.numerator, value.denominator] for value in transformed],
        "roundtrip_interval": [[value.numerator, value.denominator] for value in restored],
        "exact_roundtrip": restored == original,
        "negative_controls": controls,
        "sort": ["RealModel", "Model"],
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def five_observer_branch_certificate():
    def build(audience="fiction-032", epoch=13, active=True):
        rows, prior = [], "0" * 64
        for sequence in range(1, 7):
            body = {"sequence": sequence, "epoch": epoch, "audience": audience,
                    "active": active, "payload": f"row-{sequence}", "previous_sha256": prior}
            row = {**body, "row_sha256": canonical_hash(body)}
            rows.append(row)
            prior = row["row_sha256"]
        return rows, prior

    def verify(rows, reports, audience="fiction-032", minimum_epoch=13):
        prior = "0" * 64
        for expected, row in enumerate(rows, start=1):
            unsigned = {key: value for key, value in row.items() if key != "row_sha256"}
            if (row["sequence"] != expected or row["epoch"] < minimum_epoch
                    or row["audience"] != audience or not row["active"]
                    or row["previous_sha256"] != prior or row["row_sha256"] != canonical_hash(unsigned)):
                return False
            prior = row["row_sha256"]
        counts = {head: reports.count(head) for head in set(reports)}
        return len(reports) == 5 and counts.get(prior, 0) >= 4

    valid, head = build()
    fork = json.loads(json.dumps(valid))
    fork[3]["payload"] = "fork"
    fork[3]["row_sha256"] = canonical_hash({k: v for k, v in fork[3].items() if k != "row_sha256"})
    replay = [*valid[:4], valid[3], *valid[5:]]
    downgraded, down_head = build(epoch=12)
    wrong, wrong_head = build(audience="other")
    revoked, revoked_head = build(active=False)
    table = [
        ("valid", valid, [head] * 5, True),
        ("split_quorum", valid, [head] * 3 + ["f" * 64] * 2, False),
        ("stale_quorum", valid, [valid[-2]["row_sha256"]] * 4 + [head], False),
        ("fork", fork, [head] * 5, False),
        ("replay", replay, [head] * 5, False),
        ("downgrade", downgraded, [down_head] * 5, False),
        ("audience", wrong, [wrong_head] * 5, False),
        ("revoked", revoked, [revoked_head] * 5, False),
    ]
    controls = [{"case": name, "accepted": verify(rows, reports), "expected": expected}
                for name, rows, reports, expected in table]
    return {
        "control_table": controls,
        "all_controls_match": all(row["accepted"] == row["expected"] for row in controls),
        "terminal_sha256": head,
        "observer_count": 5,
        "quorum": 4,
        "sort": "Fiction",
        "empirical_coupling": None,
        "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v22(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    members = ["h1", "h2", "h3", "t1", "t2", "t3", "v1", "v2"]
    leaves = [canonical_hash({"domain": "uqpu-lineage-leaf-v22", "id": member}) for member in members]

    def build_levels(items):
        output = [list(items)]
        while len(output[-1]) > 1:
            row = list(output[-1])
            if len(row) % 2:
                row.append(row[-1])
            output.append([canonical_hash({"domain": "uqpu-lineage-node-v22",
                                           "left": row[i], "right": row[i + 1]})
                           for i in range(0, len(row), 2)])
        return output

    levels = build_levels(leaves)
    root = levels[-1][0]

    def proof(index):
        original, steps = index, []
        for level, row in enumerate(levels[:-1]):
            sibling = index ^ 1
            if sibling >= len(row):
                sibling = index
            steps.append({"level": level, "index": index,
                          "side": "left" if sibling < index else "right",
                          "sha256": row[sibling]})
            index //= 2
        return {"leaf_index": original, "steps": steps}

    def verify_path(leaf, item):
        value, index = leaf, item["leaf_index"]
        for level, step in enumerate(item["steps"]):
            expected_side = "left" if (index ^ 1) < index else "right"
            if step["level"] != level or step["index"] != index or step["side"] != expected_side:
                return False
            left, right = ((step["sha256"], value) if step["side"] == "left"
                           else (value, step["sha256"]))
            value = canonical_hash({"domain": "uqpu-lineage-node-v22", "left": left, "right": right})
            index //= 2
        return value == root

    selected = [0, 2, 5, 7]
    multiproof = [{"id": members[index], "leaf": leaves[index], "proof": proof(index)}
                  for index in selected]
    boundaries = [
        {"id": "a0", "upper_id": members[0], "upper": multiproof[0]},
        {"id": "z9", "lower_id": members[-1], "lower": multiproof[-1]},
    ]
    source_sha = hashlib.sha256(source_bytes).hexdigest()
    parent = canonical_hash({"version": 21, "source_sha256": source_sha})
    config = canonical_hash({"model": "synthetic-v22"})
    body = {
        "schema_version": 22,
        "parent_manifest_sha256": parent,
        "source_sha256": source_sha,
        "provenance_merkle_root": root,
        "canonical_multiproof": multiproof,
        "boundary_nonmembership": boundaries,
        "config_sha256": config,
        "heldout_metric": {"name": "fixture_loss", "value": 0.16, "unit": "1", "split": "test"},
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }
    manifest = {**body, "manifest_sha256": canonical_hash(body)}

    def verify(candidate):
        unsigned = {key: value for key, value in candidate.items() if key != "manifest_sha256"}
        proofs = candidate.get("canonical_multiproof", [])
        bounds = candidate.get("boundary_nonmembership", [])
        metric = candidate.get("heldout_metric", {})
        return (candidate.get("schema_version") == 22
                and candidate.get("parent_manifest_sha256") == parent
                and candidate.get("source_sha256") == source_sha
                and candidate.get("provenance_merkle_root") == root
                and candidate.get("config_sha256") == config
                and [item["proof"]["leaf_index"] for item in proofs] == selected
                and [item["id"] for item in proofs] == [members[index] for index in selected]
                and all(verify_path(item["leaf"], item["proof"]) for item in proofs)
                and len(bounds) == 2
                and bounds[0]["id"] < bounds[0]["upper_id"] == members[0]
                and bounds[0]["upper"] == proofs[0]
                and bounds[1]["id"] > bounds[1]["lower_id"] == members[-1]
                and bounds[1]["lower"] == proofs[-1]
                and set(metric) == {"name", "value", "unit", "split"} and metric.get("split") == "test"
                and candidate.get("manifest_sha256") == canonical_hash(unsigned))

    mutations = {
        "root": {**manifest, "provenance_merkle_root": "0" * 64},
        "source": {**manifest, "source_sha256": "0" * 64},
        "schema": {**manifest, "schema_version": 21},
        "config": {**manifest, "config_sha256": "0" * 64},
        "metric": {**manifest, "heldout_metric": {"name": "fixture_loss"}},
    }
    order_mutation = json.loads(json.dumps(manifest))
    order_mutation["canonical_multiproof"][0], order_mutation["canonical_multiproof"][1] = (
        order_mutation["canonical_multiproof"][1], order_mutation["canonical_multiproof"][0])
    mutations["proof_order"] = order_mutation
    path_mutation = json.loads(json.dumps(manifest))
    path_mutation["canonical_multiproof"][0]["proof"]["steps"][0]["side"] = "left"
    mutations["direction"] = path_mutation
    index_mutation = json.loads(json.dumps(manifest))
    index_mutation["canonical_multiproof"][0]["proof"]["leaf_index"] = 1
    mutations["index"] = index_mutation
    boundary_mutation = json.loads(json.dumps(manifest))
    boundary_mutation["boundary_nonmembership"][0]["id"] = "z0"
    mutations["boundary"] = boundary_mutation
    return {
        "manifest": manifest,
        "leaf_count": len(leaves),
        "multiproof_leaf_count": len(multiproof),
        "boundary_nonmembership_count": len(boundaries),
        "valid_manifest": verify(manifest),
        "mutation_rejections": {key: not verify(value) for key, value in mutations.items()},
        "candidate_result": None,
        "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def ten_inverse_pairs_merkle_proofs():
    mask = 0b001011

    def pair_swap(value):
        return sum((((value >> low) & 1) << (low + 1))
                   | (((value >> (low + 1)) & 1) << low) for low in (0, 2, 4))

    def reverse(value):
        return sum(((value >> bit) & 1) << (5 - bit) for bit in range(6))

    operations = [
        ("xor", lambda v: v ^ mask, lambda v: v ^ mask, 6, 6),
        ("rotate", lambda v: ((v << 1) & 63) | (v >> 5), lambda v: (v >> 1) | ((v & 1) << 5), 10, 6),
        ("pair-swap", pair_swap, pair_swap, 6, 6),
        ("bit-reverse", reverse, reverse, 15, 6),
        ("add-nine", lambda v: (v + 9) % 64, lambda v: (v - 9) % 64, 21, 6),
        ("multiply-five", lambda v: (v * 5) % 64, lambda v: (v * 13) % 64, 30, 6),
        ("multiply-twenty-one", lambda v: (v * 21) % 64, lambda v: (v * 61) % 64, 35, 6),
        ("add-seventeen", lambda v: (v + 17) % 64, lambda v: (v - 17) % 64, 41, 6),
        ("xor-high", lambda v: v ^ 0b110000, lambda v: v ^ 0b110000, 12, 6),
        ("bit-not", lambda v: v ^ 63, lambda v: v ^ 63, 6, 6),
    ]

    def apply(value, sequence, inverse=False):
        iterable = reversed(sequence) if inverse else sequence
        for _, forward, backward, _, _ in iterable:
            value = backward(value) if inverse else forward(value)
        return value

    def leaf(name, gates, qubits, index):
        return {"hash": canonical_hash({"domain": "uqpu-resource-leaf-v1", "index": index,
                                         "name": name, "gates": gates, "max_qubits": qubits}),
                "gates": gates, "max_qubits": qubits}

    leaves = [leaf(name, gates, qubits, index)
              for index, (name, _, _, gates, qubits) in enumerate(operations)]
    size = 1
    while size < len(leaves):
        size *= 2
    for index in range(len(leaves), size):
        leaves.append({"hash": canonical_hash({"domain": "uqpu-resource-padding-v1", "index": index}),
                       "gates": 0, "max_qubits": 0})
    levels = [leaves]
    while len(levels[-1]) > 1:
        row, output = levels[-1], []
        for index in range(0, len(row), 2):
            gates = row[index]["gates"] + row[index + 1]["gates"]
            qubits = max(row[index]["max_qubits"], row[index + 1]["max_qubits"])
            output.append({"hash": canonical_hash({"domain": "uqpu-resource-node-v1",
                                                    "left": row[index]["hash"],
                                                    "right": row[index + 1]["hash"],
                                                    "gates": gates, "max_qubits": qubits}),
                           "gates": gates, "max_qubits": qubits})
        levels.append(output)
    root = levels[-1][0]

    def proof(index):
        original, steps = index, []
        for level, row in enumerate(levels[:-1]):
            sibling_index = index ^ 1
            sibling = row[sibling_index]
            steps.append({"level": level, "index": index,
                          "side": "left" if sibling_index < index else "right",
                          "hash": sibling["hash"], "gates": sibling["gates"],
                          "max_qubits": sibling["max_qubits"]})
            index //= 2
        return {"leaf_index": original, "steps": steps}

    def verify_proof(index, operation, item, expected_root=root):
        name, _, _, gates, qubits = operation
        value = leaf(name, gates, qubits, index)
        cursor = index
        if item["leaf_index"] != index:
            return False
        for level, step in enumerate(item["steps"]):
            expected_side = "left" if (cursor ^ 1) < cursor else "right"
            if step["level"] != level or step["index"] != cursor or step["side"] != expected_side:
                return False
            sibling = {"hash": step["hash"], "gates": step["gates"],
                       "max_qubits": step["max_qubits"]}
            left, right = (sibling, value) if step["side"] == "left" else (value, sibling)
            total = left["gates"] + right["gates"]
            maximum = max(left["max_qubits"], right["max_qubits"])
            value = {"hash": canonical_hash({"domain": "uqpu-resource-node-v1",
                                              "left": left["hash"], "right": right["hash"],
                                              "gates": total, "max_qubits": maximum}),
                     "gates": total, "max_qubits": maximum}
            cursor //= 2
        return value == expected_root

    proofs = [proof(index) for index in range(len(operations))]
    encoded = [apply(value, operations) for value in range(64)]
    reconstructed = [apply(value, operations, inverse=True) for value in encoded]
    mutated_order = [operations[1], operations[0], *operations[2:]]
    mutated_proof = json.loads(json.dumps(proofs[0]))
    mutated_proof["steps"][0]["side"] = "left"
    resource_mutation = (*operations[9][:3], 5, 6)
    return {
        "inverse_pair_names": [item[0] for item in operations],
        "resource_merkle_root_sha256": root["hash"],
        "tree_resource_sum": root["gates"],
        "tree_max_qubits": root["max_qubits"],
        "proof_count": len(proofs),
        "all_inclusion_proofs_valid": all(verify_proof(i, operation, proofs[i])
                                             for i, operation in enumerate(operations)),
        "proof_direction_mutation_rejected": not verify_proof(0, operations[0], mutated_proof),
        "resource_mutation_rejected": not verify_proof(9, resource_mutation, proofs[9]),
        "basis_states_checked": 64,
        "distinct_outputs": len(set(encoded)),
        "residual": sum(a != b for a, b in enumerate(reconstructed)),
        "order_mutation_witness_count": sum(a != apply(value, mutated_order)
                                            for value, a in enumerate(encoded)),
        "resource_bound": {"gates": root["gates"], "max_qubits": root["max_qubits"]},
        "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle032_fixture(source_bytes, directory):
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": twelfth_graph_burnside_quotient(),
            "B": recursive_unicode_numeric_receipt_gate(),
            "C": six_reader_chained_atomicity(work),
            "D": zip64_eocd_locator_bind(),
            "E": twelve_issuer_threshold_receipts(),
            "F": sixteen_component_block_covariance(source_bytes),
            "G": three_signed_block_transforms(),
            "H": sixteen_scenario_deletion_intervals(),
            "FND/EQN": nine_source_affine_associativity(
                source_bytes, source_bytes + b":two", source_bytes + b":three",
                source_bytes + b":four", source_bytes + b":five", source_bytes + b":six",
                source_bytes + b":seven", source_bytes + b":eight", source_bytes + b":nine"),
            "SCM": five_observer_branch_certificate(),
            "AI-COST": lineage_manifest_v22(source_bytes),
            "QOS/QSVT": ten_inverse_pairs_merkle_proofs(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
