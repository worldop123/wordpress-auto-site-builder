# Site Baseline and Menus

Run this before importing lots of Elementor HTML. The aim is to make the site stable once, then build on top of it without repeated teardown.

## Baseline order

1. Confirm theme and plugins:
   - Hello Elementor active or compatible theme accepted by the user.
   - Elementor active.
   - WooCommerce active for ecommerce.
   - Rank Math active for SEO.
   - Code Snippets active or another agreed snippet mechanism.
   - Cache plugin identified.

2. Set WordPress basics:
   - Site title and tagline.
   - Logo and site icon/favicon. When a new logo is generated, also generate a separate simplified square site icon and configure both in Site Identity.
   - Timezone/language if supplied.
   - Permalink structure, usually `/%postname%/`.
   - Reading settings: homepage and posts page binding when needed.

3. Set WooCommerce basics:
   - Currency.
   - Store address/origin when supplied.
   - Shipping zones/rates if enough business data exists.
   - Payment methods if credentials/settings are available; otherwise mark as launch blocker.
   - **DEAD RULE: Regenerate WooCommerce pages** (WooCommerce → Status → Tools → "Install pages") for BOTH new and old sites. This creates/updates Shop, Cart, Checkout, My Account, and Terms pages with correct shortcodes.
   - **Bind Shop, Cart, Checkout, My Account, and Terms pages** using Code Snippets PHP with `update_option()`:
     - `woocommerce_shop_page_id` → Shop page ID
     - `woocommerce_cart_page_id` → Cart page ID
     - `woocommerce_checkout_page_id` → Checkout page ID
     - `woocommerce_myaccount_page_id` → My Account page ID
     - `woocommerce_terms_page_id` → Terms page ID
   - **Verify bindings**: Check WooCommerce → Settings → Advanced — all page selectors show correct pages.
   - Read `code-snippets-implementation-guide.md` Section 2.2 for the exact binding code.

4. Set Rank Math baseline (read `rank-math-seo-guide.md` for full configuration):
   - Enable Advanced Mode in Rank Math Dashboard.
   - Confirm sitemap enabled with correct post type and taxonomy inclusion.
   - Confirm product/post/page/category sitemap choices.
   - Configure General Settings: links (nofollow external, open in new tab), images (auto ALT), breadcrumbs (enable + shortcode).
   - Configure Titles & Meta templates for all post types using variables like `%seo_title% %sitename%`.
   - Set site name/organization/person info in Local SEO & Knowledge Graph.
   - Configure Schema templates: Product for WooCommerce, Article for blog posts, FAQPage for FAQ pages.
   - Set up Webmaster Tools verification (Google Search Console, Bing, etc.).
   - Configure social meta: OpenGraph and Twitter Card settings.
   - Enable WooCommerce module for ecommerce sites.
   - Enable Image SEO module for auto ALT text generation.
   - Use noindex for Cart, Checkout, My Account, internal search, date archives, and test pages.
   - Keep products, categories, posts, and useful pages indexable.
   - Do not overwrite detailed page/product metadata repeatedly after initial one-time writer.

5. Plan snippets (read `global-shell-architecture.md` for full architecture):
   - **Persistent global header** via Code Snippets PHP (`wp_body_open` hook).
   - **Persistent global footer** via Code Snippets PHP (`wp_footer` hook).
   - **Persistent global JS** via Code Snippets HTML/JS (`wp_footer` hook).
   - **Global CSS** via Appearance → Customize → Additional CSS.
   - Persistent checkout rules if needed.
   - Persistent age/compliance gate if needed.
   - UX polish snippets.
   - One-time Rank Math writer.
   - One-time media ALT writer.
   - Read-only QA scanner.

## Menus

## Logo and site icon baseline

Before binding the global header/footer shell, create or verify brand assets:

- Full logo for header/footer. It may be horizontal or compact depending on the market and header design.
- Header/footer logo variants for real backgrounds: transparent, light-background, and dark-background/inverted variants as needed.
- Separate square site icon/favicon. Do not reuse the full logo if it becomes dark, muddy, cropped, or unreadable at small sizes.
- Minimum site icon source size: 512x512 PNG/WebP, with enough inner padding and strong contrast.
- Do not place a logo with a white rectangular background on a dark header or footer unless that boxed look is intentionally approved. Prefer transparent or background-matched artwork.
- Verify downscaled clarity at 192x192, 64x64, and 32x32 on light and dark backgrounds.
- Configure WordPress Site Identity: `custom_logo` for logo and `site_icon` for favicon/site icon.
- Verify front-end header logo and footer logo against the actual header/footer colors. They must not look pasted on, mismatched, cropped, muddy, or low contrast.
- Verify browser tab favicon and source/icon markup.
- Record media IDs, dimensions, file types, background choices, selected header/footer variants, and verification notes in the ledger.

Create and bind menus automatically after page slugs are known.

### Primary/header menu

Recommended ecommerce structure:

- Home
- Shop
- Categories or a small curated category submenu
- Blog or Guides
- About
- FAQ
- Contact
- Cart or account/cart icon if the theme/shell supports it

Bind to the active theme's primary menu location. If the theme does not expose a useful location because a custom shell is used, still create the WordPress menu as source data and have the shell render it.

### Footer menu

Recommended footer/support structure:

- Shipping Policy
- Return Policy
- Payment Policy
- Privacy Policy
- Terms of Service
- Cookie Policy
- Age/Compliance page when needed
- FAQ
- Contact

Bind to footer menu location when available. If unavailable, render it in the global footer shell from `wp_nav_menu`.

### Mobile menu

If the theme has a separate mobile location, bind the primary menu there too. If the global shell owns mobile navigation, use the same source menu and render a mobile drawer/toggle.

## Menu automation options

Prefer WordPress APIs or WP-CLI when available:

- Create menus.
- Add page/category/custom URL items.
- Assign menu locations.

Use wp-admin UI when APIs are unavailable:

- Appearance -> Menus, or Site Editor/Navigation for block themes.
- Verify menu items by opening front-end header/footer.

## Global shell coordination

The site MUST use the global shell architecture defined in `global-shell-architecture.md`. Header, footer, global CSS, and global JS are injected globally via WordPress hooks — NOT embedded in individual page HTML widgets.

### Global header (Code Snippets PHP snippet)

- Implemented as a persistent Code Snippet using `wp_body_open` hook with priority 5.
- Renders header HTML with logo, primary navigation menu (via `wp_nav_menu`), and cart icon on ALL pages.
- The header snippet calls `wp_nav_menu()` with `theme_location => 'menu-1'` to render the WordPress primary menu.
- Do NOT hardcode menu links in the header snippet — use `wp_nav_menu()` so menu changes in WordPress admin automatically reflect.
- Mobile menu toggle is handled by global JS, not page-specific JS.

### Global footer (Code Snippets PHP snippet)

- Implemented as a persistent Code Snippet using `wp_footer` hook with priority 10.
- Renders footer HTML with footer menu (via `wp_nav_menu`), contact info, payment badges, and copyright.
- The footer snippet calls `wp_nav_menu()` with `theme_location => 'footer'` to render the WordPress footer menu.

### Global CSS (Appearance → Customize → Additional CSS)

- Contains CSS variables (design tokens): colors, spacing, typography, breakpoints.
- Contains header styles, footer styles, shared component styles (buttons, forms, cards).
- Contains responsive breakpoints for mobile/tablet.
- Page-specific CSS is NOT included here — it goes in the page's Elementor HTML widget with scoped class names.

### Global JS (Code Snippets HTML/JS snippet)

- Implemented as a persistent Code Snippet using `wp_footer` hook.
- Contains mobile menu toggle, cart counter, smooth scroll, analytics, cookie consent, and other site-wide interactions.
- Page-specific JS is NOT included here — it goes in the page's Elementor HTML widget wrapped in IIFE.

### Menu rendering in the global shell

- Render the header menu from the WordPress primary menu via `wp_nav_menu()`.
- Render the footer menu from the WordPress footer/support menu via `wp_nav_menu()`.
- Do not hardcode every menu link in PHP unless the site has no menu support and the links are generated from `site_config`.
- Keep menu markup accessible: buttons for mobile toggles, semantic nav, visible focus states.
- Menu items created in WordPress admin automatically appear in the global header/footer — no need to edit snippets when adding/removing menu items.

## Done criteria

- Primary/header menu exists and is assigned or rendered by shell.
- Footer/support menu exists and is assigned or rendered by shell.
- Shop, Cart, Checkout, My Account bindings are correct.
- Homepage and Blog/Posts settings are correct.
- Rank Math sitemap and noindex baseline are correct.
- Cache clearing method is known.
