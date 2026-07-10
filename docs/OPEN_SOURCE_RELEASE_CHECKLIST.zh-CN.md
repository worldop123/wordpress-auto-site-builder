# 开源发布检查清单

发布到 GitHub 前使用本清单。

## 仓库卫生

- [ ] 没有 WordPress 密码。
- [ ] 没有 WordPress Application Password。
- [ ] 没有 GitHub token。
- [ ] 没有 API key 或支付密钥。
- [ ] 没有浏览器 cookie、session 或 storage-state 文件。
- [ ] 没有客户数据、订单导出、供应商私有表格或未脱敏产品资料。
- [ ] 没有不应公开的客户专属声明。
- [ ] `.uploads/`、exports、backups、本地截图和临时 writer PHP 已被排除。

## 文档

- [ ] `README.md` 和 `README.zh-CN.md` 存在。
- [ ] `INSTALL.md` 和 `INSTALL.zh-CN.md` 存在。
- [ ] `CONTRIBUTING.md` 和 `CONTRIBUTING.zh-CN.md` 存在。
- [ ] `SECURITY.md` 和 `SECURITY.zh-CN.md` 存在。
- [ ] `LICENSE` 存在。
- [ ] AI 工具兼容文档有中英文版本。
- [ ] `references/ai-agent-compatibility.md` 覆盖国内外 AI 编程工具的防跳步骤、能力回退和风险判断规则。
- [ ] 中断续做协议有中英文版本。
- [ ] `TRAE_CN_USAGE.md` 可读且不只绑定 Trae。

## Skill 完整性

- [ ] `SKILL.md` frontmatter 有合法 `name` 和 `description`。
- [ ] description 覆盖新站搭建、旧站重建、现有站 SEO 优化、CSV、Rank Math、Code Snippets、QA、断点续做。
- [ ] references 能从 `SKILL.md` 找到。
- [ ] 没有文档和 `autonomous`/`ask_user` 模式冲突。
- [ ] 没有文档和中断续做协议冲突。
- [ ] 没有文档允许在文章、产品、页面、SEO、QA 未完成前上线。
- [ ] 没有文档允许在未理解产品 CSV 或现有产品前生成页面 HTML、文章计划或 Rank Math SEO 数据。
- [ ] 没有文档允许在全局页眉、页脚/底部菜单、Additional CSS、全局 JS 和动态渲染器启用并验证前生成或导入生产 Elementor 页面 HTML。
- [ ] 没有文档允许在读取 `frontend-ui-aesthetic-system.md` 并记录设计 token、页眉/页脚审美通过、页面审美通过前生成生产页面 HTML。
- [ ] 产品 CSV 改写规则要求结合目标市场/语言、单语言或多语言策略、设计/内容风格、品牌替换、支付/物流事实和币种，智能重写产品名、短描述、长正文/正文内容、可编辑图片文字和 Rank Math 字段；不允许只翻译、只换同义词、字段混用多语言、币种错误、无依据交易承诺或沿用原 CSV 的重复文案套路。
- [ ] 没有文档要求 AI 盲目认同高风险用户指令；高风险请求必须列出好坏、替代方案，并询问确认或选择安全路径。
- [ ] 现有网站 SEO 优化模式不会重做页面、替换布局或改动商品交易数据。
- [ ] Rank Math 免费版流程使用内容审计 + Code Snippets 一次性写入器，不假装能完整 CSV 导入所有 SEO 数据。

## WordPress 建站规则

- [ ] 固定技术栈写清楚：Hello Elementor、Elementor、WooCommerce、Code Snippets、Rank Math。
- [ ] 全店页面覆盖：主页、自定义页、产品、产品归档、博客归档、单篇文章、购物车、结账、账户、政策页。
- [ ] 全局壳顺序写清楚：先用 Code Snippets 做页眉/页脚/菜单，再把全局 CSS 放到 Additional CSS，再用 Code Snippets 做全局 JS 和动态渲染器，最后才逐页导入页面 HTML。
- [ ] 前端 UI 审美顺序写清楚：先定义设计 token/共享组件，再完成高质量页眉/页脚/移动菜单，最后做页面专属 Elementor HTML，并在完成前做视觉 QA。
- [ ] Elementor 页面 HTML 规则要求添加 HTML 区块前先清空默认/旧布局、占位 section、旧生成 widget 和重复 widget。
- [ ] CSV 导入完整性覆盖特色图、图库、正文图片、长描述、变体、属性和 Rank Math 字段。
- [ ] CSV 改写报告必须包含本地化策略、设计内容对齐、交易信任策略、品牌替换策略、命名策略、描述策略、SEO 策略、唯一性检查，以及被刻意保留的客户可见源文案说明。
- [ ] 品牌替换规则明确保护图片 URL、内联 `<img src>`、媒体附件 ID、CDN 路径和下载 URL，不能做字符串替换。
- [ ] WooCommerce 官方 CSV 解析优先使用支持双引号转义的 Excel/RFC 解析，并验证 `Images`、`Parent`、`Position`、`Meta:` 列。
- [ ] CSV/导入中的远程图片 URL 上线前必须本地化到媒体库或明确批准的 CDN/媒体管线，且所有使用中的图片必须转换或输出为 WebP。
- [ ] 产品知识台账必须先于首页预览、页面 HTML、文章计划、图片 ALT 规划和 Rank Math 元数据生成。
- [ ] 自定义元数据策略区分可编辑 Rank Math/Yoast SEO 字段和受保护 runtime、analytics、序列化或未知 meta 字段。
- [ ] 生成 logo 时也必须生成独立 favicon/site icon，并在 WordPress Site Identity 配置。
- [ ] 除非用户明确不要，否则初始 SEO 文章批次是必需的。
- [ ] 按钮、链接、表单、数量控件、菜单、筛选、结账都必须交互测试。
- [ ] 续做台账覆盖 WordPress IDs、snippets、产品导入、文章、QA 检查和临时凭据。
- [ ] Rank Math 生成的 writer PHP 是临时产物，不能提交。

## 验证

- [ ] 运行密钥扫描。
- [ ] 运行辅助脚本 smoke test。
- [ ] 尽量检查 Markdown 链接。
- [ ] 从“没有历史上下文的新 AI Agent”视角审一遍文档。
