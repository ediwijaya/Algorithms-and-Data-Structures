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

Use the following numbered sections in order. Keep each section brief and
include evidence rather than a score or unsupported acceptance claim.

### 1. Status

Use one of these verdicts:
- **PASS (available checks):** All executed checks passed, correctness review
  found no unresolved issue, and the implementation fits the documented
  constraints. State the validation scope; this is not official judge acceptance.
- **FAIL:** A valid counterexample, runtime error, output violation, or
  demonstrated incompatibility with a documented constraint was found.
  Identify the reason, such as Wrong Answer, Runtime Error, or Constraint Failure.
- **INCONCLUSIVE:** Validation or constraint information is insufficient, or a
  suspected issue remains unresolved. Do not force uncertainty into PASS or FAIL.

### 2. Test results

Summarize executed checks in a compact table with columns Case, Expected,
Observed, and Result. Group repetitive passing cases when useful. Distinguish
tests actually run from manual reasoning or suggested tests. If nothing was
run, say so. For a failure, include one small valid input that reproduces it
and the relevant code location. Do not invent hidden-test coverage, runtime
percentiles, or memory measurements.

### 3. Complexity

Define the input-size variables. Report time and auxiliary space bounds with
a short explanation of the operations or allocations responsible for each.
State total space separately when relevant, including input storage.

### 4. Constraint fit

Report **Suitable**, **Unsuitable**, or **Uncertain** against the sourced input
bounds and any time or memory limits. Distinguish an asymptotic assessment
from measured performance; identify limits that remain unverified. A local
timeout alone does not establish an official Time Limit Exceeded verdict.

### 5. Next step

For an unresolved issue, give one small actionable hint or tracing question,
without revealing the fix or intended algorithm. Otherwise, describe the most
useful improvement at the level permitted by the learner's progress, or state
that no material improvement is needed. Separate necessary fixes from optional
optimizations and avoid manufacturing style issues to fill this section.

Prioritize correctness and constraint failures over style suggestions.