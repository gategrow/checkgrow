# CheckGrow

**Check your AI. Grow yourself.**

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Hermes](https://img.shields.io/badge/complements-Hermes%20Agent-FFD700.svg)](https://github.com/NousResearch/hermes-agent)

---

## A 200-line script. 4 rounds of review. 9 bugs found.

**8 of those 9 were invisible to self-review.** The author stared at the same code for hours and saw nothing wrong. An adversarial subagent — told "you did NOT write this, find every bug" — caught them all in minutes.

That's the problem CheckGrow solves: **your AI produces output, but who checks it? And what do YOU learn from each interaction?**

Current AI tools (Claude Code, Cursor, Copilot, Hermes) are laser-focused on *making AI do more things*. None of them answer what happens *after* the AI finishes. CheckGrow fills that gap.

---

## What this gives you

| Without CheckGrow | With CheckGrow |
|---|---|
| AI writes code, you hope it's correct | AI's output is adversarially reviewed before you see it |
| You learn nothing from the interaction | Every session grows your personal knowledge base |
| Same mistakes repeat across sessions | Delivery gate enforces learning capture |
| Config files drift into format chaos | Format check catches drift before it degrades AI behavior |

---

## If you already use Hermes

Hermes gives your AI **memory and skills**. CheckGrow gives your AI output **accountability**.

| Hermes | CheckGrow |
|---|---|
| Gives your AI long-term memory | Gives your AI output adversarial review |
| Extends what your AI can DO | Checks what your AI DID |
| Skills run during tasks | Gate runs before delivery |
| Auto-creates skills from experience | Auto-enforces learning capture from sessions |

They complement each other. Hermes is the OS. CheckGrow is the antivirus + update log.

---

## Quick start

### 1. Install the delivery gate (30 seconds)

```bash
curl -O https://raw.githubusercontent.com/YuhaoLin2005/checkgrow/main/delivery-gate/quality-gate.py
cp quality-gate.py ~/.claude/scripts/
```

Add to `~/.claude/settings.json`:
```json
{
  "hooks": {
    "Stop": [{
      "hooks": [{
        "type": "command",
        "command": "python3 ~/.claude/scripts/quality-gate.py",
        "timeout": 5000
      }]
    }]
  }
}
```

### 2. Try the self-audit demo

```bash
python3 self-audit/self_audit.py --file examples/broken-output.txt --verbose
```

---

## What's inside

```
checkgrow/
├── delivery-gate/         Stop hook — blocks session end until quality checks pass
├── adversarial-review/    Claude Code skill — spawn adversarial subagents to review output
├── dual-pool-review/      Methodology — multi-persona cross-review with fixed+random pools
├── self-audit/            CLI tool — 4-dimension output quality audit (pip-installable)
├── format-consistency/    Checker — validates config file format consistency across files
├── docs/
│   ├── five-libraries.md
│   ├── three-tier-review.md
│   ├── five-step-decision-flow.md
│   └── quickstart.md
└── examples/
    ├── broken-output.txt
    └── delivery-gate-9-bugs.md
```

---

## Format consistency — a genuinely new insight

**Config file format inconsistency degrades AI behavior.** When CLAUDE.md uses bullet lists, AGENTS.md uses numbered steps, and .cursorrules mixes tables with prose — the LLM pays a "parsing tax" on every context switch.

In our case study: consolidating 6+ format styles across 4 config files into 3 cut total config size 28% (232→168 lines). Behavior consistency improved — same rules, less format noise.

This was confirmed via web search calibration: **no public content discusses this problem.** The `format-consistency/` check script automates detection.

---

## The decision flow that built this repo

Every architecture decision here went through:

```
Self-review → Multi-expert adversarial panel → Confirm adjustments → Implement → Non-adversarial final check
```

Applying this to the consolidation plan found **39 issues** (3 critical, 11 high) before writing a single line. Documented in `docs/five-step-decision-flow.md`.

---

## Proven in production

| Case | What happened |
|---|---|
| **delivery-gate** | 200-line script, 4 rounds review → 9 bugs, 8 invisible to self-review |
| **Remote sensing** | ENVI scripts → adversarial review caught 3 critical bugs |
| **This repo's consolidation** | 39 issues found by applying the 5-step flow to the plan itself |
| **Format consistency** | 4 config files, 6+ styles → 28% reduction, behavior improvement |

---

## License

MIT

---

*Every section of this README was adversarially reviewed before publishing.*
