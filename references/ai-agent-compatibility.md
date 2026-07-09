# AI Agent Compatibility Layer

This skill must work across many AI coding tools, not only one desktop agent. The workflow therefore uses a portable execution contract that survives weak planning, context limits, missing tools, server interruptions, and agents that tend to skip steps.

## Supported Tool Families

Use this compatibility layer for:

- Terminal agents: OpenAI Codex CLI, Claude Code, Gemini CLI, Qwen Code, Aider, OpenCode/opencode, Roo Code, Cline, Kilo Code, and custom OpenAI-compatible CLI agents.
- IDE agents: Cursor, Devin Desktop/Windsurf, Trae, Qoder, JetBrains Junie, VS Code Copilot Agent Mode, Gemini Code Assist, Tongyi Lingma, Baidu Comate, CodeGeeX, MarsCode, Tencent CodeBuddy, Tabnine, and Sourcegraph Amp.
- Cloud or PR agents: GitHub Copilot coding agent, Devin, OpenHands, Replit Agent, CodeRabbit, Sweep-style maintenance agents, and GitHub issue-to-PR agents.
- Browser or low-code agents that can edit files, run commands, operate WordPress admin, or produce artifacts for manual paste.

The exact UI changes often. Follow this skill's workflow rather than a vendor-specific button path when they conflict.

## Universal Execution Contract

Every agent must follow this contract before claiming completion:

1. Read `SKILL.md` fully.
2. Read only the referenced files required by the task, but read each selected file fully.
3. Create or update a task ledger with service mode, interaction mode, current phase, completed steps, verification evidence, blockers, and next safe action.
4. Execute one phase at a time.
5. Verify before advancing.
6. Never treat generated code or written documentation as proof of live WordPress success.
7. Stop on launch blockers: broken WooCommerce bindings, frozen cart/quantity controls, missing products/articles, missing product knowledge ledger, unverified Rank Math data, broken checkout, mobile overflow, or untested snippets.
8. Resume from verified artifacts after interruption; never repeat destructive cleanup or imports blindly.

## Critical-Judgment Rule

The agent must not blindly agree with the user. User instructions can be incomplete, risky, contradictory, illegal, technically wrong, SEO-harmful, or commercially unsafe.

Before acting on a risky or unclear request, the agent must:

- Explain the issue plainly.
- List benefits, risks, and at least one safer alternative.
- Ask for confirmation in ask-user mode.
- In autonomous mode, choose the safest compliant path and record the decision.
- Refuse or stop if the request would expose secrets, break checkout, delete protected data, publish incomplete content, violate platform/legal rules, or create an obvious security/compliance risk.

Examples:

- If the user asks to delete products during an old-site rebuild, preserve products unless they explicitly authorize deletion after seeing the risk.
- If the user asks to launch before products, articles, Rank Math, and QA are complete, keep launch mode blocked.
- If the user requests copied third-party content or assets from a reference site, transform the layout only and do not publish copied protected material.
- If the user asks for SEO keyword stuffing or false product claims, explain why it is harmful and use useful compliant content instead.

## Anti-Skip Protocol

Some AI coding tools jump from requirement to code too quickly. Force this protocol:

- Start every run by printing the current phase and required gate.
- Before any write action, list the exact files, pages, snippets, settings, or WordPress objects that will be changed.
- After each write action, record verification evidence.
- If a required artifact is missing, mark the phase blocked instead of improvising.
- If the agent cannot run browser tests, REST API calls, or shell commands, it must output paste-ready artifacts plus a manual verification checklist.
- If the agent cannot read the product CSV, it must not generate homepage/page/SEO/blog content.
- If the agent cannot access WordPress, it must produce local deliverables only and say which live steps remain.

## Capability Fallback Matrix

| Capability | Preferred behavior | Fallback if missing |
|---|---|---|
| File editing | Patch scoped files and run tests | Generate exact patch or paste-ready file content |
| Shell commands | Run scripts, linters, secret scans, git checks | Provide commands and expected outputs for a manual runner |
| Browser/admin control | Verify WordPress front end and wp-admin changes | Produce manual QA checklist with URLs and expected states |
| Network access | Check current docs, rates, or tool behavior when time-sensitive | Ask user for source material or mark current-info verification pending |
| Long context | Read required references in chunks and maintain a ledger | Summarize verified state into a resume ledger before continuing |
| GitHub/PR access | Commit, push, and watch CI | Produce commit-ready diff and CI checklist |
| WordPress API access | Use REST/Woo APIs for structured changes | Use wp-admin/manual paste artifacts, but do not claim live completion |

## Portable Instruction Files

When publishing this skill into a repository, optionally mirror the core rules into tool-native instruction files:

- `AGENTS.md`: Codex, OpenAI-style agents, OpenHands, and many terminal/PR agents.
- `CLAUDE.md`: Claude Code project memory.
- `.cursor/rules/*.mdc`: Cursor project rules.
- `.windsurfrules`: Devin Desktop/Windsurf project rules.
- `.github/copilot-instructions.md`: GitHub Copilot and VS Code agent mode.
- `GEMINI.md`: Gemini CLI / Gemini Code Assist context.
- `QWEN.md`: Qwen Code context.
- `.clinerules`, `.roo/rules/`, or equivalent extension rule files for Cline/Roo/Kilo-style VS Code agents.

Keep these mirrors short. They should point back to `SKILL.md` and the `references/` files instead of duplicating the entire workflow.

## Tool-Specific Notes

- Codex: Prefer `AGENTS.md` plus direct repository files. Use shell tests, git status, and CI checks aggressively.
- Claude Code: Use `CLAUDE.md`, keep phase gates explicit, and require verification summaries to reduce skipped steps.
- Cursor: Use `.cursor/rules` for phase gates, product knowledge gate, launch blockers, and do-not-blindly-agree behavior.
- Devin Desktop/Windsurf: Use workspace rules and task ledgers because background agents may run asynchronously.
- GitHub Copilot coding agent: Convert tasks into issue/PR-sized phases; require branch diff, tests, and PR checklist before merge.
- Gemini Code Assist / Gemini CLI: Use `GEMINI.md` and explicit tool-permission checkpoints for agent mode.
- Qwen Code / Tongyi Lingma / Qoder / Trae / Baidu Comate / Tencent CodeBuddy / CodeGeeX / MarsCode: Write Chinese-friendly project rules when users work in Chinese; require the same ledger, CSV inspection, critical-judgment rule, and verification gates.
- Aider/OpenCode/Cline/Roo/Kilo: Keep tasks small, git-first, and test-driven; require the agent to show diffs before broader rewrites.

## Release Checklist for Universal Compatibility

- `SKILL.md` has no vendor-only assumptions.
- Core rules exist in `references/` and can be read by any agent.
- All scripts run with standard Python and no private local paths.
- Docs explain what to do when the agent lacks browser, shell, GitHub, or WordPress access.
- Chinese and English docs both mention language matching, autonomous vs ask-user mode, product knowledge gate, resume ledger, critical judgment, launch gate, and live QA.
- Adapter instructions or templates exist for major agent families when possible.
