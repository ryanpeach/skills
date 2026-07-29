---
name: refactoring
description: Always use before a mechanical refactor across multiple files or call sites. Picks the right tool.
---

# Mechanical Refactors

Hand-editing dozens of call sites is slow and error-prone. It's also not verifiable by the user without reading every instance, and lastly it costs tokens! Using simple regex/sed on code often breaks on formatting, line breaks, and lookalike strings. Here are a few better tools. Pick the approach by what's being refactored:

| Refactoring... | Use |
|---|---|
| A code pattern (call signature, API migration, idiom swap) | [ast-grep](https://github.com/ast-grep/ast-grep) |
| yaml, toml, json | [yq](https://github.com/mikefarah/yq) |
| Plain text (strings, config values, docs wording) | [gsed](https://formulae.brew.sh/formula/gnu-sed) |
| One or two sites | just edit them directly |

Ground rules:

- Install the right tool if you need to.
- Start from a clean working tree (commit or stash first) so a bad mass rewrite is one `git checkout` away from undone.
- Find every site first — search before you rewrite, so you know the expected match count. Zero or way-off counts mean the pattern is wrong, not the code. Use [rg](https://github.com/burntsushi/ripgrep) for this.
- Preview the diffs before applying (`sg` prints them by default; only then `--update-all`).
- Verify after: run the tests/build, and `rg` for stragglers the structural pattern couldn't catch (comments, docs, strings).

Typical flow: search for all sites → express the change as pattern + rewrite → preview → apply → test → sweep for leftovers.
