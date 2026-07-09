# 更新日志

所有重要项目变更都应记录在这里。

## [未发布]

- 强制全局壳优先建站顺序：Code Snippets 页眉/页脚/菜单、Additional CSS 全局样式、全局 JS 和动态渲染器必须先启用并验证，之后才能做生产 Elementor 页面 HTML。
- 要求 WooCommerce 产品 CSV 智能改写产品名、短描述、长正文/正文内容、可编辑图片文字和 Rank Math 字段；明确把只翻译和沿用原 CSV 重复文案套路列为 blocker。
- 将产品 CSV 改写绑定到目标国家/语言、单语言或多语言策略、设计/内容风格、品牌替换规则、支付/物流事实、币种和本地化交易信任信息。
- 品牌名替换时保护图片 URL 不被替换，并要求远程图片本地化到媒体库或批准的媒体管线后，再转换或输出为 WebP 使用。
- 增加 GitHub 社区健康文档、CI、文档索引、支持说明、路线图和发布指南。
- 增加仿站/参考站捕获流程，包括本地 HTML 快照保存、页面类型 manifest 生成、WordPress/WooCommerce 差异化重构规则。
- 增加本地化 WooCommerce 产品导入价格货币转换流程，包括原始价格备份 meta 列和汇率台账要求。
- 增加产品知识前置门槛：创建首页预览、页面 HTML、文章计划和 Rank Math SEO 数据前，必须先检查 CSV 或现有产品并形成产品知识台账。

## [0.1.0] - 2026-07-09

- 首次开源发布 `wordpress-auto-site-builder`。
- 增加适配 Codex、Claude、Trae、Cursor、OpenHands、Aider 等工具的通用 AI Agent 工作流。
- 增加三种服务模式：新站搭建、旧站重建、现有站 SEO 优化。
- 增加 Rank Math Free 内容感知 SEO 数据一次性写入器流程。
- 增加 WooCommerce 官方 CSV 检查：产品、变体、媒体图库和自定义元数据。
- 增加 logo、favicon/site icon、页眉页脚背景匹配和交互 QA 规则。
- 增加中英文文档。
- 增加通用 AI 编程工具适配指南，包括防跳步骤协议、能力缺失回退矩阵，以及“不能盲从用户”的风险判断规则。
- 收紧流程一致性：在 `SKILL.md` 标准流程和阶段门禁中明确要求产品知识台账必须先于首页预览和内容生成。
