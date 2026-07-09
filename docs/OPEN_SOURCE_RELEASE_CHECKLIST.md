# Open Source Release Checklist

Use this before publishing the skill to GitHub.

## Repository Hygiene

- [ ] No WordPress passwords.
- [ ] No WordPress application passwords.
- [ ] No GitHub tokens.
- [ ] No API keys or payment secrets.
- [ ] No browser cookies, sessions, or storage-state files.
- [ ] No customer data, order exports, or private product supplier sheets.
- [ ] No client-specific claims that should not be public.
- [ ] `.uploads/`, exports, backups, and local screenshots are excluded.

## Documentation

- [ ] `README.md` explains purpose, stack, modes, and quick start.
- [ ] `INSTALL.md` explains installation for Codex and generic AI tools.
- [ ] `CONTRIBUTING.md` explains PR rules.
- [ ] `SECURITY.md` explains vulnerability and secret policy.
- [ ] `LICENSE` is present.
- [ ] `docs/AI_TOOL_COMPATIBILITY.md` explains multi-agent usage.
- [ ] `references/ai-agent-compatibility.md` explains anti-skip behavior, capability fallbacks, and critical-judgment rules for domestic and international AI coding tools.
- [ ] `docs/RESUME_PROTOCOL.md` explains interruption recovery.
- [ ] `TRAE_CN_USAGE.md` is readable and generic.

## Skill Integrity

- [ ] `SKILL.md` frontmatter has valid `name` and `description`.
- [ ] The description mentions major triggers and supported workflow.
- [ ] References are linked from `SKILL.md`.
- [ ] No reference contradicts autonomous/ask-user mode.
- [ ] No reference contradicts the interruption resume protocol.
- [ ] No reference allows launch before articles, products, pages, SEO, and QA are complete.
- [ ] No reference allows page HTML, article planning, or Rank Math SEO generation before product CSV/live product understanding.
- [ ] No reference allows production Elementor page HTML generation/import before global header, footer/menu, Additional CSS, global JS, and dynamic renderers are active and verified.
- [ ] CSV product rewriting rules require intelligent rewriting of product names, short descriptions, long descriptions/body content, editable image text, and Rank Math fields using target market/language, single-language or multilingual strategy, design/content tone, brand replacements, payment/shipping facts, and currency; no rule permits translation-only, synonym-only, mixed-language fields, currency mistakes, unsupported commerce promises, or repeated original CSV copy patterns.
- [ ] No reference tells agents to blindly agree with risky user instructions; risky requests require pros/cons, safer alternatives, and confirmation or a safe autonomous choice.
- [ ] No snippet guide recommends unsafe global DOM loops or unverified auto-submit.
- [ ] Rank Math Free workflow uses content-aware audit plus Code Snippets one-time writer, not unavailable CSV SEO import.

## WordPress Build Rules

- [ ] Fixed stack is documented: Hello Elementor, Elementor, WooCommerce, Code Snippets, Rank Math.
- [ ] Full store surface is required: home, custom pages, products, product archives, blog archives, single posts, cart, checkout, account, policies.
- [ ] Global shell ordering is explicit: Code Snippets header/footer/menu first, global CSS in Additional CSS, global JS in Code Snippets, dynamic renderers, then page HTML one page at a time.
- [ ] Elementor page HTML rules require clearing default/old layouts, placeholder sections, old generated widgets, and duplicate widgets before adding the intended HTML widget.
- [ ] CSV import integrity covers featured images, galleries, body images, long descriptions, variations, attributes, and Rank Math fields.
- [ ] CSV rewrite reports include localization strategy, design-content alignment, commerce trust strategy, brand replacement strategy, naming strategy, description strategy, SEO strategy, uniqueness checks, and any customer-facing source copy intentionally preserved.
- [ ] Brand replacement rules explicitly protect image URLs, inline `<img src>`, media attachment IDs, CDN paths, and download URLs from string replacement.
- [ ] Official WooCommerce CSV parsing prefers double-quote-safe Excel/RFC parsing and validates `Images`, `Parent`, `Position`, and `Meta:` columns before rewriting.
- [ ] Remote image URLs from CSV/imports are localized into Media Library or an approved CDN/media pipeline before launch, and all used images are converted/served as WebP.
- [ ] Product knowledge ledger is required before homepage preview, page HTML, article planning, image ALT planning, and Rank Math metadata.
- [ ] Custom metadata policy distinguishes editable Rank Math/Yoast SEO fields from protected runtime, analytics, serialized, or unknown meta fields.
- [ ] Logo generation also requires a separate verified site icon/favicon configured in WordPress Site Identity.
- [ ] Initial SEO article batch is required unless the user opts out.
- [ ] Buttons, links, forms, quantity controls, menus, filters, and checkout must be interaction-tested.
- [ ] Resume ledger requirements cover WordPress IDs, snippets, product imports, articles, QA checks, and temporary credentials.
- [ ] Rank Math generated writer PHP files are temporary artifacts and are not committed.

## Validation

- [ ] Run a secret scan.
- [ ] Run helper script smoke tests.
- [ ] Check Markdown links where practical.
- [ ] Review docs from the perspective of a new AI agent with no prior context.
