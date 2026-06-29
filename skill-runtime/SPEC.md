# LLM-Agnostic Skill Standard v1.0

> Skills describe WHAT to do. The runtime translates to HOW — based on the current LLM backend.

## Problem

Skills today bind to specific LLM ecosystems. Claude Code skills use `Agent`. Hermes skills use `delegate_task`. Same purpose, different syntax. Switching models breaks skills — or forces duplicate maintenance.

## Solution

Skills use **semantic verbs** — abstract action names wrapped in `{braces}`. A thin runtime adapter translates these to the current LLM's native tools at load time.

```
Skill (LLM-agnostic)           Runtime Adapter           LLM-specific output
─────────────────────          ──────────────           ────────────────────
{spawn_reviewer}          →    Claude Code: Agent(      
                              subagent_type:"code-reviewer")
                         →    Hermes: delegate_task(...)
                         →    Codex: task(...)
```

Same philosophy as SOUL/INTERFACE/BODY:
- Skill content = SOUL (what stays constant)
- Runtime mapping = INTERFACE (what changes per model)

## Semantic Verbs

Only 10 verbs. Each maps to a primitive every LLM ecosystem has.

### Core (every skill uses these)

| Verb | Semantic Meaning | Never Means |
|------|-----------------|-------------|
| `{read}` | Read file or search codebase | Write, modify, delete |
| `{write}` | Create or modify a file | Read, search, execute |
| `{execute}` | Run a shell command | File I/O |
| `{search}` | Web search or fetch URL | Local file search (use {read}) |

### Agent (multi-agent patterns)

| Verb | Semantic Meaning |
|------|-----------------|
| `{spawn}` | Create a sub-agent for a task |
| `{review}` | Spawn an adversarial reviewer |

### Verification (quality gates)

| Verb | Semantic Meaning |
|------|-----------------|
| `{verify}` | Check file existence/permissions |
| `{validate}` | Run tests, linters, schema checks |

### Extended (optional, for complex skills)

| Verb | Semantic Meaning |
|------|-----------------|
| `{notify}` | Send message to user/platform |
| `{store}` | Persist data (memory, DB, file) |

## Mapping Table

| Verb | Claude Code | Hermes | Generic CLI |
|------|------------|--------|-------------|
| `{read}` | Read, Glob, Grep | read_file, search_files | cat, grep, find |
| `{write}` | Write, Edit | write_file, patch | echo >, sed |
| `{execute}` | Bash | terminal | sh, bash |
| `{search}` | web_search, web_fetch | web_extract | curl |
| `{spawn}` | Agent | delegate_task | — |
| `{review}` | Agent(subagent_type:"code-reviewer") | delegate_task(adversarial) | — |
| `{verify}` | Read, Bash(ls) | read_file, terminal(ls) | ls, test -f |
| `{validate}` | Bash(pytest/lint) | terminal(pytest/lint) | pytest, eslint |
| `{notify}` | — (print to user) | — (gateway message) | echo |
| `{store}` | Write | write_file | echo >, sqlite |

## Skill Format

A compliant SKILL.md uses semantic verbs **instead of** tool names:

```markdown
## When to Use
...

## Procedure

### 1. Extract review criteria
{read} the requirements file to build a checklist.

### 2. Spawn adversarial reviewer
{review} with prompt: "You did NOT write this. Find every bug."

### 3. Verify output
{verify} that all claimed output files exist. {validate} with test suite.
```

### Rules

1. Semantic verbs MUST use `{verb_name}` syntax with braces
2. Skill MUST NOT reference concrete tool names (`Agent`, `delegate_task`, `Bash`, `terminal`)
3. Skill MAY include plain English description of what the verb does
4. Skill MUST declare `requires: [verb1, verb2]` in frontmatter

### Frontmatter

```yaml
---
name: adversarial-review
requires: [read, write, review, verify]
version: 2.0.0
---
```

## Runtime Adapter

The adapter is a simple Python script that:
1. Reads SKILL.md
2. Detects current LLM backend (Claude Code, Hermes, Codex, or env var)
3. Replaces `{verb}` with the mapped concrete tool call
4. Outputs adapted skill text

```bash
# Auto-detect backend
skill-adapt path/to/SKILL.md

# Explicit backend
skill-adapt --backend hermes path/to/SKILL.md

# Pipe mode
cat SKILL.md | skill-adapt --backend claude
```

## Design Principles

1. **10 verbs, not 100.** Every verb must satisfy: "does every LLM ecosystem have an equivalent?"
2. **Semantic, not syntactic.** Verbs describe intent, not implementation.
3. **Additive to agentskills.io.** agentskills.io standardizes directory structure and metadata. This standard adds content portability. Complementary, not competitive.
4. **Backward compatible.** Existing skills can migrate one verb at a time.

## Migration Path

### Phase 1: Add `requires` frontmatter
Existing skills add `requires: [...]` to declare their verb dependencies. No content changes.

### Phase 2: Replace tool names
One verb at a time: `Agent(subagent_type:"code-reviewer")` → `{review}`.

### Phase 3: Remove tool-specific prose
"Use the file-read tool" → `{read}`.

## License

MIT — free to implement, extend, and adapt.
