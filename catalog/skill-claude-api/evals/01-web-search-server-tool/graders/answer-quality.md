---
type: llm
focus: last_message
---
Evaluate the final answer: a minimal Python script on the official Anthropic SDK with server-side web search.

PASS if all of the conditions hold:
- the `anthropic` package is used (the `Anthropic()` client and `client.messages.create(...)` or stream);
- the model is given as the string `claude-opus-5`;
- `tools` contains a server tool with `type: "web_search_20260209"` and `max_uses: 3`;
- the answer does not recommend `web_search_20250305` as the current type for Opus 5 (mentioning it as outdated is fine);
- there is no `budget_tokens` in the thinking parameters.

FAIL if the code uses `requests`/`httpx` instead of the SDK, the model has a dated suffix, the old web search type is presented as the current one, or there is no code.
