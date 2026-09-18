---
type: llm
focus: last_message
---
The individual commands are checked separately. Judge here only coverage and the no-Console constraint.

PASS if all five numbered steps are answered with runnable shell commands, and no step is answered by telling the user to open the Cloud Console, a web page or any graphical tool.

FAIL if any step is skipped, if any step falls back to "in the Console, go to...", or if a step is answered with prose where a command was asked for.
