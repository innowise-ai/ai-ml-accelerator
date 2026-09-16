---
type: llm
weight: 3
---

The two stages have different jobs, so they take different metrics.

Pass if the answer assigns a recall-style metric at the wide cutoff to the first-pass retrieval AND
an order-sensitive metric (Precision@k, MRR, or NDCG@k) to the reranker, keeping them distinct.

Fail if one metric is proposed for both stages, if only the end-to-end result is measured, or if
the reranker is evaluated on recall alone.
