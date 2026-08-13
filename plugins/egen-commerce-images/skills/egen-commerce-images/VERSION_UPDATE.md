# Version Update

## v0.3.0 - 2026-08-13

### Summary

Replaced the multi-turn Step 2-9 interview flow with two fixed Markdown table forms after product image upload, while keeping Step 1 as a separate product-image calibration gate.

### Changes

- Added a product information table for product facts and optional product document paths.
- Added a task options table with numbered choices and fixed enum values for country/language, platform, knowledge style, image types, ratio, quantity, and extra requirements.
- Clarified that Markdown tables simulate an in-chat form and do not provide native dropdown menus.
- Added parsing and validation rules for table responses, including multi-select image types, `全选`, missing `其他` values, required task options, and generation quantity checks.
- Updated Step 10 to require completed table validation before outputting the analysis plan.
- Kept the Step 1 upload-only rule, knowledge image boundaries, same-type reference selection, compliance guardrails, and top-right logo safe area constraint unchanged.

### Files Updated

- `.codex-plugin/plugin.json`
- `SKILL.md`
- `VERSION_UPDATE.md`

## 2026-08-06

### Summary

Clarified that final ecommerce image execution must use the built-in `image_gen.imagegen` tool instead of external image-generation APIs, while reference prompts remain generic and tool-neutral.

### Changes

- Standardized all final image-generation wording around `image_gen.imagegen`.
- Kept reference prompt document headings generic, without model, tool, or API binding.
- Added an explicit Step 11 rule: use the built-in `image_gen.imagegen` tool for image generation.
- Added explicit prohibitions against calling external image-generation APIs, writing scripts that invoke image APIs, or asking users for API keys.
- Updated ratio and single-request limit wording to follow the capabilities of the active `image_gen.imagegen` environment.
- Updated the unavailable-generation fallback to refer specifically to `image_gen.imagegen` availability.

### Files Updated

- `SKILL.md`
- `references/style-prompts/STYLE1_PROMPTS.md`
- `references/style-prompts/STYLE2_PROMPTS.md`
- `references/style-prompts/STYLE3_PROMPTS.md`
- `references/style-prompts/STYLE4_PROMPTS.md`
- `references/style-prompts/STYLE5_PROMPTS.md`
- `references/style-prompts/STYLE6_PROMPTS.md`
- `references/style-prompts/STYLEhero_PROMPTS.md`
- `VERSION_UPDATE.md`
