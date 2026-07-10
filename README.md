# WordPress Auto Site Builder Skill

[中文 README](README.zh-CN.md) | [Documentation Index](docs/DOCUMENTATION_INDEX.md)

A universal AI-agent workflow for building, rebuilding, and repairing WordPress/WooCommerce SEO sites with a lightweight, auditable stack:

- Hello Elementor theme
- Elementor HTML widgets for page-specific layout
- Code Snippets for PHP hooks, settings writers, global shell, and scoped UI behavior
- WooCommerce for store flow
- Rank Math for SEO metadata, sitemap, schema, and indexing preparation

The skill is designed for Codex, Claude Code, Cursor, Devin Desktop/Windsurf, GitHub Copilot, Gemini Code Assist, Qwen Code, Trae, Tongyi Lingma, Qoder, Baidu Comate, CodeGeeX, MarsCode, Tencent CodeBuddy, OpenHands, Aider, Cline/Roo/Kilo, and other AI coding agents that can read repository files, edit text, operate a browser, call WordPress REST APIs, and report verification evidence.

## What It Covers

- New WordPress/WooCommerce site builds
- Old-site rebuilds that preserve products and media
- Existing-site full SEO optimization without redesigning or rebuilding pages
- Reference-site inspired builds that capture public/authorized HTML snapshots for transformed WordPress implementation
- Full-store page architecture
- Homepage, policy pages, product pages, product archives, blog archives, single posts, cart, checkout, and account pages
- Autonomous mode and ask-user mode
- Cross-agent compatibility and anti-skip rules for major domestic and international AI coding tools
- Critical-judgment rules so agents do not blindly agree with risky or wrong user instructions
- Country/language-specific design variation
- Open-source-inspired frontend UI aesthetic system: design tokens, polished header/footer/mobile drawer, ecommerce component standards, and visual QA gates before page HTML
- Strict global-shell-first order: Code Snippets header/footer/menu, Additional CSS global styles, global JS, and dynamic renderers must be verified before production Elementor page HTML
- Clean Elementor canvas rule: clear default layouts, placeholder sections, stale generated widgets, and duplicates before adding the intended page HTML widget
- SEO article batch generation
- WooCommerce product CSV rewriting and import integrity, including intelligent product name, short description, long description/body, image text, and Rank Math metadata rewrites aligned with target language, market design style, brand replacement, payment/shipping facts, currency, and SEO strategy instead of translation-only or repeated source-copy patterns. Brand replacement never rewrites image URLs, and remote images must be localized and served as WebP before final use.
- Product knowledge ledger before homepage/page HTML, article plans, and Rank Math SEO generation
- Product price currency conversion for localized/small-language WooCommerce sites
- Official WooCommerce CSV custom metadata inspection, including protected runtime meta and editable SEO meta
- Logo plus separate favicon/site icon generation and verification
- Header/footer background-aware logo variants so generated logos do not appear as mismatched pasted boxes
- Rank Math metadata and schema
- Code Snippets implementation rules
- Interaction QA for buttons, menus, forms, quantity controls, cart, and checkout
- Launch gate enforcement

## Execution Modes

Every project starts by identifying the service mode:

1. `new`: new site build.
2. `old_rebuild`: old-site rebuild preserving protected products and media.
3. `existing_seo_optimization`: existing-site SEO optimization only. This mode inventories and improves current pages, products, posts, categories, Rank Math metadata, schema, sitemap, media ALT text, and internal links without rebuilding layouts or changing commerce settings.

`ask_user` is the default mode. The agent asks before major design, SEO, deletion, plugin, payment, shipping, publishing, or launch decisions.

`autonomous` is allowed only when the user explicitly authorizes no-question execution. The agent can decide market, language, layouts, articles, menus, policies, and non-destructive implementation details from available facts, but it still must preserve protected data, verify every step, and report decisions.

## Non-Negotiable Rules

- Do not delete products, product categories, product tags, product attributes, or media unless explicitly authorized.
- Do not enter launch/indexing mode until product pages, archives, articles, SEO, and full QA pass.
- Do not ship pages with button, text, grid, image, or layout overflow.
- Do not ship buttons or controls that are blocked, frozen, hidden, or unclickable.
- Do not hardcode secrets, tokens, credentials, private endpoints, or payment keys.
- Do not create a custom theme or large plugin unless the user explicitly asks for that architecture.
- Do not dump a large unmaintainable codebase into Code Snippets.
- Do not blindly follow user instructions that would break checkout, delete protected data, skip product understanding, copy protected content, create false claims, or launch before QA.

## Quick Start for AI Agents

1. Read [`SKILL.md`](SKILL.md).
2. Read only the relevant reference files:
   - [`references/intake-checklist.md`](references/intake-checklist.md)
   - [`references/phase-playbook.md`](references/phase-playbook.md)
   - [`references/ai-agent-compatibility.md`](references/ai-agent-compatibility.md) for cross-tool adaptation and anti-skip rules
   - [`references/qa-and-launch.md`](references/qa-and-launch.md)
   - [`references/frontend-ui-aesthetic-system.md`](references/frontend-ui-aesthetic-system.md) for UI tokens, header/footer quality, component standards, and visual QA
   - [`references/product-csv-originality-seo.md`](references/product-csv-originality-seo.md) for CSV work
   - [`references/reference-site-capture.md`](references/reference-site-capture.md) for clone-style/reference-site builds
   - [`references/code-snippets-implementation-guide.md`](references/code-snippets-implementation-guide.md) for snippets
   - [`references/woocommerce-customizations-guide.md`](references/woocommerce-customizations-guide.md) for store UX
3. Build a site ledger with mode, protected data, required pages, snippets, SEO tasks, articles, and QA gates.
4. Execute step by step.
5. Verify with real browser or API evidence.
6. Produce a final report only after QA and launch gates pass.

## Resuming Interrupted Work

If an AI run stops unexpectedly, read [`docs/RESUME_PROTOCOL.md`](docs/RESUME_PROTOCOL.md) before continuing. Resume from the last verified checkpoint after a read-only live-state check. Do not repeat destructive cleanup, product imports, article publishing, snippet replacement, or launch/indexing actions automatically.

## Repository Layout

```text
wordpress-auto-site-builder/
  SKILL.md
  agents/openai.yaml
  references/
  scripts/
  docs/
  .github/
```

## Documentation

- Chinese README: [`README.zh-CN.md`](README.zh-CN.md)
- Installation: [`INSTALL.md`](INSTALL.md) / [`INSTALL.zh-CN.md`](INSTALL.zh-CN.md)
- Documentation index: [`docs/DOCUMENTATION_INDEX.md`](docs/DOCUMENTATION_INDEX.md) / [`docs/DOCUMENTATION_INDEX.zh-CN.md`](docs/DOCUMENTATION_INDEX.zh-CN.md)
- AI tool compatibility: [`docs/AI_TOOL_COMPATIBILITY.md`](docs/AI_TOOL_COMPATIBILITY.md) / [`docs/AI_TOOL_COMPATIBILITY.zh-CN.md`](docs/AI_TOOL_COMPATIBILITY.zh-CN.md)
- Resume protocol: [`docs/RESUME_PROTOCOL.md`](docs/RESUME_PROTOCOL.md) / [`docs/RESUME_PROTOCOL.zh-CN.md`](docs/RESUME_PROTOCOL.zh-CN.md)
- GitHub publishing: [`docs/GITHUB_PUBLISHING.md`](docs/GITHUB_PUBLISHING.md) / [`docs/GITHUB_PUBLISHING.zh-CN.md`](docs/GITHUB_PUBLISHING.zh-CN.md)
- Contributing: [`CONTRIBUTING.md`](CONTRIBUTING.md) / [`CONTRIBUTING.zh-CN.md`](CONTRIBUTING.zh-CN.md)
- Security: [`SECURITY.md`](SECURITY.md) / [`SECURITY.zh-CN.md`](SECURITY.zh-CN.md)
- Support: [`SUPPORT.md`](SUPPORT.md) / [`SUPPORT.zh-CN.md`](SUPPORT.zh-CN.md)
- Code of conduct: [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) / [`CODE_OF_CONDUCT.zh-CN.md`](CODE_OF_CONDUCT.zh-CN.md)
- Roadmap: [`ROADMAP.md`](ROADMAP.md) / [`ROADMAP.zh-CN.md`](ROADMAP.zh-CN.md)
- Changelog: [`CHANGELOG.md`](CHANGELOG.md) / [`CHANGELOG.zh-CN.md`](CHANGELOG.zh-CN.md)

## Helper Scripts

Generate a build plan and launch-gate checklist:

```bash
python scripts/site_plan.py docs/SITE_CONFIG_EXAMPLE.json
python scripts/site_plan.py docs/SITE_CONFIG_EXAMPLE.json --format json
python scripts/site_plan.py docs/SITE_CONFIG_EXISTING_SEO_EXAMPLE.json
python scripts/site_plan.py docs/SITE_CONFIG_REFERENCE_CLONE_EXAMPLE.json
```

Inspect a WooCommerce product CSV for identity fields, image/gallery columns, inline body images, variations, Rank Math fields, and import blockers:

```bash
python scripts/inspect_product_csv.py docs/SAMPLE_PRODUCT_IMPORT.csv
```

Convert product prices before import when source and target currencies differ:

```bash
python scripts/convert_product_prices.py docs/SAMPLE_PRODUCT_IMPORT.csv --output products-converted.csv --source-currency USD --target-currency EUR --rate 0.92 --rate-source "manual/runtime checked" --rate-timestamp "2026-07-09T12:00:00Z"
```

Capture public reference-site HTML snapshots for local layout analysis:

```bash
python scripts/reference_site_capture.py https://example.com --max-pages 40
```

Create and update a resumable ledger for interrupted AI runs:

```bash
python scripts/resume_ledger.py init build-ledger.json --brand "Example Brand" --domain example.com
python scripts/resume_ledger.py event build-ledger.json --type checkpoint --message "Pages created" --phase create_and_bind_pages --gate pages_created
python scripts/resume_ledger.py recovery build-ledger.json
```

Audit Rank Math on-page SEO checks and generate a Code Snippets one-time writer:

```bash
python scripts/rank_math_content_audit.py docs/SAMPLE_RANK_MATH_META_MAP.json
python scripts/rank_math_meta_writer.py docs/SAMPLE_RANK_MATH_META_MAP.json --output rank-math-writer.php
```

Scan for obvious secrets before publishing:

```bash
python scripts/secret_scan.py .
```

## Open Source Status

This repository is intended to be portable and tool-neutral. Tool-specific adapters are welcome, but core rules should remain vendor-neutral.
