#!/usr/bin/env python3
"""Check tstack's package metadata, skill headers, and local Markdown links.

This is a structural check, not a full client schema or behavioral validator.
Run from any directory with Python 3.9 or later.
"""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def validate():
    errors = []
    manifests = {}
    for name in (
        "plugin.json",
        ".cursor-plugin/plugin.json",
        ".claude-plugin/plugin.json",
        ".codex-plugin/plugin.json",
    ):
        try:
            value = json.loads((ROOT / name).read_text())
            if not isinstance(value, dict):
                raise ValueError("manifest must be an object")
            manifests[name] = value
        except (OSError, ValueError) as exc:
            errors.append(f"{name}: {exc}")

    portable = manifests.get("plugin.json", {})
    if portable.get("$schema") != "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json":
        errors.append("plugin.json: missing Agent Plugins schema identifier")
    for key in ("name", "version", "repository", "license"):
        expected = portable.get(key)
        if not isinstance(expected, str) or not expected.strip():
            errors.append(f"plugin.json: missing {key}")
        for name, manifest in manifests.items():
            if manifest.get(key) != expected:
                errors.append(f"{name}: {key} differs from plugin.json")

    skills = sorted((ROOT / "skills").glob("*/SKILL.md"))
    if not skills:
        errors.append("No skills found")
    for path in skills:
        text = path.read_text()
        front = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        label = path.relative_to(ROOT)
        if not front:
            errors.append(f"{label}: missing frontmatter")
            continue
        name = re.search(r"^name:\s*(\S+)\s*$", front.group(1), re.M)
        if not name or name.group(1).strip("\"'") != path.parent.name:
            errors.append(f"{label}: name must match directory")
        description = re.search(r"^description:\s*(.+)$", front.group(1), re.M)
        if not description or not 1 <= len(description.group(1)) <= 1024:
            errors.append(f"{label}: missing or oversized single-line description")
        if "../../references/principles.md" not in text:
            errors.append(f"{label}: shared principles are not linked")

    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.relative_to(ROOT).parts:
            continue
        for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
            target = target.strip("<>")
            if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
                continue
            local = target.split("#", 1)[0]
            if Path(local).is_absolute():
                errors.append(f"{path.relative_to(ROOT)}: absolute local link")
            elif not (path.parent / local).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")

    cases_path = ROOT / "evals/cases.json"
    try:
        cases = json.loads(cases_path.read_text())
        ids = set()
        for case in cases:
            if case["id"] in ids:
                errors.append(f"Duplicate evaluation case: {case['id']}")
            ids.add(case["id"])
            if not (ROOT / "skills" / case["skill"] / "SKILL.md").is_file():
                errors.append(f"Unknown evaluation skill: {case['skill']}")
            for fixture in case["fixtures"]:
                if not (ROOT / "evals" / fixture).is_file():
                    errors.append(f"Missing evaluation fixture: {fixture}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"evals/cases.json: {exc}")

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated 4 manifests, {len(skills)} skill headers, local links, and {len(cases)} evaluation cases.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
