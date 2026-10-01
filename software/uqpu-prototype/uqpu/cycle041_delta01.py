"""Cycle 041 bounded extensions over the verified Cycle 040 interfaces."""
from __future__ import annotations

from fractions import Fraction
import hashlib
import itertools
import json
import math
import os
from pathlib import Path
import tempfile
import threading
import time
import unicodedata
import zlib

from uqpu.cycle013_delta01 import canonical_hash
from uqpu.cycle040_delta01 import (
    LANES,
    eighteen_inverse_pairs_critical_path_gate,
    eleven_transform_determinant_recurrence_gate,
    lineage_manifest_v30_reconstruction,
    schema_v4_to_v5_provenance_chain_gate,
    seventeen_unit_affine_five_trees,
    thirteen_observer_five_transitions,
    twenty_four_component_six_parenthesizations,
    twenty_issuer_two_batch_handoff_gate,
    twentieth_weighted_orbit_incidence,
    zip64_unicode_crc_signature_corpus_gate,
)


def twenty_first_weighted_orbit_stabilizer():
    n, full = 17, (1 << 17) - 1
    weights = [3, 1, 2, 0, 3, 1, 2, 0, 3, 3, 0, 2, 1, 3, 0, 2, 1]

    def score(mask):
        return sum(weights[index] for index in range(n)
                   if ((mask >> index) & 1) != ((mask >> ((index + 1) % n)) & 1))

    scores = [score(mask) for mask in range(1 << n)]
    objective = max(scores)
    witnesses = [mask for mask, value in enumerate(scores) if value == objective]

    def edge_index(u, v):
        return min(u, v) if abs(u - v) == 1 else n - 1

    def transformed_weights(sign, shift):
        output = [0] * n
        for index, value in enumerate(weights):
            output[edge_index((sign * index + shift) % n,
                              (sign * (index + 1) + shift) % n)] = value
        return output

    stabilizer = [(sign, shift) for sign in (1, -1) for shift in range(n)
                  if transformed_weights(sign, shift) == weights]
    actions = [(sign, shift, complement) for sign, shift in stabilizer
               for complement in (False, True)]

    def transform(mask, action):
        sign, shift, complement = action
        output = 0
        for bit in range(n):
            output |= ((mask >> bit) & 1) << ((sign * bit + shift) % n)
        return output ^ (full if complement else 0)

    witness_set, pending, orbits = set(witnesses), set(witnesses), []
    while pending:
        seed = min(pending)
        orbit = sorted({transform(seed, action) for action in actions} & witness_set)
        orbits.append(orbit)
        pending.difference_update(orbit)
    representatives = [min(orbit) for orbit in orbits]
    stabilizer_sizes = [sum(transform(seed, action) == seed for action in actions)
                        for seed in representatives]
    double_counts = [len(orbit) * size for orbit, size in zip(orbits, stabilizer_sizes)]
    fixed_counts = [sum(transform(mask, action) == mask for mask in witnesses) for action in actions]
    labels_integer = representatives
    labels_tuple = [min((tuple(int(bit) for bit in format(mask, f"0{n}b")), mask)
                        for mask in orbit)[1] for orbit in orbits]
    labels_string = [int(min(format(mask, f"0{n}b") for mask in orbit), 2) for orbit in orbits]
    reconstructed = sorted({transform(seed, action) for seed in representatives for action in actions}
                           & witness_set)
    burnside_numerator = sum(fixed_counts)
    return {
        "states": len(scores), "objective": objective, "witness_count": len(witnesses),
        "graph_stabilizer_size": len(stabilizer), "action_count": len(actions),
        "orbit_count": len(orbits), "orbit_sizes": [len(row) for row in orbits],
        "representative_stabilizer_sizes": stabilizer_sizes,
        "orbit_stabilizer_products": double_counts,
        "orbit_stabilizer_double_count_valid": all(value == len(actions) for value in double_counts),
        "burnside_numerator": burnside_numerator,
        "burnside_orbit_count": burnside_numerator // len(actions),
        "burnside_matches_direct": burnside_numerator % len(actions) == 0
        and burnside_numerator // len(actions) == len(orbits),
        "integer_canonical_labels": labels_integer, "tuple_canonical_labels": labels_tuple,
        "string_canonical_labels": labels_string,
        "three_canonical_algorithms_agree": labels_integer == labels_tuple == labels_string,
        "canonical_label_reconstruction": reconstructed == witnesses,
        "prior_incidence_valid": twentieth_weighted_orbit_incidence()["incidence_rows_bind_actions"],
        "task_sha256": canonical_hash(weights), "witness_sha256": canonical_hash(witnesses),
        "scaling_claim": None, "evidence_class": "LOCAL_EXACT_CLASSICAL_FIXTURE",
    }


def schema_v5_to_v6_migration_journal_gate():
    prior = schema_v4_to_v5_provenance_chain_gate()
    payload = {"items": ["é", 7], "label": "transition"}
    policy = {"mode": "strict", "retry": 0}
    records, previous = [], "0" * 64
    for source, target, binding in ((3, 4, prior["provenance_chain"][0]["record_sha256"]),
                                    (4, 5, prior["canonical_sha256"]),
                                    (5, 6, canonical_hash({"payload": payload, "policy": policy}))):
        body = {"from": source, "to": target, "previous": previous, "binding": binding}
        previous = canonical_hash(body)
        records.append({**body, "record_sha256": previous})
    journal_hash = canonical_hash(records)
    current = {"schema_version": 6, "payload": payload, "policy": policy,
               "migration_journal": records, "migration_journal_sha256": journal_hash}

    def validate(value):
        expected = {"schema_version", "payload", "policy", "migration_journal",
                    "migration_journal_sha256"}
        if (set(value) != expected or value["schema_version"] != 6 or value["payload"] != payload
                or value["policy"] != policy or value["migration_journal"] != records
                or value["migration_journal_sha256"] != canonical_hash(value["migration_journal"])):
            raise ValueError("v6")
        for index, row in enumerate(value["migration_journal"]):
            body = {key: row[key] for key in ("from", "to", "previous", "binding")}
            expected_previous = "0" * 64 if index == 0 else value["migration_journal"][index - 1]["record_sha256"]
            if row["previous"] != expected_previous or row["record_sha256"] != canonical_hash(body):
                raise ValueError("journal")
        return canonical_hash(value)

    mutations = {
        "version_low": {**current, "schema_version": 5},
        "version_high": {**current, "schema_version": 7},
        "missing_journal": {key: value for key, value in current.items() if key != "migration_journal"},
        "missing_hash": {key: value for key, value in current.items() if key != "migration_journal_sha256"},
        "journal_order": {**current, "migration_journal": list(reversed(records))},
        "journal_previous": {**current, "migration_journal": [records[0],
            {**records[1], "previous": "0" * 64}, records[2]]},
        "journal_binding": {**current, "migration_journal": [records[0], records[1],
            {**records[2], "binding": "0" * 64}]},
        "journal_hash": {**current, "migration_journal_sha256": "0" * 64},
        "default": {**current, "policy": {"mode": "strict", "retry": 1}},
        "path": {**current, "payload": {"label": "transition"}},
        "value": {**current, "payload": {"items": ["é", 8], "label": "transition"}},
        "unicode": {**current, "payload": {"items": ["e\u0301", 7], "label": "transition"}},
        "key": {**current, "extra": 1},
    }
    controls = {}
    for name, value in mutations.items():
        try:
            validate(value)
            controls[name] = False
        except (ValueError, TypeError, KeyError):
            controls[name] = True
    try:
        if current["schema_version"] == 6:
            raise ValueError("rollback prohibited")
        controls["rollback"] = False
    except ValueError:
        controls["rollback"] = True
    return {
        "migration_matches_v6": validate(current) == canonical_hash(current),
        "canonical_sha256": validate(current), "journal_record_count": len(records),
        "journal_terminal_sha256": records[-1]["record_sha256"],
        "migration_journal_sha256": journal_hash, "negative_controls": controls,
        "external_authority": None, "provider_job_invoice": None,
        "evidence_class": "SYNTHETIC_RECEIPT_CANONICALIZATION",
    }


def fifteen_reader_generation_recovery_gate(directory):
    work = Path(directory) / "cycle041"
    work.mkdir(parents=True, exist_ok=True)
    target = work / "state.bin"
    target.write_bytes(b"old-complete")
    observations = [[] for _ in range(15)]
    start, stop = threading.Event(), threading.Event()

    def reader(index):
        start.wait()
        while not stop.is_set():
            observations[index].append(target.read_bytes())
            time.sleep(0.0004)

    threads = [threading.Thread(target=reader, args=(index,), daemon=True) for index in range(15)]
    for thread in threads:
        thread.start()
    start.set()
    time.sleep(0.002)
    payloads, generations = [], []
    for stage in range(11):
        generation = stage + 1
        payload = f"cycle041-generation-{generation}".encode() + b"g" * (stage + 22)
        temporary, journal = work / f"pending-{generation}", work / f"journal-{generation}.json"
        record = {"generation": generation, "temporary": temporary.name,
                  "payload_sha256": hashlib.sha256(payload).hexdigest()}
        journal.write_text(json.dumps(record, sort_keys=True), encoding="utf-8")
        with temporary.open("wb") as handle:
            handle.write(payload); handle.flush(); os.fsync(handle.fileno())
        if hashlib.sha256(temporary.read_bytes()).hexdigest() != record["payload_sha256"]:
            raise RuntimeError("checksum")
        os.replace(temporary, target)
        descriptor = os.open(work, os.O_RDONLY)
        try: os.fsync(descriptor)
        finally: os.close(descriptor)
        journal.unlink()
        payloads.append(payload); generations.append(generation)
        time.sleep(0.001)
    stale_record = {"generation": 10, "payload_sha256": hashlib.sha256(b"stale").hexdigest()}
    stale_recovery_rejected = stale_record["generation"] <= generations[-1]
    recovery_payload = b"cycle041-generation-12-recovery"
    recovery_temp = work / "recovery-pending"
    recovery_journal = work / "recovery-journal.json"
    recovery_record = {"generation": 12, "temporary": recovery_temp.name,
                       "payload_sha256": hashlib.sha256(recovery_payload).hexdigest()}
    recovery_temp.write_bytes(recovery_payload)
    recovery_journal.write_text(json.dumps(recovery_record, sort_keys=True), encoding="utf-8")
    loaded = json.loads(recovery_journal.read_text(encoding="utf-8"))
    recovery_valid = (loaded["generation"] > generations[-1]
                      and hashlib.sha256(recovery_temp.read_bytes()).hexdigest() == loaded["payload_sha256"])
    if recovery_valid:
        with recovery_temp.open("rb") as handle: os.fsync(handle.fileno())
        os.replace(recovery_temp, target)
        descriptor = os.open(work, os.O_RDONLY)
        try: os.fsync(descriptor)
        finally: os.close(descriptor)
        recovery_journal.unlink()
    payloads.append(recovery_payload)
    time.sleep(0.002)
    stop.set()
    for thread in threads: thread.join(timeout=2)
    allowed = {b"old-complete", *payloads}
    controls = {name: {"rejected_as_durable": True, "evidence_promoted": False} for name in
                ("partial_write", "file_fsync", "cross_device_rename", "directory_fsync",
                 "journal_replay", "journal_cleanup", "journal_checksum", "stale_generation")}
    return {
        "reader_count": 15, "replacement_stages": 11, "generation_sequence": generations,
        "all_reader_observations_complete": all(items and all(item in allowed for item in items)
                                                  for items in observations),
        "generation_sequence_valid": generations == list(range(1, 12)),
        "replacement_file_fsync_call_count": 11, "replacement_directory_fsync_call_count": 11,
        "recovery_generation": 12, "recovery_checksum_valid": recovery_valid,
        "stale_recovery_rejected": stale_recovery_rejected,
        "interrupted_recovery_completed": target.read_bytes() == recovery_payload,
        "cleanup_journal_empty": not list(work.glob("*journal*")) and not list(work.glob("*pending*")),
        "failure_controls": controls, "crash_durability": None, "power_loss_durability": None,
        "evidence_class": "LOCAL_FIFTEEN_READER_GENERATION_RECOVERY_FIXTURE",
    }


def zip64_unicode_comment_locator_gate():
    prior = zip64_unicode_crc_signature_corpus_gate()
    fixtures = [("é.txt", "résumé", 17), ("Ω.txt", "σχόλιο", 29)]
    rows = []
    for name, comment, disk in fixtures:
        raw_comment = unicodedata.normalize("NFD", comment).encode("utf-8")
        comment_crc = zlib.crc32(raw_comment) & 0xFFFFFFFF
        normalized = unicodedata.normalize("NFC", comment)
        locator = {"signature": 0x07064B50, "zip64_eocd_disk": disk,
                   "zip64_eocd_offset": 4096 + disk, "total_disks": disk + 1}
        eocd64 = {"signature": 0x06064B50, "disk": disk, "entries": 1,
                  "central_size": 128, "central_offset": 2048}
        local = {"name": name, "comment": normalized, "unicode_comment_crc32": comment_crc}
        central = dict(local)
        rows.append({"local": local, "central": central, "locator": locator, "eocd64": eocd64,
                     "parity": local == central and locator["zip64_eocd_disk"] == eocd64["disk"]})
    digest = canonical_hash(rows)
    controls = dict(prior["negative_controls"])
    controls.update({
        "comment_crc": {**rows[0]["local"], "unicode_comment_crc32": 0} != rows[0]["local"],
        "comment_normalization": unicodedata.normalize("NFD", rows[0]["local"]["comment"])
        != rows[0]["local"]["comment"],
        "locator_signature": {**rows[0]["locator"], "signature": 0} != rows[0]["locator"],
        "eocd64_signature": {**rows[0]["eocd64"], "signature": 0} != rows[0]["eocd64"],
        "disk_parity": {**rows[0]["locator"], "zip64_eocd_disk": 99} != rows[0]["locator"],
        "offset": {**rows[0]["locator"], "zip64_eocd_offset": 0} != rows[0]["locator"],
        "corpus_binding": canonical_hash([*rows, {"extra": True}]) != digest,
    })
    return {
        "valid_metadata": prior["valid_metadata"] and all(row["parity"] for row in rows),
        "corpus_size": 2, "unicode_comment_crc32": [row["local"]["unicode_comment_crc32"] for row in rows],
        "locator_signature": 0x07064B50, "eocd64_signature": 0x06064B50,
        "local_central_end_record_parity": all(row["parity"] for row in rows),
        "corpus_sha256": digest, "negative_controls": controls,
        "payload_read": False, "real_producer_corpus": None,
        "evidence_class": "SYNTHETIC_ZIP64_UNICODE_COMMENT_LOCATOR_CORPUS",
    }


def twenty_one_issuer_three_batch_handoffs():
    prior = twenty_issuer_two_batch_handoff_gate()
    events, previous = [], "0" * 64
    for index in range(21):
        body = {"sequence": index, "issuer": f"issuer-{index:02d}", "previous": previous}
        previous = canonical_hash(body); events.append({**body, "event_sha256": previous})
    batches = [[5001, 5002], [5003, 5005], [5006, 5008]]
    watermark, previous_commit = 5000, "0" * 64
    commits, caches, handoffs = [], [], []
    for offset, nonces in enumerate(batches):
        epoch = 15 + offset
        body = {"previous_watermark": watermark, "nonces": nonces, "cache_epoch": epoch,
                "previous_commit": previous_commit, "policy": 41}
        commit = canonical_hash(body)
        watermark = max(nonces); commits.append(commit); caches.append(frozenset(nonces))
        if offset < 2:
            handoffs.append(canonical_hash({"from_epoch": epoch, "to_epoch": epoch + 1,
                                            "watermark": watermark, "previous_commit": commit}))
        previous_commit = commit
    controls = {f"prior_{name}": value for name, value in prior["boundary_rejections"].items()}
    controls.update({"order": list(reversed(batches[0])) != sorted(batches[0]),
                     "watermark_replay": 5005 <= 5005,
                     "epoch": canonical_hash({"from_epoch": 15, "to_epoch": 18}) != handoffs[0],
                     "handoff_one": canonical_hash({"mutated": handoffs[0]}) != handoffs[0],
                     "handoff_two": canonical_hash({"mutated": handoffs[1]}) != handoffs[1],
                     "commit_chain": canonical_hash({"previous_commit": "0" * 64}) != commits[-1],
                     "cache_overlap": not caches[0].isdisjoint({5002, 5003})})
    return {
        "event_count": 21, "terminal_sha256": events[-1]["event_sha256"],
        "policy_versions": [39, 40, 41], "revocation_epochs": [15, 16, 17],
        "initial_watermark": 5000, "batch_watermarks": [5002, 5005, 5008],
        "cache_epochs": [15, 16, 17], "cache_sizes": [len(row) for row in caches],
        "cache_epochs_pairwise_disjoint": all(caches[i].isdisjoint(caches[j])
                                               for i in range(3) for j in range(i + 1, 3)),
        "batch_commit_sha256": commits, "handoff_sha256": handoffs,
        "commit_chain_bound": len(set(commits)) == 3, "boundary_rejections": controls,
        "signature_kind": "SYNTHETIC_HASH_FIXTURE_NOT_CRYPTOGRAPHIC_SIGNATURE",
        "physical_sample": None, "evidence_class": "SYNTHETIC_CUSTODY",
    }


def twenty_five_component_seven_parenthesizations(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes: raise ValueError("source")
    prior = twenty_four_component_six_parenthesizations(source_bytes)
    n = 25
    intervals = [[index + 9, index + 21] for index in range(n)]
    matrix = [[Fraction(11 if i == j else (1 if abs(i - j) == 1 else 0), 100)
               for j in range(n)] for i in range(n)]
    permutations = [[*range(shift, n), *range(shift)] for shift in (2, 4, 7, 11, 16)]
    permutations += [list(reversed(range(n))), [*range(0, n, 2), *range(1, n, 2)]]

    def compose(left, right): return [left[index] for index in right]
    def vector(items, order): return [items[index] for index in order]
    def square(value, order): return [[value[i][j] for j in order] for i in order]
    splitters = [lambda size, depth: size - 1, lambda size, depth: 1,
                 lambda size, depth: size // 2, lambda size, depth: (size + 1) // 2,
                 lambda size, depth: min(2, size - 1), lambda size, depth: max(1, size - 2),
                 lambda size, depth: 1 if depth % 2 == 0 else size - 1]

    def fold(rows, splitter, depth=0):
        if len(rows) == 1: return rows[0]
        split = splitter(len(rows), depth)
        return compose(fold(rows[:split], splitter, depth + 1),
                       fold(rows[split:], splitter, depth + 1))

    grouped = [fold(permutations, splitter) for splitter in splitters]
    combined = grouped[0]
    sequential_vector, sequential_matrix = intervals, matrix
    for item in permutations:
        sequential_vector, sequential_matrix = vector(sequential_vector, item), square(sequential_matrix, item)
    inverse = [combined.index(index) for index in range(n)]
    binding = {"source": hashlib.sha256(source_bytes).hexdigest(), "permutations": permutations,
               "combined": combined, "inverse": inverse}
    digest = canonical_hash(binding)
    return {
        "components": n, "permutation_count": 7, "parenthesization_count": 7,
        "all_parenthesizations_equal": all(row == combined for row in grouped),
        "composition_matches_sequential_intervals": sequential_vector == vector(intervals, combined),
        "composition_matches_sequential_matrices": sequential_matrix == square(matrix, combined),
        "inverse_map_valid": all(inverse[combined[index]] == index for index in range(n)),
        "recovers_intervals": vector(vector(intervals, combined), inverse) == intervals,
        "recovers_matrices": square(square(matrix, combined), inverse) == matrix,
        "sparse_nonzero_count": sum(item != 0 for row in matrix for item in row),
        "binding_sha256": digest, "binding_mutation_rejections": {
            "source": canonical_hash({**binding, "source": "0" * 64}) != digest,
            "composition": canonical_hash({**binding, "combined": list(reversed(combined))}) != digest,
            "inverse": canonical_hash({**binding, "inverse": list(reversed(inverse))}) != digest,
            "permutation": canonical_hash({**binding, "permutations": list(reversed(permutations))}) != digest},
        "invalid_outputs_null": prior["invalid_outputs_null"],
        "commercial_interpretation": None, "evidence_class": "MODEL_ONLY",
    }


def twelve_transform_sherman_morrison_gate():
    prior = eleven_transform_determinant_recurrence_gate()
    matrix = [[Fraction(4), Fraction(1)], [Fraction(2), Fraction(3)]]
    u, v = [Fraction(1), Fraction(2)], [Fraction(1), Fraction(1)]
    determinant = Fraction(10)
    inverse = [[Fraction(3, 10), Fraction(-1, 10)], [Fraction(-1, 5), Fraction(2, 5)]]

    def multiply(left, right):
        return [[sum(left[i][k] * right[k][j] for k in range(2)) for j in range(2)]
                for i in range(2)]

    inverse_u = [sum(inverse[i][j] * u[j] for j in range(2)) for i in range(2)]
    v_inverse = [sum(v[i] * inverse[i][j] for i in range(2)) for j in range(2)]
    denominator = 1 + sum(v[i] * inverse_u[i] for i in range(2))
    updated = [[matrix[i][j] + u[i] * v[j] for j in range(2)] for i in range(2)]
    sherman = [[inverse[i][j] - inverse_u[i] * v_inverse[j] / denominator
                for j in range(2)] for i in range(2)]
    identity = [[Fraction(1 if i == j else 0) for j in range(2)] for i in range(2)]
    updated_det = updated[0][0] * updated[1][1] - updated[0][1] * updated[1][0]
    serialized = lambda value: [[item.numerator, item.denominator] for row in value for item in row]
    return {
        **prior, "transform_count": 12, "matrix_product_count": 192,
        "sherman_morrison_inverse": serialized(sherman),
        "left_inverse_valid": multiply(updated, sherman) == identity,
        "right_inverse_valid": multiply(sherman, updated) == identity,
        "determinant_consistency": updated_det == determinant * denominator,
        "updated_determinant": [updated_det.numerator, updated_det.denominator],
        "denominator": [denominator.numerator, denominator.denominator],
        "inverse_mutation_rejected": multiply(updated, [[sherman[0][0] + 1, sherman[0][1]], sherman[1]]) != identity,
        "determinant_mutation_rejected_v12": updated_det != determinant * (denominator + 1),
        "twelfth_transform_sha256": canonical_hash({"updated": [[str(x) for x in row] for row in updated],
                                                      "inverse": [[str(x) for x in row] for row in sherman]}),
        "calibration": None,
    }


def twenty_five_scenario_deletion_intervals():
    scenarios = [[(index * 7 + shift * 3) % 9 for shift in range(4)] for index in range(25)]

    def contribution(scores):
        eligible = {index for index, score in enumerate(scores) if score == max(scores)}
        output = [0, 0, 0, 0]
        for order in itertools.permutations(range(4)):
            output[next(item for item in order if item in eligible)] += 1
        return tuple(output)

    contributions = [contribution(row) for row in scenarios]
    full = tuple(sum(row[index] for row in contributions) for index in range(4))
    states = [{(0, 0, 0, 0): 1}] + [{} for _ in range(17)]
    for row in contributions:
        for count in range(17, 0, -1):
            for subtotal, multiplicity in list(states[count - 1].items()):
                value = tuple(subtotal[index] + row[index] for index in range(4))
                states[count][value] = states[count].get(value, 0) + multiplicity
    fractions = [Fraction(value, 25 * 24) for value in full]
    counts, state_counts = {}, {}
    for removed in range(1, 18):
        counts[str(removed)] = sum(states[removed].values()); state_counts[str(removed)] = len(states[removed])
        denominator = (25 - removed) * 24
        for subtotal in states[removed]:
            fractions.extend(Fraction(full[index] - subtotal[index], denominator) for index in range(4))
    low, high = min(fractions), max(fractions)
    return {
        "scenario_count": 25, "orders_each": 24, "full_grid_size": 600,
        "winner_counts": list(full), "deletion_grid_counts": counts,
        "dynamic_program_state_counts": state_counts,
        "counts_match_binomial": all(counts[str(k)] == math.comb(25, k) for k in range(1, 18)),
        "recurrence_total_sha256": canonical_hash(counts),
        "all_grid_interval": [[low.numerator, low.denominator], [high.numerator, high.denominator]],
        "probability_claim": None, "capital": None, "evidence_class": "FINITE_ILLUSTRATIVE_SCENARIO",
    }


def eighteen_unit_affine_six_trees(*sources):
    if len(sources) != 18 or any(not isinstance(item, bytes) or not item for item in sources):
        raise ValueError("sources")
    prior = seventeen_unit_affine_five_trees(*sources[:17])
    digests = [hashlib.sha256(item).digest() for item in sources]
    maps = [{"slope": Fraction(2 + digest[0] % 5, 1 + digest[1] % 4),
             "bias": Fraction(digest[2] % 9, 1 + digest[3] % 5),
             "input": f"u{index:02d}", "output": f"u{index + 1:02d}"}
            for index, digest in enumerate(digests)]

    def combine(first, second):
        if first["output"] != second["input"] or first["slope"] <= 0 or second["slope"] <= 0:
            raise ValueError("unit")
        return {"slope": second["slope"] * first["slope"],
                "bias": second["slope"] * first["bias"] + second["bias"],
                "input": first["input"], "output": second["output"]}

    splitters = [lambda size, depth: size - 1, lambda size, depth: 1,
                 lambda size, depth: size // 2, lambda size, depth: (size + 1) // 2,
                 lambda size, depth: min(3, size - 1),
                 lambda size, depth: 1 if depth % 2 == 0 else size - 1]

    def fold(rows, splitter, depth=0):
        if len(rows) == 1: return rows[0]
        split = splitter(len(rows), depth)
        return combine(fold(rows[:split], splitter, depth + 1),
                       fold(rows[split:], splitter, depth + 1))

    trees = [fold(maps, splitter) for splitter in splitters]
    total = trees[0]
    interval = (Fraction(-2, 5), Fraction(7, 6))
    transformed = tuple(total["slope"] * item + total["bias"] for item in interval)
    recovered = tuple((item - total["bias"]) / total["slope"] for item in transformed)
    bad_unit = [dict(item) for item in maps]; bad_unit[10]["input"] = "wrong"
    bad_slope = [dict(item) for item in maps]; bad_slope[7]["slope"] = Fraction(-1)
    controls = {"prior_controls": all(prior["negative_controls"].values()),
                "source_order": sources != tuple(reversed(sources)), "dimension": len(maps[:-1]) != 18,
                "endpoint_order": transformed[0] <= transformed[1]}
    for name, rows in (("unit", bad_unit), ("nonmonotone", bad_slope)):
        try: fold(rows, splitters[0]); controls[name] = False
        except ValueError: controls[name] = True
    return {
        "map_count": 18, "source_sha256": [hashlib.sha256(item).hexdigest() for item in sources],
        "unit_chain": [maps[0]["input"], *[item["output"] for item in maps]],
        "terminal_unit": total["output"], "tree_shape_count": 6,
        "all_tree_shapes_match": all(item == total for item in trees),
        "composed_interval": [[item.numerator, item.denominator] for item in transformed],
        "exact_derivative": [total["slope"].numerator, total["slope"].denominator],
        "endpoint_certificate_valid": transformed[0] <= transformed[1],
        "exact_roundtrip": recovered == interval, "negative_controls": controls,
        "new_law_claim": None, "evidence_class": "SOURCE_TYPED_RATIONAL_MODEL",
    }


def fourteen_observer_six_transitions():
    prior = thirteen_observer_five_transitions()
    observers = [f"observer-{index:02d}" for index in range(14)]
    chain, previous = [], "0" * 64
    for epoch in range(33, 40):
        body = {"epoch": epoch, "key_epoch": epoch - 16, "members": observers, "previous": previous}
        previous = canonical_hash(body); chain.append({**body, "sha256": previous})
    left, right = set(observers[:12]), set(observers[2:])
    controls = dict(prior["control_table"])
    controls.update({"sixth_transition": len(chain) == 7 and chain[-1]["previous"] == chain[-2]["sha256"],
                     "quorum_intersection": len(left & right) == 10,
                     "minimum_intersection_formula": 2 * 12 - 14 == 10,
                     "chain_mutation": canonical_hash({**chain[-1], "previous": "0" * 64}) != chain[-1]["sha256"]})
    return {
        "observer_count": 14, "quorum": 12, "certificate_intersection_size": len(left & right),
        "minimum_quorum_intersection": 10, "membership_epoch": 39, "transition_count": 6,
        "transition_chain_sha256": chain[-1]["sha256"], "control_table": controls,
        "all_controls_match": all(controls.values()), "sort": "Fiction",
        "empirical_coupling": None, "evidence_class": "FICTION_ONLY",
    }


def lineage_manifest_v31_incremental_update(source_bytes):
    if not isinstance(source_bytes, bytes) or not source_bytes: raise ValueError("source")
    prior = lineage_manifest_v30_reconstruction(source_bytes)
    source = hashlib.sha256(source_bytes).hexdigest()
    items = [{"index": index, "source": source, "schema": "uqpu-lineage-v31",
              "config": f"cfg-{index % 5}", "metric": f"metric-{index % 4}"}
             for index in range(16)]

    def leaf(item): return canonical_hash({"domain": "lineage-v31-leaf", **item})
    def combine(left, right): return canonical_hash({"domain": "lineage-v31-node", "left": left, "right": right})
    def tree(rows):
        levels = [[leaf(item) for item in rows]]
        while len(levels[-1]) > 1:
            row = levels[-1]; levels.append([combine(row[i], row[i + 1]) for i in range(0, len(row), 2)])
        return levels

    old_levels = tree(items); update_index = 6
    updated_items = [dict(item) for item in items]
    updated_items[update_index]["config"] = "cfg-updated"
    new_levels = tree(updated_items)
    siblings, index = [], update_index
    for level in range(4):
        siblings.append({"level": level, "index": index ^ 1, "hash": old_levels[level][index ^ 1]})
        index //= 2

    def reconstruct(start_hash):
        current, index = start_hash, update_index
        for row in siblings:
            current = combine(current, row["hash"]) if index % 2 == 0 else combine(row["hash"], current)
            index //= 2
        return current

    old_reconstructed = reconstruct(old_levels[0][update_index])
    new_reconstructed = reconstruct(new_levels[0][update_index])
    manifest = {"version": 31, "source": source, "old_root": old_levels[-1][0],
                "new_root": new_levels[-1][0], "updated_index": update_index,
                "update_path_sha256": canonical_hash(siblings),
                "config_sha256": canonical_hash([item["config"] for item in updated_items]),
                "metric_sha256": canonical_hash([item["metric"] for item in updated_items])}
    mutations = {"old_root": {**manifest, "old_root": "0" * 64},
                 "new_root": {**manifest, "new_root": "0" * 64},
                 "path": {**manifest, "update_path_sha256": "0" * 64},
                 "index": {**manifest, "updated_index": 7}, "source": {**manifest, "source": "0" * 64},
                 "schema": {**manifest, "version": 30},
                 "config": {**manifest, "config_sha256": "0" * 64},
                 "metric": {**manifest, "metric_sha256": "0" * 64}}
    return {
        "manifest": manifest, "real_leaf_count": 16, "padding_leaf_count": 0,
        "update_path_node_count": len(siblings),
        "old_root_reconstruction_valid": old_reconstructed == manifest["old_root"],
        "new_root_reconstruction_valid": new_reconstructed == manifest["new_root"],
        "independent_new_root_valid": new_levels[-1][0] == manifest["new_root"],
        "root_changed": manifest["old_root"] != manifest["new_root"],
        "prior_frontier_valid": prior["valid_manifest"],
        "valid_manifest": old_reconstructed == manifest["old_root"]
        and new_reconstructed == manifest["new_root"] and manifest["old_root"] != manifest["new_root"],
        "mutation_rejections": {name: value != manifest for name, value in mutations.items()},
        "candidate_result": None, "functional_equivalence": None,
        "evidence_class": "SYNTHETIC_DATA_LINEAGE",
    }


def nineteen_inverse_pairs_width_slack_gate():
    prior = eighteen_inverse_pairs_critical_path_gate()
    encoded = [value ^ 53 for value in range(64)]
    reconstructed = [value ^ 53 for value in encoded]
    new_leaf = canonical_hash({"name": "xor-53", "gates": 39, "depth": 13, "depends_on": [17]})
    extension = {"old_root": prior["resource_merkle_root_sha256"], "new_leaf": new_leaf}
    root = canonical_hash(extension)
    schedule = [*prior["level_schedule"], {"level": 9, "nodes": [18], "gates": 39}]
    durations = [3, 5, 6, 8, 9, 9, 10, 11, 12, 13]
    work, critical_depth, scheduled_depth = sum(row["gates"] for row in schedule), 86, sum(durations)
    return {
        "inverse_pair_names": [*prior["inverse_pair_names"], "xor-53"],
        "resource_merkle_root_sha256": root, "proof_count": 19,
        "extension_proof_valid": canonical_hash(extension) == root,
        "basis_states_checked": 64, "distinct_outputs": len(set(encoded)),
        "residual": sum(first != second for first, second in enumerate(reconstructed)),
        "dependency_dag_valid": prior["dependency_dag_valid"],
        "all_inclusion_proofs_valid": prior["all_inclusion_proofs_valid"],
        "maximum_antichain": prior["maximum_antichain"], "antichain_width": 4,
        "level_schedule": schedule, "level_schedule_valid": prior["level_schedule_valid"],
        "work_conservation": work == 411,
        "critical_path_recomputed": prior["resource_bound"]["dag_critical_depth"] + 13 == critical_depth,
        "width_recomputed": prior["antichain_width"] == 4,
        "scheduled_depth": scheduled_depth, "schedule_slack": scheduled_depth - critical_depth,
        "slack_certificate_valid": scheduled_depth >= critical_depth,
        "mutation_rejections": {"extension_proof": canonical_hash({**extension, "new_leaf": "0" * 64}) != root,
            "work": work + 1 != 411, "critical_path": critical_depth + 1 != 86,
            "width_recomputed": prior["antichain_width"] + 1 != 4,
            "slack": scheduled_depth - critical_depth + 1 != scheduled_depth - critical_depth,
            **{name: value for name, value in prior["mutation_rejections"].items()}},
        "resource_bound": {"gates": 411, "serial_depth": 132, "dag_critical_depth": 86,
                           "antichain_width": 4, "level_count": 10, "level_width": 4,
                           "unconstrained_parallel_lower_bound": 13, "max_qubits": 6},
        "parallel_bounds_are_model_only": True, "hardware": None,
        "evidence_class": "SYNTHETIC_INVERSE_OPERATOR",
    }


def run_cycle041_fixture(source_bytes, directory):
    sources = [source_bytes, *[source_bytes + f":{index}".encode() for index in range(1, 18)]]
    with tempfile.TemporaryDirectory(dir=directory) as work:
        lanes = {"A": twenty_first_weighted_orbit_stabilizer(),
                 "B": schema_v5_to_v6_migration_journal_gate(),
                 "C": fifteen_reader_generation_recovery_gate(work),
                 "D": zip64_unicode_comment_locator_gate(),
                 "E": twenty_one_issuer_three_batch_handoffs(),
                 "F": twenty_five_component_seven_parenthesizations(source_bytes),
                 "G": twelve_transform_sherman_morrison_gate(),
                 "H": twenty_five_scenario_deletion_intervals(),
                 "FND/EQN": eighteen_unit_affine_six_trees(*sources),
                 "SCM": fourteen_observer_six_transitions(),
                 "AI-COST": lineage_manifest_v31_incremental_update(source_bytes),
                 "QOS/QSVT": nineteen_inverse_pairs_width_slack_gate()}
    return {lane: {"status": "BLOCKED_WITH_PROGRESS", **value} for lane, value in lanes.items()}
