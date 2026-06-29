# CheckGrow

**Check your AI. Grow yourself.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## A 200-line script. 4 rounds of review. 9 bugs found.

**8 of those 9 were invisible to self-review.** The author stared at the same code for hours and saw nothing wrong. An adversarial subagent — told "you did NOT write this, find every bug" — caught them all in minutes.

That's the problem CheckGrow solves: **your AI produces output, but who checks it? And what do YOU learn from each interaction?**

---

## What this gives you

| Without CheckGrow | With CheckGrow |
|---|---|
| AI writes code, you hope it's correct | AI's output is adversarially reviewed before you see it |
| You learn nothing from the interaction | Every session grows your personal knowledge base |
| Same mistakes repeat across sessions | Delivery gate enforces learning capture |
| Config files drift into format chaos | Format check catches drift before it degrades AI behavior |
| No idea how much your sessions cost | Metabolic tracking shows per-session cost + layered decisions |

---

## What's inside

```
checkgrow/
├── delivery-gate/         Stop hook — blocks session end until quality checks pass
├── adversarial-review/    Skill — spawn adversarial subagents (with Litmus Pre-Gate)
├── self-audit/            Skill — mechanical Step 0 + four-dimension reasoning audit
├── dual-pool-review/      Methodology — multi-persona cross-review
├── format-consistency/    Checker + docs — detect config format drift (OP8-validated)
├── docs/
│   ├── failure-patterns.md          10 patterns catalogued from real sessions
│   ├── five-step-decision-flow.md   Self-review → panel → confirm → implement → check
│   ├── hybrid-gate-architecture.md  Mechanical + reasoning gate design
│   └── quickstart.md
└── examples/
    └── broken-output.txt           Demo: deliberately broken AI output
```

---

## Proven in production

| Case | What happened |
|---|---|
| **delivery-gate** | 200-line script, 4 rounds review → 9 bugs, 8 invisible to self-review |
| **Remote sensing** | ENVI scripts → adversarial review caught 3 critical bugs |
| **This repo's consolidation** | 39 issues found by applying the 5-step flow to the plan itself |
| **Format consistency** | 4 config files, 6+ styles → 28% reduction, behavior improvement |

---

## Theoretical Background

CheckGrow's architecture independently converged with two production systems:

**T-CBB (SwarmAI):** T-CBB's autonomous pipeline framework lists "Config Consistency" (OP8) as one of eight operational invariants — independently confirming that format uniformity across AI config files is a system-level requirement. The four-dimension quality gate (Completeness/Consistency/Groundedness/Honesty) converged with T-CBB's Output/Requirement/Contradiction/Evidence taxonomy. T-CBB operates at pipeline boundaries; CheckGrow applies the same principle at the session level.

**Hermes Agent:** Hermes gives AI agents persistent memory and auto-created skills. CheckGrow adds the quality assurance layer — adversarial review, mechanical verification, enforced learning capture, and metabolic cost tracking — that sits alongside Hermes' skill execution.

---

## Acknowledgments

CheckGrow exists because others shared their work first. See [ATTRIBUTIONS.md](ATTRIBUTIONS.md) for the full list.

Special thanks to **xg-gh-25 (SwarmAI)** for the T-CBB review that pushed self-audit from v1.0 to v2.0 — finding the exact structural weakness in two sentences.

---

## License

MIT
