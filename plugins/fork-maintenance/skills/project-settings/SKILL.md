---
name: project-settings
description: Whenever you need to check or update project settings related to a forked repository (one with an upstream remote), clone a forked repo, or fork a repo, or user asks advice about settings for a forked repo, use this skill.
---

# Project Settings for Forked Repositories

When working in a forked repository, there are some project settings that are important to check and update as needed to ensure a smooth workflow with the upstream repository. These include:

1. In github, make sure the default branch is set to `fork` instead of `main` or `master`. This is what users will see when they visit your repo, and this also will help protect your `main` or `master` branch from accidental commits or merges that could cause conflicts with the upstream repository (they need to stay in sync with the upstream default branch to make merging easier).
2. In github, make sure the branch protections for `fork` are set to require linear history and to require pull request reviews before merging.
3. In your local git config, make sure your `origin` remote points to your forked repository and your `upstream` remote points to the original repository. This will help you keep track of where you are pushing and pulling changes, and make it easier to sync changes from the upstream repository into your fork.
4. In your local git config, make sure to set the default strategy to rebase instead of merge. This will help maintain a cleaner commit history and make it easier to keep your fork in sync with the upstream repository without creating unnecessary merge commits. You can do this by running `git config --global pull.rebase true` or by setting it in your git config file directly.
