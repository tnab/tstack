#!/usr/bin/env python3
"""Check Knowledge Stack's metadata, skill headers, playbooks, and local links.

This is a structural check, not a full client schema or behavioral validator.
Run from any directory with Python 3.9 or later.
"""

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def local_links(path):
    """Return local Markdown link targets, excluding anchors and URLs."""
    for target in re.findall(r"\]\(([^)]+)\)", path.read_text()):
        target = target.strip("<>")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        yield target.split("#", 1)[0]


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
        for target in local_links(path):
            if Path(target).is_absolute():
                errors.append(f"{path.relative_to(ROOT)}: absolute local link")
            elif not (path.parent / target).exists():
                errors.append(f"{path.relative_to(ROOT)}: broken link {target}")

    router = ROOT / "skills/kstack/SKILL.md"
    playbooks = set((router.parent / "playbooks").glob("*.md"))
    if not router.is_file():
        errors.append("Missing entry skill: skills/kstack/SKILL.md")
    elif not playbooks:
        errors.append("No entry skill playbooks found")
    else:
        reachable = set()
        pending = [router.resolve()]
        while pending:
            path = pending.pop()
            if path in reachable:
                continue
            reachable.add(path)
            for target in local_links(path):
                linked = (path.parent / target).resolve()
                if (linked.is_file() and linked.suffix == ".md"
                        and ROOT in linked.parents and linked not in reachable):
                    pending.append(linked)
        for path in sorted(playbooks):
            if path.resolve() not in reachable:
                errors.append(f"Unreachable playbook: {path.relative_to(ROOT)}")

    cases_path = ROOT / "evals/cases.json"
    cases = []
    try:
        cases = json.loads(cases_path.read_text())
        if not isinstance(cases, list):
            raise ValueError("cases must be a list")
        ids = set()
        for index, case in enumerate(cases):
            label = f"evals/cases.json case {index + 1}"
            if not isinstance(case, dict):
                errors.append(f"{label}: must be an object")
                continue
            malformed = False
            for field in ("id", "skill", "request"):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    errors.append(f"{label}: {field} must be a nonempty string")
                    malformed = True
            for field in ("fixtures", "checks"):
                value = case.get(field)
                if not isinstance(value, list) or not all(
                        isinstance(item, str) and item.strip() for item in value):
                    errors.append(f"{label}: {field} must be a list of nonempty strings")
                    malformed = True
            if not case.get("checks"):
                errors.append(f"{label}: must have at least one expected check")
            if case.get("workspace", "read-only") not in ("read-only", "scratch-copy"):
                errors.append(f"{label}: unknown workspace mode")
            if malformed:
                continue
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
    print(f"Validated 4 manifests, {len(skills)} skill headers, {len(playbooks)} reachable playbooks, local links, and {len(cases)} evaluation cases.")
    return 0


if __name__ == "__main__":
    sys.exit(validate())
