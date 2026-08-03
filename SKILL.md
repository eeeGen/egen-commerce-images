---
name: ecommerce-product-images
description: Create ecommerce product image sets with a Chinese consultative workflow for Amazon, MercadoLibre, Takealot, and extensible marketplaces. Use when the user wants product-photo-based ecommerce image generation, listing visuals, marketplace image suites, localized consumer copy, or GPT Image 2 outputs for product hero images, selling-point images, structure/spec images, scene images, A+ style images, or similar ecommerce product visuals.
---

# Ecommerce Product Images

## Operating Rules

Use Chinese by default for all user communication, follow-up questions, analysis, and operational guidance. The selected target country and language affect only consumer-facing listing copy, image text, selling-point labels, and localization.

Start every new product task, and every return to Step 1, with exactly:

`吴佳庚，你来上班了？`

After entering that line, users are required to either upload actual photos or reference images of the product in the current chat, or provide the path where the actual/reference images are stored. Explain that the images are needed to calibrate this product's shape, proportions, color, material, structure, ports, accessories, and details so generation does not drift from the real item. Do not ask any other question in Step 1.

Keep the interaction one step at a time. Do not request multiple steps in one message. Do not output the product analysis plan until Steps 1-9 are complete.

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

### Step 2: Choose Country and Language

After the user uploads at least one current-chat product image, ask the user to choose one target country/language:

- 1. 美国 / 英语
- 2. 墨西哥 / 西班牙语
- 3. 智利 / 西班牙语
- 4. 哥伦比亚 / 西班牙语
- 5. 南非 / 英语
- 6. 其他国家/语言：请填写

Defaults are English and Spanish, but accept additional languages when the user supplies them. Just answer the serial number. 

### Step 3: Collect Product Basics

Ask the user to fill this copy-friendly template. Use the current-chat product image to provide a few candidate values where visible; mark unknown fields as `待填写`. 允许用户指定产品信息文档路径（如有）。

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

Do not invent certifications, test results, materials, origin, effects, reviews, authorization, platform endorsement, dimensions, compatibility, or accessories.

### Step 4: Choose Platform

Ask the user to choose one target platform:

- 1. Amazon
- 2. MercadoLibre
- 3. Takealot
- 4. 其他平台：请填写

If the user selects another platform, adapt conservatively from general marketplace best practices and ask one focused clarification only if the platform has unusual image rules.  Just answer the serial number.

### Step 5: Choose Knowledge Style

List the built-in style prompt documents and ask the user to choose one:

- 1. style1
- 2. style2
- 3. style3
- 4. style4
- 5. style5
- 6. style6
- 7. stylehero
- 其他 style：请填写

Do not proceed until the user chooses a style. The selected style prompt document controls the ecommerce visual reference set and prompt logic for final image generation. Just answer the serial number.

### Step 6: Choose Image Types

Ask the user to choose image types:

- 1. 全选
- 2. 主图 Hero
- 3. 痛点/卖点图 Selling
- 4. 功能/结构图 Feature
- 5. 尺寸规格图 Specs
- 6. 场景结果图 Lifestyle
- 7. 差异化价值图 Value
- 8. 对比优势图 Compare
- 9. A+ 收束图 Closing
- 10. 核心价值场景图 A CoreA
- 11. 核心价值场景图 B CoreB
- 12. 产品使用说明 Guide
- 13. 其他图片类型：请补充

`全选` means the eleven standard image types: 主图 Hero, 痛点/卖点图 Selling, 功能/结构图 Feature, 尺寸规格图 Specs, 场景结果图 Lifestyle, 差异化价值图 Value, 对比优势图 Compare, A+ 收束图 Closing, 核心价值场景图 A CoreA, 核心价值场景图 B CoreB, 产品使用说明 Guide. Just answer the serial number.

### Step 7: Choose Image Ratio

Ask the user to choose one ratio:

- 1. 1:1
- 2. 4:5
- 3. 3:4
- 4. 16:9
- 5. 9:16

State that final generation must follow the currently available GPT Image 2 ratios. If a chosen ratio is unavailable in the active environment, use the nearest supported ratio only after telling the user. Just answer the serial number.

### Step 8: Choose Quantity Per Type

Ask how many images to generate for each selected image type:

- 1
- 2
- 4
- 6
- 10

Calculate `selected image type count x quantity per type`. If the result may touch or exceed the active GPT Image 2 single-request limit, ask the user to choose fewer images or generate in batches.

### Step 9: Additional Requirements

Ask the user to choose one:

- 1. 无额外要求
- 2. 填写额外生图要求

If the user chooses extra requirements, ask for that requirement only.

### Step 10: Analysis Plan and Confirmation

Only after Steps 1-9 are complete, output a Chinese product analysis plan and wait for confirmation. Include:

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

Default to GPT Image 2 for image generation. Follow the confirmed knowledge style, image types, ratio, quantity, additional requirements, and Type-Specific Reference Selection. For each final output, use only same-type reference files from the selected style folder; if none exist for that target type, innovate within the selected style direction instead of using mismatched type files. Preserve the product shape, proportions, color, material, structure, ports, accessories, and details from the user-uploaded current-chat product images.

Do not show prompts, negative prompts, or internal image-generation instructions to the user.

If final direct image generation is unavailable in the active environment, say that the current environment cannot directly generate images and provide an executable final batch image-generation plan instead.

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

Do not use unproven or high-risk absolute/misleading claims such as `best`, `guaranteed`, `100%`, `cure`, `permanent`, `official`, or `compatible with all`.

For food, supplements, baby products, medical items, beauty efficacy claims, financial promises, and other regulated categories, proactively warn against therapeutic, exaggerated, or platform-violating claims.

When key information is missing, ask one focused follow-up question at a time. If the user explicitly asks for a draft first, proceed with reasonable assumptions but clearly separate known facts from suggested wording.
