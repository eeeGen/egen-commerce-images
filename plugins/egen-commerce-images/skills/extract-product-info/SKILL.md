---
name: extract-product-info
description: Extract and reconcile structured product information from a local folder of product images, with optional supplier attributes, parameter tables, marketplace copy, or user corrections. Use when the user provides an image-folder path and asks to read images in order, complete product information image by image, organize product facts, compare image evidence with Product Attributes, or produce a conflict-aware product information summary. Run independently from ecommerce image generation and SEO image naming.
---

# Extract Product Info

Use Chinese by default. Run this as a self-contained product-information task. Do not start the `egen-commerce-images` image-generation workflow, open its product form, generate images, or rename source images.

## Input Contract

Require only:

- `folder_path`: a local folder containing product images.
- `supplementary_info` (optional): Product Attributes tables, supplier parameter sheets, marketplace copy, product documents, or explicit user corrections.

Do not ask the user to reproduce the built-in template. Ask a follow-up question only when a missing path prevents access or a material conflict requires the user's decision.

## Fixed Template

Use this exact field order:

```text
产品名称：
品牌：
商品类目：
材质/成分：
尺寸/规格：
颜色/款式：
包装清单：
适用人群：
使用场景：
核心卖点：
需要避免的表达：
其他补充：
```

## Workflow

1. Enumerate `.png`, `.jpg`, `.jpeg`, and `.webp` files directly under `folder_path`. Ignore non-image files unless the user explicitly identifies one as supplementary information.
2. Sort filenames in natural order so numeric portions sort numerically, for example `2.jpg` before `10.jpg`. State the total image count and processing order before inspection.
3. Inspect one image at a time. Immediately after each image, refresh the current template state and append a filename-specific record of facts newly added, confirmed, repeated, contradicted, or still unclear.
4. Continue until every enumerated image has been processed. Never silently skip an unreadable or unsupported image; record the failure against that filename.
5. Reconcile all image findings with `supplementary_info`, preserving source provenance for disputed values.
6. Produce the required final output only after all images are processed, unless an actual tool or context limit prevents completion.

## Evidence And Conflict Rules

- Treat an explicit user correction or an instruction such as `以以下信息为准` as authoritative for the affected field, while still recording meaningful conflicts.
- Treat structured supplementary attributes as higher priority than image marketing copy. If supplementary sources conflict with each other, do not choose silently.
- Treat legible model plates, packaging labels, dimensions, and accessory photos as image evidence. Distinguish what is physically visible from what appears only as promotional text.
- Treat claims such as `AI芯片`, `静音降噪`, `长续航`, `快速充气`, or `控温护胎` as marketing wording only unless authoritative proof is supplied. They may appear under `核心卖点` or `需要避免的表达`, but not as verified test facts, certifications, or guarantees.
- Preserve values that lack units and append `（单位待确认）`, for example `电池容量 1800（单位待确认）`.
- Mark possible translations or brand variants without resolving them, for example `欧睿达 / Orida 可能为中文与英文品牌名，需确认展示用品牌名`.
- Do not invent brand, material, dimensions, compatibility, accessories, certifications, origin, platform endorsement, reviews, test results, safety guarantees, or package contents.
- Keep unknown fields as `待填写` or `待确认`.

## Context Budget And Continuation

Do not assume a fixed per-task image-count limit. Image inputs consume model context and tool budgets, so keep each per-image record compact and periodically consolidate confirmed facts into the current template.

Process the full folder in one task when the environment permits. If an actual limit blocks completion, stop only after a completed image and output a `续接检查点` containing:

- Folder path and supplementary information source.
- Processed filenames in order.
- Remaining filenames and the next filename.
- Current filled template.
- Current per-image records.
- Current conflicts and open questions.

Set `complete: false` in that checkpoint. A later task or subagent can resume by re-enumerating the same folder, verifying the processed filenames, and continuing from the next image. On normal completion, do not add a checkpoint section.

## Final Output Contract

Return exactly these three sections on normal completion:

1. `产品信息汇总`: the fully updated fixed template in its original field order.
2. `逐图新增信息记录`: one compact entry per filename in processing order, including confirmed additions and any conflict or unreadable-image note.
3. `矛盾/歧义/待确认项`: list every unresolved discrepancy, missing unit, uncertain translation, or unsupported claim. If none exist, write `未发现明显冲突`.

If a conflict or ambiguity changes a product-facing field, ask one focused confirmation question after the three sections. Do not continue into image generation in the same task.
