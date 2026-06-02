# skill-linting

A Claude Code plugin (and marketplace) that audits skills repos.

Bundles these skills:

- **`skill-linting`** — top-level structural lint for skills repos: layout, MCP doctest hygiene, asset isolation. Delegates the mechanical checks to the two skills below.
- **`check-skill-file-links`** — ensures every file path mentioned in markdown is a real markdown link to an existing file.
- **`detect-skill-contradictions`** — finds near-duplicate paragraphs across markdown files so you can fix duplication or genuine contradictions.
- **`claude-safety`** — reviews `~/.claude/settings.json` for risky auto-allowed permissions.
- **`recommend-ci-linters`** — recommends off-the-shelf CI linters (lychee, skill-validator) for skills repos that don't already run them.

## Install

In Claude Code:

```
/plugin marketplace add ryanpeach/skills-marketplace
/plugin install skill-linting@ryanpeach
```

Then `/reload-plugins` (or restart Claude Code).

## Use

The `skill-linting` skill auto-activates when you ask Claude to lint or audit a skills repo, and pulls in `check-skill-file-links` and `detect-skill-contradictions` for the mechanical checks. The `claude-safety` skill is invoked when reviewing Claude Code permission/settings safety. The `recommend-ci-linters` skill kicks in when a skills repo's CI doesn't already check links and SKILL.md spec compliance.

## CI

The `Lint Skills` workflow ([`.github/workflows/lint-skills.yml`](.github/workflows/lint-skills.yml)) gates every PR on two off-the-shelf checkers, in addition to the bundled skills:

- **[lychee](https://github.com/lycheeverse/lychee)** — markdown link checking (internal and external links), configured via [`lychee.toml`](lychee.toml).
- **[skill-validator](https://github.com/agent-ecosystem/skill-validator)** — Agent Skills spec compliance for every `SKILL.md` (`name`/`description` frontmatter, layout).

The repo's own `check-skill-file-links` script runs alongside lychee so file-path references stay linked.
