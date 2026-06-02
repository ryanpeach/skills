---
name: updating-from-upstream
description: Whenever you need to update a forked repository (one with an upstream remote) with changes from the upstream repository, use this skill.
---

# Updating a Fork from Upstream

1. First, checkout the default branch of the upstream repository (usually `main` or `master`) and pull the latest changes to make sure you have the most recent version of the upstream code. You can do this by running `git checkout main` (or `master`) followed by `git pull upstream main` (or `master`).
2. Next, checkout your `fork` branch in your forked repository. This is the branch that you use to keep your fork up to date with the upstream repository. You can do this by running `git checkout fork`.
3. Now, rebase your `fork` branch onto the upstream default branch. This will apply any changes from the upstream repository to the bottom of your `fork` branch's history, which will make it easier to see the difference between your changes and the upstream changes long term. You can do this by running `git rebase main` (or `master`) while on the `fork` branch. **You always want your `fork` branch to have a linear history on top of the upstream default branch.**