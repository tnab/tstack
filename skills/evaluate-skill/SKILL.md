---
name: evaluate-skill
description: Assess whether a skill or playbook handles realistic requests correctly. Use to validate workflow changes, investigate failures, or compare revisions using source-grounded checks and inspected outputs.
---

# Evaluate a skill

Read [shared principles](../../references/principles.md). Define the behavior being examined before running it. Evaluation produces evidence and recommendations; edit the skill only when the user has requested revision.

## Design an exercise

Choose realistic requests that expose the changed decisions. Include a relevant boundary, such as a request that should take another route, conflicting evidence, or a missing capability. Use synthetic or permitted public material for fixtures intended for publication. Do not turn private work records into public fixtures.

Write expected checks separately from the agent's task. Distinguish factual requirements from subjective judgments. Factual checks need source evidence: for example, a recorded proposal must remain a proposal. Assess usefulness or clarity through concrete passages and the task's audience, not required phrases or arbitrary scores.

Decide whether the exercise measures discovery, execution, or both. A discovery exercise must let the agent choose among the available skills; explicitly naming the target skill tests execution alone. Scope resources, allowed side effects, and a reasonable stopping point before running.

## Run in fresh contexts

When supported, give each executing agent an isolated workspace and fresh context containing only the organic user request, applicable skills, and necessary raw material. Use ordinary project and file names. Withhold expected checks, prior verdicts, suspected failures, and proposed fixes. Ask for the deliverable a user would request, without hints about the measured behavior or demands to recite which instructions were followed.

For a comparison, keep inputs and access comparable, record the revisions and relevant runtime differences, and separate each run's artifacts. An independent reviewer can inspect anonymized outputs together against the same criteria. Do not require a particular model or tool. If isolation or reviewer blinding is unavailable, perform the useful checks you can and disclose that limitation; do not describe the result as independent or blinded.

## Inspect evidence, then conclude

Read every output and inspect generated artifacts. Verify central claims, citations, calculations, recorded actions, and material omissions against the source material. Render files when layout matters and tools permit. Review available records of actions from this exercise when routing or authorization matters; do not infer compliance from the agent's self-report or inspect unrelated conversations.

Check an independent review against the actual work. Resolve disagreements through sources or identify an ambiguous criterion. Keep factual defects separate from preferences and missing evidence. Report observable outcomes per case, with locators or examples, and describe the limited coverage. A handful of successful runs does not establish a general success rate, statistical significance, or compatibility with untested clients.

If called by an authoring workflow, return findings to that caller without calling it back. Otherwise, if revision is authorized, apply the smallest supported correction through [create-skill](../create-skill/SKILL.md), supplying the evidence and stating that this evaluation is already active. Resume here to recheck affected behavior. Stop when the agreed scope is complete or the remaining constraint is explicit.

Finish the report with [write](../write/SKILL.md). State what was exercised, what happened, what the evidence supports, and what should change. Preserve the distinction between a check that failed, one that was not run, and a judgment that remains uncertain.
