---
name: adversarial-review
description: Adversarially review your own output before delivering — spawn subagents that find what self-review misses.
version: 1.2.0
tags: [review, quality, adversarial, code-review, self-audit]
related_skills:
  - {skill: self-audit, relation: "adversarial-review finds bugs; self-audit gates delivery"}
---

# Adversarial Review Skill

> Self-review has a blind spot. Spawn independent subagents from a "you didn't write this" perspective to find what you can't see.

## When to Use

- After writing code/scripts/documents where correctness matters
- When the user says "review this", "check my work", "/adversarial-review"
- Before pushing a PR, publishing content, or delivering complex output
- After multi-file edit sessions where errors could cascade

## Skip For

- Single-line typo fixes or trivial formatting changes
- Tasks the user explicitly says don't need review

---

## Litmus Pre-Gate (30 seconds)

Before a full adversarial review, run a quick structural sanity check. Any hard-fail → return for rework immediately; don't waste a full review on something obviously broken.

| Check | Hard-Fail Condition |
|---|---|
| HF1: Scaffold-only | Changes contain only placeholder/boilerplate, no real logic |
| HF2: Coverage gaps | Acceptance criteria exist but no implementation addresses them |
| HF3: Contradictions | Output contradicts itself or stated constraints |
| HF4: Missing error handling | I/O, network, or DB operations have no error paths |

**Any HF = FAIL → fix before proceeding to full review. Max 2 litmus failures per session.**

---

## Core Principle

**Don't review your own work. Spawn someone else.** The author has confirmation bias — the subagent doesn't.

Review standard: check against requirements/spec/criteria, not "code quality" in the abstract.

## Process

### Step 1: Extract review criteria
From the user's requirements, spec, or guidelines, extract each verifiable constraint into a checklist.

### Step 2: Spawn adversarial subagent

Use the Agent tool:
```
Agent(
  subagent_type: "code-reviewer",
  prompt: "You did NOT write this output. Your job is to find every problem. Be harsh. Assume nothing works. Zero findings = invalid review round."
)
```

### Step 3: Triage findings

- **CRITICAL**: Would cause incorrect output, data loss, or security issue → must fix
- **HIGH**: Would fail under specific conditions → must fix
- **MEDIUM**: Quality reduction without breaking → fix if time permits
- **LOW**: Style, naming → note, don't block

Fix all CRITICAL + HIGH before delivery.

### Step 4: Re-verify
After fixing, spawn a second subagent: "Confirm all CRITICAL and HIGH issues from the previous review are resolved. No new issues introduced."

## Pitfalls

- **症状**: Subagent returns "looks good, no issues found" → **原因**: Adversarial framing too weak; subagent defaulting to approval → **修复**: Re-spawn with stronger framing — "You DID NOT write this. Assume at least one bug exists. Zero findings = this round is invalid."
- **症状**: Fixing one bug introduces another → **原因**: Fix changed untested code paths → **修复**: After fixing, run single-agent quick check on changed lines only (not full re-review)
- **症状**: Too many LOW findings (>10) drowning signal → **原因**: No severity filter in prompt → **修复**: Add "Only report functional correctness and security issues. Skip code style."

## Verification

After review completes, confirm:
1. Litmus Pre-Gate passed (or cleanly skipped for non-code tasks)
2. Subagent returned at least one specific, actionable finding (not generic approval)
3. All CRITICAL + HIGH findings fixed and re-verified
4. User received structured summary (agent count, findings by severity, fixes applied)

## Related Skills

- [[self-audit]] — Mechanical + reasoning quality gate for delivery
- [[dual-pool-review]] — Multi-persona cross-validation methodology
