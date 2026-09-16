---
type: llm
weight: 3
---

Forty labelled examples is small for this purpose: the recommended working size is around 100 with
both classes represented, and below roughly 60 the resulting intervals get wide.

Pass if the answer flags the 40-example test set as too small and connects that specifically to the
width of the interval or the reliability of the corrected estimate.

Fail if the sample size is not questioned, or is waved through as adequate.
