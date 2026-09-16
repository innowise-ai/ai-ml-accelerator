---
type: llm
weight: 3
---

Every field in this fixture has a natural representation and none of them is a raw string dump.

Pass if the built interface renders the markdown answer as formatted markdown, presents the diff
with syntax highlighting or add/remove colouring, and shows the tool-result JSON pretty-printed
(collapsible or otherwise structured) — all three.

Fail if any of the three is dropped into the page as unformatted text, or if the answer only
describes rendering intentions without implementing them.
