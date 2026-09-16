---
type: llm
weight: 3
---

Predefined failure categories in the first build are guesses presented as options, and reviewers
anchor to them instead of reporting what they actually see.

Pass if the delivered interface ships no predefined failure-mode categories — no dropdown of
failure types, no tag picker, no category checkboxes, no severity taxonomy. Binary Pass/Fail
buttons and a defer control are structural, not a taxonomy, and do not fail this grader.

Fail if the build includes a list of named failure categories for the reviewer to choose from,
however it is presented.
