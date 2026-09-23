#!/usr/bin/env python3
"""Enforce the canonical Obsidian-template folder structure.

The declaration lives in `90. Settings/04 Index/folder-structure.json`. It is the
contract an adopting vault enforces against, so it must never drift from the tree
it claims to describe.

Two modes:

  --strict   The template's own self-check. The declaration and the tracked tree
             must match exactly in both directions, so a folder cannot be added
             or removed without updating the declaration.

  (default)  The adopter check. The numbered root set must match exactly, and
             every declared folder must exist. Extra subfolders are allowed:
             an adopting vault organizes its own content underneath the roots.

Not every adopter wants every root. A company vault has no use for a personal
devotional root, and forcing it to carry one would make "enforced" mean "cloned".
An adopter may therefore declare omissions in
`90. Settings/04 Index/folder-structure-exceptions.json`, each with a reason.
Omitting a folder covers everything beneath it. The declaration stays the
contract: an omission that nobody wrote down still fails, and an omission that
no longer matches reality is reported so the file cannot rot.

Exceptions never apply in --strict. The template cannot except itself from the
structure it publishes.

Dependency-free on purpose: a vault is not a Python project, and this has to run
in any adopter's CI without installing anything.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

DECLARATION = Path("90. Settings/04 Index/folder-structure.json")
EXCEPTIONS = Path("90. Settings/04 Index/folder-structure-exceptions.json")
NUMBERED_ROOT = re.compile(r"^\d+\. ")


def load_exceptions(root: Path) -> tuple[dict[str, str], list[str]]:
    """Return ({omitted path: reason}, errors). Absent file means no omissions."""
    path = root / EXCEPTIONS
    if not path.exists():
        return {}, []
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return {}, [f"malformed structure exceptions: {exc}"]

    omissions: dict[str, str] = {}
    errors: list[str] = []
    for entry in document.get("omissions", []):
        omitted = entry.get("path")
        reason = (entry.get("reason") or "").strip()
        if not omitted:
            errors.append("structure exception entry has no path")
            continue
        if not reason:
            errors.append(f"structure exception has no reason: {omitted}")
            continue
        omissions[omitted] = reason
    return omissions, errors


def is_omitted(path: str, omissions: dict[str, str]) -> bool:
    """An omitted folder covers everything beneath it."""
    if path in omissions:
        return True
    return any(path.startswith(f"{omitted}/") for omitted in omissions)


def tracked_folders(root: Path) -> tuple[set[str], set[str]]:
    """Return (roots, folders) derived from git's tracked tree."""
    result = subprocess.run(
        ["git", "-C", str(root), "ls-tree", "-r", "--name-only", "HEAD"],
        capture_output=True,
        text=True,
        check=True,
    )
    roots: set[str] = set()
    folders: set[str] = set()
    for path in result.stdout.splitlines():
        parts = path.split("/")
        if not NUMBERED_ROOT.match(parts[0]):
            continue
        roots.add(parts[0])
        for index in range(1, len(parts)):
            folders.add("/".join(parts[:index]))
    return roots, folders


def present_roots(root: Path) -> set[str]:
    return {
        entry.name
        for entry in root.iterdir()
        if entry.is_dir() and NUMBERED_ROOT.match(entry.name)
    }


def verify(root: Path, strict: bool) -> list[str]:
    declaration_path = root / DECLARATION
    if not declaration_path.exists():
        return [f"missing structure declaration: {DECLARATION}"]
    try:
        declared = json.loads(declaration_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"malformed structure declaration: {exc}"]

    errors: list[str] = []
    declared_roots = set(declared.get("roots", []))
    declared_folders = set(declared.get("folders", []))
    if not declared_roots:
        errors.append("structure declaration lists no roots")

    if strict:
        omissions: dict[str, str] = {}
        if (root / EXCEPTIONS).exists():
            errors.append("the template may not except itself from its own structure")
    else:
        omissions, exception_errors = load_exceptions(root)
        errors.extend(exception_errors)
        for omitted in sorted(omissions):
            if omitted not in declared_roots and omitted not in declared_folders:
                errors.append(f"structure exception names an undeclared path: {omitted}")
            elif (root / omitted).is_dir():
                errors.append(f"structure exception is stale, the path exists: {omitted}")

    expected_roots = {name for name in declared_roots if not is_omitted(name, omissions)}

    actual_roots = present_roots(root)
    for name in sorted(actual_roots - expected_roots):
        errors.append(f"undeclared numbered root: {name}")
    for name in sorted(expected_roots - actual_roots):
        errors.append(f"missing declared root: {name}")

    for folder in sorted(declared_folders):
        if is_omitted(folder, omissions):
            continue
        if not (root / folder).is_dir():
            errors.append(f"missing declared folder: {folder}")

    if strict:
        tree_roots, tree_folders = tracked_folders(root)
        for name in sorted(tree_roots - declared_roots):
            errors.append(f"tracked root absent from declaration: {name}")
        for name in sorted(declared_roots - tree_roots):
            errors.append(f"declared root absent from tracked tree: {name}")
        for folder in sorted(tree_folders - declared_folders):
            errors.append(f"tracked folder absent from declaration: {folder}")
        for folder in sorted(declared_folders - tree_folders):
            errors.append(f"declared folder absent from tracked tree: {folder}")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".", help="vault root (default: current directory)")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="require the declaration and the tracked tree to match exactly",
    )
    args = parser.parse_args()

    root = Path(args.root).resolve()
    errors = verify(root, args.strict)
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        print(f"folder structure verification failed: {len(errors)} problem(s)")
        return 1

    declared = json.loads((root / DECLARATION).read_text(encoding="utf-8"))
    omissions, _ = ({}, []) if args.strict else load_exceptions(root)
    summary = (
        "folder structure verified: "
        f"{len(declared['roots'])} roots, {len(declared['folders'])} folders"
    )
    if omissions:
        summary += f", {len(omissions)} declared omission(s)"
    print(summary)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
