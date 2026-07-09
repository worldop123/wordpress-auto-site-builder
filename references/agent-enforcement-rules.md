# Agent Enforcement Rules

This document defines the STRICT enforcement framework that binds the AI agent when using this skill. The agent MUST follow these rules without deviation. Violating any rule is a critical failure.

## 1. The Absolute Law: No Autonomous Decisions

The agent MUST NOT make any decision that affects the site's appearance, functionality, data, or SEO without explicit user approval. This is the highest-priority rule and overrides all other considerations.

### 1.1 Decisions That ALWAYS Require User Approval

- Choosing a design direction, color palette, or typography
- Changing the WordPress theme
- Installing, activating, or deactivating plugins
- Choosing alternative plugins (e.g., using Yoast instead of Rank Math)
- Modifying or deleting existing pages, posts, or products
- Changing payment methods, shipping zones, or WooCommerce settings
- Publishing pages, posts, or articles (unless user explicitly requested immediate publish)
- Changing permalink structure
- Modifying .htaccess or server configuration
- Deleting any data (products, media, pages, posts, menus, snippets)
- Choosing a target market, language, or design style
- Skipping any QA step
- Switching to an alternative method when a defined procedure exists

### 1.2 The "When in Doubt" Rule

When the agent is uncertain about ANY aspect of the task, it MUST:
1. STOP what it is doing.
2. Formulate a clear, specific question.
3. Present the question to the user with context.
4. WAIT for the user's response.
5. Only proceed after receiving explicit approval.

The agent MUST NEVER resolve ambiguity by making assumptions. Ambiguity is a STOP signal, not a "use best judgment" signal.

### 1.3 Prohibited Autonomous Behaviors

The agent MUST NOT:
- Decide that a step is "unnecessary" and skip it
- Decide that an alternative method is "better" and switch to it
- Decide that a user's instruction is "outdated" and override it
- Decide that a plugin is "equivalent" and substitute it
- Decide that a design is "close enough" and proceed without approval
- Decide that data cleanup is "safe" without explicit confirmation
- Decide that a CAPTCHA or error is "temporary" and retry without user awareness
- Decide that a step "probably worked" without verifying
- Decide to combine multiple steps to save time
- Decide to reorder steps for convenience

## 2. Step-by-Step Execution Framework

### 2.1 The Sequential Execution Rule

Every phase, every step within a phase, and every sub-step within a step MUST be executed in the defined order. This is a HARD RULE.

- **No skipping**: Every step exists for a reason. Even if a step seems unnecessary, execute it and verify.
- **No combining**: Each step must be completed and verified independently.
- **No reordering**: The order is designed for safety and correctness.
- **No parallel execution**: Steps within a phase are sequential. Only independent research tasks may be parallelized.

### 2.2 The Verification Gate

After EVERY step, the agent MUST verify the step was completed successfully before proceeding:

1. **Execute** the step.
2. **Verify** the step completed successfully (check the result, test the output, confirm the state).
3. **Record** the verification result (what was checked, what was found).
4. **Gate**: If verification fails, STOP. Fix the issue. Retry the step. Only proceed after verification passes.

### 2.3 The Failure Protocol

When a step fails:
1. STOP immediately. Do not proceed to the next step.
2. Identify the root cause of the failure.
3. Fix the root cause (not the symptom).
4. Retry the failed step from the beginning.
5. Verify the retry succeeded.
6. Only then proceed to the next step.

The agent MUST NOT:
- Retry the same failed action more than 2 times without notifying the user
- Switch to an alternative method because the defined method failed
- Mark a failed step as "complete" and move on
- Suppress or ignore error messages

### 2.4 The Progress Reporting Rule

After completing each step, the agent MUST report:
- What step was just completed
- What was verified
- What the next step is
- Any issues encountered

This ensures the user can track progress and intervene if the agent is deviating.

## 3. Procedure Adherence Rules

### 3.1 No Method Switching

When a defined procedure exists for a task, the agent MUST follow that procedure. The agent MUST NOT:
- Switch to an alternative method because the defined method is difficult
- Switch to an alternative method because the defined method is slow
- Switch to an alternative method because the agent thinks it knows a "better" way
- Switch to an alternative method because a step failed (fix and retry instead)

### 3.2 Defined Procedures (Must Not Deviate)

The following procedures are defined and MUST be followed exactly:

- **Prerequisite check**: `prerequisite-checklist.md` — verify ALL prerequisites before any work
- **SiteGround handling**: `siteground-bypass-guide.md` — follow handling procedures for CAPTCHA, IP blocks, WAF
- **Old site rebuild**: `old-site-rebuild-procedure.md` — 13-step cleanup, no skipping
- **Global shell architecture**: `global-shell-architecture.md` — header/footer/CSS/JS injection via hooks
- **Page creation**: Create all pages first, then generate HTML with correct paths
- **Elementor HTML**: `elementor-html-automation.md` — page HTML contains only page-specific content
- **Elementor Canvas (DEAD RULE)**: Every custom page MUST have Canvas set BEFORE adding HTML widget — see Section 11.1
- **Batch import (DEAD RULE)**: Large HTML (>30,000 chars) MUST be split into batches — see Section 11.3
- **Age gate placement (DEAD RULE)**: Age gate MUST be global Code Snippet, NEVER in page HTML — see Section 11.2
- **WooCommerce page regeneration (DEAD RULE)**: ALL sites (new AND rebuild) must regenerate and bind WC pages — see Section 11.4
- **Dynamic data (DEAD RULE)**: Homepage/Blog MUST use Code Snippets PHP for dynamic product/post data — see Section 11.5
- **Step-by-step import order (DEAD RULE)**: Global shell first, then page HTML one at a time — see Section 11.7
- **SEO/Speed/WebP (DEAD RULE)**: Global optimization after all pages built — see Section 11.8
- **Site baseline**: `site-baseline-and-menus.md` — configure baseline before page content
- **Article publishing**: `scheduled-article-publishing.md` — draft-review-then-publish workflow
- **QA verification**: `qa-and-launch.md` — every link, image, button tested on desktop AND mobile
- **Post-build actions**: `post-build-actions.md` — present recommendations, wait for user choice

### 3.3 Plugin/Theme Configuration Rules

When configuring WordPress plugins, themes, or settings, the agent MUST:
1. Read `wordpress-plugins-themes-guide.md` for the correct settings, option keys, and default values.
2. Use the official option keys and REST API endpoints documented in the guide.
3. Verify each configuration change after applying it.
4. Never guess option keys or setting names — look them up in the guide.
5. Never apply settings that conflict with Elementor (e.g., Combine CSS/JS on SiteGround).

## 4. Data Integrity Rules

### 4.1 Product Data Is Sacred

WooCommerce product data must never be lost, corrupted, or accidentally modified:
- Product ID, SKU, slug, price, stock, images, categories, attributes, and variations are sacred
- When rewriting product CSV data, only rewrite customer-facing fields (title, description, SEO metadata)
- When cleaning up an old site, products and media library are PRESERVED
- If any product data is lost during any operation, STOP immediately and inform the user

### 4.2 No Data Deletion Without Confirmation

The agent MUST NOT delete any data without explicit user confirmation:
- Pages, posts, products, categories, tags
- Media library files
- Menus, menu items
- Code Snippets
- Custom CSS, theme settings
- WooCommerce orders, coupons, settings
- User accounts

### 4.3 Backup Before Destructive Operations

Before any operation that could modify or delete data:
1. Export/backup the affected data
2. Confirm the backup was successful
3. Only then proceed with the modification/deletion

## 5. Code Quality Enforcement

### 5.1 No Stacked Code

Each page must load ONLY the CSS and JS it needs:
- No CSS from other pages loading on this page
- No JS from other pages loading on this page
- No duplicate CSS/JS rules
- Use scoped class names (`.page-name .class`)
- Use IIFE for page-specific JS: `(function() { ... })()`
- Use conditional loading in Code Snippets (check page type before output)

### 5.2 No Header/Footer in Page HTML

Page HTML widgets must contain ONLY page-specific content:
- No `<header>` tags
- No `<footer>` tags
- No navigation menu HTML
- No global CSS (design tokens, shared component styles)
- No global JS (mobile menu toggle, cart counter, analytics)
- The global shell handles all shared elements via WordPress hooks

### 5.3 WebP Requirement

ALL images on the site must be in WebP format:
- Product images, gallery images, category images
- Blog post featured images and inline images
- Page hero/banner images, logo images
- Use Smush, ShortPixel, Imagify, or EWWW for conversion
- Verify WebP conversion after all images are uploaded

### 5.4 Performance Requirements

- PageSpeed mobile score: 90+
- LCP: under 2.5 seconds
- INP: under 200 milliseconds
- CLS: under 0.1
- No render-blocking CSS/JS except critical CSS
- WooCommerce cart fragments disabled on non-shop pages

## 6. Communication Rules

### 6.1 Transparency

The agent MUST be transparent about:
- What it is about to do (before doing it)
- What it just did (after doing it)
- What it verified (and the results)
- What issues it encountered
- What the next step is
- What it is uncertain about (ask the user)

### 6.2 No Silent Actions

The agent MUST NOT:
- Make changes without announcing them first
- Skip steps without explaining why
- Switch methods without explaining why
- Mark steps as complete without showing verification
- Hide errors or failures
- Make assumptions without stating them and asking for confirmation

### 6.3 User Approval Tracking

For every decision point, the agent MUST track:
- What was the decision point
- What options were presented to the user
- What the user chose
- When the user approved (timestamp or message reference)

This tracking ensures the agent can always justify its actions with user approval.

## 7. Phase Gate Enforcement

### 7.1 Phase Completion Gate

Before moving from one phase to the next, the agent MUST verify:
- All steps in the current phase were executed
- All steps in the current phase were verified
- All decisions in the current phase had user approval
- No errors are outstanding
- The phase's deliverables are confirmed

### 7.2 Phase 0 Gate (Prerequisite)

Before ANY site work begins:
- All prerequisites verified (theme, plugins, SSL, PHP)
- SiteGround detected and configured (if applicable)
- Build type determined (new vs rebuild)
- If rebuild: 13-step cleanup completed and verified

### 7.3 Phase Gate Checklist

Before each phase transition, the agent MUST present:
- Phase name and number
- Steps completed (list)
- Steps verified (list with verification results)
- Issues encountered and resolved
- Next phase name and first step
- User confirmation to proceed

## 8. Anti-Deviation Safeguards

### 8.1 The Three-Strike Rule

If the agent deviates from the defined procedure three times in a single session:
1. First deviation: STOP, self-correct, document the deviation
2. Second deviation: STOP, notify the user, ask for guidance
3. Third deviation: STOP all work, notify the user that the agent is unable to proceed without re-reading all reference files

### 8.2 The Context Refresh Rule

If the agent is uncertain about a procedure, it MUST re-read the relevant reference file before proceeding. The agent MUST NOT rely on memory for procedural details — always verify against the written reference.

### 8.3 The User Override Rule

Only the user can override a defined procedure. The agent MUST NOT override a procedure on its own. If the user requests a deviation, the agent MUST:
1. Acknowledge the deviation request
2. Explain the risks of deviating
3. Confirm the user wants to proceed despite the risks
4. Document the user-approved deviation
5. Proceed with the deviation only after explicit confirmation

### 8.4 The No-Shortcut Rule

The agent MUST NOT take shortcuts, including:
- Skipping verification to save time
- Combining steps to save time
- Using hardcoded values instead of dynamic queries
- Using fake/placeholder data instead of real data
- Skipping mobile testing
- Skipping link verification
- Marking QA as "pass" without actually testing
- Using "best guess" for settings instead of looking up the correct values

## 9. SiteGround-Specific Enforcement

### 9.1 Challenge Response Protocol

When encountering a SiteGround challenge (CAPTCHA, IP block, WAF block):
1. STOP all automation immediately
2. Do NOT retry or refresh
3. Do NOT switch to an alternative method
4. Notify the user with specific details about the challenge
5. Provide resolution options from `siteground-bypass-guide.md`
6. Wait for user to resolve or instruct
7. Only resume after the challenge is resolved

### 9.2 SG Optimizer Configuration Enforcement

When SiteGround is detected:
- MUST configure SG Optimizer for Elementor compatibility
- MUST NOT enable Combine CSS or Combine JS (breaks Elementor)
- MUST purge cache after every content change
- MUST add 2-5 second delays between automated actions
- MUST use REST API with application passwords as preferred access method

## 10. Old Site Rebuild Enforcement

### 10.1 Cleanup Procedure Enforcement

When rebuilding an old site:
- MUST follow all 13 steps in `old-site-rebuild-procedure.md` exactly
- MUST NOT skip any step
- MUST verify each step before proceeding to the next
- MUST preserve products and media library (no exceptions)
- MUST back up before cleanup
- MUST confirm with user before starting cleanup
- MUST verify product data integrity after cleanup

### 10.2 Data Preservation Verification

After cleanup, the agent MUST verify:
- All WooCommerce products still exist (count matches)
- All product categories, tags, and attributes still exist
- All media library images still exist (count matches)
- Product prices, SKUs, stock, and images are intact
- No product data was corrupted or lost

## 11. Page Building Dead Rules (No Exceptions)

These rules are DEAD RULES. The agent MUST NOT skip, forget, or work around any of them. Violating any rule produces broken websites.

### 11.1 Elementor Canvas Is Mandatory

Every custom page built with Elementor MUST have its Page Layout set to `elementor_canvas` BEFORE pasting any HTML.

- **Enforcement**: Set Canvas → Update → Reload front-end → Verify no theme header/footer → ONLY THEN add HTML widget.
- **If Canvas is not set**: Hello Elementor's default header, footer, and menu appear, duplicating the global shell. The page is broken.
- **Record**: `"canvas_set": true` in page ledger only after verification passes.
- **Pages that MUST use Canvas**: Home, Blog, Contact, About, FAQ, Policy pages, Landing pages.
- **Pages that MUST NOT use Canvas**: Shop, Cart, Checkout, My Account, product archives, single product pages.
- Read `elementor-html-automation.md` for the complete enforcement procedure.

### 11.2 Age Gate MUST Be Global Code Snippet

The age verification gate MUST be a global Code Snippets PHP snippet using `wp_footer` hook (priority 5).

- **NEVER place age gate HTML/CSS/JS in any Elementor HTML widget.** Age gate code bloats page HTML and causes Elementor paste/import failures.
- **Implementation**: Code Snippets → PHP snippet → `add_action('wp_footer', function() { ... }, 5)` → Scope: Front-end → Lifecycle: persistent.
- Read `code-snippets-implementation-guide.md` Section 8 for the complete code.

### 11.3 Batch Import for Large HTML

When HTML payload exceeds ~30,000 characters or paste fails/truncates, the agent MUST use batch import.

- **Split at natural HTML boundaries** — never split inside an open tag.
- **Use ONE HTML widget** — append all batches to the same widget.
- **Verify after EVERY batch** — Update → check front-end → confirm no broken tags.
- **CSS in first batch, JS in final batch** — never split a `<style>` or `<script>` tag.
- Read `elementor-html-automation.md` "DEAD RULE: Batch Import for Large HTML" for the complete procedure.

### 11.4 WooCommerce Page Regeneration for ALL Sites

For BOTH new builds AND old site rebuilds, the agent MUST regenerate and bind WooCommerce pages.

- **Regenerate**: WooCommerce → Status → Tools → "Install pages".
- **Bind**: Use Code Snippets PHP with `update_option()` for `woocommerce_shop_page_id`, `woocommerce_cart_page_id`, `woocommerce_checkout_page_id`, `woocommerce_myaccount_page_id`, `woocommerce_terms_page_id`.
- **Verify**: Check WooCommerce → Settings → Advanced — all page selectors show correct pages.
- Read `code-snippets-implementation-guide.md` Section 2.2 for the exact binding code.

### 11.5 Dynamic Data via Code Snippets — No Static Data in Pages

Homepage and Blog pages MUST use dynamic data fetched via Code Snippets PHP, NOT hardcoded static product/article HTML.

- **Homepage products**: Use a Code Snippets PHP snippet with `WC_get_products()` or `WP_Query` to fetch real products. Output as JSON or HTML into a container (`data-site-render="home-products"`). The page HTML widget contains only the container and scoped CSS/JS — the PHP snippet fills it with real product data.
- **Blog posts**: Use a Code Snippets PHP snippet with `WP_Query` to fetch real posts. Output into a container (`data-site-render="home-posts"` or `data-site-render="blog-posts"`).
- **NEVER hardcode product names, prices, images, or article titles in page HTML.** If a product is added/removed/changed, the page must update automatically.
- **NEVER hardcode product IDs unless the user explicitly requested a curated featured set.** If the user wants specific products featured, ask which products and use their IDs. Otherwise, use dynamic queries (latest products, featured products, best sellers, on-sale products).
- **When the user wants specific products**: Ask the user which products to feature. Use product names or SKUs to identify them. Fetch their IDs dynamically via `wc_get_product_id_by_sku()` or `get_page_by_path()`.
- Read `code-snippets-implementation-guide.md` Sections 6-7 for dynamic renderer code.

### 11.6 Product Images in Page HTML

When creating page HTML, the agent MAY use real product images from the WooCommerce media library to create visually appealing layouts.

- **Ask the user** which products or product categories to feature if the design calls for specific product imagery.
- **Fetch image URLs dynamically** via PHP (`wp_get_attachment_image_url()`) or use product gallery image URLs from the media library.
- **NEVER use placeholder images, stock photos, or fake images.** All images must be real product images from the site's media library.
- **All images must be WebP format.** If images are not yet WebP, convert them before use.
- **Image ALT text** must be descriptive and SEO-friendly.

### 11.7 Step-by-Step Import Order (MANDATORY)

When building pages, the agent MUST follow this import order. No exceptions. No reordering.

1. **FIRST: Global shell** — Create the global header (Code Snippets PHP, `wp_body_open` hook) and global footer (Code Snippets PHP, `wp_footer` hook) BEFORE any page HTML. The global shell must be active and verified on the front-end before any page HTML is imported.
2. **SECOND: Global CSS** — Add global CSS (design tokens, header styles, footer styles, shared components, responsive breakpoints) to Appearance → Customize → Additional CSS. Verify it loads on all pages.
3. **THIRD: Global JS** — Add global JS (mobile menu toggle, cart counter, smooth scroll) via Code Snippets HTML/JS snippet on `wp_footer` hook. Verify it works on all pages.
4. **FOURTH: Page HTML — one page at a time** — Import page HTML into Elementor HTML widgets, one page at a time. For each page: Set Canvas → verify → add HTML widget → paste HTML → Update → verify front-end → move to next page.
5. **FIFTH: Dynamic renderers** — Activate Code Snippets PHP snippets for dynamic product/post rendering. Verify containers are filled with real data.
6. **NEVER import all page HTML at once before the global shell is active.** The global shell must be in place first so the agent can verify that page HTML does NOT contain duplicate header/footer.

### 11.8 SEO, Speed, and WebP Optimization (MANDATORY)

After all pages are built and content is imported, the agent MUST perform global optimization. This is not optional.

- **SEO optimization**: Configure Rank Math SEO metadata for all pages, products, categories, and posts. Set meta titles, meta descriptions, focus keywords, and schema. Noindex Cart, Checkout, My Account. Index all content pages.
- **Speed optimization**: Disable WooCommerce cart fragments on non-shop pages. Defer JS. Remove query strings from static resources. Enable Gzip and browser caching. Configure SG Optimizer (if SiteGround) for Elementor compatibility. Verify PageSpeed mobile score 90+, LCP < 2.5s, INP < 200ms, CLS < 0.1.
- **WebP conversion**: Convert ALL images on the site to WebP format — product images, gallery images, category images, blog post images, page hero/banner images, logo. Use Smush, ShortPixel, Imagify, or EWWW. Verify all images load correctly in WebP after conversion.
- **Verify after optimization**: Run PageSpeed Insights, check all images are WebP, verify no broken images, verify SEO metadata is correct.

## 12. Duplicate Rule and Consistency Audit

The agent MUST periodically audit all skill reference files for:
- Duplicate rules that say the same thing in different files (consolidate or cross-reference)
- Contradictory rules that conflict (resolve and update)
- Missing cross-references (a rule in one file should reference the detailed procedure in another)
- Outdated procedures that no longer match current WordPress/Elementor/WooCommerce versions

If duplicates or contradictions are found, the agent MUST:
1. Identify all instances across all reference files.
2. Keep the most detailed, most correct version.
3. Replace other instances with a cross-reference to the authoritative version.
4. Document the consolidation in the build log.
