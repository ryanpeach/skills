# ryanpeach skills

Claude Code plugin marketplace aggregating Ryan Peach's plugins.

## Install

```
/plugin marketplace add ryanpeach/skills
/plugin install brainrot@ryanpeach
/plugin install skill-linting@ryanpeach
/plugin install fork-maintenance@ryanpeach
```

## Releasing

Releases are cut automatically when a pull request is merged into `main`.
The bump comes from the PR's labels (highest wins):

| Label | Bump | Example |
| --- | --- | --- |
| `major` | `MAJOR.0.0` | 0.1.0 -> 1.0.0 |
| `minor` | `X.MINOR.0` | 0.1.0 -> 0.2.0 |
| `patch` (default) | `X.Y.PATCH` | 0.1.0 -> 0.1.1 |

On merge the `Release` workflow bumps `.claude-plugin/marketplace.json` and
every `plugins/*/.claude-plugin/plugin.json` in lockstep, merges the bump
through a `release/vX.Y.Z` PR (required by the `main` ruleset), tags the merge
commit, and publishes a GitHub Release. PRs from forks require a
`RELEASE_TOKEN` secret with `contents: write` and `pull-requests: write`.

To bump versions locally, run `python3 scripts/bump_version.py --bump patch`
(add `--dry-run` to preview).

## Plugins

* **brainrot** - My default coding skill. Prevents me from losing my skills when using AI while coding. Prioritizes:
  * Allows the user to use cheaper models.
  * No major additional code review burden.
  * Edits are done by the user.
* **skill-linting** - Lints claude skills for styleguide stuff.
* **fork-maintenance** - My standards for working on a fork.