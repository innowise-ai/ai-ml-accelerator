#!/usr/bin/env bash
set -euo pipefail

python3 - <<'PY'
import json, random
random.seed(23)

categories = ["auto-collision", "water-damage", "theft", "liability", "travel-delay"]
channels = ["email", "web form", "phone transcript"]

# Three failure modes are planted so a real review has something to find:
#  - the assistant invents a policy exclusion that was never in the documents
#  - it drops the incident date when the customer gave it in relative form ("last Tuesday")
#  - it answers in English when the customer wrote in another language
rows = []
for i in range(48):
    cat = random.choice(categories)
    ch = random.choice(channels)
    relative_date = i % 7 == 0
    invents_exclusion = i % 11 == 0
    wrong_language = i % 13 == 0

    user = f"[{ch}] Customer describes a {cat.replace('-', ' ')} incident"
    user += " that happened last Tuesday" if relative_date else " on 2026-03-14"
    if wrong_language:
        user = "[web form] Le client décrit un sinistre dégât des eaux survenu le 14 mars 2026"

    msgs = [
        {"role": "system", "content": "You are a claims triage assistant for a mid-size insurer. Categorise the claim, extract the incident date and estimated amount, and draft a reply."},
        {"role": "user", "content": user},
        {"role": "assistant", "content": f"Looking up the policy terms for {cat}."},
        {"role": "tool_call", "content": json.dumps({"name": "policy_lookup", "args": {"category": cat}})},
        {"role": "tool_result", "content": json.dumps({"deductible": 250, "covered": True, "notes": "standard terms"})},
    ]
    reply = f"Thank you for reporting your {cat.replace('-', ' ')} claim."
    reply += " We could not determine the incident date from your message." if relative_date else " Incident date recorded as 14 March 2026."
    if invents_exclusion:
        reply += " Please note that claims arising from tenant negligence are excluded under your policy."
    if wrong_language:
        reply = "Thank you for reporting your water damage claim. Incident date recorded as 14 March 2026."
    msgs.append({"role": "assistant", "content": reply})

    rows.append({
        "id": f"clm-{i:03d}",
        "category": cat,
        "channel": ch,
        "turns": len(msgs),
        "messages": msgs,
    })

with open("traces.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r, ensure_ascii=False) + "\n")
PY

cat >README.md <<'EOF'
# claims-triage traces

48 triage traces exported from the pilot. Nobody has reviewed them yet.
EOF
