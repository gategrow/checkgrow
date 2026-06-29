# Attributions

CheckGrow exists because others shared their work first.

## T-CBB (Coding as Black Box)

**xg-gh-25 / SwarmAI** — The T-CBB autonomous pipeline framework independently converged on the same four-dimension quality gate pattern. OP8 (Config Consistency) directly validates our format consistency finding as a system-level operational invariant. The mechanical+reasoning hybrid gate architecture, binary push-ready design, and profile-based task classification all influenced CheckGrow's architecture.

- Autonomous Pipeline Design: [SwarmAI docs](https://github.com/xg-gh-25/SwarmAI/blob/main/docs/Autonomous-Pipeline-Design.md)
- PR review that pushed self-audit from v1.0 to v2.0: [anthropics/skills#1367](https://github.com/anthropics/skills/pull/1367)

Thank you for the review that found the exact structural weakness in two sentences that I had walked past for weeks.

## Hermes Agent

**Nous Research** — Hermes' skill format (YAML frontmatter, HARDLINE rules, conditional activation) shaped CheckGrow's skill standardization. The SKILL.md conventions used across CheckGrow skills are adapted from Hermes' open standard.

- [Hermes Agent](https://github.com/NousResearch/hermes-agent)
- [AgentSkills.io](https://agentskills.io)

## ECC (Everything Claude Code)

**affaan-m / daltino** — ECC provided the first community validation of delivery-gate. daltino's approval on PR #2365 confirmed the "thinking quality" concept was worth pursuing.

- [ECC #2365](https://github.com/affaan-m/ECC/pull/2365) (approved)
- [ECC #2378](https://github.com/affaan-m/ECC/pull/2378) (active)

## anthropics/skills

**Anthropic** — The skills repository provided the platform for self-audit's first public review and SwarmAI's subsequent technical review.

- [self-audit PR #1367](https://github.com/anthropics/skills/pull/1367)

## agent-best-practices

**NextFrontierBuilds** — Accepted the format consistency anti-pattern as a community contribution.

- [PR #1](https://github.com/NextFrontierBuilds/agent-best-practices/pull/1)

## Tools & Libraries

- **Python** — stdlib-only design philosophy
- **Claude Code** — the agent harness that runs CheckGrow's hooks
- **CodeRabbit & Greptile** — automated review bots that caught 9 bugs in delivery-gate

---

*"If I have seen further, it is by standing on the shoulders of giants." — Isaac Newton*
