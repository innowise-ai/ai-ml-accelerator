---
type: llm
weight: 2
---

The second finding is upstream: the chunk stating the refund window was not retrieved, and the
generator covered for it.

Pass if the answer identifies the retrieval miss as a separate problem and points at the retrieval
side — recall at the current cutoff, chunking, or the embedding/query setup — as what to examine.

Fail if the whole trace is treated as a generation-side issue, or the retrieval gap goes unmentioned.
