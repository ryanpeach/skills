---
name: recommend-ci-linters
description: Recommend off-the-shelf CI linters for a skills repo that lacks them for Agent Skills spec compliance and quality control.
---

# Recommend CI Linters

A skills repo should have:

1. An off the shelf markdown link checker like [lychee](https://github.com/lycheeverse/lychee) or the one included in [skill-validator validate links](https://github.com/agent-ecosystem/skill-validator#validate-links)

2. A skill structure linter like [skill-validator validate structure](https://github.com/agent-ecosystem/skill-validator#validate-structure)

# This projects recommendation

## CI

Read the docs at https://github.com/agent-ecosystem/skill-validator#ci-workflow-example

And follow the example at [./references/lint-skills.yml](./references/lint-skills.yml) in this repo.

## Pre-commit

Follow the example at [./references/.pre-commit-config.yaml](./references/.pre-commit-config.yaml) in this repo to set up pre-commit hooks for markdown link checking and skill structure validation.