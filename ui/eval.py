#!/usr/bin/env python3
# eval.py — one command per entry: build the plugin into catalog/, create cases, run claude plugin eval
#
#   python3 ui/eval.py lib/skills/docx            build catalog/skill-docx/ (a copy of the skill, plugin.json, a REVIEW.md template if there is none);
#                                                 if there are cases — run them and pull the result into the catalog
#   python3 ui/eval.py lib/plugins/docs.json      the same for a bundle
#   python3 ui/eval.py lib/mcp/context7.json --init            the stock claude plugin eval init (interview) in the entry folder
#   python3 ui/eval.py lib/mcp/context7.json --init --bare 01-case     an empty case template instead of the interview
#   python3 ui/eval.py lib/skills/docx --runs 3 --case 01-*    the remaining flags go to claude plugin eval
#
# The entry folder catalog/<kind>-<name> is derived from the path. For MCP the wrapper adds
# --allow-real-servers and --allow-tools itself; without them the plugin's server does not start in eval.

import json, math, subprocess, sys
from lib import (REPO, UI, load_config, load_library, load_compositions, composition_of, comp_members, parse_lib_path, parse_review,
                 entry_dir, materialize, review_template, eval_info, eval_flags, read_text, rel)

args = sys.argv[1:]
p = parse_lib_path(args[0]) if args else None
if not p:
    print('usage: python3 ui/eval.py <path> [--init [--bare <case>]] [claude plugin eval flags]\n  path: lib/skills/docx · lib/agents/x.md · lib/mcp/x.json · lib/hooks/x · lib/plugins/x.json', file=sys.stderr)
    sys.exit(2)
arg, rest = args[0], args[1:]
id = f"{p['kind']}-{p['name']}"
INIT = '--init' in rest
bare_at = rest.index('--bare') if '--bare' in rest else -1
BARE = rest[bare_at + 1] if 0 <= bare_at < len(rest) - 1 else None
passthrough = [a for i, a in enumerate(rest) if a not in ('--init', '--bare') and not (bare_at >= 0 and i == bare_at + 1)]

cfg = load_config()
lib, comps = load_library(), load_compositions()
comp = composition_of(p['kind'], p['name'], comps)
if not comp: print(f"no lib/plugins/{p['name']}.json — describe the contents: {{\"skills\": [...], \"agents\": [...], \"mcp\": [...], \"hooks\": [...]}}", file=sys.stderr); sys.exit(1)
members = comp_members(comp, lib)
missing = [m for m in members if m.get('missing')]
if not members: print(f'{id}: contents are empty — building an empty placeholder', file=sys.stderr)
names = lambda ms: ', '.join(f"{m['kind']}/{m['name']}" for m in ms)
if missing: print(f"not in the library: {names(missing)} — put it into lib/skills/ lib/agents/ lib/mcp/ lib/hooks/", file=sys.stderr); sys.exit(1)

# 1. the entry folder as a full plugin
d = entry_dir(id)
fresh = not d.exists()
d.mkdir(parents=True, exist_ok=True)
e = dict(id=id, kind=p['kind'], name=p['name'], dir=d, where=rel(d), members=members, review=parse_review(read_text(d / 'REVIEW.md')))
changed = materialize(e, cfg)
note = 'created' if fresh else 'rebuilt' if changed else 'up to date'
if not (d / 'REVIEW.md').exists(): (d / 'REVIEW.md').write_text(review_template(e), 'utf-8'); note += ', REVIEW.md — template (draft)'
print(f"{e['where']}/: {note}; contents: {names(members)}")

# 2. cases: the stock claude plugin eval init in the entry folder
if INIT:
    r = subprocess.run(['claude', 'plugin', 'eval', 'init', *(['--bare', BARE] if BARE else [])], cwd=d)
    sys.exit(r.returncode)
info = eval_info(d)
if not info['cases']:
    print(f'no cases. Create them: python3 ui/eval.py {arg} --init  (interview)  or  --init --bare 01-<case>  (empty template)\ntemplate: template/evals/  example: catalog/mcp-context7/evals/')
    sys.exit(0)

# 3. run
cmd = ['plugin', 'eval', e['where'], '--no-publish', '--trust-plugin', *eval_flags(e), '--json', *passthrough]
print('claude ' + ' '.join(cmd))
r = subprocess.run(['claude', *cmd], cwd=REPO, stdout=subprocess.PIPE, text=True)
out = r.stdout or ''
try: j = json.loads(out[out.index('{'):])
except Exception: j = None; print(out[-2000:], file=sys.stderr)
if j:
    A = j.get('aggregates') or {}
    def f(v):
        if v is None: return '–'
        x = math.floor(v * 100 + 0.5) / 100
        return str(int(x)) if x.is_integer() else repr(x)
    sign = lambda v: '+' if v is not None and v >= 0 else ''
    delta = f", Δ {sign(A.get('meanDelta'))}{f(A['meanDelta'])} vs the run without it" if A.get('meanDelta') is not None else ''
    print(f"\n{id}: with the plugin {f(A.get('overallScore'))}{delta} · {A.get('casesTotal', '?')} cases · ${j.get('costUsd') or 0:.2f} · Claude Code {j.get('claudeVersion') or '?'}{' · partial run' if j.get('partial') else ''}")
    for c in j.get('cases') or []:
        a = c.get('aggregates') or {}
        print(f"  {c['name'].ljust(36)} with {f(a.get('score'))}  without {f(a.get('scoreWithout'))}  Δ {sign(a.get('delta'))}{f(a.get('delta'))}")
    latest = eval_info(d)['latest']
    if latest and latest['report']: print(f"  report: {latest['report']}")
# 4. the catalog picks up the result
subprocess.run([sys.executable, str(UI / 'build.py')])
sys.exit(r.returncode if r.returncode >= 0 else 1)
