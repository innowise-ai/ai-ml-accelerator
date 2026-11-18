---
model: sonnet
max_turns: 5
timeout_seconds: 120
allowed_tools: [Skill]
runs: 3
---
Review this Express.js login handler for SQL injection.

```js
const express = require("express");
const session = require("express-session");
const bcrypt = require("bcrypt");
const { Pool } = require("pg");

const app = express();
const pool = new Pool();
app.use(express.json());
app.use(session({ secret: process.env.SESSION_SECRET, resave: false, saveUninitialized: false }));

app.post("/login", async (req, res) => {
  const { email, password } = req.body;
  const { rows } = await pool.query(`SELECT id, pw_hash FROM users WHERE email = '${email}'`);
  if (!rows.length || !(await bcrypt.compare(password, rows[0].pw_hash))) return res.status(401).end();
  req.session.userId = rows[0].id;
  res.json({ ok: true });
});

app.listen(3000);
```
