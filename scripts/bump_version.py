#!/usr/bin/env python3
"""Bump the version of a Claude Code plugin marketplace and all of its plugins.

The marketplace's ``metadata.version`` is the single source of truth. Every
``plugins/*/.claude-plugin/plugin.json`` is kept in lockstep with it, so a
release always publishes one coherent ``MAJOR.MINOR.PATCH`` version.

Usage:
    scripts/bump_version.py --bump patch
    scripts/bump_version.py --bump minor --dry-run
    scripts/bump_version.py --set 1.2.3

The new version is printed to stdout. ``--dry-run`` reports the files that
would change without writing them.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import NoReturn

SEMVER_RE = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
MARKETPLACE_REL = Path(".claude-plugin/marketplace.json")
PLUGIN_GLOB = "plugins/*/.claude-plugin/plugin.json"
DEFAULT_ROOT = Path(__file__).resolve().parent.parent


def die(message: str) -> NoReturn:
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_semver(value: str, source: str) -> tuple[int, int, int]:
    match = SEMVER_RE.match(value or "")
    if not match:
        die(f"{source}: {value!r} is not a MAJOR.MINOR.PATCH version")
    return int(match.group(1)), int(match.group(2)), int(match.group(3))


def bump_version(version: str, part: str) -> str:
    major, minor, patch = parse_semver(version, "current version")
    if part == "major":
        return f"{major + 1}.0.0"
    if part == "minor":
        return f"{major}.{minor + 1}.0"
    if part == "patch":
        return f"{major}.{minor}.{patch + 1}"
    die(f"unknown bump part: {part}")


def read_json(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except FileNotFoundError:
        die(f"missing file: {path}")
    except json.JSONDecodeError as exc:
        die(f"{path}: invalid JSON ({exc})")


def write_json(path: Path, data: dict, dry_run: bool) -> bool:
    """Write ``data`` if it differs from the file. Returns True when changed."""
    original = path.read_text(encoding="utf-8")
    updated = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    if updated == original:
        return False
    if not dry_run:
        path.write_text(updated, encoding="utf-8")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--bump", choices=["major", "minor", "patch"])
    group.add_argument("--set", dest="set_version", metavar="X.Y.Z")
    parser.add_argument(
        "--current",
        metavar="X.Y.Z",
        help="base version for --bump (default: marketplace version)",
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=DEFAULT_ROOT,
        help="repository root (default: parent of this script's directory)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="report changes without writing files",
    )
    args = parser.parse_args()
    if args.current is not None and args.set_version is not None:
        parser.error("--current cannot be combined with --set")

    root = args.root.resolve()
    marketplace_path = root / MARKETPLACE_REL
    marketplace = read_json(marketplace_path)
    metadata = marketplace.setdefault("metadata", {})
    current = metadata.get("version")
    if not isinstance(current, str):
        die(f"{marketplace_path}: missing metadata.version")

    if args.set_version is not None:
        parse_semver(args.set_version, "--set")
        new_version = args.set_version
    else:
        base = current
        if args.current is not None:
            base = args.current
            parse_semver(base, "--current")
        new_version = bump_version(base, args.bump)

    changed: list[Path] = []

    metadata["version"] = new_version
    if write_json(marketplace_path, marketplace, args.dry_run):
        changed.append(marketplace_path.relative_to(root))

    plugin_paths = sorted(root.glob(PLUGIN_GLOB))
    if not plugin_paths:
        die(f"no plugin manifests matched {PLUGIN_GLOB}")

    for plugin_path in plugin_paths:
        plugin = read_json(plugin_path)
        plugin["version"] = new_version
        if write_json(plugin_path, plugin, args.dry_run):
            changed.append(plugin_path.relative_to(root))

    verb = "would update" if args.dry_run else "updated"
    for path in changed:
        print(f"{verb}: {path}", file=sys.stderr)
    print(new_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
