# Pack: evaluation harness

Compose with: `data-pipeline` when the harness depends on curated or ingested
datasets.

Frameworks, suites and tools for evaluating models or agents — coding tasks, QA,
benchmarks, regression suites.

Assumes the core bank has run. Ordered by cost-of-missing; drop from the bottom.

1. What kinds of tasks or behaviours are being evaluated — coding, reasoning, QA, chat,
   infrastructure operations? [default: coding and reasoning tasks]

2. What metrics matter — pass@k, accuracy, time to solution, human rating scales, or
   something else? [default: task success/failure plus basic timing]

3. Where do tasks and datasets come from?
   [default: internal tasks and data]
   - → *follow-up:* what licensing or sensitivity constraints apply?
     [default: no external licensing constraints]

4. How must evaluations be run and reproduced — seeds, config snapshots, pinned model
   versions, environment capture? [default: reproducible enough for internal comparison]

5. Who consumes the results — you, a team, external stakeholders?
   [default: you]
   - → *follow-up:* what decisions do the results inform?
     [default: choosing models and configs]

## Notes for the PRD

- Q2 answers define what "good enough" means; they should be restated as requirements in
  the scope list, not left implicit.
- Q3 answers that mention public or licensed datasets are a supply-chain concern under
  the same rule as optional Q11; record them explicitly.
- A strong reproducibility requirement in Q4 (e.g. for scientific or compliance reasons)
  implies extra scope: environment capture, config versioning, and change tracking.
