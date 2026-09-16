---
type: llm
weight: 2
---

The reason this matters beyond one trace: a generator filling gaps from memory makes retrieval
failures invisible in end-to-end scoring, and the failure only surfaces when the parametric answer
is wrong or out of date.

Pass if the answer makes that point — that passing such traces hides retrieval problems, or that
the same behaviour will produce a confident wrong answer once the policy changes.

Fail if the answer corrects the verdict without explaining why the pattern is dangerous.
