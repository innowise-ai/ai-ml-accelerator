---
type: llm
weight: 2
---

The fix is three disjoint splits with distinct jobs.

Pass if the answer prescribes splitting the labelled data into a training portion (the only source
of few-shot examples), a dev portion for iterating on the judge, and a held-out test portion for
the final number — and states that examples used in the prompt must be excluded from the measured
sets.

Fail if the fix is only "use more data", "remove the examples from the prompt", or a two-way split
with no separation between the set used for iteration and the set used for the final figure.
