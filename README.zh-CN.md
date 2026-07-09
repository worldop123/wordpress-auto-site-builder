# WordPress Auto Site Builder Skill

这是一个通用 AI Agent 工作流，用来搭建、重建、修复和优化 WordPress/WooCommerce SEO 网站。它适配 Codex、Claude、Trae、Cursor、OpenHands、Aider 等 AI 编程工具，只要工具可以读取文件、编辑文本、操作浏览器或调用 WordPress REST API，就可以按本 skill 执行。

## 技术栈约束

- 主题依赖：Hello Elementor。
- 页面搭建：Elementor HTML 小工具，每个页面只放页面专属 HTML/CSS/JS。
- 功能实现：Code Snippets 插件承载 PHP hooks、一次性设置写入器、全局页眉页脚、局部交互 JS/CSS。
- 电商流程：WooCommerce。
- SEO：Rank Math，包含 metadata、sitemap、schema、robots/noindex、文章和产品 SEO。

除非用户明确要求，不创建自定义主题、大型插件或不可维护的大工程代码。

## 第一件事：选择服务模式

每次 WordPress 项目开始时，必须先确认客户要哪一种服务：

1. `new`：新站搭建。
2. `old_rebuild`：旧站重建，保留受保护的产品、分类、属性、媒体库。
3. `existing_seo_optimization`：现有网站全盘 SEO 优化，不重做页面、不替换布局，只优化现有页面、产品、博客、分类、媒体 ALT、Rank Math 数据、schema、sitemap、内链和内容缺口。

`ask_user` 模式下必须把这三项列给用户选择；`autonomous` 模式下可以根据用户描述自动判断，但要写入台账。

## 能做什么

- 新 WordPress/WooCommerce SEO 站点搭建。
- 旧站重建并保护产品和媒体库。
- 现有网站全盘 SEO 优化，不改页面视觉结构。
- 首页、政策页、产品页、产品归档、博客归档、单篇文章、购物车、结账、账户页重构。
- 国家/语言/市场差异化设计，避免千篇一律。
- SEO 文章批量生成、草稿、定时发布规划。
- WooCommerce 产品 CSV 改写、图库、正文图片、变体和 Rank Math 字段完整性检查。
- WooCommerce 官方导出 CSV 自定义元数据精细识别，区分受保护运行时 meta 和可编辑 SEO meta。
- 生成网站 logo 时同步生成并配置独立 favicon/site icon，检查小尺寸清晰度。
- logo 必须适配真实页眉/页脚背景，不能在深色页脚上出现突兀白底块或像截图贴上去。
- Rank Math Free 通过 Code Snippets 一次性写入器批量设置 SEO 标题、描述、关键词、robots 和 taxonomy SEO 数据。
- 按钮、菜单、表单、数量加减、购物车、结账、移动端溢出和卡死问题 QA。
- 中断续做、上线门禁、开源发布前密钥扫描。

## 执行模式

`ask_user` 是默认模式。AI 在设计、SEO、删除、插件安装、支付、物流、发布、上线前必须询问用户。

`autonomous` 只有在用户明确授权“不用询问/全自动执行”时才能启用。AI 可以自主决定目标市场、语言、布局、文章、菜单、政策和非破坏性实现细节，但仍必须保护产品/媒体、记录决策、验证每一步并输出报告。

## 硬性规则

- 未经授权，不删除产品、产品分类、产品标签、产品属性和媒体库。
- 页面、产品、归档、文章、SEO 和完整 QA 没完成前，不进入上线/索引模式。
- 页面不能有按钮、文字、网格、图片或布局溢出。
- 按钮和控件不能被遮挡、卡死、隐藏或无法点击。
- 购物车页和产品页数量加减必须可点击、不卡死、不破坏 WooCommerce 原生事件。
- 不硬编码密钥、token、账号密码、私有接口或支付密钥。
- 一次性 Rank Math 写入器执行并验证后必须禁用或删除。
- AI 中断后必须先读台账和线上状态，再从最小安全步骤续做。

## 快速开始

```bash
python scripts/site_plan.py docs/SITE_CONFIG_EXAMPLE.json
python scripts/site_plan.py docs/SITE_CONFIG_EXAMPLE.json --format json
python scripts/site_plan.py docs/SITE_CONFIG_EXISTING_SEO_EXAMPLE.json
```

检查 WooCommerce 产品 CSV：

```bash
python scripts/inspect_product_csv.py docs/SAMPLE_PRODUCT_IMPORT.csv
```

创建或更新中断续做台账：

```bash
python scripts/resume_ledger.py init build-ledger.json --brand "Example Brand" --domain example.com
python scripts/resume_ledger.py event build-ledger.json --type checkpoint --message "Pages created" --phase create_and_bind_pages --gate pages_created
python scripts/resume_ledger.py recovery build-ledger.json
```

审计 Rank Math 页面 SEO 并生成 Code Snippets 一次性写入器：

```bash
python scripts/rank_math_content_audit.py docs/SAMPLE_RANK_MATH_META_MAP.json
python scripts/rank_math_meta_writer.py docs/SAMPLE_RANK_MATH_META_MAP.json --output rank-math-writer.php
```

发布到 GitHub 前扫描明显密钥：

```bash
python scripts/secret_scan.py .
```

## 目录结构

```text
wordpress-auto-site-builder/
  SKILL.md
  references/
  scripts/
  docs/
  agents/
  .github/
```

## 中断续做

如果 AI 工具因为服务器错误、上下文限制、浏览器崩溃、网络失败或用户暂停而中断，继续前必须读取 `docs/RESUME_PROTOCOL.zh-CN.md`。只能从最后一个已验证检查点继续，不能盲目重复旧站清理、产品导入、文章发布、snippet 替换或上线索引操作。
