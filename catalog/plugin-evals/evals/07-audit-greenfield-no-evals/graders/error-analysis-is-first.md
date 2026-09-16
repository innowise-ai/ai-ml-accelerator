---
type: llm
weight: 3
---

The fixture says 6k request/response pairs are already in the log. That is the material for error
analysis, and error analysis is what has to happen first.

Pass if the first item in the recommended build order is reviewing a sample of those logged traces
by hand to discover failure modes.

Fail if the first item is anything else — defining metrics, picking a framework or vendor, writing
a judge, assembling a golden test set, or building a dashboard — even when trace review appears
later in the list.
