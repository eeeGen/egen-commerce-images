<!-- English adaptation generated for ecommerce-product-images. Preserve variables and filename tokens. -->

# style2 Universal Product Generation Index and GPT Image 2 Prompts

Positioning: warm-light immersive scenes plus dynamic green infographic styling. This file applies to any general product and is not bound to the original category of any reference image. During generation, inherit only the visual style, composition logic, information hierarchy, UI component language, scene expression, and selling-point logic.

## Mandatory Universal Product Rules

- `{product}` must come from the product image uploaded by the user or explicitly confirmed by the user in the current task. It is the only source of truth for product appearance.
- Do not copy the product, brand, structure, accessories, parameters, people, scene facts, certifications, or copywriting from any reference image.
- Replace all category-specific content with variables: `{product_category}`, `{use_context}`, `{target_user}`, `{selling_points}`, `{specs}`, `{accessories}`, `{scenes}`, `{language}`.
- If the current product does not fit an original reference scene, abstract the reference into equivalent visual logic, such as a dark atmospheric scene, a coverage visualization, or a fresh lifestyle scene. Do not reuse the original product scene as factual content.
- Any numbers, certifications, compatibility targets, comparison conclusions, materials, performance effects, accessory counts, or package contents must come from user-provided information. If the information is missing, use neutral placeholder wording instead of inventing specifics.
- On-image text must be short, readable, and adapted to `{language}`. Do not include garbled text, platform logos, competitor brands, official endorsements, certification marks, or absolute promises.

## Style DNA

- Visual style: deep immersive backgrounds, warm yellow product lighting, dynamic green information bars, and strong scene mood. Suitable for building atmosphere, event energy, outdoor energy, display value, usage emotion, or a strong result impression for any product.
- Design logic: scene images use a clear product foreground and environmental depth; infographic images use green base bars, angled sections, step cards, and icon badges.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark backgrounds, light bokeh, green motion bars, and product rim highlights.
- Product placement principle: choose front view, three-quarter view, angled view, flat lay, floating display, in-scene use, or detail close-up according to the real form of `{product}`. Do not change product proportions, color, material, ports, accessories, or structure.

## Prompt Variables

- `{product}`: any user-confirmed product.
- `{product_category}`: the product category, used to select copy and scenes, not to alter appearance.
- `{brand}`: the user-provided brand; omit it if unavailable.
- `{headline}` / `{subheadline}`: the headline and subheadline for this image.
- `{selling_points}`: verified selling points.
- `{specs}`: verified specifications.
- `{accessories}`: verified accessories.
- `{scenes}` / `{use_context}`: realistic generalized scenes suitable for this product.
- `{language}`: the target country or platform language.

## style2_hero.png

### Universal Generation Index

- Image type: Hero image / Hero.
- Variant positioning: dark atmospheric Hero.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: place the headline and 3 selling points on the left; place the glowing or highlighted product on the right or in the foreground.
- Information hierarchy: product subject first, main headline second, 3-6 core selling points third, bottom specifications or scene support fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: choose the emotional scene most relevant to the product, such as home use, outdoor use, event use, workspace use, or display-space use.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: establish product recognition, core value, and reasons to buy in one screen. Avoid stacking unverified specifications.
- Product placement form: the product occupies 35%-50% of the image. Lighting effects must be reasonable for the product material and function.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Hero image. Target filename token: Hero. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling: a deep immersive background, warm yellow product lighting, dynamic green information bars, and strong scene mood.

Composition: place the headline and exactly 3 concise selling points on the left. Place the product on the right or in the foreground as the main glowing or highlighted subject. The product should occupy 35%-50% of the canvas. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts or alter the product identity.

Information hierarchy: product subject first, {headline} second, {subheadline} and 3-6 verified selling points third, bottom specifications or scene support fourth. Use selling points only from {selling_points}, specifications only from {specs}, and accessories only from {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons. Add rounded cards, labels, icon strips, data panels, comparison tables, step cards, specification tags, or scene thumbnails only where they support this Hero image. Maintain consistent margins, alignment, and whitespace. Text and UI elements must not overlap the product.

Scene expression: choose the most relevant emotional scene from {scenes} and {use_context}, adapted to {product_category}. Use a generalized home, outdoor, event, workspace, or display-space environment when appropriate. Keep reference images isolated: inherit only style, composition, and information logic; do not reuse the original product scene or original factual content.

Rendering: use warm yellow volumetric light, environmental reflections, dark background depth, light bokeh, green motion bars, and product rim highlights. Lighting, reflections, beams, shadows, and highlights must improve product recognition and selling-point clarity without implying unverified functions.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. If data is missing, use neutral generic wording. The final image should look like a production-grade ecommerce detail image ready for use.
```

## style2_specs.png

### Universal Generation Index

- Image type: Size/specification image / Specs.
- Variant positioning: proportion and dimension diagram.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: show a front-view product on a white or light neutral background, with clear dimension lines and proportional reference elements.
- Information hierarchy: size or specification title first, front-view or flat-lay product second, rulers and parameters third, package list fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: avoid relying on a human figure. Use generalized scale references such as room space, desktop scale, wall scale, handheld scale, or storage scale.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: use restrained warm highlights and green infographic accents. For Specs, prioritize measurement clarity over dark scene mood, heavy lighting, or atmospheric effects.
- Selling-point logic: reduce size misunderstanding before purchase. Show only user-confirmed numbers and package-list items.
- Product placement form: center the product in a front view, occupying 40%-55% of the image.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Size/specification image. Target filename token: Specs. Apply the style DNA through clean green infographic accents and subtle warm highlights, but prioritize measurement readability over immersive dark scenery.

Composition: use a white or light neutral background. Place the product centered in a front view or accurate flat lay, occupying 40%-55% of the canvas. Add clean dimension lines, ruler marks, scale indicators, and optional proportional reference elements. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: size or specification title first, product view second, dimension lines and verified parameters third, package list fourth. Use {headline}, {subheadline}, specifications from {specs}, accessories from {accessories}, and only relevant selling points from {selling_points}. If exact dimensions or package contents are not provided, use neutral placeholders without numbers.

Layout and UI: use green and gold linear icons, numbered badges, specification tags, data panels, and clean callout labels. Keep all measurement labels readable in {language}. Maintain clear margins around all dimension lines and product edges. Text must not overlap the product, rulers, or package list.

Scene expression: use generalized scale contexts from {scenes} and {use_context}, adapted to {product_category}, such as room space, desktop scale, wall scale, handheld scale, or storage scale. Do not force a lifestyle scene, human figure, dramatic environment, or dark atmospheric background if it conflicts with specification clarity.

Rendering: keep shadows natural, edges sharp, and product geometry accurate. Use subtle warm highlights and green UI accents only to support readability. Do not create fake internal structures, fictional measurements, or exaggerated scale relationships.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. Keep reference images isolated and do not copy their original product facts. The final image should read as a precise production-grade ecommerce specification graphic.
```

## style2_guide.png

### Universal Generation Index

- Image type: Product usage guide / Guide.
- Variant positioning: quick three-step process.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: top headline, three step cards in the middle, connecting arrows, and bottom notes.
- Information hierarchy: step title first, numbered process second, product action third, notes or accessories fourth.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: white and green infographic background, focused on process clarity.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: use clean green infographic accents and restrained warm highlights. For Guide, process clarity must override dramatic scene effects.
- Selling-point logic: lower the usage barrier with verified steps. Do not invent installation or operation procedures.
- Product placement form: each step shows a real use or handling state without inventing actions.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Product usage guide. Target filename token: Guide. Apply the style DNA through clean green process cards, warm product highlights, and a professional infographic layout.

Composition: place {headline} at the top, three numbered step cards in the middle, directional arrows between steps, and concise notes at the bottom. Each step must show a verified real operation state, setup state, handling state, or accessory relationship for the product. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: step title first, numbered process second, product action third, notes or accessories fourth. Use {subheadline}, verified actions from {selling_points} and {use_context}, specifications from {specs} only when relevant, and accessories from {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, numbered badges, arrows, step cards, accessory icons, and note labels. Keep consistent margins and alignment. Text, arrows, and callouts must not overlap the product views.

Scene expression: use a white and green infographic background focused on process clarity. Select context only from {scenes} and {use_context}, adapted to {product_category}. Do not force an immersive scene if it makes the steps unclear.

Rendering: use restrained warm highlights, clean shadows, crisp product edges, and green UI accents. Do not create fictional installation parts, hidden mechanisms, unsupported hand actions, or unverified operation flows.

Compliance: do not invent steps, numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. Keep reference images isolated and do not copy their original product facts. The final image should read as a production-grade ecommerce usage guide.
```

## style2_lifestyle.png

### Universal Generation Index

- Image type: Lifestyle/result image / Lifestyle.
- Variant positioning: dual-scene applicability.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: left-right split screen or angled split screen comparing two use environments.
- Information hierarchy: use result or scene benefit first, product-scene relationship second, small icon explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: adapt to the product with indoor/outdoor, everyday/professional, day/night, individual/group, or similar generalized contrasts.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: show realistic generalized use results created by the product without exaggerating effects.
- Product placement form: the product appears on both sides with consistent appearance.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Lifestyle/result image. Target filename token: Lifestyle. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: create a left-right split screen or angled split screen comparing two realistic use environments. Show the same product on both sides with consistent appearance and scale logic. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: use result or scene benefit first, product-scene relationship second, small icon explanation third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, scene labels, small data panels, and concise benefit tags. Keep component spacing consistent and do not let text, icons, or split-screen dividers cover the product.

Scene expression: select two generalized scenes from {scenes} and {use_context}, adapted to {product_category}. Valid contrast patterns include indoor versus outdoor, everyday versus professional, day versus night, individual versus group, or fixed versus mobile use. Keep reference images isolated and do not reuse their original product scene as factual content.

Rendering: use warm yellow product highlights, environmental reflections, believable shadows, dark or semi-dark atmospheric depth where appropriate, light bokeh, green motion bars, and product rim highlights. Effects must support realistic use context and must not imply unverified performance.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. The final image should read as a production-grade ecommerce lifestyle comparison image.
```

## style2_selling.png

### Universal Generation Index

- Image type: Pain-point/selling-point image / Selling.
- Variant positioning: environmental adaptability and multi-condition selling points.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: 2x2 scene grid or multi-environment cards, with a green selling-point bar at the bottom.
- Information hierarchy: user pain point or benefit headline first, product solution second, icon-based selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: use generalized environments to express usage stability, without claiming unverified certifications.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: first state a generalized user pain point, then use verified selling points to show how the product addresses it.
- Product placement form: the product is clearly identifiable in every grid cell.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Pain-point/selling-point image. Target filename token: Selling. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: build a 2x2 scene grid or a set of multi-environment cards. Add a green selling-point bar at the bottom. The product must be clearly identifiable in every card or grid cell, with consistent proportions and appearance. Preserve the real product color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: user pain point or benefit headline first, product solution second, icon-based verified selling points third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, environment labels, numbered badges, shield icons only as generic visual metaphors, and concise bottom-bar copy. Keep all cards aligned with consistent margins. Text and icons must not obscure product identity.

Scene expression: choose generalized environments from {scenes} and {use_context}, adapted to {product_category}. Show stable use across relevant everyday conditions, but do not imply waterproofing, certification, safety approval, durability rating, compatibility, or guaranteed performance unless provided by the user.

Rendering: use warm highlights, environmental reflections, believable shadows, controlled dark mood, light bokeh, green motion bars, and product rim highlights. Effects must support the verified benefit without creating fake functions.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. Keep reference images isolated and do not copy their original product facts. The final image should read as a production-grade ecommerce selling-point graphic.
```

## style2_feature.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: internal or key-function lighting.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: enlarged centered product, with dark explanation cards and callouts on both sides.
- Information hierarchy: feature title first, verified product structure or components second, callout explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: dark abstract background that reinforces the feature focus.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: support selling points with the product's real structure, real components, or verified way of working. Do not invent internal structure.
- Product placement form: show only verified structures or external feature points.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Feature/structure image. Target filename token: Feature. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling, with a dark abstract technical background.

Composition: place an enlarged product in the center. Add dark explanation cards and clean callout lines on both sides, pointing only to visible, verified product structures, components, controls, materials, ports, accessories, or external feature areas. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: feature title first, verified product structure or component second, callout explanations third. Use {headline}, {subheadline}, selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, numbered badges, callout tags, data panels, and concise feature labels. Keep all callout lines accurate and connected to visible product areas. Text and cards must not overlap important product details.

Scene expression: use a dark abstract background to focus attention on the product. Do not use a lifestyle environment if it conflicts with feature clarity. Keep reference images isolated and inherit only style, composition logic, and information structure.

Rendering: use warm yellow volumetric light, product rim highlights, subtle environmental reflections, controlled shadows, green motion bars, and clean technical accents. Do not create transparent cutaways, internal mechanisms, exploded views, or functional effects unless they are verified by the user.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. The final image should read as a production-grade ecommerce feature explanation graphic.
```

## style2_feature_2.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: accessory or system explanation.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: main product plus a bottom matrix of verified accessories and side explanation cards.
- Information hierarchy: feature title first, verified product structure or components second, callout explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: light-background infographic with minimal distraction.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: use clean green infographic accents and restrained warm highlights. For accessory/system explanation, clarity and truthfulness override atmosphere.
- Selling-point logic: support selling points with the product's real structure, real components, or verified way of working. Do not invent internal structure.
- Product placement form: accessory quantity and form must come from user confirmation.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Feature/structure image. Target filename token: Feature. Apply the style DNA through green infographic accents, warm product highlights, and a clean system-explanation layout.

Composition: show the main product as the primary subject. Add a bottom matrix of verified accessories from {accessories} and side explanation cards for confirmed system relationships, components, or external features. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: feature title first, verified product structure or components second, accessory or system callouts third. Use {headline}, {subheadline}, selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. If accessory quantity, shape, or package content is not provided, use neutral placeholders and do not draw specific extra items.

Layout and UI: use green and gold linear icons, accessory icons, numbered badges, side labels, and a clean bottom accessory matrix. Keep consistent spacing and alignment. Text, labels, and matrix cells must not cover the product or imply unverified contents.

Scene expression: use a light-background infographic with minimal distraction. Select any supporting context only from {scenes} and {use_context}, adapted to {product_category}. Do not force a lifestyle scene or dramatic dark background if it conflicts with system clarity.

Rendering: use restrained warm highlights, crisp product edges, clean shadows, and green UI accents. Do not create fictional accessories, internal structures, exploded views, compatibility diagrams, or system relationships unless verified by the user.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. Keep reference images isolated and do not copy their original product facts. The final image should read as a production-grade ecommerce accessory or system explanation graphic.
```

## style2_feature_3.png

### Universal Generation Index

- Image type: Feature/structure image / Feature.
- Variant positioning: stability, support, or fixing logic.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: centered product, with arrows pointing to support points, base areas, or key structures.
- Information hierarchy: feature title first, verified product structure or components second, callout explanations third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: generalize the use environment into floor, desktop, wall, outdoor, or workspace context.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: use focused product highlights, clear arrows, and green infographic accents. Avoid visual drama that conflicts with structural clarity.
- Selling-point logic: support selling points with the product's real structure, real components, or verified way of working. Do not invent internal structure.
- Product placement form: standing, placed, or installed position must be realistic for the product.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Feature/structure image. Target filename token: Feature. Apply the style DNA through warm product highlights, green infographic callouts, and a clear structural explanation layout.

Composition: center the product in a realistic standing, placed, mounted, or installed position suitable for {product_category}. Use arrows to point only to verified support points, base areas, fixing points, contact areas, controls, ports, or other visible key structures. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: feature title first, verified product structure or components second, callout explanations third. Use {headline}, {subheadline}, selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, arrows, callout cards, specification tags, and concise feature labels. Keep arrows precise and labels readable. Text and callouts must not cover key product structure.

Scene expression: generalize the environment from {scenes} and {use_context}, adapted to {product_category}, such as floor, desktop, wall, outdoor, or workspace context. Do not use a scene that contradicts the product's real placement or use.

Rendering: use focused warm highlights, realistic shadows, accurate contact points, green UI accents, and crisp product edges. Do not create fake stability mechanisms, hidden structures, exaggerated load-bearing effects, or unverified fixing hardware.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. Keep reference images isolated and do not copy their original product facts. The final image should read as a production-grade ecommerce structural feature graphic.
```

## style2_corea.png

### Universal Generation Index

- Image type: Core value scene image A / CoreA.
- Variant positioning: first core emotional scene.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: product in the foreground, high-value use space in the background, and minimal text.
- Information hierarchy: first core use scene first, real product participation second, limited selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: choose the most typical use scene for the product; generalize all people and environments.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: show the most typical and important reason to buy, with the scene automatically adapted to the product category.
- Product placement form: the product occupies 25%-45% of the image and acts as the scene light source or visual focus.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Core value scene image A. Target filename token: CoreA. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: place the product in the foreground with a high-value use space in the background. Use minimal text. The product should occupy 25%-45% of the canvas and serve as the visual focus or a plausible scene light source only when that is believable for the product. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: first core use scene first, real product participation second, limited verified selling points third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use a restrained number of green and gold linear icons, small labels, or concise benefit tags. Keep the product dominant and avoid dense infographic clutter. Text must not overlap the product or important scene elements.

Scene expression: choose the most typical high-value use scene from {scenes} and {use_context}, adapted to {product_category}. Generalize people, environment, props, and actions. Keep reference images isolated and do not reuse their original product scene or factual content.

Rendering: use warm yellow volumetric light, environmental reflections, dark background depth where appropriate, light bokeh, green motion accents, and product rim highlights. Effects must support product recognition and verified value without implying unverified performance.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. The final image should read as a production-grade ecommerce core-value scene.
```

## style2_closing.png

### Universal Generation Index

- Image type: A+ closing image / Closing.
- Variant positioning: multi-scene collage closing image.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: 1 large main scene plus 3 small scenes, with a core selling-point bar at the bottom.
- Information hierarchy: closing headline first, multi-scene or multi-selling-point summary second, bottom core reason third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: summarize multiple use spaces or target user groups for the product.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: compress the image set's information into final reasons to buy, creating a complete brand feeling and a clear closing message.
- Product placement form: the product is identifiable in every scene.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: A+ closing image. Target filename token: Closing. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: create 1 large main scene plus 3 smaller supporting scenes. Add a core selling-point bar at the bottom. The product must be identifiable in every scene, with consistent appearance and no invented variants. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: closing headline first, multi-scene or multi-selling-point summary second, bottom core reason third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use green and gold linear icons, scene labels, compact benefit tags, a bottom selling-point bar, and clean collage framing. Keep consistent margins and alignment. Text and UI elements must not cover the product.

Scene expression: summarize multiple use spaces or target user groups from {scenes} and {use_context}, adapted to {product_category}. Keep each scene generalized and factual. Do not reuse reference-image scene facts, people, brands, or product-specific content.

Rendering: use warm yellow product highlights, environmental reflections, coherent shadows across scenes, dark or semi-dark depth where appropriate, light bokeh, green motion bars, and product rim highlights. Effects must unify the collage without implying unverified product results.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. The final image should read as a production-grade ecommerce A+ closing graphic.
```

## style2_corea_2.png

### Universal Generation Index

- Image type: Core value scene image A / CoreA.
- Variant positioning: first core scene variant.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: a more lifestyle-oriented or closer core scene, with a clear relationship between product and user action.
- Information hierarchy: first core use scene first, real product participation second, limited selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: use the same reason to buy as CoreA, but switch to another space or camera distance.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: show the most typical and important reason to buy, with the scene automatically adapted to the product category.
- Product placement form: the product appears in the foreground or middle ground with realistic proportions.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Core value scene image A. Target filename token: CoreA. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: create a more lifestyle-oriented or closer version of the CoreA scene. Show a clear, realistic relationship between the product and the user's action or environment. Place the product in the foreground or middle ground with realistic proportions. Preserve the real product color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: first core use scene first, real product participation second, limited verified selling points third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use minimal green and gold linear icons, small labels, or concise benefit tags. Keep the scene natural and product-focused. Text must not overlap the product, hands, interaction area, or important scene details.

Scene expression: use the same purchase reason as CoreA, but shift to another space, camera distance, or more intimate use moment selected from {scenes} and {use_context}. Adapt it to {product_category}. Generalize people, environment, props, and actions. Keep reference images isolated and do not copy their original scene facts.

Rendering: use warm yellow product highlights, environmental reflections, believable shadows, dark or semi-dark depth where appropriate, light bokeh, green motion accents, and product rim highlights. Effects must support realistic product participation without implying unverified performance.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. The final image should read as a production-grade ecommerce core-value scene variant.
```

## style2_coreb.png

### Universal Generation Index

- Image type: Core value scene image B / CoreB.
- Variant positioning: second core scene.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: a user group, space, or use result that is clearly different from CoreA.
- Information hierarchy: second core use scene first, differentiated user group, space, or result second, limited selling points third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: choose a second high-value scene, such as outdoor use, group use, professional use, display use, storage use, or mobile use.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: create a clear difference from CoreA in scene and user group, showing another high-value use path.
- Product placement form: the product is the scene focus and must not be overpowered by the background.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Core value scene image B. Target filename token: CoreB. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: create a user group, space, or use result that is clearly different from CoreA. Keep the product as the scene focus so the background does not overpower it. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish.

Information hierarchy: second core use scene first, differentiated user group, space, or result second, limited verified selling points third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use minimal green and gold linear icons, small labels, concise benefit tags, or light callouts. Keep the scene readable and product-centered. Text must not overlap the product or important scene elements.

Scene expression: select a second high-value scene from {scenes} and {use_context}, adapted to {product_category}. Options may include outdoor use, group use, professional use, display use, storage use, or mobile use when they fit the product. Generalize people, environment, props, and actions. Keep reference images isolated and do not copy their original scene facts.

Rendering: use warm yellow volumetric light, environmental reflections, believable shadows, dark or semi-dark background depth where appropriate, light bokeh, green motion accents, and product rim highlights. Effects must support a distinct verified use path without implying unverified performance.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. The final image should read as a production-grade ecommerce second core-value scene.
```

## style2_lifestyle_2.png

### Universal Generation Index

- Image type: Lifestyle/result image / Lifestyle.
- Variant positioning: everyday use result.
- Visual style: use the warm-light immersive scene plus dynamic green infographic style, while replacing every product and scene with a generalized expression of the current `{product}`.
- Composition: realistic photographic main scene plus minimal text and small icons.
- Information hierarchy: use result or scene benefit first, product-scene relationship second, small icon explanation third.
- Layout: headline, product, selling points, specifications, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: green and gold linear icons, numbered badges, shield icons, environment icons, step icons, and accessory icons.
- Scene expression: everyday, relaxed, and credible. Do not use third-party IP or private information.
- UI component design: use rounded cards, labels, icon strips, data panels, comparison tables, or step cards according to this image type. Keep all components consistently spaced and aligned.
- Effects rendering language: warm yellow volumetric light, environmental reflections, dark background, light bokeh, green motion bars, and product rim highlights.
- Selling-point logic: show realistic generalized use results created by the product without exaggerating effects.
- Product placement form: the product appears in a natural use position.
- Compliance boundary: do not state unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### Production-Ready GPT Image 2 Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: Lifestyle/result image. Target filename token: Lifestyle. Apply the style DNA of warm-light immersive scenes plus dynamic green infographic styling.

Composition: create a realistic photographic main scene with minimal text and small icons. Place the product in a natural use position that fits {product_category}. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: use result or scene benefit first, product-scene relationship second, small icon explanation third. Use {headline}, {subheadline}, selling points from {selling_points}, and only relevant specifications or accessories from {specs} and {accessories}. All on-image text must use {language}, short readable phrases, clean typography, and no garbled characters.

Layout and UI: use a restrained set of green and gold linear icons, small labels, or concise benefit tags. Maintain clean spacing and a credible lifestyle look. Text and icons must not overlap the product or the main action area.

Scene expression: choose an everyday, relaxed, and credible scene from {scenes} and {use_context}, adapted to {product_category}. Do not use third-party IP, private information, platform UI, competitor marks, or branded props unless supplied by the user and allowed for the image.

Rendering: use warm product highlights, environmental reflections, believable shadows, natural photographic depth, optional dark or semi-dark ambience where appropriate, light bokeh, green motion accents, and product rim highlights. Effects must support realistic use context and must not exaggerate results.

Compliance: do not invent numbers, certifications, compatibility claims, performance results, materials, accessories, official endorsements, absolute promises, competitor weaknesses, platform marks, certification logos, or brand claims. Keep reference images isolated and do not copy their original product facts. The final image should read as a production-grade ecommerce everyday lifestyle image.
```
