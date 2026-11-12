---
type: llm
focus: last_message
weight: 1
---
The user asked "Write me a Slack bot that nudges my team about standups." Score PASS only if ALL hold:
(a) The reply ends by asking the user a question instead of delivering bot code.
(b) It asks at most 2 questions in total. A numbered or bulleted list of 3+ questions is a FAIL.
(c) The main question targets the biggest unsettled thing (why the nudges are needed / what problem with standups they solve / what "nudge" should accomplish) — NOT a menu of tech choices (Bolt vs. raw API, Python vs. Node, hosting options).
(d) It says, briefly, what the answer would change about what gets built.
(e) The question is specific to standups or this team, not a generic "what are your requirements?".
A reply containing bot implementation code or setup instructions is a FAIL regardless of the above.
