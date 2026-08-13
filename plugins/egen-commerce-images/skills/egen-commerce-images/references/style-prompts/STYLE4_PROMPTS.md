# style4 Universal Product Generation Index and Prompts

Positioning: blue safety-coverage and monitoring-technology style. This file applies to any general product and is not tied to the original category of any reference image. During generation, inherit only the visual style, composition, information hierarchy, UI components, scene expression, and selling-point logic.

## Mandatory Universal Product Rules

- `{product}` must come from the product image uploaded or explicitly confirmed by the user in the current chat, and it is the only source of truth for product appearance.
- Do not copy the product, brand, structure, accessories, parameters, people, scene facts, certifications, or copywriting from reference images.
- Replace all category-specific content with variables: `{product_category}`, `{use_context}`, `{target_user}`, `{selling_points}`, `{specs}`, `{accessories}`, `{scenes}`, `{language}`.
- If the product does not fit an original reference scene, abstract the scene into equivalent visual logic, such as "dark atmospheric scene", "coverage-range visualization", or "clean lifestyle scene", instead of reusing the original product scene.
- Any numbers, certifications, compatibility targets, comparison conclusions, materials, effects, or accessory counts must come from user-provided information. If they are missing, use neutral placeholder wording.
- On-image text must be short, readable, and adapted to `{language}`. Do not generate garbled text, platform logos, competitor brands, official endorsements, or absolute claims.

## Style DNA

- Primary palette: #345a91 + #f2d84d
- Visual style: professional technology style emphasizing safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. It is suitable for making any product feel clearer, more controllable, more reassuring, and more visually covered.
- Design logic: large headline + product + blue coverage/path/monitoring beams + bottom specification bar. Use structured UI for process diagrams and comparison images.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Product placement principle: choose front view, 3/4 angle, diagonal view, flat lay, floating display, in-scene use, or detail close-up according to the real form of `{product}`. Do not alter product proportions, color, material, ports, accessories, or structure.

## Prompt Variables

- `{product}`: any user-confirmed product.
- `{product_category}`: the product category, used to select copy and scenes, not to change product appearance.
- `{brand}`: user-provided brand; omit it if unavailable.
- `{headline}` / `{subheadline}`: headline and subheadline for this image.
- `{selling_points}`: verified selling points.
- `{specs}`: verified specifications.
- `{accessories}`: verified accessories.
- `{scenes}` / `{use_context}`: realistic generalized scenes suitable for this product.
- `{language}`: target country or platform language.

## style4_guide.png

### Universal Generation Index

- Image type: Product usage guide / Guide.
- Variant positioning: three-step installation or usage workflow.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: show the real usage position in the upper half and three step-flow cards in the lower half.
- Information hierarchy: step headline first, numbered workflow second, product action third, caution note or accessory fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: installation, placement, connection, activation, or maintenance workflow for any product.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: reduce the usage barrier with real steps. Do not invent installation or operating procedures.
- Product placement form: place the product in a reasonable use position without blocking key areas.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Product usage guide". Target filename token: Guide. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: show the real usage position in the upper half and three step-flow cards in the lower half. Product placement: place the product in a reasonable use position without blocking key areas. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: step headline first, numbered workflow second, product action third, caution note or accessory fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: show an installation, placement, connection, activation, or maintenance workflow for the current product. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: use real steps to reduce the usage barrier, without inventing installation or operating procedures. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_specs.png

### Universal Generation Index

- Image type: Size and specification image / Specs.
- Variant positioning: dimensions + packing list.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: show the product from multiple angles on a white background, with dimension lines and an accessory list box.
- Information hierarchy: dimension/specification title first, front-view or flat-lay product second, measurement guides and parameters third, packing list fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: specification page, with no complex scene.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: reduce pre-purchase dimension misunderstanding, and show only user-confirmed numbers and list items.
- Product placement form: group the product and verified accessories clearly.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Size and specification image". Target filename token: Specs. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: show the product from multiple angles on a white background, with dimension lines and an accessory list box. Product placement: group the product and verified accessories clearly. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: dimension/specification title first, front-view or flat-lay product second, measurement guides and parameters third, packing list fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: create a specification page with no complex scene. Select scenes from {scenes} and {use_context} only when needed for the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: reduce pre-purchase dimension misunderstanding, and show only user-confirmed numbers and packing-list items. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_feature.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: coverage range or visualized function.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: product in the foreground, with blue fan-shaped beams, paths, or coverage lines explaining the functional range.
- Information hierarchy: feature title first, real product structure or component second, callout explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: adapt the scene to the product, such as desktop, room, outdoor area, workspace, or use space.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: support selling points with the product's real structure, components, or working method. Do not invent internal structures.
- Product placement form: beams must originate from real functional points on the product.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Feature/structure image". Target filename token: Feature. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: place the product in the foreground, with blue fan-shaped beams, paths, or coverage lines explaining the functional range. Product placement: beams must originate from real functional points on the product. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: feature title first, real product structure or component second, callout explanation third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: adapt the scene to the product, such as desktop, room, outdoor area, workspace, or use space. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: support selling points with the product's real structure, components, or working method, without inventing internal structures. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_feature_2.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: cycle, workflow, or protection function.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: centered product surrounded by a circular workflow band or status cards.
- Information hierarchy: feature title first, real product structure or component second, callout explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: abstract workflow background, without accident imagery or fear-based visuals.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: support selling points with the product's real structure, components, or working method. Do not invent internal structures.
- Product placement form: keep the product screen, panel, or key area clear.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Feature/structure image". Target filename token: Feature. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: center the product and surround it with a circular workflow band or status cards. Product placement: keep the product screen, panel, or key area clear. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: feature title first, real product structure or component second, callout explanation third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: use an abstract workflow background, without accident imagery or fear-based visuals. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: support selling points with the product's real structure, components, or working method, without inventing internal structures. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_lifestyle.png

### Universal Generation Index

- Image type: Lifestyle/result image / Lifestyle.
- Variant positioning: low-light or complex-environment result.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: main scene + two result comparison boxes at the bottom.
- Information hierarchy: usage result or scene benefit first, relationship between product and scene second, small icon explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: choose a night, low-light, busy, outdoor, or complex environment according to the product.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: use realistic generalized scenes to show product-driven usage results without exaggerating effects.
- Product placement form: show the product in an actual use position.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Lifestyle/result image". Target filename token: Lifestyle. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: create a main scene with two result comparison boxes at the bottom. Product placement: show the product in an actual use position. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: usage result or scene benefit first, relationship between product and scene second, small icon explanations third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: choose a night, low-light, busy, outdoor, or complex environment according to the product. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: use realistic generalized scenes to show product-driven usage results without exaggerating effects. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_corea.png

### Universal Generation Index

- Image type: Core value scene image A / CoreA.
- Variant positioning: primary safety or reassurance scene.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: real main scene + product + multi-image or multi-state result cards.
- Information hierarchy: primary core use scene first, the product's real participation method second, a small number of selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: choose the core scene that best expresses reassurance, recording, coverage, control, or protection.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: show the most typical and important purchase reason, with the scene automatically adapted to the product category.
- Product placement form: the product should occupy 30%-45% of the image and relate clearly to the scene result.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Core value scene image A". Target filename token: CoreA. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: create a real main scene with the product and multi-image or multi-state result cards. Product placement: the product should occupy 30%-45% of the image and relate clearly to the scene result. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: primary core use scene first, the product's real participation method second, a small number of selling points third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: choose the core scene that best expresses reassurance, recording, coverage, control, or protection. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: show the most typical and important purchase reason, with the scene automatically adapted to the product category. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_lifestyle_2.png

### Universal Generation Index

- Image type: Lifestyle/result image / Lifestyle.
- Variant positioning: protection or monitoring result.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: scene background + product + lock/shield/protection light effect + bottom selling-point bar.
- Information hierarchy: usage result or scene benefit first, relationship between product and scene second, small icon explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: suitable for storage, in-use protection, status monitoring, or environmental reminders for any product.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: use realistic generalized scenes to show product-driven usage results without exaggerating effects.
- Product placement form: keep the product visible; protection symbols must not cover the main subject.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Lifestyle/result image". Target filename token: Lifestyle. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: create a scene background with the product, lock/shield/protection light effect, and a bottom selling-point bar. Product placement: keep the product visible; protection symbols must not cover the main subject. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: usage result or scene benefit first, relationship between product and scene second, small icon explanations third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: show storage, in-use protection, status monitoring, or environmental reminders suitable for the current product. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: use realistic generalized scenes to show product-driven usage results without exaggerating effects. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_compare.png

### Universal Generation Index

- Image type: Comparison advantage image / Compare.
- Variant positioning: coverage or range comparison.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: left-right comparison or top-down schematic, with blue coverage range versus gray limited range.
- Information hierarchy: comparison headline first, user product and generic ordinary product second, check/cross table third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: use a generalized spatial schematic, not a specific device-bound scene.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: compare only provable differences. The ordinary product must be a brandless generic placeholder.
- Product placement form: keep the user product and generic solution at comparable visual size.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Comparison advantage image". Target filename token: Compare. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: create a left-right comparison or top-down schematic, with blue coverage range versus gray limited range. Product placement: keep the user product and generic solution at comparable visual size. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: comparison headline first, user product and generic ordinary product second, check/cross table third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: use a generalized spatial schematic, not a specific device-bound scene. Select scenes from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: compare only provable differences, and show the ordinary product as a brandless generic placeholder. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style4_compare_2.png

### Universal Generation Index

- Image type: Comparison advantage image / Compare.
- Variant positioning: reason-to-choose table.
- Visual style: follow the blue safety-coverage and monitoring-technology style, while replacing all products and scenes with a general-product expression for the current `{product}`.
- Composition: product comparison at the top, with a 6-8 row check/cross table below.
- Information hierarchy: comparison headline first, user product and generic ordinary product second, check/cross table third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Do not let text press against or cover the product.
- Icon system: blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons.
- Scene expression: white-background data page.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to the image type, with consistent spacing and alignment across all components.
- Effects rendering language: blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background.
- Selling-point logic: compare only provable differences. The ordinary product must be a brandless generic placeholder.
- Product placement form: render the ordinary product as brandless, gray, and generic.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance, and generate a 1:1 ecommerce detail image for a general product. Image type: "Comparison advantage image". Target filename token: Compare. Use the visual DNA of "blue safety-coverage and monitoring-technology style": a professional white-gray-blue technology look that emphasizes safety, coverage range, a monitoring viewpoint, workflow clarity, protection, and comparison. The image should make any product feel clearer, more controllable, more reassuring, and more visually covered.

Composition requirements: place the product comparison at the top, with a 6-8 row check/cross table below. Product placement: render the ordinary product as brandless, gray, and generic. Preserve the real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts.

Information hierarchy: comparison headline first, user product and generic ordinary product second, check/cross table third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}; keep it short, readable, and free of garbled characters.

Layout and UI: use blue shield, lock, field-of-view, step, coverage, check/cross, and specification icons. Add rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails according to this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, not cluttered.

Scene expression: create a white-background data page. Select scenes from {scenes} and {use_context} only when needed for the current {product_category}. Do not reuse the original product scene from reference images.

Effects rendering: use blue transparent beams, glass reflections, crisp screen or panel glow, and a professional white-gray background. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point expression without creating fake functions.

Selling-point logic: compare only provable differences, and show the ordinary product as a brandless generic placeholder. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute claims, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```
