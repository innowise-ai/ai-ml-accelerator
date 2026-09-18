---
type: llm
focus: last_message
---
The SQL shape is checked separately. Judge here only the "keep running in production for months" half of the question.

PASS if both conditions hold:
- a continuous query run under a user account stops after at most two days, so a service account is required to run for longer (up to 150 days);
- running continuous queries requires an Enterprise or Enterprise Plus edition reservation with a `CONTINUOUS` job type assignment.

FAIL if either is missing, if on-demand/ad-hoc pricing is presented as sufficient, or if the answer claims the query simply runs indefinitely with no further setup.
