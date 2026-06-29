# Format Consistency Checker

**Config file format inconsistency degrades AI behavior.** When CLAUDE.md uses bullet lists, AGENTS.md uses numbered steps, and .cursorrules mixes tables with prose — the LLM pays a "parsing tax" on every context switch.

## The problem

LLMs parse your config files on every session startup. When the format convention shifts between files, the model re-learns how to parse each file instead of just reading what it says. This wastes attention that should go to following your actual rules.

## Real data

In our case study: consolidating 6+ format styles across 4 config files into 3 cut total config size 28% (232→168 lines). Behavior consistency improved — same rules, less format noise.

## External validation

This finding is independently corroborated by SwarmAI's T-CBB (Coding as Black Box) autonomous pipeline framework, which identifies **Config Consistency (OP8)** as one of eight operational invariants:

> OP8 — Config consistency: All copies in sync or explicitly excluded.

T-CBB treats config format uniformity as a system-level requirement for autonomous coding pipelines. CheckGrow applies the same principle at the individual developer's config file level — same pattern, different granularity.

## Three rules

1. **One base format across all config files.** Pick bullets or numbered steps as your primary format, not both.
2. **Tables are for comparison data only.** A list of conventions? Bullets. Don't mix.
3. **Audit format drift like dependency drift.** New config section? Check: does its format match the rest?

## Related

- T-CBB Autonomous Pipeline Design: OP8 Config Consistency
- [Format Consistency article on DEV.to](https://dev.to/yuhaolin2005/your-ai-config-files-are-fighting-each-other-13c7)
