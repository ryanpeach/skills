---
name: refactoring
description: Always use before a mechanical refactor across multiple files or call sites. Picks the right tool - ast-grep rewrites over regex/sed.
---

# Mechanical Refactors

Hand-editing dozens of call sites is slow and error-prone; regex/sed on code breaks on formatting, line breaks, and lookalike strings. Pick the approach by what's changing:

| Changing... | Use |
|---|---|
| A code pattern (call signature, API migration, idiom swap) | `sg -p ... -r ...` (ast-grep) |
| Plain text (strings, config values, docs wording) | `rg -l` + Edit, or `sed` |
| One or two sites | just edit them directly |

Before rewriting with ast-grep for the first time this session, read `references/ast-grep-rewrite.md` (pattern syntax, metavariables, YAML rules for constrained matches).

Ground rules:

- Start from a clean working tree (commit or stash first) so a bad mass rewrite is one `git checkout` away from undone.
- Find every site first — search before you rewrite, so you know the expected match count. Zero or way-off counts mean the pattern is wrong, not the code.
- Preview the diffs before applying (`sg` prints them by default; only then `--update-all`).
- Verify after: run the tests/build, and `rg` for stragglers the structural pattern couldn't catch (comments, docs, strings).

Typical flow: search for all sites → express the change as pattern + rewrite → preview → apply → test → sweep for leftovers.
