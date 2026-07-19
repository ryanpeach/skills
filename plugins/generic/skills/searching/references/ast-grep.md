# ast-grep (sg): structural code search

Install: `brew install ast-grep` / `cargo install ast-grep --locked` / `npm i -g @ast-grep/cli`

**Gotcha:** on Linux, `sg` is often the shadow-utils `setgroups` command. If `sg --version` doesn't identify ast-grep, use the `ast-grep` binary directly.

ast-grep matches patterns against the AST, so formatting and whitespace don't matter. Patterns are code, not regex — write them the way the code would be written, and don't escape anything. Metavariables:

- `$NAME` — one node (an identifier, expression, argument)
- `$$$ARGS` — zero or more nodes (argument lists, statement bodies)

```bash
sg -p 'console.log($$$ARGS)' -l js src/   # every console.log, any args
sg -p 'requests.get($URL)' -l py          # calls with exactly one arg
sg -p 'if $COND: return $VAL' -l py       # structural, not textual
sg -p 'useEffect($FN, [])' -l tsx src/    # framework patterns
```

Language via `-l` (js, ts, tsx, py, rs, go, java, ...). `--json` for machine-readable matches. If a pattern matches nothing, it's usually not parseable code in isolation — simplify it to a complete expression or statement.

Structural find-and-replace — the safe way to plan a mechanical refactor:

```bash
sg -p 'foo($A, $B)' -r 'bar($B, $A)' -l py                         # preview diffs
sg -p '$X.unwrap()' -r '$X.expect("checked")' -l rs --update-all   # apply
```

Preview before `--update-all`, always.

Good workflow: `rg -l` to find candidate files cheaply, then run the precise structural query over just those.
