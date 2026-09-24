---
type: regex
target: last_message
pattern: '--ssl-mode[= ]\s*ENCRYPTED_ONLY'
flags: i
---
"Every connection must be encrypted" is set by `--ssl-mode=ENCRYPTED_ONLY`. From memory the model reaches for the deprecated `--require-ssl`, or omits the flag altogether and only mentions the Cloud SQL Auth Proxy.
