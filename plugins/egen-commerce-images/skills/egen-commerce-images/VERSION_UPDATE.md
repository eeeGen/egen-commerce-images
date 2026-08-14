# Version Update

## v0.7.2 - 2026-08-14

### Summary

Changed the ecommerce image output archival rule so final generated images are copied into the product workspace output folder while the Codex default generated-images archive remains intact.

### Changes

- Updated Step 11 to copy generated image files into the product output folder instead of moving them.
- Required the original files under `$CODEX_HOME/generated_images/...` to remain as the Codex default archive.
- Kept the existing output folder naming convention, collision handling, JSON schema, form service, and generation workflow unchanged.
- Updated the plugin manifest version to `0.7.2`.

### Files Updated

- `.codex-plugin/plugin.json`
- `skills/egen-commerce-images/SKILL.md`
- `VERSION_UPDATE.md`

## v0.7.1 - 2026-08-14

### Summary

Improved the StarFlow night product task form by switching the two large form sections through top-bar tabs and moving all save, validation, and split-status messages into the left status rail.

### Changes

- Changed the browser form from showing both `产品信息` and `任务选项` panels at once to a top-bar tab interaction that shows one panel at a time.
- Moved the form status component from the bottom of the form into the left rail so success, error, and processing messages are visible without scrolling.
- Kept the existing JSON schema, save payload, `/save`, `/wait`, form service behavior, and skill workflow unchanged.
- Updated the plugin manifest version to `0.7.1`.

### Files Updated

- `.codex-plugin/plugin.json`
- `assets/product-task-form.html`
- `VERSION_UPDATE.md`
- `docs/plan-archives/2026-08-14-v0.7.1-form-tabs-status-rail.md`

## v0.7.0 - 2026-08-13

### Summary

Added `extract-product-info` as the plugin's third independent skill. It reads product image folders in order, fills a fixed product information template, and reconciles optional supplemental attributes without entering the ecommerce image-generation workflow.

### Changes

- Added the independent `extract-product-info` skill with its own trigger description and UI metadata.
- Built the fixed product information template into the new skill so users only need to provide a folder path and optional supplemental information such as Product Attributes tables.
- Required image-by-image processing in natural filename order, with the current template refreshed and per-file findings recorded after each image.
- Added precedence and provenance rules for user corrections, structured attributes, visible evidence, and image marketing copy, while requiring conflicts, missing units, and possible brand translations to be flagged.
- Added context-budget guidance and a deterministic continuation checkpoint for an actual tool or context limit, without claiming a fixed per-task image count.
- Kept `egen-commerce-images` focused on its existing 11-step ecommerce image-generation workflow and kept `seo-naming` unchanged.
- Defined a self-contained input/output boundary suitable for a future subagent integration, without enabling subagent orchestration in this version.
- Updated the plugin manifest version to `0.7.0`.

### Files Updated

- `.codex-plugin/plugin.json`
- `skills/extract-product-info/SKILL.md`
- `skills/extract-product-info/agents/openai.yaml`
- `VERSION_UPDATE.md`
- `docs/plan-archives/2026-08-13-v0.7.0-product-info-template-workflow.md`

## v0.6.0 - 2026-08-13

### Summary

Aligned the local product task form with the StarFlow STUDIO night-mode interface while keeping the existing form data flow and schema unchanged.

### Changes

- Restyled `product-task-form.html` with the StarFlow night palette, glass panels, compact workbench layout, top brand bar, workflow rail, and dark form controls.
- Embedded the StarFlow night Q mark and assistant character assets inside the plugin so the form does not depend on LogoToolkit local paths.
- Added a restricted `/assets/...` static route to the local form server for read-only plugin asset delivery.
- Kept the existing conditional fields, country-to-platform autofill, image type multi-select, product-info splitting, JSON schema version, `/wait` flow, and save behavior unchanged.
- Updated the plugin manifest version to `0.6.0` and aligned the manifest brand color with the StarFlow night accent.

### Files Updated

- `.codex-plugin/plugin.json`
- `assets/product-task-form.html`
- `assets/skin/Q_night.png`
- `assets/skin/nailong.png`
- `scripts/product_form_server.py`
- `VERSION_UPDATE.md`

## v0.5.0 - 2026-08-13

### Summary

Improved the local browser form workflow with conditional fields, task-specific JSON files, automatic save waiting, deterministic product-info splitting, and final image output relocation rules.

### Changes

- Hid runtime save paths from the browser UI and replaced save messages with user-friendly status text plus timestamp.
- Added conditional display for custom country/language, custom platform, custom image type, and extra requirement content.
- Removed custom knowledge style input from the browser form and fallback table.
- Added deterministic large-text product information splitting into empty product fields.
- Added country-to-platform autofill for Mexico/MercadoLibre and South Africa/Takealot, and defaulted image ratio to `1:1`.
- Changed form saves from a shared `latest-product-task.json` path to task-specific JSON files under `%TEMP%\egen-commerce-images\tasks\`.
- Added `/wait` long polling so Codex can automatically detect a saved form and read the returned `jsonPath`.
- Updated Step 11 to move final generated images out of the Codex generated-images folder into the product output folder with the required marketplace/country/style naming convention.
- Updated the plugin manifest version to `0.5.0`.

### Files Updated

- `.codex-plugin/plugin.json`
- `assets/product-task-form.html`
- `scripts/product_form_server.py`
- `SKILL.md`
- `VERSION_UPDATE.md`

## v0.4.3 - 2026-08-13

### Summary

Fixed the local browser form startup instructions so Codex starts the form service as a background process instead of using a foreground command that can time out and kill the server before the browser opens.

### Changes

- Replaced the foreground `python ..\..\scripts\product_form_server.py` startup example with a `Start-Process` background startup template.
- Added guidance to prefer the Codex bundled Python executable when available.
- Added a failure rule: exit code `124`, missing `FORM_URL`, or a dead printed `PID` means startup failed and must be retried with background startup before opening the browser.
- Updated the plugin manifest version to `0.4.3`.

### Files Updated

- `.codex-plugin/plugin.json`
- `SKILL.md`
- `VERSION_UPDATE.md`

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
