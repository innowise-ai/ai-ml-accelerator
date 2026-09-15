---
type: llm
focus: last_message
---
Evaluate the final answer to the question of how, in the current Vercel AI SDK, to limit the number of steps of the tool-calling loop in `generateText`.

PASS if all of the conditions hold:
- the answer names the `isStepCount` helper and shows it in the `stopWhen` parameter;
- the example contains an import from the `ai` package (for example, `import { generateText, isStepCount } from 'ai'`);
- the answer does not present `maxSteps` as the current way (mentioning it as outdated is fine).

FAIL if the answer recommends `maxSteps` as the current way, names the helper differently (for example, only `stepCountIs`) or contains no code example.
