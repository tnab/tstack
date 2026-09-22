# Behavioral checks

These exercises use only fictional records. They test observable decisions, not exact wording. They do not establish live connector behavior or compatibility with every agent.

Give a fresh agent the requested skill, the relevant fixtures, and only the `request` from a case in [cases.json](cases.json). Keep the `checks`, other cases, and previous evaluation results out of its context and accessible workspace. Permit reads of the bundled skills and principles; disallow live accounts, external searches, and unrelated files. Compare the result with the checks afterward.

Cases whose `skill` is `kstack` exercise the entry point. Start with that skill and let the agent choose its playbook and components. Collect its actual file reads, tool activity, output, and any edits so routing and unnecessary work can be assessed without requiring it to narrate its process. These cases cover meeting preparation, a simple wording edit, a document with conflicting sources, a custom onboarding exercise, and skill authoring with evaluation. Judge scope and results, not exact phrasing or a rigid sequence of tool calls.

Source material is read-only by default; save generated outputs separately. For a case with `workspace: "scratch-copy"`, prepare a disposable plugin containing the manifests, skills, shared references, license notices, maintainer instructions, and validator. Seed `evals/cases.json` with an empty list so validation can run without exposing expected checks. Omit evaluation reports and documentation linking to omitted files. Give the agent only that case's fixtures. Allow edits within this disposable copy; do not let the exercise change the maintained repository. Preserve its diff for inspection. If a requested evaluation cannot actually run with fresh workers, the output must say what remains untested.

For the follow-ups case, rerun the request using the first result as the existing register and confirm that it preserves identities and does not create duplicate actions. For the review case, verify that a review request leaves the supplied memo unchanged. For meeting preparation, confirm the agent prepares for the discussion without inventing an outcome.

Vary names, dates, order, and wording before repeating. A passing example is limited evidence; improve instructions from demonstrated failures and compare against an unassisted baseline before claiming quality gains.

Adding or structurally validating a case does not mean its behavior has passed. Record actual runs separately with the revision, agent, allowed capabilities, observed failures, and remaining gaps. Earlier results for individual skills do not establish that the entry router works.
