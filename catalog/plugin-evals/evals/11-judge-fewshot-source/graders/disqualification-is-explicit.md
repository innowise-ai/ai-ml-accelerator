---
type: llm
weight: 3
---

The operative rule is that using a trace as a few-shot example removes it from the measured sets.
Measured 2026-09-16: an earlier version of this rubric demanded the rule AND a named consequence in
the same breath and failed 3/3 in both arms — nobody phrases it that way. Only the rule is required
here; the consequence is a bonus, not a condition.

Pass if the answer makes clear that traces used as few-shot examples in the judge prompt must not
also be scored when measuring the judge — stated as a rule, as a property of the split, or as an
instruction to keep the sets disjoint.

Fail if the answer never establishes that separation, or leaves it possible to read that the same
traces serve both roles.
