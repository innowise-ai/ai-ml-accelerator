---
type: regex
target: last_message
pattern: 'MRR|NDCG|mean reciprocal rank|precision\s*@'
flags: 'i'
weight: 1
---

Mechanical check that a concrete order-sensitive metric is named for the reranking stage rather
than gestured at.
