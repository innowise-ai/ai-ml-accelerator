---
type: llm
weight: 3
---

A RAG pipeline fails in two distinct places. A single end-to-end number cannot distinguish "the
right chunk was never retrieved" from "the right chunk was retrieved and misread", and those have
opposite fixes.

Pass if the answer insists on measuring retrieval and generation separately, and says to determine
which component is responsible before choosing metrics — by inspecting what was retrieved against
what the answer needed.

Fail if a single end-to-end metric is proposed, however sophisticated, or if the two components are
never distinguished.
