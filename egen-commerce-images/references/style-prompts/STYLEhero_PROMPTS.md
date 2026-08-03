<!-- English adaptation for ecommerce-product-images. Preserve variables and filename tokens. -->

# style_hero Universal Product Generation Index and GPT Image 2 Prompt

Scope: Hero images for any general product presented as a bundle, multi-pack, or complete configuration. Do not bind the output to the original product category in any reference image. Reuse only the high-information-density layout logic: quantity or set headline, bundle display, accessory list, functional icons, and bottom multi-scene card strip.

## Mandatory Universal Product Rules

- `{product}` must come from the product image uploaded or explicitly confirmed by the user in the current chat. It is the only source of truth for product appearance.
- Do not copy the product, brand, structure, accessories, parameters, people, scene facts, certifications, or text from any reference image.
- All product facts must come from user-provided material: `{product_category}`, `{use_context}`, `{target_user}`, `{selling_points}`, `{specs}`, `{accessories}`, `{scenes}`, `{language}`, and `{quantity}`.
- `{target_user}` describes the intended buyer or user group. Use it only to guide wording, scene relevance, and benefit framing; do not invent demographics, medical needs, occupations, or usage claims that the user did not provide.
- `{brand}` may be shown only when the user provides it. If `{brand}` is missing, leave the brand area blank or omit it entirely; do not invent a brand, manufacturer, certification body, store name, platform name, or competitor name.
- If the product is not a multi-pack, replace the `{quantity}` area with `{bundle_headline}`, such as "Complete Set", "All-in-One Kit", or "Ready to Use". Never fabricate a quantity.
- If the product does not fit a scene from the original reference, abstract that scene into equivalent visual logic, such as "dark atmospheric usage scene", "coverage or range visualization", or "fresh lifestyle scene", instead of carrying over the original product scene. Bottom scene cards must express generalized usage environments only; they must not transfer scene facts from the reference image.
- Any numbers, certifications, compatibility targets, comparison conclusions, materials, performance effects, use effects, benefit effects, and accessory counts must come from user-provided information. If missing, use neutral placeholder wording.
- Text in the image must use `{language}`. Keep it short, readable, and free of garbled characters. Do not show platform logos, competitor brands, certification marks, or absolute claims.
- Treat only user-mentioned facts as confirmed facts. When the user states a fact, do not require test reports, validation documents, endorsements, or certification files inside the prompt; treat the stated fact as available input.
- Reference images are layout and style references only. Isolate them from product semantics: never reuse their product identity, feature claims, accessories, scenarios, data, badges, people, or brand language unless the user independently provides the same facts for `{product}`.

## Style DNA

- Visual style: white or light-gray technology background, led by deep blue, bright blue, and black, with small amounts of silver gray and highlight blue to reinforce an industrial product feel.
- Design logic: make one screen clearly communicate whether this is a multi-piece pack or complete set, what is included, what problem it solves, and which usage scenes it fits.
- Composition characteristics: oversized quantity or bundle headline on the left, main product bundle display on the right, accessory matrix in the middle or lower area, functional icon grid on the left, and horizontal multi-scene cards along the bottom.
- Information density: high, but modular. Headlines, selling points, accessories, and scenes must have clear spacing and separation.
- Icon system: blue linear icons, circular or square icon cards, deep-blue pill labels, and white rounded information blocks.
- UI components: large-number headline, specification pills, 2x3 functional icon grid, blue horizontal core-benefit card, accessory list matrix, and 3-4 bottom scene cards.
- Effects rendering language: soft product shadows, white-blue rim lighting, local highlights, subtle light trails, and clean reflections. Realistic highlights may emphasize visible product details, but must not imply functions that do not exist.

## Prompt Variables

- `{product}`: any user-confirmed product.
- `{product_category}`: product category, used only to choose copy and scenes.
- `{brand}`: user-provided brand; omit if unavailable.
- `{quantity}`: real item count or bundle quantity.
- `{headline}` / `{subheadline}`: the main title and subtitle for this image.
- `{bundle_headline}`: set headline used when the product is not a multi-pack.
- `{headline}`: main title.
- `{subheadline}`: one core value statement.
- `{selling_points}`: 4-6 real selling points.
- `{specs}`: real specification parameters.
- `{accessories}`: real accessories or packing list.
- `{scenes}` / `{use_context}`: 3-4 realistic generalized scenes suitable for this product.
- `{target_user}`: intended buyer or user group; use for relevance and tone only, without inventing unprovided claims.
- `{language}`: target market language.

### Universal Generation Index

- Image type: Main image / Hero.
- Variant positioning: comprehensive first-screen overview.
- Visual style: use the high-information-density comprehensive Hero style, while replacing all products and scenes with general-product expressions for the current `{product}`.
- Composition: enlarged product at a diagonal angle or centered position, specification or selling-point cards on the right, and bottom scene thumbnails plus a parameter bar.
- Information hierarchy: product body first, main title second, 3-6 core selling points third, and bottom parameters or scene support fourth.
- Layout: title, product, selling points, parameters, icons, and scene modules must have clear whitespace. Text must not press against or cover the product.
- Icon system: blue circular linear icons, deep-blue bottom parameter icons, white rounded cards, and specification badges.
- Scene expression: use 3-5 generalized usage-scene mini cards to express suitable environments.
- UI component design: use rounded cards, labels, icon bars, data panels, comparison tables, or step cards according to this image type. Keep all component margins and alignment consistent.
- Effects rendering language: soft product shadows, blue-white rim lighting, light-gray technology textures, subtle light trails, and clean reflections.
- Selling-point logic: use one screen to establish product recognition, core value, and reasons to purchase. Avoid stacking unconfirmed specifications.
- Product placement form: in this universal index, the product should occupy about 40%-55% of the canvas. Local close-ups may be used, but must not alter the real structure.
- Product scale rule: the 40%-55% range is the general index range for reusable Hero layouts. If a final prompt below specifies a different product share, that final prompt-specific range overrides the index for that prompt only.
- Compliance boundary: do not write unconfirmed parameters, do not use competitor, platform, or certification logos, and do not copy original product facts from reference images.

### GPT Image 2 Industrial Production Prompt

```text
Use the user-uploaded and confirmed {product} as the only source of truth for product appearance. Generate a 1:1 ecommerce detail image for a general product. Image type: "Main image". Target filename token: Hero. Apply a high-information-density comprehensive Hero visual system: white or light-gray technology background, deep blue, bright blue, and black as the main palette, with small gold or yellow accents only for key emphasis. The result should function as a single-screen overview for any product category.

Composition requirements: show the product enlarged at a diagonal angle or centered position, with specification and selling-point cards on the right, a bottom strip of scene thumbnails, and a parameter bar. Product placement for this final prompt: the product should occupy about 70%-75% of the canvas. This prompt-specific 70%-75% product share overrides the universal index range of 40%-55% for this prompt only. Local close-ups are allowed, but they must not change the real structure. Preserve the real product proportions, colors, materials, structure, ports, accessories, surface finish, and edge details. Do not add unconfirmed parts.

If {quantity} is provided and the product is a real multi-pack or bundle, create a prominent quantity title area that clearly communicates the true count or set size. If the product is not a multi-pack, use {bundle_headline} in that same title area instead, such as "Complete Set", "All-in-One Kit", or "Ready to Use". Do not invent counts, included items, package size, or configuration details. If {accessories} is provided, show a clean accessory list or accessory matrix using only the real accessories or packing-list items from {accessories}; if it is missing, use neutral wording without item counts.

Information hierarchy: product body first, main title second, 3-6 core selling points third, and bottom parameters or scene support fourth. Use {headline} for the main title and {subheadline} for the subtitle. Draw selling points only from {selling_points}, specifications only from {specs}, accessories only from {accessories}, and scenes only from {scenes} and {use_context}. Use {target_user} only to make the benefits and scenes relevant to the intended buyer or user group; do not invent user attributes or claims. If {brand} is provided, place it as a restrained brand mark or small brand text. If {brand} is empty, omit the brand area entirely. All visible text must be in {language}, concise, readable, and free of garbled characters.

Layout and UI: use blue circular linear icons, deep-blue bottom parameter icons, white rounded cards, specification badges, rounded cards, icon bars, data panels, step cards, specification labels, comparison tables, or scene thumbnails as appropriate for a Hero image. Keep component spacing consistent and alignment precise. Text must not overlap the product, icons, scene cards, or other text. The image should feel information-rich and professionally modular, not cluttered.

Scene expression: create 3-5 generalized usage-scene mini cards for suitable environments. Select scene concepts only from {scenes} and {use_context}, and adapt them to the current {product_category}. Do not reuse the original product scene from any reference image. The bottom scene cards may mimic a multi-screen display frame with curved line accents, depth, lighting, and controlled glow, but the scene facts must remain generic and tied to {product}.

Effects rendering: use soft product shadows, blue-white rim lighting, light-gray technology textures, subtle light trails, clean reflections, realistic local highlights, and controlled glow. Lighting, reflections, beams, shadows, and highlights must support product recognition and selling-point communication. Do not create false functions, fake mechanisms, fake output effects, or unprovided performance effects.

Selling-point logic: use one screen to establish product recognition, core value, included configuration, and reasons to purchase. Do not invent numbers, certifications, compatibility, performance effects, use effects, efficacy, official endorsements, absolute promises, competitor defects, platform marks, or certification logos. The final image should look like an industrial-grade ecommerce detail image ready for direct use.
```
