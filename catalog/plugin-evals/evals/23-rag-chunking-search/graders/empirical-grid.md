---
type: llm
weight: 3
---

Chunking interacts with the corpus, the embedding model and the query mix, so the right value is
measured rather than recommended.

Pass if the answer prescribes sweeping multiple configurations — varying chunk size AND overlap —
re-indexing for each and comparing retrieval metrics on a fixed evaluation set, with the decision
coming from that comparison.

Fail if the answer recommends a specific chunk size as the fix, sweeps size while ignoring overlap,
or proposes changing the chunking and watching end-to-end answer quality instead of retrieval
metrics.
