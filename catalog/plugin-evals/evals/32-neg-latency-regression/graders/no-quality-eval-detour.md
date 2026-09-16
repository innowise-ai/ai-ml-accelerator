---
type: llm
weight: 3
---

This is a performance regression. Output quality is not in question and no evaluator would surface
a latency change.

Pass if the answer does not prescribe error analysis on traces, failure-mode discovery, LLM judges
or eval datasets as part of diagnosing the latency regression.

Fail if any of that is proposed as a step here.
