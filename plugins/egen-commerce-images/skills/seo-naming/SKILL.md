---
name: seo-naming
description: Rename and organize ecommerce product images with structured SEO-friendly filenames. Use when Codex needs to analyze product image content, assign marketplace image types such as Hero/Selling/Feature/Specs/Lifestyle, research Mercado Libre same-category top-selling listing keywords, and rename image files with product code, type order, and SEO terms.
---

# Product Image SEO Naming

## Overview

Use this skill to rename ecommerce product images into structured SEO-friendly filenames for marketplace operations, asset management, and database tracking.

Expected format:

```text
productcode-##-type-seo-keywords.ext
```

Example:

```text
a003-01-hero-flatware-set-32-piece-service-for-8.png
```

Read `references/naming-standard.md` when the task requires detailed naming rules, rationale, examples, or ambiguous type decisions.

## Required Workflow

1. Inspect the target folder and list image files only. Do not delete files.
2. Visually analyze image content before assigning types. Do not rely only on original filenames, timestamps, or generation order.
3. Identify the product code from the folder, user request, or existing files. Normalize it to lowercase in filenames, such as `a003`.
4. Determine marketplace and locale. If the user says Mercado Libre or Meikeduo and gives no country, assume Mercado Libre Mexico and Spanish Mexico keywords.
5. Research same-category marketplace keywords before SEO naming:
   - Search Mercado Libre same-category result pages and top-selling or high-ranking listings.
   - Prefer the top 10 listing title keywords when visible.
   - Also use platform filters, attribute terms, and buyer search phrases.
   - Extract natural phrases instead of keyword stuffing.
   - If exact sales ranking is not exposed, say so and use high-ranking search result keyword research.
6. Assign image types according to content and the type order below. Files may omit types, and types may repeat.
7. Rename files with stable temporary names first when target names may collide.
8. Verify the final folder listing, checking sequence, type order, missing or duplicate types, and extensions.

## Type Order

Use this order for numbering when the corresponding image type exists:

| Best Order | Type | Meaning | Placement Logic |
| --- | --- | --- | --- |
| 01 | Hero | Main image | 首图先建立产品识别、外观、质感和基础吸引力，是点击入口。 |
| 02 | Selling | Pain point or selling point image | 第二张直接回答“为什么需要买”，优先放最大痛点或最强卖点。 |
| 03 | CoreA | Core value scene A | 用第一个核心场景承接卖点，让用户看到产品最主要的使用价值。 |
| 04 | CoreB | Core value scene B | 补充第二个核心场景，扩大适用人群或使用场景覆盖面。 |
| 05 | Feature | Function or structure image | 在用户产生兴趣后解释功能、结构、材质、设计细节，建立理性认知。 |
| 06 | Specs | Size or specification image | 功能之后展示尺寸、容量、数量、规格等硬信息，降低购买不确定性。 |
| 07 | Value | Differentiated value image | 进一步说明差异化价值，强化“为什么选这个而不是普通款”。 |
| 08 | Compare | Comparison advantage image | 在差异化之后做对比，更容易让用户理解优势和替代品差距。 |
| 09 | Lifestyle | Scene or result image | 后段展示真实生活效果、氛围或结果，增强代入感和购买想象。 |
| 10 | Guide | Product use guide | 接近结尾展示使用方式、安装步骤、清洁维护或注意事项，降低售后疑虑。 |
| 11 | Closing | A+ closing image | 最后一张做品牌感、情绪收束、购买理由总结，形成完整闭环。 |

Use lowercase type tokens in filenames:

```text
hero, selling, corea, coreb, feature, specs, value, compare, lifestyle, guide, closing
```

If a type is missing, skip it. If a type repeats, keep the correct display order and make filenames unique with the sequence number.

## Mercado Libre Keyword Research

When the user requests Mercado Libre or Meikeduo keyword naming, search the relevant Mercado Libre site for same-category terms before renaming.

Default search targets:

```text
Mercado Libre Mexico: https://listado.mercadolibre.com.mx/
Search query: site:mercadolibre.com.mx <category/product keywords>
Search query: site:listado.mercadolibre.com.mx <category/product keywords>
```

Collect keyword signals from top-selling or high-ranking same-category listings where visible:

- Common title nouns, such as `juego de cubiertos`.
- Quantity and spec terms, such as `32 piezas`.
- Material terms, such as `acero inoxidable`.
- Color and style terms, such as `plateado` or `plata`.
- Use-case terms, such as `servicio para 8`, `mesa`, `comedor`, `uso diario`.
- Feature terms, such as `apto para lavavajillas`, `facil limpieza`.

Do not claim a precise top-10 sales ranking unless the source exposes that ranking. If exact sales order is unavailable, describe the work as high-ranking search-result keyword research.

## Filename Rules

- Use lowercase ASCII only.
- Use hyphens `-` between words.
- Do not use underscores `_` for SEO filenames.
- Do not use spaces, Chinese characters, parentheses, commas, or decorative symbols.
- Keep filenames readable and avoid keyword stuffing.
- Preserve the real file extension.
- Keep `productcode-##-type` at the front for sorting and database operations.

## Database Notes

When relevant, explain that filenames are not database primary keys. Store structured fields separately:

```text
id, product_code, sort_order, image_type, original_filename, current_filename,
seo_filename, storage_path, public_url, platform, locale, version, is_active,
width, height, file_size, mime_type, checksum, created_at, updated_at
```

## Safety

Respect local deletion constraints. Do not batch-delete files or directories. If temporary overview images are created for visual analysis, delete only one explicit file path at a time, or leave them and tell the user.

