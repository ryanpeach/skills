# ast-grep rewrites

Install: `brew install ast-grep` / `cargo install ast-grep --locked` / `npm i -g @ast-grep/cli`

**Gotcha:** on Linux, `sg` is often the shadow-utils `setgroups` command. If `sg --version` doesn't identify ast-grep, use the `ast-grep` binary directly.

Patterns are code, not regex — write them the way the code would be written, and don't escape anything. Metavariables carry matched nodes from pattern to rewrite:

- `$NAME` — one node (an identifier, expression, argument)
- `$$$ARGS` — zero or more nodes (argument lists, statement bodies)

```bash
sg -p 'foo($A, $B)' -r 'bar($B, $A)' -l py                         # preview diffs
sg -p '$X.unwrap()' -r '$X.expect("checked")' -l rs                # preview
sg -p 'axios.get($URL)' -r 'fetch($URL)' -l ts src/ --update-all   # apply
```

Language via `-l` (js, ts, tsx, py, rs, go, java, ...). If a pattern matches nothing, it's usually not parseable code in isolation — simplify it to a complete expression or statement, then add back specifics.

## Constrained matches: YAML rules

When "match this pattern" isn't enough — only inside certain functions, only when an argument is a literal, everywhere *except* tests — use a rule file with `sg scan`:

```yaml
# rule.yml
id: no-print-in-lib
language: python
rule:
  pattern: print($$$ARGS)
  inside:
    kind: function_definition
    stopBy: end
fix: logger.info($$$ARGS)
```

```bash
sg scan -r rule.yml            # preview
sg scan -r rule.yml --update-all
```

Rules compose with `inside`, `has`, `not`, `all`, `any` — check `sg scan --help` and the ast-grep docs for the full vocabulary.

## Limits worth knowing

- Rewrites are per-node: ast-grep won't rename across files that merely *reference* the changed symbol (imports, docs, strings). Sweep with `rg` afterward.
- One language per run — repeat for each `-l` if the pattern spans e.g. `.ts` and `.tsx`.
- Semantic renames (scope-aware, collision-safe) are a language-server job; ast-grep matches syntax. For a plain identifier rename with a unique name, that distinction rarely matters — for overloaded names it does.
