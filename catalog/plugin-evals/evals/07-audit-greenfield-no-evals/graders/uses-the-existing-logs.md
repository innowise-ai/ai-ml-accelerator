---
type: llm
weight: 2
---

A team with 6k real traces does not need synthetic data, and does not need to wait for anything.

Pass if the answer directs the user to sample from the traces they already have, rather than
proposing to generate synthetic inputs first or to start collecting data.

Fail if synthetic generation is proposed as the starting point, or if the answer does not notice
that production traffic already exists.
