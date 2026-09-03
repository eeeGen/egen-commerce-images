# 客户参考风格工作流

当保存的任务 JSON 中 `taskOptions.styleSource` 为 `customer-reference` 时使用本参考；不读取内置 style prompt 文件或 `E:\e-commerce\knowledge` 的风格图。

## 任务资料

本地表单会把扫描后的素材 ID 解析为路径。只信任以下已解析字段，不使用浏览器传回的 ID 或自行猜测素材路径：

- `referenceWorkflow.colorMasterPath`
- 每张 `referenceWorkflow.outputs[]` 的 `productImagePaths`
- 每张 `referenceWorkflow.outputs[]` 的 `styleReferencePath`

每张输出卡片都必须有名称、1–4 条 `productImagePaths` 与恰好 1 条 `styleReferencePath`。产品实拍用于直接校准产品外观；不要以文字描述替代或扩展产品的外形、比例、颜色、材质、结构、接口、配件和细节。

`colorMasterPath` 由客户手动选择。若它不是该卡片的 `styleReferencePath`，只将其色彩倾向转为简短调色约束；不可把它作为第二张风格参考传给 Image Gen。参考图的画幅不决定输出比例；使用全局比例或客户在 `ratioOverride` 中明确覆写的比例。

`colorPriority` 为 `scene` 时，优先保留该风格图的大面积场景环境色；为 `master` 时优先遵循色彩母版；为 `auto` 时在生成配方总览中说明采用哪一个并让客户确认。

## 生成配方总览

在生图前，用中文逐卡列出：卡片名称、表达意图、产品实拍文件名、风格参考文件名、色彩母版文件名、色彩策略、最终比例和文案草案。客户可修改卡片、文案或映射；只有明确确认后才生成。

文案草案只能根据已确认的真实产品资料、卡片意图、平台和目标语言撰写。保留参考图的文字位置、层级、密度、字体气质和通用组件语言，但不用其品牌、原文案、平台标识或产品事实。

## 单卡生成

每张输出卡片独立调用一次 `image_gen.imagegen`，通过 `referenced_image_paths` 传入：

1. 该卡片的 1–4 张 `productImagePaths`；
2. 紧接其后的 1 张 `styleReferencePath`。

不得批量合并多个卡片、不得传入未映射的产品图、不得传入第二张风格参考图。产品图直接决定产品外观；风格图直接决定构图、场景、版式和视觉语言。提示词只要求以客户产品替换参考图中的产品，并包含已确认的卡片意图、文案草案、色彩策略、比例和通用安全区要求。

尽量保留参考图的场景、构图、镜头、光线、信息层级和版式节奏；将竞品产品换为客户产品，并将品牌、商标、平台标识、人物脸、角色/IP、独特插画和受保护文案替换为中性、功能等价元素。不要生成未证实的产品事实。

生成后直接交付所有结果；不做自动视觉核验或自动重试。按原有输出归档规则保存，每张卡片使用文件安全的卡片名称，并将 style token 记为 `customer-reference`。
