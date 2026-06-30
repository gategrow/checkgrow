# Contributing to CheckGrow

CheckGrow is a methodology project — every contribution is a piece of insight about how AI agents fail and how to catch it.

## Two Ways to Contribute

### 1. Content (the core of CheckGrow)

| What | Where | Example |
|------|-------|---------|
| Failure pattern | `docs/failure-patterns/` | A new way agents degrade that you've observed |
| Skill | `skills/` directory | A review/audit/check skill that catches failures |
| Real-world example | `docs/examples/` | A concrete case where a failure pattern was caught |
| Backend mapping | `semantic-map.json` | Verb mappings for a new AI backend |

### 2. Documentation

Fix typos, clarify explanations, add diagrams. See `docs/` and `README.md`.

## Development Setup

Zero build. Just write:

```bash
# Check semantic map coverage (if you touch config files)
python3 adapt.py --check
```

`adapt.py` is the only code — it translates semantic verbs (like `{read}`) to concrete tool calls across LLM backends via `semantic-map.json`.

## Code Standards (for skills and config)

- **YAML frontmatter** — every skill file starts with `---` frontmatter block
- **HARDLINE rules** — behavioral rules use SHALL/MUST, not "should"
- **Semantic map entries** — `<field>: <description>` format, one entry per line
- **Markdown** — all documentation in CommonMark-compatible markdown

## PR Process

1. **Open an issue first** — especially for new failure patterns and skills. Let's discuss before you write.
2. Fork and create a feature branch
3. One concern per PR — a single failure pattern, a single backend mapping, etc.
4. If adding a failure pattern, include: name, symptoms, root cause, detection method, real-world example
5. Reference related docs and patterns

## Project Philosophy

- **Observation over speculation** — failure patterns must be based on observed behavior, not hypothetical risks
- **Mechanical where possible, reasoning where necessary** — prefer checks that don't require AI judgment
- **Open loop tracking** — every check should produce a record that can be reviewed later
