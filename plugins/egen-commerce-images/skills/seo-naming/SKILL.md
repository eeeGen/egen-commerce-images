---
name: seo-naming
description: Rename and organize ecommerce product images with structured SEO-friendly filenames. Use when Codex needs to analyze product image content, assign marketplace image types such as Hero/Selling/Feature/Specs/Lifestyle, research Mercado Libre same-category top-selling listing keywords, and rename image files with product code, type order, and SEO terms.
---

# Product Image SEO Naming

## Overview

Use this skill to rename ecommerce product images into structured SEO-friendly filenames for marketplace operations, asset management, and database tracking.

Before assigning image types or renaming files, read [the naming standard](references/naming-standard.md). It is the canonical source for filename syntax, image-type definitions and order, and examples.

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
6. Assign image types according to visual content and the definitions and order in the naming standard. Types may be omitted or repeated.
7. Follow the naming standard and use stable temporary names first when target names may collide.
8. Verify the final folder listing, checking sequence, type order, missing or duplicate types, and extensions.

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

## Database Notes

When relevant, explain that filenames are not database primary keys. Store structured fields separately:

```text
id, product_code, sort_order, image_type, original_filename, current_filename,
seo_filename, storage_path, public_url, platform, locale, version, is_active,
width, height, file_size, mime_type, checksum, created_at, updated_at
```

## Safety

Respect local deletion constraints. Do not batch-delete files or directories. If temporary overview images are created for visual analysis, delete only one explicit file path at a time, or leave them and tell the user.

