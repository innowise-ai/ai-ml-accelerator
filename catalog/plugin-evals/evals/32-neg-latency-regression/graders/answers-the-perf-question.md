---
type: llm
weight: 3
---

The available fields make this a straightforward segmentation problem.

Pass if the answer proposes splitting the logs by route (and ideally model), comparing the
pre-deploy and post-deploy windows within each segment at percentile level, and checking whether
the token distributions or the traffic mix changed — enough for the user to find the responsible
route from the data they have.

Fail if the answer offers only generic performance advice with no use of the named fields, or
redirects away from the question.
