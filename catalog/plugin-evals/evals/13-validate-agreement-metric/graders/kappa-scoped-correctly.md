---
type: llm
weight: 2
---

Cohen's Kappa measures agreement between two annotators of equal standing. Human labels here are
the ground truth, not a second opinion, so Kappa is the wrong instrument for judge validation.

Pass if Cohen's Kappa is either not mentioned at all, or is mentioned only as something for
human-versus-human annotator agreement and explicitly not as the judge alignment metric.

Fail if Kappa is recommended as the metric for measuring the judge against human labels.
