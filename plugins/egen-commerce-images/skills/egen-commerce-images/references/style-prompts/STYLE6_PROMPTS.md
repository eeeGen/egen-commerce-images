# style6 Universal Product Generation Index and Prompts

Positioning: blue-and-gold high-density scene-evidence style. This file applies to any general product and is not bound to the original category of the reference images. During generation, inherit only the visual style, composition, information hierarchy, UI components, scene expression, and selling-point logic.

## Mandatory Universal Product Rules

- `{product}` must come from the product image uploaded or explicitly confirmed by the user in the current chat, and is the only source of truth for product appearance.
- Do not copy the products, brands, structures, accessories, parameters, people, scene facts, certifications, or copywriting from reference images.
- Replace all category-specific content with variables: `{product_category}`, `{use_context}`, `{target_user}`, `{selling_points}`, `{specs}`, `{accessories}`, `{scenes}`, `{language}`.
- If the product does not fit an original reference scene, abstract that scene into equivalent visual logic, such as a high-value use scenario, multi-angle result preview, kit accessory matrix, or blue-and-gold comparison table, instead of reusing the original product scene.
- Any numbers, certifications, compatibility targets, comparison conclusions, materials, effects, or accessory quantities must come from user-provided data. If data is missing, use neutral placeholder wording.
- On-image text must be short, readable, and adapted to `{language}`. No gibberish, platform logos, competitor brands, official endorsements, or absolute claims.

## Style DNA

- Main palette: deep navy, bright blue, white/light gray, and black, with limited yellow/gold accents for title bars, emphasis words, checkmarks, and key borders.
- Visual style: blue-and-gold high-density scene-evidence style, combining realistic scene photography with professional infographics to emphasize complete configuration, clear proof, usage results, reasons to choose, and trustworthy purchase decisions.
- Design logic: use a large headline and realistic scene in the upper half to establish value; use deep-blue information bars, icon strips, preview frames, accessory matrices, dimension cards, or comparison tables in the lower half to explain facts clearly.
- Icon system: blue circular or square linear icons, yellow emphasis badges, deep-blue parameter bars, check/cross tables, preview frames, callout labels, and accessory list cards.
- Effects rendering language: blue technology light beams, deep-blue gradient bottom bars, glass highlights, clean product shadows, yellow accent lines, realistic natural light, or cool professional scene lighting.
- Product placement principle: choose front view, 3/4 angle, angled view, flat lay, floating view, in-scene use, or detail close-up according to the real form of `{product}`. Do not change product proportions, color, material, ports, accessories, or structure.

## Prompt Variables

- `{product}`: any user-confirmed product.
- `{product_category}`: the product category, used to select copy and scenes, not to alter appearance.
- `{brand}`: the user-provided brand; omit it if unavailable.
- `{headline}` / `{subheadline}`: the main headline and subheadline for this image.
- `{selling_points}`: verified selling points.
- `{specs}`: verified specifications.
- `{accessories}`: verified accessories.
- `{scenes}` / `{use_context}`: realistic generalized scenes suitable for this product.
- `{language}`: the target country/platform language.

## style6-02-selling.png

### Universal Generation Index

- Image type: Pain Point / Selling Point Image / Selling.
- Variant positioning: all-scenario confidence selling points plus multiple result previews.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: oversized headline in the upper left, realistic lifestyle/use scene on the right, large product in the foreground, 2-3 result preview frames in the lower right, and a deep-blue parameter icon strip at the bottom.
- Information hierarchy: user pain point or benefit headline first, product solution second, result previews and icon selling points third, bottom parameters fourth.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: blue circular icons, deep-blue parameter bar, preview frames, and shield/person/group/scene/function icons.
- Scene expression: choose a realistic generalized scene that best communicates confidence, efficiency, convenience, or visible results in use.
- UI component design: rounded preview frames, deep-blue pill subheadline, icon selling-point group, and bottom parameter bar, with consistent spacing and alignment across all components.
- Effects rendering language: blue light beams, pale mist transitions, deep-blue bottom bar, product highlights, and realistic natural scene lighting.
- Selling-point logic: first state the general use benefit, then use verified selling points and visualized results to show how the product solves the need.
- Product placement form: the product occupies 35%-50% of the foreground; scenes and preview frames must not obstruct the main product.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Pain Point / Selling Point Image"; target filename token: Selling. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: oversized headline in the upper left, realistic lifestyle/use scene on the right, large product in the foreground, 2-3 result preview frames in the lower right, and a deep-blue parameter icon strip at the bottom. Product placement: the product should occupy 35%-50% of the foreground; scenes and preview frames must not obstruct the main product. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: user pain point or benefit headline first, product solution second, result previews and icon selling points third, bottom parameters fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use blue circular icons, a deep-blue parameter bar, preview frames, and shield/person/group/scene/function icons. Add rounded preview frames, a deep-blue pill subheadline, an icon selling-point group, bottom parameter bar, spec labels, or scene thumbnails as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: choose a realistic generalized scene that best communicates confidence, efficiency, convenience, or visible results in use. The scene must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: blue light beams, pale mist transitions, deep-blue bottom bar, product highlights, and realistic natural scene lighting. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point communication, not imply unverified functions.

Selling-point logic: first state the general use benefit, then use verified selling points and visualized results to show how the product solves the need. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-03-corea.png

### Universal Generation Index

- Image type: Core Value Scene Image A / CoreA.
- Variant positioning: dark immersive performance scene.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: dark high-value use scene on the right side or in the background, enlarged angled product in the foreground, large headline and vertical icon selling points on the left, and a specification bar at the bottom.
- Information hierarchy: primary core use scenario first, real product participation method second, limited selling points third.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: blue glowing linear icons, performance/speed/stability/compatibility icons, and dark parameter capsules at the bottom.
- Scene expression: choose the product's most typical high-intensity, professional, entertainment, work, or display scenario.
- UI component design: left-side vertical icon column, specification badges, and bottom parameter bar, using cool-blue strokes and translucent dark backgrounds.
- Effects rendering language: deep-blue ambient light, cool rim light, speed light trails, screen/panel glow, and metallic or material highlights.
- Selling-point logic: show the most typical and important reason to buy, with the scene automatically replaced according to the product category.
- Product placement form: the product occupies 25%-45%, sits close to the camera, and presents its key functional face toward the viewer.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Core Value Scene Image A"; target filename token: CoreA. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: dark high-value use scene on the right side or in the background, enlarged angled product in the foreground, large headline and vertical icon selling points on the left, and a specification bar at the bottom. Product placement: the product should occupy 25%-45%, sit close to the camera, and present its key functional face toward the viewer. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: primary core use scenario first, real product participation method second, limited selling points third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use blue glowing linear icons, performance/speed/stability/compatibility icons, and dark parameter capsules at the bottom. Add a left-side vertical icon column, specification badges, bottom parameter bar, translucent dark cards, or scene result markers as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: choose the product's most typical high-intensity, professional, entertainment, work, or display scenario. The scene must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: deep-blue ambient light, cool rim light, speed light trails, screen/panel glow, and metallic or material highlights. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point communication, not imply unverified functions.

Selling-point logic: show the most typical and important reason to buy, with the scene automatically replaced according to the product category. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-04-coreb.png

### Universal Generation Index

- Image type: Core Value Scene Image B / CoreB.
- Variant positioning: safety/protection/status-alert scene.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: light realistic scene background, large headline in the upper left, product on the right side or foreground, lock/shield/status-alert visual symbols, and a two-layer selling-point and parameter bar at the bottom.
- Information hierarchy: secondary core use scenario first, differentiated user group/space/result second, limited selling points third.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: blue glowing square icons, lock/shield/confidence/status icons, and a deep-blue bottom parameter bar.
- Scene expression: choose a second high-value scenario, such as storage, mobility, protection, monitoring, backup use, complex environments, or unattended status.
- UI component design: glowing icon cards, small result previews, bottom icon selling-point strip, and deep-blue gradient parameter band.
- Effects rendering language: blue protective light effects, translucent status ripples, cool-blue rim light, light-gray scene mist, and deep-blue bottom gradient.
- Selling-point logic: create clear separation from CoreA in scenario and user group, showing another high-value usage path.
- Product placement form: the product occupies 30%-45% and connects visually to protection, status, or result symbols without being obstructed.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Core Value Scene Image B"; target filename token: CoreB. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: light realistic scene background, large headline in the upper left, product on the right side or foreground, lock/shield/status-alert visual symbols, and a two-layer selling-point and parameter bar at the bottom. Product placement: the product should occupy 30%-45% and connect visually to protection, status, or result symbols without being obstructed. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: secondary core use scenario first, differentiated user group/space/result second, limited selling points third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use blue glowing square icons, lock/shield/confidence/status icons, and a deep-blue bottom parameter bar. Add glowing icon cards, small result previews, a bottom icon selling-point strip, and a deep-blue gradient parameter band as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: choose a second high-value scenario, such as storage, mobility, protection, monitoring, backup use, complex environments, or unattended status. The scene must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: blue protective light effects, translucent status ripples, cool-blue rim light, light-gray scene mist, and deep-blue bottom gradient. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point communication, not imply unverified functions.

Selling-point logic: create clear separation from CoreA in scenario and user group, showing another high-value usage path. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-05-feature.png

### Universal Generation Index

- Image type: Feature / Structure Image / Feature.
- Variant positioning: structural breakdown plus key component explanation.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: white technical page, large headline and 3 icon selling points on the left, large angled product display in the center, callout labels around the product, and bottom accessory/component plus scene explanation cards.
- Information hierarchy: feature headline first, real product structure/components second, callout explanations third, supporting scene/accessories fourth.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: deep-blue hexagonal or circular icons, blue callout point lines, yellow title bar, and deep-blue information cards.
- Scene expression: prioritize structural explanation; a small realistic use scene or detail close-up may be added at the bottom.
- UI component design: component labels, enlarged circular close-up frames, accessory flat-lay cards, deep-blue explanation panels, and yellow key phrases.
- Effects rendering language: white-gray technical background, clean shadow, blue local halo, yellow short divider lines, and realistic product material highlights.
- Selling-point logic: support selling points with the product's real structure, visible components, or working method. Do not invent internal structures.
- Product placement form: the product or key section occupies 45%-60%; callouts must attach to real visible components.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Feature / Structure Image"; target filename token: Feature. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: white technical page, large headline and 3 icon selling points on the left, large angled product display in the center, callout labels around the product, and bottom accessory/component plus scene explanation cards. Product placement: the product or key section should occupy 45%-60%; callouts must attach to real visible components. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: feature headline first, real product structure/components second, callout explanations third, supporting scene/accessories fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use deep-blue hexagonal or circular icons, blue callout point lines, yellow title bar, and deep-blue information cards. Add component labels, enlarged circular close-up frames, accessory flat-lay cards, deep-blue explanation panels, and yellow key phrases as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: prioritize structural explanation; a small realistic use scene or detail close-up may be added at the bottom. Any scene must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: white-gray technical background, clean shadow, blue local halo, yellow short divider lines, and realistic product material highlights. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point communication, not imply unverified functions.

Selling-point logic: support selling points with the product's real structure, visible components, or working method. Do not invent internal structures. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-06-specs.png

### Universal Generation Index

- Image type: Size / Specification Image / Specs.
- Variant positioning: dimensions, details, and packing list.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: white specification page, large main product image in the center with multiple dimension/component callouts, sub-product/accessory dimension cards on the sides or bottom, and a complete packing list plus icon parameter strip at the bottom.
- Information hierarchy: dimension/specification headline first, front-view or flat-lay product second, rulers and parameters third, packing list fourth.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: blue dimension lines, rounded white labels, deep-blue small title bars, and blue linear icons at the bottom.
- Scene expression: do not use complex scenes on the specification page; use only light-gray technical texture or a simple spatial reference.
- UI component design: dimension cards, accessory cards, packing list matrix, blue divider lines, and bottom icon strip.
- Effects rendering language: white-gray background, light-blue circular texture, clean product shadow, and deep-blue technical linework along the bottom edge.
- Selling-point logic: reduce pre-purchase size misunderstanding by showing only user-confirmed numbers and list items.
- Product placement form: the main product must be unobstructed; verified accessories should be grouped clearly; dimension points must align to real product boundaries.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Size / Specification Image"; target filename token: Specs. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: white specification page, large main product image in the center with multiple dimension/component callouts, sub-product/accessory dimension cards on the sides or bottom, and a complete packing list plus icon parameter strip at the bottom. Product placement: the main product must be unobstructed; verified accessories should be grouped clearly; dimension points must align to real product boundaries. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: dimension/specification headline first, front-view or flat-lay product second, rulers and parameters third, packing list fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use blue dimension lines, rounded white labels, deep-blue small title bars, and blue linear icons at the bottom. Add dimension cards, accessory cards, a packing list matrix, blue divider lines, and a bottom icon strip as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: do not use complex scenes on the specification page; use only light-gray technical texture or a simple spatial reference. If a spatial reference is needed, select it from {scenes} and {use_context}, fit it to the current {product_category}, and do not reuse the original product scene from the reference image.

Effects rendering: white-gray background, light-blue circular texture, clean product shadow, and deep-blue technical linework along the bottom edge. Lighting, reflections, beams, shadows, and local highlights must support product recognition and specification clarity, not imply unverified functions.

Selling-point logic: reduce pre-purchase size misunderstanding by showing only user-confirmed numbers and list items. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-07-value.png

### Universal Generation Index

- Image type: Differentiated Value Image / Value.
- Variant positioning: kit value plus multi-scenario applicability.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: large product and accessory combination on a white background occupying the right side/center, oversized headline and 4-6 circular icon selling points on the left, a wavy blue divider band across the lower middle, and multi-scenario cards plus a deep-blue parameter bar at the bottom.
- Information hierarchy: value headline first, value breakdown/data visualization second, product third, multi-scenario supplement fourth.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: blue circular icons, yellow parameter badges, circular scene icons, and deep-blue bottom parameter bar.
- Scene expression: use 4-5 confirmed use-scenario cards to show the coverage of product value.
- UI component design: kit/combination display, icon selling-point grid, blue wavy divider, scene thumbnails, and bottom yellow icon parameter strip.
- Effects rendering language: clean white-gray highlights, soft product shadow, blue divider band, and yellow emphasis capsules.
- Selling-point logic: convert differentiated value into readable combined benefits, multi-scenario uses, or factual explanations.
- Product placement form: product and verified accessories are shown completely, occupying 45%-60%; do not invent accessories.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Differentiated Value Image"; target filename token: Value. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: large product and accessory combination on a white background occupying the right side/center, oversized headline and 4-6 circular icon selling points on the left, a wavy blue divider band across the lower middle, and multi-scenario cards plus a deep-blue parameter bar at the bottom. Product placement: product and verified accessories should be shown completely and occupy 45%-60%; do not invent accessories. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: value headline first, value breakdown/data visualization second, product third, multi-scenario supplement fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use blue circular icons, yellow parameter badges, circular scene icons, and a deep-blue bottom parameter bar. Add kit/combination display, icon selling-point grid, blue wavy divider, scene thumbnails, and a bottom yellow icon parameter strip as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: use 4-5 confirmed use-scenario cards to show the coverage of product value. Scenes must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: clean white-gray highlights, soft product shadow, blue divider band, and yellow emphasis capsules. Lighting, reflections, beams, shadows, and local highlights must support product recognition and selling-point communication, not imply unverified functions.

Selling-point logic: convert differentiated value into readable combined benefits, multi-scenario uses, or factual explanations. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-08-compare.png

### Universal Generation Index

- Image type: Comparison Advantage Image / Compare.
- Variant positioning: complete solution vs basic solution.
- Visual style: follow the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: realistic professional use scene in the upper half, large headline with yellow emphasis in the upper left; three comparison modules in the middle: effect/result comparison, user product or kit, and generic basic solution; deep-blue check/cross table and benefit icons at the bottom.
- Information hierarchy: comparison headline first, user product versus generic ordinary product second, check/cross table third, bottom purchase reasons fourth.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: yellow checkmarks, gray missing symbols, deep-blue table, yellow borders, and white linear function icons.
- Scene expression: use realistic generalized scenes that can show result differences for the product; do not create exaggerated before/after claims.
- UI component design: VS comparison cards, kit/basic-solution cards, check/cross table, and bottom benefit icon strip.
- Effects rendering language: deep-blue industrial background, yellow emphasis edges, cool realistic scene lighting, and glass-like table texture.
- Selling-point logic: compare only provable differences. The ordinary product must be a brandless generic placeholder.
- Product placement form: the user product must be complete and clear; the ordinary product may be grayed out or simplified, but must not imitate a competitor product.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Comparison Advantage Image"; target filename token: Compare. Use the blue-and-gold high-density scene-evidence visual DNA: realistic scene photography combined with professional infographics; deep navy, bright blue, and white/light gray as the main colors; limited yellow/gold accents for key points. The image should communicate complete configuration, clear proof, visible usage results, reasons to choose, and a trustworthy purchase decision for any product category.

Composition requirements: realistic professional use scene in the upper half, large headline with yellow emphasis in the upper left; three comparison modules in the middle: effect/result comparison, user product or kit, and generic basic solution; deep-blue check/cross table and benefit icons at the bottom. Product placement: the user product must be complete and clear; the ordinary product may be grayed out or simplified, but must not imitate a competitor product. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: comparison headline first, user product versus generic ordinary product second, check/cross table third, bottom purchase reasons fourth. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use yellow checkmarks, gray missing symbols, a deep-blue table, yellow borders, and white linear function icons. Add VS comparison cards, kit/basic-solution cards, a check/cross table, and a bottom benefit icon strip as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The information density should feel professional, evidence-rich, and organized, not cluttered.

Scene expression: use realistic generalized scenes that can show result differences for the product; do not create exaggerated before/after claims. Scenes must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: deep-blue industrial background, yellow emphasis edges, cool realistic scene lighting, and glass-like table texture. Lighting, reflections, beams, shadows, and local highlights must support product recognition and comparison clarity, not imply unverified functions.

Selling-point logic: compare only provable differences. The ordinary product must be a brandless generic placeholder. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```

## style6-09-lifestyle.png

### Universal Generation Index

- Image type: Lifestyle / Result Image / Lifestyle.
- Variant positioning: premium lifestyle result scene.
- Visual style: follow the lifestyle branch of the blue-and-gold high-density scene-evidence style, while replacing all products and scenes with generalized expressions for the current `{product}`.
- Composition: realistic warm lifestyle scene occupying the right side and background, elegant large headline, subheadline, and 3 vertical icon selling points on the left, with the product clearly shown in a natural use position.
- Information hierarchy: usage result or scene benefit first, product-scene relationship second, limited icon explanation third.
- Layout: headline, product, selling points, specs, icons, and scene modules must have clear whitespace. Text must not press into or cover the product.
- Icon system: fine gold line decoration, deep-blue fine-line icons, circular icon frames, and elegant headline divider lines.
- Scene expression: replace the scene according to the product with a warm and credible home, dining table, office, travel, care, display, gifting, or professional-space context.
- UI component design: left-side text area, vertical icon selling points, fine-line decoration, and no heavy tables, making the image feel closer to a lifestyle advertisement.
- Effects rendering language: warm natural light, light ivory space, soft depth of field, gold accents, realistic product reflections, and material highlights.
- Selling-point logic: use realistic generalized scenes to show the usage result brought by the product without exaggerating effects.
- Product placement form: the product occupies 25%-45%, with a clear relationship to real use action or spatial context.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor/platform/certification logos, and do not copy original product facts from reference images.

### Production-Ready Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Lifestyle / Result Image"; target filename token: Lifestyle. Use the lifestyle branch of the blue-and-gold high-density scene-evidence visual DNA: realistic warm lifestyle scene, deep-blue text, fine gold line decoration, limited circular icon selling points, and natural product highlights. The image should communicate everyday use, refined display, gifting, comfort, coordination, and lifestyle results for any product category.

Composition requirements: realistic warm lifestyle scene occupying the right side and background, elegant large headline, subheadline, and 3 vertical icon selling points on the left, with the product clearly shown in a natural use position. Product placement: the product should occupy 25%-45%, with a clear relationship to real use action or spatial context. Preserve the real product proportions, color, material, structure, ports, accessories, edge details, and visible finish. Do not add unconfirmed parts.

Information hierarchy: usage result or scene benefit first, product-scene relationship second, limited icon explanation third. Use {headline} as the main headline and {subheadline} as the subheadline. Use selling points from {selling_points}, specifications from {specs}, and accessories from {accessories}. All text must use {language}, be short and readable, and contain no gibberish.

Layout and UI: use fine gold line decoration, deep-blue fine-line icons, circular icon frames, and elegant headline divider lines. Add a left-side text area, vertical icon selling points, fine-line decoration, and natural scene whitespace as appropriate for this image type. Keep component spacing consistent. Text must not cover the product. The image should feel premium, clear, and not overly information-heavy.

Scene expression: replace the scene according to the product with a warm and credible home, dining table, office, travel, care, display, gifting, or professional-space context. The scene must be selected from {scenes} and {use_context}, fit the current {product_category}, and must not reuse the original product scene from the reference image.

Effects rendering: warm natural light, light ivory space, soft depth of field, gold accents, realistic product reflections, and material highlights. Lighting, reflections, shadows, and local highlights must support product recognition and scene-result communication, not imply unverified functions.

Selling-point logic: use realistic generalized scenes to show the usage result brought by the product without exaggerating effects. Do not invent numbers, certifications, compatibility, efficacy, official endorsements, absolute promises, competitor defects, or platform marks. The final image should look like a production-grade ecommerce detail image ready for direct use.
```
