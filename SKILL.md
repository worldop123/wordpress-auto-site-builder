---
name: wordpress-auto-site-builder
description: Universal AI-agent workflow for building or repairing customizable WordPress/WooCommerce SEO sites using Hello Elementor, Elementor HTML blocks, Code Snippets PHP/CSS/JS, Rank Math, varied page designs, full-store QA, CSV product/media integrity, reference-site layout capture/adaptation, and autonomous or ask-user execution modes. Use with Codex, Claude, Trae, Cursor, OpenHands, Aider, or other AI coding agents when the user wants requirements intake, WordPress operation, old-site rebuilds, reference-site/clone-style builds, homepage/style previews, pages/products/categories/policies/blogs, product CSV originality rewriting, Rank Math metadata, non-repetitive layouts, snippet implementation, interaction testing, launch gating, or a reusable automated WordPress site-building workflow.
---

# WordPress Auto Site Builder

## Overview

Use this skill to act as an end-to-end WordPress site-building agent for simple but real WooCommerce sites where the visual layer is mostly Hello Elementor plus one Elementor HTML block per custom page, and functional behavior is implemented through Code Snippets and standard WordPress/WooCommerce data.

This skill is intentionally written for broad AI-agent portability. Codex, Claude, Trae, Cursor, OpenHands, Aider, and similar tools should be able to follow it as long as they can read files, operate a browser or REST API, edit text artifacts, and report verification evidence. Tool-specific files are optional adapters; the workflow rules remain the same.

The goal is not to reuse fixed content. Always turn brand, contact details, products, shipping, compliance, SEO keywords, design tone, language, and policies into inputs. Prefer a working storefront, clean mobile UX, dynamic products/posts, and verifiable purchase flow over cosmetic SEO-score chasing.

For multi-tool compatibility, read `references/ai-agent-compatibility.md` when adapting this skill to Codex, Claude Code, Cursor, Devin Desktop/Windsurf, GitHub Copilot, Gemini Code Assist, Qwen Code, Trae, Tongyi Lingma, Qoder, Baidu Comate, CodeGeeX, MarsCode, Tencent CodeBuddy, Cline/Roo/Kilo, Aider, OpenHands, Replit Agent, or other AI coding tools.

## CRITICAL: Language Matching

The agent MUST communicate in the user's language:

- If the user writes in Chinese, reply in Chinese for progress updates, questions, reports, and final answers.
- If the user writes in English, reply in English unless they ask for another language.
- If the user requests bilingual output, provide Chinese and English.
- Generated website content must use the target market language from `site_config`, not necessarily the chat language.
- GitHub/open-source documentation should include English and Chinese versions for public usability.

## CRITICAL: Fixed Technical Stack Contract

This skill builds WordPress/WooCommerce sites using a strict lightweight stack:

- **Theme dependency**: Hello Elementor.
- **Page builder dependency**: Elementor plugin.
- **Page content implementation**: Elementor HTML widgets containing page-specific HTML/CSS/JS only.
- **Functional implementation**: Code Snippets plugin using PHP hooks, shortcodes, settings writers, and scoped front-end JS/CSS when needed.
- **Do not create a custom theme, child theme, large plugin, or file-based application** unless the user explicitly asks for that different architecture.
- **Do not scatter business logic across theme files, Elementor templates, custom plugins, and snippets at the same time.** Keep the implementation ledger clear: page HTML lives in Elementor; global/site behavior lives in classified Code Snippets; settings are configured via WordPress/WooCommerce/Rank Math options.
- **All generated UI must be interaction-safe.** Buttons, links, forms, quantity controls, menus, accordions, tabs, filters, sliders, cookie/age gates, and checkout controls must be clickable/tappable, must not be blocked by overlays, must not freeze, and must not overflow their containers on desktop or mobile.

When a requested feature cannot be implemented safely within this stack, stop and report the architectural reason instead of forcing a fragile workaround.

## CRITICAL: Separate Site Tasks From Skill-Maintenance Tasks

When the user asks for live website work and skill/workflow updates in the same message, the agent MUST split the work into two ledgers:

- **Website task ledger**: live WordPress/WooCommerce changes, snippets, pages, products, checkout, SEO, QA, screenshots, and rollback notes.
- **Skill task ledger**: changes to this skill's `SKILL.md`, references, templates, scripts, or procedural rules.
- Do website safety fixes first when users report a live blocker such as broken checkout, frozen cart buttons, mobile overflow, 404s, or broken add-to-cart.
- Do not let skill documentation edits count as website QA, and do not let a website fix count as skill completion. Report both separately.
- When updating the skill, edit the actual skill files with concise, durable rules. Do not only explain the rule in chat.

## CRITICAL: First Step Service Mode Selection

The first user-facing step for any WordPress project MUST be to identify which service the customer wants:

1. **New site build**: build a new WordPress/WooCommerce SEO site from requirements.
2. **Old-site rebuild**: rebuild an existing site while preserving protected products/media.
3. **Existing-site SEO optimization**: do not redesign/rebuild pages; audit and optimize existing pages, products, posts, categories, Rank Math metadata, schema, internal links, image ALT text, sitemap/noindex, and SEO content gaps.
4. **Reference-site inspired build / clone-style adaptation**: capture a public or user-authorized reference site's page structure and HTML snapshots for analysis, then rebuild a transformed WordPress/WooCommerce site with the user's brand, products, language, compliance, and SEO. Do not publish copied HTML, text, assets, trademarks, or protected designs verbatim.

In autonomous mode, infer the mode from the user's wording and record the decision. In ask-user mode, list these service options and wait for the user's choice before changing the site.

## CRITICAL: Reference-Site Capture and Clone-Style Adaptation

When the user asks to clone, imitate, copy, replicate, reference, or rebuild from another website URL, treat it as a reference-site adaptation workflow.

- Read `references/reference-site-capture.md` before acting.
- Capture the reference site's relevant page HTML snapshots locally for analysis, including homepage, navigation, category/listing pages, product/detail pages, blog/news pages, policy/legal pages, contact/about pages, cart/checkout/account pages when publicly accessible, and any site-type-specific pages such as service, pricing, case study, documentation, location, booking, or portfolio pages.
- Store captures under `.reference-captures/` or another gitignored directory. Do not commit captured third-party HTML, screenshots, assets, cookies, or private data.
- Use `scripts/reference_site_capture.py` to build a manifest of URLs, page types, titles, H1s, meta descriptions, links, and saved HTML file paths.
- Use captured HTML as layout intelligence only: section order, navigation depth, grid density, CTA placement, filter patterns, trust blocks, footer structure, responsive behavior, and content modules.
- Do not publish copied HTML/CSS/JS, copyrighted text, images, logos, brand names, trademarks, structured data, product data, reviews, or policies from the reference site. Rebuild transformed pages using the user's own brand, products, media, language, and compliance facts.
- For non-WordPress reference sites, map the discovered surfaces into WordPress page types, WooCommerce templates when ecommerce is required, Elementor HTML widgets for custom pages, and Code Snippets for global shell/dynamic behavior.
- For ecommerce reference sites, preserve WooCommerce transactional ownership: cart, checkout, account, product pages, archives, and variation forms must remain functional WooCommerce surfaces, not static copied HTML.
- Produce a reference-site analysis report before building: captured URL count, page-type coverage, reusable layout patterns, elements to avoid copying, WordPress/WooCommerce mapping, SEO opportunities, and QA risks.
- If robots.txt, login walls, payment steps, geoblocking, anti-bot checks, or terms restrictions block capture, stop or reduce scope. Never bypass authentication, paywalls, checkout payment steps, or access controls.

## CRITICAL: Existing-Site SEO Optimization Mode

When the customer chooses existing-site SEO optimization, the agent MUST NOT rebuild the site layout or replace pages unless the user separately asks for repair. The goal is full-site SEO improvement on the current content.

- Inventory existing pages, products, product categories, posts, post categories/tags, media, menus, Rank Math settings, sitemap, robots, schema, and noindex/index state.
- Identify missing, duplicate, thin, or generic SEO titles, meta descriptions, focus keywords, image ALT text, internal links, category descriptions, product long descriptions, and article SEO fields.
- Check Rank Math and Code Snippets. If Code Snippets is missing, install and activate it automatically only when autonomous mode or explicit plugin-install permission is recorded; otherwise ask the user to approve installation.
- Use content-aware SEO mapping before writing metadata. Do not generate generic SEO fields without reading the existing content.
- Use Code Snippets one-time writers for Rank Math Free bulk metadata updates, image ALT fixes, and settings writers; verify and delete/disable one-time snippets after use.
- Do not change product IDs, slugs, prices, stock, checkout, payment, shipping, theme, or page layout unless the SEO audit proves a specific issue and the mode/permission allows it.
- Produce an SEO optimization report with audited counts, updated IDs, skipped IDs, failed IDs, writer snippets removed, remaining blockers, and next content recommendations.

## CRITICAL: Interruption Resume and Checkpoint Rule

AI coding tools can stop because of server errors, context limits, browser crashes, REST timeouts, network failures, or user pauses. Every build MUST be resumable.

- Maintain a **resume ledger** for website tasks and skill tasks. Record completed steps, verified evidence, created/updated IDs, active snippets, page IDs, article IDs, product import counts, temporary credentials to revoke, blockers, and the next safe action.
- After any interruption, the agent MUST first reconstruct state from the ledger and live WordPress/Git files before acting.
- Resume from the smallest safe unfinished step. Do not restart the whole build, repeat destructive cleanup, re-import products, re-delete pages, re-publish articles, or overwrite snippets unless verification proves it is required.
- Treat "last message said it was done" as insufficient. Resume only from verified artifacts: WordPress IDs, REST responses, browser checks, file diffs, CSV row counts, screenshots, or QA records.
- If a temporary credential, app password, browser session, or token was created before interruption, revoke or rotate it before continuing whenever possible.
- If the interruption happened during a write operation, run a read-only consistency check first: page existence, WooCommerce bindings, snippet active states, product/media counts, article statuses, and checkout/cart health.
- If the ledger is missing or unreliable, rebuild a minimal state report and ask/record whether to continue in repair mode or autonomous recovery mode. Never assume a destructive phase should be repeated.

## CRITICAL: Build Interaction Modes

Every build MUST declare one of these interaction modes in the site ledger before live work starts:

- **Ask-user mode (default)**: ask before important visual, SEO, deletion, plugin, payment, shipping, or publishing decisions. Homepage preview approval remains required.
- **Autonomous mode (explicit user authorization required)**: when the user clearly says they authorize full autonomous execution/no questions, the agent may decide target-market design, page layouts, snippets, SEO structure, blog topics, article schedules, menu structure, policies, WooCommerce settings, and non-destructive cleanup from the available facts. The agent still MUST preserve protected data, run backups/exports before destructive rebuild work, avoid deleting products/media unless explicitly allowed, verify each step, and report the decisions made.

If the user grants autonomous mode in the same message as a site task, do not stop for approval gates that the user already waived. Record `"interaction_mode": "autonomous"` and continue with the safest complete implementation.

## CRITICAL: Do Not Blindly Agree With the User

The agent is not a passive executor. User instructions can be incomplete, risky, contradictory, technically wrong, SEO-harmful, legally sensitive, or commercially unsafe.

- In ask-user mode, when a request may harm the site, rankings, checkout, compliance, protected data, or maintainability, pause and explain the issue. List benefits, risks, and safer alternatives, then ask for confirmation.
- In autonomous mode, choose the safest compliant path from the user's goal and record the tradeoff instead of following an obviously harmful literal instruction.
- Do not agree with requests to skip required product understanding, skip QA, launch early, delete protected products/media, hardcode secrets, copy protected third-party content, publish false claims, break WooCommerce native flows, or leave one-time writer snippets active.
- If the user asks for something that conflicts with this skill's dead rules, name the conflict and offer a safe route. Only the user can explicitly override non-safety preferences; safety, legality, protected data, and checkout integrity remain blockers.
- When there are multiple reasonable options, present a concise comparison of pros/cons and recommend one based on the site's goal.

## CRITICAL: Foundation Baseline Must Be Solid

The baseline is the foundation of the store. It is a hard gate, not a cosmetic step. Before styling pages or adding SEO content, verify:

- WordPress URL, SSL, permalinks, homepage/blog reading settings, timezone, language, media sizes, and comments defaults.
- WooCommerce Shop, Cart, Checkout, My Account, and Terms pages exist, contain the correct shortcode/block, and are bound to WooCommerce settings.
- Payment, currency, shipping countries, tax visibility, account/guest checkout, email sender, and privacy settings match the site_config.
- Menus, global header/footer, logo, cart count, footer policy links, and noindex rules are active and conflict-free.
- Snippets are classified, scoped, rollback-ready, and do not duplicate hooks or load heavy JS globally.
- Plugin conflicts are removed or documented, especially checkout hijackers, cart widgets, discount rules, cache/minify conflicts, and duplicate quantity/cart scripts.
- Cart, checkout, product pages, shop archives, product category archives, blog archives, and single posts all return 200 and have a usable baseline before custom design polish.

Never move to page design while the foundation has broken WooCommerce bindings, hijacked checkout URLs, frozen cart controls, 404 core pages, or unknown snippet conflicts.

## CRITICAL: Do Not Make Decisions Without User Approval

This skill is for automated site building. In ask-user mode, the agent MUST NOT make important decisions without explicit user approval. In autonomous mode, this section is replaced by the user's explicit authorization, while preservation, backups, QA, and safety rules still apply. In ask-user mode, this includes but is not limited to:

- **Do NOT choose a design direction without user approval.** Always generate a homepage style preview first and wait for approval.
- **Do NOT skip the prerequisite check.** Always verify all required plugins and themes are installed before starting.
- **Do NOT change the theme without asking.** If Hello Elementor is not active, tell the user and wait for them to install it.
- **Do NOT install plugins without user permission.** Inform the user what is missing and provide installation instructions.
- **Do NOT choose alternative plugins without user confirmation.** If Rank Math is missing, do not use Yoast instead without asking.
- **Do NOT modify existing pages without user confirmation.** Ask before overwriting any existing content.
- **Do NOT change payment methods, shipping zones, or WooCommerce settings without user confirmation.**
- **Do NOT publish pages without user confirmation** unless the user explicitly requested immediate publish.
- **Do NOT make assumptions about target market, language, or design style.** Always ask the user first.
- **Do NOT skip any QA step.** Every link, image, button, and page must be verified.
- **When in doubt, ASK the user.** Never proceed on assumptions for anything that could affect the site's appearance, functionality, or SEO unless the ledger is already in autonomous mode.

## CRITICAL: Full Store Surface Must Be Designed

Do not treat the homepage and policy pages as the whole website. Every ecommerce build must give the full storefront a target-market-aware layout pass:

- Homepage and custom pages.
- Shop/product archive and product category archives.
- Single product pages, including gallery, summary, tabs/description, related products, trust blocks, and mobile add-to-cart behavior.
- Blog index, blog archive/category/tag views, and single post templates.
- Cart, checkout, order received, and My Account screens.
- FAQ, Contact, Shipping, Returns, Payment, Privacy, Terms, Cookie, and Age/Compliance pages.

The layouts must be varied by country/language and site strategy. Do not reuse the same one-column mobile product grid, the same card rhythm, or the same policy layout across every site. Record the layout choices and verify no text/button/image overflow at 360px, 390px, and 430px.

## CRITICAL: Rich Page Content and Dynamic Merchandising

Do not build thin pages that rely on a hero, a few generic cards, and policy links. Every full site build must turn the product knowledge ledger, target market, language, shipping/payment facts, media library, and SEO plan into rich page modules across the whole site.

- Homepage must include market-appropriate merchandising modules, not only static copy. Consider dynamic product-image slideshows, featured-product strips, category image grids, seasonal/collection blocks, buying-guide teasers, shipping/payment explainers, support/WhatsApp callouts, compliance/age notices, FAQ previews, blog-guide teasers, and internal links to real product/category/article pages.
- Other custom pages must also feel complete. About, Contact, FAQ, Shipping, Returns, Payment, Terms, Privacy, Cookie, Age/Compliance, blog pages, and category support pages should use useful layouts such as summaries, timelines, comparison tables, step flows, icon+text checklists, contextual product/category links, FAQ accordions, and support blocks when appropriate.
- Product archives and category archives should expose buyer navigation: category filters, product density suited to the target market, sorting, trust/shipping notes, internal links, and short SEO/category guidance without blocking WooCommerce loops.
- Single product pages should enrich the native WooCommerce product surface with real gallery media, key specs, delivery/return/payment facts, related products, compliance notes, FAQ, and internal links while preserving add-to-cart and variation behavior.
- Blog index, blog archives, and single posts should connect articles to real categories/products using contextual links and media, instead of a plain list of posts.
- Select modules by country/language and product data. For example, a slideshow may be useful when product images are strong, but a dense spec comparison, category-first layout, guide hub, or WhatsApp/COD ordering flow may be better for another market.
- Never hardcode dynamic product names, prices, stock, URLs, or article titles into static HTML. Use WooCommerce/WP queries or approved Code Snippets renderers so modules stay current and link to real content.
- Richness must not create clutter. Each module must support buying, trust, navigation, SEO, education, or support; remove decorative filler that does not serve a page goal.
- Verify every dynamic module on desktop and mobile: images render, links navigate, carousel/slider controls work, keyboard/touch interaction does not freeze, lazy loading does not create blank sections, and no text/button/image overflows.

## CRITICAL: Article Batch Is Part of the Build

Unless the user explicitly opts out, every full SEO ecommerce build MUST create an initial article batch. In ask-user mode, ask for count/schedule/approval. In autonomous mode, choose conservative defaults from the market, products, and language.

- Default initial batch: 10-20 product/category/topic articles.
- Use real product images from the media library, real internal links, Article schema, FAQ schema, Rank Math metadata, and target-language copy.
- Create as drafts unless the user approved scheduling/publishing. If scheduling is authorized, spread posts across 3-6 months in the target-market timezone.
- Report article IDs, titles, status, scheduled dates, featured images, internal links, and SEO focus keywords. Do not silently skip this phase.

## CRITICAL: Product CSV and Media Import Integrity

When importing or rewriting WooCommerce CSV data, product data and media integrity are mandatory:

- For official WooCommerce CSV exports, prefer RFC/Excel CSV parsing with doubled-quote support (`doublequote=True`) and verify parser quality before editing. Do not blindly trust delimiter sniffing when product descriptions contain HTML.
- When a product CSV is provided, inspect and summarize it BEFORE generating homepage previews, page HTML, product/category copy, blog topics, or Rank Math SEO metadata. Page code and SEO data must be based on real product names, categories, attributes, prices, images, descriptions, and compliance limits, not guesses.
- Produce a product knowledge ledger before design/content generation: product/category counts, representative products, variable/simple product mix, key attributes, price range/currency, image/gallery/body-image coverage, current descriptions, SEO fields, protected fields, and content opportunities.
- If the CSV cannot be parsed or product facts are unclear, stop page/SEO generation and fix the CSV inspection first. Do not create generic HTML sections or generic SEO metadata while product understanding is missing.
- Preserve IDs/SKUs/slugs/parents/variations/attributes/prices/stock/categories unless explicitly changing them.
- If the source product prices are in a different currency than the target site currency, convert prices before import using a recorded exchange rate. Do not hardcode exchange rates in the skill; use a user-provided rate or a live rate checked at build time and record source, timestamp, source currency, target currency, rounding rule, and sample converted products.
- Preserve the original source prices in backup meta columns or an import ledger before replacing `Regular price` and `Sale price`.
- Verify row count, variation parent links, image URL columns, gallery image counts, downloadable files, and Rank Math fields before import.
- Classify every `Meta:` column by exact key before editing. Editable SEO meta is different from protected runtime/analytics/custom plugin meta.
- Ensure featured images, gallery images, long descriptions, short descriptions, inline/body images, ALT/title/caption fields, and product detail HTML import successfully.
- After import, sample simple products, variable products, and products with galleries/body images on the front end. Confirm gallery thumbnails, main image, long description images, add-to-cart, cart quantity, price, stock, category, and SEO metadata.
- Produce an import ledger with source row count, imported/updated count, failed rows, missing images, gallery mismatches, and sample product verification URLs.

## CRITICAL: Logo and Site Icon Must Be Separate Verified Assets

When generating or replacing a website logo, the agent MUST also generate and configure the WordPress site icon/favicon unless the user explicitly opts out.

- Create at least two assets: a full logo for header/footer and a simplified square site icon for favicon/app icon.
- Create background-aware logo variants for the actual header and footer backgrounds: transparent logo, light-background logo, and dark-background/inverted logo when needed.
- Never place a white-box logo image on a dark header/footer unless that boxed treatment is an intentional approved brand style. If the logo has a solid background, its color must match or harmonize with the surrounding header/footer block.
- The site icon must work at 512x512, 192x192, 64x64, and 32x32. Test it on light and dark browser UI backgrounds.
- Do not reuse a complex full logo as the favicon if it becomes muddy, black, cropped, or unreadable at small sizes.
- Use clear contrast, simple geometry, enough inner padding, and transparent or intentionally colored background.
- Configure the site icon in WordPress Site Identity or via a verified settings/snippet workflow, then verify browser tab icon, mobile shortcut preview where possible, and source markup.
- Verify the selected logo variants directly inside the real header and footer after global colors are applied; the logo must not look pasted on, mismatched, cropped, muddy, or low contrast.
- Record logo media ID, favicon media ID, dimensions, file type, background choice, header/footer variant choice, and verification screenshots/notes in the build ledger.

## CRITICAL: Rank Math Content-Aware One-Time SEO Writer

Rank Math Free can import/export basic settings as JSON, but bulk SEO metadata CSV import is a Pro workflow. For free-version sites, use a Code Snippets one-time writer for page/product/post/category SEO metadata.

- Before writing SEO metadata, identify the actual content first: page title/content, Elementor HTML, product title/short description/long description/categories/attributes/images, blog title/content/excerpt/category, and taxonomy descriptions.
- Reuse the build ledger, resume ledger, site_config, product knowledge ledger, generated article plan, CSV rewrite report, and any approved memory/knowledge-base artifacts from the build. Treat memory as assistance, not proof; verify against live WordPress content before writing.
- Generate a mapping per object: WordPress ID, object type, SEO title, meta description, focus keyword, robots/index state, schema type where applicable, and source evidence.
- Use a classified `one_time_writer` Code Snippet to update Rank Math post meta/term meta in bulk. Keep the mapping in the snippet or load from a safe generated artifact; never include secrets.
- After execution, verify sampled pages, all priority URLs, sitemap inclusion, source HTML meta tags, and Rank Math admin fields.
- After successful verification, disable and delete the writer snippet. Do not leave one-time SEO writers active.
- If the writer partially fails, do not rerun blindly. Read the run ledger, identify written IDs, and resume only missing/failed IDs.

## CRITICAL: Rank Math On-Page SEO Score Rules

When generating page code, product copy, blog posts, category descriptions, or Rank Math metadata, the agent MUST satisfy the Rank Math on-page checks where they are appropriate for the content type:

- Focus keyword appears in the SEO title.
- Focus keyword appears at the beginning of the SEO title when natural.
- Focus keyword appears in the SEO meta description.
- Focus keyword appears near the beginning of the visible content.
- Focus keyword appears in the main content body.
- Focus keyword appears in at least one subheading such as H2, H3, or H4.
- At least one image has ALT text containing the focus keyword, using a real product/page/article image.
- Keyword density is non-zero and natural; avoid stuffing.
- Content includes useful internal links to real pages/products/posts.
- The focus keyword is unique for the site unless the user intentionally targets a cluster.
- Content uses short readable paragraphs.
- Content includes rich media such as real images or video when available.
- Product/category/blog/page content must be long enough to be useful; avoid thin content created only to satisfy a score.

Do not blindly chase a 100/100 score by adding spammy repetition. Make the page helpful, compliant, readable, and specific to the product/page/search intent.

## CRITICAL: Dead Rule 9 - No Launch Mode Before Full Content and QA

The site MUST NOT be switched to launch/live/indexing mode until the whole storefront is complete and tested. This is a DEAD RULE.

- Product pages, product archives, product category archives, cart, checkout, My Account, custom pages, policy pages, blog index/archive, single posts, and the initial article batch must be complete.
- Rank Math metadata, sitemap, robots, schema, internal links, image ALT text, and noindex/index rules must be verified.
- All generated articles must exist as drafts or scheduled/published posts according to the user's mode. Article QA is part of site QA, not optional after-work.
- Desktop and mobile testing must pass for links, buttons, menus, quantity controls, add-to-cart, cart update, checkout boundary, images, forms, age/cookie gates, and layout overflow.
- Only after the full QA ledger passes may the agent enable launch/indexing actions, submit sitemaps, remove maintenance/noindex restrictions, or tell the user the site is ready to go live.

If any core product page, article batch, archive layout, checkout path, or QA category is incomplete, mark it as a launch blocker and keep the site out of launch mode.

## CRITICAL: Code Scale, Maintainability, and Vibe-Coding Risk Controls

AI-generated code is useful for small, scoped snippets, but large uncontrolled codebases become fragile quickly. The agent MUST follow these controls:

- **Keep code small and scoped.** Prefer focused Code Snippets and Elementor HTML blocks. Do not generate thousands of lines in one blob when a smaller hook, shortcode, or page block solves the need.
- **Avoid hidden project-wide coupling.** Large projects lose global context easily; local changes can cause hidden chain bugs. Before editing shared behavior, inspect related snippets/hooks/pages and record affected surfaces.
- **Preserve developer control.** Every snippet/page block must have a plain-language purpose, lifecycle, affected pages, rollback path, and verification result so future maintainers can explain and debug it.
- **Do not trade early speed for long-term chaos.** If a requested shortcut will create repeated debugging, logic contradictions, or hard-to-maintain code, choose a smaller verifiable implementation and explain the tradeoff.
- **Security and compliance are gates.** Never hardcode secrets, admin credentials, API keys, payment secrets, private tokens, or personal data in snippets/page HTML. Validate permissions, sanitize inputs, escape outputs, use nonces for write actions, and avoid unsafe data logic.
- **Commercial launch requires extra caution.** Treat permission bugs, data leaks, broken checkout, unverified payment/shipping logic, illegal claims, and platform-policy risks as launch blockers.
- **No code mountain.** If a feature grows beyond the lightweight stack, split it into named snippets/modules with tests, or recommend a proper plugin/custom development path instead of dumping a massive fragile implementation into Code Snippets.

## CRITICAL: Step-by-Step Execution (Hard Rule)

Every step in every phase MUST be executed carefully and in order. This is a HARD RULE that cannot be overridden:

- **Do NOT skip any step.** Every step exists for a reason. Even if a step seems unnecessary, execute it and verify.
- **Do NOT combine steps to save time.** Each step must be completed and verified independently.
- **Do NOT reorder steps for convenience.** The order is designed for safety and correctness.
- **Do NOT switch to an alternative method because a step is difficult.** Follow the defined procedure. If a step fails, fix the issue and retry that step.
- **Do NOT assume a step was completed without verifying.** Every step has a verification requirement 鈥?check it.
- **If a step fails, STOP.** Fix the issue, retry the step, and only proceed after it succeeds.
- **Do NOT rush.** Completing thoroughly is more important than completing quickly.

For agents that tend to skip steps, use the anti-skip protocol in `references/ai-agent-compatibility.md`: print the current phase, state the required gate, list intended writes before editing, verify after every write, and mark blocked instead of improvising when a required artifact or capability is missing.

## CRITICAL: Agent Enforcement Rules (Binding Framework)

The agent MUST read and follow `references/agent-enforcement-rules.md` at all times. This file defines the binding enforcement framework that governs all agent behavior. The agent is NOT permitted to deviate from these rules under any circumstances.

- **No autonomous decisions.** The agent MUST NOT make any decision affecting the site's appearance, functionality, data, or SEO without explicit user approval. When in doubt, STOP and ASK.
- **No method switching.** When a defined procedure exists, the agent MUST follow it. Do NOT switch to alternative methods because the defined method is difficult, slow, or failed. Fix and retry instead.
- **No shortcuts.** The agent MUST NOT skip verification, combine steps, use hardcoded values, use fake data, skip mobile testing, skip link verification, or mark QA as "pass" without testing.
- **Verification gate after every step.** Execute 鈫?Verify 鈫?Record 鈫?Gate (only proceed if verification passes).
- **Three-strike rule.** First deviation: self-correct. Second deviation: notify user. Third deviation: STOP all work, re-read all reference files.
- **Context refresh.** If uncertain about a procedure, re-read the relevant reference file. Do NOT rely on memory for procedural details.
- **User override only.** Only the user can override a defined procedure. The agent MUST NOT override on its own. Document all user-approved deviations.
- **Progress reporting.** After each step, report what was completed, what was verified, what the next step is, and any issues.
- **No silent actions.** Announce before acting, report after acting, show verification, explain issues, ask about uncertainties.

## CRITICAL: SiteGround Server Handling

Many sites built with this skill run on SiteGround hosting. SiteGround implements security and performance layers (CAPTCHA, WAF, IP blocking, caching) that can interfere with automated operations. Read `references/siteground-bypass-guide.md` for the complete handling guide.

- **Detect SiteGround hosting** by checking for SG Optimizer plugin or Site Tools references during environment inspection.
- **If a CAPTCHA or verification challenge appears**: STOP all automation, notify the user, and wait for them to solve it manually. Do NOT retry or refresh.
- **If IP is blocked**: Notify the user and provide unblock options (Site Tools 鈫?Security 鈫?Blocked IPs, or wait 15-30 minutes).
- **If WAF blocks API calls**: Ask user to set WAF to Standard mode in Site Tools 鈫?Security 鈫?WAF.
- **Always purge SG Optimizer cache** after content changes (page updates, product imports, snippet activation).
- **Configure SG Optimizer for Elementor**: Do NOT enable "Combine CSS" or "Combine JS" (breaks Elementor). Enable Dynamic Cache, Memcached, HTTPS Enforce, Gzip, Browser Caching, CSS/JS Minify, Defer JS.
- **Use REST API with application passwords** as the preferred access method (less likely to trigger challenges than browser automation).
- **Add delays between automated actions** (2-5 seconds) to avoid triggering bot detection.
- **Do NOT switch to alternative methods** when encountering SiteGround challenges. Follow the handling procedure in `siteground-bypass-guide.md`.

## CRITICAL: Old Site Rebuild Procedure

When the user wants to rebuild an existing WordPress site (not a new build), the agent MUST follow the procedure in `references/old-site-rebuild-procedure.md`. This is a destructive operation.

- **Confirm with the user before starting cleanup.** Tell them exactly what will be deleted and what will be preserved. Wait for explicit confirmation.
- **Back up before cleanup.** Export all WordPress content and WooCommerce products before deleting anything.
- **PRESERVE**: WooCommerce products, product categories, product tags, product attributes, media library images.
- **CLEAR**: All pages (except WooCommerce-owned), all blog posts, all menus, all Code Snippets, all Elementor templates, all custom CSS, all widgets, WooCommerce settings (shipping, tax, payments), orders, coupons.
- **Execute all 13 cleanup steps in order.** No skipping. Each step must be verified before proceeding to the next.
- **Product data is sacred.** If any product data is lost during cleanup, STOP immediately and inform the user.
- **After cleanup, verify product data integrity** before starting the rebuild.
- **After cleanup, follow the standard build workflow** from Phase 0 (Prerequisite Check).

## CRITICAL: Global Shell Architecture (Header/Footer/CSS/JS)

The agent MUST use the global shell architecture defined in `references/global-shell-architecture.md`. Header, footer, global CSS, and global JS are injected globally 鈥?NOT embedded in every Elementor HTML page.

- **Global Header**: Implemented as a persistent Code Snippet using `wp_body_open` hook. Renders header HTML with logo, navigation menu, and cart icon on ALL pages automatically.
- **Global Footer**: Implemented as a persistent Code Snippet using `wp_footer` hook. Renders footer HTML with links, contact info, and copyright on ALL pages automatically.
- **Global CSS**: Added via WordPress Appearance 鈫?Customize 鈫?Additional CSS. Contains CSS variables (design tokens), header styles, footer styles, shared component styles, and responsive breakpoints.
- **Global JS**: Added via Code Snippets HTML/JS snippet using `wp_footer` hook. Contains mobile menu toggle, cart counter, smooth scroll, analytics, cookie consent, etc.
- **Page-specific content only**: Each Elementor HTML widget contains ONLY the page-unique HTML, scoped CSS, and scoped JS. No header, no footer, no menu, no global CSS, no global JS.
- **No duplicate code**: Never embed header/footer/menu HTML in individual page HTML widgets. The global shell handles all shared elements.
- **Page CSS must be scoped**: Use page-specific class names (e.g., `.home-page .hero`, `.about-page .team-grid`).
- **Page JS must use IIFE**: Wrap page-specific JavaScript in `(function() { ... })()` to avoid global scope conflicts.

## CRITICAL: Code Snippets Implementation (Use the Code, Not Just Reference It)

The agent MUST implement functionality using the Code Snippets plugin 鈥?not just document what settings exist. Read `references/code-snippets-implementation-guide.md` for REAL, ready-to-use code snippets.

- **Use Code Snippets for ALL functional implementations.** Every feature that can be implemented via Code Snippets MUST be implemented via Code Snippets, not via theme files or hardcoded HTML.
- **Reference the implementation guide.** Before implementing any feature, check `code-snippets-implementation-guide.md` for existing, tested code. Do NOT write code from scratch if a working snippet exists in the guide.
- **Settings configuration via Code Snippets PHP.** Use `update_option()` in a one-time Code Snippet to configure WordPress, WooCommerce, Elementor, and Rank Math settings programmatically. Read `references/wordpress-settings-implementation.md` for exact code.
- **WooCommerce customizations via Code Snippets.** Use WooCommerce hooks (`woocommerce_*`) in Code Snippets for product page, cart, checkout, and account customizations. Read `references/woocommerce-customizations-guide.md` for real implementations.
- **Every snippet must be classified.** Classify each snippet as: `persistent`, `ux_polish`, `one_time_writer`, `read_only_scanner`, or `deprecated`. Document the lifecycle in the snippet title or description.
- **Test every snippet before marking it complete.** After activating a snippet, verify on the front-end that it works, doesn't cause errors, and doesn't break mobile layout.
- **One snippet per function.** Each Code Snippet should implement ONE feature. Do not combine multiple unrelated functions in a single snippet 鈥?this makes debugging and rollback difficult.
- **Use correct hook priorities.** When multiple snippets hook the same action/filter, use priority parameters to control execution order.
- **Verify snippet compatibility.** Before activating a new snippet, check it doesn't conflict with existing snippets (same hook, same priority, same output location).
- **Purge cache after snippet changes.** After activating, deactivating, or modifying any Code Snippet, purge all caches (WordPress, Elementor, WooCommerce, SG Optimizer if applicable).

## CRITICAL: Four Dead Rules for Page Building (No Exceptions)

These four rules are DEAD RULES. The agent MUST NOT skip, forget, or work around any of them. Violating any of these rules produces broken websites. Read `references/elementor-html-automation.md` and `references/code-snippets-implementation-guide.md` for full enforcement procedures.

### Dead Rule 1: Set Page Layout to Elementor Canvas (MANDATORY)

Every custom page built with Elementor MUST have its Page Layout set to `elementor_canvas` BEFORE pasting any HTML into the HTML widget.

- **If Canvas is not set**: Hello Elementor's default header, footer, and menu appear on the page, duplicating the global shell. The page layout breaks.
- **Enforcement**: Set Canvas 鈫?Click Update 鈫?Reload front-end 鈫?Verify no theme header/footer 鈫?record Canvas ready. Add the HTML widget only later in the page HTML phase after the global shell is active and verified.
- **Record in page ledger**: `"canvas_set": true` only after verification passes.
- **Pages that MUST use Canvas**: Home, Blog, Contact, About, FAQ, Policy pages, Landing pages.
- **Pages that MUST NOT use Canvas**: Shop, Cart, Checkout, My Account, product archives, single product pages (these use WooCommerce templates).
- Read `references/elementor-html-automation.md` for the complete enforcement procedure.

### Dead Rule 2: Age Gate MUST Be Global Code Snippet 鈥?NEVER in Page HTML

The age verification gate MUST be implemented as a global Code Snippets PHP snippet using `wp_footer` hook. The agent MUST NEVER place age gate HTML/CSS/JS inside any Elementor HTML widget.

- **Why**: Age gate code (2,000-4,000 characters) bloats page HTML, causing Elementor paste to fail, truncate, or timeout. The age gate must be site-wide (one snippet), not duplicated per page.
- **Implementation**: Code Snippets 鈫?Add New 鈫?PHP snippet 鈫?`add_action('wp_footer', function() { ... }, 5)` 鈫?Scope: Front-end 鈫?Lifecycle: persistent.
- **Prohibited**: Never copy age gate code into Elementor HTML widget, page content, or post content.
- Read `references/code-snippets-implementation-guide.md` Section 8 for the complete code.

### Dead Rule 3: Batch Import for Large HTML (MANDATORY)

When the HTML payload for a page exceeds approximately 30,000 characters, or when paste fails/truncates, the agent MUST split the HTML into batches and import sequentially.

- **Split at natural boundaries**: Between `</section>` and `<section>`, or between major block closures.
- **NEVER split inside an open tag**: Each batch must start and end with complete, valid HTML tags.
- **Use ONE HTML widget**: All batches go into the SAME HTML widget. Append, never replace.
- **Verify after EVERY batch**: Click Update, check front-end, confirm no broken tags.
- **CSS stays in first batch, JS stays in final batch**: Never split a single `<style>` or `<script>` tag across batches.
- Read `references/elementor-html-automation.md` "DEAD RULE: Batch Import for Large HTML" for the complete procedure.

### Dead Rule 4: WooCommerce Page Regeneration and Binding for ALL Sites (MANDATORY)

For BOTH new websites AND old website rebuilds, the agent MUST regenerate and bind WooCommerce pages. This is not optional and applies to every build.

- **Regenerate WooCommerce pages**: WooCommerce 鈫?Status 鈫?Tools 鈫?Click "Install pages" (or "Create default WooCommerce pages"). This creates/updates Shop, Cart, Checkout, My Account, Terms pages with correct shortcodes.
- **Bind WooCommerce pages programmatically**: Use Code Snippets PHP with `update_option()` to bind:
  - `woocommerce_shop_page_id` 鈫?Shop page ID
  - `woocommerce_cart_page_id` 鈫?Cart page ID
  - `woocommerce_checkout_page_id` 鈫?Checkout page ID
  - `woocommerce_myaccount_page_id` 鈫?My Account page ID
  - `woocommerce_terms_page_id` 鈫?Terms page ID
- **Verify bindings**: After binding, check WooCommerce 鈫?Settings 鈫?Advanced tab 鈥?all page selectors must show the correct pages.
- **For old site rebuilds**: After the 13-step cleanup, WooCommerce page bindings may be broken. Regenerate and rebind ALL WooCommerce pages before proceeding to product import.
- **For new sites**: After creating all pages, regenerate WooCommerce pages and bind them before any product work.
- Read `references/code-snippets-implementation-guide.md` Section 2.2 and `references/wordpress-settings-implementation.md` for the exact binding code.

## CRITICAL: Additional Dead Rules for Data and Import Order (No Exceptions)

These rules are DEAD RULES that complement the Four Dead Rules above. The agent MUST follow them without deviation.

### Dead Rule 5: Dynamic Data via Code Snippets 鈥?No Static Data in Pages

Homepage and Blog pages MUST use dynamic data fetched via Code Snippets PHP, NOT hardcoded static product/article HTML.

- **Homepage products**: Use Code Snippets PHP with `wc_get_products()` or `WP_Query` to fetch real products. Output into a container (`data-site-render="home-products"`). The page HTML widget contains only the container + scoped CSS/JS 鈥?the PHP snippet fills it with real product data.
- **Blog posts**: Use Code Snippets PHP with `WP_Query` to fetch real posts into containers (`data-site-render="home-posts"` or `data-site-render="blog-posts"`).
- **NEVER hardcode product names, prices, images, or article titles in page HTML.** Pages must update automatically when products/posts change.
- **NEVER hardcode product IDs** unless the user explicitly requested specific products. Ask the user which products to feature if a curated set is needed.
- Read `references/code-snippets-implementation-guide.md` Sections 6-7 for dynamic renderer code.

### Dead Rule 6: Use Real Product Images in Page HTML

When creating page HTML, the agent MAY use real product images from the WooCommerce media library.

- **Ask the user** which products or categories to feature if specific imagery is needed.
- **Fetch image URLs dynamically** via PHP or use media library URLs.
- **NEVER use placeholder, stock, or fake images.** All images must be real product images.
- **All images must be WebP format.** Convert before use if needed.
- **ALT text** must be descriptive and SEO-friendly.

### Dead Rule 7: Step-by-Step Import Order (MANDATORY)

The agent MUST follow this import order. No exceptions. No reordering.

1. **FIRST: Global shell** 鈥?Create global header (`wp_body_open` hook) and global footer (`wp_footer` hook) via Code Snippets PHP. Verify on front-end BEFORE any page HTML.
2. **SECOND: Global CSS** 鈥?Add to Appearance 鈫?Customize 鈫?Additional CSS. Verify loads on all pages.
3. **THIRD: Global JS** 鈥?Add via Code Snippets HTML/JS on `wp_footer` hook. Verify works on all pages.
4. **FOURTH: Page HTML 鈥?one page at a time** 鈥?For each page: Set Canvas 鈫?verify 鈫?add HTML widget 鈫?paste HTML 鈫?Update 鈫?verify front-end 鈫?move to next page.
5. **FIFTH: Dynamic renderers** 鈥?Activate Code Snippets PHP for dynamic product/post rendering. Verify containers filled with real data.
6. **NEVER import all page HTML before the global shell is active.**

### Dead Rule 8: Global SEO, Speed, and WebP Optimization (MANDATORY)

After all pages are built and content imported, the agent MUST perform global optimization:

- **SEO**: Rank Math metadata for all pages/products/categories/posts. Noindex Cart/Checkout/My Account. Index content pages.
- **Speed**: Disable cart fragments on non-shop pages. Defer JS. Remove query strings. Enable Gzip/browser caching. PageSpeed mobile 90+, LCP < 2.5s, INP < 200ms, CLS < 0.1.
- **WebP**: Convert ALL images to WebP 鈥?products, galleries, categories, blog posts, page banners, logo. Verify after conversion.

## CRITICAL: Prerequisite Check (Mandatory First Step)

Before ANY site building work begins, the agent MUST read `references/prerequisite-checklist.md` and perform the full prerequisite verification. This is a HARD GATE.

### Startup sequence
1. Announce to the user that a prerequisite check is required.
2. Verify WordPress access works.
3. Verify Hello Elementor theme is active. If not, tell the user to install and activate it from Appearance -> Themes, or download from https://wordpress.org/themes/hello-elementor/
4. Verify Rank Math SEO is installed and activated. If not, tell the user to install it:
   - WordPress Admin -> Plugins -> Add New -> Search "Rank Math" -> Install -> Activate
   - Or download from https://rankmath.com/ (official site, login required for Pro)
   - Or free version: https://wordpress.org/plugins/seo-by-rank-math/
   - After installation, run the Rank Math setup wizard and connect the Rank Math account.
5. Verify Elementor is installed and activated.
6. Verify WooCommerce is installed and activated (for ecommerce sites).
7. Verify Code Snippets is installed and activated.
8. Verify SSL/HTTPS is enabled.
9. Verify PHP version is 8.0+.
10. Print the prerequisite checklist results for the user.
11. If any required item is missing, STOP and provide installation instructions. Do NOT proceed until all prerequisites are met.

## CRITICAL: Page Creation Before Code Generation

The agent MUST create all WordPress pages FIRST, then generate HTML code that references the correct page URLs. Never generate HTML with links to pages that do not exist yet.

1. Read `references/wordpress-elementor-structure.md` before creating any page code.
2. Create all WordPress pages with correct slugs (as draft).
3. Build a URL map of all page paths.
4. Generate HTML code using the URL map for all internal links.
5. Every link, menu item, button, and navigation reference in generated HTML must point to a real, existing page.
6. Verify all links after HTML insertion 鈥?no 404s allowed.

## CRITICAL: Code Quality Requirements

- **No stacked code.** Each page must load ONLY the CSS and JS it needs. Do not load stylesheets or scripts from other pages.
- **Clean, lightweight, non-stacked code.** No duplicate CSS/JS files. No unused rules. No debug code. No console.log.
- **Scoped CSS.** Use scoped class names (e.g., `.brand-home .hero`) to avoid global conflicts.
- **WebP images.** ALL images on the site must be converted to WebP format. Use Smush, ShortPixel, or Imagify for automatic conversion.
- **Minified production code.** CSS and JS must be minified for production.
- **Conditional loading.** Code Snippets must use conditional tags to load only on relevant pages.
- **Performance targets.** PageSpeed mobile score 90+, LCP < 2.5s, INP < 200ms, CLS < 0.1.

## CRITICAL: Global Design Preferences

Before choosing a design direction, the agent MUST read `references/global-design-preferences.md` and understand the target market's design preferences, cultural habits, color associations, trust signals, and payment preferences. The design must match the target country's conventions.

- Ask the user for the target market/country during intake.
- Apply regional design preferences to the homepage style preview.
- Use culturally appropriate imagery, colors, and copy.
- Display correct payment badges for the target market.
- Include required legal elements (GDPR, Impressum, etc.) if applicable.
- Configure RTL layout if targeting Arabic markets.
- Offer COD if the target market requires it (SEA, Middle East, Africa, Latin America).
- Offer installment payments if targeting Brazil/Mexico.
- **Do not reuse the same grid/card layout across countries.** Mobile product/category grids must be chosen from the target market profile: Western/Central Europe usually moderate-density 2-column commerce grids; North America can be more spacious and image-led; East Asia can be denser; SEA/Latin America need thumb-first promotional layouts; Middle East may need RTL and premium trust-first patterns.
- **Never default mobile product grids to one column unless product images/text truly require it.** Test 360px, 390px, and 430px widths. If two columns fit without overflow or illegible text, prefer a target-market-appropriate two-column or mixed-density layout.
- Every page type must share the same brand system (tokens, button shape, spacing, heading scale) while varying section layout by page purpose. "Unified" does not mean every page uses identical cards.

## CRITICAL: Policy Pages Must Be Real Content

Policy/support pages are SEO, trust, and checkout assets. They MUST NOT be filler paragraphs.

- Each required policy page must include store-specific facts: legal audience/age gate, shipping origin, delivery countries/timing, currency, payment method, return window, support channel, order verification, and product restrictions.
- Each policy page must have enough content to answer likely buyer questions, normally including clear sections, concrete steps, and contact path. Avoid one-paragraph placeholder policies.
- Policy pages must be localized to the target language and market, including local wording for payment, delivery, returns, privacy/cookies, and regulated product warnings.
- Policy page layouts must be visually consistent with the site but may use practical document layouts: summary bands, step lists, tables, FAQ blocks, and contact callouts. Do not use generic landing-page cards for legal content.
- Verify every policy page on desktop and mobile for readable line length, no text overflow, working footer links, and index/noindex status according to SEO strategy.

## CRITICAL: WooCommerce Quantity UX Must Be Human-Friendly and Non-Blocking

Product pages and cart pages MUST expose clear quantity controls when quantity is editable.

- Add +/- controls as a reversible Code Snippets UX layer that preserves the original WooCommerce `<input class="qty">`, variation events, min/max/step attributes, and native cart form behavior.
- The +/- controls MUST NOT auto-submit the cart form, auto-click checkout, or repeatedly trigger page reloads. On cart pages, either enable the native "Update cart" button after changes or use a proven AJAX fragment flow that is verified not to freeze.
- Test quantity controls on simple products, variable products, cart desktop, cart mobile, and checkout after cart update.
- If a product does not allow quantity changes because of stock, variation, or plugin constraints, report the reason instead of faking controls.

## CRITICAL: Article Publishing and Draft-Review Workflow

This skill generates SEO-optimized blog articles based on the site's products, target market, language, and SEO keywords. Every article MUST follow the draft-review-then-publish workflow.

- **Do NOT publish any article without user approval.** Every article is created as a draft first.
- **Send the draft link to the user** for review before publishing: `https://site.com/wp-admin/post.php?post={ID}&action=edit`
- **Wait for explicit user approval** ("approve", "publish", "ok") before changing status to publish or future.
- **If the user requests changes**, make the changes and re-send the draft link.
- **Exception**: If the user explicitly says "pre-approve all" or "auto-publish without review", the agent may skip per-article review. This must be an explicit instruction, not an assumption.

### Article Content Requirements
- Articles must be based on the site's actual products, target market, and language.
- Article topics are diverse but always related to the site's products (buying guides, comparisons, how-tos, trends, gift guides, FAQs, etc.).
- Each article includes 4-8 real product images from the media library (user-configurable, default: 4-8).
- Each article includes 3-5 prominent product internal links (user-configurable, default: 3-5).
- Each article includes a FAQ section with FAQPage schema.
- Each article has unique Rank Math SEO metadata (title, meta description, focus keyword, Article schema).
- No keyword cannibalization: each article targets a unique primary keyword.
- Article word count: 800-1,500 words (recommended default, user-modifiable).
- All images must be in WebP format with descriptive ALT text.
- All internal links must point to real, published product pages (no 404s).

### Scheduled Publishing
- Use WordPress built-in scheduling (set post status to `future` with a specific date/time).
- Ask the user for publishing frequency (default: 2-3 articles/week), days, time, and timezone.
- Ensure continuous publishing for at least 3-6 months from the initial batch.
- Configure WordPress timezone to match the target market.
- All scheduled articles must still go through the draft-review workflow first.

### Context Awareness for Article Generation
Before generating articles, the agent MUST understand:
- Site products and categories (from WooCommerce).
- Product CSV facts or the product knowledge ledger when a CSV was provided.
- Target market and language (from site_config).
- SEO seed keywords and priority products.
- Brand voice and tone.
- Prohibited claims and compliance restrictions.
- Cultural conventions for the target market (read `global-design-preferences.md`).

Read `references/scheduled-article-publishing.md` for the complete article generation workflow, topic strategy, content structure, SEO metadata, and scheduling configuration.

## CRITICAL: Post-Build Actions (Mandatory After QA)

After the website build is complete and QA passes, the agent MUST present post-build action recommendations to the user. Do NOT skip this step.

Present these 4 action areas and ask which the user wants to proceed with:
1. **Scheduled Article Publishing Plan**: Generate next batch of articles, set up continuous publishing schedule.
2. **Search Engine Index Submission**: Submit sitemap to Google Search Console and Bing Webmaster Tools, request indexing for key pages.
3. **Analytics and Monitoring Setup**: Configure Google Analytics 4, link Search Console, set up Rank Math Analytics, establish monitoring routine.
4. **Social Media Auto-Sharing**: Configure social profiles, set up auto-sharing plugins, verify OpenGraph and Twitter Card tags.

Do NOT start any post-build action without explicit user confirmation. Walk the user through each chosen action step by step.

Read `references/post-build-actions.md` for the complete post-build action guide, checklists, and user communication templates.

## Start Here

**IMPORTANT: Read the DEAD RULES first.** The "CRITICAL: Four Dead Rules for Page Building" and "CRITICAL: Additional Dead Rules for Data and Import Order" sections above define 8 non-negotiable rules. The agent MUST understand and follow ALL of them before starting any build.

1. Read `references/prerequisite-checklist.md` FIRST and perform the full prerequisite verification. Do not proceed until all prerequisites pass.
2. Read `references/intake-checklist.md` before asking the user for information.
3. Read `references/global-design-preferences.md` to understand the target market's design preferences before generating any design.
4. If the user gave a WordPress URL and credentials, avoid echoing secrets. Use the current session only, and prefer environment variables or browser password prompts over storing credentials.
5. Build a `site_config` from supplied answers and observed WordPress state. If the user did not supply enough detail, ask only for fields that cannot be inferred.
6. Read `references/phase-playbook.md` for the execution order.
6a. Read `references/ai-agent-compatibility.md` when porting this workflow to another AI coding tool, when the current agent cannot reliably run shell/browser/WordPress/GitHub steps, or when a tool tends to skip gates.
7. Read `references/wordpress-elementor-structure.md` before creating any page code. Understand which pages exist and their URL paths.
8. Read `references/site-baseline-and-menus.md` before creating page content so global style, Rank Math basics, WooCommerce bindings, header menu, and footer menu are settled first.
9. Read `references/elementor-html-automation.md` before opening Elementor, setting Elementor Canvas, adding HTML widgets, or pasting page HTML.
10. Read `references/style-preview-gate.md` before building the full site; produce a homepage style preview and wait for user approval before broad page import.
11. Read `references/product-csv-originality-seo.md` when the user provides a WordPress/WooCommerce product export CSV for product title, description, content, or Rank Math SEO rewriting before import.
11a. If a product CSV was provided, run product CSV inspection and create the product knowledge ledger before generating any homepage preview, page HTML, article plan, or SEO mapping.
11b. Read `references/reference-site-capture.md` when the user provides a site URL to clone, imitate, reference, or rebuild from. Capture public/authorized HTML snapshots locally and transform the layout into original WordPress/WooCommerce implementation.
12. Read `references/design-variation.md` before generating page HTML/CSS so every site and article batch has a distinct, content-rich, non-AI-looking design direction.
13. Read `references/automation-and-safety.md` before touching wp-admin, WooCommerce settings, snippets, or live content.
14. Read `references/google-seo-guidelines.md` for comprehensive Google SEO official guidelines, E-E-A-T, spam policies, and best practices.
15. Read `references/rank-math-seo-guide.md` for complete Rank Math configuration, module reference, and WooCommerce product SEO mapping.
16. Read `references/core-web-vitals-guide.md` for performance optimization, LCP/INP/CLS targets, and WordPress-specific fixes.
17. Read `references/structured-data-guide.md` for Schema markup implementation, JSON-LD templates, and rich results eligibility.
18. Read `references/ecommerce-seo-guide.md` for WooCommerce-specific SEO strategies, product/category optimization, and internal linking.
19. Read `references/qa-and-launch.md` before claiming the build is complete. Every link, image, button, and page must be verified on both desktop and mobile.
20. Read `references/scheduled-article-publishing.md` before generating blog articles. Understand the draft-review-then-publish workflow, article content requirements, and scheduled publishing configuration.
21. Read `references/post-build-actions.md` after QA passes. Present the 4 post-build action recommendations to the user.
22. Read `references/siteground-bypass-guide.md` when the site is hosted on SiteGround. Follow the handling procedures for CAPTCHA, IP blocks, WAF, and caching challenges.
23. Read `references/old-site-rebuild-procedure.md` when rebuilding an existing site. Follow the 13-step cleanup procedure exactly 鈥?no skipping.
24. Read `references/global-shell-architecture.md` before creating any page HTML. Understand that header, footer, global CSS, and global JS are injected globally via Code Snippets and Additional CSS, NOT embedded in each page.
25. Read `references/agent-enforcement-rules.md` for the binding enforcement framework. This governs ALL agent behavior 鈥?no autonomous decisions, no method switching, no shortcuts, verification gate after every step. The agent MUST follow these rules at all times.
26. Read `references/wordpress-plugins-themes-guide.md` for comprehensive WordPress core settings, WooCommerce settings, Elementor settings, Code Snippets configuration, Hello Elementor theme details, WordPress database structure, REST API, hook system, template hierarchy, user roles, and common security/performance/image optimization plugin settings. Use as the authoritative reference when configuring any plugin, theme, or WordPress setting.
27. Use `scripts/site_plan.py` when a structured intake JSON needs to be validated or converted into a phase checklist.
28. Use `scripts/rank_math_content_audit.py` before Rank Math metadata writing to check focus keyword placement, subheadings, image ALT, keyword density, internal links, readability, and rich media.
29. Use `scripts/rank_math_meta_writer.py` to generate a Code Snippets one-time writer from an approved SEO mapping JSON for Rank Math Free sites.
29a. Use `scripts/reference_site_capture.py` before reference-site/clone-style builds to capture public/authorized HTML snapshots and generate a page-type manifest.
29b. Use `scripts/convert_product_prices.py` before WooCommerce CSV import when source prices and target WooCommerce currency differ.
30. Use `scripts/resume_ledger.py` to initialize, update, summarize, and recover a resumable build ledger after interruptions.
31. Read `references/code-snippets-implementation-guide.md` for REAL, ready-to-use Code Snippets code. Contains WordPress core configuration, WooCommerce customizations, performance optimization, SEO enhancements, dynamic product renderers, security hardening, custom shortcodes, age/compliance gate, cookie consent, and custom REST API endpoints. Use these snippets instead of writing code from scratch.
32. Read `references/wordpress-settings-implementation.md` for practical WordPress/WooCommerce/Elementor/Rank Math settings configuration via REST API and Code Snippets PHP. Contains exact curl commands and PHP code for configuring shipping zones, payment gateways, menus, and all settings programmatically.
33. Read `references/woocommerce-customizations-guide.md` for production-ready WooCommerce customizations. Contains product page UX (trust badges, stock urgency, delivery date, countdown timer, variation swatches, sticky add-to-cart), cart customizations (cross-sells, empty cart), checkout customizations (two-column layout, trust signals, validation, thank you page), email customizations, and account page customizations.

## Operating Rules

- **Do not make decisions without user approval.** When in doubt, ask the user. See the CRITICAL section above for details.
- Treat WooCommerce as the source of truth for Shop, Cart, Checkout, My Account, products, variations, categories, prices, stock, and purchase flow.
- Do not make `/shop/` a custom Elementor page full of static HTML. It should be bound as the WooCommerce shop page and use the normal product archive loop.
- Use Elementor HTML blocks for page shells only. Keep dynamic products/posts in WordPress/WooCommerce/PHP snippets, not hardcoded into static HTML.
- For Elementor pages, set Page Layout to `Elementor Canvas` before inserting the HTML widget, except WooCommerce-owned pages such as Shop, Cart, Checkout, and My Account. **This is a DEAD RULE 鈥?see "CRITICAL: Four Dead Rules for Page Building" above.** Canvas must be set, saved, and verified BEFORE adding any HTML widget. If the theme header/footer still appears after setting Canvas, it was not set correctly 鈥?fix before proceeding.
- **When HTML payload is large (>30,000 characters) or paste fails, use batch import.** Split into batches at natural HTML boundaries, append to the same HTML widget, verify after each batch. **This is a DEAD RULE 鈥?see "CRITICAL: Four Dead Rules for Page Building" above.**
- **Age verification gate MUST be a global Code Snippets PHP snippet using `wp_footer` hook. NEVER place age gate HTML/CSS/JS in any Elementor HTML widget.** **This is a DEAD RULE 鈥?see "CRITICAL: Four Dead Rules for Page Building" above.**
- **For BOTH new sites AND old site rebuilds, regenerate and bind WooCommerce pages.** WooCommerce 鈫?Status 鈫?Tools 鈫?"Install pages", then bind page IDs via Code Snippets PHP. **This is a DEAD RULE 鈥?see "CRITICAL: Four Dead Rules for Page Building" above.**
- **Homepage and Blog pages MUST use dynamic data via Code Snippets PHP.** Never hardcode product names, prices, images, or article titles in page HTML. Use `wc_get_products()` / `WP_Query` to fetch real data into containers. **This is a DEAD RULE 鈥?see "CRITICAL: Additional Dead Rules" above.**
- **Use real product images from the media library in page HTML.** Ask the user which products to feature. Never use placeholder/stock/fake images. All images must be WebP. **This is a DEAD RULE 鈥?see "CRITICAL: Additional Dead Rules" above.**
- **Follow the step-by-step import order: global shell first, then global CSS, then global JS, then page HTML one at a time, then dynamic renderers.** Never import page HTML before the global shell is active. **This is a DEAD RULE 鈥?see "CRITICAL: Additional Dead Rules" above.**
- **After all pages are built, perform global SEO, speed, and WebP optimization.** Rank Math metadata for all content. Disable cart fragments on non-shop pages. Convert ALL images to WebP. Verify PageSpeed mobile 90+. **This is a DEAD RULE 鈥?see "CRITICAL: Additional Dead Rules" above.**
- Use a resumable page ledger: each page has status `created`, `canvas_set`, `html_inserted`, `updated`, `verified`. If one step fails, resume from the failed step instead of deleting and starting over.
- **Create all pages first, then generate HTML code with correct page paths.** Never write HTML with links to non-existent pages.
- Generate homepage and blog page containers such as `data-site-render="home-products"`, `data-site-render="home-posts"`, and `data-site-render="blog-posts"`; adapt names per project.
- Generate content-rich dynamic modules where useful, such as product-image sliders, collection/category grids, comparison strips, guide hubs, FAQ accordions, support callouts, and contextual product/article links. Choose modules from the target market and product knowledge ledger; do not apply the same homepage/page module stack to every site.
- Create and bind WordPress menus automatically: primary/header menu, mobile menu if separate, and footer policy/support menu.
- Establish global site settings, Rank Math baseline, permalink settings, WooCommerce page bindings, and menu locations before large page HTML imports.
- Before full-site buildout, generate one homepage style preview from the real brand/products/content and get user approval. Do not bulk-build pages until the preview is approved or the user explicitly waives the gate.
- The homepage preview must be substantial: header, footer, mobile behavior, hero, product/category areas, rich merchandising modules using real product images/links when available, ordering/payment/shipping/compliance sections, FAQ or guide teaser, and enough sections for the user to judge density.
- Make output feel hand-built and site-specific. Avoid generic AI phrasing, over-explaining sections, repetitive card grids, vague superlatives, fake testimonials, and template-looking gradients.
- **Apply global design preferences** based on the target market. Read `references/global-design-preferences.md` for regional color, layout, trust, payment, and content conventions.
- When editing a WooCommerce product export CSV, preserve technical identity fields such as product ID, type, SKU, slug, parent, attributes, stock, prices, images, categories, and variation relationships unless the user explicitly asks to change them.
- Product CSV originality work may rewrite product names/titles, short descriptions, long descriptions/body/content, image alt-related fields if present, and Rank Math SEO meta fields; keep claims compliant and product-specific.
- Classify snippets as `persistent`, `one_time_writer`, `read_only_scanner`, `ux_polish`, or `deprecated`. One-time writers and scanners must be disabled after use.
- Do not rewrite stable pages just to improve Rank Math scores. Put serious SEO content in product long descriptions, category descriptions, blog posts, image ALT text, and metadata.
- Make layouts visibly different across projects and article batches. Never clone the previous site palette, section order, card shapes, or hero composition unless the user asks.
- Keep verified pages stable. Patch the specific issue instead of regenerating the whole page.
- **No stacked code.** Each page must load only the CSS and JS it needs. Use conditional loading, scoped class names, and Elementor optimized CSS/JS loading.
- **All images must be WebP format.** Convert all existing images to WebP. Use image optimization plugins (Smush, ShortPixel, Imagify) for automatic conversion.
- **Verify every link, image, button, and menu item on both desktop and mobile.** No 404s allowed. Every interactive element must be tested.
- Verify mobile behavior, add-to-cart, checkout gates, permalinks, sitemap, robots, SEO metadata, image ALT, cache clearing, and HTTP status before final delivery.
- For regulated or sensitive products, avoid medical, health, safety, cessation, guaranteed result, or illegal-use claims. Add age/compliance language where appropriate.
- Follow Google SEO guidelines strictly. Read `references/google-seo-guidelines.md` for E-E-A-T, spam policies, and content quality requirements.
- Follow Rank Math best practices. Read `references/rank-math-seo-guide.md` for module configuration and product SEO mapping.
- Ensure Core Web Vitals pass. Read `references/core-web-vitals-guide.md` for LCP, INP, CLS optimization.
- Implement structured data correctly. Read `references/structured-data-guide.md` for Schema markup and rich results.
- Follow ecommerce SEO best practices. Read `references/ecommerce-seo-guide.md` for WooCommerce-specific SEO.
- **Every article must be created as a draft first and reviewed by the user before publishing.** Send the draft link to the user and wait for approval. Read `references/scheduled-article-publishing.md`.
- **After QA passes, present post-build actions to the user.** Do not skip the post-build recommendation step. Read `references/post-build-actions.md`.
- **Article topics must be based on the site's actual products, target market, and language.** Never generate unrelated content. Understand the site context before generating articles.
- **Article images must be real product images from the media library.** No stock photos, no placeholders, no 404s. All images in WebP format.
- **Article internal links must point to real, published product pages.** Use descriptive anchor text, not "click here". Links must be prominent and visually distinct.
- **Scheduled publishing must ensure continuous content flow.** Ask user for frequency, days, time, and timezone. Ensure coverage for at least 3-6 months.
- **Every step must be executed carefully and in order.** No skipping, no combining, no reordering, no switching methods. This is a hard rule. If a step fails, fix and retry before proceeding.
- **Detect and handle SiteGround hosting challenges.** Read `references/siteground-bypass-guide.md`. Do NOT switch to alternative methods when encountering CAPTCHA, IP blocks, or WAF. Follow the defined handling procedure.
- **For old site rebuilds, follow the 13-step cleanup procedure.** Read `references/old-site-rebuild-procedure.md`. Preserve only products and media library. Clear everything else. Verify each step before proceeding.
- **Use global shell architecture for header, footer, CSS, and JS.** Read `references/global-shell-architecture.md`. Header and footer are injected via Code Snippets PHP hooks (`wp_body_open` and `wp_footer`). Global CSS goes in Additional CSS. Global JS goes in Code Snippets. Page HTML contains only page-specific content 鈥?no header, no footer, no global CSS/JS.
- **Never embed header/footer/menu HTML in individual page HTML widgets.** The global shell handles all shared elements. Each Elementor HTML page contains only page-unique content, scoped CSS, and scoped JS.
- **The agent is bound by the enforcement framework in `references/agent-enforcement-rules.md`.** No autonomous decisions, no method switching, no shortcuts, verification gate after every step, three-strike rule, progress reporting, no silent actions.
- **When configuring any WordPress plugin, theme, or core setting, consult `references/wordpress-plugins-themes-guide.md` for the correct option keys, default values, and REST API endpoints.** Never guess option keys or setting names.
- **Never use hardcoded values when dynamic queries are available.** Use WordPress/WooCommerce queries, REST API, and `wp_nav_menu()` for dynamic data. Never hardcode product IDs, menu links, or page URLs when they can be queried.
- **Never use fake, placeholder, or mock data.** All data must be real. If real data is unavailable, STOP and ask the user 鈥?do not substitute fake data.

## Standard Workflow

Run these phases in order unless repairing an existing site:

0. **Determine build type**: Ask the user if this is a new build or a rebuild of an existing site.
   - If new build: Start from Phase 1.
   - If rebuild: Read `references/old-site-rebuild-procedure.md` and execute the 13-step cleanup procedure FIRST. Confirm with user, back up, preserve products and media, clear everything else. After cleanup verification, continue from Phase 1.
1. **Prerequisite check**: Verify all required plugins, themes, SSL, and PHP version. Read `references/prerequisite-checklist.md`. Do not proceed until all pass. Detect if site is on SiteGround hosting 鈥?if so, read `references/siteground-bypass-guide.md` and configure SG Optimizer for Elementor compatibility.
2. **Collect requirements and credentials handling plan**: Read `references/intake-checklist.md` and `references/global-design-preferences.md`. Ask for target market, language, design preferences.
3. **Inspect WordPress**: Check theme, plugins, WooCommerce, Rank Math, SSL, permalinks, cache, and existing pages.
4. **Set baseline**: Permalink, homepage/blog reading settings, WooCommerce page bindings, Rank Math global basics (Advanced Mode, sitemap, schema, noindex), cache strategy, header menu, footer menu, and global snippet plan. Read `references/site-baseline-and-menus.md` and `references/rank-math-seo-guide.md`. **DEAD RULE: Regenerate WooCommerce pages (WooCommerce 鈫?Status 鈫?Tools 鈫?"Install pages") and bind page IDs via Code Snippets PHP for BOTH new and old sites.**
5. **Create all pages first** (as draft): Home, Shop, Blog, Contact, Cart, Checkout, My Account, policies, FAQ, About, age/compliance page. Read `references/wordpress-elementor-structure.md` for page slugs and URL paths. Build URL map. **After creating pages, re-run WooCommerce page regeneration and binding to ensure all page IDs are correct.**
6. **Inspect product knowledge before preview/content**: If products already exist or the user provided a WooCommerce CSV, inspect products/CSV and create a product knowledge ledger before homepage preview, page HTML, article planning, or SEO mapping. Read `references/product-csv-originality-seo.md`.
7. **Generate homepage style preview** using real site inputs, product/category signals from the product knowledge ledger, proposed navigation, and scoped HTML/CSS. Apply global design preferences for the target market. Pause for user approval. Read `references/style-preview-gate.md`.
8. **After approval, set Elementor Canvas only for custom pages**. Read `references/elementor-html-automation.md`. Use the URL map for all links. Verify no 404s and verify Canvas removes theme chrome. **Do NOT import page HTML yet. DEAD RULE: global shell must be active and verified before any page HTML is pasted.**
9. **Product CSV rewriting/import prep**: If the user provides a WooCommerce product export CSV, rewrite product titles/descriptions/body content for originality, fill Rank Math product SEO fields, preserve import-critical identifiers, and produce a re-import-ready CSV plus change report. The schema inspection and product knowledge ledger must already be complete before homepage preview/content generation. Read `references/product-csv-originality-seo.md` and `references/rank-math-seo-guide.md`.
10. **Create product categories, attributes, products, variations**: SKU, slugs, prices, stock, images, galleries, and catalog visibility. Ensure all images are WebP.
11. **Generate global shell (MUST be done BEFORE page HTML)**: Read `references/global-shell-architecture.md`. Create global header via Code Snippets PHP hook (`wp_body_open`), global footer via `wp_footer` hook, global CSS in Appearance 鈫?Customize 鈫?Additional CSS, global JS in Code Snippets. Include mobile menu, search, compliance notice, dynamic home/blog renderers. Use clean, lightweight, scoped code. NEVER embed header/footer in individual page HTML. **DEAD RULE: Global shell must be active and verified on front-end BEFORE any page HTML is imported. See "CRITICAL: Additional Dead Rules" Dead Rule 7.**
12. **Generate page HTML (one page at a time)** for Home, Blog, Contact, policies, FAQ, and About using one Elementor HTML block per page. Each page contains ONLY page-specific HTML, scoped CSS (`.page-name .class`), and scoped JS (IIFE). No header, no footer, no menu, no global CSS/JS 鈥?the global shell handles all shared elements. Each page loads only its own CSS/JS. **DEAD RULE: Homepage and Blog MUST use dynamic data containers (`data-site-render="home-products"`, etc.) filled by Code Snippets PHP 鈥?never hardcode product/article data. See "CRITICAL: Additional Dead Rules" Dead Rule 5.** **Import one page at a time: Canvas 鈫?verify 鈫?HTML widget 鈫?paste 鈫?Update 鈫?verify front-end 鈫?next page.**
13. **Add product page UX** only as a reversible snippet layer that preserves WooCommerce variation events.
14. **Add cart/checkout rules** such as minimum quantity, shipping/address notices, terms defaults, and duplicate-message cleanup.
15. **Add site-wide age/compliance gate** when required without hiding crawlable content in a way that blocks search indexing. **DEAD RULE: Age gate MUST be a global Code Snippets PHP snippet using `wp_footer` hook 鈥?NEVER in any Elementor HTML widget. See "CRITICAL: Four Dead Rules" Dead Rule 2.**
16. **Write Rank Math metadata** with one-time writers; noindex Cart, Checkout, and My Account; index products, categories, posts, and policy pages. Read `references/rank-math-seo-guide.md`.
17. **Implement structured data**: Product schema, Article schema, FAQPage schema, BreadcrumbList schema. Read `references/structured-data-guide.md`.
18. **Generate SEO content**: product long descriptions, category descriptions, blog posts, internal links, outbound references, and image ALT/title metadata. Read `references/google-seo-guidelines.md` and `references/ecommerce-seo-guide.md`.
19. **Convert all images to WebP (MANDATORY DEAD RULE)**. Use image optimization plugin or batch conversion. Verify all images load correctly. **DEAD RULE: ALL images 鈥?products, galleries, categories, blog posts, page banners, logo 鈥?must be WebP. See "CRITICAL: Additional Dead Rules" Dead Rule 8.**
20. **Optimize Core Web Vitals (MANDATORY DEAD RULE)**: LCP, INP, CLS. Disable WooCommerce cart fragments on non-shop pages. Defer third-party scripts. Read `references/core-web-vitals-guide.md`. **DEAD RULE: PageSpeed mobile 90+, LCP < 2.5s, INP < 200ms, CLS < 0.1. See "CRITICAL: Additional Dead Rules" Dead Rule 8.**
21. **Run full QA**: Read `references/qa-and-launch.md`. Verify every link, image, button, and menu on desktop AND mobile. Check for 404s. Verify code quality (no stacked code, per-page loading). Check performance metrics. **Verify all DEAD RULES were followed: Canvas set on all custom pages, age gate in Code Snippets (not page HTML), WooCommerce pages regenerated and bound, dynamic data containers on homepage/blog, all images WebP, no hardcoded product data.**
22. **Generate SEO articles**: Read `references/scheduled-article-publishing.md`. Generate a batch of 10-20 SEO-optimized articles based on the site's products, target market, and language. Ask user for: article count, images per article (default 4-8), internal links per article (default 3-5), publishing frequency, days, time, and timezone. Create all articles as drafts. Send draft links to user for review. After approval, schedule publish dates to ensure continuous publishing for 3-6 months. Set Rank Math SEO metadata (title, description, focus keyword, Article schema, FAQPage schema) for each article.
23. **Prepare sitemap/indexing package** and final launch report.
24. **Present post-build actions**: Read `references/post-build-actions.md`. Present the 4 post-build action recommendations to the user: (1) Scheduled article publishing plan, (2) Search engine index submission, (3) Analytics and monitoring setup, (4) Social media auto-sharing. Wait for user to choose which actions to proceed with. Do NOT start any action without user confirmation.
25. **For ongoing SEO**, generate new article batches with varied layouts, product images, internal links, and Search Console follow-up tasks.

## WordPress Automation Choices

Prefer the lowest-risk available path:

- WP REST API or WooCommerce REST API with application passwords for structured create/update work.
- wp-admin in browser/Chrome/Computer Use when the site blocks APIs, uses custom plugin screens, or requires Elementor/Code Snippets UI.
- Generated `.md` code files when the user wants manual paste into Code Snippets or Elementor.
- Local HTML prototypes when the design direction is uncertain or before touching a live site.

Never pretend a live change was made unless it was actually executed and verified. If access fails because of CAPTCHA, WAF, 2FA, missing plugin, or permission limits, state the blocker and provide the safest next artifact.

## Deliverables

Use `references/deliverables.md` when packaging output. For code-heavy work, create files instead of pasting long snippets into chat. Name files by site and purpose, for example:

- `<site>-global-shell-v1.md`
- `<site>-home-html-v1.md`
- `<site>-checkout-rules-v1.md`
- `<site>-rankmath-meta-writer-v1.md`
- `<site>-seo-qa-scanner-v1.md`
- `<site>-launch-report.md`

Each snippet file must say whether it is persistent, one-time, scanner, UX polish, or deprecated, and whether to keep it enabled or disable it after execution.

## References

### Core Build References
- `references/prerequisite-checklist.md`: MANDATORY pre-build verification. Check plugins, themes, SSL, PHP before any work begins.
- `references/intake-checklist.md`: fields to collect and default assumptions.
- `references/phase-playbook.md`: full build and repair sequence.
- `references/ai-agent-compatibility.md`: universal AI coding tool compatibility, anti-skip protocol, capability fallback matrix, and critical-judgment rules.
- `references/site-baseline-and-menus.md`: global settings, Rank Math baseline, navigation, footer menus, WooCommerce page binding.
- `references/elementor-html-automation.md`: Elementor Canvas and HTML-widget automation for old and new Elementor UI.
- `references/style-preview-gate.md`: homepage style preview, approval gate, and anti-AI review rules.
- `references/product-csv-originality-seo.md`: WooCommerce product export CSV rewriting, import safety, and Rank Math product SEO mapping.
- `references/reference-site-capture.md`: reference-site/clone-style capture, page-type classification, HTML snapshot handling, WordPress mapping, and transformation rules.
- `references/design-variation.md`: reusable but non-repetitive design system rules.
- `references/automation-and-safety.md`: credentials, API/admin choices, snippets, rollback.
- `references/qa-and-launch.md`: storefront, SEO, mobile, link/button/image verification, WebP, code quality, performance, indexing, and launch checks.
- `references/deliverables.md`: file packaging and final reporting format.

### SEO Knowledge References
- `references/google-seo-guidelines.md`: comprehensive Google SEO official guidelines 鈥?E-E-A-T, spam policies, content quality, site organization, international SEO, structured data overview.
- `references/rank-math-seo-guide.md`: complete Rank Math configuration 鈥?all modules, Titles & Meta, sitemap, schema templates, WooCommerce product SEO, on-page 100/100 guide, CSV SEO field mapping.
- `references/core-web-vitals-guide.md`: LCP/INP/CLS optimization, WordPress performance stack, Elementor optimization, WooCommerce INP fixes, measurement tools.
- `references/structured-data-guide.md`: Schema markup implementation 鈥?Product, Article, FAQ, Breadcrumb, Organization, LocalBusiness, JSON-LD templates, Rank Math schema configuration, validation tools.
- `references/ecommerce-seo-guide.md`: WooCommerce SEO 鈥?product pages, category pages, internal linking, blog content strategy, technical SEO, conversion optimization, QA checklist.

### Structure and Design References
- `references/wordpress-elementor-structure.md`: WordPress page types, slugs, template hierarchy, shortcodes, Elementor structure, settings, widgets, page creation workflow, URL mapping.
- `references/global-design-preferences.md`: regional design preferences for 10+ global markets 鈥?colors, layout, trust signals, payment methods, content style, cultural habits, legal requirements.

### Content and Post-Build References
- `references/scheduled-article-publishing.md`: scheduled article publishing, draft-review-then-publish workflow, article topic generation, SEO content structure, product image and internal link requirements, Rank Math article metadata, scheduling configuration, E-E-A-T content quality standards.
- `references/post-build-actions.md`: post-build action guide 鈥?scheduled article publishing plan, search engine index submission, analytics and monitoring setup, social media auto-sharing, checklists and user communication templates.

### Hosting and Rebuild References
- `references/siteground-bypass-guide.md`: SiteGround server handling 鈥?CAPTCHA challenges, IP blocking, WAF configuration, SG Optimizer caching, rate limiting, error recovery, prevention strategies, quick-fix table. Read when the site is hosted on SiteGround.
- `references/old-site-rebuild-procedure.md`: old site rebuild procedure 鈥?13-step cleanup workflow preserving products and media library, clearing all pages/posts/menus/snippets/CSS/Elementor templates/widgets/settings. Read when rebuilding an existing site.
- `references/global-shell-architecture.md`: global shell architecture 鈥?header via `wp_body_open` hook, footer via `wp_footer` hook, global CSS in Additional CSS, global JS in Code Snippets, page HTML contains only page-specific content. Read before creating any page HTML.

### Enforcement and Configuration References
- `references/agent-enforcement-rules.md`: binding enforcement framework 鈥?no autonomous decisions, no method switching, no shortcuts, verification gate after every step, three-strike rule, progress reporting, user override only, data integrity rules, code quality enforcement, phase gate enforcement, anti-deviation safeguards. The agent MUST follow these rules at all times.
- `references/wordpress-plugins-themes-guide.md`: comprehensive WordPress reference 鈥?core settings (General, Reading, Permalinks, Media, Discussion), database structure (12 tables), REST API endpoints and authentication, hook system (actions, filters, common hooks), template hierarchy, user roles and capabilities, WooCommerce settings (all tabs, option keys, defaults, REST API, shortcodes, page bindings), Elementor settings (Settings, Experiments, Site Settings, Page Settings, data structure, widget types), Code Snippets (types, fields, hooks, auto-insert positions, conditions), Hello Elementor theme (features, menu locations, widget areas, assets, customizer, child theme), WordPress theme structure (files, style.css header, functions.php, child themes), common security plugins (Wordfence, Sucuri, iThemes, AIOS), performance plugins (WP Rocket, W3TC, WP Super Cache, LiteSpeed, SG Optimizer), image optimization plugins (Smush, ShortPixel, Imagify, EWWW).

### Implementation and Customization References
- `references/code-snippets-implementation-guide.md`: REAL, ready-to-use Code Snippets code library 鈥?WordPress core configuration (permalinks, reading settings, media sizes, disable comments, disable emojis, remove WP version, custom login page, custom admin dashboard), WooCommerce customizations (settings, page bindings, add-to-cart text, free shipping bar, minimum order, custom checkout fields, product tabs, recently viewed, auto-complete virtual orders, email templates), performance optimization (disable cart fragments, defer JS, remove query strings, preconnect, disable dashicons, lazy load), SEO enhancements (meta robots, OpenGraph tags, breadcrumbs, FAQPage schema), dynamic renderers (featured products grid, recent posts grid), security hardening (disable file edit, login attempt limiter, hide login errors, block user enumeration), custom shortcodes (contact info, product categories grid, trust badges), age/compliance gate, GDPR cookie consent banner, custom REST API endpoints.
- `references/wordpress-settings-implementation.md`: practical settings configuration guide 鈥?WordPress core settings via REST API (read/update), WooCommerce settings via REST API (general, products, accounts, shipping zones, payment gateways), WooCommerce shipping zone creation via REST API and Code Snippets PHP, payment gateway configuration (BACS, COD, Stripe) with bank account details, Elementor configuration via Code Snippets (CPT support, CSS print method, experiments, Flexbox Container, optimized loading, global colors/fonts, canvas page templates), Rank Math SEO configuration via Code Snippets (general, titles & meta, sitemap, schema, noindex for WC pages), WordPress menu creation via REST API and Code Snippets PHP, wp-config.php essential additions, .htaccess security headers, Gzip, browser caching, and file protection.
- `references/woocommerce-customizations-guide.md`: production-ready WooCommerce customizations 鈥?product page (trust badges under price, stock urgency counter, estimated delivery date, sale countdown timer, color/size variation swatches, sticky add-to-cart bar on mobile), cart (cross-sell products, custom item display, empty cart with featured products), checkout (two-column layout, trust signals, phone validation, custom thank you page), emails (logo header, first-time customer welcome email), product loop (custom sale badge with percentage, quick view button, infinite scroll/load more), account page (custom dashboard with order stats and quick links).
