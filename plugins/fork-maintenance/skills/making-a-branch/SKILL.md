---
name: making-a-branch
description: Whenever making a branch inside a forked repository (one with an upstream remote), use this skill.
---

# Making a Branch in a Fork Repo

When working in a fork repository, we want to distinguish a few kinds of branches:

1. `fork` is the branch that acts as your fork's default branch. It's where you keep work that is specific to your fork, and can contain commits from both your `personal/*` and `contrib/*` branches. It can also be rebased on top of upstream changes from the original repo's default branch as needed.
2. `personal/*` branches are for work that is personal to the fork and will never be shared back to the original repo. These can be used for experiments, prototypes, necessary changes to CICD for your own uses, personal features that will never be accepted upstream, or any other work that isn't intended to be contributed back. **These need to maintain a linear history** so that the fork branch can cleanly rebase upstream changes from the original repo as needed, but they don't need to be branched from upstream's default branch and can be branched from `fork` itself.
3. `contrib/*` branches are for work that is possible to be shared back to the original repo. It may or may not ever be approved, but you intend to contribute it. These are meant to be contributed both into your `fork` branch **AND** the original repo's default branch. **These have to be branched from upstream's default branch** and **maintain a linear history** in order to make clean contributions back to the original repo easier.

## Justification

The point of this naming scheme is correlation. Any branch in your fork that shares its name with a branch in the upstream repo should be treated as the "same branch" — the fork copy is a backup of, and a tracking point for, that upstream branch. This keeps updating from upstream simple and makes it obvious which fork branch corresponds to which upstream branch.

The `fork` branch is the case worth calling out specifically: always treat it as a **future-main** branch. It is what upstream's default branch *will become* once all of your in-flight `contrib/*` branches have been merged in. In other words, `fork` is meant to sit *slightly ahead of* `main` — it carries upstream plus your pending contributions.
