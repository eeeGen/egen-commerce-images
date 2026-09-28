# 客户参考风格工作流

当保存的任务 JSON 中 `taskOptions.styleSource` 为 `customer-reference` 时使用本参考；风格来源是客户选中的本地图片。

## 任务资料

schema v4 使用服务端解析的 `referenceWorkflow.productImagePaths`（共用外形参考图，至少一张）、按用户选中顺序排列的 `referenceWorkflow.styleReferencePaths`（仿照图，至少一张）、`referenceWorkflow.colorMasterPath`（单张色彩母版）和全局 `referenceWorkflow.colorPriority`。只信任这些已解析路径；浏览器传回的 ID 和目录字段不用于生图。母版可以不在仿照图列表中；它不增加输出数量。

如读取已保存的 schema v3 客户参考任务，沿用该任务 `referenceWorkflow.outputs[]` 中逐卡解析的 `productImagePaths`、`styleReferencePath`、`colorPriority`、`ratioOverride`、`intent` 和 `copyOverride`，每卡生成一张。旧任务不转换为 v4。

外形参考图直接校准产品外观；不要以文字描述替代或扩展产品的外形、比例、颜色、材质、结构、接口、配件和细节。参考图画幅不决定输出比例；v4 使用 `taskOptions.ratio`，v3 使用全局比例或卡片的 `ratioOverride`。

色彩母版只提供跨图片的调色方向。若它不同于当前仿照图，只将其色彩倾向转为简短调色约束，不将它作为第二张风格参考传给 Image Gen。`colorPriority` 为 `scene` 时优先保留当前仿照图的大面积场景环境色，为 `master` 时优先遵循母版，为 `auto` 时在总览中说明建议并让客户确认。

## 生成配方总览

生图前用中文列出共用外形参考图文件名、按生成顺序排列的仿照图文件名、色彩母版文件名、色彩策略、最终比例和各图文案草案。v3 继续逐卡列出名称、意图及对应图片。客户可以修改图片选择、顺序、文案或映射；明确确认后逐张生成。

文案草案只能根据已确认的真实产品资料、额外要求、平台和目标语言撰写。保留仿照图的文字位置、层级、密度、字体气质和通用组件语言，但不用其品牌、原文案、平台标识或产品事实。

## 逐张生成

v4 按 `styleReferencePaths` 顺序，每张仿照图独立调用一次 `image_gen.imagegen`。每次通过 `referenced_image_paths` 先传入全部 `productImagePaths`，再传入当前这一条风格图路径。v3 逐卡独立调用，每次传入该卡片的产品图和风格图。

产品图决定产品外观；当前风格图决定构图、场景、版式和视觉语言。提示词要求以客户产品替换仿照图中的产品，并包含已确认的文案、色彩策略、比例和通用安全区要求。

尽量保留仿照图的场景、构图、镜头、光线、信息层级和版式节奏；将竞品产品换为客户产品，并将品牌、商标、平台标识、人物脸、角色/IP、独特插画和受保护文案替换为中性、功能等价元素。不要生成未证实的产品事实。

生成后直接交付所有结果；不做自动视觉核验或自动重试。按原有输出归档规则保存，v4 使用仿照图文件名的文件安全主干和两位生成序号，v3 使用文件安全的卡片名称，并将 style token 记为 `customer-reference`。
