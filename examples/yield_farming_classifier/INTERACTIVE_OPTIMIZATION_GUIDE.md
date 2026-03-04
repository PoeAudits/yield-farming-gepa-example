# Interactive Prompt Optimization Guide

This document explains how to operate the interactive prompt optimization loop for the yield farming classifier. The system uses GEPA (a prompt optimization engine) with a human-in-the-loop proposer that pauses between iterations so you can review failures and write improved prompts.

You are the "reflection engine" — the part of the system that analyzes classification failures, identifies patterns, and proposes targeted prompt changes.

---

## What the system does

The yield farming classifier reads crypto Telegram/Discord messages and outputs `yes` or `no` — whether the message describes an actionable yield farming opportunity. A system prompt controls the LLM's classification behavior. The goal is to iteratively refine this prompt to maximize classification accuracy across a labeled validation set.

Each optimization iteration:

1. GEPA evaluates the current prompt against a mini-batch of labeled examples
2. The system writes a structured failure analysis report (`report.md`)
3. You review the report, analyze failure patterns, and write a revised prompt (`new_prompt.md`)
4. GEPA evaluates the new prompt and accepts it if it scores better on the mini-batch

The optimization pauses between steps 2 and 3, waiting for you.

---

## Directory structure

All artifacts live under the handoff directory:

```
examples/yield_farming_classifier/handoff/
  session_state.json       # Iteration counter, score history, metadata
  gepa_state.bin           # GEPA optimizer state (binary, do not modify)
  iteration_001/
    report.md              # Failure analysis for the seed prompt
    prompt_used.md         # The prompt that was evaluated
    new_prompt.md          # YOUR revised prompt (you write this)
  iteration_002/
    report.md              # Failure analysis for your first revision
    prompt_used.md         # The prompt that was evaluated
    new_prompt.md          # YOUR next revision (you write this)
  ...
```

---

## Your workflow

### Step 1: Read the report

After each evaluation, find the latest `iteration_NNN/report.md`. This report contains:

| Section | What it tells you |
|---------|-------------------|
| **Aggregate scores** | Current accuracy, false positive count, false negative count |
| **Score history** | Table of all iterations with accuracy and delta from previous |
| **False positives** | Messages the model incorrectly classified as `yes` (should be `no`), grouped by source file |
| **False negatives** | Messages the model incorrectly classified as `no` (should be `yes`), grouped by source file |
| **Edge cases** | Low-confidence or ambiguous examples |
| **Prompt refinement suggestions** | Heuristic analysis of failure patterns with suggested directions |
| **GEPA acceptance note** | Reminder about GEPA's acceptance criterion |

### Step 2: Analyze failure patterns

Look for systematic errors — categories of messages the prompt handles poorly:

- **False positives (model says `yes`, should be `no`):** The prompt is too permissive for these cases. Look for common patterns — vague marketing language the model mistakenly treats as actionable, generic platform promotions with APY numbers, past-tense reward announcements.

- **False negatives (model says `no`, should be `yes`):** The prompt is too restrictive for these cases. Look for legitimate opportunities the model rejects — perhaps deposit bonuses, tiered reward programs, or launch announcements with participation details.

- **Source file groupings matter:**
  - `agreed` — examples where the original classifier and human annotator agreed on the label. Failures here suggest clear prompt gaps.
  - `disagreed` — examples where they disagreed. These are genuinely harder cases.
  - `low_confidence` — examples the original classifier was uncertain about. Failures here are expected but still worth addressing.

- **Read the full message text** in each failure entry. Understand *why* the model got it wrong. Is the prompt missing a rule? Is an existing rule ambiguous? Does the model need a more explicit boundary?

### Step 3: Write the revised prompt

Write the full, complete prompt text to `iteration_NNN/new_prompt.md` in the current iteration directory.

**Critical rules for `new_prompt.md`:**

1. **Write the ENTIRE prompt.** This is not a diff or patch — it is the complete replacement prompt. The system reads this file and uses its full content as the new system prompt.

2. **Plain text only.** No markdown headers, no frontmatter, no wrapper. Just the prompt text exactly as the LLM should receive it.

3. **The file goes in the CURRENT iteration directory.** If the latest report is `iteration_001/report.md`, write your prompt to `iteration_001/new_prompt.md`.

4. **The prompt must produce single-token output.** The evaluator expects the LLM to respond with exactly `yes` or `no`. Your prompt must maintain this constraint (typically with "Respond with only: yes or no" at the end).

### Step 4: Resume

After writing `new_prompt.md`, the human operator runs:

```
make optimize-resume
```

This evaluates your new prompt, updates the score history, and generates the next iteration's report. The cycle repeats.

---

## How to make effective prompt changes

### General strategy

1. **Be surgical.** Change one thing at a time when possible. If you change five rules simultaneously and accuracy drops, you won't know which change caused the regression.

2. **Address the highest-impact failure pattern first.** If 8 of 12 false positives share the same pattern (e.g., vague marketing with "up to X% APY"), fix that one pattern rather than trying to address all 12.

3. **Use the exact language from failure examples.** If messages containing "earn more" are false positives, add "earn more" as an explicit example in the NO rules rather than adding abstract criteria.

4. **Balance FP and FN fixes.** Tightening criteria to reduce false positives often increases false negatives and vice versa. Check both sides after each change.

5. **Preserve what works.** If accuracy is 0.85 and you're fixing edge cases, keep the core structure intact. Rewriting the entire prompt risks regressing on cases that already work.

### Common prompt refinement patterns

| Failure pattern | Fix approach |
|----------------|-------------|
| FP: Vague marketing treated as actionable | Add the specific phrase as a NO example; tighten the "actionable" definition |
| FP: Generic platform promotion with APY | Add explicit rule that "up to X%" without a specific product/asset is NO |
| FP: Past-tense rewards treated as current | Strengthen past-tense exclusion rule with more examples |
| FN: Deposit bonuses rejected | Add or strengthen the exception rule for deposit bonuses/matches |
| FN: Launch announcements with details rejected | Add explicit YES rule for launches that include participation instructions |
| FN: Tiered reward programs rejected | Ensure YES rule 4 is prominent and well-exampled |
| Mixed: Certain source categories fail disproportionately | Add rules targeting the specific language patterns in that source |

### Understanding GEPA's acceptance criterion

GEPA evaluates your new prompt on a **mini-batch** (not the full dataset) and accepts it only if the new score is **strictly greater** than the old score on that mini-batch. This means:

- A prompt that improves overall accuracy might still be **rejected** if it doesn't improve on the specific mini-batch GEPA samples
- If your prompt is rejected, it doesn't necessarily mean it's worse — it may just not have improved on the sampled examples
- After rejection, GEPA keeps the old prompt. The next iteration's report will still reflect the old prompt's performance
- Don't be discouraged by rejections. Try again with a different approach or a more targeted change

---

## Reading the current prompt

The evaluated prompt is saved in `iteration_NNN/prompt_used.md` with a markdown header:

```markdown
## system_prompt

[full prompt text here]
```

The content under the `## system_prompt` header is the actual prompt that was sent to the LLM. When writing `new_prompt.md`, write only the prompt text — no `## system_prompt` header.

---

## Score interpretation

- **Accuracy:** Fraction of examples classified correctly (1.0 = perfect). This is the primary metric.
- **False positives:** Count of messages wrongly classified as `yes`. These are messages that are NOT actionable yield opportunities but the model said they were.
- **False negatives:** Count of messages wrongly classified as `no`. These are genuine yield opportunities the model missed.
- **Delta:** Change in accuracy from the previous iteration. Positive = improvement.

The score history table in the report tracks these across all iterations so you can see the optimization trajectory.

---

## The seed prompt

The optimization starts from `examples/yield_farming_classifier/best_prompt.md`. This is a 62-line classification prompt structured as:

1. Role and task definition
2. Output format constraint (`yes` or `no` only)
3. Decision principle (strict, default to NO)
4. YES rules (5 categories of actionable opportunities)
5. NO rules (6 categories of common false positive traps)
6. Quick checklist (WHAT/WHERE/WHICH asset test)
7. Final output constraint

The seed prompt already encodes substantial domain knowledge. Your refinements build on this foundation.

---

## Dataset characteristics

The validation set contains examples from three sources:

| Source | Description | Typical difficulty |
|--------|-------------|-------------------|
| `agreed` | Original classifier and human annotator agreed | Easier — clear-cut examples |
| `disagreed` | Original classifier and human annotator disagreed | Harder — ambiguous cases |
| `low_confidence` | Original classifier was uncertain | Moderate — borderline examples |

Each example includes:
- `text` — the full message content
- `label` — ground truth (`yes` or `no`)
- `explanation` — human reasoning for the label
- `predicted_category` — what the original classifier predicted
- `confidence` — original classifier's confidence
- `source_file` — which source dataset (`agreed`, `disagreed`, `low_confidence`)

The report extracts these fields into the failure analysis when available.

---

## Commands reference

| Command | What it does |
|---------|-------------|
| `make optimize-interactive` | Start a new session. Evaluates seed prompt, writes first report, exits. |
| `make optimize-resume` | Resume after writing `new_prompt.md`. Evaluates new prompt, writes next report, exits. |

Both commands accept flags via the underlying script:

```bash
# Start with mock evaluator (no API calls, deterministic scoring)
uv run python examples/yield_farming_classifier/run_interactive.py start --mock

# Resume with mock evaluator
uv run python examples/yield_farming_classifier/run_interactive.py resume --mock

# Use a custom handoff directory
uv run python examples/yield_farming_classifier/run_interactive.py start --handoff-dir /tmp/my-session

# Start with a different seed prompt
uv run python examples/yield_farming_classifier/run_interactive.py start --prompt path/to/prompt.md
```

---

## Troubleshooting

| Problem | Cause | Fix |
|---------|-------|-----|
| "Session already exists" on start | `session_state.json` or `gepa_state.bin` already present | Use `resume` instead, or delete the handoff directory to start fresh |
| "No session state found" on resume | No prior `start` was run | Run `make optimize-interactive` first |
| "new_prompt.md not found" on resume | You haven't written the revised prompt yet | Write the full prompt to `iteration_NNN/new_prompt.md` |
| Prompt rejected by GEPA | New prompt didn't score higher on the mini-batch | Not necessarily bad — try a different approach. See acceptance criterion section above |
| Missing API key error | `OPENAI_API_KEY` not set | Set the environment variable, or use `--mock` for testing |

---

## Summary of the cycle

```
1. make optimize-interactive          # First time only
   ↓
2. Read handoff/iteration_001/report.md
   ↓
3. Analyze failures, write new prompt
   ↓
4. Save to handoff/iteration_001/new_prompt.md
   ↓
5. make optimize-resume
   ↓
6. Read handoff/iteration_002/report.md
   ↓
7. Analyze failures, write new prompt
   ↓
8. Save to handoff/iteration_002/new_prompt.md
   ↓
9. make optimize-resume
   ↓
   ... repeat until satisfied with accuracy ...
```
