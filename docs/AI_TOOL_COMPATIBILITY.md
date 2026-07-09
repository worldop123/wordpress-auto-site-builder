# AI Tool Compatibility

This skill is tool-neutral. It should work with any AI coding agent that can read files and operate WordPress through browser automation, REST APIs, or user-guided manual steps.

For the full compatibility contract, anti-skip protocol, capability fallback matrix, and critical-judgment rules, read [`../references/ai-agent-compatibility.md`](../references/ai-agent-compatibility.md).

## Supported Agent Patterns

| Tool family | Recommended use |
|---|---|
| Codex | Install under `.codex/skills`, then trigger with `$wordpress-auto-site-builder`. |
| Claude | Attach or reference this folder, then ask Claude to read `SKILL.md` and task-relevant references. |
| Trae | Add this folder as a skill/reference package and use `TRAE_CN_USAGE.md` for Chinese startup guidance. |
| Cursor | Add as project context or docs, then point the agent to `SKILL.md`. |
| OpenHands | Mount this repository and ask the agent to read the workflow references before acting. |
| Aider | Use as a repository reference; ask Aider to edit only skill files or generated artifacts, not live secrets. |
| Domestic/international IDE agents | For Qwen Code, Tongyi Lingma, Qoder, Baidu Comate, CodeGeeX, MarsCode, Tencent CodeBuddy, Gemini Code Assist, GitHub Copilot, Devin Desktop/Windsurf, Cline/Roo/Kilo, and similar tools, use the same phase gates and fallback matrix in `references/ai-agent-compatibility.md`. |

## Minimum Agent Capabilities

- Read local files.
- Edit Markdown and script files.
- Run helper scripts when needed.
- Use browser automation or guide the user through WordPress admin.
- Use REST APIs when credentials are available.
- Keep secrets out of files and logs.
- Report verification evidence.

## Universal Startup Prompt

```text
Use the wordpress-auto-site-builder skill in this repository.
First read SKILL.md, then read only the reference files needed for my task.
Use autonomous mode only if I explicitly authorize it; otherwise use ask-user mode.
Keep products/media protected, implement through Hello Elementor + Elementor HTML + Code Snippets, and do not enter launch mode until pages, products, articles, SEO, and full QA pass.
Start by asking which service mode I need: new site build, old-site rebuild, or existing-site SEO optimization. If I choose existing-site SEO optimization, do not rebuild pages; inventory current content and update SEO data only.
```

## Tool-Specific Notes

- If a tool cannot control a browser, it should generate exact WordPress REST/API operations or manual admin steps instead of pretending live changes were made.
- If a tool cannot execute scripts, it should still follow the reference checklists and produce artifacts for the user.
- If a tool cannot safely store credentials, use user-guided login or short-lived application passwords and revoke them after use.
- If a tool cannot run full QA, it must mark the missing checks as blockers instead of claiming launch readiness.
- If a tool cannot read or inspect the product CSV/live products, it must not generate homepage HTML, page copy, article topics, image ALT plans, or Rank Math SEO metadata.
- If a user request is risky or likely wrong, the agent must explain benefits, risks, and safer alternatives before acting. It must not blindly agree with requests that break checkout, delete protected data, skip QA, copy protected content, hardcode secrets, or launch early.
