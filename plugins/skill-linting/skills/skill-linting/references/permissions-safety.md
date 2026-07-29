---
name: permissions-safety
description: Review .claude/settings.json for risky auto-allowed permissions. Use when auditing a Claude Code configuration for safety, or when asked to check that the agent cannot run code, delete files, reach the network, or read secrets without confirmation.
---

# Claude Safety

Check `.claude/settings.json` and `.claudeignore` (at all levels, home and project). Make sure that the agent can not do any of the following automatically:

1. Run any arbitrary code (e.g. via `python` or `bash` commands)
2. Delete any files or directories
3. Access any files outside of the project directory (e.g. via `cat /etc/passwd` or `ls ~`)
4. Make any network requests (e.g. via `curl` or `requests` library)
5. Install any new software on the system itself (e.g. via `apt install` or `brew install`)

And can not do any of the following ever:

1. Put any sensitive environment variables (e.g. `AWS_SECRET_KEY` or `DATABASE_URL`) into context, or read the `.env` file
2. Use `sudo`
3. Escape a sandbox

Help the user create a `.claudeignore` and a `settings.json` if not already existing or not following these rules.