#!/usr/bin/env bash
set -euo pipefail

mkdir -p evals

cat >evals/eval_config.yaml <<'EOF'
suite: incident-summariser
primary_metric: rouge_l
secondary_metrics:
  - bert_score_f1
  - answer_length_ratio
references: evals/reference_summaries.jsonl
gate:
  block_release_if: rouge_l < 0.38
schedule: weekly
EOF

cat >evals/reference_summaries.jsonl <<'EOF'
{"incident": "INC-2201", "reference": "Checkout latency rose after the 14:10 deploy; rolled back at 14:52; root cause was an unbounded retry loop in the payments adapter."}
{"incident": "INC-2207", "reference": "Search returned stale results for 40 minutes because the index refresh job silently failed; restarted manually."}
{"incident": "INC-2214", "reference": "Auth outage for EU customers caused by an expired intermediate certificate; renewed and automated the renewal."}
EOF

cat >evals/trend.md <<'EOF'
# Weekly quality trend

| Week | ROUGE-L | BERTScore F1 |
|---|---|---|
| w31 | 0.36 | 0.71 |
| w32 | 0.37 | 0.72 |
| w33 | 0.41 | 0.74 |

w33 shipped the new summariser prompt. ROUGE-L up 4 points, so we called it a win
and moved on.
EOF
