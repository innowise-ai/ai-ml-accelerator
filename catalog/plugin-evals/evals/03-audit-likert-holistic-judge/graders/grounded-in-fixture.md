---
type: llm
weight: 2
---

Running an audit as a checklist without reading the artifacts is the named anti-pattern. The
findings have to come from these files.

Pass if the answer references concrete specifics of the fixture — for example the 1-5 wording in
the judge prompt, the mean-of-scores aggregation in `run_eval.py`, the five traces in
`traces.jsonl`, or the weekly team-channel process in the README — rather than describing eval
problems in the abstract.

Fail if the findings would read identically against any other codebase, with no detail that could
only come from these files.
