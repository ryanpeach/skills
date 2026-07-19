# ck: semantic search for markdown and prose

Install: `cargo install ck-search` (cargo-only for now; compiles from source, takes a few minutes — for a single quick lookup, `rg -i 'synonym1|synonym2'` may be the pragmatic fallback)

Regex quietly fails on prose: docs say "credentials" where you searched "auth". ck embeds file chunks and searches by meaning — the query is a description of what you want, not a string that must appear. Default choice for READMEs, design docs, ADRs, notes, runbooks; also works on code comments and docstrings.

```bash
ck --index .                                   # build the index once per tree
ck --sem "how deployments are rolled back" docs/
ck --sem --full-section "database migration strategy"   # whole sections, not lines
ck --hybrid "onboarding checklist" .           # semantic + keyword combined
ck --topk 5 --sem "error budget policy"        # cap result count
ck --json --sem "release process" docs/        # structured output
```

Choosing the mode:

- `--sem` — you know the concept, not the wording. Phrase the query as a short natural-language description ("how auth tokens get refreshed"), not keywords.
- `--hybrid` — you know one real term plus the concept; best default when unsure.
- No flag — grep-compatible (`-i`, `-n`, `-A`/`-B`, `-l` all work).

Index before the first semantic search and after large changes: `ck --status .` to check, `ck --clean .` to rebuild. If a full tree is too slow to index for a one-off question, scope it (`ck --index docs/`). Never launch `ck --tui`.
