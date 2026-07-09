# 维护者指南

## 设计目标

- 让工作流在多种 AI 编程工具里都可用。
- 保持 WordPress 技术栈简单、可审计。
- 用真实验证代替乐观总结。
- 把上线准备当成严格闸门。
- 生成代码必须小、局部、可回滚。

## 规则放在哪里

- `SKILL.md`：核心规则、触发关键行为、死规则、reference 路由。
- `references/intake-checklist.md`：需求采集和 site_config schema。
- `references/phase-playbook.md`：建站流程和阶段闸门。
- `references/qa-and-launch.md`：验证和上线标准。
- `references/code-snippets-implementation-guide.md`：snippet 安全、交互和实现规则。
- `references/woocommerce-customizations-guide.md`：WooCommerce UX 模式。
- `references/product-csv-originality-seo.md`：CSV 改写/导入/媒体完整性。
- `docs/RESUME_PROTOCOL.md` / `docs/RESUME_PROTOCOL.zh-CN.md`：中断恢复和检查点要求。
- `docs/`：GitHub 公开使用和维护文档。

## 避免 Skill 膨胀

`SKILL.md` 已经很大。详细内容优先放到 reference 或 docs，再从 `SKILL.md` 链接过去。

只有“skill 触发后必须马上看到”的规则才放进 `SKILL.md`。

## 发布流程

1. 判断改动属于工作流规则、实现示例还是公开文档。
2. 修改最小相关文件。
3. 搜索是否有矛盾规则。
4. 确认中断续做协议仍然阻止重复破坏性操作。
5. 运行密钥扫描。
6. 运行辅助脚本 smoke test。
7. 如使用 GitHub releases，更新发布说明。

## 兼容性审查

合并前检查：

- Codex 能否执行？
- Claude 能否从本地文件执行？
- Trae/Cursor/OpenHands/Aider 能否在不依赖 Codex 专属 API 的情况下执行？
- 是否避免假设某一种浏览器工具或操作系统？
- live automation 被阻塞时有没有 fallback？
- 服务器错误、浏览器崩溃、上下文压缩或网络失败后，能否安全续做？

## 安全审查

拒绝以下改动：

- 鼓励保存凭据。
- 鼓励危险支付或结账逻辑。
- 跳过产品/媒体保护。
- 静默跳过文章生成。
- 允许 QA 前上线。
- 中断后不做只读恢复检查就重复破坏性操作。
- 创建大块不可理解代码。
- 依赖某个客户的私有数据。
