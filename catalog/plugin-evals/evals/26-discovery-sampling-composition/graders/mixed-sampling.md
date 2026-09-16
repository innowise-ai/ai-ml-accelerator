---
type: llm
weight: 3
---

Pure clustering samples miss whatever the feature space failed to capture; pure random sampling
over-represents the common case. The recipe mixes both, with clusters the larger share.

Pass if the selection combines cluster/group representatives with an explicitly random component,
AND the answer states why random picks are included — that the clustering may not capture every
dimension that matters.

Fail if the batch is purely random, purely cluster-based, or if a random component appears with no
reason given for it.
