---
name: tstack-followups
description: Find and reconcile outstanding commitments across meeting notes, documents, messages, and task records. Use to identify open actions, owners, deadlines, blockers, and completion evidence, or to update an existing action register when authorized.
---

# tstack follow-ups

Read and apply the [shared principles](../../references/principles.md) first.

Establish the topic, people, source scope, and cutoff date. Reuse supplied evidence and any existing action register. Use [tstack-search](../tstack-search/SKILL.md) only for material gaps or status checks within that scope. Do not scan unrelated personal history or expand a bounded review into a workspace audit.

## Identify commitments

Read the underlying messages or notes, including nearby replies and conditions. Capture the action, intended result, person or team named, source date, deadline wording, dependencies, and an exact source locator. Preserve enough context to distinguish the item from similar work.

Classify each candidate as a proposal, request, assignment, or accepted commitment. A named recipient, suggestion, or unanswered request does not prove acceptance. Preserve assigned ownership when the record establishes it, but identify acceptance as unconfirmed when relevant. Keep suggested next steps separate from recorded commitments. Never invent an owner or deadline to complete a row.

Resolve relative dates only when the reference date and relevant calendar or timezone are unambiguous. Keep the original wording beside a normalized date when useful. Mark uncertain dates as needing clarification; do not silently interpret "Friday," "end of day," or "next sprint." Treat a forecast or aspirational target differently from an agreed deadline.

## Reconcile the record

Match candidates to existing items by stable IDs where available, then by intended outcome, scope, owner, and source lineage. Merge repeated mentions of the same commitment and retain supporting links. Similar titles alone do not establish identity. Keep separate deliverables separate; flag uncertain matches instead of merging them.

Read later evidence through the cutoff for completion, changed ownership, changed dates, cancellation, or supersession. Prefer explicit updates from the responsible person or authoritative record over a newer ambiguous mention. Preserve unresolved conflicts. A finished draft does not prove delivery or approval; a closed task may have been canceled rather than completed.

Use statuses that reflect the evidence: open, blocked, unverified, completed, canceled, or superseded. Include blocked items and items whose current status is unverified in the outstanding view. Do not close work because it disappeared from later notes or a search found nothing. Link completed items to completion evidence and superseded items to their replacement. Apply "overdue" only when the deadline and cutoff comparison support it.

## Deliver or update

Return a compact list or table with action, owner, due date, status, and source. Add the blocker or uncertainty where it affects the next step. Order by recorded urgency, deadline, or dependency; label any prioritization you propose. State the cutoff and material coverage gaps. Summarize resolved items separately when useful for reconciliation.

Update an existing register only within explicit authorization. Preserve its IDs and unrelated fields; reconcile before adding rows. On a retry, reread the current register and apply only missing changes so repeated runs do not duplicate items. Inspect the saved result and verify changed statuses against their evidence.

Finish through [tstack-write](../tstack-write/SKILL.md). Do not automatically send reminders, assign work, create tasks, or schedule future checks. Those are separate actions requiring user authorization.
