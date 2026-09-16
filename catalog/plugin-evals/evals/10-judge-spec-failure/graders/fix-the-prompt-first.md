---
type: llm
weight: 3
---

The quoted system prompt contains no citation requirement. Measuring a behaviour that was never
asked for produces a judge that fails everything and tells the team nothing new.

Pass if the answer identifies that the system prompt does not request citations and says the
instruction should be added to the prompt before (or as a precondition of) relying on the judge.

Fail if the answer proceeds straight to writing the judge without noticing the omission, or treats
the missing citations purely as a model quality problem.
