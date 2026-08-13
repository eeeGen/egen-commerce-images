# Version Update

## v0.4.2 - 2026-08-13

### Summary

Added an explicit shutdown path for the local browser form service so Codex can close the background process after reading the saved product task JSON into context.

### Changes

- Added a `/shutdown` endpoint to `scripts/product_form_server.py`.
- Printed the service `PID` on startup for precise fallback cleanup.
- Updated the form workflow to read `FORM_URL`, `LATEST_URL`, `JSON_PATH`, and `PID`.
- Updated Step 3 to close the form server after saved JSON has been captured, before continuing to the analysis plan.
- Updated the plugin manifest version to `0.4.2`.

### Files Updated

- `.codex-plugin/plugin.json`
- `scripts/product_form_server.py`
- `SKILL.md`
- `VERSION_UPDATE.md`

## v0.4.1 - 2026-08-13

### Summary

Fixed the local browser form service instructions so Codex resolves the bundled service script from the skill folder to the plugin root correctly.

### Changes

- Clarified that `product_form_server.py` is stored in the plugin root `scripts/` directory, not under the skill folder.
- Updated Step 2 startup instructions to use `..\..\scripts\product_form_server.py` when resolving relative to `SKILL.md`.
- Updated Step 3 JSON-reading wording to reference the corrected script path.
- Updated the plugin manifest version to `0.4.1`.

### Files Updated

- `.codex-plugin/plugin.json`
- `SKILL.md`
- `VERSION_UPDATE.md`

## v0.4.0 - 2026-08-13

### Summary

Added a local browser form workflow that lets users fill dropdowns, checkboxes, and text fields in the Codex in-app Browser, then saves task data to a local JSON file that Codex reads directly.

### Changes

- Added `scripts/product_form_server.py` to serve the product task form on `127.0.0.1` and save JSON to `%TEMP%\egen-commerce-images\latest-product-task.json`.
- Added `assets/product-task-form.html` with product information fields, task option dropdowns, image type checkboxes, and save status feedback.
- Updated Step 2 to use the local browser form as the primary workflow after product image upload.
- Updated Step 3 to read the saved JSON directly instead of asking users to paste JSON into chat.
- Kept the Markdown two-table workflow as a fallback when the local service or browser is unavailable.
- Updated the plugin manifest version to `0.4.0`.

### Files Updated

- `.codex-plugin/plugin.json`
- `assets/product-task-form.html`
- `scripts/product_form_server.py`
- `SKILL.md`
- `VERSION_UPDATE.md`

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
