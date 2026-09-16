---
type: llm
weight: 3
---

Repeatedly measuring on the held-out set and changing the judge in response is how a test set stops
being held out. Whatever number it eventually reports is optimistic and unverifiable.

Pass if the answer rejects the proposed loop and states that iterating against the test set
invalidates it as an unbiased estimate.

Fail if the plan is endorsed, if the only objection is that 0.90 is ambitious, or if the answer
helps optimise the loop without challenging it.
