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

After Step 1 is complete, immediately run the bundled browser form workflow in Step 2. A user-provided product-image path completes Step 1. The form attempt is a required gate: launch the service, verify `FORM_URL` responds, and open that URL in the Codex in-app Browser when available before requesting the remaining task options. An unopened service is not evidence that the form is unavailable. Read the saved JSON from `WAIT_URL`; after capturing it, shut down the service. Do not ask the user to copy JSON into chat.

`taskOptions.styleSource` selects the visual workflow. Treat a missing value in legacy JSON as `builtin`. For `builtin`, follow the built-in style-prompt workflow below. For `customer-reference`, read [客户参考风格工作流](references/customer-reference-workflow.md) before parsing the task, planning, or generating; use customer-selected images as the style source without mixing in built-in style prompts.

Use the two Markdown fallback tables only after a concrete service launch, health check, or browser-open attempt fails. Tell the user which attempt failed. An unavailable browser is a fallback condition only when the active environment has no usable browser surface. Markdown tables only simulate an in-chat form; do not claim Codex provides native dropdown menus.

Do not output the product analysis plan until the saved form JSON or fallback tables are filled sufficiently and required task options have passed validation.

## Image Source Boundary

Distinguish style sources from the current product's actual/reference images.

- The built-in style prompt document root is `references/style-prompts/` inside this skill folder. These Markdown files are the authoritative style prompt documents for the workflow.
- In customer-reference mode, use the customer's selected style images only for composition, layout, hierarchy, and visual language. They do not establish the current product's facts or appearance and do not satisfy Step 1.
- The current product must come from newly uploaded product real photos or reference photos in the current chat, or from the user-provided local product-material path. If neither is available, stay at Step 1 and keep asking for an upload or path.

### Customer Reference Source Mode

When `taskOptions.styleSource` is `customer-reference`, customer-selected local reference images are the only style source. Do not read a built-in style prompt document or apply built-in prompt selection rules. Follow [客户参考风格工作流](references/customer-reference-workflow.md) for the shared product references, ordered style references, color-master rule, confirmation gate, and image-generation calls.

### Built-in Style Source Mode

When choosing a style, first let the user choose one available built-in style prompt document. The available style documents are:

- `style1` -> `references/style-prompts/STYLE1_PROMPTS.md`
- `style2` -> `references/style-prompts/STYLE2_PROMPTS.md`
- `style3` -> `references/style-prompts/STYLE3_PROMPTS.md`
- `style4` -> `references/style-prompts/STYLE4_PROMPTS.md`
- `style5` -> `references/style-prompts/STYLE5_PROMPTS.md`
- `style6` -> `references/style-prompts/STYLE6_PROMPTS.md`
- `style6-v2` -> `references/style-prompts/STYLE6_V2_PROMPTS.md` (Amazon 强信息转化；用于快速扫描、事实证据与下单决策)
- `style6-v3` -> `references/style-prompts/STYLE6_V3_PROMPTS.md` (品牌官网式情绪叙事；用于 A+、品牌页与质感故事表达)
- `style6-v3-2` -> `references/style-prompts/STYLE6_V3_2_PROMPTS.md` (品牌散文式情绪叙事；用于以具象、克制的视觉描写增强品牌页与 A+ 叙事)
- `style6plus` -> `references/style-prompts/STYLE6PLUS_PROMPTS.md` (Feature validation only; read `STYLE6_PROMPTS.md` first for its inherited visual DNA)
- `stylehero` -> `references/style-prompts/STYLEhero_PROMPTS.md`

Use the selected style prompt document as the only style, layout, prompt-structure, and visual-DNA source for built-in image generation, together with the current product's materials for product facts and appearance. Use only the selected style unless the user explicitly changes it.

`style6plus` is a narrow validation style, not a replacement for `style6`. It supports only the `Feature` image type. For it, first read `STYLE6_PROMPTS.md` for the inherited blue-and-gold visual DNA, then read `STYLE6PLUS_PROMPTS.md` as the authoritative Feature layout, input gate, prompt structure, and acceptance checklist. If a task selects `style6plus` with any image type other than `Feature`, ask the user to select only `Feature` or choose another style before planning.

Within the selected style prompt document, borrow only visual style, composition, information hierarchy, selling-point expression, layout, prompt variables, UI component logic, and design logic. Do not copy any product facts from the style document. If additional matching is useful within the same image type, prefer style sections or examples in this order: same image type, same platform and language, same country/region, same category, similar price band. Briefly state which style/category/type rules were borrowed, without claiming the style document proves any current product fact.

For `style6-v2`, `style6-v3`, and `style6-v3-2`, first create one set-level Coverage Matrix before drafting any per-image prompt. It must map every selected image type to a distinct product presentation, decision question, scene/moment, camera treatment, UI density, and evidence source. For `style6-v3-2`, include the prose-style visual moment and whether the frame is a verified full-set, single-item, or single-component view. When product materials verify a multi-component set or multi-PCS item, schedule at least one single-item/single-component image and do not repeat the full set across every image; a single-item view must not imply that it is sold separately. When the same product is tested in both styles, lock product facts, selected identity references, image types, ratio, country/language, platform, and visible factual copy; change only the selected style document's visual-directing rules. Do not use the presence of multiple product reference images as evidence of a multi-pack, and do not repeat a product lineup across the set.

### Type-Specific Prompt Selection

Use this image-type token table to select sections in the chosen style prompt document:

| Image type | Prompt token |
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

- For every final output, determine the target image type and its prompt token, then use the matching section or prompt in the selected style document.
- The confirmed shot row controls what enters the frame. Fill the style template's product, `{selling_points}` and `{accessories}` slots with just that row's subject and evidence. On a core selling-point image, replace generic counts of benefits with the one approved point. Use an overall product view or inset only when the row calls for it. Keep the style's visual language and the selected image type's purpose.
- Use only sections matching that image type, rather than every section for one output.
- If no same-type section exists, create an original layout using the selected style document's general direction, such as palette, typography feel, visual density, hierarchy, background treatment, UI component language, and ecommerce design logic. Briefly state that no same-type prompt section was found and the image will innovate within the selected style.
- For a nonstandard user-supplied image type, map it to the nearest standard type only when the mapping is clear. Otherwise, treat it as a custom type and innovate from the selected style direction without borrowing concrete layouts from mismatched types.

If customer-selected style references appear to come from competitors or third parties, extract only structure, style, expression logic, layout, and hierarchy. Do not copy trademarks, patented product appearance, brand assets, people likenesses, official platform marks, or protected copy. If brand names, IP, celebrities, film/game characters, competitor marks, or platform marks appear, warn about infringement risk and use generic alternatives.

## Fixed Workflow

### Step 1: Upload Product Image

Output the required opening line, then only ask:

`请在当前会话框上传至少一张产品实拍图或参考图，用于校准本次产品的外形、比例、颜色、材质、结构、接口、配件和细节，避免生成偏离实物。`

Complete this step with the current product's actual/reference images.

### Step 2: Fill Product Task Form

After the user uploads at least one current-chat product image or provides a path to actual/reference product images, run the bundled local form workflow:

1. Use the absolute path of the `SKILL.md` file you loaded. Its containing directory is the skill folder; resolve `..\..\scripts\product_form_server.py` from that folder, independent of the shell's current working directory. Verify the resulting script exists.

2. Start the local service as a background process. Prefer the Codex bundled Python executable from `codex_app.load_workspace_dependencies` when available; otherwise use a verified local `python` or `py` command. Use a unique log filename for this form session. Wait until the process prints `FORM_URL` and `/health` responds; this is the startup completion criterion. Do not run the server in the foreground.

```powershell
$skillFile = '<absolute path of the SKILL.md file just loaded>'
$skillDir = Split-Path -Parent $skillFile
$script = (Resolve-Path -LiteralPath (Join-Path $skillDir '..\..\scripts\product_form_server.py')).Path
$pythonExe = (Get-Command python -ErrorAction Stop).Source
$tag = [guid]::NewGuid().ToString('N')
$out = Join-Path $env:TEMP "egen-commerce-images-form-$tag.out.log"
$err = Join-Path $env:TEMP "egen-commerce-images-form-$tag.err.log"
$proc = Start-Process -WindowStyle Hidden -FilePath $pythonExe -ArgumentList @('-B', "`"$script`"") -RedirectStandardOutput $out -RedirectStandardError $err -PassThru
$log = ''
for ($i = 0; $i -lt 20; $i++) {
    Start-Sleep -Milliseconds 250
    $log = Get-Content -LiteralPath $out -Raw -ErrorAction SilentlyContinue
    if ($log -match '(?m)^FORM_URL=' -or $proc.HasExited) { break }
}
if ($log -notmatch '(?m)^FORM_URL=(\S+)') {
    Get-Content -LiteralPath $err -Raw -ErrorAction SilentlyContinue
    throw "Form server did not publish FORM_URL (PID $($proc.Id))."
}
$formUrl = $Matches[1]
$health = Invoke-RestMethod -Uri ($formUrl.TrimEnd('/') + '/health') -TimeoutSec 3
if (-not $health.ok) { throw "Form server health check failed: $formUrl" }
$log
```

3. Read the printed `FORM_URL`, `LATEST_URL`, `WAIT_URL`, `JSON_DIR`, `TASK_ID`, and `PID`.
4. Open `FORM_URL` in the Codex in-app Browser when available.
5. Ask the user to fill the browser form and click `保存表单`.
6. In parallel with the user filling the browser form, call `WAIT_URL` or `GET <FORM_URL base>/wait?timeout=600`. When it returns, read the returned `jsonPath`. Do not require the user to manually type `已保存`.
7. If `/wait` times out or cannot be reached, ask the user to confirm after clicking `保存表单`, then read the current task result from `LATEST_URL`.

The browser form provides target country/language, platform, style-source mode, ratio, and extra requirement options. Built-in mode retains knowledge style, image types, and quantity. Customer-reference mode scans the product directory and offers a style menu from the bound local image library alongside a manual reference-directory option. From the displayed style images the user selects ordered imitation images, one required color master and an optional font master. If the library cannot be found, the form opens a system folder chooser; the manual reference option remains available after cancellation. It saves each submission to a task-specific JSON file under `%TEMP%\egen-commerce-images\tasks\product-task-YYYYMMDD-HHMMSS-<taskId>-<saveCount>.json`, so different form sessions do not conflict. Runtime form results must stay outside the repository; do not commit generated JSON files.

If startup fails, inspect this session's error log and retry once with the verified absolute script and Python paths. If the process starts but the browser cannot open `FORM_URL`, attempt the available in-app browser surface and record the concrete failure. Only after these attempts fail, output the following two fixed Markdown tables in one message and state the failure that triggered the fallback. Tell the user they can copy the tables and modify only the `填写` column. Use the current-chat product image to provide a few candidate product information values where visible; mark unknown fields as `待填写`. 允许用户指定产品信息文档路径（如有）.

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
| 风格来源 | 1 内置风格；2 客户参考风格 | 待填写 |
| knowledge style（仅内置风格） | 1 style1；2 style2；3 style3；4 style4；5 style5；6 style6；7 style6-v2（Amazon 强信息转化）；8 style6-v3（品牌官网情绪叙事）；9 style6-v3-2（品牌散文式情绪叙事）；10 stylehero；11 style6plus（仅 Feature 验证） | 待填写 |
| 图片类型（仅内置风格） | 1 全选；2 Hero；3 Selling；4 Feature；5 Specs；6 Lifestyle；7 Value；8 Compare；9 Closing；10 CoreA；11 CoreB；12 Guide；13 其他：请填写 | 待填写 |
| 图片比例 | 1 1:1；2 4:5；3 3:4；4 16:9；5 9:16 | 待填写 |
| 每类数量（仅内置风格） | 1；2；4；6；10 | 待填写 |
| 字体母版（仅客户参考风格，选填） | 当前风格图片中的一张，填写路径；留空则各图沿用自己的仿照图字体 | 无 |
| 额外生图要求 | 1 无额外要求；2 填写额外要求 | 1 |

For a Markdown fallback in customer-reference mode, collect the ordered `外形参考图路径` and `仿照图路径`, one `全局色彩母版路径`, one `色彩策略` (`auto`/`master`/`scene`), and the optional font master from the table. Treat a missing field, a blank or `无` as no font master. For a supplied font path, clean it as below and check it against the direct image candidates in the same selected style or manual style directory as the imitation images. If outside that selection, ask for a current candidate or a clear selection. A master can also be an imitation or share the other master's file. Only the ordered imitation list determines output count.

For every customer-reference path supplied manually, including the Markdown fallback lists, color and font masters, and optional product-information document, trim outer whitespace and then remove one complete pair of surrounding ASCII double quotes. Preserve all characters inside the path. Do not add a path-existence check to this string cleanup; existing material-reading steps still perform their normal scans and reads.

Do not proceed until the required task options are filled. Built-in mode requires target country/language, platform, knowledge style, image types, ratio, and quantity per type. Customer-reference mode requires target country/language, platform, global ratio, at least one product reference, at least one imitation reference, and a color mother path. Defaults are English and Spanish, but accept additional languages when the user supplies them.

### Step 3: Parse and Validate Form Data

For the local browser form workflow, read the saved JSON from the `jsonPath` returned by `WAIT_URL` / `/wait`. If `/wait` failed after the user saved, read the current service result from `LATEST_URL`. Do not ask the user to paste JSON into chat. The current JSON schema is version 4; schema versions 1 and 2 remain valid legacy built-in-style inputs, and version 3 customer-reference tasks retain their per-card mapping. Once the saved JSON has been read into context, close the form server before continuing to the analysis plan. Prefer `POST <FORM_URL base>/shutdown`; if the shutdown request is unavailable or fails, stop only the exact `PID` printed by the server. Do not leave the product form service running in the background after the task data has been captured.

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
    "styleSource": "builtin",
    "knowledgeStyle": "style1",
    "imageTypes": ["Hero"],
    "ratio": "1:1",
    "quantityPerType": 1,
    "extraRequirementMode": "none",
    "extraRequirements": ""
  },
  "referenceWorkflow": null,
  "meta": {
    "schemaVersion": 4,
    "taskId": "short task id",
    "formStartedAt": "ISO-8601 timestamp",
    "savedAt": "ISO-8601 timestamp",
    "saveCount": 1
  }
}
```

For customer-reference JSON, use [the customer reference workflow](references/customer-reference-workflow.md) as the canonical source for schema v3/v4 fields, resolved-path handling, required selections, and legacy-card validation. Reject incomplete selections before planning.

For fallback Markdown tables, parse the user's filled tables and normalize numbered options or fixed enum values. Image types support multiple selections such as `2,3,5`, `Hero,Selling,Specs`, or Chinese image type names.

`全选` means the eleven standard image types: 主图 Hero, 痛点/卖点图 Selling, 功能/结构图 Feature, 尺寸规格图 Specs, 场景结果图 Lifestyle, 差异化价值图 Value, 对比优势图 Compare, A+ 收束图 Closing, 核心价值场景图 A CoreA, 核心价值场景图 B CoreB, 产品使用说明 Guide.

If the saved JSON or fallback tables use `OTHER` / `其他` for country/language, platform, image type, or additional requirements but do not provide the custom value, ask one focused follow-up question for that item only. The HTML form and fallback table do not support custom knowledge styles in built-in mode; if the user needs a new built-in style, treat it as a separate skill update request before generation. Customer-reference mode uses client images instead. If the user selects another platform, adapt conservatively from general marketplace best practices and ask one focused clarification only if the platform has unusual image rules.

Do not invent certifications, test results, materials, origin, effects, reviews, authorization, platform endorsement, dimensions, compatibility, accessories, or other product facts. Product information fields may remain `待填写`; clearly separate known facts from assumptions or suggested wording.

State that final generation must follow the ratios currently supported by the built-in `image_gen.imagegen` tool. If a chosen ratio is unavailable in the active environment, use the nearest supported ratio only after telling the user. In built-in mode, calculate `selected image type count x quantity per type` and batch only when needed. For customer-reference output count and order, follow the customer reference workflow.

### Step 10: Analysis Plan and Confirmation

Only after Step 1 is complete and the Step 2 saved form JSON or fallback tables have passed Step 3 validation, output a Chinese product analysis plan and wait for confirmation. Include:

- 详尽产品描述
- 目标客群
- 核心卖点
- 场景策略
- 电商标题建议：关键词优化版
- 电商标题建议：卖点突出版
- 合规提醒
- 套图生成范围包括平台、国家/语言、比例与补充要求。内置模式列出 knowledge style、图片类型与每类数量。客户参考模式按[客户参考风格工作流](references/customer-reference-workflow.md)列出选图、母版、色彩策略和文案。旧 v3 沿用逐卡配方。
- 两种模式都在同一份总览里按实际出图顺序列出逐图取景表。每行写明「图位｜用途或核心卖点｜画面主体｜景别与角度｜实物依据（参考图文件名或上传序号，以及能看见的部位）」。每张成图一行，包括同一类型的多个变体。已有 Coverage Matrix 的内置风格把这些列并入原表。

Compare the rows before presenting them. Assign full product, full kit, single item, individual accessory, detail or use views according to the buying question. For a verified kit with a suitable slot and a recognizable component, assign at least one row to that component alone. A single-item product can support detail and use views. If rows repeat the same lineup and angle with only different copy or backgrounds, revise the shot. Full-kit views follow their purpose or an explicit user request. Use only visible features and supported angles. A single-component view retains the confirmed sale unit. In a core selling-point row, one verified benefit determines the subject and crop. Single-image tasks need only their own row.

If the user requests changes, output a revised plan and continue waiting for confirmation. Do not generate any image until the user clearly confirms the final plan.

### Step 11: Generate Final Outputs

After the user confirms the final analysis plan, generate the final localized product description and confirmed ecommerce image set. In built-in mode, generate `selected image type count x quantity per type` images. For customer-reference modes, follow the referenced workflow's output count and order.

In **each image's initial generation prompt**, bind its confirmed row to the real reference by name or index. State the one subject or kit relationship that belongs in frame, its crop and angle, the supporting visible feature and the verified point it illustrates. For example, a connector-detail row uses the visible connector from the full-kit reference as the sole focal subject. Use the same real product references to calibrate appearance across the set. Deliver the confirmed slots after this first pass.

Use the built-in `image_gen.imagegen` tool for image generation. Do not call external image-generation APIs, do not write scripts that invoke image APIs, and do not ask the user for API keys. In built-in mode, follow the confirmed built-in style, image types, ratio, quantity, additional requirements, and Type-Specific Prompt Selection. Preserve the product shape, proportions, color, material, structure, ports, accessories, and details from the user-uploaded current-chat product images.

In customer-reference mode, follow [客户参考风格工作流](references/customer-reference-workflow.md) for reference selection, generation calls, prompt constraints, delivery, and archive conventions.

After each final image is generated, copy the selected generated file from the Codex default generated-images location into the product output folder. Copy files; do not move or delete the original generated files, and intentionally keep the Codex default generated-images archive in `$CODEX_HOME/generated_images/...`.

Resolve the product output root from Step 1:

- If Step 1 provides a valid product reference path and it is accessible, use that path to derive the product root.
- If the path is a file under a directory named `material`, `image`, `images`, `input`, `source`, `reference`, or `references`, use that directory's parent as the product root.
- If the path is any other file, use the file's parent directory as the product root.
- If the path is a directory named `material`, `image`, `images`, `input`, `source`, `reference`, or `references`, use that directory's parent as the product root.
- If the path is any other directory, use that directory as the product root.
- If Step 1 has no usable local path, or the derived root is not writable, create a folder named after the product's Chinese name in the current writable workspace. If the product Chinese name is missing, ask one focused follow-up question for that name before moving files.

Use this final path format:

`<product-root>\output\<platform>-<country>-<allStyle>\<order>-<imageType>-<style>.png`

Use lowercase file-safe slugs for `platform`, `country`, and `allStyle`. Map country codes as `US_EN -> us`, `MX_ES -> mx`, `CL_ES -> cl`, `CO_ES -> co`, `ZA_EN -> za`; for custom countries, create a conservative file-safe slug from the user's value. `allStyle` is the confirmed style token, or multiple confirmed style tokens joined by `-` if the user explicitly requested a combined style. In customer-reference v4, use `customer-reference` as `allStyle` and the imitation image filename stem as the file-safe `imageType`; for legacy v3, use the file-safe card name. Use two-digit order numbers in confirmed order, starting at `01`. Example:

`E:\e-commerce\product\Q-020 2PCS音频线\output\mercadolibre-mx-stylehero-style6\01-Hero-stylehero.png`

If a target file already exists, do not overwrite it. Ask the user whether to replace it or save with the next safe filename suffix.

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
