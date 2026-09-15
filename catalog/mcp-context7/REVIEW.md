---
verdict: must-have
rating: 5
security: 4
economy: +4%
full-body: 1.2k
---
## Summary
Pulls up the current documentation of libraries. Just RAG over current, continuously updated documentation. Almost always pays off.

## Examples
- We want to build an agent on LangGraph => with it, takes the modern create_agent abstraction from langchain v1 instead of a tool loop from scratch
- Updated the Vercel AI SDK, `maxSteps` is gone => without it, writes `stepCountIs` from v5 from memory, with it, takes the current `isStepCount`

## Notes
One of the most popular and convenient MCPs;
The answer averages 3.5k tokens (on average 3-5 per session)
Fires almost always (for me ~80% of sessions)
Safe; only the library name and the topic of the request go out, no code goes out
