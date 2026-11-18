---
type: llm
focus: last_message
---
Check: the answer has a section or list of things it could not judge from the code it was given, and that list names at least one specific item tied to this code (for example a module that is imported but not shown, how an input is obtained or authenticated, database permissions, deployment, vendor settings), not only generic advice.
A single closing sentence counts if it names specific unreviewed parts (e.g. "I haven't checked the auth layer or git history"). An offer to do more work ("I can draft a hardened version") does not count.
PASS if such a specific list or statement is present. FAIL otherwise, and quote what the answer has instead.
