# 插件版本与发布

## 版本与文档

- 插件包版本以 `plugins/egen-commerce-images/.codex-plugin/plugin.json` 的 `version` 字段为准；构建标识沿用 `+codex.YYYYMMDDHHMMSS` 格式。正式 tag 使用不带构建标识的 `vMAJOR.MINOR.PATCH`。
- 用户可见的新功能按次版本升级；修订号用于兼容性范围内的修复和小优化。
- 每次版本记录同步更新 `docs/VERSION_UPDATE.md`、用户更新说明 `docs/RELEASE_NOTES.md` 和 `docs/plan-archives/` 中的版本计划。

## 合并与正式发布

- 合并或推送到 `main` 表示代码集成，不自动表示插件已正式发布。未获正式发布确认前，记录为待发布，不创建版本 tag。
- 正式发布确认后，将版本文档状态改为已发布，以包含最终发布记录的提交创建 `vMAJOR.MINOR.PATCH` 轻量 tag，并推送 `main` 与 tag。该项目现有的 `v0.11.0` 和 `v0.12.0` 均采用轻量 tag。

## 本地测试市场命名

- 为避免本地已安装的同一插件冲突，可临时改动 `.agents/plugins/marketplace.json` 中的测试市场名称。
- 该重命名只用于本地测试；提交和同步到 `main` 时保留正式市场名 `egen-commerce-images-marketplace` / `eGen Commerce Images`。
