# Skill authoring

Create the smallest reusable instructions that change the agent's decisions.

1. Use [create-skill](../../create-skill/SKILL.md) for the requested skill creation or revision. Inspect existing skills and callers before adding another layer.
2. Validate frontmatter, referenced files, and cross-skill links with available validators. Check that the result preserves scope and works with the capabilities its intended users have.
3. For routing or other consequential behavioral changes, use [evaluate-skill](../../evaluate-skill/SKILL.md) with realistic cases and expected outcomes held back from workers. Inspect their actual output before claiming success.
4. Inspect the final diff for redundant instructions, private content, and attribution. Finish the handoff through [write](../../write/SKILL.md), stating the change, validation, and limits. Commit or publish only within the user's requested scope.

Done when the skill and its dependencies are usable and the claimed behavior has appropriate evidence. Editing instructions about Knowledge Stack is maintenance work; merely using Knowledge Stack does not authorize it.
