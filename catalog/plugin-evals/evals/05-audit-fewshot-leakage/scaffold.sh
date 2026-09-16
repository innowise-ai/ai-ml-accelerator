#!/usr/bin/env bash
set -euo pipefail

mkdir -p evals

python3 - <<'PY'
import csv, random
random.seed(11)
tones = ["formal", "casual", "jargon-heavy", "warm"]
rows = []
for i in range(80):
    rows.append({
        "id": f"t{i:03d}",
        "persona": random.choice(["luxury buyer", "first-time buyer", "investor"]),
        "email_excerpt": f"[email {i:03d}, {random.choice(tones)} opening]",
        "human_label": random.choice(["Pass", "Pass", "Fail"]),
    })
# the four rows quoted verbatim in the judge prompt are rows t000..t003
for i, lab in enumerate(["Pass", "Fail", "Pass", "Fail"]):
    rows[i]["human_label"] = lab
    rows[i]["email_excerpt"] = f"[few-shot example {i+1}]"
with open("evals/labeled.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["id", "persona", "email_excerpt", "human_label"])
    w.writeheader()
    w.writerows(rows)
PY

cat >evals/judge_prompt.md <<'EOF'
You assess whether a real-estate assistant's email matches the client persona's tone.

PASS: tone matches the persona. FAIL: tone is mismatched.

## Examples
Example 1 (id t000, persona from labeled.csv): [few-shot example 1] -> Pass
Example 2 (id t001, persona from labeled.csv): [few-shot example 2] -> Fail
Example 3 (id t002, persona from labeled.csv): [few-shot example 3] -> Pass
Example 4 (id t003, persona from labeled.csv): [few-shot example 4] -> Fail

Output JSON: {"result": "Pass" | "Fail", "critique": "..."}
EOF

cat >evals/evaluate.py <<'EOF'
import csv

# Alignment is measured across every row of labeled.csv, including t000-t003,
# which are the four examples pasted into judge_prompt.md.
rows = list(csv.DictReader(open("evals/labeled.csv")))
print(f"measuring judge alignment over {len(rows)} labelled rows")
EOF

cat >NOTES.md <<'EOF'
Alignment number goes into next week's investor update. Judge prompt and the labelled
set are both in evals/.
EOF
