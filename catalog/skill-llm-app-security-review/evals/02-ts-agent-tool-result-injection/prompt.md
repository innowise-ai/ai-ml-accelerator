---
model: sonnet
max_turns: 5
timeout_seconds: 180
allowed_tools: [Skill]
runs: 3
---
Our support staff will use this agent to triage tickets. Is it safe to roll out?

```ts
import Anthropic from "@anthropic-ai/sdk";
import { db, payments, mailer } from "./services";
import { SYSTEM, TOOL_SCHEMAS } from "./config";

const client = new Anthropic();

const tools: Record<string, (args: any) => Promise<unknown>> = {
  fetchTicket: async ({ ticketId }) => db.tickets.get(ticketId), // ticket body is written by customers
  deleteUser: async ({ userId }) => db.users.delete(userId),
  refundOrder: async ({ orderId, amount }) => payments.refund(orderId, amount),
  sendEmail: async ({ to, subject, body }) => mailer.send(to, subject, body),
};

export async function triage(staffMessage: string) {
  const messages: Anthropic.MessageParam[] = [{ role: "user", content: staffMessage }];
  for (let step = 0; step < 20; step++) {
    const res = await client.messages.create({
      model: "claude-sonnet-5-5",
      max_tokens: 1024,
      system: SYSTEM,
      tools: TOOL_SCHEMAS,
      messages,
    });
    const calls = res.content.filter((b): b is Anthropic.ToolUseBlock => b.type === "tool_use");
    if (calls.length === 0) return res.content;
    const results: Anthropic.ToolResultBlockParam[] = [];
    for (const call of calls) {
      const output = await tools[call.name](call.input);
      results.push({ type: "tool_result", tool_use_id: call.id, content: JSON.stringify(output) });
    }
    messages.push({ role: "assistant", content: res.content });
    messages.push({ role: "user", content: results });
  }
  throw new Error("step limit reached");
}
```
