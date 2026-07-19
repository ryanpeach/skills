---
name: searching
description: How to search codebases and documentation effectively by picking the right tool for the job - rg and fzf for a fast first pass over big sets of files, ast-grep (sg) for structure-aware code search, and ck for semantic search over markdown and prose. Use this skill whenever you are about to search a repository for anything - finding where something is defined or used, locating a file by half-remembered name, hunting through docs or markdown notes, planning a refactor across many call sites, or exploring an unfamiliar codebase. Even a simple "grep for X" request benefits from this skill's tool selection.
---

# Searching Codebases and Docs

Four tools, four different strengths. Most bad searches come from using the wrong tool: regex-grepping prose that doesn't share your vocabulary, or text-matching code patterns that regex can't express. Pick by what you're searching, not by habit.

| Searching for... | Use | Why |
|---|---|---|
| A first look over many/unknown files | `rg`, `fzf --filter` | Fastest way to map territory and narrow scope |
| Exact strings, identifiers, log messages | `rg` | Literal/regex match is exactly the right semantics |
| Code *structure* (call sites, patterns, refactors) | `sg` (ast-grep) | Matches the AST, immune to formatting/whitespace |
| Markdown, docs, comments, prose | `ck --sem` / `ck --hybrid` | Prose rarely uses your exact words; semantic search finds meaning |
| A file by fuzzy/half-remembered name | `fzf --filter` | Fuzzy ranking beats guessing regexes |

Rules of thumb: **markdown → ck. code structure → sg. first pass over a big tree → rg and fzf.** Prefer the specialized tool — it usually turns several failed grep attempts into one good query.

## Missing tools: install them

Check availability with `command -v rg ck ast-grep fzf` before assuming. If a tool this skill calls for is missing, install it rather than settling for a worse search — installation takes seconds and pays for itself on the first query:

```bash
# rg (ripgrep)
brew install ripgrep        # macOS
sudo apt-get install -y ripgrep   # Debian/Ubuntu

# ast-grep (binary is `ast-grep`; often aliased to `sg`)
brew install ast-grep
cargo install ast-grep --locked
npm i -g @ast-grep/cli

# fzf
brew install fzf
sudo apt-get install -y fzf

# ck (cargo only for now; crate is ck-search, binary is ck)
cargo install ck-search
```

Pick whichever package manager the system already has (`brew`, `apt-get`, `cargo`, `npm`). If installation genuinely isn't possible — no network, no package manager, no permission to install — fall back to `rg` approximations: keyword/synonym searches (`rg -i 'rollback|revert'`) in place of ck, and text patterns over `rg -l` shortlists in place of sg. Note `cargo install` compiles from source and can take a few minutes; that's still usually worth it for ck on a docs-heavy task, but for a single quick lookup the rg fallback is reasonable.

## First look: rg + fzf

When you don't yet know where things live, start broad and cheap. Goal: shrink "the whole repo" down to a handful of files worth reading.

```bash
rg -l "PaymentProvider"              # which files mention it at all
rg -c "PaymentProvider" | sort -t: -k2 -rn | head   # which files mention it most
rg -t py "def process_"              # scope by language
rg -i -C2 "retry"                    # case-insensitive, with context
rg -F 'foo(bar)'                     # -F = literal string, no regex escaping
rg --hidden --no-ignore "SECRET"     # include dotfiles / gitignored files
```

Useful habits:
- Start with `-l` (files only) to gauge the blast radius before dumping matches into context. Hundreds of hits means your pattern is too broad — tighten it (`-w` for whole words, `-t`/`--glob` to scope) rather than paging through noise.
- Zero hits on a term you *know* exists usually means it's split across lines, generated, or in an ignored file. Try `-U --multiline`, `--no-ignore --hidden`, or search a shorter fragment.
- If your environment provides a dedicated Grep tool backed by ripgrep, prefer it over shelling out to `rg` for these searches; the flags translate directly.

For finding *files* rather than contents, fzf's non-interactive filter mode ranks candidates by fuzzy match — ideal when you only half-remember a name:

```bash
rg --files | fzf --filter 'authsvc' | head        # best matches first
git ls-files | fzf -f 'usercntrlr'                # tolerates missing letters
```

Never launch fzf's interactive TUI (or `ck --tui`) from an agent session — there's no terminal for it. `--filter`/`-f` is the scriptable mode: candidates on stdin, ranked matches on stdout.

## Code: ast-grep (sg)

Once the question is about code *structure* — "all call sites of X", "everywhere we `await` inside a loop", "this pattern but with any argument" — switch from text matching to AST matching. ast-grep parses the code and matches patterns against the tree, so formatting, line breaks, and whitespace don't matter, and you can capture "any expression here" with metavariables:

- `$NAME` matches one node (an identifier, an expression, an argument)
- `$$$ARGS` matches zero or more nodes (argument lists, statement bodies)

```bash
sg -p 'console.log($$$ARGS)' -l js src/          # every console.log, any args
sg -p 'requests.get($URL)' -l py                  # calls with exactly one arg
sg -p 'if $COND: return $VAL' -l py               # structural, not textual
sg -p 'useEffect($FN, [])' -l tsx src/            # framework patterns
```

The pattern is code, not regex — write it the way the code would be written, and don't escape anything. If a pattern mysteriously matches nothing, it's usually not valid parseable code for that language in isolation; simplify it to a complete expression or statement.

ast-grep also does structural find-and-replace, which is the safe way to plan a mechanical refactor:

```bash
sg -p 'foo($A, $B)' -r 'bar($B, $A)' -l py        # preview rewrites as diffs
sg -p '$X.unwrap()' -r '$X.expect("checked")' -l rs --update-all   # apply
```

Preview before `--update-all`, always. `--json` gives machine-readable matches when you need to post-process.

**Gotcha:** on Linux, `sg` is often the shadow-utils `setgroups` command. If `sg --version` doesn't identify ast-grep, use the `ast-grep` binary directly. Language must be given via `-l` (js, ts, tsx, py, rs, go, java, ...) or inferred from `--globs`.

A good workflow is rg-then-sg: use `rg -l` to find the candidate files cheaply, then run the precise structural query over just those.

## Markdown and prose: ck

Prose is where regex search quietly fails: docs say "credentials" where you searched "auth", "retries" where you searched "backoff". ck is a semantic grep — it embeds file chunks and searches by meaning, so the query is a description of what you want, not a string that must literally appear. This makes it the default for markdown: READMEs, design docs, ADRs, notes, runbooks.

```bash
ck --index .                                   # build the index once per tree
ck --sem "how deployments are rolled back" docs/
ck --sem --full-section "database migration strategy"   # whole sections, not lines
ck --hybrid "onboarding checklist" .           # semantic + keyword combined
ck --topk 5 --sem "error budget policy"        # cap result count
ck --json --sem "release process" docs/        # structured output
```

How to choose the mode:
- `--sem` — you know the concept, not the wording. Phrase the query as a short natural-language description ("how auth tokens get refreshed"), not keywords.
- `--hybrid` — you know one real term plus the concept; best default when unsure.
- No flag — ck behaves like grep (`-i`, `-n`, `-A`/`-B`, `-l` all work), so it's fine for exact matches in the same tree too.

Index notes: run `ck --index .` before the first semantic search and after large changes (`ck --status .` to check, `ck --clean .` to rebuild). If indexing a huge tree is too slow for a one-off question, scope it (`ck --index docs/`) or fall back to a few `rg -i` synonym searches (`rg -i 'rollback|revert|roll back' docs/`).

ck works on code comments and docstrings too — "where do we explain the caching strategy" is a semantic query even when the answer lives in a `.py` file.

## Putting it together

For a typical "find where X happens in this unfamiliar repo" task:

1. **Map**: `rg -l` / `rg -c` a couple of distinctive terms; `fzf --filter` if you're guessing at file names. Get down to a shortlist of files/dirs.
2. **Pinpoint**: if X is a code pattern, express it as an `sg` pattern over the shortlist. If X is described in docs, ask `ck --sem` over `docs/` and markdown.
3. **Read**: open the few files that survived. Search narrows; reading confirms.

Report findings with `file:line` references so they're actionable. If two tools disagree — rg finds nothing but ck finds a doc section — trust the reading, not the tool: open the file and verify.
