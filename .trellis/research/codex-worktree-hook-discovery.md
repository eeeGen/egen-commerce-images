# Codex worktree hook 未显示（2026-10-30）

## 已验证的原因

- 当前目录 `E:\projects\ecommerce-product-images-new-work` 是 linked worktree；主仓库为 `E:\projects\ecommerce-product-images`。
- 当前项目在用户配置中已经是 `trusted`，本地 `.codex/hooks.json` 格式正常。`hooks/list` 在 0.165.0-alpha.1.2 和应用 daemon 0.166.0 均只返回用户级 hook，没有项目 hook，也没有解析错误。
- Codex 对 linked worktree 将 hook 配置目录重定向到对应的主仓库目录；普通项目配置仍来自 worktree。主仓库当时没有 `.codex/hooks.json`，因此本地 hook 无法进入信任列表。
- 公开源码 `root_checkout_hooks_folder_for_dir` 计算重定向；`merge_root_checkout_project_hooks` 移除 worktree 的内联 `hooks`，再导入主仓库内联定义。因此改成本地内联 hook 也不能解决。
- 源码：https://github.com/openai/codex/blob/main/codex-rs/config/src/loader/mod.rs
- hook 信任说明：https://learn.chatgpt.com/docs/hooks

## 排除项与恢复

- 两版本结果一致；临时路径大小写、主仓库信任、根标记覆盖测试没有改善结果。
- 本地内联 hook 诊断修改已逐字节恢复，没有保留实验配置。
- 不要把“项目 trusted”和“具体 hook trusted_hash”混为一谈；后者必须先能发现定义。

## 已批准并完成的修复

用户明确批准“在主仓库将其标记为可信”。已在主仓库新增 `.codex/hooks.json` 和 `.codex/hooks/mini-trellis-session-start.py`。后者只转发到当前 checkout 已安装的 mini-trellis SessionStart 脚本，没有安装则跳过，避免影响未安装 mini-trellis 的 checkout。

通过 Codex `config/value/write` API 在用户级 `C:\Users\eGen\.codex\config.toml` 写入主仓库 hook 的 `trusted_hash`，未改动其他配置：

- key：`E:\projects\ecommerce-product-images\.codex\hooks.json:session_start:0:0`
- hash：`sha256:47313fb80cf6c81fb3736aff38b1748d292ff6d8274e6e7a6322c372b1de6235`
- 备份：`C:\Users\eGen\AppData\Local\Temp\codex-config-before-hook-trust-20261030.toml`

安装后的 `hooks/list` 检查：主仓库及当前 worktree 均发现来自主仓库的同一个 hook，`enabled=true`、`trustStatus=trusted`，warnings/errors 均为空。

手动测试实际安装的分发脚本：当前 worktree、其 docs 子目录均输出有效 SessionStart additionalContext（1186 字符）；没有 mini-trellis 的主仓库退出成功且无输出。已验证用户 TOML 的语义差异仅为本 hook 的信任记录，当前 worktree 配置与诊断前逐字节相同。尚未观察应用新会话自动触发或设置页刷新；这与已通过的后端发现/信任检查分开表述。

首次自动审批因跨 worktree 影响范围未获明确授权而拒绝；用户随后明确批准，本次安装及信任写入已成功。没有使用跳过 hook 信任的启动参数。
