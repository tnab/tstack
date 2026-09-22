# Maintaining Knowledge Stack

This repository is public. Keep all examples synthetic or drawn from cited public material. Do not commit credentials, private documents, internal URLs, customer information, personal filesystem paths, account configuration, or conversation exports.

The reusable instructions live in `skills/`. Keep them independent of a particular model, agent runtime, account, and local workspace. Treat tools and subagents as capabilities to discover, not guaranteed APIs.

The product name is Knowledge Stack and the repository, plugin, and main skill slug is `kstack`. Other skill names describe their function without a product prefix. The primary experience starts at `skills/kstack/SKILL.md`, which selects an on-demand playbook from `skills/kstack/playbooks/`. Playbooks own sequencing and completion checks; specialized skills own detailed procedures. Keep simple tasks proportionate and avoid loading every playbook.

Preserve prominent thanks to Lauren Tan and credit pstack's substantial architectural and instructional influence. Retain its full license notice and record upstream revisions in `THIRD_PARTY_NOTICES.md` and `references/sources.md`.

Keep the identity and version consistent across `plugin.json` and the Cursor, Claude Code, and Codex manifests. Validate changed manifests and skills. Do not claim runtime compatibility without testing it.

Every skill must explicitly load `references/principles.md`. Final prose follows `write`; avoid recursive skill calls. Keep the shared references and sibling skills available when packaging.

Use `skills/create-skill/SKILL.md` for new or revised skills and `skills/evaluate-skill/SKILL.md` to design behavioral checks. Update the main routing table, relevant playbooks, and README when supported workflows change. Do not claim a deferred capability is implemented.

Run `python3 scripts/validate.py` after edits. For workflow changes, run relevant synthetic cases from `evals/` with a fresh agent that has not seen the expected checks, then inspect its output. Treat those checks as limited evidence, not a claim of universal reliability.

Write concise, direct prose. Preserve factual qualifications and citations when editing. Keep the early scope focused; add instructions in response to demonstrated needs.
