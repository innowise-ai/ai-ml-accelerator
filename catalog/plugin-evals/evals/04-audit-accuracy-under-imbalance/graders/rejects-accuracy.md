---
type: llm
weight: 3
---

`metrics.py` reports accuracy and percent agreement. With 90 Pass and 10 Fail labels, a judge that
answered "Pass" every time would score 90%, so the headline number carries almost no information.

Pass if the answer states that raw accuracy / percent agreement is the wrong metric here AND ties
that to the class imbalance in the labelled data — for example by noting that an always-Pass judge
would score about 90% on this set.

Fail if accuracy is accepted as a reasonable headline, if the only criticism is that the sample is
small, or if the imbalance is never connected to why the number misleads.
