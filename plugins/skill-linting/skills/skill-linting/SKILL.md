---
name: skill-linting
description: Miscellaneous guidelines for skill linting that don't fit into other categories.
---

# Skill Linting

If provided a github PR as an argument. Pull that PR's diff. Only dynamically review skills changed in the diff. Modify the following instructions as needed.

## Length

Skills should be short and to the point (usually < 50 lines), and follow progressive disclosure via a `./references` folder.

## MCPs

Try to enforce doctests as much as possible, especially in MCPs where the docstrings become context for the agent.

MCPs should not return raw data structures that require the agent to inspect the output before it knows what it will be. They should return simple strings or structs that can be easily converted to a complete JSON schema and shown to the agent via `get_schema`.

## Structure

### Skill asset isolation

Skills must not hardcode paths outside their own directory. External files are exposed to the skill via symlinks in `skills/{skill}/assets/`:

```
skills/scan/assets/portals.yml -> ../../../personal/portals.yml
skills/scan/assets/search.yml  -> ../../../personal/search.yml
```

Use symlinks from an external file to a file in the skill if a file is needed in more than one skill.

### Scripts

Executable scripts live in `skills/{skill}/scripts/`. They must be self-contained, runnable directly, and accept all external paths as CLI options with sensible defaults.

#### Python UV scripts

Standalone scripts use uv inline script metadata so they run with no manual venv:

```python
#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = ["pydantic>=2", "pyyaml>=6", "typer>=0.12"]
# ///
```

We do this so skills can be exported from the repo as self-contained units with no external setup.

ALSO add the dependencies to the root `pyproject.toml` if it exists so they are available in the venv for linting.

#### Javascript

For JS bins we recommend either:

1. using `.cjs` extension without any libraries.
2. Using [deno](https://docs.deno.com/runtime/fundamentals/node/) so that dependencies can be imported directly in the script and run with `deno run` with no manual setup.

# Finally

Run all the skills in [references](./references/)

* [Check Skill Nonlinks](./references/check-skill-nonlinks.md)
* [Detect Skill Contradictions/Duplications](./references/detect-skill-contradictions-duplications.md)
* [Permissions Safety](./references/permissions-safety.md)
* [Recommended CI Linters](./references/recommend-ci-linters.md)