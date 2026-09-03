# style6plus Feature Validation Prompt

## Scope and inheritance

`style6plus` is a Feature-only validation branch. It inherits the deep navy, bright blue, white/light gray, and limited gold visual DNA of `STYLE6_PROMPTS.md`; it does not alter or replace style6. Read the style6 Feature rules for visual language, then use this document for the layout, evidence gate, and quality bar.

Use only verified facts and the current product images. The spray gun, Spanish copy, mechanic, cup, nozzle, regulator, and filter in the originating style6 reference are layout examples, not reusable product, person, scene, accessory, or copy facts.

## Required evidence gate

Before proposing or generating a style6plus Feature image, assemble this evidence map from the current product materials:

| Required role | Minimum evidence |
| --- | --- |
| Main product | One clear full-product image that reveals the visible feature side. |
| Callouts | Three visible, user-confirmed components or structural features, each with an exact label and visible anchor. |
| Detail inset | One crop or product image that clearly supports one confirmed feature. |
| Support items (conditional) | Confirmed accessories or visible subcomponents, only when they will appear in the lower-left zone. |
| Use proof | One confirmed use context or a product image that can truthfully support the lower-right scene panel. |
| Copy | One headline, one short subheadline, and three concise feature labels in the target language. |

Do not silently replace missing evidence with invented objects, internal mechanisms, people, performance effects, quantities, or claims. If a required role is unavailable, stop before generation, identify the missing role, and request that specific evidence. Support items are optional only when their zone is omitted. This validation branch deliberately favors an incomplete plan over a visually complete but ungrounded Feature image.

## Fixed composition blueprint

Generate a square Feature image using this structure. Percentages refer to the full canvas; they are layout anchors, not permission to crop or distort the product.

1. **Header block:** place the headline in the upper-left `x 4-45%, y 5-19%`; put the short subheadline on a flat gold band immediately below, within `x 0-42%, y 20-25%`.
2. **Feature rail:** place exactly three deep-blue hexagonal or circular icons in a vertical rail at `x 4-29%, y 28-61%`. Pair each with one verified short feature label. Keep this rail independent from the product silhouette.
3. **Product anchor:** place one large, complete, naturally angled product at `x 30-76%, y 2-73%`. It is the dominant object and must retain its real proportions, color, materials, ports, controls, accessories, and edge details.
4. **Callout field:** connect the three confirmed component labels to visible product anchors with thin blue leader lines. Use the right-side field `x 72-96%, y 15-68%` for labels when possible; use the lower-left field only for a visible anchor that cannot be read from the right. Lines must end on the real component, never a guessed internal part.
5. **Detail inset:** add one circular magnified crop at `x 23-43%, y 50-69%`, linked to the corresponding visible component. It must show the same product feature, not a decorative substitute.
6. **Support-item zone:** if and only if confirmed accessories or visible subcomponents exist, arrange them as separate factual cutouts at `x 0-31%, y 67-91%`. Omit this zone rather than adding unverified objects.
7. **Bottom proof band:** make a single deep-navy rounded horizontal band at `x 30-100%, y 73-100%`. It has three adjacent panels in this order: confirmed detail visual (about 32% of the band), short evidence-led message (about 43%), and confirmed use-context visual (about 25%). This is one asymmetric proof band, not unrelated floating cards.
8. **Logo-safe zone:** preserve a clean, natural top-right area at `x 80-100%, y 0-12%` for future logo placement. No text, icon, callout, product, border, or card may enter it.

Use a white/light-gray technical background, deep-blue typography and leader lines, blue feature icons, restrained yellow dividers and emphasis, clean product shadows, and realistic material highlights. The composition should read as one evidence chain: product structure -> labelled component -> detail proof -> use proof.

## Generation instruction

Use the current product images as the sole appearance source. Generate a 1:1 ecommerce Feature image with the inherited style6 blue-and-gold visual DNA and the fixed style6plus composition blueprint. Establish the named layout zones before rendering decorative effects. Preserve the product exactly; do not add parts or accessories.

Render only the verified `{headline}`, `{subheadline}`, `{component_labels}`, `{detail_feature}`, `{accessories}`, and `{use_context}`. The lower proof band is required only after the evidence gate is satisfied. All visible wording must be concise, readable, and in `{language}`. Use neutral language for unverified benefits. Do not reproduce the source reference's product, person, scene, logos, text, quantities, dimensions, claims, or component names.

Top-right logo safe area: keep a clean natural background area for future logo placement. Do not draw any visible placeholder box, border, outline, rounded rectangle, frame, shadow panel, icon, text, logo, or product in this area. The area should blend seamlessly with the same background texture and lighting as the rest of the image.

## Acceptance checklist

Before delivering the image, verify all of the following:

- The image is square and the top-right safe zone is empty.
- The main product is complete, recognizably faithful, and dominates the central area.
- There are exactly three icon-and-label items in the left rail.
- Every callout leader line terminates on a visible, verified product component.
- The circular detail inset shows the same confirmed feature as one callout.
- The lower region is one deep-navy three-panel proof band, not scattered cards.
- Every accessory, scene, number, claim, and label is supported by current-product evidence.

If any required layout module is missing, regenerate or edit only that module while locking the accepted product appearance and all already-correct zones.
