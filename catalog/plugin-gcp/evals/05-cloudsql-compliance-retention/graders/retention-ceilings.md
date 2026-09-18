---
type: llm
focus: last_message
---
The edition, the PITR flag, the Backup and DR Service and the immutability features are each checked separately. Judge here only whether the numeric ceilings are right.

PASS if both conditions hold:
- PITR retention is given as up to 7 days on Enterprise and up to 35 days on Enterprise Plus, so the 30-day requirement forces Enterprise Plus;
- enhanced backups are given as retaining up to 10 years against roughly 1 year for standard backups, so three years is inside the enhanced ceiling and outside the standard one.

FAIL if either pair of numbers is wrong or missing, or if the answer claims standard instance-level backups can already hold three years immutably.
