#!/usr/bin/env bash
# Builds the fixture inside the eval's temp directory so the no-plugin arm never sees a path
# into the catalog (one directory walk from SKILL.md and these graders).
set -euo pipefail

mkdir -p evals

cat >evals/judge_prompt.txt <<'EOF'
You are evaluating the output of our customer support assistant.

Rate the overall helpfulness of the assistant's answer on a scale of 1 to 5, where
1 = not helpful at all and 5 = extremely helpful. Consider tone, accuracy,
completeness and whether the customer would be satisfied.

Reply with the number only.
EOF

cat >evals/run_eval.py <<'EOF'
import json, statistics
from openai import OpenAI

client = OpenAI()
PROMPT = open("evals/judge_prompt.txt").read()

def score(trace):
    r = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": PROMPT},
                  {"role": "user", "content": trace["assistant_answer"]}],
    )
    return int(r.choices[0].message.content.strip())

rows = [json.loads(l) for l in open("evals/traces.jsonl")]
scores = [score(t) for t in rows]
print("mean helpfulness:", statistics.mean(scores))
EOF

cat >evals/traces.jsonl <<'EOF'
{"id": 1, "user_message": "my order 88121 never arrived", "assistant_answer": "I'm sorry about that! Your order is marked delivered on Tuesday. Please check with your neighbours."}
{"id": 2, "user_message": "how do I cancel my plan", "assistant_answer": "You can cancel any time from Settings > Billing > Cancel plan. Your access continues until the end of the period."}
{"id": 3, "user_message": "do you ship to Norway", "assistant_answer": "Yes, we ship worldwide. Delivery to Norway typically takes 4-7 business days."}
{"id": 4, "user_message": "I was charged twice in March", "assistant_answer": "Duplicate charges usually settle within 5 days. If it has not cleared, contact your bank."}
{"id": 5, "user_message": "is the XR-200 waterproof", "assistant_answer": "The XR-200 carries an IP68 rating, so it is fully waterproof to 2 metres for 30 minutes."}
EOF

cat >README.md <<'EOF'
# support-copilot

Customer support assistant. Quality tracking lives in `evals/`: we run `run_eval.py`
weekly and post the mean helpfulness score in the team channel.
EOF
