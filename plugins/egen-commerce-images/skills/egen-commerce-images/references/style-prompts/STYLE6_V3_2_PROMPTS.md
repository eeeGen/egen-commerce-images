# style6-v3-2 品牌散文式情绪叙事图组系统

## 定位与继承关系

`style6-v3-2` 是 `style6-v3` 的独立强化分支，用于品牌官网、A+ 页面和需要让产品“被看见、被感到、被记住”的叙事型详情图。它继承 v3 的低 UI、真实产品优先、安静空间和章节化套图节奏；不同之处在于，每一幅图在形成 Image Gen 指令前，必须先写成一段克制而具象的品牌散文式视觉导演描述。

这段描述不是虚构品牌故事，也不是画面上要渲染的长文案。它的作用是把已确认的产品事实转化为可拍摄的光线、空间、材质、动作和观看节奏：让画面有温度和停顿，却始终能够回到真实产品本身。

与 `style6-v3`、`style6-v2` 做同输入测试时，必须锁定同一份产品事实、身份参考、图片类型、比例、目标市场/语言、可见文案事实和 logo 安全区；只允许改变视觉导演策略。不得通过增加虚构配件、改变商品数量或修改卖点来制造风格差异。

## 绝对事实边界

- 产品图片是外形、颜色、材质、结构、接口、包装和配件的唯一事实来源。
- 多张参考图用于校准同一真实产品的不同角度；除非包装清单或实拍明确证明为套装，不得把它们渲染为多个产品或多个包装。
- 只有可证实的组件、配件、尺寸、功能和使用场景才能进入画面或文案。没有事实时留白，不以优美措辞填补未知。
- 不虚构内部结构、认证、性能结果、人物身份、品牌历史、生活方式、销售单位或配件关系。
- 顶右角始终保留自然 logo 安全区，不放置产品、文字、图标、边框或占位元素。
- 文学性只用于内部导演描述；所有可见文字仅可使用已确认的 `{headline}`、`{subheadline}`、`{selling_points}`、`{specs}`、`{accessories}`、`{scenes}` 与 `{use_context}`，并使用 `{language}`。不得将散文段落直接作为画面文案。

## 产品参考角色

每张图只选 1--4 张当前镜头最相关的产品参考，并标记其角色：

- `identity-anchor`：锁定整体外形、颜色和比例的主参考。
- `view-proof`：证明另一角度、接口或可见结构的参考。
- `set-proof`：证明包装内容、组件数量和真实套装关系的参考。
- `detail-proof`：证明纹理、按键、边缘、材质或局部结构的参考。

只传入当前镜头必要的参考。参考数量不代表画面中的产品数量；除非 `set-proof` 明确支持，不得生成产品阵列、重复实例、多个包装或虚构配件。

## 套装、多组件与多 PCS 的单件镜头规则

在撰写单图 prompt 前，先判断产品资料是否证实为多组件套装、含配件套装或多 PCS 同款商品。若是，Coverage Matrix 必须安排至少一个单件/单组件镜头，且整组图片不得反复展示完整套装。

- **多 PCS 同款商品**：至少一幅图只展示一个真实单品，作为外形、材质、局部细节或使用中的视觉主角。此镜头用于理解单件产品，不得据此暗示单件单独销售、改变包装数量或新增售卖选项。
- **多组件或配件套装**：只在总览、经确认的包装说明或收束镜头展示完整套装；在 Selling、Feature、Specs、CoreA、CoreB 或 Lifestyle 等合适章节中，选取一个真实主件或一个已验证配件作为单独镜头主角。
- **单件镜头的事实关系**：构图可以只让一个组件入镜，但可见文字和叙事不得把它说成独立商品；若需解释归属，只使用已确认的包装/配件事实。
- **镜头分配优先级**：少量图片时，优先安排“完整关系（如已证实）→ 单件主角 → 细节/使用 → 安静收束”，而不是在每幅图里重复所有组件。

## 套图 Coverage Matrix 与反重复规则

在写任何单图 prompt 前，先建立一张 set-level Coverage Matrix。每张已选图片必须记录：叙事章节、产品形态（完整套装/单件/单组件/微距/使用中）、真实证据、故事瞬间、空间与时段、景别与机位、信息密度，以及避重复策略。

| 类型 | 叙事章节 | 推荐产品呈现 | 单件/套装要求 |
| --- | --- | --- | --- |
| Hero | 初见 | 单件主产品或已验证套装 | 套装只在需要说明整体关系时出现 |
| Selling | 靠近 | 单件主产品加一个真实证据 | 多件商品优先单件主角 |
| CoreA | 融入 | 使用中的单件或主件 | 以一个真实动作承载场景 |
| CoreB | 延展 | 与 CoreA 不同的单件/组件状态 | 改变空间、时段或使用路径 |
| Feature | 触感 | 单件局部或单组件微距 | 不绘制内部结构或虚构零件 |
| Specs | 了解 | 单件多视角或已验证包装关系 | 仅在证据需要时展示整套 |
| Value | 选择 | 单件配少量真实价值节点 | 避免再做套装陈列 |
| Compare | 辨别 | 客户单件与中性通用对照 | 只比较可证明的属性 |
| Lifestyle | 日常 | 自然环境中的单件或主件 | 产品必须易于辨认 |
| Closing | 回望 | 单件或已验证套装 | 与 Hero 改变角度、光线或空间 |
| Guide | 开始 | 连续操作中的真实主件/配件 | 每步均需实际证据支持 |

新镜头相对前图至少改变四项：产品形态、景别、机位、空间、时间/光线、叙事动作、信息密度、完整套装与单件的关系。完整套装不能成为整组的默认构图。

## 品牌散文式导演配方

每张图先完成以下配方，再将其转化为结构化 Image Gen 指令。散文段落应以可见的空间、光线、材质和动作描写为主；可写“空气、停顿、光影或触感”，但不可把未确认的心理、背景故事或产品效果当作事实。

```text
故事瞬间：<由已确认场景支持、可被镜头看见的时刻>
散文式导演描述：<2--4 句克制、具象、可拍摄的场景描写>
观者感受：<从真实特征合理推导的情绪，不夸大结果>
产品形态：<单件 / 已验证套装 / 单组件 / 微距 / 使用中>
真实证据：<本图允许展示的组件、结构、卖点、规格>
镜头：<景别、机位、焦点、前中后景、产品占比>
空间层次：<氛围背景 → 叙事环境 → 产品 → 触感/证据 → 编辑留白>
可见文字：<仅限已确认字段，或完全留白；使用 {language}>
光色：<实际光源、材质反射、系列色彩关系>
避免：<重复套装、虚构配件/功能、密集 UI、过度电影特效>
```

## Image Gen 指令结构

最终 prompt 使用下列结构。将散文式导演描述转译为镜头语言，而不是原样当作需要渲染的文字；若资料不足，删除对应字段，不补写猜测。

```text
Use case: product-mockup
Asset type: <品牌官网 / A+ / 详情图的具体图片类型>
Primary request: <本图的真实叙事目标>
Scene/backdrop: <由散文描述提炼的、已证实或中性工作室空间>
Subject: <单件、单组件或已验证套装；明确真实外形和关系>
Style/medium: photorealistic editorial product photography, quiet brand prose sensibility
Composition/framing: <景别、机位、产品占比、留白与安全区>
Lighting/mood: <实际光源、阴影、材质高光与克制情绪>
Materials/textures: <仅限已确认材质、表面和触感细节>
Text (verbatim): <仅含已确认 {language} 文案；没有则 no visible text>
Constraints: preserve the exact product identity, proportions, components, and verified set relationship; reserve the top-right logo safe area
Avoid: invented accessories, repeated product instances, unverified claims, dense UI, long prose rendered as text, watermark
```

## style6-v3-2 分镜指令

### Hero — 初见：让真实产品先安静地出现

**散文式导演描述**：让已确认的主产品停在一个能够呼吸的空间里。侧光从画外缓慢掠过真实的边缘和材质，接触阴影把它稳稳放在桌面、织物或干净影棚中；周围没有急于解释的配件，只有足够的留白，让第一次注视先落在产品本身。若完整套装已被证实且总览确有必要，组件以前后层次轻轻回应主件，而不是排成陈列队。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Hero brand-site product image
Primary request: introduce the verified product with quiet, tangible presence
Scene/backdrop: a restrained studio still life or a verified use-context surface, with breathable negative space
Subject: one verified primary product; include the verified full set only when an overview is required
Composition/framing: sculptural 45-degree or low-angle medium-wide shot; product occupies 38--62%; keep the top-right logo safe area naturally empty
Lighting/mood: soft side window light or controlled studio light, real contact shadow, subtle material highlights
Constraints: show no repeated instances; use only verified components and factual copy
Avoid: flat product lineup, dense panels, invented props, long visible prose
```

### Selling — 靠近：一个真实价值被温柔看见

**散文式导演描述**：镜头靠近一个真实的结构、表面或已确认的使用动作，让产品不必大声证明自己。光线在可见细节上停留片刻，背景退成安静的色块或浅景深；画面只留下一个可核对的理由，像编辑页上一句恰到好处的旁注。对于套装或多 PCS 商品，此处优先由一个单件承担讲述，而不是把所有物品再次摆开。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Selling-point editorial image
Primary request: reveal one verified value through a single product or component and one visible proof
Scene/backdrop: quiet, shallow-depth environment supported by verified context or a neutral studio surface
Subject: one verified single item or component, never a repeated full set by default
Composition/framing: medium-close shot with a distinct camera angle from Hero; one restrained evidence detail
Lighting/mood: soft directional light that makes the verified texture or structure legible
Text (verbatim): only one short verified {language} headline or no visible text
Constraints: preserve product identity and verified set relationship without implying separate sale
Avoid: feature lists, icon grids, invented claims, duplicated products
```

### CoreA — 融入：最典型的真实使用时刻

**散文式导演描述**：选择资料已确认的主要场景，让一个真实单件或主件自然进入一个可见动作的前一秒或进行中。手部、桌面、收纳位置或环境光只是叙事的余音，人物不看镜头，也不被塑造成代言人；产品仍清楚地留在画面的呼吸中心。这个瞬间应像生活本来就有的节奏，而不是为了广告临时搭起的舞台。

**Image Gen 转译重点**：

```text
Use case: photorealistic-natural
Asset type: CoreA primary use-moment image
Primary request: show one verified product naturally participating in its most supported use context
Scene/backdrop: only the confirmed {scenes} or {use_context}; otherwise use a no-person studio narrative
Subject: one recognizable verified single item or primary component in a real, supported action
Composition/framing: environmental medium shot with foreground, middle ground, and softly receding background
Lighting/mood: authentic light from the depicted space; natural shadow and restrained color
Constraints: hands and environment serve the product; no unsupported user identity or outcome claim
Avoid: complete set laid out in the scene, staged endorsement pose, cluttered information cards
```

### CoreB — 延展：另一段被证实的生活节奏

**散文式导演描述**：让故事换一个时段、空间、动作或观看距离，而不是把同一画面换一块背景。产品在另一种已确认的节奏里被拿起、放回、准备、整理或结束使用；光的温度和镜头的距离随之改变。它仍是同一个真实物件，却在不同章节里显出另一种可见的存在方式。

**Image Gen 转译重点**：

```text
Use case: photorealistic-natural
Asset type: CoreB alternate use-moment image
Primary request: extend the product narrative through a second verified context or action
Scene/backdrop: a confirmed alternative scene, time of day, or spatial rhythm distinct from CoreA
Subject: one verified single item or component in a supported alternate state
Composition/framing: deliberately change at least two of scene, action, temperature, camera angle, or distance from CoreA
Lighting/mood: a new but believable light condition with real material response
Constraints: use only verified context and components; retain clear product recognizability
Avoid: repeating CoreA pose, repeating full-set layout, speculative activities
```

### Feature — 触感：细节在光里说话

**散文式导演描述**：把镜头收进真实表面、按键、接口、边缘或可见结构的近处。高光不必炫耀，只需沿着材质留下可信的轮廓；阴影让凹凸、转折和手指可触及的地方慢慢显现。画面的一角可以保留少量完整轮廓作方位提示，但真正被阅读的是一个已存在的细节，而不是被想象出来的内部世界。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Feature detail image
Primary request: make one verified surface, button, port, edge, or visible structure tangible and precise
Scene/backdrop: minimal material surface or controlled dark-to-soft background, with no unsupported context
Subject: a verified single-item macro detail; optionally retain a small complete silhouette for orientation
Composition/framing: macro or tight close-up, shallow focus placed on the real feature, at most one fine factual callout
Lighting/mood: precise raking light, controlled reflection, authentic micro-texture and shadow
Constraints: do not invent internal parts, x-ray views, energy effects, or extra components
Avoid: technical-dashboard UI, exploded diagrams, duplicate product instances, fabricated labels
```

### Specs — 了解：形态被从容地说明

**散文式导演描述**：让产品在近似画册的留白中转过真实的角度。正面、侧面、背面或一个局部结构依次出现，像手指翻过一页页克制的纸面；若资料已给出尺寸或包装关系，细线和小注只在需要的地方落下。对于多 PCS 商品，至少一个视角只呈现一个单品，使观者能够先理解它自身的比例与轮廓。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Specs and form-proof image
Primary request: explain verified form, view, dimension, or package relationship with editorial restraint
Scene/backdrop: near-white, softly toned, catalog-like negative space
Subject: one verified single item shown from 2--3 real views; add verified package relationship only when needed
Composition/framing: rhythmic multi-view layout without copying the product into a retail lineup
Text (verbatim): only verified {language} specs or dimensions; otherwise no numbers and minimal labels
Lighting/mood: soft even studio light that preserves true color, proportion, and edges
Constraints: a multi-PCS product must include at least one single-item view; do not imply separate sale
Avoid: invented views, fabricated measurements, dense tables, complete-set repetition
```

### Value — 选择：理由留在留白之间

**散文式导演描述**：一个真实单件停在留白的中心，周围不是喧闹的承诺，而是最多三个被确认的价值节点，像从画面边缘轻轻靠近的注脚。材质微距、真实配件或已证实场景的色彩回声可以出现一次，却不抢走主体。画面的节奏应让观者先看见产品，再慢慢读到值得停留的理由。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Value editorial image
Primary request: support selection with a single verified product and up to three factual value points
Scene/backdrop: spacious editorial field with a restrained color echo from a verified material or scene
Subject: one verified single item as the visual center; only minimal supporting evidence
Composition/framing: asymmetric, generous negative space; clear hierarchy from product to factual annotations
Text (verbatim): at most three short verified {language} value points
Lighting/mood: calm studio or natural light, deep readable body text color, one muted editorial accent
Constraints: facts first; if a value point is not verified, omit it
Avoid: six-benefit lists, full-set spread, dense cards, exaggerated performance language
```

### Compare — 辨别：差异不需要喧哗

**散文式导演描述**：让客户产品以真实的轮廓、材质和焦点站在安静的一侧；另一侧只是无品牌、无可识别外观的通用替代物，退在较弱的光里。对比不是审判，而是把可证实的结构、收纳关系或包装事实轻轻并置。画面不使用红叉、贬损语或戏剧化失败效果，只让已经存在的差别自然可见。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Compare image
Primary request: make a small number of verified differences legible without disparagement
Scene/backdrop: quiet neutral comparison field with editorial spacing
Subject: the exact verified customer single item beside a generic, unbranded, non-identifiable alternative only when a factual comparison is supported
Composition/framing: balanced but not symmetrical; customer product has clearer focus and truthful material light
Text (verbatim): only 2--4 short verified {language} comparison facts, or no visible text when facts are insufficient
Lighting/mood: restrained contrast, no dramatic failure cues
Constraints: never mimic competitor packaging or design; compare only provable attributes
Avoid: logos, red X marks, absolute claims, imagined results, repeated full set
```

### Lifestyle — 日常：产品在生活里留下一个片段

**散文式导演描述**：镜头从一个自然的前景、柔焦的背景或窗边的光中望向产品。它不是被摆出来证明什么，而是在一个已确认的生活片段里安静地被拿着、放着或等待下一次使用；环境提供层次，产品仍保有清楚的外形和位置。让画面像偶然被看见的一段日常，而不是堆满参数的销售页。

**Image Gen 转译重点**：

```text
Use case: photorealistic-natural
Asset type: Lifestyle brand-story image
Primary request: place one verified product naturally inside one supported everyday moment
Scene/backdrop: only a confirmed use environment, with foreground depth and softly defocused background
Subject: one easy-to-recognize verified single item or primary component
Composition/framing: natural environmental framing; product remains readable even when not centered
Lighting/mood: believable available light with soft texture and quiet atmosphere
Text (verbatim): no visible text or one short verified {language} title
Constraints: preserve the exact product identity; do not add unsupported people, props, or accessories
Avoid: product lineup, floating UI cards, dense specs, generic luxury clichés
```

### Closing — 回望：故事安静地收束

**散文式导演描述**：回到真实产品，但不要重复 Hero 的答案。也许天色更深一点，纸张、织物或干净的背景纹理接住更柔和的边光；产品像一段叙事走到尾页后留下的物件，安静、清楚、没有多余的承诺。若完整套装确有必要，可以以真实关系轻轻出现；否则由一个单件完成收束。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Closing brand-site image
Primary request: close the verified product story with a quieter, distinct final still life
Scene/backdrop: restrained studio, paper, textile, or verified surface with a different atmosphere from Hero
Subject: one verified single product by default; include the verified set only when it is factually necessary
Composition/framing: a new angle, lighting condition, or background relationship from Hero; top-right safe area remains empty
Lighting/mood: low-saturation depth, soft edge light, authentic contact shadow
Text (verbatim): only provided brand/product name and one verified {language} summary, if available
Constraints: do not create a brand history, awards, price promotion, platform marks, or unsupported promise
Avoid: Hero repetition, component lineup, overdone cinematic glow, long visible prose
```

### Guide — 开始：每一步都来自真实关系

**散文式导演描述**：把已证实的开始动作拆成两到四个连贯片段。手势、产品与真实配件在同一安静空间中依次靠近、连接、放置或完成；每一帧都像上一帧自然留下的余温，不靠夸张箭头催促。若步骤只涉及一个主件，就让单件持续承担视线中心；只有实际需要时才让已验证配件进入。

**Image Gen 转译重点**：

```text
Use case: product-mockup
Asset type: Guide / first-use image
Primary request: show 2--4 coherent, fact-supported opening actions in a single calm visual sequence
Scene/backdrop: one consistent, uncluttered, verified or neutral preparation space
Subject: the verified primary single item and only the components required by each confirmed step
Composition/framing: connected frames with a natural eye path; product-and-hand relationship remains legible
Text (verbatim): small step numbers and short verified {language} action verbs only
Lighting/mood: stable, believable light across the sequence
Constraints: every step must be supported by product photos, accessories, or confirmed instructions
Avoid: guessed setup, charging, cleaning, maintenance, safety steps, decorative technical UI, repeated full-set layout
```

## A/B 与成片验收

- 首眼应像有空间、触感和章节节奏的品牌官网/A+ 编辑页；散文感来自真实镜头组织，不来自冗长的画面文字。
- 每张图必须有一个可见、可拍摄、由证据支持的故事瞬间；情绪只能从真实材质、空间、光线和动作中合理推导。
- 套装、多组件和多 PCS 商品的 Coverage Matrix 必须明确至少一个单件/单组件镜头；整套图不得在每一张中重复完整套装。
- 多 PCS 商品的单件图必须准确保留真实外形、比例、颜色和结构，不得暗示单件独立销售或改变已确认的包装数量。
- 主产品、真实组件和已确认卖点应始终可核对；没有依据的文字、配件、人物、场景或效果宁可省略。
- 相比 `style6-v3`，v3-2 应显著提升每幅图的可见瞬间、感官细节和章节文学性；相比 `style6-v2`，它仍应保持更低 UI 密度、更强空间层次和更安静的叙事节奏。
