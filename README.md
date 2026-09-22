# Knowledge Stack

**Knowledge Stack (`kstack`) is a set of skills optimized for non-coding work.** Use it to research a question, create a document, prepare a meeting, reconcile follow-ups, or turn a pile of sources into clear writing.

Start with `/kstack` and describe the result you need. It selects a playbook, calls the relevant skills, checks the result, and keeps the writing direct. You can also call any skill individually.

```text
/kstack Find why we chose this approach, and whether that decision still stands.
/kstack Prepare me for tomorrow's project review using these notes and documents.
/kstack Turn this research into a one-page recommendation for the operations lead.
/kstack Reconcile this meeting transcript with our existing action register.
/kstack Tighten this memo without losing its caveats.
```

`/kstack` is shorthand for invoking the main skill. Exact command syntax and discovery depend on the agent and plugin client. You can always ask your agent to read and follow [skills/kstack/SKILL.md](skills/kstack/SKILL.md).

**Early work in progress.** The current release focuses on research, documents, writing, meetings, and decisions. Slides are part of the intended scope but are not implemented yet. The workflows need continued testing and refinement through use.

## Thank you, Lauren

Knowledge Stack builds heavily on [Lauren Tan](https://github.com/poteto)'s [pstack](https://github.com/cursor/plugins/tree/main/pstack). Thank you, Lauren, for publishing the architecture and practices that make this project possible.

The adaptation is substantial. The main mode, task-specific playbooks, reusable skills, shared principles, evidence standards, concise writing, and verification approach all draw from pstack. Knowledge Stack applies that structure to knowledge work, with portable instructions and tools supplied by the user's agent environment.

The main foundations are [Poteto Mode](https://github.com/cursor/plugins/blob/main/pstack/skills/poteto-mode/SKILL.md), its authoring and evaluation playbooks, [why](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md), [unslop](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md), [technical-writing](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md), and pstack's principles. [Sources and adaptations](references/sources.md) records the mapping and revisions. Lauren's full MIT notice is preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## How it works

The [kstack skill](skills/kstack/SKILL.md) is the main entry point. It establishes the outcome, audience, source boundaries, and any missing information that would change the work. Then it loads the relevant [playbook](skills/kstack/playbooks/) and composes the skills needed to finish the task. A small edit stays small; a research-backed recommendation may need search, synthesis, a decision, review, and writing.

Playbooks cover research, document creation, briefs, meeting preparation, meeting notes, follow-ups, decisions, catch-ups, reviews, skill authoring, and evaluation. A custom playbook handles requests that span several workflows or do not fit one. Playbooks define the sequence and completion checks; specialized skills own the detailed instructions.

| Skill | Purpose |
|---|---|
| [kstack](skills/kstack/SKILL.md) | Route a request through the right playbook and carry it to a checked result. |
| [search](skills/search/SKILL.md) | Find answers and reconstruct decisions across available sources. |
| [brief](skills/brief/SKILL.md) | Synthesize a document packet into a sourced brief. |
| [write](skills/write/SKILL.md) | Draft or edit direct, succinct prose while preserving meaning. |
| [review](skills/review/SKILL.md) | Find consequential factual, logical, numerical, and practical problems. |
| [meeting](skills/meeting/SKILL.md) | Prepare a focused meeting or separate discussion, decisions, and commitments in notes. |
| [followups](skills/followups/SKILL.md) | Reconcile actions, owners, dates, blockers, and completion evidence. |
| [decide](skills/decide/SKILL.md) | Compare credible options and produce a recommendation or decision record. |
| [catchup](skills/catchup/SKILL.md) | Reconstruct current state and meaningful changes since a prior update. |
| [create-skill](skills/create-skill/SKILL.md) | Create or improve a portable skill with focused instructions and validation. |
| [evaluate-skill](skills/evaluate-skill/SKILL.md) | Check skill behavior using realistic tasks and evidence from the actual outputs. |

All skills load the [shared principles](references/principles.md). Ground claims in evidence. Preserve uncertainty, disagreement, and history. Challenge weak premises. Match effort to the task. Verify the delivered artifact. Remove filler and formulaic language without erasing qualifications or attribution.

These are instructions for an agent, not an executable workflow engine or a global output filter. They use available tools and accounts; they do not include connectors, credentials, or a search index. Searching code, Slack, Notion, Drive, or other sources requires configured access. Reading a source does not authorize sending messages, assigning work, or publishing its contents.

## Use it with your agent

The skills use the [Agent Skills format](https://agentskills.io/specification). A root [Agent Plugins manifest](https://agent-plugins.org/plugin-authors/manifest) packages them for clients that support that standard. Cursor, Claude Code, and Codex manifests wrap the same skill files.

The instructions do not require a particular model or runtime. Installation, invocation syntax, automatic discovery, and available tools vary by client. Compatibility has not been verified in every agent.

To inspect or use the skills directly:

```sh
git clone https://github.com/tnab/kstack.git
cd kstack
```

Ask your agent to read and follow `skills/kstack/SKILL.md`, or install the plugin through its supported workflow. Keep the full `skills/` and `references/` directories together. Copying a single `SKILL.md` omits playbooks and shared dependencies.

### Cursor

For local plugin discovery, clone into Cursor's plugin directory instead:

```sh
mkdir -p ~/.cursor/plugins/local
git clone https://github.com/tnab/kstack.git ~/.cursor/plugins/local/kstack
```

Restart Cursor or run **Developer: Reload Window**, then check **Customize**. See [Cursor's local plugin workflow](https://cursor.com/docs/plugins#test-plugins-locally). Team settings may restrict local imports.

This repository is a single plugin. It has not been submitted to the official Cursor Marketplace. Public listings require a public repository and Cursor review; see the [submission requirements](https://cursor.com/docs/reference/plugins#submitting-a-plugin).

### Claude Code

From a local clone, load the plugin for a session:

```sh
claude --plugin-dir .
```

See the [Claude Code plugin reference](https://code.claude.com/docs/en/plugins-reference) for installation and discovery options.

### Codex and other agents

Use the client's supported plugin or skill installation flow, or load the skill files directly. The Codex manifest is at `.codex-plugin/plugin.json`; the portable manifest is at `plugin.json`. All clients share the same `skills/` content.

## Check and improve the skills

Use the authoring and evaluation playbooks through the main skill:

```text
/kstack Create a skill for turning a research packet into a customer briefing.
/kstack Evaluate whether this skill preserves conflicting evidence and unknown owners.
```

Run structural checks with Python 3.9 or later:

```sh
python3 scripts/validate.py
```

The [behavioral exercises](evals/README.md) use synthetic material to check evidence handling and workflow behavior. Evaluate decisions and evidence rather than requiring identical wording. The [initial results](evals/results-2026-09-18.md) document tests of the earlier individual skills; they do not establish that every playbook or client works.

The [entry-workflow results](evals/results-2026-09-22.md) cover five synthetic requests through `kstack`, including skill authoring, plus a separate run of the authored skill. Structural checks passed. A Cursor CLI smoke test stopped at authentication, so Cursor runtime verification is still open.

Improve the workflows from observed failures: whether the right sources were found, the reasoning holds, and the result helps its reader. Live connector behavior and installation across clients need verification in those environments.

## License

[MIT](LICENSE), with upstream attribution preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
