# 通用 AI 工具使用说明

这个 skill 不是只给 Trae 使用。它可以给 Codex、Claude、Trae、Cursor、OpenHands、Aider 以及其他能读取文件和操作浏览器/REST API 的 AI 编程工具使用。

## 推荐启动方式

让 AI 先读取：

- `SKILL.md`
- `references/intake-checklist.md`
- `references/phase-playbook.md`
- `references/qa-and-launch.md`

如果涉及产品 CSV，再读取：

- `references/product-csv-originality-seo.md`

如果涉及代码片段、按钮交互、购物车、结账或全局功能，再读取：

- `references/code-snippets-implementation-guide.md`
- `references/woocommerce-customizations-guide.md`

## 两种执行模式

- `autonomous`：用户明确授权后，AI 可以自主决定国家/语言、页面布局、文章主题、SEO 结构、菜单、政策内容和非破坏性实现细节。
- `ask_user`：默认模式。AI 在设计、删除、插件、支付、物流、发布和上线前询问用户。

无论哪种模式，都不能跳过备份、产品保留、QA、上线死规则和安全规则。

## 固定技术栈

- 主题：Hello Elementor
- 页面：Elementor HTML widget
- 功能：Code Snippets 插件中的 PHP hooks/snippets
- SEO：Rank Math
- 电商：WooCommerce

不要把大量业务逻辑散落到主题文件、自定义插件、Elementor 模板和 snippets 里。页面内容归页面，功能逻辑归 Code Snippets，设置归 WordPress/WooCommerce/Rank Math。

## 上线死规则

产品页、产品归档、分类归档、博客页、博客归档、单篇文章、购物车、结账、我的账户、政策页、初始文章批次没有完成并通过测试前，不能进入上线/索引/提交模式。

## 交互死规则

所有按钮、链接、菜单、数量加减、表单、弹窗、筛选、标签页、购物车更新和结账控件必须真实点击测试。不能有遮挡、卡死、重复刷新、不可点击、文本溢出或移动端横向滚动。

## 密钥规则

不要把 WordPress 密码、GitHub token、API key、支付密钥或任何私密信息写入文件、提交记录、截图、日志或最终报告。
