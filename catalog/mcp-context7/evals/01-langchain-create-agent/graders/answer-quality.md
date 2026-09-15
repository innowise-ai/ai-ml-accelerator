---
type: llm
focus: last_message
---
Evaluate the final answer to the request to build a minimal agent with tools and SummarizationMiddleware on LangChain 1.x (Python).

PASS if all of the conditions hold:
- the main example uses `create_agent` from `langchain.agents`, the `get_weather` tool is passed in `tools=[...]`, the system prompt is set via `system_prompt=`;
- `SummarizationMiddleware` is imported from `langchain.agents.middleware` and passed in `middleware=[...]`;
- the threshold and the amount of history kept are set with current parameters of the form `trigger=("tokens", 4000)` and `keep=("messages", 20)`;
- there is a brief explanation of the imports.

FAIL if the outdated `max_tokens_before_summary=` or `messages_to_keep=` are used as the current middleware parameters, if the example is built on `create_react_agent`/`AgentExecutor`/`initialize_agent`, or the code is missing.
