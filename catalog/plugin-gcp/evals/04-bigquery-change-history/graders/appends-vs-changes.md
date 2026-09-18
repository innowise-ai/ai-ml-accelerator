---
type: llm
focus: last_message
---
The function name, the table option and the pseudo-column are checked separately. Judge here only whether the two functions are told apart correctly.

PASS if the answer makes clear that `APPENDS` covers appended rows only and needs no table option, while `CHANGES` covers inserts, updates and deletes and does require `enable_change_history`, and picks `CHANGES` for this use case.

FAIL if the two are conflated, if `APPENDS` is offered as sufficient for updates and deletes, or if the answer proposes a hand-rolled solution (an updated_at column, a full-table diff, `FOR SYSTEM_TIME AS OF`) as the primary mechanism.
