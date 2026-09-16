---
type: llm
weight: 2
---

The system prompt is byte-identical in all 24 records. Re-reading it 24 times costs attention and
teaches nothing, but hiding it entirely removes context the reviewer may need.

Pass if the repeated system prompt is collapsed by default behind a toggle, details element, or
equivalent, and remains expandable.

Fail if it is rendered in full on every record, or removed from the interface altogether.
