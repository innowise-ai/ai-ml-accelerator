---
type: llm
weight: 3
---

A single agreement figure hides which direction the judge errs in. The two rates that matter are
computed separately over the human-Pass rows and the human-Fail rows.

Pass if the answer requires reporting two separate per-class rates — true positive rate and true
negative rate, sensitivity and specificity, or spelled out as "of what humans called Fail, how many
did the judge call Fail" plus the Pass equivalent.

Fail if a single aggregate figure is endorsed, or if the proposed replacement is precision/recall/F1
without the per-class Pass and Fail agreement rates.
