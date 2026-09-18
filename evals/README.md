# Behavioral checks

These exercises use only fictional records. They test observable decisions, not exact wording. They do not establish live connector behavior or compatibility with every agent.

Give a fresh agent the requested skill, the relevant fixture, and the `request` from a case in [cases.json](cases.json). Keep the `checks` from that agent until it has produced an answer. Permit reads of the bundled skills and principles; disallow live accounts, external searches, and unrelated files. Compare the result with the checks afterward.

For the follow-ups case, rerun the request using the first result as the existing register and confirm that it preserves identities and does not create duplicate actions. For the review case, verify that a review request leaves the supplied memo unchanged. For meeting preparation, confirm the agent prepares for the discussion without inventing an outcome.

Vary names, dates, order, and wording before repeating. A passing example is limited evidence; improve instructions from demonstrated failures and compare against an unassisted baseline before claiming quality gains.
