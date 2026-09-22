# Sources and adaptations

These sources inform the workflows. They are not runtime dependencies or instructions to read every source on each task. Knowledge Stack's instructions are adaptations for knowledge work; the authors of these sources do not endorse this project.

## Lauren Tan's pstack

The starting point is [Lauren Tan's pstack](https://github.com/cursor/plugins/tree/main/pstack). The initial individual skills and shared principles drew from revision `e31650eea443aaea1e84cc15d88c13f40080b275`. The Knowledge Stack mode, playbook architecture, and authoring and evaluation workflows additionally draw from revision `53e579f1481697931fc44f5445171397cfa2b24b`.

This is a substantial adaptation of pstack's architecture and ethos for non-coding work. Thank you, Lauren, for making it available. Its MIT notice is retained in [THIRD_PARTY_NOTICES.md](../THIRD_PARTY_NOTICES.md).

| Upstream material | Adaptation in Knowledge Stack |
|---|---|
| [Poteto Mode](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/SKILL.md) and its [playbooks](https://github.com/cursor/plugins/tree/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/playbooks) | One main entry point that routes work to focused playbooks, composes reusable skills, applies shared principles, and verifies completion. Knowledge Stack selects knowledge-work workflows and discovers available tools without requiring a named model or runtime. |
| [Authoring a skill](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/playbooks/authoring-a-skill.md) | Focused instructions, references instead of duplication, metadata and link validation, and behavior checks where they can establish correctness. A bundled portable `create-skill` replaces reliance on Cursor's built-in authoring skill. |
| [Eval](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/poteto-mode/playbooks/eval.md) | Realistic task prompts, expected checks withheld from the executing agent, review of actual outputs, and explicit limits on what a run establishes. No fixed transcript paths, model requirements, or automatic access to unrelated conversations. |
| [Figure it out](https://github.com/cursor/plugins/blob/53e579f1481697931fc44f5445171397cfa2b24b/pstack/skills/figure-it-out/SKILL.md) | A custom knowledge-work playbook that defines the deliverable and completion check, resolves uncertainty early, sequences verifiable work, and inspects the combined result. |
| [why](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) and [epistemics](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/epistemics.md) | Source discovery, evidence before inference, contradictions, and explicit gaps across search, briefs, decisions, meetings, and reviews. |
| [unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md) and [technical-writing](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md) | A shared writing pass that removes formulaic language while preserving meaning. |
| [recall](https://github.com/cursor/plugins/blob/main/pstack/skills/recall/SKILL.md) | Scoped catch-ups, current-state checks, and useful handoffs. No fixed transcript paths or automatic history mining. |
| [interrogate](https://github.com/cursor/plugins/blob/main/pstack/skills/interrogate/SKILL.md) | Evidence-backed criticism, consequential findings, independent checks when useful, and judgment about which findings deserve action. |
| [prove it works](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-prove-it-works/SKILL.md) | Check the actual source, calculation, delivered revision, or saved record. |
| [minimize reader load](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-minimize-reader-load/SKILL.md), [subtract before adding](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-subtract-before-you-add/SKILL.md), and [guard context](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-guard-the-context-window/SKILL.md) | Concise prose, selective reading, proportionate workflows, and compact evidence notes. |
| [exhaust the design space](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-exhaust-the-design-space/SKILL.md) and [attack the premise](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-attack-the-premise/SKILL.md) | Compare credible alternatives and test assumptions without a fixed option count or engineering-specific procedure. |
| [make operations idempotent](https://github.com/cursor/plugins/blob/main/pstack/skills/principle-make-operations-idempotent/SKILL.md) | Reconcile follow-ups against existing records, preserve IDs, and avoid duplicates during authorized repeated updates. |

## Additional practice guides

- [HM Treasury: synthesis of existing evidence](https://www.gov.uk/government/publications/the-magenta-book/magenta-book-annex-a-analytical-methods-for-use-within-an-evaluation-html#a4-methods-for-synthesis-of-existing-evidence). Informs question-led synthesis, assessment of evidence quality, and transparent coverage limits. A work brief is not presented as a systematic review.
- [House of Commons Library editorial policy](https://commonslibrary.parliament.uk/editorial-policy/). Informs accuracy, treatment of competing views, and attention to revision dates in briefs and catch-ups.
- [Atlassian: page-led meetings](https://www.atlassian.com/team-playbook/plays/page-led-meeting) and [meeting notes](https://www.atlassian.com/software/confluence/templates/meeting-notes). Inform outcome-first preparation, relevant prereading, and separation of discussion, decisions, and actions.
- [Atlassian: action items](https://www.atlassian.com/work-management/project-collaboration/team-meetings/action-items). Informs specific outcomes, recorded owners and dates, and tracking. Knowledge Stack additionally preserves unknowns and distinguishes assignment from acceptance.
- [Atlassian: DACI](https://www.atlassian.com/team-playbook/plays/daci). Informs the distinction between coordinating and approving a decision, explicit decision factors, and a durable record. Knowledge Stack does not impose DACI roles on every task.
- [Atlassian: sparring](https://www.atlassian.com/team-playbook/plays/sparring). Informs reviews scoped to purpose, audience, stage, and actionable feedback.

Additional guides were consulted on 2026-09-18. Their underlying ideas are adapted in original wording; their content is not bundled with the plugin.
