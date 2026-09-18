---
type: llm
focus: last_message
---
That the read pool instance type, the edition and the autoscaling flags appear is checked separately. Judge here only whether the constraints are stated correctly.

PASS if the answer gets the limits right: up to 20 read pool nodes for PostgreSQL, and the combined total of standalone read replicas and read pool nodes per primary capped at 20.

FAIL if it invents a different ceiling, or states no limit at all.
