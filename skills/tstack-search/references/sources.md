# Source guidance

These are search strategies, not connector APIs. Inspect the tools available for the current source before choosing a query.

| Source | Find and read | Distinction to preserve |
|---|---|---|
| Local code or GitHub | Use the available code search; prefer `rg` for local symbols and terms when a shell is available. Read relevant code and tests. Use available history, PRs, and issues to trace changes and rationale. | A test describes expected behavior; a merged change is not proof of deployment. Code alone does not establish why a choice was made. |
| Notion | Search titles and text if supported. Read page contents, relevant child blocks, linked decision records, authors, dates, and approval status. | Some tools search titles only. A missing result then says little about page contents. An edited draft is not an approved plan. |
| Slack | Search exact terms and aliases with supported date, person, and channel filters. Read the parent and relevant replies, then follow linked records and later resolutions. | One message may be a proposal. A reaction is not an explicit commitment. Access and retention can leave gaps. |
| Drive or shared documents | Search names and full text where supported. Open the actual document and relevant linked material. Check ownership, revision context, and comments when available. | File modification time may reflect formatting. Exported copies can be stale. Search metadata alone cannot establish the document's contents. |
| Meeting notes or transcripts | Read the relevant discussion and conclusion. Preserve speaker attribution and distinguish a proposed action from an accepted one. | Auto-generated notes may misattribute a statement. Verify consequential commitments against the transcript or another primary record when available. |
| Issue trackers or email | Follow related issues or the complete relevant email thread. Check assignee, status, dates, explicit decisions, and subsequent updates. | A ticket's assignee may differ from the decision owner. A forwarded message is not independent corroboration. |

For a known-document request, return the best matching document and a short reason. For a current-state request, look for later amendments to the applicable decision. For a rationale request, look for contemporaneous discussion, not only today's implementation.
