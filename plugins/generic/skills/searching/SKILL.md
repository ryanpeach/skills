---
name: searching
description: Always use before searching a codebase or docs. Picks the right tool - rg, fzf, ast-grep, or ck.
---

# Searching Codebases and Docs

Most bad searches come from using the wrong tool: regex-grepping prose that doesn't share your vocabulary, or text-matching code patterns regex can't express. Pick by what you're searching, not by habit:

| Searching for... | Use |
|---|---|
| First look over many/unknown files; exact strings and identifiers | `rg` |
| A file by fuzzy/half-remembered name | `fzf --filter` |
| Code *structure* (call sites, patterns, refactors) | `sg` (ast-grep) |
| Markdown, docs, comments, prose | `ck --sem` |

Before using a tool for the first time this session, read its reference:

- `references/rg-fzf.md` — first-pass mapping, narrowing flags, fuzzy filename matching
- `references/ast-grep.md` — pattern syntax, metavariables, structural rewrites
- `references/ck.md` — indexing, semantic vs. hybrid mode, query phrasing

Ground rules:

- If a tool is missing (`command -v`), install it — each reference has install commands. Fall back to rg approximations only when installing is impossible.
- Never launch interactive TUIs (bare `fzf`, `ck --tui`); there's no terminal for them.
- Start cheap: `rg -l` to gauge blast radius, then narrow, then read. Search narrows; reading confirms.
- Report findings as `file:line` so they're actionable.

Typical flow for "find where X happens": map candidates with rg/fzf → pinpoint with sg (code pattern) or ck (described in prose) → read the few files that survive.
