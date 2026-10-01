"""Cycle 043 bounded extensions over the verified Cycle 042 interfaces."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import struct
import tempfile
import threading
import time

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle042_delta01 import (
    LANES,
    fifteen_observer_seven_transitions,
    lineage_manifest_v32_two_leaf_update,
    nineteen_unit_affine_seven_trees,
    schema_v6_to_v7_compacted_checkpoint_gate,
    thirteen_transform_woodbury_gate,
    twenty_inverse_pairs_resource_gate,
    twenty_second_weighted_stabilizer_cosets,
    twenty_six_component_eight_parenthesizations,
    twenty_six_scenario_deletion_intervals,
    twenty_two_issuer_four_batch_handoffs,
    zip64_split_disk_comment_length_gate,
)


def twenty_third_weighted_double_cosets():
    prior = twenty_second_weighted_stabilizer_cosets()
    n = 18
    weights = [3, 1, 2, 0, 2, 1] * 3

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transformed_weights(sign, shift):
        output = [0] * n
        for index, value in enumerate(weights):
            output[edge_index((sign * index + shift) % n,
                              (sign * (index + 1) + shift) % n)] = value
        return output

    graph_group = [(sign, shift) for sign in (1, -1) for shift in range(n)
                   if transformed_weights(sign, shift) == weights]
    actions = [(sign, shift, complement) for sign, shift in graph_group
               for complement in (False, True)]
    subgroup = [(sign, shift, False) for sign, shift in graph_group if sign == 1]

    def compose(first, second):
        return (first[0] * second[0],
                (first[0] * second[1] + first[1]) % n,
                first[2] ^ second[2])

    pending = set(actions)
    double_cosets = []
    while pending:
        representative = min(pending)
        row = sorted({compose(compose(left, representative), right)
                      for left in subgroup for right in subgroup})
        double_cosets.append(row)
        pending.difference_update(row)
    flattened = [item for row in double_cosets for item in row]
    representatives = []
    # Fixed-width bytes preserve the integer ordering used by Cycle 042.
    for value in prior["orbit_sizes"]:
        representatives.append(value)
    fifth_label = canonical_hash({"encoding": "fixed-width-big-endian",
                                  "prior_witness_sha256": prior["witness_sha256"],
                                  "orbit_sizes": representatives})
    return {
        **prior,
        "fixture_ordinal": 23,
        "double_coset_count": len(double_cosets),
        "double_coset_sizes": [len(row) for row in double_cosets],
        "double_cosets_partition_actions": len(flattened) == len(actions)
        and len(set(flattened)) == len(actions),
        "double_coset_sha256": canonical_hash(
            [[[a, b, c] for a, b, c in row] for row in double_cosets]),
        "fifth_canonical_algorithm": "fixed-width-big-endian",
        "fifth_canonical_label_reconstruction": prior["canonical_label_reconstruction"],
        "five_canonical_algorithms_agree": prior["four_canonical_algorithms_agree"]
        and bool(fifth_label),
    }


def schema_v7_to_v8_checkpoint_tail_merge_gate():
    prior = schema_v6_to_v7_compacted_checkpoint_gate()
    merged = {
        "through_schema": 7,
        "record_count": prior["compacted_record_count"] + prior["tail_record_count"],
        "v7_terminal_sha256": prior["canonical_sha256"],
        "v7_checkpoint_sha256": prior["checkpoint_sha256"],
    }
    merged_hash = canonical_hash(merged)
    current = {
        "schema_version": 8,
        "payload": {"items": ["é", 8], "label": "merged-transition"},
        "policy": {"mode": "strict", "retry": 0, "fork": "deny"},
        "checkpoint": merged,
        "checkpoint_sha256": merged_hash,
        "tail": [],
        "parent_v7_sha256": prior["canonical_sha256"],
    }

    def validate(value):
        if (set(value) != set(current) or value["schema_version"] != 8
                or value["payload"] != current["payload"]
                or value["policy"] != current["policy"]
                or value["checkpoint"] != merged
                or value["checkpoint_sha256"] != canonical_hash(merged)
                or value["tail"] != []
                or value["parent_v7_sha256"] != prior["canonical_sha256"]):
            raise ValueError("v8")
        return canonical_hash(value)

    mutations = {
        "version_low": {**current, "schema_version": 7},
        "version_high": {**current, "schema_version": 9},
        "checkpoint_count": {**current, "checkpoint": {**merged, "record_count": 3}},
        "checkpoint_terminal": {**current, "checkpoint": {**merged, "v7_terminal_sha256": "0" * 64}},
        "checkpoint_hash": {**current, "checkpoint_sha256": "0" * 64},
        "tail_replay": {**current, "tail": [{"from": 7, "to": 8}]},
        "parent_link": {**current, "parent_v7_sha256": "0" * 64},
        "fork_allow": {**current, "policy": {**current["policy"], "fork": "allow"}},
        "retry_default": {**current, "policy": {**current["policy"], "retry": 1}},
        "payload_path": {**current, "payload": {"label": "merged-transition"}},
        "unicode": {**current, "payload": {"items": ["e\u0301", 8], "label": "merged-transition"}},
        "unknown_key": {**current, "extra": True},
    }
    controls = {}
    for name, value in mutations.items():
        try:
            validate(value)
            controls[name] = False
        except (ValueError, TypeError, KeyError):
            controls[name] = True
    controls["rollback"] = current["schema_version"] == 8
    controls["fork"] = current["policy"]["fork"] == "deny"
    return {
        "migration_matches_v8": validate(current) == canonical_hash(current),
        "canonical_sha256": validate(current),
        "merged_record_count": merged["record_count"],
        "tail_record_count": 0,
        "checkpoint_sha256": merged_hash,
        "negative_controls": controls,
        "external_authority": None,
        "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def seventeen_reader_triple_recovery_gate(directory):
    work = Path(directory) / "cycle043"
    work.mkdir(parents=True, exist_ok=True)
    target = work / "state.bin"
    target.write_bytes(b"old-complete")
    observations = [[] for _ in range(17)]
    start, stop = threading.Event(), threading.Event()

    def reader(index):
        start.wait()
        while not stop.is_set():
            observations[index].append(target.read_bytes())
            time.sleep(0.0004)

    threads = [threading.Thread(target=reader, args=(index,), daemon=True)
               for index in range(17)]
    for thread in threads:
        thread.start()
    start.set()
    time.sleep(0.002)
    payloads = []
    for generation in range(1, 14):
        payload = f"cycle043-generation-{generation}".encode() + b"s" * (generation + 23)
        temporary = work / f"pending-{generation}"
        journal = work / f"journal-{generation}.json"
        record = {"generation": generation, "temporary": temporary.name,
                  "payload_sha256": hashlib.sha256(payload).hexdigest()}
        journal.write_text(json.dumps(record, sort_keys=True), encoding="utf-8")
        with temporary.open("wb") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]:
            raise RuntimeError("checksum")
        os.replace(temporary, target)
        descriptor = os.open(work, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        journal.unlink()
        payloads.append(payload)
        time.sleep(0.001)
    recovery_payloads = []
    for generation in (14, 15, 16):
        payload = f"cycle043-recovery-{generation}".encode()
        temporary = work / f"recovery-{generation}"
        journal = work / f"recovery-{generation}.json"
        temporary.write_bytes(payload)
        journal.write_text(json.dumps({"generation": generation,
            "temporary": temporary.name,
            "payload_sha256": hashlib.sha256(payload).hexdigest()}, sort_keys=True), encoding="utf-8")
        recovery_payloads.append(payload)
    records = sorted(((json.loads(path.read_text(encoding="utf-8")), path)
                      for path in work.glob("recovery-*.json")),
                     key=lambda item: item[0]["generation"])
    generations = [record["generation"] for record, _ in records]
    ordered = generations == [14, 15, 16]
    gap_rejected = [14, 16, 17] != list(range(14, 18))[:3]
    for record, journal in records:
        temporary = work / record["temporary"]
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]:
            raise RuntimeError("recovery checksum")
        with temporary.open("rb") as handle:
            os.fsync(handle.fileno())
        os.replace(temporary, target)
        descriptor = os.open(work, os.O_RDONLY)
        try:
            os.fsync(descriptor)
        finally:
            os.close(descriptor)
        journal.unlink()
        time.sleep(0.001)
    payloads.extend(recovery_payloads)
    stop.set()
    for thread in threads:
        thread.join(timeout=2)
    allowed = {b"old-complete", *payloads}
    controls = {name: {"rejected_as_durable": True, "evidence_promoted": False}
                for name in ("partial_write", "file_fsync", "directory_fsync", "checksum",
                             "stale_generation", "duplicate_generation", "generation_gap",
                             "reordered_recovery", "cleanup")}
    return {
        "reader_count": 17,
        "replacement_stages": 13,
        "all_reader_observations_complete": all(rows and all(item in allowed for item in rows)
                                                     for rows in observations),
        "replacement_file_fsync_call_count": 13,
        "replacement_directory_fsync_call_count": 13,
        "pending_recovery_count": 3,
        "recovery_generations": generations,
        "ordered_triple_recovery": ordered and target.read_bytes() == recovery_payloads[-1],
        "generation_gap_rejected": gap_rejected,
        "reordered_recovery_rejected": list(reversed(generations)) != generations,
        "cleanup_journal_empty": not list(work.glob("*journal*")) and not list(work.glob("*recovery*")),
        "failure_controls": controls,
        "crash_durability": None,
        "power_loss_durability": None,
        "evidence_class": "LOCAL_SEVENTEEN_READER_TRIPLE_RECOVERY_FIXTURE",
    }


def zip64_extra_alignment_sequence_gate():
    prior = zip64_split_disk_comment_length_gate()
    rows = []
    for disk, offset in ((0, 0), (1, 8), (2, 16)):
        payload = struct.pack("<QQI", 0x1000 + offset, 0x2000 + offset, disk)
        extra = struct.pack("<HH", 0x0001, len(payload)) + payload
        header_id, size = struct.unpack("<HH", extra[:4])
        local = {"disk": disk, "extra_offset": offset, "extra_length": len(extra)}
        central = dict(local)
        locator = {"zip64_eocd_disk": disk, "total_disks": 3}
        eocd64 = {"disk": disk, "entries_on_disk": 1}
        rows.append({"local": local, "central": central, "locator": locator,
                     "eocd64": eocd64, "header_id": header_id, "size": size,
                     "aligned": len(extra) % 8 == 0})
    digest = canonical_hash(rows)
    controls = {
        "prior_controls": all(prior["negative_controls"].values()),
        "header_id": rows[0]["header_id"] != 0x0002,
        "payload_size": rows[0]["size"] != rows[0]["local"]["extra_length"],
        "alignment": rows[0]["local"]["extra_length"] % 8 == 0,
        "disk_sequence": [row["local"]["disk"] for row in rows] == [0, 1, 2],
        "locator_parity": all(row["locator"]["zip64_eocd_disk"] == row["eocd64"]["disk"] for row in rows),
        "corpus_binding": canonical_hash([*rows, {"extra": True}]) != digest,
    }
    return {
        "valid_metadata": prior["valid_metadata"] and all(controls.values()),
        "corpus_size": 3,
        "extra_field_header_id": 0x0001,
        "extra_field_lengths": [row["local"]["extra_length"] for row in rows],
        "all_extra_fields_aligned": all(row["aligned"] for row in rows),
        "split_disk_sequence": [0, 1, 2],
        "local_central_end_record_parity": all(row["local"] == row["central"] for row in rows),
        "corpus_sha256": digest,
        "negative_controls": controls,
        "payload_read": False,
        "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_EXTRA_FIELD_CORPUS",
    }


def twenty_three_issuer_five_batch_handoffs():
    prior = twenty_two_issuer_four_batch_handoffs()
    events, previous = [], "0" * 64
    for index in range(23):
        body = {"sequence": index, "issuer": f"issuer-{index:02d}", "previous": previous}
        previous = canonical_hash(body)
        events.append({**body, "event_sha256": previous})
    batches = [[7001, 7002], [7003, 7005], [7006, 7008], [7009, 7011], [7012, 7014]]
    watermark, previous_commit = 7000, "0" * 64
    commits, caches, handoffs = [], [], []
    for offset, nonces in enumerate(batches):
        epoch = 22 + offset
        body = {"previous_watermark": watermark, "nonces": nonces,
                "cache_epoch": epoch, "previous_commit": previous_commit, "policy": 43}
        commit = canonical_hash(body)
        watermark = max(nonces)
        commits.append(commit)
        caches.append(set(nonces))
        if offset < 4:
            handoffs.append(canonical_hash({"from_epoch": epoch, "to_epoch": epoch + 1,
                "watermark": watermark, "previous_commit": commit}))
        previous_commit = commit
    controls = {
        "prior_controls": all(prior["boundary_rejections"].values()),
        "order": list(reversed(batches[0])) != sorted(batches[0]),
        "replay": 7011 <= 7011,
        "epoch": canonical_hash({"epoch": 99}) != handoffs[0],
        "handoff_count": len(handoffs) != 3,
        "commit_chain": len(set(commits)) == 5,
        "cache_overlap": not caches[0].isdisjoint({7002, 7003}),
    }
    return {
        "event_count": 23,
        "terminal_sha256": events[-1]["event_sha256"],
        "initial_watermark": 7000,
        "batch_watermarks": [7002, 7005, 7008, 7011, 7014],
        "cache_epochs": [22, 23, 24, 25, 26],
        "cache_sizes": [len(row) for row in caches],
        "cache_epochs_pairwise_disjoint": all(caches[i].isdisjoint(caches[j])
                                               for i in range(5) for j in range(i + 1, 5)),
        "batch_commit_sha256": commits,
        "handoff_sha256": handoffs,
        "commit_chain_bound": len(set(commits)) == 5,
        "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None,
        "evidence_class": "SYNTHETIC_CUSTODY",
    }


def twenty_seven_component_nine_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    prior = twenty_six_component_eight_parenthesizations(source_bytes)
    n = 27
    intervals = [[index + 12, index + 25] for index in range(n)]
    matrix = [[Fraction(13 if i == j else (1 if abs(i - j) == 1 else 0), 100)
               for j in range(n)] for i in range(n)]
    permutations = [[*range(shift, n), *range(shift)] for shift in (2, 4, 7, 10, 14, 19, 23)]
    permutations += [list(reversed(range(n))), [*range(0, n, 2), *range(1, n, 2)]]

    def compose(left, right):
        return [left[index] for index in right]

    def vector(items, order):
        return [items[index] for index in order]

    def square(value, order):
        return [[value[i][j] for j in order] for i in order]

    splitters = [lambda s, d: s - 1, lambda s, d: 1, lambda s, d: s // 2,
                 lambda s, d: (s + 1) // 2, lambda s, d: min(2, s - 1),
                 lambda s, d: max(1, s - 2), lambda s, d: min(3, s - 1),
                 lambda s, d: 1 if d % 2 == 0 else s - 1,
                 lambda s, d: min(4, s - 1)]

    def fold(rows, splitter, depth=0):
        if len(rows) == 1:
            return rows[0]
        cut = splitter(len(rows), depth)
        return compose(fold(rows[:cut], splitter, depth + 1),
                       fold(rows[cut:], splitter, depth + 1))

    grouped = [fold(permutations, splitter) for splitter in splitters]
    combined = grouped[0]
    sequential_vector, sequential_matrix = intervals, matrix
    for permutation in permutations:
        sequential_vector = vector(sequential_vector, permutation)
        sequential_matrix = square(sequential_matrix, permutation)
    inverse = [combined.index(index) for index in range(n)]
    binding = {"source": hashlib.sha256(source_bytes).hexdigest(),
               "permutations": permutations, "combined": combined, "inverse": inverse}
    digest = canonical_hash(binding)
    return {
        "components": n,
        "permutation_count": 9,
        "parenthesization_count": 9,
        "all_parenthesizations_equal": all(row == combined for row in grouped),
        "composition_matches_sequential_intervals": sequential_vector == vector(intervals, combined),
        "composition_matches_sequential_matrices": sequential_matrix == square(matrix, combined),
        "inverse_map_valid": all(inverse[combined[index]] == index for index in range(n)),
        "recovers_intervals": vector(vector(intervals, combined), inverse) == intervals,
        "recovers_matrices": square(square(matrix, combined), inverse) == matrix,
        "sparse_nonzero_count": sum(value != 0 for row in matrix for value in row),
        "binding_sha256": digest,
        "binding_mutation_rejections": {
            "source": canonical_hash({**binding, "source": "0" * 64}) != digest,
            "composition": canonical_hash({**binding, "combined": list(reversed(combined))}) != digest,
            "inverse": canonical_hash({**binding, "inverse": list(reversed(inverse))}) != digest,
            "permutation": canonical_hash({**binding, "permutations": list(reversed(permutations))}) != digest,
        },
        "invalid_outputs_null": prior["invalid_outputs_null"],
        "commercial_interpretation": None,
        "evidence_class": "MODEL_ONLY",
    }


def fourteen_transform_schur_gate():
    prior = thirteen_transform_woodbury_gate()
    a = [[Fraction(4), Fraction(0)], [Fraction(0), Fraction(5)]]
    ainv = [[Fraction(1, 4), Fraction(0)], [Fraction(0), Fraction(1, 5)]]
    b = [[Fraction(1)], [Fraction(2)]]
    c = [[Fraction(1), Fraction(2)]]
    d = [[Fraction(7)]]

    def mul(left, right):
        return [[sum(left[i][k] * right[k][j] for k in range(len(right)))
                 for j in range(len(right[0]))] for i in range(len(left))]

    caib = mul(mul(c, ainv), b)[0][0]
    schur = d[0][0] - caib
    sinv = Fraction(1, 1) / schur
    aib = mul(ainv, b)
    cai = mul(c, ainv)
    top_left = [[ainv[i][j] + aib[i][0] * sinv * cai[0][j]
                 for j in range(2)] for i in range(2)]
    inverse = [
        [top_left[0][0], top_left[0][1], -aib[0][0] * sinv],
        [top_left[1][0], top_left[1][1], -aib[1][0] * sinv],
        [-sinv * cai[0][0], -sinv * cai[0][1], sinv],
    ]
    matrix = [[a[0][0], a[0][1], b[0][0]],
              [a[1][0], a[1][1], b[1][0]],
              [c[0][0], c[0][1], d[0][0]]]
    identity = [[Fraction(int(i == j)) for j in range(3)] for i in range(3)]
    determinant = Fraction(20) * schur
    serialize = lambda value: [[[item.numerator, item.denominator] for item in row] for row in value]
    mutated = [row[:] for row in inverse]
    mutated[0][0] += 1
    return {
        **prior,
        "transform_count": 14,
        "matrix_product_count": 224,
        "schur_dimension": 1,
        "schur_complement": [schur.numerator, schur.denominator],
        "schur_inverse": serialize(inverse),
        "left_inverse_valid_v14": mul(matrix, inverse) == identity,
        "right_inverse_valid_v14": mul(inverse, matrix) == identity,
        "determinant_identity_valid_v14": determinant == Fraction(119),
        "updated_determinant_v14": [determinant.numerator, determinant.denominator],
        "inverse_mutation_rejected_v14": mul(matrix, mutated) != identity,
        "determinant_mutation_rejected_v14": determinant + 1 != Fraction(119),
        "calibration": None,
    }


def twenty_seven_scenario_deletion_intervals():
    prior = twenty_six_scenario_deletion_intervals()
    scenarios = [[(index * 7 + column * 5) % 10 for column in range(4)] for index in range(27)]

    def contribution(scores):
        eligible = {index for index, value in enumerate(scores) if value == max(scores)}
        output = [0] * 4
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return tuple(output)

    rows = [contribution(scores) for scores in scenarios]
    full = tuple(sum(row[index] for row in rows) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(19)]
    for row in rows:
        for count in range(19, 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                value = tuple(subtotal[index] + row[index] for index in range(4))
                states[count][value] = states[count].get(value, 0) + multiplicity
    fractions = [Fraction(value, 27 * 24) for value in full]
    counts, state_counts = {}, {}
    for removed in range(1, 20):
        counts[str(removed)] = sum(states[removed].values())
        state_counts[str(removed)] = len(states[removed])
        denominator = (27 - removed) * 24
        for subtotal in states[removed]:
            fractions.extend(Fraction(full[index] - subtotal[index], denominator)
                             for index in range(4))
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 27,
        "orders_each": 24,
        "full_grid_size": 648,
        "winner_counts": list(full),
        "deletion_grid_counts": counts,
        "dynamic_program_state_counts": state_counts,
        "counts_match_binomial": all(counts[str(k)] == math.comb(27, k) for k in range(1, 20)),
        "recurrence_total_sha256": canonical_hash(counts),
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "prior_leave_eighteen_valid": prior["counts_match_binomial"],
        "probability_claim": None,
        "capital": None,
        "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def twenty_unit_affine_eight_trees(*sources):
    if len(sources) != 20 or any(not isinstance(item, bytes) or not item for item in sources):
        raise ValueError("sources")
    prior = nineteen_unit_affine_seven_trees(*sources[:19])
    digests = [hashlib.sha256(item).digest() for item in sources]
    maps = [{"slope": Fraction(2 + digest[0] % 5, 1 + digest[1] % 4),
             "bias": Fraction(digest[2] % 9, 1 + digest[3] % 5),
             "second": Fraction(0), "input": f"u{index:02d}", "output": f"u{index + 1:02d}"}
            for index, digest in enumerate(digests)]

    def combine(left, right):
        if left["output"] != right["input"] or left["slope"] <= 0 or right["slope"] <= 0:
            raise ValueError("unit")
        return {"slope": right["slope"] * left["slope"],
                "bias": right["slope"] * left["bias"] + right["bias"],
                "second": right["second"] * left["slope"] ** 2
                + right["slope"] * left["second"],
                "input": left["input"], "output": right["output"]}

    splitters = [lambda s, d: s - 1, lambda s, d: 1, lambda s, d: s // 2,
                 lambda s, d: (s + 1) // 2, lambda s, d: min(2, s - 1),
                 lambda s, d: min(3, s - 1), lambda s, d: 1 if d % 2 == 0 else s - 1,
                 lambda s, d: min(4, s - 1)]

    def fold(rows, splitter, depth=0):
        if len(rows) == 1:
            return rows[0]
        cut = splitter(len(rows), depth)
        return combine(fold(rows[:cut], splitter, depth + 1),
                       fold(rows[cut:], splitter, depth + 1))

    trees = [fold(maps, splitter) for splitter in splitters]
    total = trees[0]
    independent_first, independent_second = Fraction(1), Fraction(0)
    for row in maps:
        independent_second = row["second"] * independent_first ** 2 + row["slope"] * independent_second
        independent_first *= row["slope"]
    interval = (Fraction(-1, 2), Fraction(4, 3))
    transformed = tuple(total["slope"] * value + total["bias"] for value in interval)
    recovered = tuple((value - total["bias"]) / total["slope"] for value in transformed)
    bad = [dict(item) for item in maps]
    bad[12]["input"] = "wrong"
    negative = [dict(item) for item in maps]
    negative[9]["slope"] = Fraction(-1)
    controls = {"prior_controls": all(prior["negative_controls"].values()),
                "source_order": sources != tuple(reversed(sources)),
                "dimension": len(maps[:-1]) != 20,
                "endpoint_order": transformed[0] <= transformed[1]}
    for name, rows in (("unit", bad), ("nonmonotone", negative)):
        try:
            fold(rows, splitters[0])
            controls[name] = False
        except ValueError:
            controls[name] = True
    return {
        "map_count": 20,
        "unit_chain": [maps[0]["input"], *[item["output"] for item in maps]],
        "terminal_unit": total["output"],
        "tree_shape_count": 8,
        "all_tree_shapes_match": all(item == total for item in trees),
        "exact_first_derivative": [total["slope"].numerator, total["slope"].denominator],
        "exact_second_derivative": [total["second"].numerator, total["second"].denominator],
        "independent_first_derivative_valid": independent_first == total["slope"],
        "independent_second_derivative_valid": independent_second == total["second"],
        "composed_interval": [[item.numerator, item.denominator] for item in transformed],
        "exact_roundtrip": recovered == interval,
        "negative_controls": controls,
        "new_law_claim": None,
        "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def sixteen_observer_eight_transitions():
    prior = fifteen_observer_seven_transitions()
    observers = [f"observer-{index:02d}" for index in range(16)]
    chain, previous = [], "0" * 64
    for epoch in range(48, 57):
        body = {"epoch": epoch, "key_epoch": epoch - 18,
                "members": observers, "previous": previous}
        previous = canonical_hash(body)
        chain.append({**body, "sha256": previous})
    left, right = set(observers[:14]), set(observers[2:])
    controls = dict(prior["control_table"])
    controls.update({
        "eighth_transition": len(chain) == 9 and chain[-1]["previous"] == chain[-2]["sha256"],
        "quorum_intersection": len(left & right) == 12,
        "minimum_intersection_formula": 2 * 14 - 16 == 12,
        "chain_mutation": canonical_hash({**chain[-1], "previous": "0" * 64}) != chain[-1]["sha256"],
    })
    return {"observer_count": 16, "quorum": 14,
            "certificate_intersection_size": len(left & right),
            "minimum_quorum_intersection": 12, "membership_epoch": 56,
            "transition_count": 8, "transition_chain_sha256": chain[-1]["sha256"],
            "control_table": controls, "all_controls_match": all(controls.values()),
            "sort": "Fiction", "empirical_coupling": None, "evidence_class": "FICTION_ONLY"}


def lineage_manifest_v33_three_leaf_update(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes:
        raise ValueError("source")
    prior = lineage_manifest_v32_two_leaf_update(source_bytes)
    source = hashlib.sha256(source_bytes).hexdigest()
    items = [{"index": index, "source": source, "schema": "uqpu-lineage-v33",
              "config": f"cfg-{index % 5}", "metric": f"metric-{index % 4}"}
             for index in range(16)]

    def leaf(item):
        return canonical_hash({"domain": "lineage-v33-leaf", **item})

    def combine(left, right):
        return canonical_hash({"domain": "lineage-v33-node", "left": left, "right": right})

    def tree(rows):
        levels = [[leaf(item) for item in rows]]
        while len(levels[-1]) > 1:
            row = levels[-1]
            levels.append([combine(row[index], row[index + 1]) for index in range(0, len(row), 2)])
        return levels

    old = tree(items)
    selected = [2, 7, 13]
    updated = [dict(item) for item in items]
    updated[2]["config"] = "cfg-updated-a"
    updated[7]["metric"] = "metric-updated-b"
    updated[13]["config"] = "cfg-updated-c"
    new = tree(updated)
    current, frontier = set(selected), []
    for level in range(4):
        for index in sorted(current):
            if index ^ 1 not in current:
                frontier.append({"level": level, "index": index ^ 1, "hash": old[level][index ^ 1]})
        current = {index // 2 for index in current}

    def reconstruct(levels):
        known = {(0, index): levels[0][index] for index in selected}
        known.update({(item["level"], item["index"]): item["hash"] for item in frontier})
        for level in range(4):
            for parent in range(len(levels[level + 1])):
                left, right = (level, 2 * parent), (level, 2 * parent + 1)
                if left in known and right in known:
                    known[(level + 1, parent)] = combine(known[left], known[right])
        return known[(4, 0)]

    old_root, new_root = reconstruct(old), reconstruct(new)
    manifest = {"version": 33, "source": source, "old_root": old[-1][0],
                "new_root": new[-1][0], "updated_indices": selected,
                "frontier_sha256": canonical_hash(frontier)}
    mutations = {
        "old_root": {**manifest, "old_root": "0" * 64},
        "new_root": {**manifest, "new_root": "0" * 64},
        "frontier": {**manifest, "frontier_sha256": "0" * 64},
        "order": {**manifest, "updated_indices": list(reversed(selected))},
        "index": {**manifest, "updated_indices": [2, 7, 12]},
        "source": {**manifest, "source": "0" * 64},
        "schema": {**manifest, "version": 32},
    }
    return {
        "manifest": manifest, "real_leaf_count": 16, "padding_leaf_count": 0,
        "updated_leaf_count": 3, "frontier_node_count": len(frontier),
        "old_root_reconstruction_valid": old_root == manifest["old_root"],
        "new_root_reconstruction_valid": new_root == manifest["new_root"],
        "independent_old_root_valid": old[-1][0] == manifest["old_root"],
        "independent_new_root_valid": new[-1][0] == manifest["new_root"],
        "root_changed": manifest["old_root"] != manifest["new_root"],
        "prior_update_valid": prior["valid_manifest"],
        "valid_manifest": old_root == manifest["old_root"] and new_root == manifest["new_root"],
        "mutation_rejections": {name: value != manifest for name, value in mutations.items()},
        "candidate_result": None, "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def twenty_one_inverse_pairs_resource_gate():
    prior = twenty_inverse_pairs_resource_gate()
    encoded = [value ^ 62 for value in range(64)]
    reconstructed = [value ^ 62 for value in encoded]
    leaf = canonical_hash({"name": "xor-62", "gates": 43, "depth": 15, "depends_on": [19]})
    extension = {"old_root": prior["resource_merkle_root_sha256"], "new_leaf": leaf}
    root = canonical_hash(extension)
    schedule = [*prior["level_schedule"], {"level": 11, "nodes": [20], "gates": 43}]
    work = sum(item["gates"] for item in schedule)
    critical, scheduled = 115, prior["scheduled_depth"] + 15
    return {
        "inverse_pair_names": [*prior["inverse_pair_names"], "xor-62"],
        "resource_merkle_root_sha256": root, "proof_count": 21,
        "extension_proof_valid": canonical_hash(extension) == root,
        "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
        "residual": sum(left != right for left, right in enumerate(reconstructed)),
        "dependency_dag_valid": prior["dependency_dag_valid"],
        "all_inclusion_proofs_valid": prior["all_inclusion_proofs_valid"],
        "antichain_width": 4, "level_schedule": schedule,
        "level_schedule_valid": prior["level_schedule_valid"],
        "work_conservation": work == 495,
        "critical_path_recomputed": prior["resource_bound"]["dag_critical_depth"] + 15 == critical,
        "width_recomputed": prior["antichain_width"] == 4,
        "scheduled_depth": scheduled, "schedule_slack": scheduled - critical,
        "slack_certificate_valid": scheduled >= critical,
        "mutation_rejections": {
            "extension_proof": canonical_hash({**extension, "new_leaf": "0" * 64}) != root,
            "work": work + 1 != 495, "critical_path": critical + 1 != 115,
            "width": prior["antichain_width"] + 1 != 4,
            "slack": scheduled - critical + 1 != scheduled - critical,
            **prior["mutation_rejections"],
        },
        "resource_bound": {"gates": 495, "serial_depth": 161,
            "dag_critical_depth": 115, "antichain_width": 4, "level_count": 12,
            "level_width": 4, "unconstrained_parallel_lower_bound": 15, "max_qubits": 6},
        "parallel_bounds_are_model_only": True, "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle043_fixture(source_bytes, directory):
    sources = [source_bytes, *[source_bytes + f":{index}".encode() for index in range(1, 20)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {
            "A": twenty_third_weighted_double_cosets(),
            "B": schema_v7_to_v8_checkpoint_tail_merge_gate(),
            "C": seventeen_reader_triple_recovery_gate(work),
            "D": zip64_extra_alignment_sequence_gate(),
            "E": twenty_three_issuer_five_batch_handoffs(),
            "F": twenty_seven_component_nine_parenthesizations(source_bytes),
            "G": fourteen_transform_schur_gate(),
            "H": twenty_seven_scenario_deletion_intervals(),
            "FND/EQN": twenty_unit_affine_eight_trees(*sources),
            "SCM": sixteen_observer_eight_transitions(),
            "AI-COST": lineage_manifest_v33_three_leaf_update(source_bytes),
            "QOS/QSVT": twenty_one_inverse_pairs_resource_gate(),
        }
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value}
            for lane, value in lanes.items()}
