# CheckGrow

**Check your AI. Grow yourself.**

> AI output quality toolkit: adversarial review + delivery gate + format consistency + metabolic cost tracking. For Claude Code, Cursor, Hermes, and any AI agent user.

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Start Here

First time? Pick your path:

| You want to... | Start here |
|---|---|
| Understand the whole framework | [METHODOLOGY.md](docs/METHODOLOGY.md) — core thesis, principles, how pieces connect |
| Install the mechanical gate | [delivery-gate](https://github.com/gategrow/delivery-gate) — two Python scripts, zero dependencies |
| Learn from real AI failures | [failure-patterns.md](docs/failure-patterns.md) — 10 patterns from real sessions |
| Add adversarial review to your workflow | [adversarial-review/](adversarial-review/) — spawn review subagents |
| Audit AI reasoning quality | [self-audit/](self-audit/) — four-dimension reasoning audit CLI |
| Contribute a pattern or skill | [CONTRIBUTING.md](CONTRIBUTING.md) — open an issue first |

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
| No idea how much sessions cost | Metabolic tracking shows per-session cost + layered decisions |

---

## What's inside

```
checkgrow/
├── docs/
│   ├── METHODOLOGY.md                ★ Start here — the unified framework
│   ├── failure-patterns.md          10 patterns catalogued from real sessions
│   ├── five-step-decision-flow.md   Self-review → panel → confirm → implement → check
│   ├── hybrid-gate-architecture.md  Mechanical + reasoning gate design
│   └── t-cbb-convergence.md        Architecture convergence with SwarmAI's T-CBB
├── adversarial-review/    Skill — spawn adversarial subagents (with Litmus Pre-Gate)
├── self-audit/            Skill — mechanical Step 0 + four-dimension reasoning audit
├── format-consistency/    Docs — detect config format drift (independently validated by T-CBB OP8)
└── examples/
    └── broken-output.txt           Demo: deliberately broken AI output

Also available as standalone tools:
├── delivery-gate → github.com/gategrow/delivery-gate
├── dual-pool-review → github.com/gategrow/dual-pool-review
└── self-audit pip package → github.com/gategrow/self-audit
```

---

## Canonical Sources

This repository is the **canonical source for the CheckGrow methodology**: failure patterns, hybrid gate architecture, decision flow, and the unified framework. The methodology defines *why* and *what*.

| Aspect | Canonical source |
|---|---|
| Methodology (why, what) | **checkgrow** (this repo) — docs/ |
| Python reference implementation | **[delivery-gate](https://github.com/gategrow/delivery-gate)** — config-health.py + quality-gate.py |
| Production deployment (Node.js) | **[ECC fork](https://github.com/YuhaoLin2005/ecc/blob/master/skills/delivery-gate/SKILL.md)** — Stop hook with zero-config auto-trigger |

**Implementation differences are by design, not drift.** Python reference has rationalization detection + config-health (full feature set). Node.js production fork removes rationalization (regex on non-English transcripts is unreliable) and adds zero-config auto-registration. If you're adding a feature, start with the Python reference implementation — it's the easiest to test and iterate on.

---

## Proven

| Case | What happened |
|---|---|
| **delivery-gate** | 200-line script, 4 rounds review → 9 bugs, 8 invisible to self-review |
| **Remote sensing** | ENVI scripts → adversarial review caught 3 critical bugs |
| **Format consistency** | 4 config files, 6+ styles → 28% reduction, behavior improvement |

---

## Theoretical Background

CheckGrow's architecture independently converged with two production systems:

**T-CBB (SwarmAI):** T-CBB's autonomous pipeline framework lists "Config Consistency" (OP8) as one of eight operational invariants. The four-dimension quality gate taxonomy converged across both systems. T-CBB operates at pipeline boundaries; CheckGrow applies the same principle at the session level. [See acknowledgments.](ACKNOWLEDGMENTS.md)

**Hermes Agent:** Hermes gives AI agents persistent memory and auto-created skills. CheckGrow adds the quality assurance layer — adversarial review, mechanical verification, enforced learning capture, and metabolic cost tracking.

---

## Community

Contributions welcome. Here's how to get involved:

- **Found something wrong?** [Report a bug](https://github.com/gategrow/checkgrow/issues/new?template=bug_report.md)
- **Have a failure pattern to add?** [Propose it](https://github.com/gategrow/checkgrow/issues/new?template=feature_request.md)
- **First time contributing?** Read [CONTRIBUTING.md](CONTRIBUTING.md)

Maintained by [@YuhaoLin2005](https://github.com/YuhaoLin2005)

---

## Acknowledgments

See [ACKNOWLEDGMENTS.md](ACKNOWLEDGMENTS.md). Special thanks to **xg-gh-25 (SwarmAI)** for the T-CBB review that found the exact structural weakness in self-audit v1.0 in two sentences.

---

## License

MIT
