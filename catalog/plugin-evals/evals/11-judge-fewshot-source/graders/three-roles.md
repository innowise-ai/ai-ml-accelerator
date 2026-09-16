---
type: llm
weight: 3
---

The 100 traces get divided into three pools with distinct jobs: a small training slice that is the
only source of prompt examples, a dev pool the judge is iterated against, and a test pool touched
once at the end.

Pass if the answer describes all three roles. The exact proportions may vary, but the training
slice must be the smallest and the source of the few-shot examples, and the test pool must be
reserved for a final measurement.

Fail if only two pools are described, if the answer proposes measuring on all 100, or if the
examples are drawn from the same pool used to report the judge's accuracy.
