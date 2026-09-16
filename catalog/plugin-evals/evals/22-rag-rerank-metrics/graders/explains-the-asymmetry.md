---
type: llm
weight: 2
---

The reason is the pipeline's shape: the first pass sets the ceiling, and nothing the reranker does
can recover a document the first pass dropped.

Pass if the answer explains why the metrics differ in those terms — the first stage bounds what is
achievable, the second stage only reorders what it was given.

Fail if the metrics are assigned with no reasoning, or the reasoning is limited to "recall is for
retrieval, precision is for ranking" with no account of why.
