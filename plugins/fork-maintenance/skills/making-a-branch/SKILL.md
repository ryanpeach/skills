---
name: making-a-branch
description: Whenever making a branch inside a forked repository (one with an upstream remote), use this skill.
---

# Making a Branch in a Fork Repo

When working in a fork repository, we want to distinguish a few kinds of branches:

1. `fork` is the branch that acts as your forks default branch. It's where you keep work that is specific to your fork, and can contain merges from both your personal and feature branches. It can also merge upstream changes from the original repo's default branch as needed.
2. `fork/*` branches are for work that is personal to the fork and will never be shared back to the original repo. These can be used for experiments, prototypes, or any work that isn't intended to be merged back. **These need to maintain a linear history** so that the fork branch can cleanly merge upstream changes from the original repo as needed, but they don't need to be branched from upstream's default branch and can be branched from `fork` itself.
3. `feature/*` branches are for work that is possible to be shared back to the original repo. It may or may not ever be approved, but you intend to contribute it. These are meant to be merged both into your fork's personal or release branches and the original repo's default branch. **These have to be branched from upstream's default branch** and **maintain a linear history** in order to make clean merges back to the original repo easier.
