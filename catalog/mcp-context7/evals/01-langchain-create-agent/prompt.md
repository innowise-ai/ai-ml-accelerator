---
runs: 1
max_turns: 8
timeout_seconds: 180
tags: [docs, langchain, python]
---
Build a minimal agent with tools on LangChain 1.x (Python): one `get_weather(city)` tool, a system prompt, and hook up the built-in `SummarizationMiddleware` so that the history is compressed once it accumulates 4000 tokens, while the last 20 messages stay as they are. I need the exact names of the middleware constructor parameters from the current documentation, not the outdated ones. Show the code with imports and briefly explain what is imported from where.
