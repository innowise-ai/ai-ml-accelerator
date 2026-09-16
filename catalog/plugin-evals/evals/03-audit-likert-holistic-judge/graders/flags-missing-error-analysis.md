---
type: llm
weight: 2
---

Nothing in the fixture contains failure categories, labelled traces or review notes. The judge was
written from imagination, not from observed failures — which is why it measures "helpfulness".

Pass if the answer identifies that no error analysis / trace review / failure-mode definition work
has been done, and says the evaluator should be rebuilt from observed failure modes.

Fail if the absence of error analysis is never raised, or if the answer treats the missing piece as
merely "more test data" or "a bigger trace sample".
