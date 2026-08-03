# style1 Universal Product Generation Index and GPT Image 2 Prompts

Positioning: blue and white technical specification style. This file applies to any generic product and is not tied to the original category of any reference image. During generation, inherit only the visual style, composition, information hierarchy, UI components, scene treatment, and selling-point logic. Do not inherit product facts from reference images.

## Mandatory Universal Product Rules

- `{product}` must come from the product image uploaded or explicitly confirmed by the user in the current chat. It is the only source of truth for product appearance.
- Do not copy the product, brand, structure, accessories, parameters, people, scene facts, certifications, or copywriting from reference images.
- Replace all category-specific content with variables: `{product_category}`, `{use_context}`, `{target_user}`, `{selling_points}`, `{specs}`, `{accessories}`, `{scenes}`, `{language}`.
- If the current product does not fit an original reference scene, abstract that scene into equivalent visual logic, such as a dark atmospheric scene, a coverage-range diagram, or a fresh lifestyle scene. Do not reuse the original product scene.
- Any numbers, certifications, compatible objects, comparison conclusions, materials, effects, and accessory counts must come from user-provided information. If information is missing, use neutral placeholder wording instead of invented claims.
- On-image text must be short, readable, and adapted to `{language}`. Do not generate garbled text, platform logos, competitor brands, official endorsements, or absolute promises.

## Style DNA

- Visual style: bright blue and white technical ecommerce style with a light gray background, blue visual anchors, rounded cards, structural labels, and specification visualization. Suitable for any product that needs to explain functions, specifications, structure, or use scenarios.
- Design logic: large headline at the top, product in the center, card-based selling points around it. Structural diagrams use numbered callouts. Scene images use grid layouts.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Product placement principle: choose front view, three-quarter angle, diagonal view, flat lay, floating display, in-scene use, or close-up based on the real form of `{product}`. Do not alter product proportions, color, material, ports, accessories, or structure.

## Prompt Variables

- `{product}`: any user-confirmed product.
- `{product_category}`: the product category, used to choose copy and scenes, never to change appearance.
- `{brand}`: the user-provided brand. Omit brand text entirely if `{brand}` is missing, unknown, or not confirmed by the user.
- `{headline}` / `{subheadline}`: the main headline and subheadline for the current image.
- `{selling_points}`: verified selling points.
- `{specs}`: verified specifications.
- `{accessories}`: verified accessories.
- `{scenes}` / `{use_context}`: realistic generalized scenes suitable for this product.
- `{target_user}`: the verified target audience or user role. Use it only for audience relevance and use-context framing. Do not invent demographics, professional qualifications, medical needs, or authority claims.
- `{language}`: the language used by the target country or platform.

## style1_hero.png

### Universal Generation Index

- Image type: Main image / Hero.
- Variant positioning: bright specification Hero.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: show the product large in the center or at a diagonal angle, with 4-6 selling-point icons along the side.
- Information hierarchy: product first, main headline second, 3-6 core selling points third, bottom specifications or scene support fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: the background must not compete with the product. Use either a faded scene or an abstract technical background.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: establish product recognition, core value, and purchase rationale in one screen without stacking unconfirmed specifications.
- Product placement form: product occupies 45%-65% of the image. Choose flat lay, standing display, floating display, or three-quarter angle based on product form.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Main image. Target filename token: Hero. Use the visual DNA of a blue and white technical specification style: bright blue and white ecommerce design, light gray background, blue visual anchors, rounded cards, structural labels, and specification visualization.

Place the product large in the center or at a clean diagonal angle, with 4-6 selling-point icons along the side. The product should occupy 45%-65% of the image. Preserve real proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts, functions, attachments, packaging, or decorative product features.

Information hierarchy: product first, {headline} second, 3-6 core selling points from {selling_points} third, and bottom support from {specs}, {accessories}, {scenes}, or {use_context} fourth. Use {subheadline} only for verified context. If {brand} is confirmed, place it subtly; otherwise omit brand text. Use {target_user} only to make benefit framing relevant, not to invent demographics or authority claims. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, magnifier labels, generic device or scene icons, rounded cards, icon strips, data panels, step cards, specification labels, comparison tables, or scene thumbnails only when they support the image type. Keep spacing consistent, alignment precise, and text off the product.

Use a faded scene or abstract technical background selected from {scenes} and {use_context}, suitable for {product_category}. Treat reference images as style references only. Do not reuse original reference product scenes, setting facts, people, claims, or copy.

Use light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework. Do not visualize fake functions, fake performance, or unrealistic effects. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, award badges, safety guarantees, medical claims, or regulatory claims.
```

## style1_specs.png

### Universal Generation Index

- Image type: Size and specification image / Specs.
- Variant positioning: dimensions and fit space.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: show the product horizontally or front-facing, with dimension lines around it and 2-4 fit-scenario cards at the bottom.
- Information hierarchy: size or specification headline first, front-view or flat-lay product second, rulers and parameters third, package list fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: express fit space through generic cards, such as desktop, storage, installation area, or usage radius.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: reduce pre-purchase size misunderstanding by showing only user-confirmed numbers and lists.
- Product placement form: keep the product unobstructed, with rulers aligned to real product boundaries.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Size and specification image. Target filename token: Specs. Use the blue and white technical specification style.

Show the product horizontally, front-facing, or as a clean flat lay, with dimension lines around the real product outline and 2-4 fit-scenario cards at the bottom. Keep the product unobstructed and align rulers, arrows, and dimension guides to real visible boundaries. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts or resize the product in a misleading way.

Information hierarchy: size or specification headline first, product second, rulers and parameters from {specs} third, package list from {accessories} fourth. Use {headline} and {subheadline} only for verified sizing, fit, or product-context messaging. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only when it clarifies verified fit context. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, magnifier labels, generic fit-space icons, dimension arrows, rulers, specification labels, and rounded cards. Express fit space through generic cards selected from {scenes} and {use_context}, suitable for {product_category}. Examples may include desktop, storage, installation area, usage radius, shelf, bag, counter, wall area, or vehicle space only when confirmed.

Use only numbers, sizes, materials, accessories, and quantities from {specs} or {accessories}. If data is missing, use neutral labels such as Size Details, Fit Guide, or Package Includes without invented values. Do not invent certifications, compatibility, official endorsements, absolute promises, platform marks, or competitor comparisons.
```

## style1_feature.png

### Universal Generation Index

- Image type: Function or structure image / Feature.
- Variant positioning: numbered structure breakdown.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: center a product detail or cutaway view, using 01/02/03 modules to explain real structure.
- Information hierarchy: function headline first, real product structure or component second, callout explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: abstract technical background, without complex lifestyle scenery.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: support selling points with the product's real structure, real components, or verified working method. Do not invent internal structure.
- Product placement form: show only internal or external structures confirmed by the user.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Function or structure image. Target filename token: Feature. Use the blue and white technical specification style.

Center a real product detail, exterior structure, or confirmed cutaway view. Use 01/02/03 modules to explain verified structure. Show only internal or external structures confirmed by the user. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed hidden mechanisms, sensors, layers, circuitry, filters, coatings, or exploded-view components.

Information hierarchy: function headline first, real product structure or component second, callout explanation third. Use {headline}, {subheadline}, {selling_points}, {specs}, and {accessories} only when verified. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to frame why the verified structure matters for that user. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, magnifier labels, callout arrows, structure labels, and rounded explanation cards. Use an abstract technical background only. Treat reference images as style references only. Do not reuse their product structure, labels, scene facts, or claims.

Highlight only visible or confirmed structures. Do not render fake cross-sections, fake transparency, fake internal mechanisms, or exaggerated functional effects. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, or regulatory claims.
```

## style1_feature_2.png

### Universal Generation Index

- Image type: Function or structure image / Feature.
- Variant positioning: key component callout.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: show a large central component or key area, with explanation cards in the four corners connected by arrows.
- Information hierarchy: function headline first, real product structure or component second, callout explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: no scene; focus on credible details.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: support selling points with the product's real structure, real components, or verified working method. Do not invent internal structure.
- Product placement form: enlarge the key area to 45%-60% of the image without obstruction.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Function or structure image. Target filename token: Feature. Use the blue and white technical specification style.

Show a large central component or key product area, with explanation cards in the four corners connected by clean arrows. Enlarge the key area to 45%-60% of the image without obstruction. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed components, internal layers, surface treatments, attachments, or mechanisms.

Information hierarchy: function headline first, real component or structure second, callout explanation third. Use {headline}, {subheadline}, {selling_points}, {specs}, and {accessories} only for verified details. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to clarify audience relevance. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, magnifier labels, callout arrows, structure labels, and rounded cards. Do not include a scene. Treat reference images as style references only. Do not reuse their original product, component labels, setting facts, or claims.

Highlight only the confirmed detail being explained. Do not visualize fake functions, fake performance, or unverified structure. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, or regulatory claims.
```

## style1_feature_3.png

### Universal Generation Index

- Image type: Function or structure image / Feature.
- Variant positioning: close-up detail plus specification card.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: product close-up on the right, vertical selling-point cards on the left, and a small specification strip at the bottom.
- Information hierarchy: function headline first, real product structure or component second, callout explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: white-background technical infographic.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: support selling points with the product's real structure, real components, or verified working method. Do not invent internal structure.
- Product placement form: bring a key functional surface, port, button, texture, or structural node close to the camera.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Function or structure image. Target filename token: Feature. Use a white or light gray blue and white technical infographic style.

Place a product close-up on the right, vertical selling-point cards on the left, and a compact specification strip at the bottom. Bring a key functional surface, port, button, texture, seam, or structural node close to the camera only if it exists in the confirmed product image or user data. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed buttons, ports, textures, coatings, modules, or mechanisms.

Information hierarchy: function headline first, real product detail second, callout explanation third. Use {headline}, {subheadline}, {selling_points}, {specs}, and {accessories} only for verified product information. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to explain relevance to verified use. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, magnifier labels, callout arrows, vertical feature cards, and a bottom specification strip. Treat reference images as style references only. Do not reuse their original product, detail labels, scenes, facts, or copy.

Highlight only the confirmed detail being explained. Do not create fake macro texture, fake material, fake transparency, or fake functional effects. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, or regulatory claims.
```

## style1_selling.png

### Universal Generation Index

- Image type: Pain-point or selling-point image / Selling.
- Variant positioning: durability, reliability, and reassurance selling points.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: selling-point headline at the top, horizontal icon cards, product and abstract environment below.
- Information hierarchy: user pain point or benefit headline first, product solution second, icon selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: use an abstract environment as a metaphor for everyday challenges. Do not show unverified extreme testing.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: begin with a generalized use pain point, then use verified selling points to explain how the product addresses it.
- Product placement form: display the product stably in the lower-middle area, occupying 35%-50% of the image.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Pain-point or selling-point image. Target filename token: Selling. Use the blue and white technical specification style.

Place a selling-point headline at the top, a horizontal row of icon cards beneath it, and the product in a stable lower-middle position with an abstract environment around it. Display the product clearly, occupying 35%-50% of the image. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed protective layers, testing equipment, damage marks, accessories, or features.

Information hierarchy: user pain point or benefit headline first, product solution second, icon selling points third. Use {headline}, {subheadline}, and {selling_points} to communicate only verified benefits. Use {specs} and {accessories} only when relevant and confirmed. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} to frame the pain point for a verified audience or use case, not to invent user identity, professional status, or special needs. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, rounded cards, benefit labels, and a clean icon strip. Use an abstract environment to suggest everyday challenges or use context selected from {scenes} and {use_context}, suitable for {product_category}. Do not show unverified extreme testing, destructive comparisons, safety demonstrations, medical scenarios, or official certification environments.

Effects may imply clarity, organization, stability, or reassurance, but must not imply unverified durability, protection, performance, or guaranteed outcomes. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, or regulatory claims.
```

## style1_selling_2.png

### Universal Generation Index

- Image type: Pain-point or selling-point image / Selling.
- Variant positioning: core benefit plus icon column.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: large central product, vertical icon selling points beside it, optional core benefit phrase in the center.
- Information hierarchy: user pain point or benefit headline first, product solution second, icon selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: abstract background that emphasizes the purchase rationale.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: begin with a generalized use pain point, then use verified selling points to explain how the product addresses it.
- Product placement form: use the product as the visual center, adapted to any product form.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Pain-point or selling-point image. Target filename token: Selling. Use the blue and white technical specification style.

Place the product as a large central visual anchor, add a vertical column of icon selling points beside it, and include an optional central core benefit phrase only when it comes from verified {selling_points}. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts, protective effects, accessories, or feature indicators.

Information hierarchy: user pain point or benefit headline first, product solution second, icon selling points third. Use {headline}, {subheadline}, and {selling_points} for verified benefit messaging. Use {specs} and {accessories} only when confirmed and useful. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to make the pain point or benefit relevant to the verified audience. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, rounded cards, benefit labels, vertical icon cards, and a clean central benefit phrase. Use an abstract background that supports the purchase rationale and fits {product_category}, {scenes}, and {use_context}. Treat reference images as style references only.

Effects must support product recognition and verified benefit communication, without implying fake performance or guaranteed outcomes. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, or regulatory claims.
```

## style1_value.png

### Universal Generation Index

- Image type: Differentiated value image / Value.
- Variant positioning: data or value visualization.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: large data panel, progress bar, or value breakdown cards, with the product as a supporting element nearby.
- Information hierarchy: value headline first, value breakdown or data visualization second, product third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: a faded device or scene background may be used, but it must stay generalized.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: translate differentiated value into readable data panels, benefit breakdowns, or factual explanations.
- Product placement form: product occupies 25%-40% of the image and supports the data panel.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Differentiated value image. Target filename token: Value. Use the blue and white technical specification style.

Build a large data panel, progress bar, or value breakdown card system, with the product placed nearby as a supporting visual. The product should occupy 25%-40% of the image and support the data panel rather than dominate it. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed parts, usage outputs, performance visuals, or comparison objects.

Information hierarchy: value headline first, value breakdown or data visualization second, product third. Use {headline}, {subheadline}, {selling_points}, and {specs} only for verified factual value. Use {accessories} only when the value includes confirmed package content. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to frame the value for a verified audience, not to invent market superiority, professional endorsement, or user outcomes. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, rounded cards, data panels, progress bars, value labels, factual notes, and optional comparison tables only when comparison data is user-confirmed. A faded device or scene background may be used if selected from {scenes} and {use_context}, suitable for {product_category}. Keep it generalized and secondary.

Effects should make the value panel readable and modern, without implying unverified performance, savings, protection, or guaranteed results. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, best-in-class statements, safety guarantees, medical claims, or regulatory claims.
```

## style1_lifestyle.png

### Universal Generation Index

- Image type: Scenario result image / Lifestyle.
- Variant positioning: single main scene plus scene support.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: main scene showing the relationship between product and use, with 3-4 scene cards at the bottom.
- Information hierarchy: use result or scenario benefit first, relationship between product and scene second, small icon explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: adapt to any product with home, office, outdoor, travel, or professional settings as appropriate.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: use realistic generalized scenes to show the product's use result without exaggerating effects.
- Product placement form: product occupies 30%-45% of the image, with a clear relationship to the use action or space.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Scenario result image. Target filename token: Lifestyle. Use the blue and white technical specification style.

Create one main scene that shows the relationship between the product and its real use context, with 3-4 supporting scene cards at the bottom. The product should occupy 30%-45% of the image and have a clear relationship to the use action or space. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed accessories, users, environments, outputs, or product effects.

Information hierarchy: use result or scenario benefit first, product-scene relationship second, small icon explanations third. Use {headline}, {subheadline}, {selling_points}, {scenes}, and {use_context} only for verified use-context messaging. Use {specs} and {accessories} only when relevant and confirmed. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to select or frame a relevant verified scene, not to invent demographics, professions, authority, or special conditions. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, rounded scene cards, small labels, and a clean bottom scene strip. Select home, office, outdoor, travel, or professional settings only when appropriate for {product_category} and supported by {scenes} or {use_context}. Keep scenes generalized and credible. Treat reference images as style references only.

Keep the product visually true and recognizable in the scene. Do not exaggerate results, show impossible use, or imply guaranteed outcomes. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, regulatory claims, or unrealistic lifestyle outcomes.
```

## style1_selling_3.png

### Universal Generation Index

- Image type: Pain-point or selling-point image / Selling.
- Variant positioning: protection feeling and reliability.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: place the product within a protective light effect or shield metaphor, with icon selling points above.
- Information hierarchy: user pain point or benefit headline first, product solution second, icon selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: abstract risk environment, without writing unconfirmed protection ratings.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: begin with a generalized use pain point, then use verified selling points to explain how the product addresses it.
- Product placement form: keep the product clear in the foreground, with environmental elements never covering it.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Pain-point or selling-point image. Target filename token: Selling. Use the blue and white technical specification style.

Place the product inside a protective light effect or shield metaphor, with icon selling points above. Keep the product clear in the foreground and do not let environmental elements cover it. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed protective shells, ratings, layers, damage states, test scenes, or certification symbols.

Information hierarchy: user pain point or benefit headline first, product solution second, icon selling points third. Use {headline}, {subheadline}, and {selling_points} only for verified benefit messaging. Use {specs} only for confirmed protection, reliability, durability, or material facts. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to frame the risk or reassurance message for a verified audience or use context. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, rounded selling-point cards, shield-like abstract geometry, and clean benefit labels. Use an abstract risk environment selected from {scenes} and {use_context}, suitable for {product_category}. Do not write unconfirmed protection ratings or show unverified extreme conditions.

Effects may imply organization and care, but must not imply unverified waterproofing, drop resistance, fire resistance, medical protection, safety certification, or guaranteed protection. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, regulatory claims, or guaranteed protection outcomes.
```

## style1_feature_4.png

### Universal Generation Index

- Image type: Function or structure image / Feature.
- Variant positioning: fit or compatibility matrix.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: product in the center, surrounded by 6-8 generic confirmed fit or compatibility object cards.
- Information hierarchy: function headline first, real product structure or component second, callout explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: show only user-confirmed fit or compatibility objects, with generalized icons.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: support selling points with the product's real structure, real components, or verified working method. Do not invent internal structure.
- Product placement form: connect the product to fit or compatibility objects with blue connector lines.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Function or structure image. Target filename token: Feature. Use the blue and white technical specification style.

Place the product in the center, surrounded by 6-8 generic fit or compatibility object cards. Connect the product to fit or compatibility objects with clean blue connector lines. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed adapters, ports, accessories, devices, object categories, or compatibility marks.

Information hierarchy: function headline first, real fit or compatibility logic second, callout explanation third. Use {headline}, {subheadline}, {selling_points}, {specs}, and {accessories} only for confirmed compatibility, fit, structure, or use information. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to explain why the confirmed fit matters for a verified audience or use context. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, generic object icons, rounded compatibility cards, connector lines, and concise labels. Show only fit or compatibility objects confirmed by the user through {specs}, {accessories}, {scenes}, or {use_context}. Use generalized icons instead of platform logos, competitor products, brand names, official badges, or copyrighted device artwork.

Make the connector logic clear without implying unsupported compatibility or official approval. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, official support status, safety guarantees, medical claims, or regulatory claims.
```

## style1_lifestyle_2.png

### Universal Generation Index

- Image type: Scenario result image / Lifestyle.
- Variant positioning: multi-scene grid.
- Visual style: follow the blue and white technical specification style, but replace all products and scenes with generic product expression for the current `{product}`.
- Composition: 2x3 or 3x3 scene-card grid, with the product as the unified visual anchor.
- Information hierarchy: use result or scenario benefit first, relationship between product and scene second, small icon explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular line icons, numbered badges, magnifier labels, and generic device or scene icons.
- Scene expression: each card corresponds to one confirmed use scene.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards as appropriate for the image type. Keep all components aligned with consistent spacing.
- Effects rendering language: light blue gradients, soft shadows, blue-white rim lighting, localized highlights, and subtle technical linework.
- Selling-point logic: use realistic generalized scenes to show the product's use result without exaggerating effects.
- Product placement form: repeat the product in the main card or corners while preserving real proportions.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a generic product. Image type: Scenario result image. Target filename token: Lifestyle. Use the blue and white technical specification style.

Create a 2x3 or 3x3 grid of scene cards, with the product used as the unified visual anchor across the grid. Repeat the product in the main card or card corners while preserving real proportions and recognizable details. Preserve real product proportions, color, material, structure, ports, accessories, and edge details. Do not add unconfirmed accessories, users, environments, outputs, or product effects.

Information hierarchy: use result or scenario benefit first, product-scene relationship second, small icon explanations third. Use {headline}, {subheadline}, {selling_points}, {scenes}, and {use_context} only for verified scene messaging. Use {specs} and {accessories} only when relevant and confirmed. If {brand} is confirmed, place it subtly; otherwise omit it. Use {target_user} only to choose or frame confirmed scenes for a verified audience. All text must use {language}, stay short and readable, and avoid garbled characters.

Use blue circular line icons, numbered badges, rounded scene cards, scene labels, small benefit tags, and a consistent grid system. Each card must correspond to one confirmed use scene from {scenes} or {use_context}, suitable for {product_category}. Keep all scenes generalized and credible. Treat reference images as style references only.

Maintain product authenticity across repeated appearances. Do not exaggerate results, show impossible use, imply guaranteed outcomes, or invent lifestyle benefits. Do not invent numbers, certifications, compatibility, materials, efficacy, official endorsements, absolute promises, competitor defects, platform marks, safety guarantees, medical claims, regulatory claims, or unrealistic lifestyle outcomes.
```
