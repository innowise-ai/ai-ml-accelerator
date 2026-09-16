---
type: llm
weight: 3
---

First-pass retrieval is optimised for recall: a generator can ignore an irrelevant chunk, but it
cannot recover a chunk that was never retrieved.

Pass if the answer names Recall@k (or recall at some cutoff) as the primary first-pass retrieval
metric AND gives that asymmetry as the reason.

Fail if recall is not named for the retrieval stage, or is named with no reason attached, or if
precision is presented as the primary first-pass target.
