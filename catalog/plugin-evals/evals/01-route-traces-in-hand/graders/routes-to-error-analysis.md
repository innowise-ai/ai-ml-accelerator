---
type: llm
weight: 3
---

The user has traces and no failure taxonomy. The only correct first step is manual error analysis
over those traces.

Pass if the first concrete step in the answer is reviewing/annotating a sample of the existing 800
traces to discover failure modes — described as error analysis, trace review, open coding, or
equivalent, whatever it is called.

Fail if the first step is anything else: defining metrics, choosing a framework, writing an LLM
judge, building a dashboard, collecting more data, or a generic "align on what good looks like"
workshop with no trace reading in it.
