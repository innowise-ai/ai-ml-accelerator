#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json, random
random.seed(41)
topics = ["billing", "shipping", "returns", "account access", "product specs", "warranty"]
sentiments = ["neutral", "frustrated", "polite"]
rows = []
for i in range(200):
    t = topics[i % len(topics)]
    rows.append({
        "id": f"t-{i:04d}",
        "topic": t,
        "sentiment": random.choice(sentiments),
        "turns": random.randint(2, 9),
        "resolved": random.random() > 0.28,
        "user_message": f"[{t}] customer question {i}",
        "assistant_answer": f"[{t}] assistant reply {i}",
    })
with open("traces.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")
PY

cat >README.md <<'EOF'
# support-copilot traces

200 exported traces. No error analysis has been done on this product.
EOF
