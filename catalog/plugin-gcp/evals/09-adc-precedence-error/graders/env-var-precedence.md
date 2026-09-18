---
type: llm
focus: last_message
---
PASS if the answer identifies that `GOOGLE_APPLICATION_CREDENTIALS` is checked first in the ADC lookup order, and that when it points to a missing or invalid file, ADC fails immediately instead of falling back to the local ADC file or the metadata server.

FAIL if the answer never mentions the stale environment variable as a likely cause, or claims ADC silently skips an invalid `GOOGLE_APPLICATION_CREDENTIALS` and falls back on its own.
