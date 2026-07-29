---
name: searching
description: Always use before searching a codebase or docs. Picks the right tool.
---

# Searching Codebases and Docs

Most bad searches come from using the wrong tool: regex-grepping prose that doesn't share your vocabulary, or text-matching code patterns regex can't express. Pick by what you're searching, not by habit:

| Searching for... | Use |
|---|---|
| First look over many/unknown files; exact strings and identifiers | [rg](https://github.com/burntsushi/ripgrep) |
| A file or variable name by fuzzy/half-remembered name | [fzf](https://github.com/junegunn/fzf) |
| Code *structure* (call sites, patterns, refactors) | [ast-grep](https://github.com/ast-grep/ast-grep) |
| Natural language text, docs, comments, prose | [ck](https://github.com/BeaconBay/ck) |

You can also combine these tools via piping.

Ground rules:

- If a tool is missing (`command -v`), install it.
- Never launch interactive TUIs. There's no terminal for them.
- Report findings as `file:line` so they're actionable.
