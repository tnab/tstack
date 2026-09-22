# Evaluation

Determine whether the requested workflow works on realistic tasks.

1. Use [evaluate-skill](../../evaluate-skill/SKILL.md) to define observable success, choose representative inputs, and keep expected checks separate from the worker's task.
2. Run within isolated, permitted resources. When comparing versions, use the same inputs and capabilities. If independent contexts or execution tools are unavailable, report that limitation and distinguish a static review from a behavioral run.
3. Inspect complete artifacts and available task-local execution evidence. Resolve disagreements between a judge and the source material; do not treat the worker's self-report as proof of routing or success.
4. Finish through [write](../../write/SKILL.md) with observed results, failures, and limits. Recommend a change when warranted; use [skill authoring](authoring-a-skill.md) to implement it only when requested.

Done when the evidence supports a bounded judgment about the workflow. A handful of passing examples is not proof of general reliability.
