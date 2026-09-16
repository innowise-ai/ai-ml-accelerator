#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json, os, random
random.seed(59)
topics = ["billing", "shipping", "returns", "account access", "warranty"]
rows = []
for i in range(200):
    t = topics[i % len(topics)]
    rows.append({
        "id": f"t-{i:04d}",
        "topic": t,
        "turns": random.randint(2, 9),
        "user_message": f"[{t}] customer question {i}",
        "assistant_answer": f"[{t}] assistant reply {i}",
    })
with open("traces.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")

os.makedirs("error_discovery_data", exist_ok=True)
# exactly one annotation, on one record
with open("error_discovery_data/annotations.json", "w") as f:
    json.dump([{
        "record_id": "t-0007",
        "quote": "assistant reply 7",
        "note": "told the customer to check with their bank instead of looking up the charge",
        "created_at": "2026-05-02T10:14:00Z"
    }], f, indent=2)
PY
