---
type: llm
weight: 3
---

ROUGE and BERTScore compare a generated summary against a reference string. They suit retrieval
ranking, not generation quality: a summary that names the wrong root cause in the reference's
vocabulary can outscore a correct summary written differently.

Pass if the answer states that these metrics measure surface or semantic overlap with a reference
rather than correctness, and that they are not a trustworthy primary quality signal for this
generation task.

Fail if the metrics are treated as valid, or if the only criticism is that there are too few
reference summaries or that a different ROUGE variant would be better.
