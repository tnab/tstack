---
name: create-skill
description: Create or revise a reusable skill or playbook when the user requests workflow authoring. Use to turn a recurring knowledge-work task into concise instructions and validate the resulting behavior.
---

# Create a skill

Read [shared principles](../../references/principles.md). Author only within the requested scope. Completing ordinary knowledge work does not authorize changing the skills that govern it.

## Choose the smallest useful change

Identify the requests this capability should handle, the result it should produce, and the decisions existing instructions get wrong or leave unclear. Use the user's examples; ask only for information that materially changes the design.

Inspect nearby skills and playbooks before adding another. Extend an existing capability when it already owns the task. Use a playbook to coordinate existing skills; create a skill when a distinct capability deserves reuse and discovery. An available host authoring skill may help with its file format, but it is not a runtime dependency.

## Write instructions that change decisions

Use a short, descriptive name with lowercase letters, digits, and hyphens, under 64 characters. Match the directory to the frontmatter `name`. Keep individual skill names free of the Knowledge Stack brand prefix. The frontmatter `description` should explain what the skill does and when to use it, with a boundary where misrouting is likely.

Put the essential workflow and constraints in `SKILL.md`. Link detailed procedures or examples only when a particular mode needs them. Point to maintained sources and existing skills instead of copying their instructions. Add scripts or assets only for a demonstrated use; remove unused scaffold files.

State the action directly. Keep explanations that resolve ambiguity. Remove generic advice and rules invented for hypothetical failures. Discover available tools and delegate only when supported. Preserve the user's scope and authorization for external actions.

For Knowledge Stack skills, explicitly load the shared principles and use the bundled writing skill for final prose. Keep relative references resolvable in the distributed package and prevent recursive handoffs. Record adapted public sources and retain their attribution and license notices.

## Validate the result

Check frontmatter, naming, references, cross-skill links, and any changed packaging. Run the repository's validator when available, and execute new scripts on representative inputs. Structural validation cannot establish that the instructions work.

For changes to routing, evidence handling, or consequential workflow behavior, use [evaluate-skill](../evaluate-skill/SKILL.md) with realistic requests and isolated fresh contexts where available. Keep expected checks and proposed fixes out of the executing agent's context. Inspect its actual outputs against the sources. If an evaluation is already active, return the changes and structural checks to that evaluator for the behavioral recheck; do not start another evaluation. For a wording-only change, compare meaning and readability directly; do not invent a behavioral benchmark.

Correct demonstrated failures narrowly, then rerun the affected exercise. An evaluation called from here returns findings; it does not start another authoring cycle. Finish with [write](../write/SKILL.md): summarize the resulting capability, material design choices, validation evidence, and remaining limits. Do not claim installation or client compatibility from file checks alone.
