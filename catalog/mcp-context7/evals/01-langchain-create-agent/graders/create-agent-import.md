---
type: regex
target: last_message
pattern: 'from\s+langchain\.agents\s+import[\s\S]{0,120}?create_agent'
flags: i
---
In LangChain v1 the agent is built by the `create_agent` function from `langchain.agents` (and not by `create_react_agent` from `langgraph.prebuilt`, and not by `AgentExecutor`).
