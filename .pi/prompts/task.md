---
description: Implement ONE task from a spec in a strict TDD cycle, delegated to the worker persona (execution mode).
argument-hint: "<spec-path> <task-id>"
---
You are the ORCHESTRATOR for a SINGLE task in EXECUTION mode. You do not write the
implementation yourself: the `worker` persona implements, you brief it and verify its
report. Do not redesign the spec, do not expand scope, do not start the next task.

Spec file: $1
Task to implement: $2
(If only one argument was given, treat the whole of it as the spec path and ask me
which task id to implement.)

1. PREPARE.
   Read the spec file and the task. Confirm a clean tree and that you are on a
   branch named `task-<id>` (ask me which base branch if unclear). Extract the
   task's Verify line, Files list, Acceptance, and the spec's Boundaries — they
   are the worker's contract.

2. DELEGATE — spawn the `worker` persona (subagent tool, agent "worker") with a
   self-contained brief containing:
   - the spec path and task id, plus the task text: Verify line, Files list,
     Acceptance, and the spec's Always / Ask first / Never boundaries;
   - the mode rules:
     1. RED — turn the Verify line into a real test in the real test file. Run it.
        Confirm it FAILS for the right reason (behavior missing, not a typo or
        import error). Do not proceed on a test that passes immediately. For
        DB-touching work: write an integration test against the ephemeral test
        database and include the migration; the test must fail before the DDL
        exists.
     2. GREEN — the least code that makes the failing test pass. Run the FULL
        suite, not just the new test. Do not advance while anything is red.
     3. REFACTOR — clean up while staying green. Re-run the suite after.
     4. Do NOT commit. Do NOT start the next task. If implementing reveals a
        flaw in the spec, STOP and report it — the spec is the living source of
        truth and is fixed, never papered over in code.
   - the required report format: files changed (checked against the Files list),
     the verbatim RED evidence, the final full-suite output, lint/typecheck
     results, and a proposed conventional commit message
     `<type>(<scope>): <summary> (Task <id>)`.

3. VERIFY the report yourself. Run the task's Verify line and the full suite once
   (commands only). Check `git status` and `git diff --stat` against what the
   worker reported. If anything disagrees, surface the discrepancy — do not
   smooth it over.

4. STOP and report to me: the worker's findings, your verification results, and
   the proposed commit message. I review and commit; a fresh session starts the
   next task.

If the `worker` persona cannot be spawned (tool or persona missing), STOP and tell
me. Never silently implement the task yourself — that substitution is exactly what
this template exists to prevent.
