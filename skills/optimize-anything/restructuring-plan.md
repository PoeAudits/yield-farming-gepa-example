# Restructuring Plan: optimize-anything Skill

Concrete plan for restructuring the optimize-anything skill based on three sources: current content analysis, GEPA codebase research, and skill-development conventions.

---

## 1. Final File Structure

```
skills/optimize-anything/
├── SKILL.md                          MODIFY — protocol corrections, GEPA content, structural changes
└── references/
    ├── api-patterns.md               MODIFY — remove evaluator protocol section, add new config fields
    ├── evaluator-examples.md         DELETE — content redistributed to two new files
    ├── evaluator-implementations.md  CREATE — evaluator protocol + three implementation templates
    └── asi-payload.md                CREATE — ASI design, structure, conventions, pitfalls
```

**Net change:** 1 file deleted, 2 files created, 2 files modified.

---

## 2. Content Mapping

### `SKILL.md` — Modify

| Section | Change | Source |
|---------|--------|--------|
| Section 3 Anatomy — evaluator protocol | Correct signature to reflect actual GEPA `Evaluator` protocol | GEPA source `optimize_anything.py:384-438` |
| Section 3 Anatomy — optimization modes | Correct single-task description: `dataset=None` means evaluator receives no `example` | GEPA source lines 1017-1030 |
| Section 3 Anatomy — config | Add `MergeConfig`, `RefinerConfig`, `TrackingConfig` to config anatomy | GEPA source lines 719-787 |
| Section 3 Anatomy — seedless mode | Add seedless mode (`seed_candidate=None`) as a fourth operational mode | GEPA source lines 44-49, 1119-1128 |
| Section 5 Rules — evaluator rules | Add rule: return `float` (score-only) is valid when using `oa.log()` | GEPA source lines 384-438 |
| Section 5 Rules — config rules | Add rule: at least one stopping condition required (`max_metric_calls` or `stop_callbacks`) | GEPA source lines 1229-1233 |
| Section 5 Rules — thread safety | Add rule: do not call `oa.log()` from child threads without propagating context via `get_log_context()` / `set_log_context()` | GEPA source lines 303-343 |
| Section 5 Rules — ASI reserved keys | Add rule: avoid `"log"`, `"stdout"`, `"stderr"` as ASI keys; GEPA renames them to `_gepa_log` etc. on collision | GEPA source lines 957-975 |
| Section 5 Rules — cache config | Add rule: `cache_evaluation=True` with `cache_evaluation_storage="disk"` requires `run_dir` | GEPA source lines 1174-1176 |
| Section 7 Common Mistakes | Add 5 new rows from GEPA pitfalls (see Section 6 of this plan) | GEPA codebase research |
| Section 8 References | Update to reference all four reference files with accurate path descriptions | Skill-development conventions |

**Keep unchanged in SKILL.md:** Sections 1, 2, 4, 6 — these are structurally sound and do not require GEPA corrections.

---

### `references/api-patterns.md` — Modify

| Section | Change | Source |
|---------|--------|--------|
| Section 2 Configuration | Expand `GEPAConfig` table to include `MergeConfig`, `RefinerConfig`, `TrackingConfig` fields | GEPA source lines 719-813 |
| Section 2 Configuration | Add `EngineConfig` fields: `run_dir`, `parallel`, `max_workers`, `cache_evaluation`, `cache_evaluation_storage`, `capture_stdio`, `frontier_type`, `candidate_selection_strategy` | GEPA source lines 443-494 |
| Section 2 Configuration | Add `ReflectionConfig` fields: `skip_perfect_score`, `perfect_score`, `reflection_minibatch_size`, `module_selector` | GEPA source lines 693-716 |
| Section 6 Evaluator Protocol | **DELETE** this entire section | Moved to `evaluator-implementations.md` |
| All sections | Add note about `str` candidate mode (evaluator receives `str` when `seed_candidate` is a string) | GEPA source lines 1130-1133 |

**Note on stopping conditions:** Add a new subsection under Configuration covering stopping conditions. The current file omits this entirely; GEPA raises `ValueError` if no stopping condition is provided (line 1229-1233). The preset factories already set `max_metric_calls` so this only matters when using raw `GEPAConfig`.

---

### `references/evaluator-implementations.md` — Create (from `evaluator-examples.md` Sections 1–4 + 6)

This file consolidates the evaluator protocol definition with the three implementation templates. It contains:

1. **Evaluator Protocol** — H1 title + purpose statement, then the corrected protocol definition sourced from `evaluator-examples.md` Section 1 but corrected against GEPA source:
   - Actual signature: `(candidate: str | dict[str, str], example=None, **kwargs) -> float | tuple[float, dict]`
   - Two valid return forms: score-only `float` OR `(score, side_info)` tuple
   - `example` is `None` in single-task mode (`dataset=None`)
   - `opt_state: OptimizationState` is a reserved injected kwarg for warm-starting
   - `oa.log()` as alternative ASI channel (captured under `"log"` key)
   - `capture_stdio=True` in `EngineConfig` as another ASI channel (captured under `"stdout"`/`"stderr"`)

2. **Classification Evaluator (Complete)** — Moved verbatim from `evaluator-examples.md` Section 2

3. **Agent-Definition Evaluator (Skeleton)** — Moved verbatim from `evaluator-examples.md` Section 3

4. **Skill Evaluator (Skeleton)** — Moved verbatim from `evaluator-examples.md` Section 4

5. **Common Evaluator Mistakes** — Moved from `evaluator-examples.md` Section 6, expanded with 3 new entries from GEPA codebase:
   - Raising exceptions inside evaluators when per-example failure is expected (use `raise_on_exception=False` in `EngineConfig` to catch and score as 0.0 instead)
   - Mixing return types inconsistently (some calls return `float`, others return `(float, dict)`) — GEPA normalizes both but ASI is absent for score-only returns
   - Calling `oa.log()` from a child thread without propagating log context via `get_log_context()` / `set_log_context()` — output is silently discarded with a warning

**What is NOT included here:** ASI design, field naming conventions, and ASI best practices — those go to `asi-payload.md`.

---

### `references/asi-payload.md` — Create (from `evaluator-examples.md` Section 5 + GEPA source)

This file consolidates all ASI guidance. It contains:

1. **Purpose statement:** ASI is "the gradient for text optimization" — the structured evidence that tells the reflection LLM why a candidate failed and how to fix it.

2. **Two delivery mechanisms** (new content from GEPA source):
   - Return `(score, side_info_dict)` tuple from evaluator — explicit, full control
   - Call `oa.log(...)` inside evaluator — captured under `"log"` key automatically
   - `capture_stdio=True` in `EngineConfig` — captures `print()` under `"stdout"`/`"stderr"`

3. **SideInfo structure** (expanded from GEPA source `SideInfo` docstring, lines 171-229):
   - `"scores"` key — multi-objective metrics for Pareto tracking (all values must be "higher is better")
   - Contextual fields — `"Input"`, `"Output"`, `"Expected"`, `"Feedback"`, `"Error"`, `"Reasoning"`
   - Parameter-specific info — `"<param_name>_specific_info"` dicts with their own `"scores"` and fields
   - Images via `Image()` class — for visual feedback with VLM reflection models

4. **Reserved keys** (new content from GEPA source, lines 432-437, 957-975):
   - `"log"` — used by `oa.log()` capture
   - `"stdout"` — used by `capture_stdio=True`
   - `"stderr"` — used by `capture_stdio=True`
   - Collision behavior: GEPA renames colliding keys to `_gepa_log`, `_gepa_stdout`, `_gepa_stderr` with a runtime warning

5. **Field naming conventions** — Moved verbatim from `evaluator-examples.md` Section 5 (snake_case, `_score`, `_raw`, `_results`, `_count`, `missing_`, `failing_` suffixes)

6. **Minimal and rich ASI examples** — Moved from `evaluator-examples.md` Section 5

7. **Thread-safe logging** (new content from GEPA source, lines 262-343):
   - `oa.log()` is thread-safe within the main evaluator thread
   - Child threads require explicit context propagation via `get_log_context()` / `set_log_context()`
   - `oa.log()` outside evaluator context emits a warning and discards output

8. **`OptimizationState` warm-starting** (new content from GEPA source, lines 232-255):
   - Add `opt_state: OptimizationState` to evaluator signature to receive top-K historical evaluations
   - Use `opt_state.best_example_evals[0]["side_info"]` to warm-start from previous best results

---

### `references/evaluator-examples.md` — Delete

All content redistributed:
- Section 1 (Protocol) → `evaluator-implementations.md` (corrected)
- Section 2 (Classification) → `evaluator-implementations.md`
- Section 3 (Agent-Definition skeleton) → `evaluator-implementations.md`
- Section 4 (Skill skeleton) → `evaluator-implementations.md`
- Section 5 (ASI best practices) → `asi-payload.md`
- Section 6 (Common mistakes) → `evaluator-implementations.md`

---

## 3. New Content to Write

All new content derives from GEPA source file `gepa/src/gepa/optimize_anything.py`. No content is invented.

### For `SKILL.md` Section 3 — Anatomy corrections

**Corrected evaluator protocol paragraph** (replaces lines 69-79):

```
Follow the actual GEPA evaluator protocol from `gepa.optimize_anything.Evaluator`:

- Signature: `(candidate: str | dict[str, str], example=None, **kwargs) -> float | tuple[float, dict]`
- `candidate` type mirrors `seed_candidate`: `str` if a string was passed, `dict[str, str]` if a dict was passed.
- `example` is omitted entirely in single-task mode (`dataset=None`); present in multi-task and generalization modes.
- Return either a bare `float` score, or a `(score, asi)` tuple. Score-only returns are valid when using `oa.log()`.
- Declare `opt_state: OptimizationState` in the signature to receive historical best evaluations for warm-starting.
```

**Seedless mode** (new bullet in optimization modes list):

```
- Seedless mode: pass `seed_candidate=None` with a required `objective`; the reflection LLM generates the initial candidate. Useful for exploratory tasks where the solution space is large and no starting artifact exists.
```

**Config anatomy correction** (replaces line 57):

```
- `config`: `GEPAConfig` composed from `EngineConfig`, `ReflectionConfig`, and optionally `MergeConfig`, `RefinerConfig`, `TrackingConfig`.
```

### For `SKILL.md` Section 5 — New structural rules

Five new rules sourced from GEPA codebase:

1. **Stopping condition rule:** `MUST NOT create a raw `GEPAConfig` without setting `max_metric_calls` or `stop_callbacks`; GEPA raises `ValueError` if no stopping condition is present. Preset factories satisfy this automatically.`

2. **Thread-safe logging rule:** `MUST NOT call `oa.log()` from child threads spawned inside an evaluator without first propagating the log context via `oa.get_log_context()` / `oa.set_log_context()`. Calls outside context are silently discarded.`

3. **ASI reserved key rule:** `MUST NOT use `"log"`, `"stdout"`, or `"stderr"` as keys in the returned ASI dict. These are reserved by GEPA's capture mechanism; conflicts cause key renaming with a runtime warning.`

4. **Disk cache rule:** `MUST NOT set `cache_evaluation_storage="disk"` without also setting `run_dir` in `EngineConfig`; raises `ValueError`.`

5. **Non-serializable ASI rule:** `MUST NOT include non-JSON-serializable values in the ASI dict unless using `Image()` for VLM feedback. Non-serializable values prevent disk caching and may cause errors in experiment tracking.`

### For `SKILL.md` Section 7 — New common mistakes rows

Five new rows (bringing total to 17, satisfying the 6+ requirement with room to spare):

| Mistake | Problem | Fix |
|---------|---------|-----|
| Raising exceptions for per-example failures inside evaluator | When `raise_on_exception=True` (default), any exception terminates the optimization run. Per-example failures are normal and should be scored as 0.0. | Catch expected failures, return `(0.0, {"error": str(e)})`, and set `EngineConfig(raise_on_exception=False)` only for truly fault-tolerant runs. |
| Using `oa.log()` in a child thread without propagating context | Log output is silently discarded with a warning. Diagnostic data from concurrent evaluations is lost. | Capture the log context with `ctx = oa.get_log_context()` before spawning, then call `oa.set_log_context(ctx)` inside the child thread. |
| Creating raw `GEPAConfig` without any stopping condition | GEPA raises `ValueError` before the first evaluation. The run never starts. | Set `max_metric_calls` in `EngineConfig`, or pass `stop_callbacks` to `GEPAConfig`. Preset factories set this automatically. |
| Using `"log"`, `"stdout"`, or `"stderr"` as ASI dict keys | GEPA reserves these keys for captured output. Collisions cause key renaming to `_gepa_log` etc. with a runtime warning and confusion in downstream ASI analysis. | Use distinct field names (e.g., `"run_log"`, `"program_output"`) for evaluator-owned content. |
| Setting `cache_evaluation_storage="disk"` without `run_dir` | GEPA raises `ValueError` at configuration validation time. | Either set `EngineConfig(run_dir="path/to/dir")`, or use `cache_evaluation_storage="memory"` (the default for non-file runs). |

---

## 4. Content to Remove

| Location | Content | Reason |
|----------|---------|--------|
| `evaluator-examples.md` | Entire file | Split into two focused reference files |
| `api-patterns.md` Section 6 | Evaluator Protocol section (lines 462–557) | Moved to `evaluator-implementations.md`; triplication resolved |
| `SKILL.md` lines 69-79 | Template evaluator list (`llm_classification_evaluator`, etc.) | These are implementation detail; anatomize in Section 3 via reference pointer. Keep one-line mention, remove detailed list. |
| `api-patterns.md` Section 6 custom evaluator example | Custom evaluator code block (lines 532-557) | Kept in `evaluator-implementations.md`; no need to maintain it in two reference files |

---

## 5. Content to Consolidate

### Evaluator Protocol Triplication → Single Source

Currently defined in three places:
- `SKILL.md` lines 69-79 (summary form)
- `api-patterns.md` Section 6 (full EvaluatorFn type alias + parameters)
- `evaluator-examples.md` Section 1 (full protocol + parameter descriptions)

**Resolution:** Authoritative definition lives in `evaluator-implementations.md` Section 1. `SKILL.md` keeps a corrected one-paragraph summary pointing to the reference. `api-patterns.md` removes its evaluator protocol section entirely (it describes API shapes; evaluator design belongs in the evaluator reference).

### ASI Content Scattering → Single Source

Currently spread across:
- `SKILL.md` lines 175-182 (ASI rules, structural rules section)
- `api-patterns.md` Section 6 (ASI fields in template descriptions)
- `evaluator-examples.md` Section 5 (ASI best practices, field naming)

**Resolution:** All design guidance and naming conventions live in `asi-payload.md`. `SKILL.md` keeps its ASI rules in Section 5 as hard constraints (these are rules, not guidance — they belong in the rules section). The `api-patterns.md` template descriptions keep their brief ASI field lists (e.g., "ASI fields: `response`, `expected`, `match`, `input`") because they contextualize the template behavior — these are not duplicates of the design guidance.

### Common Mistakes Fragmentation → Two Cohesive Tables

Currently split:
- `SKILL.md` Section 7: 12 high-level workflow mistakes
- `evaluator-examples.md` Section 6: 6 evaluator-specific mistakes with code

**Resolution:** `SKILL.md` Section 7 becomes the comprehensive workflow mistakes table (17 rows: 12 existing + 5 new GEPA pitfalls). `evaluator-implementations.md` contains evaluator implementation mistakes with code examples (7 rows: 6 existing + 1 new thread-safety mistake). This preserves the code-level detail in the reference while keeping the structural failures in the body.

---

## 6. SKILL.md Specific Changes

### Section 3 — Anatomy/Structure (targeted edits)

**Lines 69-87 — Evaluator protocol block:** Replace with corrected paragraph:

```markdown
Follow the GEPA evaluator protocol defined by `gepa.optimize_anything.Evaluator`:

- Signature: `(candidate: str | dict[str, str], example=None, **kwargs) -> float | tuple[float, dict]`
- `candidate` matches the `seed_candidate` type: plain `str` for string seeds, `dict[str, str]` for dict seeds.
- `example` is omitted in single-task mode (`dataset=None`); present per-item in multi-task and generalization modes.
- Return a bare `float` score OR a `(score, asi)` tuple. Use `oa.log()` as an alternative ASI channel.
- Declare `opt_state: OptimizationState` in the signature to receive the top-K historical evaluations for warm-starting.

Consult `skills/optimize-anything/references/evaluator-implementations.md` for complete implementations.
```

**Lines 57 — Config line:** Replace `EngineConfig` and `ReflectionConfig` mention:

```markdown
- `config`: `GEPAConfig` composed from `EngineConfig`, `ReflectionConfig`, and optionally `MergeConfig`, `RefinerConfig`, `TrackingConfig`.
```

**Lines 14-20 — Optimization modes:** Extend the list with seedless mode:

```markdown
- Seedless mode: no starting artifact; pass `seed_candidate=None` with `objective`; the reflection LLM bootstraps the first candidate.
```

**Lines 89-93 — Mode to data organization:** Extend to include single-task clarification:

```markdown
- Single-task mode: `dataset=None`; evaluator called once per iteration without `example`; candidate is the solution.
```

### Section 5 — Structural Rules (additions)

After the "Evaluator protocol rules" block (after line 166), add a new rule block:

```markdown
Stopping condition rules:

- MUST set `max_metric_calls` in `EngineConfig` or `stop_callbacks` in `GEPAConfig` when using raw config. Preset factories satisfy this automatically.
- MUST NOT set `cache_evaluation_storage="disk"` without `run_dir` in `EngineConfig`.
- MUST NOT set `skip_perfect_score=True` in `ReflectionConfig` without also setting `perfect_score` to a float value.

ASI capture rules:

- MUST NOT use `"log"`, `"stdout"`, or `"stderr"` as keys in the returned ASI dict.
- MUST NOT call `oa.log()` from child threads without propagating the log context.
- MUST NOT return non-JSON-serializable values in ASI when disk caching or experiment tracking is enabled.
```

### Section 6 — Validation Checklist (additions)

Add after line 233:

```markdown
- [ ] Confirm evaluator does not raise exceptions for per-example failures; catch and return `(0.0, {"error": ...})` instead.
- [ ] Confirm ASI dict does not use reserved keys `"log"`, `"stdout"`, or `"stderr"`.
- [ ] Confirm `GEPAConfig` with no preset has at least one stopping condition (`max_metric_calls` or `stop_callbacks`).
```

### Section 7 — Common Mistakes (additions)

Append 5 new rows (specified in Section 3 above).

### Section 8 — References Usage (full replacement)

Replace current two-entry block with four entries:

```markdown
- **`skills/optimize-anything/references/api-patterns.md`** — Consult for `optimize_anything()` function signatures, `GEPAConfig` / `EngineConfig` / `ReflectionConfig` / `MergeConfig` / `RefinerConfig` / `TrackingConfig` structures, `seed_candidate` format by artifact type, optimization mode examples, result object access, stopping conditions, and the public import surface.

- **`skills/optimize-anything/references/evaluator-implementations.md`** — Consult when implementing evaluators: the authoritative protocol definition, classification evaluator (complete), agent-definition evaluator (skeleton), skill format evaluator (skeleton), and a catalog of common evaluator implementation mistakes with corrected code.

- **`skills/optimize-anything/references/asi-payload.md`** — Consult when designing ASI payloads: delivery mechanisms (`oa.log()`, return tuple, `capture_stdio`), SideInfo structure (`"scores"`, contextual fields, parameter-specific info, `Image()`), reserved key collision behavior, field naming conventions, thread-safe logging, and warm-starting via `OptimizationState`.

- **`skills/optimize-anything/references/api-patterns.md`** and **`skills/optimize-anything/references/evaluator-implementations.md`** together cover all implementation surfaces. Prefer this SKILL body for default execution. Escalate to reference files only when edge cases, cross-task coupling, or evaluator complexity exceeds the default path.
```

---

## 7. Validation Against Skill-Development Checklist

| Requirement | Satisfied After Restructure? | Notes |
|-------------|------------------------------|-------|
| `SKILL.md` exists at `skills/optimize-anything/SKILL.md` | ✅ | Unchanged path |
| YAML frontmatter with exactly `name` + `description` | ✅ | Unchanged frontmatter |
| `name` matches directory | ✅ | `optimize-anything` |
| `description` starts with "This skill should be used when" | ✅ | Unchanged |
| Eight body sections in correct order | ✅ | No section additions or removals |
| Body word count 1,500–3,000 | ⚠️ | Current body is ~1,900 words. New content in Sections 3, 5, 7, 8 adds ~400 words, estimated final ~2,300 words. Within range; verify after edits. |
| No second person language | ✅ | Current file clean; new content follows same convention |
| Validation checklist uses checkbox format | ✅ | Section 6 uses `- [ ]` throughout |
| Common mistakes table has 6+ entries | ✅ | Currently 12; grows to 17 with new rows |
| `references/` directory exists | ✅ | Will contain 3 files after restructure |
| Each reference file has H1 title + purpose statement + no frontmatter | ✅ | `api-patterns.md` already satisfies; new files must be written to satisfy |
| Each reference file explicitly mentioned in References Usage | ✅ | Section 8 updated to list all four |
| Imperative voice throughout | ✅ | Maintained; new content follows same convention |

**One item requiring attention:** The `evaluator-implementations.md` and `asi-payload.md` files will be authored fresh. Their opening H1 title and purpose statement must be written explicitly (not just moved content with no header). Both files must confirm no second-person language in their bodies.

---

## 8. Execution Order

The implementation agent should execute in this order to avoid a broken intermediate state:

1. Create `references/asi-payload.md` (new file, no dependencies)
2. Create `references/evaluator-implementations.md` (new file, consolidates from `evaluator-examples.md`)
3. Modify `references/api-patterns.md` (remove Section 6, expand Section 2)
4. Modify `SKILL.md` (correct protocol, add new rules, update common mistakes, update Section 8)
5. Delete `references/evaluator-examples.md` (only after Steps 1–2 are verified complete)

Do not delete `evaluator-examples.md` until both new reference files are written and verified to contain all mapped content.

---

## 9. Open Questions and Unresolved Risks

1. **`EvaluatorFn` type alias in `src/optimize_anything/evaluators/base.py`:** The local library still defines `EvaluatorFn = Callable[[dict[str, str], dict[str, Any]], tuple[float, dict[str, Any]]]`. This is narrower than the actual GEPA `Evaluator` protocol which accepts `str | dict[str, str]` and returns `float | tuple[float, dict]`. The skill should describe the actual GEPA protocol while noting that the local library's `EvaluatorFn` type alias enforces a stricter subset. The implementation agent should check whether `base.py` needs updating or just noting.

2. **`skip_perfect_score` and `perfect_score` interaction:** The source (line 709-710) shows `skip_perfect_score: bool = False` and `perfect_score: float | None = None`. Setting `skip_perfect_score=True` without `perfect_score` is a pitfall flagged in the research but the exact behavior (what GEPA does with `None`) should be verified against the core engine before documenting it as a hard rule.

3. **`run_optimization` and `run_from_file` local wrapper behavior:** These wrappers exist in the local library but the synthesis does not have full visibility into whether they have been updated to pass through the full GEPA `Evaluator` protocol (including score-only returns, `oa.log()`, and `opt_state`). Implementation agent should verify that the local wrappers do not inadvertently restrict the protocol.

4. **Word count after edits:** Final SKILL.md word count should be measured after all edits to confirm it stays within 1,500–3,000 words. The additions in Sections 3, 5, 6, 7, and 8 are estimated to bring the total to ~2,300 words, but this is an estimate and must be verified.
