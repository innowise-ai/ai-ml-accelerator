---
type: llm
weight: 3
---

This is a pure function with a small, enumerable edge-case surface.

Pass if the reply contains runnable pytest test functions covering at least four distinct edge
cases from: empty input, a single span, spans that merely touch at a boundary, spans that do not
overlap, a span fully contained in another, unsorted input, and duplicate spans.

Fail if fewer than four distinct edge cases are covered, if the tests are pseudocode, or if the
tests would not run against the function as written.
