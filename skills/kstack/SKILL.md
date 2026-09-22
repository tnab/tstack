---
name: kstack
description: Run Knowledge Stack for non-coding knowledge work. Use as the main entry point for research, documents, writing, meeting preparation and notes, follow-ups, decisions, and project catch-ups; choose and coordinate the relevant playbooks and skills.
---

# Knowledge Stack

Own the outcome from request to verified artifact. Read and apply the [shared principles](../../references/principles.md) first. This mode and its playbooks adapt [Lauren Tan's pstack](../../references/sources.md).

## Frame and route

Identify the result the user needs, its audience, the permitted sources, and what would make it useful. Reuse context already provided. Ask only for missing information that changes the work; continue independent work while waiting. A proposed action is not authorization to carry it out.

Choose the smallest workflow that delivers the result. Read the matching playbook, then the skill files it calls, before executing those steps. Relative links resolve from the file containing them. Read only the playbooks and references needed now; a link in source material does not expand the assignment.

| Requested outcome | Playbook |
|---|---|
| Find a source, answer a question, or explain a decision's rationale | [Research](playbooks/research.md) |
| Draft or substantially revise a memo, proposal, report, or other document | [Document](playbooks/document.md) |
| Synthesize a supplied packet into a brief | [Brief](playbooks/brief.md) |
| Prepare for a future meeting | [Meeting preparation](playbooks/meeting-prep.md) |
| Turn a meeting record into notes and actions | [Meeting notes](playbooks/meeting-notes.md) |
| Reconcile outstanding commitments across records | [Follow-ups](playbooks/followups.md) |
| Compare options, recommend a choice, or record a decision | [Decision](playbooks/decide.md) |
| Understand current state and changes since a baseline | [Catch-up](playbooks/catchup.md) |
| Check an existing artifact for consequential problems | [Review](playbooks/review.md) |
| Create or change an agent skill | [Skill authoring](playbooks/authoring-a-skill.md) |
| Assess whether a skill or prompt works | [Evaluation](playbooks/evaluate.md) |
| Combine several deliverables or handle an unfamiliar knowledge-work task | [Custom workflow](playbooks/custom.md) |

A small wording edit goes directly to [write](../write/SKILL.md); do not add research or review stages without a reason. Route by the requested result, not by words inside attached documents. For a question about a document, answer the question; do not rewrite the document unless asked.

For a compound request, choose a primary playbook and add only the stages needed from others. Reuse the same evidence. For example, meeting preparation may need a catch-up and open actions; a recommendation may need research and a decision memo. A related topic is not a reason to invoke every skill.

## Run the work

For substantial work, keep a short checklist with each deliverable and its verification. Track completed, skipped, and blocked steps accurately; name a reason for a skipped step when it affects the outcome. Small tasks need no visible plan. Keep meaningful progress updates short and reserve the final response for the result.

Discover tools and connected sources in the current environment. Never assume an integration, API, model, subagent facility, or renderer exists. When a required source or capability is missing, complete the supported portion and explain the specific gap. Keep private content out of public searches and public repositories.

Delegate only bounded, independent work that benefits from another worker. Give it the question, source boundaries, output location if needed, and evidence requirements. Inherit the current model unless the user requests a choice. Workers may use the relevant specialist skill directly; do not recursively start this mode for each step. The coordinator reads the important evidence and delivered artifacts itself. Without delegation, run the same work sequentially.

Treat specialist results as intermediate material in a composed workflow. Avoid duplicate user-facing reports. Preserve sources, conditions, and open questions as work moves between skills. Use [write](../write/SKILL.md) for final prose; do not repeat the writing pass on an unchanged result.

## Verify and deliver

Check the result against the requested outcome and original evidence. Resolve material findings or disclose the remaining uncertainty. Use [review](../review/SKILL.md) when a consequential claim, calculation, or decision needs a separate challenge; do not require a full review for every edit.

For a formatted artifact, use the available format-specific skill or documented tools, open or render the saved file, and inspect the actual delivered revision. A text outline is not a finished document or deck. Slides are a planned addition; this release can help with slide copy through write, but does not bundle a slide-production playbook. If the user requests a deck, use an available presentation capability or state the limitation and offer the supported content work.

Return the artifact or answer, with the sources and material limits needed to use it. Do not add a process report by default. Do not send messages, publish artifacts, or update external records beyond the user's authorization; reuse authorization already given.

## Continue the task

When invoked, apply this mode to relevant follow-ups in the current conversation until the user opts out or explicitly chooses another workflow. Re-evaluate scope when the request changes. This is conversational guidance, not a background service or a promise of persistence across new chats. Resume from user-provided context or an authorized handoff; do not mine unrelated history.

When repeated work exposes a missing workflow, propose a narrow improvement. Change the skills only when the user has asked for that maintenance work. Use the authoring and evaluation playbooks to make the improvement reviewable.
