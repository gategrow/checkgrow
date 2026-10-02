# Contributor setup

CheckGrow is a methodology and documentation repository, not an application to
build. You do not need an API key or Python to contribute Markdown.

## Get the source

```sh
git clone https://github.com/gategrow/checkgrow.git
cd checkgrow
```

Read the [Start Here table](README.md#start-here), then
[CONTRIBUTING.md](CONTRIBUTING.md). Choose one focused change and discuss new
patterns or skills in an [issue](https://github.com/gategrow/checkgrow/issues)
before implementing them. An existing issue can supply that discussion.

## Choose a path

| Contribution | Setup and verification |
| --- | --- |
| Documentation | Edit Markdown in your editor. Preview it, check fenced code blocks and tables, and follow changed relative links. No installation is required. |
| Methodology or failure pattern | Read `docs/METHODOLOGY.md` and `docs/failure-patterns.md`. Supply an observed example, symptoms and a detection method, not a hypothetical incident. |
| Skill changes | Use a compatible agent such as Claude Code to test manually in a disposable project. Review the skill instructions before installing or invoking them; keep credentials and private transcripts out of your PR. |

Skill verification depends on the particular skill and backend. Read its
documentation first; do not install every tool to make a documentation edit.
The mechanical Python scripts are maintained in the separate
[delivery-gate repository](https://github.com/gategrow/delivery-gate), not in
this checkout. If you test those scripts, Python 3.8+ is required there.

## Find the relevant files

```text
docs/                 methodology, failure patterns, and decision flow
adversarial-review/   adversarial review skill
self-audit/           reasoning audit skill and supporting material
format-consistency/   configuration-format guidance
examples/             example outputs
README.md             entry points and links to standalone tools
```

There is no package install or automated test command needed for a docs-only
change. In particular, this checkout does not contain the `adapt.py` or
`semantic-map.json` mentioned in the older contributor setup text; do not try
to run a missing script as a validation step.

## Send the change

Create a branch in your fork, keep the diff focused, and explain what you
changed and how you verified it. Use the repository's contribution checklist
when available. For questions, use the
[issue tracker](https://github.com/gategrow/checkgrow/issues).
