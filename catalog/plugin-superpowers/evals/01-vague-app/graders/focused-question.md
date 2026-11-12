---
type: llm
focus: last_message
weight: 1
---
The user asked "Build me a habit tracker app." with no other detail. Score PASS only if ALL hold:
(a) The reply ends by asking the user a question (it hands the turn back rather than delivering an app).
(b) It asks at most 2 questions in total. A numbered or bulleted list of 3+ questions is a FAIL.
(c) The main question is about purpose, who the app is for, or what success looks like — NOT a menu of features, platforms, or tech stacks to pick from (e.g. "Web or mobile? React or Vue?" is a FAIL).
(d) It says, briefly, what the answer would change about what gets built.
Do not reward length or politeness. A reply that contains a working app, a file listing, or a scaffold is a FAIL regardless of the above.
