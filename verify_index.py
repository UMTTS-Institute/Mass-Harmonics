#!/usr/bin/env python3
from pathlib import Path
import json, sys

root = Path(__file__).resolve().parent
index = json.loads((root / "MH_Canonical_Causal_Map_Index_Web.json").read_text(encoding="utf-8"))
lock = json.loads((root / "MH_Canonical_Causal_Map_Index_Web_SOURCE_LOCK.json").read_text(encoding="utf-8"))

errors = []

if index["source_lock"]["commit"] != lock["source_baseline_commit"]:
    errors.append("baseline commit mismatch")
if index["source_lock"]["tree"] != lock["source_baseline_tree"]:
    errors.append("baseline tree mismatch")

source_ids = set(lock["sources"])
node_ids = [n["id"] for n in index["nodes"]]
if len(node_ids) != len(set(node_ids)):
    errors.append("duplicate node IDs")

for n in index["nodes"]:
    if n["source"] not in source_ids:
        errors.append(f"node {n['id']} references unknown source {n['source']}")
    for field in ("locator", "anchor", "purpose"):
        if not str(n.get(field, "")).strip():
            errors.append(f"node {n['id']} missing {field}")

for chain in index["canonical_chains"]:
    if chain["source"] not in source_ids:
        errors.append(f"chain {chain['id']} references unknown source")
    if len(chain["chain"]) < 2:
        errors.append(f"chain {chain['id']} is too short")

# Regression sentinels inspect declared chains only, not the prose record that names repaired failures.
declared_chain_strings = [" → ".join(c["chain"]) for c in index["canonical_chains"]]
if any("CORE_TO_IONOSPHERE_SAA → COBALT_NUCLEAR_SPIN" in c for c in declared_chain_strings):
    errors.append("prohibited legacy SAA->Cobalt causal edge reintroduced")
if any("CASIMIR_EFFECT → TVP_PROTOCOL" in c for c in declared_chain_strings):
    errors.append("prohibited legacy Casimir->TVP causal edge reintroduced")

brain = next((n for n in index["nodes"] if n["id"] == "BIOLOGICAL_METABOLISM"), None)
if brain and "exactly 20.0 W" in (brain["anchor"] + " " + brain["purpose"]):
    errors.append("Resonant Brain approximately-20-W result amplified to exact 20.0 W")

print(f"nodes={len(index['nodes'])}")
print(f"sources={len(lock['sources'])}")
print(f"chains={len(index['canonical_chains'])}")
print("status=" + ("PASS" if not errors else "FAIL"))

if errors:
    for e in errors:
        print("ERROR:", e)
    sys.exit(1)
