#!/usr/bin/env python3
"""Simple local secret scanner for this skill repository."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_PATTERNS = {
    "github_pat": re.compile(r"github_pat_[A-Za-z0-9_]+"),
    "github_token": re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    "private_key": re.compile(r"-----BEGIN (RSA |EC |OPENSSH |DSA )?PRIVATE KEY-----"),
    "aws_access_key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "generic_api_key": re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{12,}['\"]"),
}

SKIP_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", ".venv", "venv"}
TEXT_SUFFIXES = {".md", ".txt", ".py", ".json", ".yaml", ".yml", ".toml", ".ini", ".cfg", ".html", ".css", ".js"}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if path.is_file() and (path.suffix.lower() in TEXT_SUFFIXES or path.name in {".gitignore", "LICENSE"}):
            yield path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", type=Path, default=Path.cwd())
    args = parser.parse_args()

    findings: list[tuple[str, int, str]] = []
    for path in iter_files(args.root):
        try:
            text = path.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for line_no, line in enumerate(text.splitlines(), start=1):
            for name, pattern in DEFAULT_PATTERNS.items():
                if pattern.search(line):
                    findings.append((str(path), line_no, name))

    if findings:
        print("Potential secrets found:")
        for file, line_no, name in findings:
            print(f"- {file}:{line_no} [{name}]")
        return 2

    print("No obvious secrets found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
