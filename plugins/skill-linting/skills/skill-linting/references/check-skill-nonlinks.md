---
name: check-skill-nonlinks
description: Ensure every file path mentioned in a skill's markdown is a real markdown link to an existing file, so linters can verify references.
---

# Check Skill File Links

Skill docs reference other files constantly: sibling `SKILL.md`s, bin scripts, asset symlinks, external standards. If those references are bare backticks or plain text, nothing catches it when the target gets renamed or deleted. Making every path a real markdown link turns "did I break a reference?" into a fast, mechanical check.

Once this is in place, you can run a linter like [lychee](https://github.com/lycheeverse/lychee) to automatically verify links.

## The rule

Every file path mentioned in markdown must be a proper markdown link so linters can verify it exists:

```markdown
<!-- wrong -->
See `STYLEGUIDE.md` for conventions.

<!-- right -->
See [STYLEGUIDE.md](STYLEGUIDE.md) for conventions.
```

The exception is filenames that are referencing a *type* of file, not a specific file. For example, `SKILL.md` might refer to a specific file OR to the general type of file that all skills have. In the first case, it should be a link. In the second, it should not. If it should be a link, prefer [`./SKILL.md`](./SKILL.md) to be explicit that it's referring to the file in the current directory.

## How to check

Scan the skill using `grep` for

```re
`[^`]*\.[^`]*`
```

to find things inside a `` block that look like a file.
