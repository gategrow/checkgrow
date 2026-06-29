# Failure Patterns

> Catalogued from real sessions. Each pattern: symptom → root cause → fix. These are what the delivery gate and adversarial review are designed to catch.

## Pattern 1: Aspirational Trigger

**Symptom:** Rule says "run check X after complex tasks." Two days later, zero checks ran.
**Root cause:** Trigger condition is vague ("complex task" undefined). Rule is a wish, not a mechanism.
**Fix:** Replace subjective triggers with mechanical ones. "≥3 file edits" or "≥1 Edit/Write call" is machine-checkable. "Complex task" is not.
**Sessions:** 2026-06-26 (四库空转), 2026-06-27 (quality-gate阈值5/5太宽)

## Pattern 2: Analysis Without Action

**Symptom:** Agent produces detailed analysis, identifies optimization, recommends fix — then does nothing.
**Root cause:** "Analyze and report" is the default mode. "Analyze and self-execute" requires explicit training.
**Fix:** After any analysis that contains "should/could/recommend [action]", ask: "Can I execute this action myself without user involvement?" If yes → execute, then report. If no → report with recommendation.
**Sessions:** 2026-06-27 (35%浪费分析), 2026-06-27 (quality-gate阈值分析不修)

## Pattern 3: Format Drift

**Symptom:** Config files accumulate different format styles over time. LLM behavior degrades — same rules, less consistent output.
**Root cause:** Each file is written at a different time, by a different mental model. No format audit exists.
**Fix:** Session-start check: verify all config files use consistent format (bullets vs numbered, header depth, table usage). Auto-correct on detection.
**Sessions:** 2026-06-27-style (6+ formats → 3 formats, -28% lines)
**T-CBB Corroboration:** OP8 Config Consistency is listed as a system-level operational invariant for autonomous pipelines.

## Pattern 4: Config Inheritance ≠ Behavior Inheritance

**Symptom:** Rules persist across sessions (files on disk), but behavior resets each session (LLM context is fresh).
**Root cause:** File inheritance is physical. Behavior inheritance requires re-activation at session start.
**Fix:** Session-start sequence must actively re-load and re-verify all behavioral rules. "续接上一轮" → automatically classify as complex session.
**Sessions:** 2026-06-26 (翻车12)

## Pattern 5: Single-Environment Testing Blindness

**Symptom:** Code tested on Python 3.12 passes. Deployed to Python 3.8 → crashes.
**Root cause:** Developer tests on their own environment. Edge cases invisible from inside.
**Fix:** Adversarial subagent uses different assumptions: "What if this runs on Python 3.8? What if the directory isn't flat?"
**Sessions:** 2026-06-26 (翻车10, delivery-gate list[str] crash)

## Pattern 6: Threshold Too Wide

**Symptom:** Automated check written, but never fires. "All 5 libraries must be stale" → never blocks because at least one gets updated.
**Root cause:** Threshold is calibrated for the ideal case, not the common case.
**Fix:** Set thresholds to catch the common failure mode. "≥3/5 stale OR growth-log stale → block" catches real misses. "5/5 stale → block" catches nothing.
**Sessions:** 2026-06-27-enforcement

## Pattern 7: Self-Review Confirmation Bias

**Symptom:** Author reviews own code → finds nothing. Independent reviewer → finds critical bugs.
**Root cause:** Author's mental model auto-corrects errors. They see what they intended to write, not what they wrote.
**Fix:** Never self-review for critical work. Spawn independent agent with adversarial framing: "You did NOT write this."
**Sessions:** 2026-06-28 (遥感ENVI 3致命bug), delivery-gate (8/9 bugs missed by self-review)

## Pattern 8: Git Operation Scope Error

**Symptom:** `git rebase --exec --root` rewrites entire repo history, destroys fork, auto-closes PR.
**Root cause:** `--root` means "from the first commit" — entire repo scope, not branch scope.
**Fix:** Before any git operation with `--root` or `--force`: verify scope. `HEAD~N` for branch; `--root` for entire repo.
**Sessions:** 2026-06-26 (翻车13深夜)

## Pattern 9: Duplicate Config Rules

**Symptom:** Same behavioral rule defined in 3 files. One gets updated, others stay stale → inconsistent behavior.
**Root cause:** Copy-paste is easier than reference. No single-source-of-truth enforcement.
**Fix:** Designate one authority file per rule category. Other files reference it; never duplicate.
**Sessions:** 2026-06-29 (agent-rules.md duplicated INTERFACE.md rules)

## Pattern 10: Secret Exposure via Config Backup

**Symptom:** Config backup repo contains API keys, session transcripts, operational details in public.
**Root cause:** "Backup my config" treats secrets and public settings as the same category.
**Fix:** .gitignore must explicitly list all sensitive files. Assume `git add .` will happen accidentally.
**Sessions:** 2026-06-29 (claude-config API key exposure)

---

## How to use this catalog

- **Before a session:** Scan for patterns that match your task type
- **During adversarial review:** Check output against each pattern
- **After a翻车:** If it fits an existing pattern → tighten the fix. If it's new → add it here.
