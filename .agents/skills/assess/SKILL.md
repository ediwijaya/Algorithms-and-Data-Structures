---
name: assess
description: Assess a learner's DSA exercise attempt for correctness, time and space complexity, assignment constraint fit, and opportunities for improvement. Use when the learner requests assessment or review of an exercise.
---

Assess the learner's current implementation while preserving independent
problem solving. Follow the repository's AGENTS.md.

## Establish scope

- Use the explicitly named file, or the active exercise when unambiguous.
- Start from the learner's implementation and explanation.
- Read the relevant assignment statement and available tests for input/output
  requirements, input bounds, time limits, and memory limits.
- Cite the source of constraints. If unavailable, state what is unknown;
  continue assessing what can be established without inventing requirements.
- Do not read previous solutions on main, in .practice-archive/, or in other
  completed implementations unless the learner requests a comparison.

## Check correctness

- Examine the invariant, termination, boundary cases, and input/output behavior.
- Run supplied samples and a focused set of valid edge cases when feasible.
- Use bounded test runs; keep temporary harnesses outside the repository.
- For non-unique outputs, validate the required properties rather than exact
  output text.
- Distinguish a demonstrated failure, a suspected issue, and behavior that
  passed the checks performed. Passing samples alone does not prove correctness.
- For a demonstrated failure, show a small valid counterexample, expected
  behavior, observed behavior, and the relevant code location.

## Analyze complexity

- Define input-size variables.
- Derive worst-case time and auxiliary space from the actual implementation.
- Include recursion depth, temporary allocations, copying, slicing, sorting,
  and data-structure operations where relevant.
- Distinguish auxiliary space from total space including input storage.
- Explain expected or amortized bounds when applicable.
- Compare the derived costs with the documented maximum input sizes.
- Separate asymptotic suitability from runtime measurements. Do not promise
  judge acceptance based on local timing.

## Preserve learning

- Provide the assessment and complexity explanation directly.
- For an unresolved issue, give one small actionable hint or tracing question
  before proposing a fix.
- Describe the bottleneck without revealing an undiscovered algorithm.
- Discuss alternatives and tradeoffs more freely after the learner has solved
  the exercise or explicitly requests them.
- Do not edit exercise implementations, add solution files, or update
  PROGRESS.md unless requested.

## Report

Keep the report concise:
- Verdict and supporting evidence, including any validation limitations.
- Time and space complexity with a short derivation.
- Constraint fit: suitable, unsuitable, or uncertain, with reasons.
- One next hint for an unresolved issue; otherwise the most useful improvement
  or a statement that no material improvement is needed.

Prioritize correctness and constraint failures over style suggestions.