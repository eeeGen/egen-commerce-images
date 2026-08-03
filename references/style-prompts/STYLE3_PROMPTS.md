# style3 Universal Product Generation Index and GPT Image 2 Prompts

Positioning: premium black-and-white performance technology style. This file applies to any general product and is not bound to the original category of any reference image. During generation, inherit only the visual style, composition, information hierarchy, UI components, scene logic, and selling-point logic.

## Mandatory Universal Product Rules

- `{product}` must come from the product image uploaded or explicitly confirmed by the user in the current chat, and it is the only source of truth for product appearance.
- Do not copy any product, brand, structure, accessory, parameter, person, scene fact, certification, or copywriting from reference images.
- Replace all category-specific content with variables: `{product_category}`, `{use_context}`, `{target_user}`, `{selling_points}`, `{specs}`, `{accessories}`, `{scenes}`, `{language}`.
- If the product does not fit an original reference scene, abstract the scene into equivalent visual logic, such as "dark atmospheric scene", "coverage-range visualization", or "clean lifestyle scene", instead of reusing the original product scene.
- Any number, certification, compatibility target, comparison conclusion, material, effect claim, or accessory count must come from user-provided information. Use neutral placeholder wording when information is missing.
- On-image text must be short, readable, and adapted to `{language}`. Do not generate garbled text, platform logos, competitor brands, official endorsements, or absolute promises.

## Style DNA

- Visual style: a premium system combining clean white-background technical pages with black-background high-performance scene pages. Use black, white, deep blue, gold, and silver gray to communicate performance, speed, quality, compatibility, comparison, and professional credibility for any product.
- Design logic: white-background pages explain structure, compatibility, dimensions, and tables; black-background pages express performance, immersion, speed, and premium impact.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Product placement principle: choose front view, 3/4 angle, diagonal angle, flat lay, floating display, in-scene use, or detail close-up according to the real form of `{product}`. Do not alter product proportions, color, material, ports, accessories, or structure.

## Prompt Variables

- `{product}`: any user-confirmed product.
- `{product_category}`: the product category, used to select copy and scenes, not to change appearance.
- `{brand}`: the user-provided brand; omit it if unavailable.
- `{headline}` / `{subheadline}`: the headline and subheadline for this image.
- `{selling_points}`: verified selling points.
- `{specs}`: verified specifications.
- `{accessories}`: verified accessories.
- `{scenes}` / `{use_context}`: realistic generalized scenes suitable for this product.
- `{language}`: the target country or platform language.

## style3_feature.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: structural cutaway/detail breakdown.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: large close-up of a product detail, surrounded by labels, on a premium white technical background.
- Information hierarchy: function headline first, real product structure/components second, callout explanations third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: no complex scene.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: support selling points with the product's real structure, components, or working method; do not invent internal structures.
- Product placement form: key area occupies 50%-65% of the image; do not create a cutaway when the internal structure is unknown.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Feature/structure image". Target filename token: Feature. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: create a large close-up of a product detail, surrounded by precise callout labels, on a premium white technical background. Product placement: the key area should occupy 50%-65% of the image; do not create a cutaway when the internal structure is unknown. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: function headline first, real product structure/components second, callout explanations third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: no complex scene. If any context is needed, select it from {scenes} and {use_context}, adapt it to the current {product_category}, and do not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue speed light trails where relevant, precise shadows on white backgrounds, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, beam, shadow, and highlight must support product recognition and selling-point expression; do not imply fake functions.

Selling-point logic: support each selling point with the product's real structure, components, or working method. Do not invent internal structures, numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style3_corea.png

### Universal Generation Index

- Image type: Core value scene image A / CoreA.
- Variant positioning: first high-value experience scene.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: real scene background + foreground product + corner specification badge.
- Information hierarchy: first core use scenario first, the product's real participation in the scene second, a small number of selling points third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: choose the first core scene according to the product, such as home, office, professional, display, or creation scenarios.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: show the most typical and important reason to buy; automatically replace the scene according to the product category.
- Product placement form: product occupies 25%-40% of the image and has a clear relationship with the scene result.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Core value scene image A". Target filename token: CoreA. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: build a real scene background with the product in the foreground and a corner specification badge. Product placement: the product should occupy 25%-40% of the image and clearly connect to the scene result. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: first core use scenario first, the product's real participation in the scene second, a small number of selling points third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: choose the first core scene according to the product, such as home, office, professional, display, or creation scenarios. The scene must be selected from {scenes} and {use_context}, adapted to the current {product_category}, and must not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue speed light trails where relevant, neon accents only when the scene supports them, precise shadows, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, beam, shadow, and highlight must support product recognition and selling-point expression; do not imply fake functions.

Selling-point logic: show the most typical and important reason to buy, with the scene automatically adjusted to the product category. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style3_feature_2.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: compatibility/input-output matrix.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: place a compatibility object matrix, checkmarks, and relationship labels beside the product.
- Information hierarchy: function headline first, real product structure/components second, callout explanations third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: use generic object icons only; do not show third-party brands.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: support selling points with the product's real structure, components, or working method; do not invent internal structures.
- Product placement form: clearly show the key connection or operation area.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Feature/structure image". Target filename token: Feature. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: place a compatibility object matrix, checkmarks, and relationship labels beside the product. Product placement: clearly show the key connection or operation area. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: function headline first, real product structure/components second, callout explanations third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use a clear compatibility/input-output matrix with generic object icons, checkmarks, relationship labels, black bottom specification bars, gold specification badges, blue linear icons, and optional comparison tables. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: use generic object icons only and never display third-party brands. Any contextual cue must be selected from {scenes} and {use_context}, adapted to the current {product_category}, and must not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue speed light trails where relevant, precise shadows on white backgrounds, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, beam, shadow, and highlight must support product recognition and selling-point expression; do not imply fake functions.

Selling-point logic: support each selling point with the product's real structure, components, or working method. Do not invent internal structures, numbers, certifications, compatibility targets, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style3_lifestyle.png

### Universal Generation Index

- Image type: Lifestyle/result image / Lifestyle.
- Variant positioning: professional/office result scene.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: bright scene background, foreground product, bottom icon strip.
- Information hierarchy: use result or scene benefit first, product-scene relationship second, a small number of icon explanations third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: choose an office, meeting, display, production, learning, or creation environment according to the product.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: use realistic generalized scenes to show the usage result brought by the product without exaggerating effects.
- Product placement form: product occupies 25%-40% of the image and connects to a scene action.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Lifestyle/result image". Target filename token: Lifestyle. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: create a bright scene background with the product in the foreground and a bottom icon strip. Product placement: the product should occupy 25%-40% of the image and connect naturally to a scene action. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: use result or scene benefit first, product-scene relationship second, a small number of icon explanations third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices when they support the story. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: choose an office, meeting, display, production, learning, or creation environment according to the product. The scene must be selected from {scenes} and {use_context}, adapted to the current {product_category}, and must not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue speed light trails where relevant, precise shadows on white backgrounds, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, beam, shadow, and highlight must support product recognition and selling-point expression; do not imply fake functions.

Selling-point logic: use realistic generalized scenes to show the usage result brought by the product without exaggerating effects. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style3_coreb.png

### Universal Generation Index

- Image type: Core value scene image B / CoreB.
- Variant positioning: second high-performance scene.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: immersive black-background scene, diagonal foreground product, speed/energy light effects.
- Information hierarchy: second core use scenario first, differentiated user/space/result second, a small number of selling points third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: differentiate from CoreA with a high-intensity, mobile, nighttime, professional, or immersive scene.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: separate the scene and audience from CoreA and show another high-value use path.
- Product placement form: product occupies 30%-45% of the image and acts as the visual guide for performance.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Core value scene image B". Target filename token: CoreB. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: create an immersive black-background scene with the product placed diagonally in the foreground and supported by speed or energy light effects. Product placement: the product should occupy 30%-45% of the image and act as the visual guide for performance. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: second core use scenario first, differentiated user/space/result second, a small number of selling points third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices when they support the performance story. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: differentiate this image from CoreA with a high-intensity, mobile, nighttime, professional, or immersive scene. The scene must be selected from {scenes} and {use_context}, adapted to the current {product_category}, and must not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows where needed, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, beam, shadow, and highlight must support product recognition and selling-point expression; do not imply fake functions.

Selling-point logic: separate the scene and audience from CoreA and show another high-value use path. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style3_compare.png

### Universal Generation Index

- Image type: Comparison advantage image / Compare.
- Variant positioning: product vs generic ordinary product.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: left-right split layout, user product highlighted, ordinary product desaturated or grayed out.
- Information hierarchy: comparison headline first, user product and generic ordinary product second, check/cross table third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: white-background comparison table.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: compare only provable differences; represent the ordinary product with a brandless generic placeholder.
- Product placement form: user product and ordinary product must be the same size; the ordinary product must not imitate any competitor.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Comparison advantage image". Target filename token: Compare. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: create a left-right split layout with the user product highlighted and a generic ordinary product desaturated or grayed out. Product placement: the user product and ordinary product must be the same size; the ordinary product must be a brandless generic placeholder and must not imitate any competitor. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details of the user product. Do not add unconfirmed parts.

Information hierarchy: comparison headline first, user product and generic ordinary product second, check/cross comparison table third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use a white-background comparison table with clean columns, check/cross indicators, black bottom specification bars, gold specification badges, blue linear icons, and optional compatibility matrices only when they are supported by user-provided information. Add rounded cards, icon strips, data panels, step cards, specification labels, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: keep the scene as a white-background comparison table. Do not introduce a lifestyle scene unless it is selected from {scenes} and {use_context}, adapted to the current {product_category}, and necessary for a verified comparison point. Do not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, precise white-background shadows, high-sharpness product rendering, controlled reflections, and restrained emphasis lighting on the user product. Avoid effects that imply unverified superiority. Every highlight must support product recognition and comparison readability.

Selling-point logic: compare only differences that can be proven from user-provided information. The comparison must be between the user product and a brandless generic ordinary product, not a named competitor or platform. Do not invent numbers, certifications, compatibility targets, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a compliant, production-grade ecommerce comparison detail image ready for direct use.
```

## style3_value.png

### Universal Generation Index

- Image type: Differentiated value image / Value.
- Variant positioning: specification/value table.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: large table or value-breakdown panel, with the product as side support.
- Information hierarchy: value headline first, value breakdown/data visualization second, product third.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: minimal technical page.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: translate differentiated value into readable data panels, benefit breakdowns, or factual explanations.
- Product placement form: product occupies 25%-35% of the image and does not block the table.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Differentiated value image". Target filename token: Value. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: create a large table or value-breakdown panel, with the product placed on the side as supporting visual evidence. Product placement: the product should occupy 25%-35% of the image and must not block the table. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: value headline first, value breakdown or data visualization second, product third. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use a minimal technical page with readable data panels, benefit breakdowns, factual explanation blocks, black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices where supported. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel professional, not cluttered.

Scene expression: keep the image as a minimal technical page. If contextual support is needed, select it from {scenes} and {use_context}, adapt it to the current {product_category}, and do not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue accents where relevant, precise white-background shadows, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, shadow, and highlight must support product recognition and value explanation; do not imply fake functions.

Selling-point logic: translate differentiated value into readable data panels, benefit breakdowns, or factual explanations. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce value detail image ready for direct use.
```

## style3_hero.png

### Universal Generation Index

- Image type: Hero image / Hero.
- Variant positioning: black-and-gold performance Hero.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: black background with speed light trails, enlarged diagonal product, bottom specification bar.
- Information hierarchy: product body first, main headline second, 3-6 core selling points third, bottom specifications or scene support fourth.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: abstract performance background without any specific IP.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: establish product recognition, core value, and reasons to buy in one image; avoid stacking unconfirmed specifications.
- Product placement form: product occupies 40%-55% of the image, with the key face oriented toward the camera.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Hero image". Target filename token: Hero. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: create a black background with speed light trails, an enlarged diagonal product, and a bottom specification bar. Product placement: the product should occupy 40%-55% of the image, with the key face oriented toward the camera. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: product body first, main headline second, 3-6 core selling points third, bottom specifications or scene support fourth. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use a premium black-and-gold performance layout with a black bottom specification bar, gold specification badges, blue linear icons, comparison tables, and compatibility matrices where supported. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel premium and decisive, not cluttered.

Scene expression: use an abstract performance background without any specific IP. If scene context is needed, select it from {scenes} and {use_context}, adapt it to the current {product_category}, and do not reuse the original product scene from reference images.

Effects rendering: use metallic highlights, blue speed light trails, restrained neon accents on the black background, high-sharpness product rendering, controlled reflections, and local highlights. Every light effect, reflection, beam, shadow, and highlight must support product recognition and core value expression; do not imply fake functions.

Selling-point logic: establish product recognition, core value, and reasons to buy in one image while avoiding unconfirmed specifications. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce hero detail image ready for direct use.
```

## style3_specs.png

### Universal Generation Index

- Image type: Size/specification image / Specs.
- Variant positioning: white-background dimensions page.
- Visual style: follow the premium black-and-white performance technology style, while replacing every product and scene with the current `{product}` and its general-product expression.
- Composition: product flat lay/front view, dimension lines, and small specification cards.
- Information hierarchy: dimensions/specification headline first, front-view or flat-lay product second, rulers and parameters third, package list fourth.
- Layout: the headline, product, selling points, specs, icons, and scene modules must have clear whitespace; text must not press into or cover the product.
- Icon system: black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices.
- Scene expression: no complex scene.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for this image type; keep all component margins and alignment consistent.
- Effects rendering language: metallic highlights, blue speed light trails, neon accents on black backgrounds, precise shadows on white backgrounds, and high-sharpness product rendering.
- Selling-point logic: reduce pre-purchase size misunderstanding; show only user-confirmed numbers and lists.
- Product placement form: product occupies 45%-60% of the image, and dimension points align with real product boundaries.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Size/specification image". Target filename token: Specs. Use the visual DNA of "premium black-and-white performance technology style": clean white-background technical pages combined with black-background high-performance scene pages, using black, white, deep blue, gold, and silver gray to express performance, speed, quality, compatibility, comparison, and professional credibility.

Composition: show the product in flat lay or front view with dimension lines and small specification cards. Product placement: the product should occupy 45%-60% of the image, and dimension points must align with real product boundaries. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: dimensions/specification headline first, front-view or flat-lay product second, rulers and parameters third, package list fourth. Use {headline} as the main headline and {subheadline} as the secondary headline. Selling points must come from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use a white-background technical dimensions page with precise dimension lines, specification cards, black bottom specification bars, gold specification badges, blue linear icons, comparison tables, and compatibility matrices where supported. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they fit this image type. Keep component spacing consistent, keep alignment precise, and prevent text from covering the product. The information density should feel technical and readable, not cluttered.

Scene expression: no complex scene. If any contextual cue is needed, select it from {scenes} and {use_context}, adapt it to the current {product_category}, and do not reuse the original product scene from reference images.

Effects rendering: use precise shadows on white backgrounds, high-sharpness product rendering, subtle metallic highlights where appropriate, controlled reflections, and local highlights. Every shadow and highlight must support product recognition and measurement readability; do not imply fake functions.

Selling-point logic: reduce pre-purchase size misunderstanding by showing only user-confirmed numbers, dimensions, specifications, accessories, and package lists. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce specification detail image ready for direct use.
```
