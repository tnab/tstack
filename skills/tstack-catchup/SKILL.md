---
name: tstack-catchup
description: Reconstruct where a topic or project stands as of a specified date and what changed since a prior update. Use for catch-ups, returning to work, status refreshes, and concise handoffs grounded in available records.
---

# tstack catchup

Read and apply the [shared principles](../../references/principles.md) first.

Give the reader enough context to resume useful work: where things stand, what changed, what remains unresolved, and the next useful move.

## Bound the reconstruction

Identify the topic, project, relevant time window, and as-of date. Use the user's last update or supplied handoff as the baseline when available. If “recent” is unspecified, choose and disclose a sensible window for the task. Do not silently narrow a request for the full history.

Start from supplied context and artifacts. A usable handoff can eliminate history reconstruction. Access conversation history only when relevant and within the user's requested scope; do not mine unrelated projects, accounts, or transcripts. Discover available tools rather than assuming a particular application's storage paths.

Use [tstack-search](../tstack-search/SKILL.md) only for a missing fact or current-state check that the task requires and permits. Give it the topic, dates, source restrictions, and exact gap. A request to summarize supplied records does not automatically authorize broadening the corpus. State unavailable evidence and continue with what is known.

## Establish change and current state

Build a compact timeline of consequential events from the relevant records. Track event dates separately from publication or edit dates. Consolidate repeated reports of the same event. Keep older context only when it explains an active constraint, decision, failure, or dependency.

Compare the record with the baseline. Identify changed decisions, completed work, setbacks, ownership changes, and unresolved issues. If no reliable baseline exists, describe recent developments without claiming what is new to the reader. Do not infer “unchanged” from a lack of updates.

Verify consequential status claims against the available authoritative record as of the requested date. Distinguish planned, in progress, blocked, completed, cancelled, and unknown where those distinctions matter. A past update establishes last-known state; it does not prove present status. A merged change does not establish deployment, and an assigned task does not establish accepted ownership.

Resolve apparent conflicts through explicit superseding evidence. Preserve reversals and failed attempts that affect the next step. If verification is unavailable, give the last confirmed date and state what remains unverified. For a historical cutoff, exclude later developments from the reported state or clearly separate them if requested.

## Hand back the context

Lead with a short current-state summary and as-of date. Follow with the material changes since the baseline, active blockers or questions, and the most useful next action. Group by workstream only when several distinct threads need attention. Keep adjacent topics out unless they constrain this work.

Cite consequential statuses and changes. For recorded commitments, preserve explicit owners and due dates and check for completion or cancellation. Mark missing ownership or timing as unspecified. Separate suggested next steps from existing commitments; this brief does not send messages or update trackers.

Include any coverage limit that could change the reader's next move. Check that completed items are not presented as open and that stale evidence is not labeled current. Apply [tstack-write](../tstack-write/SKILL.md) before delivering the handoff.
