---
name: optimize-anything
description: 'This skill should be used when optimizing text artifacts with the GEPA optimize_anything API through the local optimize_anything library. Trigger phrases include "GEPA optimize_anything", "seed_candidate dict[str, str]", "EvaluatorFn ASI", "run_optimization", and "optimize prompt artifact".'
---

## 1. Purpose and Scope

Use this skill to design, run, and operationalize optimization workflows for text artifacts with the GEPA `optimize_anything` API and the local `optimize_anything` Python library. Treat this skill as the primary operating guide for converting a static artifact into an iterative search process that improves measurable outcomes.

Apply this skill when the artifact can be represented as structured text sections and evaluated against example data. Cover system prompts, instruction templates, rubric text, policy snippets, or any markdown and CSV artifact that can be loaded into a `seed_candidate` dictionary. Align optimization runs with explicit objectives, controlled budgets, and reflection-friendly evaluator feedback.

Keep this skill self-contained. Avoid prerequisite skill loading. Keep decisions local to this workflow: shape the candidate, define the evaluator, select configuration, run optimization, and apply the resulting candidate. Use references in `skills/optimize-anything/references/` for deeper API notes, evaluator recipes, and artifact-specific patterns when edge-case detail exceeds this core guide.

Operate across three optimization modes:

- Single-task optimization: maximize performance on one narrowly defined task with one objective function.
- Multi-task optimization: balance performance across multiple related tasks under one candidate representation.
- Generalization optimization: optimize for transfer quality on held-out or distribution-shifted examples, not only in-sample fit.

Constrain scope to optimization design and execution. Exclude deployment automation, CI orchestration, vendor billing strategy, and production observability wiring. Treat those concerns as downstream integration tasks.

## 2. Core Principles

1. Represent artifacts as named sections, not monolithic strings.
   Preserve semantic boundaries inside `seed_candidate` keys such as `system_prompt`, `policy`, `format_rules`, or markdown heading keys. Enable GEPA reflection loops to target specific sections. Reduce accidental regressions caused by whole-document rewrites.

2. Define evaluator semantics before spending optimization budget.
   Lock scoring criteria and ASI shape first. Prevent wasted metric calls on unstable reward definitions. Keep scores in the `0.0` to `1.0` range and keep evaluator behavior deterministic where possible.

3. Treat ASI as first-class optimization signal.
   Return dense, structured, and diagnostic metadata with every score. Include fields that explain failure mode, expected behavior, observed output, and constraint violations. Enable stronger reflection updates than scalar-only scoring.

4. Separate objective intent from domain background.
   Write `objective` as direct optimization target language. Write `background` as constraints, context, and domain assumptions. Prevent prompt pollution from mixed concerns.

5. Validate transfer, not only training improvement.
   Use `valset` whenever possible. Reject candidates that overfit `dataset` examples but degrade on held-out cases. Favor improvements that preserve behavior across prompt variations and input diversity.

## 3. Anatomy/Structure

Model the workflow as five coupled parts: GEPA API call surface, candidate representation, evaluator protocol, configuration preset, and execution runner.

GEPA API structure centers on one optimization function:

- `seed_candidate`: initial artifact state as `dict[str, str]`.
- `evaluator`: callable that scores each candidate-example pair.
- `dataset`: training examples used for search feedback.
- `valset`: optional validation examples for generalization tracking.
- `objective`: concise textual target of optimization.
- `background`: domain context and constraints for reflection.
- `config`: `GEPAConfig` composed from `EngineConfig` and `ReflectionConfig`.

The local library mirrors this shape through `run_optimization` and `run_from_file` in `src/optimize_anything/runners/optimize.py`. Prefer those wrappers for project-level consistency and file-type dispatch.

Represent `seed_candidate` as `dict[str, str]` with stable, named keys:

- For simple prompt optimization, use `{"system_prompt": "..."}`.
- For markdown artifacts, load with `load_markdown_artifact`; retain `frontmatter`, preamble body, and header-keyed sections.
- For CSV artifacts, load with `load_csv_artifact`; map columns or fields to section keys suitable for evaluator use.

Keep key names stable across runs. Avoid renaming keys mid-experiment. Preserve shape compatibility between loaders, evaluators, and writers.

Follow the evaluator protocol from `src/optimize_anything/evaluators/base.py`:

- Signature: `(candidate: dict[str, str], example: dict[str, Any]) -> tuple[float, dict[str, Any]]`.
- First return item: score in `[0.0, 1.0]`.
- Second return item: ASI dictionary with actionable evidence for reflection.
- Handle per-example failures inside evaluator logic. Return `(0.0, {"error": ...})` for recoverable failures instead of raising exceptions.
- Use `oa.log()` as an auxiliary diagnostic channel when tuple-return ASI needs lightweight trace lines.

Use evaluator templates in `src/optimize_anything/evaluators/templates.py` as canonical patterns:

- `llm_classification_evaluator`: exact-match task scoring against expected labels.
- `rubric_evaluator`: LLM-as-judge scoring normalized from `0-10` to `[0,1]`.
- `mock_evaluator`: deterministic baseline for tests and offline iteration.

Use preset factories in `src/optimize_anything/config/presets.py`:

- `quick_preset`: low budget (`max_metric_calls=30`) for early debugging.
- `standard_preset`: medium budget (`max_metric_calls=100`) for regular runs.
- `thorough_preset`: higher budget (`max_metric_calls=300`) for deeper search.

Use public imports from `src/optimize_anything/__init__.py` to keep scripts concise and stable. Import `run_optimization`, `run_from_file`, loaders, evaluators, and presets from the package root when building external workflows.

Align optimization mode to data organization:

- Single-task mode: one dataset schema, one evaluator, one objective.
- Multi-task mode: mixed dataset with task tags or multiple evaluator branches sharing a candidate.
- Generalization mode: explicit train/validation split with evaluator checks that highlight transfer failures in ASI.

## 4. Creation Process

1. Load and normalize the artifact.
   Select in-memory or file-based entry.
   Use `run_optimization` for direct dictionaries.
   Use `run_from_file` when optimizing markdown or CSV artifacts.
   Confirm that every candidate value is `str`, keys are semantically named, and serialization round-trips through writers.

2. Choose optimization mode.
   Start with single-task for first implementation.
   Switch to multi-task when one artifact must satisfy multiple task families.
   Switch to generalization when distribution shift or robustness is the main requirement.
   Encode mode intent inside objective wording and dataset design.

3. Define evaluator contract and ASI schema.
   Implement the evaluator with required signature and normalized scoring.
   Keep scoring deterministic where possible.
   For LLM task evaluation, capture raw response, normalized response, expected output, and match flags.
   For rubric scoring, record raw score, normalized score drivers, and explanation text.
   Include compact but rich ASI fields that isolate errors and proposed correction directions.

4. Draft objective and background text.
   Write `objective` as one direct sentence describing measurable optimization intent.
   Write `background` as short constraints: domain rules, response format limits, prohibited behavior, safety boundaries, and known ambiguities.
   Keep objective and background stable across comparative runs to preserve interpretability.

5. Select configuration strategy.
   Start from `quick_preset` while debugging evaluator logic and candidate shape.
   Move to `standard_preset` once improvements become stable.
   Reserve `thorough_preset` for final quality search or hard tasks.
   Override `reflection_lm` only when reflection quality or cost profile requires adjustment.

6. Prepare datasets.
   Build `dataset` examples with consistent schema and representative complexity.
   Provide `valset` for transfer checks whenever available.
   Balance class labels and edge cases for classification tasks.
   Preserve strict typing for evaluator-referenced keys.

7. Execute the run.
   Call `run_optimization` or `run_from_file` with candidate, evaluator, dataset, objective, background, and config or preset.
   Keep one controlled variable per experiment series: evaluator logic, budget, or objective phrasing.
   Record run metadata externally if repeatability auditing is needed.

8. Interpret result object.
   Extract `best_candidate` as primary artifact output.
   Inspect available score fields such as `best_score`, `score`, or validation-centric fields.
   Review summary or stats fields for optimization trace indicators.
   Compare failure clusters in ASI across examples to detect systematic weaknesses.

9. Apply optimized candidate.
   For file-based flow with `write_back=True`, permit writer-based artifact persistence.
   For manual application, route `best_candidate` through `write_markdown_artifact` or `write_csv_artifact`.
   Preserve format fidelity and perform diff review before final acceptance.

10. Run post-optimization validation.
    Re-evaluate best candidate on held-out examples.
    Confirm no regression on hard constraints from background.
    Confirm output format compliance and task-specific invariants.
    Archive candidate, evaluator version, objective, background, and config to support reproducibility.

## 5. Structural Rules

Enforce the following mandatory rules for every optimization workflow.

Evaluator protocol rules:

- Implement evaluator as callable accepting `(candidate, example)` and returning `(score, asi)`.
- Return score as float in `[0.0, 1.0]`; clamp when upstream raw scales differ.
- Return ASI as `dict[str, Any]`; never return plain string or unstructured blob.
- Handle per-example evaluation failures gracefully inside the evaluator. Return `(0.0, {"error": ...})` instead of raising exceptions. Reserve exceptions for unrecoverable failures only.
- Keep evaluator pure relative to candidate-example input where practical; avoid hidden mutable global state.
- Avoid nondeterministic scoring noise unless task semantics require stochasticity.

Seed candidate rules:

- Represent candidate as `dict[str, str]` only.
- Keep keys stable across run series.
- Use meaningful section names; avoid opaque keys like `field1` unless legacy constraints require them.
- Preserve artifact hierarchy in key naming when loading from markdown sections.
- Ensure every value is UTF-8-safe text and compatible with writer functions.

ASI rules:

- Include evidence fields: observed output, expected output, and match or error indicators.
- Include diagnosis fields: failure category, violated rule, ambiguity marker, or parse status.
- Keep ASI concise but specific; avoid verbose narrative without structured fields.
- Maintain consistent ASI schema across examples in the same run.
- Prefer machine-parseable primitives: booleans, strings, numbers, and compact lists.
- Keep ASI values JSON-serializable. Avoid numpy arrays, custom objects, or non-serializable types.

Objective and background rules:

- Write objective as measurable target language tied to evaluator semantics.
- Write background as constraints and domain context, not redundant objective text.
- Avoid contradictory constraints between objective and background.
- Keep both strings concise to preserve reflection signal clarity.

Configuration rules:

- Use preset names `quick`, `standard`, or `thorough` when config is not explicitly provided.
- Reject invalid preset values; handle errors early.
- Prefer explicit `config` object only when preset defaults are insufficient.
- Tune budget after evaluator quality is validated, not before. Use `quick_preset` for early debugging, `standard_preset` for stable development, and `thorough_preset` only for final quality sweeps.
- Set at least one stopping condition (`max_metric_calls` or `max_candidate_proposals`). Omitting both raises `ValueError`.

Runner and artifact rules:

- Use file extension dispatch only for `.md`, `.markdown`, and `.csv` in built-in runner paths.
- Treat unsupported extensions as hard errors and resolve with custom loaders externally.
- Use writers to apply optimized candidates; avoid ad hoc serialization that breaks artifact structure.
- Preserve frontmatter, section boundaries, and formatting constraints when applying optimized output. Load from source format and write back with compatible writers to maintain round-trip integrity.
- Keep write-back optional and explicit to avoid accidental file mutation.

Mode selection rules:

- Start in single-task mode unless multi-task coupling is required by problem definition.
- Use multi-task mode only when shared candidate structure offers clear cross-task leverage.
- Use generalization mode whenever production conditions differ from training distribution.
- Prefer validation-focused decisions over training-only score gains.

Prohibited actions:

- MUST NOT use positional lists or raw strings as `seed_candidate`; always use `dict[str, str]` with named keys.
- MUST NOT return an evaluator result without an ASI dictionary, even when the score is `1.0`.
- MUST NOT use `run_from_file` with file extensions other than `.md`, `.markdown`, or `.csv` without a custom loader.
- MUST NOT mutate global state inside evaluators; keep evaluator logic pure relative to candidate-example input.
- MUST NOT change `objective` text and `config` budget simultaneously across comparison runs.
- MUST NOT bypass writer functions when applying optimized candidates to structured artifacts.
- MUST NOT omit `valset` when the workflow targets generalization or transfer quality.

## 6. Validation Checklist

- [ ] Confirm candidate representation uses `dict[str, str]` with stable section keys.
- [ ] Confirm evaluator signature matches `(dict[str, str], dict[str, Any]) -> tuple[float, dict[str, Any]]`.
- [ ] Confirm evaluator score always falls inside `[0.0, 1.0]`.
- [ ] Confirm ASI contains actionable fields beyond a scalar score.
- [ ] Confirm objective states measurable optimization target in one direct sentence.
- [ ] Confirm background captures constraints and context without duplicating objective.
- [ ] Confirm preset or config is explicitly set (`quick`, `standard`, `thorough`, or `GEPAConfig`).
- [ ] Confirm dataset schema matches evaluator key access patterns.
- [ ] Confirm valset is present for generalization-sensitive workflows.
- [ ] Confirm run executes through `run_optimization` or `run_from_file` with no signature drift.
- [ ] Confirm result parsing extracts `best_candidate` and available score/summary fields.
- [ ] Confirm optimized candidate is applied through writer-compatible path.
- [ ] Confirm post-run validation checks hard constraints and transfer behavior.
- [ ] Confirm workflow references deeper guidance in `skills/optimize-anything/references/` when advanced patterns are needed.

## 7. Common Mistakes

| Mistake | Problem | Fix |
|---------|---------|-----|
| Treating the artifact as one raw string | Loses section boundaries; GEPA cannot target specific sections for reflection updates, causing whole-document rewrites and accidental regressions. | Preserve named keys and loader-derived structure in `seed_candidate`. |
| Returning only score from evaluator and omitting ASI | The reflection loop receives no evidence to diagnose failures, producing blind revision proposals instead of targeted fixes. | Add structured diagnostics with observed output, expected output, match flag, and failure category. |
| Emitting raw rubric scores on `0-10` scale | GEPA expects scores in `[0.0, 1.0]`. Un-normalized scores corrupt the optimization objective and produce misleading progress signals. | Convert to `[0, 1]` with `max(0.0, min(1.0, score_raw / 10.0))` before return. |
| Mixing objective and background into one paragraph | Pollutes the optimization target with contextual constraints, reducing reflection clarity and making objective intent ambiguous. | Split measurable target into `objective` and domain constraints into `background`. |
| Running `thorough` budget before evaluator debugging | Wastes API budget on an unstable evaluator; broken scoring logic invalidates all search progress. | Start with `quick_preset` and escalate only after evaluator produces stable, diagnostic ASI. |
| Ignoring validation dataset | Celebrates training gains that may not transfer; optimized candidate overfits `dataset` examples. | Add `valset` and prioritize transfer-safe candidates over training-only improvements. |
| Renaming candidate keys across experiments | Breaks evaluator assumptions and key access patterns; causes `KeyError` or silent misalignment. | Freeze key schema per run family and document required keys in evaluator docstring. |
| Writing optimized markdown manually | Corrupts frontmatter, section headers, or formatting constraints that writer functions preserve. | Use `write_markdown_artifact` or `write_csv_artifact` for serialization. |
| Packing ASI with long prose and no structured fields | Reflection loop cannot parse narrative text into actionable revision targets; reduces optimization efficiency. | Use concise keys for response, expectation, failure type, and parse state. |
| Using unsupported file extensions with `run_from_file` | `run_from_file` supports `.md`, `.markdown`, and `.csv` only; unsupported extensions raise `ValueError`. | Convert artifact format or implement a custom loader/writer path. |
| Comparing runs with changed objective and changed config | Confounds experimental variables; improvements cannot be attributed to either change. | Control one variable per comparison: evaluator logic, budget, or objective phrasing. |
| Assuming one evaluator template fits every task | Template defaults may not match task-specific scoring semantics, producing misleading scores. | Adapt template internals (label keys, rubric text, scoring logic) while preserving the `(candidate, example) -> (score, asi)` protocol. |
| Raising exceptions in evaluator on bad input | Terminates the optimization run on a single bad example instead of continuing with remaining examples. | Return `(0.0, {"error": str(e)})` and let the optimizer continue. |
| Using mutable global state in evaluators with `parallel=True` | Race conditions produce non-deterministic scores and corrupt ASI when evaluators share state across threads. | Keep evaluator logic pure; avoid global counters or shared caches without thread locks. |
| Missing stopping condition in config | `ValueError` raised immediately; no optimization runs. | Set `max_metric_calls` or `max_candidate_proposals` in `EngineConfig`. |
| Inconsistent ASI schema across examples | Reflection loop cannot aggregate diagnostics systematically; revision proposals become unfocused. | Return the same field set in all branches; use `None` as sentinel for absent values. |
| Non-serializable ASI values | ASI payload fails to serialize for reflection and logging. | Use plain Python types: strings, numbers, booleans, lists, dicts. Convert numpy arrays to lists. |

## 8. References Usage

Use `skills/optimize-anything/references/` as the detailed companion directory for advanced workflows. Keep core execution in this file and consult references when deeper implementation patterns are required.

- **`skills/optimize-anything/references/api-patterns.md`** — Consult when the core SKILL.md leaves a specific API question unanswered. Covers `optimize_anything()` function signatures, expanded `GEPAConfig` composition, `EngineConfig` and `ReflectionConfig` fields, `seed_candidate` formats by artifact type, optimization mode examples, result object access patterns, stopping-condition constraints, configuration pitfalls, and the public import surface.

- **`skills/optimize-anything/references/evaluator-implementations.md`** — Consult when designing evaluators, selecting evaluator templates, understanding the evaluator protocol, or debugging common evaluator implementation errors. Provides the full evaluator protocol definition, three complete evaluator implementations (classification, agent-definition, skill-format), advanced patterns (graceful error handling, multi-objective, parameter-specific feedback, thread safety), and a catalog of common evaluator mistakes with corrected examples.

- **`skills/optimize-anything/references/asi-payload.md`** — Consult when structuring ASI payloads, choosing field naming conventions, understanding ASI delivery mechanisms, or designing multi-objective feedback. Provides the ASI field taxonomy (evidence, diagnosis, quantitative, multi-objective, parameter-specific), two delivery mechanisms (return tuple vs. `oa.log()`), reserved key handling, thread safety for parallel evaluation, serialization requirements, and minimal-to-rich ASI examples.

Prefer this SKILL body for default execution. Escalate to reference files only when edge cases, cross-task coupling, or evaluator complexity exceeds the default path.
