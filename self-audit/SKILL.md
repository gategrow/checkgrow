---
name: self-audit
description: Hybrid quality gate — mechanical artifact check + four-dimension reasoning audit. Catches what tests miss.
version: 2.0.0
tags: [quality, audit, verification, delivery-gate]
---

# Self-Audit (v2.0 — Hybrid Gate)

Before you ship, verify mechanically first, then audit reasoning. This is a hybrid gate:

- **Mechanical (Step 0)**: Did you actually produce what you claim? No trust, verify.
- **Reasoning (Steps 1-4)**: Is your thinking sound? Four dimensions of audit.

Tests verify code. Nothing verifies reasoning. And **nothing verifies that the agent actually wrote the file it claims it wrote.** This skill fills both gaps.

---

## Step 0 — Mechanical Artifact Check (NEW in v2.0)

**Before any reasoning audit, verify the output physically exists.**

If the agent claimed to produce files:
```bash
# For each claimed output file
ls -la <path>  # or: python3 -c "import os; print(os.path.exists('<path>'))"
```

If the file doesn't exist → **BLOCK immediately. Do not proceed to reasoning audit.** The agent's claim is mechanically false.

This catches: "I generated report.md" when no file was written. No amount of reasoning audit can detect a physically absent artifact.

**Gate:** All claimed output files exist AND are readable → proceed to Step 1. Any missing → BLOCK, report to user, do not pass go.

---

## The Four Reasoning Questions

1. **Did I answer everything?** (Completeness)
2. **Did I contradict myself?** (Consistency)
3. **Did I show evidence?** (Groundedness)
4. **Am I being honest about the limits?** (Honesty)

If any answer is no → fix it → re-ask. Code can pass all tests with sloppy thinking behind it.

## Priority Order

1. **Honesty** — Never misrepresent what was done.
2. **Completeness** — Missing requirements cause more harm than inconsistency.
3. **Consistency** — Contradictions confuse but rarely cause data loss.
4. **Groundedness** — Complete honest soft evidence > evidenced but missing half.

## Hard Constraints

- **Never fabricate findings.** If all four dimensions pass, report PASS. If any fail, report FIXED with specifics.
- **Never expose sensitive data.** Redact paths, secrets, tokens, PII before displaying audit output.
- **Never block on subjective grounds.** Flag only concrete, verifiable gaps — not stylistic preferences.
- **Step 0 is non-negotiable.** If agent claimed to produce files, mechanical check runs first. No exceptions.

## When to Use

- Complex task completed (3+ file edits)
- Agent about to stop and deliver results
- After architectural decisions with downstream impact
- Agent claimed to produce output files (Step 0 applies)
- Proactively: if you are about to ship, audit first

## The Four Questions

### 1. Completeness
List each request. Verify response or deferral. Flag partials as full. If input was a spec/feature-list → map each requirement to the output section that addresses it. Flag unmapped requirements.

### 2. Consistency
Scan vs earlier. Check project rules. Flag A-and-not-A.

### 3. Groundedness
Identify claims. Evidence or words? Distinguish not-verified vs hidden.

### 4. Honesty
Check over-packaging. Edge cases mentioned? Verified without showing? Missing error handling = production ready?

## Process

0. **MECHANICAL**: If agent claimed output files → `os.path.exists()` each one. Missing → BLOCK.
1. COMPLETE task
2. ASK four. Fail → fix → re-ask.
3. 3+ stuck: report blocking, ask user.
4. All pass → stop.

Output:
```
Self-Audit (v2.0):
Step 0 (Mechanical):  PASS | BLOCKED [file not found: <path>]
Completeness:         OK | FIXED [what]
Consistency:          OK | FIXED [what]
Groundedness:         OK | FIXED [what]
Honesty:              OK | FIXED [what]
```

## Failure Modes

- **Step 0 blocks but reasoning would pass**: The agent's reasoning was fine but it forgot to write the file. This is exactly why Step 0 exists — reasoning audit alone cannot catch this.
- **Overly long**: Sample 5 most critical.
- **Data leak**: Redact before display.
- **Fatigue**: Detail mode for shipping only.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| Simple change, no audit | Simple changes cause bugs. 30s saves hours. |
| Checked as I went | Cross-cutting only in dedicated pass. |
| User will catch | Users not QA. |
| All four OK no detail | Complex tasks find >=1 issue. |
| Verified internally | Without output = assumption. |
| I'm sure I wrote the file | Step 0 verifies mechanically. Trust no one. |

## Red Flags

- Stopping without audit
- Step 0 skipped when files were claimed
- All OK no specifics
- Verified without showing
- Requirements dropped silently
- Audit hidden in reasoning

## Verification

- [ ] Step 0: All claimed output files mechanically verified to exist
- [ ] Requirement traceability: if spec was provided, each requirement mapped to output section
- [ ] Four questions answered with specific evidence (not "seems fine")
- [ ] FIXED applied for every failed dimension
- [ ] Audit output visible in the response (not buried in reasoning)
- [ ] Hard constraints respected — no fabricated findings, no leaked data
- [ ] No rationalized omissions (skipped work documented as skipped, not as done)

## Architecture Note

This skill is the **reasoning** half of a hybrid quality gate. The **mechanical** half is `delivery-gate` — a Stop hook that checks file timestamps and disk space without trusting any agent claims.

Together they implement the T-CBB (Coding as Black Box) pattern: treat agent output as untrusted, verify mechanically first, audit reasoning second. SwarmAI deploys the same four-dimension gate at pipeline handoff boundaries.

## See Also

- `delivery-gate` — Mechanical Stop hook (gategrow/delivery-gate)
- `adversarial-review` — Spawn adversarial subagents for code review
- `code-reviewer` — Review code changes for correctness and quality
- `security-review` — Identify vulnerabilities in the output
