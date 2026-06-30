# CheckGrow Methodology

> The unified framework behind the mechanical gate, reasoning audit, and failure pattern catalog. Start here if you want to understand **why** CheckGrow is built the way it is, not just **how** to use it.

---

## Core Thesis

**AI output cannot be trusted on the AI's word alone.** Every claim an AI makes about its own work — "I tested this," "I captured the lesson," "no contradictions" — must be verified by something that cannot rationalize.

This sounds obvious. But the corollary is what makes CheckGrow a system rather than a single check:

> **No single verification method catches everything. Mechanical checks miss reasoning errors. Reasoning checks miss mechanical omissions. You need both — and you need them to not trust each other.**

This thesis produces three architectural commitments:

1. **Hybrid gate**: mechanical + reasoning, each verifying what the other can't
2. **Failure-driven design**: every gate rule traces back to a specific, documented failure pattern
3. **Self-application**: the methodology must be applied to itself (decisions get reviewed, patterns get catalogued, the framework evolves)

---

## The Four Dimensions: C/C/G/H

Why these four? Because they answer four questions that any AI output must survive:

| Dimension | Question | If it fails |
|-----------|----------|-------------|
| **Completeness** | Did you do everything you said you would? | Missing output, unfulfilled promises |
| **Consistency** | Do any claims contradict each other? | Self-contradiction across files or within one file |
| **Groundedness** | Is every claim backed by evidence? | Hallucinated facts, unsupported assertions |
| **Honesty** | Did you rationalize skipping work? | "This is a pre-existing bug," "skip tests for now" |

These four did not come from abstract taxonomy design. They came from cataloguing failure patterns across 40+ sessions and asking: "What category of verification would have caught this?" Every discovered failure fit into one of these four buckets. The taxonomy is **empirical**, not theoretical.

This convergence was independently validated: SwarmAI's T-CBB pipeline uses the same four-dimension taxonomy (Output/Requirement/Contradiction/Evidence) for autonomous code delivery. Two independent teams, solving different problems at different scales, arrived at the same answer. The problem space is real. See [T-CBB Convergence Notes](t-cbb-convergence.md).

---

## The Mechanical–Reasoning Boundary

The single most important design decision in CheckGrow is **what gets a mechanical check vs. what gets a reasoning check.**

The principle:

> **If the AI can lie about it without leaving physical evidence, it needs a mechanical check. If the physical evidence exists but the interpretation might be wrong, it needs a reasoning check.**

| Layer | What it catches | What it misses | Example |
|-------|----------------|----------------|---------|
| **Mechanical** | File not created, disk full, rationalization phrases in transcript | Correct file with wrong content | "report.md exists? Yes. Contents correct? No idea." |
| **Reasoning** | Contradiction between sections, unsupported claims, incomplete coverage | File that was claimed but never created | "All sections covered? Yes. File actually exists? Didn't check." |

Each layer is blind to what the other sees. That's the point — they compensate.

The mechanical layer itself splits into two sub-layers:

| Sub-layer | Principle | Blocks? | Example |
|-----------|-----------|---------|---------|
| **Process (soft)** | Rule execution can be retroactively tracked | Never | Marker counting, verification window |
| **Output (hard)** | Missed output is lost forever | Yes | Five-library freshness, disk space |

The boundary between soft and hard is: **"Can this be fixed later?"**

For the full architecture, see [Hybrid Gate Architecture](hybrid-gate-architecture.md).

---

## The Failure Pattern Feedback Loop

This is the engine that makes CheckGrow improve over time:

```
Session produces a failure
        ↓
Catalogue it as a pattern (failure-patterns.md)
        ↓
Ask: "What check would have caught this?"
        ↓
Add the check to the gate (mechanical or reasoning)
        ↓
Next session: gate catches it before it becomes a problem
```

Example: **Pattern 6 (Threshold Too Wide).** The original quality-gate required 5/5 libraries stale to block. It never fired because at least one library got incidental updates. The fix ("≥3/5 OR growth-log stale") came directly from analysing this failure. Without the pattern catalogue, the threshold would have stayed at 5/5 indefinitely — nobody would have noticed a check that silently never fires.

This loop is what separates CheckGrow from a static checklist. Each failure makes the gate stronger. The 10 patterns in [failure-patterns.md](failure-patterns.md) are not just documentation — they are the **design rationale** for every gate rule.

---

## How the Pieces Connect

```
FAILURE PATTERNS (failure-patterns.md)
    │  Catalogued from real sessions. Each pattern → a gate rule.
    │
    ├──→ MECHANICAL GATE (delivery-gate)
    │       config-health.py: rule markers, verification tracking
    │       quality-gate.py: file freshness, disk space, rationalization
    │       Principle: "verify what can be checked without reasoning"
    │
    ├──→ REASONING AUDIT (self-audit)
    │       Step 0 (mechanical): claimed files exist?
    │       Steps 1-4 (reasoning): C/C/G/H four-dimension audit
    │       Principle: "verify what requires understanding to check"
    │
    └──→ ADVERSARIAL REVIEW (adversarial-review)
            Spawn independent subagent told "you did NOT write this"
            Principle: "self-review is structurally unreliable"
            Pattern 7 (Self-Review Confirmation Bias) is the direct warrant
```

And for **decisions** (not outputs):

```
FIVE-STEP DECISION FLOW (five-step-decision-flow.md)
    Self-review → Expert panel → Synthesize → Implement → Final check
    Principle: "decisions deserve the same scrutiny as code"
```

---

## Principles (Summary)

1. **No single verifier is enough.** Mechanical + reasoning, each verifying what the other can't.
2. **Every gate rule has a documented failure behind it.** No speculative checks. If there's no pattern, there's no rule.
3. **Soft vs. hard = "can this be fixed later?"** Not importance. Process is soft, output is hard.
4. **Self-review is structurally unreliable.** Adversarial framing ("you did NOT write this") is the minimum bar.
5. **The methodology applies to itself.** Decision flow, pattern cataloguing, format consistency — the framework eats its own dog food.
6. **Silence on success.** Normal paths consume zero tokens. Only anomalies speak.

---

## What CheckGrow Is Not

- **Not a CI pipeline.** CheckGrow operates at the session level (per AI interaction), not the repository level (per commit). T-CBB operates at the pipeline level; the two are complementary, not competing.
- **Not a replacement for human review.** The gate catches mechanical failures and obvious reasoning errors. It does not catch subtle domain-specific mistakes. Human judgment is still the final authority.
- **Not a static checklist.** The failure pattern catalogue grows. Gate rules evolve. The system is designed to get better the more it fails.

---

## Reading Path

| You want to understand... | Read |
|---|---|
| The overall framework (you are here) | This document |
| Why mechanical + reasoning, and how they interact | [Hybrid Gate Architecture](hybrid-gate-architecture.md) |
| What specific failures the system defends against | [Failure Patterns](failure-patterns.md) |
| How decisions get reviewed before implementation | [Five-Step Decision Flow](five-step-decision-flow.md) |
| How CheckGrow relates to industrial systems | [T-CBB Convergence Notes](t-cbb-convergence.md) |
| The running implementation | [delivery-gate](https://github.com/gategrow/delivery-gate) |

---

## Acknowledgments

The four-dimension taxonomy converged independently with SwarmAI's T-CBB. The adversarial review framing ("you did NOT write this") was directly inspired by the observation that self-review caught 1/9 bugs in delivery-gate's code review. See [ACKNOWLEDGMENTS.md](../ACKNOWLEDGMENTS.md) for the full list.
