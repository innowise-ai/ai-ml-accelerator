---
type: regex
target: last_message
pattern: 'TPR|true positive rate|sensitivit'
flags: 'i'
weight: 0.5
---

Mechanical secondary check that the per-class Pass rate is named. Low weight: the scored signal is
the outcome grader above, not the vocabulary.
