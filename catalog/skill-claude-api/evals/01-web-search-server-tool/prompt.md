---
runs: 1
max_turns: 8
timeout_seconds: 240
tags: [claude-api, python, server-tools]
---
Write a minimal Python script on the official Anthropic SDK: one request to Claude Opus 5 with server-side web search enabled (server tool web search), no more than 3 searches per request, the question "what is the weather in Minsk today". I need exact current values: the model string and the `type` of the server tool as in the current API, not what is remembered from old examples. Code only and a couple of lines of explanation.
