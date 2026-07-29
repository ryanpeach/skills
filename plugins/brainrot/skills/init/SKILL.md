---
name: init
description: Initializes the brainrot style into the users personal settings on a project.
---

# Style

Make sure the user has their [outputStyle](https://code.claude.com/docs/en/output-styles#change-your-output-style) set to `brainrot`. Use `.claude/settings.local.json` and make sure its gitignored.

# Instructions

Add the following instructions to the `CLAUDE.local.md` (make sure it's gitignored too):

- The LLM is not allowed to co-author a commit, or create a commit message, and the user must take full responsibility for a PR.
- The LLM is not allowed to write documentation.
  - The LLM should identify missing or outdated documentation and alert the user.
- The LLM is not allowed to directly edit code.
  - The LLM should provide small (function sized) snippets, templates, documentation links, etc, like a google search or stack overflow search would.
  - The LLM may use skills in the brainrot plugin to suppliment not being able to edit, like the `refactoring` skill which uses bash tools for deterministic edits.
- The LLM should not fix bugs pasted in.
  - It should highlight the most important parts of a stack trace or stderr so that the user doesn't have to scan lots of messages on an error.
  - It should search for documentation, issues, and lines of code in the source that echo the given error message and link them to the user

# Rules

**Do this last so you don't lose edit permissions until the end.**

Add the following to the `settings.local.json`:

- `Deny`
  - `Edit(*)` - We don't allow the agent to directly edit things. The user does that themselves.
  - `Bash(git commit -m *)` - The user writes their own commit messages
