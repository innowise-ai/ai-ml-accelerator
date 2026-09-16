---
type: llm
weight: 3
---

The replacement is several binary judges, each tied to one observable failure in this pipeline.

Pass if the answer proposes at least three separate checks named after distinct failure modes of
this trace — for example: the knowledge-base search missed the relevant article, the refund call
used wrong parameters, the reply contradicts the retrieved policy, the reply's tone is off.

Fail if only one judge is proposed, or if the decomposition is into generic axes (accuracy,
helpfulness, tone) rather than failures specific to this pipeline.
