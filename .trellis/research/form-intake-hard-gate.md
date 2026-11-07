# 电商图片表单硬门槛方案评估（2026-11-06）

## 已核实

- 当前 `egen-commerce-images` 插件依靠 `SKILL.md` 和默认提示要求优先启动表单；插件本身没有 MCP 服务或表单专用 hook。[技能](../../plugins/egen-commerce-images/skills/egen-commerce-images/SKILL.md)、[插件清单](../../plugins/egen-commerce-images/.codex-plugin/plugin.json)。现有项目 `.codex/hooks.json` 仅配置 mini-trellis 的 `SessionStart`，不对应每次产品任务。
- Codex hook 有 `UserPromptSubmit`、`PreToolUse`、`Stop` 等事件，但没有专门的“某个 skill 被调用”事件。`UserPromptSubmit` 的 matcher 当前不生效；`Stop` 可让代理继续执行。非托管的插件 hook 须先审核并信任，定义变更后要重新审核；部分工具路径可绕过工具 hook。[官方 Hooks 文档](https://learn.chatgpt.com/docs/hooks)、[插件打包文档](https://developers.openai.com/plugins/build/plugins)。
- MCP 工具能封装启动、校验和读取表单的动作；工具由模型选择调用，单独增加 MCP 工具不能强制模型先用表单。[官方 MCP 文档](https://developers.openai.com/plugins/concepts/mcp-server)。
- 本仓库是 linked worktree；此前已验证项目 hook 在此环境下从主仓库配置发现，并需单独信任。详见 [worktree hook 调查](codex-worktree-hook-discovery.md)。

## 方案判断（尚未确认采用）

- **建议：表单先行入口。** 用户从确定性的本地启动器进入：启动现有服务、检查 `/health`、打开表单；保存 JSON 后才把任务交给代理。这个入口可由程序保证顺序，也只在产品任务启动时运行。但若仍允许直接通过 `@plugin` 聊天开始同类任务，该路径可绕过启动器；需要决定是否保留及如何处理。
- **保留聊天入口时的补强：** 插件级 `UserPromptSubmit` hook 可识别相关提示并预启动服务，`Stop` hook 可检查任务状态并要求继续；这比新建 MCP UI 改动少，但需处理无专属 skill 事件、产品图是否已提供、hook 信任和误触发。它不是无条件的硬门槛。
- **MCP 工具：** 适合作为表单启动/读取的统一接口，或供未来的插件 UI 调用；只有把用户入口也交给确定性的 UI/启动器时，才能把“先填表单”从模型选择变成程序约束。[插件界面文档](https://developers.openai.com/plugins/build/extensions)。

尚未确认的选择：是否继续以 `@plugin` 聊天消息作为唯一入口，以及表单必须打开在 Codex 内置浏览器还是可用系统浏览器。未实现上述任一硬门槛方案。
