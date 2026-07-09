# AI 工具兼容说明

这个 skill 是工具无关的。任何能读取文件、编辑文本、操作浏览器、调用 WordPress REST API，或能引导用户在后台手动操作的 AI 编程工具都可以使用。

## 支持的工具形态

| 工具 | 推荐方式 |
|---|---|
| Codex | 放到 `.codex/skills`，用 `$wordpress-auto-site-builder` 触发。 |
| Claude | 将本文件夹作为上下文或附件，要求 Claude 先读 `SKILL.md` 和相关 references。 |
| Trae | 作为 skill/reference 包导入，中文启动可看 `TRAE_CN_USAGE.md`。 |
| Cursor | 作为项目文档或上下文，要求 Agent 指向 `SKILL.md`。 |
| OpenHands | 挂载本仓库，先读工作流 references 再执行。 |
| Aider | 作为仓库参考，只编辑 skill 文件或生成物，不写入 live secrets。 |

## 最小能力要求

- 能读取本地文件。
- 能编辑 Markdown 和脚本文件。
- 必要时能运行辅助脚本。
- 能通过浏览器自动化、REST API 或用户引导方式操作 WordPress。
- 能避免把密钥写入文件和日志。
- 能报告验证证据。

## 通用启动提示

```text
请使用本仓库里的 wordpress-auto-site-builder skill。
先读取 SKILL.md，再只读取当前任务需要的 reference 文件。
第一步请先列出三种服务模式让我选择：新站搭建、旧站重建、现有网站 SEO 优化。
只有我明确授权时才使用 autonomous 模式，否则使用 ask_user 模式。
如果我选择现有网站 SEO 优化，不要重做页面，只盘点现有内容并更新 SEO 数据。
保护产品和媒体库，通过 Hello Elementor + Elementor HTML + Code Snippets 实现。
页面、产品、文章、SEO 和完整 QA 没通过前，不允许进入上线模式。
```

## 工具差异处理

- 如果工具不能控制浏览器，应输出准确 REST/API 操作或后台手动步骤，不能假装已完成 live changes。
- 如果工具不能执行脚本，仍必须遵守 references 清单并生成交付物。
- 如果工具不能安全存储凭据，应使用用户引导登录或短期 Application Password，并在使用后撤销。
- 如果工具不能完成完整 QA，必须把缺失检查标为 blocker，不能声称 ready to launch。
