# evals plugin — eval suite

Ablation evals for the whole `ai-evals-course/evals-skills` plugin (8 skills). Every case runs the
same prompt twice — with the plugin and without — so the headline number is the delta, not the pass
rate.

```sh
# full suite: 32 cases x 3 runs x 2 arms
claude plugin eval catalog/plugin-evals --ablation with-without --scaffold \
  --allow-tools Bash Write Edit --judge-model sonnet --no-publish

# cheap pilot before spending the full budget
claude plugin eval catalog/plugin-evals --case '14-*' --runs 1 --ablation with-without \
  --scaffold --judge-model sonnet --no-publish
```

`--scaffold` is required: ten cases build their fixture from `scaffold.sh` inside the run's temp
directory. Fixtures are deliberately not referenced out of this repo — an `add_dirs` path would put
the no-plugin arm one directory walk from `skills/` and the graders, and a baseline that has read
the skill is not a baseline.

`--judge-model sonnet` is required: the default haiku judge does not hold the scoping instructions
these rubrics rely on ("pass if X is absent from the final answer", "judge only the deliverable").

## What each case measures

| Case | Skill | The mistake it catches |
|---|---|---|
| 01-route-traces-in-hand | evals-start | Building evaluators before anyone has read a trace |
| 02-route-no-traces-yet | evals-start | Reaching for off-the-shelf metrics when there is no data yet |
| 03-audit-likert-holistic-judge | eval-audit | A 1-5 scale and one holistic "helpfulness" verdict |
| 04-audit-accuracy-under-imbalance | eval-audit | 91% accuracy hiding a judge that catches 1 failure in 10 |
| 05-audit-fewshot-leakage | eval-audit | Few-shot examples that are rows of the measured set |
| 06-audit-similarity-metric | eval-audit | ROUGE-L as a release gate, and a 4-point move read as a win |
| 07-audit-greenfield-no-evals | eval-audit | Judge and dashboard first, error analysis later |
| 08-judge-four-components | write-judge-prompt | Verdict before critique; missing Pass/Fail definitions |
| 09-judge-should-be-code | write-judge-prompt | An LLM judge for something a regex decides exactly |
| 10-judge-spec-failure | write-judge-prompt | Measuring a behaviour the system prompt never asked for |
| 11-judge-fewshot-source | write-judge-prompt | Prompt examples drawn from the evaluation set |
| 12-judge-holistic-trace | write-judge-prompt | One judge over the whole trace, scoring "overall quality" |
| 13-validate-agreement-metric | validate-evaluator | A single agreement figure; Kappa as the alignment metric |
| 14-validate-correction-invalid | validate-evaluator | Reporting a corrected rate from a judge no better than chance |
| 15-validate-interval-and-sample | validate-evaluator | A point estimate off 40 examples, no interval |
| 16-validate-test-set-once | validate-evaluator | Tuning against the held-out set until it passes |
| 17-validate-splits-and-labeller | validate-evaluator | Splitting labels that non-experts produced |
| 18-synth-dimensions-and-tuples | generate-synthetic-data | Twenty variations of the same happy path |
| 19-synth-arbitrary-dimensions | generate-synthetic-data | Dimensions the model never sees (browser, weekday) |
| 20-synth-wrong-tool | generate-synthetic-data | Synthetic data nobody on the team can judge |
| 21-rag-separate-stages | evaluate-rag | One end-to-end similarity score over two components |
| 22-rag-rerank-metrics | evaluate-rag | The same metric for first-pass retrieval and reranking |
| 23-rag-chunking-search | evaluate-rag | Picking a chunk size instead of measuring one |
| 24-rag-faithfulness-definition | evaluate-rag | Passing a correct fact the model supplied itself |
| 25-discovery-noninteractive-honesty | error-discovery | Narrating a human review session that never happened |
| 26-discovery-sampling-composition | error-discovery | A purely random or purely clustered first batch |
| 27-discovery-freetext-first | error-discovery | Shipping a failure-mode dropdown before the taxonomy exists |
| 28-discovery-premature-scan | error-discovery | A prevalence number built on one annotation |
| 29-review-interface-rendering | build-review-interface | Raw JSON and unrendered markdown in the review UI |
| 30-neg-foundation-benchmark | — | Over-firing on MMLU/HumanEval benchmarking |
| 31-neg-unit-test-request | — | Over-firing on pytest for a deterministic function |
| 32-neg-latency-regression | — | Over-firing on a p95 latency regression |

Cases 30-32 must NOT fire. Their `tool_used: Skill` grader carries `min: 0, max: 0, arm: both`, so
it is scored in both arms — unlike the positive cases, where the same grader is display-only and
never moves the delta.

## Grader conventions

- Outcome graders decide the score. `tool_used: Skill` in cases 01-29 is a trigger indicator only.
- `regex` graders are mechanical and weighted 0.5-3. None of them use `not_contains` over prose: a
  correct answer that names the anti-pattern in order to reject it would fail such a check.
- Rubrics state what passes and what fails, and say which part of the answer is being judged. The
  deliverable is graded, not the agent's narration.
- Fixture-grounded cases (03-07) include a grader that fails a generic answer that would read the
  same against any other codebase.

## Provenance

Plugin: https://github.com/ai-evals-course/evals-skills (v0.3.1, 8 skills, no licence file).
Installed as a plugin rather than copied into `lib/` would be the correct handling if the licence
mattered for redistribution — see REVIEW.md.

## Measured

Full run 2026-09-16, `--runs 3 --ablation with-without --judge-model sonnet -j 4`, 192 agent runs,
$44.09, 37 minutes. **The run is half-dead and its headline number must not be quoted.** From case
18 onward every agent run exited with `You've hit your org's monthly spend limit`, so cases 18-32
carry no data. The runner still reported `partial: false` and printed an overall 0.51 / Δ +0.11,
averaging 16 real cases with 15 dead ones.

Over the 16 cases that actually ran (case 10 was hit halfway and is excluded):

| | with plugin | without | Δ |
|---|---:|---:|---:|
| mean | 0.93 | 0.70 | **+0.22** |

13 of 16 gained, 1 flat, 2 lost. The largest deltas are the stance cases, not the knowledge ones:
greenfield build order +0.63, judge structure +0.57, agreement metric +0.56, accuracy under
imbalance +0.35.

Still unmeasured at `runs: 3`: every `generate-synthetic-data`, `evaluate-rag`, `error-discovery`
and `build-review-interface` case, and all three should-not-fire cases. Cases 25 and 30 were
piloted separately at `runs: 1` (Δ +0.18 and Δ −0.25 respectively — the latter is the negative
case correctly catching an over-trigger on an MMLU benchmarking question).

### How to tell a dead run from a real one

A spend-limit or rate-limit kill does not look like a failure in the summary. Check before reading
any score:

```sh
python3 - <<'EOF'
import json, glob
d = json.load(open(sorted(glob.glob('evals/results/*/aggregate-result.json'))[-1]))
runs = [r for c in d['cases'] for a in c['arms'].values() for r in a]
bad = [r for r in runs if r.get('error')]
print(f"{len(bad)}/{len(runs)} agent runs errored")
EOF
```

Two signatures to recognise: a positive case scoring exactly 0 in **both** arms, and a should-not-fire
case scoring exactly 0.25 in both arms — the latter is the `tool_used: Skill` grader with
`min: 0, max: 0` passing vacuously because the agent never ran and therefore never called anything.

### Calibration changes made from this run's traces

- `11-judge-fewshot-source/disqualification-is-explicit` demanded the rule *and* a named
  consequence; it failed 3/3 in both arms. A grader that never passes in either arm measures
  nothing. Relaxed to the rule alone.
- `12-judge-context-window` scored 0.95 in the baseline: what to feed a faithfulness judge is
  textbook RAG advice a capable model already knows. Replaced with `12-judge-holistic-trace`, which
  tests a refusal rather than a fact.
- The same reasoning retired the original `14-validate-bias-correction` during the pilot: the
  baseline derived Rogan-Gladen unaided and scored Δ 0.
