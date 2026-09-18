# tstack

Open-source skills for knowledge work, designed for use across AI agents. Find answers across code and work documents, then turn that research into clear, concise writing.

**Work in progress. This is an early iteration.** We are starting with search and writing, testing them on real work, and adding capabilities as we learn what is useful.

## Credit to Lauren and pstack

tstack draws heavily from [Lauren Tan](https://github.com/poteto)'s [pstack](https://github.com/cursor/plugins/tree/main/pstack). Much of this first version's search and writing guidance adapts her work. Thank you, Lauren, for publishing it and making it available to build on.

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

Search applies the writing pass before delivery. That shared writing standard is intended to carry into future skills for documents, meeting notes, and slides. It is an instruction-based review, not a global output filter.

The skills use the tools and accounts available in the agent's environment. They do not include connectors, credentials, or a search index. Searching Slack, Notion, Drive, or other private sources requires access through your configured tools.

## Use it with your agent

The shared skills use the [Agent Skills format](https://agentskills.io/specification). A root [Agent Plugins manifest](https://agent-plugins.org/plugin-authors/manifest) packages them for clients that support that standard. Cursor, Claude Code, and Codex manifests are included around the same skill files.

The instructions do not require a particular model or agent runtime. Available search tools and account access determine which sources an agent can read. Installation and automatic skill discovery vary by client; compatibility has not been verified in every agent.

To inspect or use the skills directly:

```sh
git clone https://github.com/tnab/tstack.git
cd tstack
```

Ask your agent to read and follow `skills/tstack-search/SKILL.md` or `skills/tstack-write/SKILL.md`, or install them through its supported skill workflow. Keep both skill directories together: search references the writing skill.

Example requests after loading the relevant skill:

```text
Use tstack-search to find why we chose this approach, with sources.
Use tstack-search to find the current plan and unresolved follow-ups.
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

## What comes next

First, test search against real questions: a known document, a past decision, a current plan, conflicting sources, and missing evidence. Check the evidence and usefulness of each answer, then refine the instructions.

After that, expand into reading and synthesizing large document sets, meeting notes, follow-up extraction, documents, and slides. These are directions for iteration; the repository currently contains only the two starter skills.

The initial draft passed skill and Codex manifest format checks. One synthetic exercise checked conflicting plans, an unavailable source, and a completed follow-up. Live connector behavior and installation across clients still need verification through use.

## License

[MIT](LICENSE), with upstream attribution preserved in [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
