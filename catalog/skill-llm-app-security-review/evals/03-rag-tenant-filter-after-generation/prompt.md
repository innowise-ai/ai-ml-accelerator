---
model: sonnet
max_turns: 5
timeout_seconds: 180
allowed_tools: [Skill]
runs: 3
---
Threat-model this multi-tenant document Q&A endpoint.

```python
from fastapi import FastAPI, UploadFile, Depends
from fastapi.responses import HTMLResponse
from markdown import markdown
from .auth import current_user
from .store import index, embed, extract_text
from .llm import complete

app = FastAPI()

@app.post("/upload")
async def upload(f: UploadFile, user=Depends(current_user)):
    text = extract_text(await f.read())
    index.add(embed(text), {"tenant": user.tenant_id, "text": text, "name": f.filename})
    return {"ok": True}

@app.get("/ask", response_class=HTMLResponse)
async def ask(q: str, user=Depends(current_user)):
    hits = index.search(embed(q), top_k=8)
    context = "\n---\n".join(h.meta["text"] for h in hits)
    answer = complete(f"Answer using these documents:\n{context}\n\nQuestion: {q}", max_tokens=800)
    sources = [h.meta["name"] for h in hits if h.meta["tenant"] == user.tenant_id]
    return f"<div class='answer'>{markdown(answer)}</div><ul>{''.join(f'<li>{s}</li>' for s in sources)}</ul>"
```
