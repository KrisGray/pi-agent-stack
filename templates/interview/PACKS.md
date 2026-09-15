# Interview Packs Index

The routing vocabulary. Do not route to a pack that is not listed here and has no file in
this directory.

**Ownership.** This file owns the pack table, boundary tests, and Q4 risk-seed cues,
and nothing else. `interview.md` owns the questions, the budget and the routing
procedure; `AI-INSTRUCTIONS.md` owns the playback format. Where this file and
`interview.md` appear to disagree about procedure, `interview.md` wins.

Each pack file owns its own `Compose with:` line. The *Composes with* column below mirrors
those lines — if the two ever drift, the pack file is right and this table is stale.

## Pack list

The *Usually* column is advisory, not a gate. It records which position a pack normally
takes when two are loaded; it does not restrict what can pair with what.

| Pack | Usually | Summary | Composes with |
|---|---|---|---|
| `script` | primary | Standalone script or small tool, run once by one person. | `cli-tool`, `batch-worker`, `data-pipeline` once it stops being one-off |
| `cli-tool` | primary | Command-line tools that are reused or distributed. | `script`, `infra-change` |
| `data-pipeline` | primary | Fetching, parsing and landing external data into a database. | `schema-change` |
| `batch-worker` | primary | Background workers, job processors, queue consumers. | `data-pipeline`, `schema-change` |
| `orm-model` | primary | Adding or changing ORM models, relationships or migrations. | `schema-change` |
| `schema-change` | secondary | Relational migration on a live database that already holds data. | any pack that alters database shape |
| `rest-api` | primary | HTTP API consumed by other code. | `schema-change`, `auth-permissions` |
| `website` | primary | Public-facing site, mostly unauthenticated content. | `schema-change` |
| `web-app` | primary | Authenticated multi-user app with roles and workflows. | `auth-permissions`, `schema-change` |
| `auth-permissions` | secondary | Roles, permissions and data isolation. | `web-app`, `rest-api`, `agent-framework`, `analytics-dashboard` |
| `analytics-dashboard` | primary | Dashboards and reporting over data that already exists. | `data-pipeline`, `schema-change` |
| `infra-change` | primary | Changes to IaC, environments or cloud services. | `schema-change`, `batch-worker` |
| `llm-integration` | primary | Wiring an app or service into LLM APIs. | `rest-api`, `web-app`, `website`, `data-pipeline` |
| `agent-framework` | primary | Agents and orchestrators that call tools, APIs or code. | `auth-permissions`, `infra-change`, `llm-integration` |
| `evaluation-harness` | primary | Suites for evaluating models or agents. | `data-pipeline` |

## Boundary tests

Several packs sit close enough together that the summaries above won't separate them from
a single answer. Each test below is decidable from core Q1 or one short follow-up — use
the test rather than guessing, and state the result as part of the routing announcement.

| Torn between | Ask | Routes to |
|---|---|---|
| `script` / `cli-tool` | Does anyone but you run it? | No → `script`. Yes → `cli-tool`. |
| `script` / `batch-worker` | Does something other than a person start it? | A person → `script`. A scheduler or queue → `batch-worker`. |
| `data-pipeline` / `batch-worker` | What arrives first — data, or a job? | Data, on a schedule → `data-pipeline`. Jobs, on a queue → `batch-worker`. |
| `website` / `web-app` | Does a user log in? | No → `website`. Yes → `web-app`. |
| `orm-model` / `schema-change` | Does the database shape change? | No → `orm-model` alone. Yes → both. |
| `llm-integration` / `agent-framework` | Does the model choose what to call next? | No, the flow is fixed → `llm-integration`. Yes → `agent-framework`. |
| `analytics-dashboard` / `data-pipeline` | Is the data already landed? | Yes → `analytics-dashboard`. No → `data-pipeline` first, and say so. |

A wrong answer to one of these costs three to five questions, which is why they are worth
one short follow-up. If the user's answer straddles a boundary, take the pack that covers
the side the user knows less well — hesitation on the boundary test is the signal, not
some later question. These clarifications are follow-ups to core Q1 and count toward the
same 12-question budget.

## Q4 risk-seed cues by pack

Use these cues when compiling core Q4's difficulty shortlist. Fill in order: one cue per
loaded pack first, then charter one-way-door cues, then inventory/drift and dependency
cues. Cues in each row are priority-ordered; when a pack contributes one slot, take the
first cue.

| Pack | Default risk-seed cues |
|---|---|
| `script` | Re-run safety unclear; one-off quietly becoming shared/scheduled infrastructure |
| `cli-tool` | Distribution/runtime drift; compatibility promise stronger than planned |
| `data-pipeline` | Source format changes without notice; dedupe identity/idempotency gaps |
| `batch-worker` | Delivery semantics and idempotency mismatch; retries causing hidden ops load |
| `orm-model` | Source-of-truth inversion; key/cascade integrity edge-cases; outside-ORM consumers |
| `schema-change` | Lock window too small for row volume; dual-shape deploy hazards; backfill validity |
| `rest-api` | Existing clients break on change; unversioned additive-only constraint; write retries duplicate effects |
| `website` | URL contract breakage; editor workflow mismatch; cache invalidation blind spots |
| `web-app` | Role/journey ambiguity; auth/session mismatch; state consistency surprises |
| `auth-permissions` | Weak tenant/data isolation; audit obligations wider than assumed |
| `analytics-dashboard` | Freshness expectation mismatch; heavy-query performance or cost cliffs |
| `infra-change` | IaC drift/manual changes; rollback path weaker than expected; observability gaps |
| `llm-integration` | Sensitive context leakage; latency/fallback policy gaps; behaviour unobservable |
| `agent-framework` | Guardrail boundaries too weak; tool-discovery drift; state persistence ambiguity |
| `evaluation-harness` | Metrics not decision-useful; reproducibility gaps; dataset licensing/sensitivity risk |

## Routing

Procedure lives in `interview.md`. In outline: ask core Q1, say the classification out
loud in one line, then load **at most two packs** from the table above — three questions
from the first, two from the second. A project needing three packs is a project that
needs splitting.
