#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json

SYSTEM = ("You are a code-review assistant. Review the diff, explain the risk in markdown, "
          "and return a verdict. Always cite file and line. Never approve a change that "
          "removes a test.")

rows = []
for i in range(24):
    rows.append({
        "id": f"rev-{i:03d}",
        "repo": "payments-api",
        "pr": 4100 + i,
        # identical in every record on purpose: the reviewer should not have to re-read it
        "system_prompt": SYSTEM,
        "diff": (
            "--- a/payments/retry.py\n"
            "+++ b/payments/retry.py\n"
            "@@ -12,7 +12,7 @@\n"
            "-    for attempt in range(MAX_RETRIES):\n"
            "+    while True:\n"
            "         try:\n"
            "             return charge(order)\n"
        ),
        "tool_result": json.dumps({
            "linter": {"errors": [], "warnings": ["W0105 unused variable 'ctx'"]},
            "coverage": {"before": 0.812, "after": 0.798, "files": [
                {"path": "payments/retry.py", "pct": 0.71},
                {"path": "payments/adapter.py", "pct": 0.88},
            ]},
        }),
        "assistant_answer": (
            f"## Verdict\n\n**Request changes.**\n\n"
            f"The change in `payments/retry.py:12` replaces a bounded loop with `while True`, "
            f"removing the retry cap.\n\n"
            f"- Risk: an unbounded retry loop under a failing downstream\n"
            f"- Coverage dropped from 81.2% to 79.8%\n"
        ),
    })

with open("traces.json", "w") as f:
    json.dump(rows, f, indent=2)
PY

cat >README.md <<'EOF'
# code-review assistant traces

24 traces for expert labelling. Each has the system prompt (identical across records),
a unified diff, a verbose tool result, and the assistant's markdown answer.
EOF
