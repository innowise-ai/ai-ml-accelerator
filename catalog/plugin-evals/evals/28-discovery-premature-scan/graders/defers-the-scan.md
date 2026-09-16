---
type: llm
weight: 3
---

A single note is one reviewer's reaction to one record. Scanning 200 traces against it encodes that
one reaction as the definition of the failure mode, and every later count inherits it.

Pass if the answer declines to run the corpus-wide scan now and explains that one annotation is too
weak a signal to define the mode, asking for more annotated records first.

Fail if the scan is run and results are reported, or if the answer agrees to scan while merely
noting the result may be rough.
