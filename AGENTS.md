# Maintaining tstack

This repository is public. Keep all examples synthetic or drawn from cited public material. Do not commit credentials, private documents, internal URLs, customer information, personal filesystem paths, account configuration, or conversation exports.

The reusable instructions live in `skills/`. Keep them independent of a particular model, agent runtime, account, and local workspace. Treat tools and subagents as capabilities to discover, not guaranteed APIs.

Preserve Lauren Tan's pstack attribution and license notice when adapting upstream work. Record the upstream revision in `THIRD_PARTY_NOTICES.md`.

Keep the identity and version consistent across `plugin.json` and the Cursor, Claude Code, and Codex manifests. Validate changed manifests and skills. Do not claim runtime compatibility without testing it.

Every skill must explicitly load `references/principles.md`. Final prose follows `write`; avoid recursive skill calls. Keep the shared references and sibling skills available when packaging.

Run `python3 scripts/validate.py` after edits. For workflow changes, run relevant synthetic cases from `evals/` with a fresh agent that has not seen the expected checks, then inspect its output. Treat those checks as limited evidence, not a claim of universal reliability.

Write concise, direct prose. Preserve factual qualifications and citations when editing. Keep the early scope focused; add instructions in response to demonstrated needs.
