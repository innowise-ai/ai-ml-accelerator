---
type: llm
weight: 3
---

The replacement metrics are true positive rate and true negative rate, measured separately, because
they map directly onto the bias-correction formula used later.

Pass if the answer requires the judge's agreement to be reported as two separate rates — one over
the human-Pass cases and one over the human-Fail cases — named as TPR/TNR, sensitivity/specificity,
or spelled out as "of the failures the humans marked, how many did the judge catch".

Fail if only a single aggregate agreement figure is proposed, or if precision/recall/F1 is offered
as the replacement without the per-class Pass and Fail rates.
