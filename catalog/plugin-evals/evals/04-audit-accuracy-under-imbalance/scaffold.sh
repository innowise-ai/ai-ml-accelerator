#!/usr/bin/env bash
set -euo pipefail

mkdir -p evals

# 100 labels, 90 Pass / 10 Fail: an always-Pass judge scores 90% "accuracy" here.
python3 - <<'PY'
import json, random
random.seed(7)
rows = []
for i in range(100):
    human = "Pass" if i >= 10 else "Fail"
    # the judge agrees on every Pass and catches only 1 of the 10 Fails
    judge = "Pass" if human == "Pass" else ("Fail" if i == 3 else "Pass")
    rows.append({"id": i, "human_label": human, "judge_label": judge})
with open("evals/labels.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")
PY

cat >evals/metrics.py <<'EOF'
import json

rows = [json.loads(l) for l in open("evals/labels.jsonl")]
agree = sum(1 for r in rows if r["human_label"] == r["judge_label"])
print(f"accuracy: {agree / len(rows):.0%}")
print(f"percent agreement: {agree / len(rows):.0%}")
EOF

cat >evals/judge_prompt.md <<'EOF'
You check whether a refund-policy answer from our assistant is correct.

PASS: the answer states the correct refund window and the correct exceptions.
FAIL: the answer states a wrong window, invents an exception, or omits a stated exception.

Reply with PASS or FAIL.
EOF

cat >NOTES.md <<'EOF'
Judge shipped in March. metrics.py reports 91% accuracy against our labelled set,
so we turned off manual spot checks.
EOF
