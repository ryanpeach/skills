# rg + fzf: first pass over a big tree

Install: `brew install ripgrep fzf` / `sudo apt-get install -y ripgrep fzf`

Goal: shrink "the whole repo" to a handful of files worth reading.

```bash
rg -l "PaymentProvider"              # which files mention it at all
rg -c "PaymentProvider" | sort -t: -k2 -rn | head   # which mention it most
rg -t py "def process_"              # scope by language
rg -i -C2 "retry"                    # case-insensitive, with context
rg -F 'foo(bar)'                     # literal string, no regex escaping
rg --hidden --no-ignore "SECRET"     # include dotfiles / gitignored files
```

- Hundreds of hits → pattern too broad: tighten with `-w` (whole words), `-t`/`--glob` (scope), before paging through noise.
- Zero hits on a term you *know* exists → it's split across lines, generated, or ignored: try `-U --multiline`, `--no-ignore --hidden`, or a shorter fragment.
- If your environment has a dedicated Grep tool backed by ripgrep, prefer it over shelling out; flags translate directly.

## fzf: fuzzy filename matching

Use filter mode (`--filter`/`-f`) — candidates on stdin, ranked matches on stdout. Never launch the interactive TUI.

```bash
rg --files | fzf --filter 'authsvc' | head   # best matches first
git ls-files | fzf -f 'usercntrlr'           # tolerates missing letters
```
