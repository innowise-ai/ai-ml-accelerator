---
type: llm
weight: 2
---

The reason a single number fails is class imbalance: when most traces pass, a judge that always
says Pass scores high while catching nothing.

Pass if the answer explains why the aggregate is misleading in terms of the class distribution —
for example that a trivial always-Pass judge would score close to 88% on a set where most traces
pass.

Fail if the answer swaps the metric without explaining what goes wrong with the old one, or blames
only the sample size.
