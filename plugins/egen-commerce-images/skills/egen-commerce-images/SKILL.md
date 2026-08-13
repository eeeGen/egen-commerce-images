---
name: egen-commerce-images
description: Create ecommerce product image sets with a Chinese consultative workflow for Amazon, MercadoLibre, Takealot, and extensible marketplaces. Use when the user wants product-photo-based ecommerce image generation, listing visuals, marketplace image suites, localized consumer copy, or built-in image_gen.imagegen outputs for product hero images, selling-point images, structure/spec images, scene images, A+ style images, or similar ecommerce product visuals.
---

# Ecommerce Product Images

## Operating Rules

Use Chinese by default for all user communication, follow-up questions, analysis, and operational guidance. The selected target country and language affect only consumer-facing listing copy, image text, selling-point labels, and localization.

Start every new product task, and every return to Step 1, with exactly:

`吴佳庚，你来上班了？`

After entering that line, users are required to either upload actual photos or reference images of the product in the current chat, or provide the path where the actual/reference images are stored. Explain that the images are needed to calibrate this product's shape, proportions, color, material, structure, ports, accessories, and details so generation does not drift from the real item. Do not ask any other question in Step 1.

Keep Step 1 separate from all other information collection. Do not ask for country, platform, style, product details, image types, ratio, quantity, or additional requirements in Step 1.

After Step 1 is complete, collect the original Steps 2-9 primarily with the bundled local browser form service. The service script is at `../../scripts/product_form_server.py` relative to this `SKILL.md` file, inside the plugin root's `scripts/` directory. Start that script as a background process, open its local URL in the Codex in-app Browser when available, have the user fill the HTML form, and then read the saved JSON directly from `%TEMP%\egen-commerce-images\latest-product-task.json` or the `JSON_PATH` printed by the server. Never start the service with a foreground shell command that waits for `product_form_server.py` to exit. After reading the saved JSON into context, close the local service by calling its `/shutdown` endpoint; if that fails, stop only the printed `PID`. Do not ask the user to copy JSON back into chat.

If the local form service or browser flow is unavailable, fall back to the two fixed Markdown tables: one product information table and one task options table. Markdown tables only simulate an in-chat form; do not claim that Codex provides native dropdown menus. Use numbered options, fixed enum values, and editable `填写` cells instead.

Do not output the product analysis plan until the saved form JSON or fallback tables are filled sufficiently and required task options have passed validation.

## Image Source Boundary

Strictly distinguish `knowledge` library images from product images uploaded by the user in the current chat.

- The fixed knowledge root is `E:\e-commerce\knowledge`. Always use this absolute path even when the current working directory is elsewhere.
- Style reference folders are direct children named `style1`, `style2`, and so on. Each style folder contains one ecommerce visual style represented by `.png`, `.jpg`, or `.jpeg` images.
- The built-in style prompt document root is `references/style-prompts/` inside this skill folder. These Markdown files are the authoritative style prompt documents for the workflow.
- Treat `knowledge` images only as references for ecommerce style, composition, information hierarchy, selling-point expression, layout, and design logic.
- Never treat `knowledge` images as the current product's real photo.
- Never infer that the user has completed Step 1 from `knowledge` images.
- Never use the product, facts, dimensions, colors, accessories, functions, brand, or visual details from `knowledge` images as facts about the current product.
- The current product must come from newly uploaded product real photos or reference photos in the current chat. If the current chat has no new user-uploaded product image, stay at Step 1 and keep asking for an upload.

When choosing a style, first let the user choose one available built-in style prompt document. The available style documents are:

- `style1` -> `references/style-prompts/STYLE1_PROMPTS.md`
- `style2` -> `references/style-prompts/STYLE2_PROMPTS.md`
- `style3` -> `references/style-prompts/STYLE3_PROMPTS.md`
- `style4` -> `references/style-prompts/STYLE4_PROMPTS.md`
- `style5` -> `references/style-prompts/STYLE5_PROMPTS.md`
- `style6` -> `references/style-prompts/STYLE6_PROMPTS.md`
- `stylehero` -> `references/style-prompts/STYLEhero_PROMPTS.md`

Use the selected style prompt document as the primary style, layout, prompt-structure, and visual-DNA reference for final image generation. If matching `knowledge` images also exist under `E:\e-commerce\knowledge`, they are secondary visual references only. Use only the selected style unless the user explicitly changes it.

Within the selected style prompt document, borrow only visual style, composition, information hierarchy, selling-point expression, layout, prompt variables, UI component logic, and design logic. Do not copy any product facts from the style document. If additional matching is useful within the same image type, prefer style sections or examples in this order: same image type, same platform and language, same country/region, same category, similar price band. Briefly state which style/category/type rules were borrowed, without claiming the style document or knowledge library proves any current product fact.

### Type-Specific Reference Selection

Use this filename token table to match reference images in the selected style folder:

| Image type | Filename token |
| --- | --- |
| 主图 | `Hero` |
| 痛点/卖点图 | `Selling` |
| 功能/结构图 | `Feature` |
| 尺寸规格图 | `Specs` |
| 场景结果图 | `Lifestyle` |
| 差异化价值图 | `Value` |
| 对比优势图 | `Compare` |
| A+ 收束图 | `Closing` |
| 核心价值场景图 A | `CoreA` |
| 核心价值场景图 B | `CoreB` |
| 产品使用说明 | `Guide` |

- For every final output, determine the target image type and its filename token before selecting `knowledge` references.
- In the selected style prompt document, use the section or prompt whose filename/image-type token matches the target type as the concrete prompt reference for that output.
- If using secondary `knowledge` images, use only `.png`, `.jpg`, and `.jpeg` files whose filename contains the matching token, case-insensitive, as concrete visual references for that output.
- Do not mix references from other image types. Do not use every section or every image for one output.
- If no same-type section or reference file exists, do not borrow composition, content, copy, or product presentation from mismatched image types. Create an original layout using the selected style document's general style direction, such as palette, typography feel, visual density, hierarchy, background treatment, UI component language, and ecommerce design logic. Briefly state that no same-type reference was found and the image will innovate within the selected style.
- For a nonstandard user-supplied image type, map it to the nearest standard type only when the mapping is clear. If there is no clear mapping, treat it as a custom type and innovate from the selected style direction without using mismatched type images as concrete references.

If `knowledge` materials appear to come from competitors or third parties, extract only structure, style, expression logic, layout, and hierarchy. Do not copy trademarks, patented product appearance, brand assets, people likenesses, official platform marks, or protected copy. If brand names, IP, celebrities, film/game characters, competitor marks, or platform marks appear, warn about infringement risk and use generic alternatives.

## Fixed Workflow

### Step 1: Upload Product Image

Output the required opening line, then only ask:

`请在当前会话框上传至少一张产品实拍图或参考图，用于校准本次产品的外形、比例、颜色、材质、结构、接口、配件和细节，避免生成偏离实物。`

Do not use `knowledge` images to satisfy this step.

### Step 2: Fill Product Task Form

After the user uploads at least one current-chat product image or provides a path to actual/reference product images, use the bundled local form workflow by default:

1. Resolve the plugin root as two directories above this `SKILL.md` file. From the skill folder, the service script path is `..\..\scripts\product_form_server.py`; from the plugin root, it is `.\scripts\product_form_server.py`.

2. Start the local service as a background process with the resolved script path. Prefer the Codex bundled Python executable from `codex_app.load_workspace_dependencies` when available; otherwise use a verified local `python` or `py` command. Do not run `python ..\..\scripts\product_form_server.py` as a foreground command.

```powershell
$script = Resolve-Path '..\..\scripts\product_form_server.py'
$out = Join-Path $env:TEMP 'egen-commerce-images-form.out.log'
$err = Join-Path $env:TEMP 'egen-commerce-images-form.err.log'
Start-Process -WindowStyle Hidden -FilePath python -ArgumentList @($script) -RedirectStandardOutput $out -RedirectStandardError $err -PassThru
Start-Sleep -Seconds 1
Get-Content -LiteralPath $out -Raw -ErrorAction SilentlyContinue
Get-Content -LiteralPath $err -Raw -ErrorAction SilentlyContinue
```

3. Read the printed `FORM_URL`, `LATEST_URL`, `JSON_PATH`, and `PID`.
4. Open `FORM_URL` in the Codex in-app Browser when available.
5. Ask the user to fill the browser form and click `保存表单`.
6. After the user says the form is saved, read the JSON file at `JSON_PATH`. The default path is `%TEMP%\egen-commerce-images\latest-product-task.json`.

The browser form provides dropdowns for target country/language, platform, knowledge style, ratio, quantity, and extra requirement mode. It provides checkboxes for image type selection, including `全选`. Runtime form results must stay outside the repository; do not commit generated JSON files.

If the startup command returns exit code `124`, if the log does not contain `FORM_URL`, or if the printed `PID` is no longer running, treat the startup as failed and retry with a background `Start-Process` command before opening the browser. If the service cannot start or the browser cannot be used, output the following two fixed Markdown tables in one message as a fallback. Tell the user they can copy the tables and modify only the `填写` column. Use the current-chat product image to provide a few candidate product information values where visible; mark unknown fields as `待填写`. 允许用户指定产品信息文档路径（如有）.

#### Fallback 产品信息表

| 字段 | 填写 |
| --- | --- |
| 产品名称 | 待填写 |
| 品牌 | 待填写 |
| 商品类目 | 待填写 |
| 材质/成分 | 待填写 |
| 尺寸/规格 | 待填写 |
| 颜色/款式 | 待填写 |
| 包装清单 | 待填写 |
| 适用人群 | 待填写 |
| 使用场景 | 待填写 |
| 核心卖点 | 待填写 |
| 需要避免的表达 | 待填写 |
| 其他补充 | 待填写 |
| 产品信息文档路径（如有） | 无 |

#### Fallback 任务选项表

| 项目 | 编号选项 / 固定枚举 | 填写 |
| --- | --- | --- |
| 目标国家/语言 | 1 美国/英语；2 墨西哥/西班牙语；3 智利/西班牙语；4 哥伦比亚/西班牙语；5 南非/英语；6 其他：请填写 | 待填写 |
| 目标平台 | 1 Amazon；2 MercadoLibre；3 Takealot；4 其他：请填写 | 待填写 |
| knowledge style | 1 style1；2 style2；3 style3；4 style4；5 style5；6 style6；7 stylehero；8 其他：请填写 | 待填写 |
| 图片类型 | 1 全选；2 Hero；3 Selling；4 Feature；5 Specs；6 Lifestyle；7 Value；8 Compare；9 Closing；10 CoreA；11 CoreB；12 Guide；13 其他：请填写 | 待填写 |
| 图片比例 | 1 1:1；2 4:5；3 3:4；4 16:9；5 9:16 | 待填写 |
| 每类数量 | 1；2；4；6；10 | 待填写 |
| 额外生图要求 | 1 无额外要求；2 填写额外要求 | 1 |

Do not proceed until the required task options are filled: target country/language, platform, knowledge style, image types, ratio, and quantity per type. Defaults are English and Spanish, but accept additional languages when the user supplies them.

### Step 3: Parse and Validate Form Data

For the local browser form workflow, read the saved JSON directly from `%TEMP%\egen-commerce-images\latest-product-task.json` or the `JSON_PATH` printed by `../../scripts/product_form_server.py`. Do not ask the user to paste JSON into chat. Once the saved JSON has been read into context, close the form server before continuing to the analysis plan. Prefer `POST <FORM_URL base>/shutdown`; if the shutdown request is unavailable or fails, stop only the exact `PID` printed by the server. Do not leave the product form service running in the background after the task data has been captured.

Expected saved JSON shape:

```json
{
  "productInfo": {
    "productName": "",
    "brand": "",
    "category": "",
    "material": "",
    "sizeSpec": "",
    "colorVariant": "",
    "packageList": "",
    "targetUsers": "",
    "useScenarios": "",
    "sellingPoints": "",
    "avoidExpressions": "",
    "additionalNotes": "",
    "productInfoPath": ""
  },
  "taskOptions": {
    "countryLanguage": "US_EN",
    "platform": "Amazon",
    "knowledgeStyle": "style1",
    "imageTypes": ["Hero"],
    "ratio": "1:1",
    "quantityPerType": 1,
    "extraRequirementMode": "none",
    "extraRequirements": ""
  },
  "meta": {
    "schemaVersion": 1,
    "savedAt": "ISO-8601 timestamp"
  }
}
```

For fallback Markdown tables, parse the user's filled tables and normalize numbered options or fixed enum values. Image types support multiple selections such as `2,3,5`, `Hero,Selling,Specs`, or Chinese image type names.

`全选` means the eleven standard image types: 主图 Hero, 痛点/卖点图 Selling, 功能/结构图 Feature, 尺寸规格图 Specs, 场景结果图 Lifestyle, 差异化价值图 Value, 对比优势图 Compare, A+ 收束图 Closing, 核心价值场景图 A CoreA, 核心价值场景图 B CoreB, 产品使用说明 Guide.

If the saved JSON or fallback tables use `OTHER` / `其他` for country/language, platform, style, image type, or additional requirements but do not provide the custom value, ask one focused follow-up question for that item only. If the user selects another platform, adapt conservatively from general marketplace best practices and ask one focused clarification only if the platform has unusual image rules.

Do not invent certifications, test results, materials, origin, effects, reviews, authorization, platform endorsement, dimensions, compatibility, accessories, or other product facts. Product information fields may remain `待填写`; clearly separate known facts from assumptions or suggested wording.

State that final generation must follow the ratios currently supported by the built-in `image_gen.imagegen` tool. If a chosen ratio is unavailable in the active environment, use the nearest supported ratio only after telling the user. Calculate `selected image type count x quantity per type`. If the result may touch or exceed the active `image_gen.imagegen` single-request limit, ask the user to choose fewer images or generate in batches.

### Step 10: Analysis Plan and Confirmation

Only after Step 1 is complete and the Step 2 saved form JSON or fallback tables have passed Step 3 validation, output a Chinese product analysis plan and wait for confirmation. Include:

- 详尽产品描述
- 目标客群
- 核心卖点
- 场景策略
- 电商标题建议：关键词优化版
- 电商标题建议：卖点突出版
- 合规提醒
- 套图生成范围：平台、国家/语言、knowledge style、图片类型、比例、每类数量、补充要求

If the user requests changes, output a revised plan and continue waiting for confirmation. Do not generate any image until the user clearly confirms the final plan.

### Step 11: Generate Final Outputs

After the user confirms the final analysis plan, generate the final localized product description and the confirmed final ecommerce image set of `selected image type count x quantity per type` images. Adapt each image to its selected image type while following the confirmed visual style, platform, country/language, product facts, ratio, quantity, and additional requirements.

Use the built-in `image_gen.imagegen` tool for image generation. Do not call external image-generation APIs, do not write scripts that invoke image APIs, and do not ask the user for API keys. Follow the confirmed knowledge style, image types, ratio, quantity, additional requirements, and Type-Specific Reference Selection. For each final output, use only same-type reference files from the selected style folder; if none exist for that target type, innovate within the selected style direction instead of using mismatched type files. Preserve the product shape, proportions, color, material, structure, ports, accessories, and details from the user-uploaded current-chat product images.

Every final image must include this exact constraint in its image-generation instructions:

`Top-right logo safe area: keep a clean natural background area for future logo placement. Do not draw any visible placeholder box, border, outline, rounded rectangle, frame, shadow panel, icon, text, logo, or product in this area. The area should blend seamlessly with the same background texture and lighting as the rest of the image.`

Do not show prompts, negative prompts, or internal image-generation instructions to the user.

If the built-in `image_gen.imagegen` tool is unavailable in the active environment, say that the current environment cannot directly generate images and provide an executable final batch image-generation plan instead.

## Final Product Description

Generate final consumer-facing copy in the selected country/language and adapted to the selected platform. Include at least:

- Platform-adapted title
- Short selling points
- Long description
- Key parameter phrasing
- Scenario-based benefits
- Localized expression suggestions
- Necessary compliance reminders

Keep internal analysis and workflow guidance in Chinese unless it is consumer-facing content requested for the target country/language.

## Compliance Guardrails

Avoid exaggerated effects, absolute promises, cheap/low-end framing, obvious AI style, infringement elements, platform-prohibited terms, and any expression that would make image details diverge from the real product.

Top-right logo safe area: keep a clean natural background area for future logo placement. Do not draw any visible placeholder box, border, outline, rounded rectangle, frame, shadow panel, icon, text, logo, or product in this area. The area should blend seamlessly with the same background texture and lighting as the rest of the image.

Do not use unproven or high-risk absolute/misleading claims such as `best`, `guaranteed`, `100%`, `cure`, `permanent`, `official`, or `compatible with all`.

For food, supplements, baby products, medical items, beauty efficacy claims, financial promises, and other regulated categories, proactively warn against therapeutic, exaggerated, or platform-violating claims.

When key information is missing, ask one focused follow-up question at a time. If the user explicitly asks for a draft first, proceed with reasonable assumptions but clearly separate known facts from suggested wording.
