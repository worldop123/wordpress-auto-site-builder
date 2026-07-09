# Changelog

All notable project changes should be recorded here.

## [Unreleased]

- Require intelligent WooCommerce product CSV rewriting for product names, short descriptions, long descriptions/body content, editable image text, and Rank Math fields; translation-only and repeated source-copy patterns are explicit blockers.
- Tie product CSV rewriting to target country/language, single-language or multilingual strategy, design/content tone, brand replacement rules, payment/shipping facts, currency, and localized commerce trust signals.
- Protect image URLs from brand-name replacement and require remote images to be localized into Media Library or an approved media pipeline, then converted/served as WebP before final use.
- Add GitHub community health files, CI, documentation index, support policy, roadmap, and publishing guide.
- Add reference-site capture / clone-style adaptation workflow, including local HTML snapshot capture, page-type manifest generation, and WordPress/WooCommerce transformation rules.
- Add product price currency conversion workflow for localized WooCommerce imports, including original-price backup meta columns and exchange-rate ledger requirements.
- Add a product knowledge gate requiring CSV/live product inspection before homepage previews, page HTML, article planning, and Rank Math SEO metadata generation.
- Add universal AI coding agent compatibility guidance, including anti-skip protocol, capability fallback matrix, and critical-judgment rules so agents do not blindly follow risky user instructions.
- Tighten workflow consistency so the product knowledge ledger is explicitly required before homepage previews/content generation in both `SKILL.md` and phase gates.

## [0.1.0] - 2026-07-09

- Initial open-source release of `wordpress-auto-site-builder`.
- Add universal AI-agent workflow for Codex, Claude, Trae, Cursor, OpenHands, Aider, and similar tools.
- Add service modes: new site build, old-site rebuild, and existing-site SEO optimization.
- Add Rank Math content-aware metadata writer workflow for Rank Math Free sites.
- Add WooCommerce official CSV inspection for products, variations, media galleries, and custom metadata.
- Add logo, favicon/site icon, header/footer background matching, and interaction QA rules.
- Add Chinese and English documentation.
