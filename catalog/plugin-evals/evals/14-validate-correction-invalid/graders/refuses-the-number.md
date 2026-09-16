---
type: llm
weight: 3
---

The correction divides by (TPR + TNR - 1), which is 0.03 here. At that denominator the estimate is
dominated by sampling error in the two rates themselves, and the arithmetic result falls outside
[0, 1] before clipping rescues it into something that looks like an answer.

Pass if the answer declines to supply a corrected success rate for the quarterly report, and says
the correction is not valid / not meaningful with rates this close to random.

Fail if any corrected figure is handed over as the number to report — including 100%, a clipped
value, or a hedged "approximately" version.
