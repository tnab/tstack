# tstack

Open-source skills for knowledge work, designed for use across AI agents. Find answers across code and work documents, then turn that research into clear, concise writing.

**Work in progress. This is an early iteration.** Eight skills cover research, synthesis, meetings, follow-ups, decisions, review, and writing. We are testing these workflows and refining them through use.

## Credit to Lauren and pstack

tstack draws heavily from [Lauren Tan](https://github.com/poteto)'s [pstack](https://github.com/cursor/plugins/tree/main/pstack). The search, writing, review, catch-up, and shared principles adapt substantial parts of her approach. Thank you, Lauren, for publishing it and making it available to build on.

The main foundations are:

- [`why`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/SKILL.md) and its evidence framework: discover sources, investigate independently where useful, read the underlying record, and distinguish evidence from inference.
- The [`Notion`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/sources/notion.md) and [`Slack`](https://github.com/cursor/plugins/blob/main/pstack/skills/why/references/sources/slack.md) playbooks: read full context, preserve attribution, check dates and decision status, and report gaps.
- [`unslop`](https://github.com/cursor/plugins/blob/main/pstack/skills/unslop/SKILL.md) and [`technical-writing`](https://github.com/cursor/plugins/blob/main/pstack/skills/technical-writing/SKILL.md): remove filler and formulaic language, write concretely, and keep the reader's effort low.

tstack adapts those foundations for everyday knowledge work. Searches can begin with a project, question, person, or document. The depth of research follows the question. Answers stay concise while preserving sources, caveats, and unresolved disagreements.

The upstream revision and Lauren's MIT copyright notice are recorded in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## What is here

| Skill | Purpose |
|---|---|
| [tstack-search](skills/tstack-search/SKILL.md) | Find documents, reconstruct decisions, check current plans, and answer questions across available sources. Return evidence, relevant gaps, and unresolved follow-ups. |
| [tstack-write](skills/tstack-write/SKILL.md) | Draft or edit prose to be direct, succinct, and natural. Remove AI tells without changing facts, uncertainty, attribution, or commitments. |
| [tstack-brief](skills/tstack-brief/SKILL.md) | Synthesize a document packet into a sourced brief, preserving disagreements and coverage limits. |
| [tstack-review](skills/tstack-review/SKILL.md) | Find consequential factual, logical, numerical, and practical problems in a document or plan. |
| [tstack-meeting](skills/tstack-meeting/SKILL.md) | Prepare a focused meeting or produce notes that distinguish discussion, decisions, and commitments. |
| [tstack-followups](skills/tstack-followups/SKILL.md) | Reconcile outstanding actions, owners, dates, blockers, and completion evidence across records. |
| [tstack-decide](skills/tstack-decide/SKILL.md) | Compare credible options and write a recommendation or an accurate decision record. |
| [tstack-catchup](skills/tstack-catchup/SKILL.md) | Reconstruct current state and meaningful changes since a prior update. |

Every skill explicitly loads the [shared principles](references/principles.md). Output-producing workflows finish through the writing skill. These instructions guide the agent; they are not a global output filter.

Choose the skill by the result you need. Search retrieves evidence; brief synthesizes it; catch-up emphasizes changes over time; decide makes a recommendation; review challenges an existing artifact. Meeting handles one meeting, while follow-ups reconciles commitments across records. Skills call each other only when the task needs it.

The [source notes](references/sources.md) document the pstack adaptations and additional practice guides.

The skills use the tools and accounts available in the agent's environment. They do not include connectors, credentials, or a search index. Searching Slack, Notion, Drive, or other private sources requires access through your configured tools.

## Use it with your agent

The shared skills use the [Agent Skills format](https://agentskills.io/specification). A root [Agent Plugins manifest](https://agent-plugins.org/plugin-authors/manifest) packages them for clients that support that standard. Cursor, Claude Code, and Codex manifests are included around the same skill files.

The instructions do not require a particular model or agent runtime. Available search tools and account access determine which sources an agent can read. Installation and automatic skill discovery vary by client; compatibility has not been verified in every agent.

To inspect or use the skills directly:

```sh
git clone https://github.com/tnab/tstack.git
cd tstack
```

Ask your agent to read and follow `skills/tstack-search/SKILL.md` or `skills/tstack-write/SKILL.md`, or install them through its supported skill workflow. Keep the full `skills/` and `references/` directories together. The skills share principles and refer to one another; copying a single `SKILL.md` omits dependencies.

Example requests after loading the relevant skill:

```text
Use tstack-search to find why we chose this approach, with sources.
Use tstack-search to find the current plan and unresolved follow-ups.
Use tstack-brief to summarize this packet for the operations lead, with sources.
Use tstack-meeting to turn this transcript into decisions and actions.
Use tstack-followups to reconcile these notes with our action register.
Use tstack-decide to compare these options against our constraints.
Use tstack-review to check this memo against the source material.
Use tstack-catchup to explain what changed since my last update.
Use tstack-write to tighten this memo while preserving its facts and caveats.
```

### Cursor

For local plugin discovery, clone into Cursor's plugin directory instead:

```sh
mkdir -p ~/.cursor/plugins/local
git clone https://github.com/tnab/tstack.git ~/.cursor/plugins/local/tstack
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

Run the structural checks with Python 3.9 or later:

```sh
python3 scripts/validate.py
```

The [behavioral exercises](evals/README.md) cover conflicting evidence, historical cutoffs, declined assignments, completed work, numerical errors, and infeasible choices. All fixtures are synthetic. Evaluate decisions and evidence rather than requiring identical wording.

The [initial results](evals/results-2026-09-18.md) record seven passing scenarios and a repeated follow-up reconciliation, with the limits of that testing.

The next iteration should come from real usage: whether the right sources were found, the reasoning holds, and the result is useful to its reader. Live connector behavior and installation across clients need verification in those environments. Slides are outside this release.

## License

[MIT](LICENSE), with upstream attribution preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
