---
name: making-a-pr
description: Whenever making a PR inside a forked repository (one with an upstream remote), use this skill.
---

# Making a PR in a Fork Repository

## Feature Branch PRs

When you make a PR from a `feature/*` branch in your forked repo, you want to make 2 PRs:

1. A PR from your `feature/*` branch to the `fork` branch in your forked repo. This is a PR updates your own use of the project whether or not the upsteam accepts your contribution.
2. A PR from your `feature/*` branch to the `main` (or default) branch in the original repo. This is the PR that may or may not get accepted by the upstream maintainers, but it's good for getting feedback and code review from the maintainers and the community, and is necessary for your contribution to be merged back to the original repo.

## Fork Branch PRs

When you make a PR from a `fork/*` branch, you only need to make the PR to your own `fork` branch, since that work is not intended to be shared back to the original repo.