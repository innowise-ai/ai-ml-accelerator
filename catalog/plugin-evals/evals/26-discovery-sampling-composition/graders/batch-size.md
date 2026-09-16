---
type: llm
weight: 2
---

The first batch is sized for a human to finish in one sitting and then be re-sampled from, not to
be statistically representative.

Pass if the proposed initial batch is roughly 15-25 traces (anything from about 12 to 30 counts).

Fail if the answer proposes reviewing all 200, a fixed percentage that lands far outside that band,
or a handful of 3-5.
