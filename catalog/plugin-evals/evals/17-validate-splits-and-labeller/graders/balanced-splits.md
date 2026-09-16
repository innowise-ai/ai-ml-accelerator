---
type: llm
weight: 2
---

Both rates have to be measurable, so each split needs enough of both classes — which means
stratifying, and deliberately balancing even when real-world prevalence is skewed.

Pass if the answer says the splits must preserve or balance the Pass/Fail mix (stratified sampling,
or an explicit instruction to keep roughly equal numbers of each class), and ties that to being
able to measure the failure-side rate.

Fail if the split is described purely as a random division with no attention to class composition.
