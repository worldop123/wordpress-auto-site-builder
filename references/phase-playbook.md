# Phase Playbook

Use this order for a new build. For repair work, identify the current phase, inspect existing state, and continue from the smallest safe phase.

## CRITICAL: Enforcement Framework

Before starting any phase, read `agent-enforcement-rules.md`. The agent is bound by these rules throughout all phases:
- Interaction mode controls decisions: `ask_user` asks when uncertain; `autonomous` is allowed only after explicit user authorization and must record AI decisions instead of stopping for routine approvals.
- No method switching — follow defined procedures
- No shortcuts — execute and verify every step
- Verification gate after every step — Execute → Verify → Record → Gate
- Phase gate — before moving to the next phase, verify all steps completed and verified
- Progress reporting — after each step, report what was done, what was verified, and what is next
- When configuring any plugin/theme/setting, consult `wordpress-plugins-themes-guide.md` for correct option keys

## 0. Prerequisite check and build type determination (MANDATORY)

### 0r. Resume after interruption

If the task is resumed after an AI/tool/server/browser/network interruption, do this before any write action:

1. Read the latest website task ledger and skill task ledger if available.
2. Identify the last verified phase gate, not merely the last attempted step.
3. Re-check current live state read-only:
   - Pages and page IDs.
   - WooCommerce page bindings.
   - Active/inactive snippets.
   - Product/category/media counts.
   - Article IDs/statuses/scheduled dates.
   - Menus, homepage/blog settings, Rank Math sitemap state.
   - Cart, checkout, and product page availability.
4. Compare live state with the ledger and mark mismatches.
5. Revoke or rotate temporary credentials created before the interruption.
6. Continue from the smallest safe unfinished step.

Do not repeat old-site cleanup, product CSV imports, media imports, article publishing, page deletion, snippet replacement, or launch/indexing actions unless the read-only recovery check proves they are incomplete or broken.

### 0a. Determine service mode

The first user-facing step is to list the three primary service choices and record one value in `site.build_mode`:

1. **New site build** (`new`): build a new WordPress/WooCommerce SEO site from requirements.
2. **Old-site rebuild** (`old_rebuild`): rebuild an existing site while preserving protected WooCommerce products, product data, and media.
3. **Existing-site SEO optimization** (`existing_seo_optimization`): do not redesign or rebuild pages; audit and optimize SEO data for the current pages, products, posts, categories, media, Rank Math settings, schema, sitemap, image ALT text, and internal-link gaps.
4. **Reference-site inspired build / clone-style adaptation** (`reference_site_clone`): capture a public or authorized reference site's page HTML snapshots, analyze all relevant page types, and rebuild transformed WordPress/WooCommerce pages with the user's own brand/content/assets.

In `ask_user` mode, show these choices and wait for the user's selection before changing the site. In `autonomous` mode, infer the service mode from the user's wording, record the reason, and continue with the safest branch.

- **If new build**: Continue to 0b.
- **If rebuild**: Read `old-site-rebuild-procedure.md` and execute the 13-step cleanup procedure FIRST.
  - Confirm with user before starting cleanup — tell them exactly what will be deleted and preserved.
  - Back up before cleanup — export all WordPress content and WooCommerce products.
  - PRESERVE: WooCommerce products, product categories/tags/attributes, media library images.
  - CLEAR: All pages (except WooCommerce-owned), all blog posts, all menus, all Code Snippets, all Elementor templates, all custom CSS, all widgets, WooCommerce settings, orders, coupons.
  - Execute all 13 cleanup steps in order. No skipping. Each step must be verified before proceeding.
  - After cleanup, verify product data integrity before continuing.
  - After cleanup verification, continue to 0b.
- **If existing-site SEO optimization**: Continue to 0b, then follow "Existing-site SEO optimization flow" in Phase 10. Do not run old-site cleanup, create replacement layouts, overwrite Elementor pages, change WooCommerce commerce data, or regenerate the visual design unless the user separately approves repair work.
- **If reference-site clone/adaptation**: Read `reference-site-capture.md`, capture authorized/public HTML snapshots to a gitignored folder, produce a page-type analysis report, then continue through the build phases using transformed layouts and original user content. Do not publish copied third-party HTML, text, images, logos, product data, reviews, policies, trackers, or private endpoints.

### 0b. Prerequisite verification

Read `prerequisite-checklist.md` and verify ALL prerequisites before any work begins:
- Hello Elementor theme active.
- Rank Math SEO installed, activated, and configured in Advanced Mode.
- If Rank Math is being used on this site for the first time, tell the user to connect the relevant Rank Math account in the setup wizard/account screen. Record whether it was connected, skipped by user choice, or blocked.
- Elementor installed and activated.
- WooCommerce installed and activated (for ecommerce).
- Code Snippets installed and activated.
- SSL/HTTPS enabled.
- PHP 8.0+ (8.1+ recommended).

If any prerequisite is missing, STOP and provide installation instructions to the user. Do NOT proceed until all prerequisites pass. Do NOT install plugins without user permission, except when `interaction_mode` is `autonomous` or explicit plugin-install permission is already recorded. For existing-site SEO optimization, Code Snippets may be installed/activated automatically only under that same autonomous/authorized condition.

### 0c. SiteGround detection

During environment inspection, detect if the site is hosted on SiteGround:
- Check for SG Optimizer plugin active.
- Check for Site Tools references in wp-admin.
- Check server software headers.

If SiteGround is detected:
- Read `siteground-bypass-guide.md` for the complete handling guide.
- Configure SG Optimizer for Elementor compatibility (enable Dynamic Cache, Memcached, HTTPS Enforce, Gzip, Browser Caching, CSS/JS Minify, Defer JS; do NOT enable Combine CSS or Combine JS).
- Add 2-5 second delays between automated actions to avoid triggering bot detection.
- Use REST API with application passwords as the preferred access method.
- If CAPTCHA or verification challenge appears: STOP, notify user, wait for manual resolution. Do NOT retry or switch methods.

## 1. Requirements and site_config

- Read `intake-checklist.md` and `global-design-preferences.md` before asking the user for information.
- Determine and record interaction mode:
  - `ask_user`: ask for approvals and pause at required gates.
  - `autonomous`: if the user explicitly authorized no-question execution, choose target market/language/layout/article defaults from the available details and continue while preserving protected data.
- Ask for target market/country, language, design preferences, and payment method requirements.
- Convert user answers into a structured `site_config`.
- Mark unknowns explicitly.
- Ask only for unknowns that block execution or could cause a harmful live change.

### 1a. Product understanding gate for CSV-backed builds

If the user provides a WooCommerce product CSV, inspect it before generating homepage previews, page HTML, category copy, article topics, or Rank Math SEO mappings. Product understanding is an upstream content dependency, not only an import step.

Required product knowledge ledger:

- CSV file name, encoding, delimiter, parser quality, row count, column count, and product type counts.
- Product/category/tag/attribute summary, including simple vs variable product mix and variation parent health.
- Representative products, priority categories, price range, currency context, sale-price relationships, stock/publish/catalog visibility signals, and shipping/compliance clues.
- Existing short descriptions, long descriptions, body/detail images, featured/gallery image coverage, Rank Math fields, and custom meta policies.
- Content opportunities for homepage sections, shop/category copy, product page trust blocks, FAQ/policy wording, article topics, internal links, focus keywords, and image ALT text.
- Protected fields that must not be rewritten or used as assumptions.

Do not proceed to style preview, page HTML, article generation, or SEO metadata writing until this ledger exists and CSV blockers are resolved. If no CSV is provided, build the same understanding from live WooCommerce products before generating SEO-sensitive content.

## 2. Environment inspection

Check:

- WordPress accessible and SSL valid.
- Theme is Hello Elementor or compatible.
- Elementor, WooCommerce, Rank Math, Code Snippets, and cache plugin states.
- Pages exist and publish status.
- WooCommerce page bindings.
- Permalink settings.
- Existing snippets and their active/inactive status.
- Existing products, categories, posts, policies, and media.

Output a concise environment report before live edits.

## 3. Page creation and binding

Before importing Elementor HTML, read `site-baseline-and-menus.md` and `wordpress-elementor-structure.md` and complete the baseline pass:

- Permalinks.
- Homepage/posts page settings.
- WooCommerce page bindings.
- Rank Math global/noindex baseline.
- Header/primary menu.
- Footer/support menu.
- Cache clearing method.

### Foundation baseline gate

Do not style or import content until the foundation is verified:

- Core settings: SSL, permalink structure, site language/timezone, homepage/blog setting, media sizes, comment defaults.
- WooCommerce: Shop, Cart, Checkout, My Account, and Terms pages exist, contain correct WooCommerce content, and are bound to WooCommerce options.
- Store operations: currency, selling countries, shipping zone/rates/notices, tax display, COD/payment gateways, account/guest checkout, order emails.
- Navigation and shell: logo uploaded, primary/footer menus created, header/footer snippets active, cart count visible, policy links valid.
- Snippet health: no duplicate quantity/cart handlers, no checkout hijacker, no floating widget overlap, no active discount rule that changes prices unexpectedly.
- URL health: home, shop, product archive, product category archive, single product, blog/archive, single post, cart, checkout, my account, and policy pages return 200.

Record a foundation ledger. If cart controls freeze, checkout is hijacked, or WooCommerce page bindings are wrong, fix the foundation before building page designs.

### DEAD RULE: WooCommerce Page Regeneration (MANDATORY for ALL sites — new AND rebuild)

Before full page buildout, the agent MUST regenerate and bind WooCommerce pages. This applies to BOTH new builds and old site rebuilds. No exceptions.

1. **Regenerate WooCommerce pages**: Go to WooCommerce → Status → Tools → Click "Install pages" (or "Create default WooCommerce pages"). This creates or updates Shop, Cart, Checkout, My Account, and Terms pages with correct WooCommerce shortcodes.
2. **Bind WooCommerce pages programmatically**: Create a Code Snippets PHP snippet (one_time_writer) that uses `update_option()` to bind page IDs:
   - `woocommerce_shop_page_id` → Shop page ID
   - `woocommerce_cart_page_id` → Cart page ID
   - `woocommerce_checkout_page_id` → Checkout page ID
   - `woocommerce_myaccount_page_id` → My Account page ID
   - `woocommerce_terms_page_id` → Terms page ID
3. **Verify bindings**: Check WooCommerce → Settings → Advanced — all page selectors must show the correct pages. If any selector is empty or wrong, rebind.
4. **For old site rebuilds**: After the 13-step cleanup, WooCommerce page bindings are likely broken. This step is CRITICAL — do NOT skip it.
5. **For new sites**: After creating all pages, this step ensures WooCommerce knows which pages to use.
6. **Record**: `"woocommerce_pages_regenerated": true` and `"woocommerce_pages_bound": true` in the build ledger.

Read `code-snippets-implementation-guide.md` Section 2.2 for the exact binding code.

Before full page buildout, read `style-preview-gate.md` and generate one homepage style preview. If a product CSV or live products are available, the preview must use the product knowledge ledger. Pause for approval unless the user explicitly waived the gate. Use the approved preview as the source of truth for visual language, spacing, menu emphasis, section rhythm, and copy tone.

Create or verify:

- Home `/`
- Shop `/shop/`
- Blog `/blog/`
- Contact `/contact-us/` or project equivalent
- Cart `/cart/`
- Checkout `/checkout/`
- My Account `/my-account/`
- Shipping, Returns, Privacy, Terms, Payment, Cookie, FAQ, About, Age/Compliance pages as needed.

Rules:

- Set Shop as the WooCommerce shop page and leave the page body empty or minimal.
- Bind Cart, Checkout, and My Account to WooCommerce settings and shortcodes/blocks as required by the installed WooCommerce version.
- Make Blog show posts, not static copied article cards.
- Do not overwrite existing verified pages without a user request or clear defect.

### DEAD RULE: Elementor Canvas (MANDATORY for all custom pages)

For Elementor-designed pages, read `elementor-html-automation.md` and use a resumable page ledger. **The agent MUST set Page Layout to Elementor Canvas on EVERY custom page BEFORE adding any HTML widget.** This is a DEAD RULE.

Enforcement procedure for EACH custom page:
1. Create or open the page in Elementor.
2. Set Page Layout to `Elementor Canvas` (see `elementor-html-automation.md` for UI steps).
3. Click Update to save the Canvas setting.
4. Reload the front-end URL — verify NO theme header/footer/menu appears.
5. If theme chrome still appears: Canvas was NOT set correctly. Re-set, Update, re-verify.
6. Record `"canvas_set": true` in the page ledger.
7. Do NOT add the HTML widget or paste page HTML in this phase. Page HTML import happens only after the global shell is active and verified in Phase 5.

**Pages that MUST use Canvas**: Home, Blog, Contact, About, FAQ, Policy pages, Landing pages.
**Pages that MUST NOT use Canvas** (WooCommerce-owned): Shop, Cart, Checkout, My Account, product archives, single product pages.

### DEAD RULE: Batch Import for Large HTML

When a page's HTML payload exceeds ~30,000 characters or paste fails/truncates, use batch import:
1. Split at natural HTML boundaries (between sections).
2. Never split inside an open tag.
3. Use ONE HTML widget — append all batches to the same widget.
4. Verify after EVERY batch (Update → check front-end).
5. CSS in first batch, JS in final batch — never split a `<style>` or `<script>` tag.

Read `elementor-html-automation.md` "DEAD RULE: Batch Import for Large HTML" for the complete procedure.

## 4. Products and categories

If the user provides an official WooCommerce product export CSV, read `product-csv-originality-seo.md` before product import work. Preserve product identity and commerce fields, rewrite only safe customer-facing fields, and prepare Rank Math product SEO data. Validate row count, headers, SKU/parent relationships, and CSV quoting before import.

For every import/update, create a product import ledger:

- Source row count, expected product/variation count, imported/updated count, failed rows, and skipped rows.
- Featured image URL/media ID, gallery image count, inline/body image URLs, and missing-image list per sampled product.
- Long description, short description, tabs/detail HTML, Rank Math fields, categories, tags, attributes, variations, price, stock, and slug verification.
- Front-end sample checks for at least one simple product, one variable product, and one product with multiple gallery/body images.

Configure WooCommerce settings using `wordpress-settings-implementation.md` — use REST API or Code Snippets PHP (`update_option()`) to configure general settings, products tab, accounts & privacy, shipping zones, and payment gateways. Do NOT manually click through WooCommerce settings if programmatic configuration is available.

Create product categories first, then attributes, then products and variations.

Validate:

- Product is published.
- Catalog visibility is shop and search unless intentionally hidden.
- Stock status allows purchase if intended.
- SKU, slug, price, category, image, gallery, and variant options are correct.
- Imported CSV product titles, short descriptions, long descriptions, and Rank Math product SEO fields match the rewritten source.
- Product URL, category URL, Shop listing, add-to-cart, and cart quantity work.

## 5. Global shell and dynamic renderers

### DEAD RULE: Global Shell Must Be Active BEFORE Page HTML Import

The global shell MUST be created, activated, and verified on the front-end BEFORE any page HTML is imported into Elementor. This is a DEAD RULE — see `agent-enforcement-rules.md` Section 11.7.

Step-by-step import order (MANDATORY — no reordering):
1. **Global header** (Code Snippets PHP, `wp_body_open` hook, priority 5) — verify on front-end.
2. **Global footer** (Code Snippets PHP, `wp_footer` hook, priority 10) — verify on front-end.
3. **Global CSS** (Appearance → Customize → Additional CSS) — verify loads on all pages.
4. **Global JS** (Code Snippets HTML/JS, `wp_footer` hook) — verify mobile menu, cart counter, smooth scroll work.
5. ONLY THEN proceed to Phase 6 (Page HTML).

Read `global-shell-architecture.md` for the complete architecture before creating any snippets or page HTML.

Create the global shell using Code Snippets and Additional CSS:

- **Global header**: Persistent Code Snippet PHP using `wp_body_open` hook (priority 5). Renders header HTML with logo, navigation menu (via `wp_nav_menu`), and cart icon on ALL pages.
- **Global footer**: Persistent Code Snippet PHP using `wp_footer` hook (priority 10). Renders footer HTML with footer menu (via `wp_nav_menu`), contact info, payment badges, and copyright.
- **Global CSS**: Added via Appearance → Customize → Additional CSS. Contains CSS variables (design tokens), header styles, footer styles, shared component styles, and responsive breakpoints.
- **Global JS**: Persistent Code Snippet HTML/JS using `wp_footer` hook. Contains mobile menu toggle, cart counter, smooth scroll, analytics, cookie consent.
- Mobile navigation (handled by global JS + global header).
- Search.
- Compliance notice.
- Dynamic homepage product renderer.
- Dynamic homepage/blog post renderer.
- Archive compatibility fixes only when necessary.

Dynamic renderer rules:

- Use WordPress/WooCommerce queries server-side.
- Do not hardcode product IDs unless the user requested a curated featured set.
- Escape output and keep markup resilient when products/posts are missing.
- Avoid REST-only front-end fetches for core product/post rendering.

## 6. Page HTML

### DEAD RULE: Dynamic Data via Code Snippets — No Static Data

Generate Elementor HTML block content for Home, Blog, Contact, policies, FAQ, and About.

Before writing page HTML, read the product knowledge ledger created in Phase 1a or the live WooCommerce product inventory. Use it to decide which sections, category groupings, product benefits, compliance notes, FAQs, internal links, and dynamic containers belong on each page. Do not write generic ecommerce sections when product facts are available.

### Full storefront surface layout

Design and verify the complete store surface, not only custom Elementor pages:

- Home and all custom pages.
- Shop/product archive and product category archives, including sort/filter/product-card density and target-market mobile grid.
- Single product pages, including gallery, summary, quantity, tabs/long description, trust areas, related products, and mobile purchase controls.
- Blog index, category/tag/date archives, and single post pages with article typography, product internal links, and CTA styling.
- Cart, checkout, order received, and My Account pages with usable forms, buttons, and mobile spacing.

Each surface must share a coherent brand system while using different section rhythms and layouts. Do not ship cloned grids across different countries/languages.

**Homepage and Blog pages MUST use dynamic data containers, NOT hardcoded static product/article HTML.** This is a DEAD RULE — see `agent-enforcement-rules.md` Section 11.5.

- **Homepage**: Include containers like `data-site-render="home-products"` and `data-site-render="home-posts"`. The page HTML contains only the container div + scoped CSS/JS. A Code Snippets PHP snippet fetches real products via `wc_get_products()` / `WP_Query` and fills the container.
- **Blog page**: Include container `data-site-render="blog-posts"`. A Code Snippets PHP snippet fetches real posts via `WP_Query`.
- **NEVER hardcode** product names, prices, images, article titles, or product IDs in page HTML. Pages must update automatically when products/posts change.
- **If the user wants specific products featured**: Ask the user which products. Use product names or SKUs to identify them. Fetch IDs dynamically.
- **Product images in page HTML**: MAY use real product images from the media library. Ask the user which products/categories to feature. NEVER use placeholder/stock/fake images. All images must be WebP.
- **Target-market mobile layout**: Before generating page CSS, choose a mobile layout seed from `global-design-preferences.md` and `design-variation.md`. Record whether product/category sections use two-column, mixed grid, horizontal scroller, or one-column, and why it fits the target country/language.
- **Policy pages**: Shipping, returns, payment, privacy, terms, cookies, contact, FAQ, and age/compliance pages must contain store-specific facts and buyer steps. Do not create shallow placeholder policies. Use document-style layouts with summaries, lists, tables, and support callouts where helpful.

### Step-by-Step Page Import (One Page at a Time)

Import page HTML ONE PAGE AT A TIME. For each page:
1. Open the page in Elementor.
2. Verify Canvas is set (from Phase 3). If not set, set it now.
3. Add HTML widget.
4. Paste page HTML (use batch import if >30,000 characters).
5. Click Update.
6. Open front-end URL and verify: HTML renders, scoped CSS applies, no duplicate header/footer, dynamic containers present, mobile layout works.
7. Only then move to the next page.

### Page HTML Rules

- **Page HTML contains ONLY page-specific content.** No header, no footer, no menu, no global CSS, no global JS. The global shell (Phase 5) handles all shared elements.
- Keep custom page HTML visual and structural.
- Use scoped CSS class names (e.g., `.home-page .hero`, `.about-page .team-grid`).
- Wrap page-specific JS in IIFE `(function() { ... })()` to avoid global scope conflicts.
- Include dynamic containers for products/posts.
- Avoid huge SEO filler blocks on normal pages.
- Keep mobile layout first-class.
- Test mobile page layouts at 360px, 390px, and 430px. Fix text overflow, clipped buttons, overlapping floating widgets, and one-column defaults that do not match the target market.
- Make each site visually distinct.
- Apply the approved homepage style direction across the rest of the site without cloning every section.
- Run an anti-AI pass: remove generic slogans, repeated card grids, fake claims, decorative filler, and copy that could fit any business.

## 7. Product page UX

Use reversible snippets for:

- Gallery polish.
- Variant option buttons that still update WooCommerce variation selects/events.
- Add-to-cart notices.
- Mobile layout fixes.

Read `woocommerce-customizations-guide.md` for production-ready implementations: trust badges under price, stock urgency counter, estimated delivery date, sale countdown timer, color/size variation swatches, sticky add-to-cart bar on mobile. Use these implementations instead of writing from scratch.

Read `code-snippets-implementation-guide.md` for WordPress core configuration, performance optimization, SEO enhancements, security hardening, custom shortcodes, age/compliance gate, cookie consent banner, and custom REST API endpoints. Use these snippets for all functional implementations.

Never break the native variation form, price updates, stock checks, or add-to-cart event.

Quantity controls:

- If product quantity is editable, add safe +/- controls as a reversible `ux_polish` snippet.
- Preserve WooCommerce's original quantity input, min/max/step, variation events, and add-to-cart behavior.
- Do not auto-submit product or cart forms from +/- clicks unless a tested AJAX implementation is already proven on this exact site.
- Verify simple product, variable product, cart desktop, cart mobile, and checkout after cart update.

## 8. Cart and checkout

Implement project-specific rules using snippets from `woocommerce-customizations-guide.md`:

- Minimum quantity/value (code in guide).
- Quantity plus/minus if needed.
- Address and shipping notices.
- Terms default state if legally acceptable for the store.
- Duplicate notice cleanup.
- Cross-sell products in cart.
- Custom empty cart page with featured products.
- Two-column checkout layout.
- Trust signals in checkout.
- Phone field validation.
- Custom thank you page with order summary and next steps.

Read `wordpress-settings-implementation.md` for shipping zone and payment gateway configuration via REST API or Code Snippets PHP.

Validate failing and passing checkout scenarios.

## 9. Compliance and age gate

### DEAD RULE: Age Gate MUST Be Global Code Snippet — NEVER in Page HTML

For adult or regulated products:

- **The age/compliance gate MUST be implemented as a global Code Snippets PHP snippet using `wp_footer` hook (priority 5).** This is a DEAD RULE.
- **NEVER place age gate HTML, CSS, or JS inside any Elementor HTML widget.** Putting age gate code in page HTML bloats the payload and causes Elementor paste/import failures.
- Use cookie/localStorage after confirmation.
- Keep crawlable content available enough for SEO; do not hide the entire document from crawlers with server-side denial unless legally required.
- Add consistent footer/header/policy disclaimers.
- Read `code-snippets-implementation-guide.md` Section 8 for the complete age gate Code Snippet code.
- After activating the age gate snippet, verify on the front-end: gate appears on first visit, disappears after confirmation, works on all pages.

## 10. SEO metadata and content

Use one-time writers for Rank Math metadata and disable them after execution.

### Content-aware Rank Math writer workflow

Rank Math Free does not provide the same bulk CSV SEO metadata import workflow as Rank Math Pro. For free-version sites, use a Code Snippets `one_time_writer`:

1. Build a content inventory from live WordPress and build artifacts:
   - Pages: title, slug, rendered content, Elementor HTML, purpose, internal links.
   - Products: title, slug, short description, long description, categories, tags, attributes, images, gallery, price context.
   - Posts: title, excerpt, content, category, tags, linked products, featured image.
   - Terms: category/tag/product-category name, slug, description, product/post count.
2. Reuse the site ledger, resume ledger, approved copy, generated article plans, product knowledge ledger, and product CSV rewrite report as a knowledge base. Verify against live content before writing.
3. Generate an SEO mapping for every indexable object: ID, object type, SEO title, meta description, focus keyword, robots/index state, schema type, and source evidence.
4. Run the Rank Math on-page audit: focus keyword in SEO title, meta description, content start, body, subheading, image ALT, natural keyword density, internal links, unique focus keyword, short paragraphs, and rich media.
5. Fix content first when the audit fails because page/product/blog content is missing the keyword, image ALT, subheading, or rich media.
6. Create a Code Snippets PHP one-time writer to write Rank Math metadata in bulk.
7. Run once, capture written/skipped/failed IDs, then verify front-end meta tags, Rank Math admin fields, sitemap inclusion, and noindex rules.
8. Disable and delete the writer snippet after success. If it fails, resume only failed/missing IDs from the writer ledger.

Prioritize:

- Rank Math product SEO fields supplied through safe CSV import or one-time writer mapping.
- Product long descriptions.
- Product category descriptions.
- Blog articles.
- Image ALT/title/caption.
- Internal links.
- Clean meta titles/descriptions.

Do not chase Rank Math scores by bloating every page.

### Existing-site SEO optimization flow

Use this branch when `site.build_mode` is `existing_seo_optimization`. The purpose is to improve SEO without rebuilding the site.

1. Preserve current layouts, theme, slugs, menus, products, prices, stock, checkout, payment gateways, shipping, taxes, and existing page structure unless the user explicitly approves a repair.
2. Verify Rank Math. If this is the first Rank Math use on the site, ask the user to connect the relevant Rank Math account and record `connected`, `user_skipped`, or `blocked`.
3. Verify Code Snippets. If missing, install and activate it only in `autonomous` mode or when explicit plugin-install permission is recorded; otherwise pause and ask for approval or give manual install steps.
4. Build a read-only SEO inventory for pages, products, posts, product categories, post categories, tags, media ALT text, current Rank Math metadata, robots/noindex state, sitemap URLs, schema, canonical tags, internal links, word counts, and thin-content risks.
5. Identify missing, duplicate, generic, or weak SEO title, meta description, focus keyword, image ALT, category description, product long description, article excerpt, internal-link, schema, and noindex/sitemap issues.
6. Generate a content-aware SEO mapping from actual live content. Preserve strong human-written custom SEO metadata unless it is missing, clearly generic, duplicated, or the user authorized overwrite.
7. Run `scripts/rank_math_content_audit.py` against the mapping and fix content gaps first when the focus keyword is absent from visible content, subheadings, ALT text, internal links, or rich media.
8. Generate a temporary Rank Math one-time writer with `scripts/rank_math_meta_writer.py`.
9. Run the writer once through Code Snippets, capture written/skipped/failed IDs, then verify Rank Math admin fields, front-end source meta tags, sitemap inclusion, robots/noindex, and sampled search snippets.
10. Disable and delete the writer snippet after successful verification. If partial failures occur, resume only failed or missing IDs from the writer ledger.
11. Run regression QA proving there were no unintended layout, slug, product price, stock, checkout, payment, shipping, or theme changes.
12. Report audited counts, updated IDs, skipped IDs, failed IDs, snippet cleanup status, remaining blockers, and next content recommendations.

## 11. SEO article generation

Read `scheduled-article-publishing.md` before generating any articles.

1. Ask user for article publishing preferences in ask-user mode. In autonomous mode, choose defaults: 10-20 initial articles, 2 posts/week, 4-8 real product images, 3-5 product links, 800-1,500 words, target-market timezone.
2. Generate 10-20 article topics based on site products, target market, language, and SEO keywords. Present topic list to user for approval.
3. For each approved topic:
   - Write article content following the SEO-optimized structure template.
   - Select 4-8 real product images from media library (WebP format).
   - Add 3-5 prominent product internal links with descriptive anchor text.
   - Add FAQ section with FAQPage schema.
   - Set Rank Math SEO metadata (title, meta description, focus keyword, Article schema).
   - Set article category and tags.
   - Set featured image (real product image, WebP).
   - Create article as `draft` in WordPress.
   - Send draft link to user for review.
4. After user approval, schedule publish dates for continuous publishing (3-6 months coverage).
5. Set WordPress timezone to match target market.
6. Submit published articles to Google Search Console for indexing when access is available, otherwise include a manual indexing package.
7. Report article IDs, titles, statuses, scheduled dates, featured image IDs/URLs, linked product URLs, focus keywords, and any draft/publishing blocker. Never silently skip article generation in a full SEO ecommerce build.

## 12. QA, indexing, and handoff

Run read-only scanners and manual/browser checks. Fix failures through small patches. Prepare indexing files and final report only after verification.

### DEAD RULE: No launch mode before full completion

Do not enable launch/live/indexing mode until all storefront content and QA have passed:

- Product pages, product archives, product category archives, single product layout, cart, checkout, My Account, policy pages, custom pages, blog index/archive, single posts, and initial SEO article batch are complete.
- Article batch exists as drafts, scheduled posts, or published posts according to the recorded interaction mode and user authorization.
- Rank Math metadata, sitemap, robots, schema, internal links, image ALT text, and noindex/index rules are verified.
- Desktop and mobile browser checks pass for links, buttons, menus, product quantity, add-to-cart, cart update, checkout boundary, forms, images, and overflow.
- Launch blockers such as broken checkout, missing articles, incomplete products, missing policy pages, bad sitemap, noindex mistakes, untested snippets, or frozen interactions are resolved.

Only after this gate passes may the agent submit indexing, remove maintenance/noindex launch restrictions, or report that the website is ready to go live.

### Article-specific QA:
- Every article has Rank Math SEO title, meta description, and focus keyword.
- Every article has a unique focus keyword (no cannibalization).
- Every article has 4-8 real product images with ALT text (no 404s).
- Every article has 3-5 product internal links pointing to real, published products (no 404s).
- Every article has FAQPage schema.
- Every article has Article schema with author and date.
- Every article has a featured image in WebP format.
- Every article has an author byline (E-E-A-T).
- Scheduled articles have correct future publish dates in target market timezone.
- No article is published without user review and approval.

## 13. Post-build actions

Read `post-build-actions.md` and present the 4 post-build action recommendations to the user:

1. Scheduled article publishing plan (generate next batch, continuous publishing).
2. Search engine index submission (Google Search Console, Bing Webmaster Tools).
3. Analytics and monitoring setup (GA4, Search Console, Rank Math Analytics).
4. Social media auto-sharing (social profiles, auto-sharing plugins, OpenGraph verification).

Wait for user to choose which actions to proceed with. Do NOT start any action without user confirmation.

## Phase Gate Checklist (MANDATORY before each phase transition)

Before moving from one phase to the next, the agent MUST verify and report:

1. **All steps completed**: Every step in the current phase was executed (not skipped).
2. **All steps verified**: Every step's verification passed (not assumed).
3. **No outstanding errors**: All issues encountered were resolved.
4. **User approvals obtained**: All decisions that required user approval have been confirmed.
5. **Phase deliverables confirmed**: The phase's output is verified and correct.
6. **Report to user**: Present the phase summary — what was done, what was verified, issues resolved, next phase name and first step.
7. **Wait for confirmation**: Do NOT proceed to the next phase until the user confirms (or the user has pre-approved auto-progression).

## Resume Ledger Requirements

Every phase must update a resumable ledger with:

- Current phase and last verified gate.
- Created/updated WordPress IDs: pages, posts, products, media, menus, snippets, templates.
- Snippet names, IDs, lifecycle, active state, and rollback notes.
- Product CSV source row count, imported/updated count, failed rows, gallery/body image verification status.
- Article IDs, statuses, scheduled dates, focus keywords, featured images, and linked product URLs.
- QA checks already passed and checks still pending.
- Temporary credentials/sessions created and whether they were revoked.
- Next safe action if work is interrupted.

When resuming, the ledger is a starting point, not proof. Verify live state before continuing.

### Quick reference: Phase gates

| Gate | Before Phase | Must Verify |
|---|---|---|
| Gate 0→1 | Prerequisites complete | All plugins/themes/SSL/PHP verified; build type determined; SiteGround configured |
| Gate 1→2 | Requirements collected | site_config complete; all unknowns resolved with user |
| Gate 2→3 | Environment inspected | Full environment report; no surprises |
| Gate 3→4 | Baseline set | Permalinks, WC bindings, Rank Math baseline, menus, cache strategy; **DEAD RULE: WooCommerce pages regenerated and bound** |
| Gate 4→5 | Pages created | All pages exist with correct slugs; URL map built; **WooCommerce page IDs re-verified after page creation** |
| Gate 4a | Product knowledge ready | Product CSV or live products inspected; product knowledge ledger exists before homepage preview, page HTML, article planning, and SEO mapping |
| Gate 5→6 | Preview approved | Homepage style preview approved by user; **DEAD RULE: Global shell (header/footer/CSS/JS) active and verified BEFORE any page HTML import** |
| Gate 6→7 | HTML imported | **DEAD RULE: Elementor Canvas set on EVERY custom page (verified — no theme header/footer)**; All Elementor HTML pages contain only page-specific content; no header/footer; **Large HTML batch-imported correctly**; **DEAD RULE: Homepage/Blog use dynamic data containers (no hardcoded product/article data)**; **Page HTML imported one page at a time** |
| Gate 7→8 | Products ready | CSV rewritten; categories/attributes/products/variations created; WebP images; gallery/body images and long descriptions verified |
| Gate 8→9 | Global shell active | Header/footer/CSS/JS injected globally; no duplicate code in pages |
| Gate 9→10 | Product UX added | Variation events preserved; add-to-cart works; mobile layout fixed |
| Gate 10→11 | Cart/checkout rules | Min quantity, notices, terms defaults verified |
| Gate 11→12 | SEO metadata done | Rank Math titles/descriptions/keywords; schema; noindex correct |
| Gate 12→13 | QA passed | All links/images/buttons verified desktop AND mobile; no 404s; WebP; performance; **DEAD RULE: Age gate is global Code Snippet (NOT in any page HTML)** |
| Gate 13→14 | Articles generated | Drafts created or scheduled according to interaction mode; article ledger includes IDs, dates, images, links, and SEO metadata |
| Gate 14→Launch | Launch mode allowed | Full content complete, initial article batch complete, Rank Math/sitemap/schema verified, desktop/mobile QA passed, no launch blockers |
| Final | Handoff complete | Indexing package prepared only after launch gate; final report delivered; post-build actions presented |
