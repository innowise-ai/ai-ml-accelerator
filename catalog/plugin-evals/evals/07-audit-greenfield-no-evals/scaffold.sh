#!/usr/bin/env bash
set -euo pipefail

cat >app.py <<'EOF'
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

SYSTEM = """You are a claims triage assistant for a mid-size insurer.
Given a customer's description of an incident, decide the claim category,
extract the incident date and estimated amount, and draft a reply to the customer."""

def triage(message: str) -> str:
    r = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": SYSTEM},
                  {"role": "user", "content": message}],
    )
    return r.choices[0].message.content
EOF

cat >TODO.md <<'EOF'
- [ ] add evals before the next release
- [ ] figure out what "good" means for triage replies
- [x] ship v1 to 200 pilot users
EOF

cat >README.md <<'EOF'
# claims-triage

Live with 200 pilot users since March. Request/response pairs are written to the
application log (about 6k of them so far). No test suite for the model output.
EOF
