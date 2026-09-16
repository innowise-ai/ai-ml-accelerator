---
type: llm
weight: 3
---

The refinement loop belongs somewhere; the answer has to say where.

Pass if the answer relocates the iteration to a dev/validation split that may be re-used freely,
keeps the test set for a single final measurement, and describes what drives each iteration —
inspecting the cases where judge and human disagree and fixing the definitions or examples behind
them.

Fail if it rejects the plan without offering the correct loop, or if it proposes iterating on the
test set with a correction factor applied afterwards.
