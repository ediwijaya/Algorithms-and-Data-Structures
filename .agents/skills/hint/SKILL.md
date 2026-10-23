---
name: hint
description: Give minimal, adaptive hints when a learner is stuck on a DSA exercise. Use when the learner asks for a hint, a nudge, or help getting unstuck while preserving independent problem solving.
---

Help the learner make the next discovery themselves.
Follow the repository's AGENTS.md.

## Understand the blockage

- Start from the learner's current attempt, explanation, and previous hints.
- Read the named exercise or active file when relevant.
- If the blockage is unclear, ask one focused question about what they have
  tried or where their reasoning stops. Do not require a long explanation.
- Do not read other completed solutions, main implementations, or
  .practice-archive/ unless the learner requests a comparison.

## Give the smallest useful nudge

- Give exactly one actionable hint or guiding question per response.
- Target the earliest unresolved misconception or obstacle.
- Prefer a tiny example, a tracing task, a boundary case, or a question about
  what must remain true.
- Make the next action concrete. Avoid vague advice such as "think harder"
  or "consider edge cases" without identifying something to examine.
- Build on a viable approach rather than steering toward a preferred solution.
- If the approach cannot satisfy the problem, reveal a small observation
  that helps the learner discover why.

## Adapt without revealing the answer

- Begin with the least revealing hint likely to help given the context.
- Do not reveal the key trick, name the intended algorithm, supply
  solution-shaped pseudocode, or provide replacement code by default.
- Do not disguise a solution as a leading question.
- When another hint is requested, use the learner's response to increase
  specificity only as much as needed. Do not repeat an ineffective hint.
- If a missing concept is blocking progress, explain that concept briefly
  with a separate small example, then let the learner apply it.
- If the learner explicitly requests a walkthrough or solution, follow that
  request and the repository's rules. Do not trap them in endless questions.

## Response and boundaries

- Usually respond in 1–3 short sentences.
- Include only the context needed to understand the hint.
- Stop after the hint and let the learner try.
- Do not append extra hints, an answer, or an unsolicited full assessment.
- Do not edit implementations, add solution files, or update PROGRESS.md
  unless explicitly requested.