---
name: updating-from-upstream
description: Whenever you need to update a forked repository (one with an upstream remote) with changes from the upstream repository, use this skill.
---

# Updating a Fork from Upstream

1. First, checkout the default branch of the upstream repository (usually `main` or `master`) and pull the latest changes to make sure you have the most recent version of the upstream code. You can do this by running `git checkout main` (or `master`) followed by `git pull upstream main` (or `master`). Then push with `git push origin main` (or `master`) to update your fork's default branch with the latest changes from upstream. This will help ensure that your fork is up to date with the upstream repository, which will make it easier to create feature branches for contributions later on.
2. Next, checkout your `fork` branch in your forked repository. This is the branch that you use to keep your fork up to date with the upstream repository. You can do this by running `git checkout fork`.
3. The next step is potentially destructive, so I first recommend creating a `release/*` of your `fork` branch as backup. You can do this by running `git checkout -b release/<version>` while on the `fork` branch, and then pushing this new branch to your forked repository with `git push origin release/<version>`. This way, if anything goes wrong with the rebase in the next step, you have a backup of your `fork` branch that you can easily go back to.
4. Now, rebase your `fork` branch onto the upstream default branch. This will apply any changes from the upstream repository to the bottom of your `fork` branch's history, which will make it easier to see the difference between your changes and the upstream changes long term. You can do this by running `git rebase main` (or `master`) while on the `fork` branch. **You always want your `fork` branch to have a linear history on top of the upstream default branch.** Then push with `git push --force-with-lease origin fork`.