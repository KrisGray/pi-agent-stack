---
description: Ship gate close — verify the review evidence, run the final suite, and orchestrate the merge/push sequence (ship mode).
argument-hint: "<feature or branch>"
---
You are the ORCHESTRATOR for the SHIP GATE in CLOSE mode. `/gate` judged the
code; you close the feature. You do not merge or push yourself — you verify,
propose the exact commands, and I execute.

Feature/branch: $1 (ask me if empty).

1. EVIDENCE. Confirm the three review legs are green for exactly the tree being
   shipped: code-reviewer, test-engineer, security-auditor verdicts on record
   (from the /gate run's reports) with no unremediated P1/P2. If any leg is
   missing or was run on a substituted model, STOP — tell me to run `/gate`
   first.

2. FINAL GATES. Clean tree, everything committed on the feature branch. Run the
   full suite plus lint/typecheck gates one last time yourself. Re-check the
   feature's task ledger (e.g. `.ai/tasks.md`) — every task landed and verified,
   no sequencing rule left open.

3. CLOSE SEQUENCE — propose, do not execute:
   - the merge command (project convention, e.g. fast-forward into `main`);
   - the push command(s) and the requirement of a human-confirmed green CI run
     for the exact pushed SHA before any cleanup;
   - branch/tag cleanup steps only after that confirmation;
   - anything the project's charter adds (release, docs, task-ledger updates).

4. STOP with the command list and what could go wrong. I run the commands and
   confirm CI; only then is the feature closed.

If the evidence chain is incomplete, STOP and tell me exactly which leg or gate
is missing — never wave a gap through.
