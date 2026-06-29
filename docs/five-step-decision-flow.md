# Five-Step Decision Flow

> Every significant decision — repo consolidation, architecture change, community contribution — goes through this process before implementation.

## Why this exists

Existing review systems (adversarial-review, dual-pool-review, self-audit) review **outputs** (code, documents, configs). But **decisions themselves** — "should I consolidate 7 repos into 1?" — had no structured review process. This fills that gap.

## The five steps

### Step 1: Self-review

Do a thorough first-pass review yourself. Identify obvious issues, missing pieces, assumptions.

- Output: categorized findings (Critical/High/Medium/Low) + known issues list
- Gate: at least 10 findings OR explicit confirmation

### Step 2: Multi-expert adversarial panel

Spawn 3+ independent expert agents with different perspectives:
- **Engineer A**: Technical correctness
- **Engineer B**: Architecture and integration
- **Product (Kathy Sierra)**: User value, over-engineering detection

Each agent receives the proposal + self-review findings. Agents are independent — they don't see each other's output.

### Step 3: Confirm adjustments

Synthesize all findings. Cross-reference which appear in multiple reviews (higher confidence), which contradict (needs human judgment). Output: confirmed action plan.

### Step 4: Implement

Execute the confirmed plan. Fix all Critical + High before proceeding. Each fix gets its own commit. If implementation reveals new issues → pause, re-enter Step 1.

### Step 5: Non-adversarial final check

Sanity check: Did we do what we said? Are all Critical/High resolved? Is the output internally consistent? No new problems? This is verification, not bug hunting.

## When to use

- Consolidating repositories
- Choosing between architectural approaches
- Making significant open-source contribution decisions
- Any decision where getting it wrong costs more than doing the review

## When to skip

- Single-line fixes or trivial changes
- Time-critical situations where delay is worse than imperfection

## Real example: CheckGrow consolidation

Applying this flow to the CheckGrow consolidation plan found **39 issues** (3 Critical, 11 High) before a single line of code was written. The self-review's 15 findings grew to 32 after the expert panel. Fixing these BEFORE implementation saved an estimated 4-6 hours of rework.

## Related

- [[three-tier-review]] — output review (双池→自审→交付门)
- [[dual-pool-review]] — the multi-expert panel methodology
