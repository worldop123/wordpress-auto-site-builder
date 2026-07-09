# QA and Launch Checklist

Do not claim completion until relevant checks are run or explicitly blocked. Every item in this checklist must be verified on BOTH desktop and mobile unless explicitly noted.

## Launch Mode Dead Rule

The site cannot enter launch/live/indexing mode until the entire website is complete and the full QA ledger passes.

- Product pages, product archives, product category archives, cart, checkout, My Account, policy pages, homepage, custom pages, blog index/archive, single posts, and the initial SEO article batch are complete.
- All articles required for the initial build exist as drafts, scheduled posts, or published posts according to the user-approved/autonomous mode plan.
- Rank Math metadata, schema, sitemap, robots.txt, canonical/noindex rules, image ALT text, and internal links are verified.
- Desktop and mobile tests pass for all links, buttons, menus, quantity controls, add-to-cart, cart update, checkout boundary, contact forms, age/cookie gates, images, and layout overflow.
- Any missing products, missing articles, broken checkout, frozen interaction, incomplete archive layout, broken image, missing policy, noindex error, sitemap error, or untested snippet is a launch blocker.

Only after all items pass can the agent say the website is ready to launch, submit indexing, or remove launch restrictions.

## Interruption and Resume QA

If work was interrupted or resumed, verify the recovery before launch:

- [ ] Latest resume ledger was read.
- [ ] Last verified gate was identified.
- [ ] Live WordPress state was checked read-only before new writes.
- [ ] Page IDs, WooCommerce bindings, snippet states, product/media counts, article statuses, menus, and Rank Math sitemap state match the ledger or differences are explained.
- [ ] Temporary credentials, app passwords, tokens, or browser sessions created before interruption were revoked/rotated or marked as a blocker.
- [ ] No destructive phase was repeated without evidence.
- [ ] Product imports, media imports, article scheduling/publishing, and snippet updates were not duplicated.
- [ ] The final report states where work resumed and what consistency checks passed.

## Prerequisite verification (Phase 0)

- All prerequisites from `prerequisite-checklist.md` have been verified.
- Hello Elementor theme is active.
- Rank Math SEO is installed, activated, and configured in Advanced Mode.
- If Rank Math is first used on this site, the user was asked to connect the relevant Rank Math account; result recorded as connected, skipped by user choice, or blocked.
- Elementor is installed and activated with performance settings enabled.
- WooCommerce is installed and activated for ecommerce sites.
- Code Snippets is installed and activated.
- SSL/HTTPS is enabled site-wide.
- PHP version is 8.0 or higher (8.1+ recommended).

## Link, Button, and Navigation verification (Desktop AND Mobile)

This section is MANDATORY. Every interactive element must be tested on both desktop and mobile viewports.

### All links
- Every internal link in the HTML points to a real, existing page (no 404s).
- Every menu item navigates to the correct page when clicked.
- Every footer link navigates to the correct policy/support page.
- Every category link in navigation points to a valid WooCommerce category archive.
- Every product link points to a valid, published product page.
- Every blog post link points to a valid, published post.
- Every "Read more" or "Learn more" link points to real content.
- Every CTA button navigates to the correct destination (Shop, Contact, etc.).
- Every social media link points to the correct profile URL.
- Every email link uses `mailto:` and opens email client.
- Every phone link uses `tel:` and opens dialer on mobile.
- Every external link opens correctly (new tab if configured).
- No link returns a 404 error.
- No link returns a 500 error.
- No link redirects to an unexpected URL.

### Desktop-specific link checks
- Header menu items are clickable and navigate correctly.
- Dropdown/submenu items are clickable and navigate correctly.
- Footer links are clickable and navigate correctly.
- Breadcrumb links are clickable and navigate correctly.
- In-content contextual links are clickable and navigate correctly.
- Sidebar links (if any) are clickable and navigate correctly.

### Mobile-specific link checks
- Hamburger menu opens and closes correctly.
- All menu items in mobile menu are tappable (minimum 44x44px touch target).
- Mobile menu items navigate to the correct pages.
- Mobile footer links are tappable and navigate correctly.
- Mobile breadcrumb links are tappable and navigate correctly.
- Mobile in-content links are tappable and navigate correctly.
- No links are too close together (minimum 8px spacing between tappable elements).
- Sticky elements (header, add-to-cart) do not block link taps.
- Floating widgets such as WhatsApp, cart bubbles, chat, cookie banners, and age gates do not overlap primary mobile actions, checkout fields, quantity steppers, or update-cart buttons.

### Button checks (Desktop AND Mobile)
- Add to cart button works on every product page.
- Add to cart button shows success/added-to-cart feedback.
- Quantity +/- controls work on product pages when quantity is editable. Plus increments by step, minus respects minimum, and neither button freezes the page.
- Quantity +/- controls work on cart pages when quantity is editable. They must preserve the native WooCommerce quantity input and must not auto-submit in a way that causes repeated reloads or browser hangs.
- Cart update behavior is clear: either the native "Update cart" button is enabled after a quantity change, or a verified AJAX update completes without console errors.
- Checkout button navigates to checkout page.
- Place order button works (or reaches payment gateway boundary).
- Contact form submit button works and sends data.
- Search button opens search results.
- Newsletter/subscribe button works if present.
- All filter/sort buttons on shop page work.
- All accordion/toggle buttons expand and collapse correctly.
- All tab buttons switch tabs correctly.
- Back to top button works if present.
- Every button has a visible hover state (desktop) and active state (mobile).
- Every newly generated page script has been tested by real click/input actions, not only by visual inspection.
- No button click causes a frozen page, long main-thread lock, repeated reload loop, disabled pointer-events issue, hidden overlay interception, or console error.
- Generated accordions, tabs, filters, sliders, mobile menus, cookie/age gates, search, product cards, cart buttons, checkout controls, and contact CTAs are all verified interactively.
- Quantity stepper code must not use a body-wide `MutationObserver` that mutates the same quantity DOM on every childList change. It must not auto-click cart update unless the exact AJAX flow is proven on that site.

## Image verification (Desktop AND Mobile)

### All images
- Every image URL loads successfully (no 404s, no broken images).
- Every image has descriptive ALT text.
- Every image has appropriate width and height attributes (prevents CLS).
- Every product image displays correctly in gallery.
- Every product image zoom/lightbox works (desktop).
- Every product image swipe works (mobile).
- Every blog post featured image loads.
- Every hero/banner image loads.
- Every logo image loads (header and footer if different).
- Header/footer logo variant matches the actual background color; no accidental white rectangle on dark header/footer and no "pasted screenshot" look.
- Logo remains readable on desktop and mobile header/footer states, including sticky header, drawer menu, and footer compact layout.
- Every favicon loads.
- Site icon/favicon remains clear at 32x32 and 64x64; it is not dark, muddy, cropped, or visually merged into browser UI.
- WordPress `custom_logo` and `site_icon` are configured with separate suitable assets when the generated full logo is too detailed for favicon use.
- Every social sharing image (OpenGraph) is configured.
- Every image is optimized (not oversized 鈥?check file size vs display size).
- Every image uses WebP format (see WebP conversion section below).

### Mobile-specific image checks
- Images are responsive and do not overflow viewport.
- Images maintain aspect ratio on mobile.
- Product gallery images are swipeable.
- No horizontal scroll caused by images.
- Lazy-loaded images appear when scrolled into view.

## WebP image conversion (MANDATORY)

ALL images on the site must be converted to WebP format. This is a hard requirement.

### Conversion checklist
- [ ] All product images converted to WebP.
- [ ] All product gallery images converted to WebP.
- [ ] All category/thumbnail images converted to WebP.
- [ ] All blog post featured images converted to WebP.
- [ ] All blog post inline images converted to WebP.
- [ ] All page hero/banner images converted to WebP.
- [ ] All logo and brand images converted to WebP.
- [ ] All icon images (if using image files) converted to WebP.
- [ ] All favicon variants generated (PNG fallback for older browsers).
- [ ] All OpenGraph/social sharing images have WebP or JPEG fallback.

### Conversion methods
1. **Plugin-based (recommended)**: Use Smush, ShortPixel, or Imagify to auto-convert all existing and new uploads to WebP.
2. **Server-based**: Configure nginx/apache to serve WebP with JPEG/PNG fallback via `picture` element or content negotiation.
3. **Batch conversion**: Use a script to convert all images in `wp-content/uploads/` to WebP.

### Verification
- [ ] Check page source: images use `.webp` extension or `image/webp` MIME type.
- [ ] Verify fallback: JPEG/PNG fallback exists for browsers without WebP support.
- [ ] Test in Chrome, Firefox, and Safari: images display correctly.
- [ ] Run PageSpeed Insights: confirm images are in WebP format.
- [ ] No image returns 404 after conversion.

## Code quality and performance (MANDATORY)

### Clean, lightweight, non-stacked code
- [ ] No stacked/duplicate CSS files loading on the same page.
- [ ] No stacked/duplicate JavaScript files loading on the same page.
- [ ] No unused CSS rules from other pages loading on this page.
- [ ] No unused JavaScript from other pages loading on this page.
- [ ] Each page loads ONLY the CSS and JS it needs.
- [ ] CSS is minified for production.
- [ ] JavaScript is minified for production.
- [ ] HTML is clean and well-structured (no unnecessary nesting).
- [ ] No inline styles where CSS classes should be used.
- [ ] No duplicate HTML widgets in Elementor (one per page).
- [ ] No leftover debug code, console.log, or commented-out code blocks.
- [ ] No hardcoded data that should be dynamic.
- [ ] Scoped CSS class names used (e.g., `.brand-home .hero`, not global `.hero`).

### Per-page CSS/JS loading
- [ ] Elementor Optimized CSS Loading is enabled (loads only used widget CSS).
- [ ] Elementor Optimized JS Loading is enabled if available.
- [ ] Code Snippets are scoped to specific pages where possible (using conditional tags).
- [ ] WooCommerce cart fragments script is disabled on non-shop pages.
- [ ] WooCommerce scripts are not loaded on non-ecommerce pages.
- [ ] Third-party scripts (analytics, chat) are deferred or loaded with delay.
- [ ] No render-blocking CSS/JS in the `<head>` except critical CSS.
- [ ] Critical CSS is inlined for above-the-fold content.

### Performance metrics
- [ ] PageSpeed Insights mobile score: 90 or higher.
- [ ] PageSpeed Insights desktop score: 95 or higher.
- [ ] LCP (Largest Contentful Paint): under 2.5 seconds.
- [ ] INP (Interaction to Next Paint): under 200 milliseconds.
- [ ] CLS (Cumulative Layout Shift): under 0.1.
- [ ] Total page weight: under 2MB for standard pages, under 3MB for product-heavy pages.
- [ ] Server response time (TTFB): under 800ms.
- [ ] No excessive DOM elements (under 1500 nodes per page).

## Storefront checks

- Homepage style preview was approved or the user explicitly waived the preview gate.
- Final homepage still matches the approved direction.
- Homepage preview and final homepage include a complete header, footer, mobile behavior, product/category area, payment/shipping/order facts, and buyer guidance.
- Homepage and major custom pages pass the content-richness gate from `design-variation.md`: no thin hero-only pages, no generic three-card filler, and each section supports buying, trust, navigation, SEO, education, or support.
- Homepage includes at least 2 useful dynamic or data-driven modules from real products/categories/posts when data exists, such as product-image slideshow, featured-product strip, category image grid, comparison block, guide hub, FAQ preview, or support/COD ordering module.
- Rich modules use real internal links to products, categories, posts, policies, or support pages; no decorative buttons point to `#`, empty URLs, missing pages, or irrelevant destinations.
- Any slideshow, carousel, tab, accordion, filter, or expandable module was tested on desktop and mobile; controls are visible, touch/click works, focus is not trapped, and product/category links are not blocked.
- Page copy and visual treatment pass anti-AI review: no generic filler slogans, fake claims, repeated template sections, or unsupported social proof.
- Home returns HTTP 200 and renders header/footer.
- Custom Elementor pages use Elementor Canvas where required. **DEAD RULE: Verify EVERY custom page has Canvas set 鈥?no theme header/footer visible on any custom page.**
- Custom Elementor pages contain the intended HTML widget content and no duplicate generated widgets.

### DEAD RULE Verification (MANDATORY 鈥?All Must Pass)

Before marking the build as complete, verify ALL dead rules were followed:

- [ ] **Dead Rule 1 鈥?Elementor Canvas**: Every custom page (Home, Blog, Contact, About, FAQ, Policy pages) has Canvas set. Verified by loading each page 鈥?no Hello Elementor default header/footer/menu visible.
- [ ] **Dead Rule 2 鈥?Age Gate**: Age gate is a global Code Snippets PHP snippet using `wp_footer` hook. NOT in any Elementor HTML widget. Verified: age gate appears on first visit, disappears after confirmation, works on all pages.
- [ ] **Dead Rule 3 鈥?Batch Import**: If any page used batch import, verify: no broken HTML tags, no orphaned closing tags, no missing sections, complete page renders correctly.
- [ ] **Dead Rule 4 鈥?WooCommerce Pages**: WooCommerce pages regenerated (Status 鈫?Tools 鈫?Install pages) and bound (Settings 鈫?Advanced shows correct pages). Verified for BOTH new and old sites.
- [ ] **Dead Rule 5 鈥?Dynamic Data**: Homepage and Blog use dynamic data containers filled by Code Snippets PHP. No hardcoded product names, prices, images, or article titles in page HTML. Containers show real data.
- [ ] **Dead Rule 6 鈥?Product Images**: All images in page HTML are real product images from the media library. No placeholder/stock/fake images. All images are WebP.
- [ ] **Dead Rule 7 鈥?Import Order**: Global shell (header/footer/CSS/JS) was created and verified BEFORE any page HTML was imported. Page HTML was imported one page at a time.
- [ ] **Dead Rule 8 鈥?SEO/Speed/WebP**: Rank Math metadata set for all content. PageSpeed mobile 90+. ALL images converted to WebP. Cart fragments disabled on non-shop pages.
- [ ] **Dead Rule 9 鈥?No Launch Before Completion**: Product/store pages, archives, blog surfaces, initial article batch, Rank Math SEO, sitemap/schema, and full desktop/mobile QA are complete before launch/indexing mode.
- [ ] **Product Knowledge Gate**: If a product CSV or live products were available, a product knowledge ledger was created before homepage preview, page HTML, article planning, and Rank Math metadata generation.
- Header/primary menu renders expected links.
- Footer/support menu renders expected policy/support links.
- Mobile menu opens, closes, and links to the same intended destinations.
- Mobile homepage product/category layout matches the target market profile from `global-design-preferences.md` and `design-variation.md`; it must not default to the same one-column/card style for every country.
- Mobile product grids are tested at 360px, 390px, and 430px widths. Record whether the product grid is two-column, mixed, horizontal, or one-column and why.
- Shop returns HTTP 200 and shows products or a correct empty-state message.
- Product category archives return HTTP 200.
- Shop/product archives are redesigned or styled for the target market with verified product-card density, sort/filter usability, pagination/load-more behavior, and mobile grid choice.
- Product pages render gallery, price, variants, stock, and add-to-cart.
- Single product pages have a verified layout pass: gallery, summary, long description/tabs, trust information, related products, quantity input, and mobile purchase area.
- Blog index, blog archives, and single posts have a verified layout pass: article cards, category/tag/date archives, typography, product internal links, schema, and mobile readability.
- Blog surfaces include article discovery and topic grouping when SEO content exists; they are not left as plain default lists unless the user explicitly chose a minimal blog.
- Cart quantity changes work.
- Cart quantity changes do not freeze, repeatedly reload, or leave the cart total/update state ambiguous.
- Checkout blocks invalid minimum quantity/value.
- Checkout allows valid order path up to payment/place-order boundary.
- Contact, FAQ, About, and policy pages return HTTP 200.
- Policy pages are not placeholders: each policy page contains store-specific facts, clear sections, buyer steps, and contact/support instructions relevant to the target country/language.
- Policy pages have readable mobile layouts, no text overflow, working internal links, and accurate SEO metadata.
- Mobile header, menu, product page, cart, and checkout are usable.
- All page links verified on desktop (see Link verification section).
- All page links verified on mobile (see Link verification section).
- All buttons verified on desktop and mobile (see Button checks section).
- All images verified on desktop and mobile (see Image verification section).

## WooCommerce checks

- Shop page bound.
- Cart, Checkout, My Account bound.
- Home page and posts/blog page reading settings are correct.
- Header, footer, and mobile menu locations are assigned or rendered from the global shell.
- If products were prepared from CSV, row count, IDs, SKUs, slugs, parent/variation relationships, prices, stock, categories, and image URLs were preserved unless intentionally changed.
- If products were prepared from CSV, homepage sections, page copy, category copy, article topics, image ALT themes, and Rank Math metadata can be traced back to the product knowledge ledger instead of generic ecommerce assumptions.
- If product prices were converted from another currency, the import ledger records source currency, target currency, rate, rate source/timestamp, rounding rule, converted columns, original backup columns, and sample converted products.
- Converted product prices display in the target WooCommerce currency on product pages, archives, cart, checkout, order review, and Product schema `priceCurrency`.
- If products were imported from rewritten CSV, sample products show rewritten title, short description, long description, and correct Rank Math product SEO data.
- If products were imported from CSV, featured images, every gallery image, inline/body images in product descriptions, ALT/title/caption metadata, and product detail HTML were checked against the import ledger.
- Products with galleries must show the expected thumbnail count and open/switch gallery images on desktop and mobile.
- Products with long descriptions/body images must render those details on the single product page without broken images, clipped content, or missing HTML sections.
- Currency correct.
- Shipping zones and rates configured or marked as launch blocker.
- Payment methods configured or marked as launch blocker.
- Emails/SMTP configured or marked as launch blocker.
- Permalinks saved after structural changes.
- All product images are in WebP format.
- All product category images are in WebP format.

## SEO checks

- Rank Math active and in Advanced Mode.
- Rank Math sitemap enabled and accessible at `/sitemap_index.xml`.
- Product, category, post, and page meta titles/descriptions/focus keywords exist.
- Rank Math metadata was generated from a content inventory, not generic templates alone.
- Pages, products, posts, and taxonomies have object-specific SEO titles, descriptions, and focus keywords based on their actual content.
- Rank Math on-page checks were reviewed for each indexable page/product/post/category: focus keyword in SEO title, meta description, content start, content body, subheading, image ALT, and natural keyword density.
- Content readability checks passed: short paragraphs and useful rich media such as real images/video where available.
- Focus keywords are unique or documented as an intentional topic cluster.
- Internal links in SEO pages/posts/products point to real URLs.
- If a Code Snippets one-time writer was used for Rank Math metadata, its written/skipped/failed ID ledger was captured.
- Rank Math one-time writer snippets are disabled and deleted after successful verification.
- Products rewritten from CSV have unique product-specific SEO titles, meta descriptions, and focus keywords.
- Cart, Checkout, and My Account are noindex.
- Products, categories, posts, and key pages are indexable.
- Product long descriptions exist.
- Category descriptions exist.
- Blog post count meets the requested batch.
- Full SEO ecommerce builds include an initial article batch unless the user opted out. The final report must list article IDs, titles, statuses, scheduled dates, focus keywords, featured images, and internal product links.
- Images have ALT/title where practical.
- sitemap_index.xml works.
- product-sitemap.xml and post/page/category sitemaps work when enabled.
- robots.txt includes sitemap and blocks cart/checkout/my-account.
- No important URL returns 404.
- Structured data (Product, Article, FAQ, Breadcrumb) is valid (test with Rich Results Test).
- Breadcrumbs are displayed and have BreadcrumbList schema.
- OpenGraph and Twitter Card meta tags are set for all pages.
- Canonical tags are correct on all pages.
- hreflang tags are set if multilingual site.
- Page experience: HTTPS, mobile-friendly, no intrusive interstitials.
- Core Web Vitals: LCP < 2.5s, INP < 200ms, CLS < 0.1 (see core-web-vitals-guide.md).
- Content passes E-E-A-T self-assessment (see google-seo-guidelines.md).
- No spam policy violations (see google-seo-guidelines.md spam policies section).
- No keyword stuffing in any content.
- No hidden text or links.
- No thin or scraped content.
- No AI-generated bulk content without human value-add.

## Existing-site SEO optimization QA

Use this section when `site.build_mode` is `existing_seo_optimization`. Passing this QA proves the SEO task did not become an accidental rebuild.

- [ ] No page layout, Elementor content, theme, menu structure, global header/footer, or archive template was rebuilt unless a separate repair approval exists.
- [ ] No product ID, SKU, slug, price, stock, variation, checkout, payment, shipping, tax, or order setting changed unless explicitly authorized and recorded.
- [ ] Read-only inventory counts are recorded for pages, products, posts, product categories, post categories/tags, media, and indexable URLs.
- [ ] Rank Math title, description, focus keyword, robots, schema, sitemap, canonical, and OpenGraph changes are mapped to specific object IDs.
- [ ] Image ALT updates are mapped to media IDs and use real page/product/article context.
- [ ] Existing strong human-written SEO metadata was preserved unless missing, duplicated, generic, or approved for overwrite.
- [ ] Code Snippets one-time writers record written/skipped/failed IDs and are disabled/deleted after verification.
- [ ] Sample front-end source checks confirm updated meta tags without visual regressions.
- [ ] Sitemap and robots/noindex checks pass after SEO writes.
- [ ] Final report lists audited counts, changed IDs, skipped IDs, failed IDs, snippets removed, remaining blockers, and next content recommendations.

## Article checks (if articles were generated)

- Every article was created as a draft and reviewed by the user before publishing.
- Every article has a unique Rank Math SEO title (50-60 characters).
- Every article has a unique meta description (120-160 characters).
- Every article has a unique focus keyword (no keyword cannibalization).
- Every article has Article schema with author, datePublished, and publisher.
- Every article has FAQPage schema for FAQ sections.
- Every article has BreadcrumbList schema.
- Every article has OpenGraph and Twitter Card meta tags.
- Every article has a featured image in WebP format with descriptive ALT text.
- Every article has 4-8 real product images (user-configurable count) with ALT text.
- All article images are in WebP format.
- No article image returns 404.
- Every article has 3-5 prominent product internal links (user-configurable count).
- All article internal links point to real, published product pages (no 404s).
- All article internal links use descriptive anchor text (not "click here").
- Every article has an author byline with bio (E-E-A-T).
- Every article has a FAQ section with 3-5 Q&A pairs.
- Every article word count is within the user-specified range.
- Article topics are diverse (no two articles cover the same angle).
- Article topics are related to the site's actual products.
- Article content is original (not scraped or duplicated).
- Scheduled articles have correct future publish dates in target market timezone.
- WordPress timezone is set to match the target market.
- No article is published without explicit user approval.
- Published articles are submitted to Google Search Console for indexing.
- Published articles are submitted to Bing Webmaster Tools.
- Article categories and tags are properly assigned.
- Articles have internal links to other related articles (no orphan articles).

## Snippet checks

- Persistent snippets enabled.
- One-time writers disabled after successful run.
- Read-only scanners disabled after run.
- Deprecated snippets inactive.
- Rollback notes documented.
- All snippets are scoped to load only on relevant pages (conditional loading).
- No snippet loads unnecessary CSS/JS on pages that don't need it.

## Global shell checks (MANDATORY)

The global shell architecture must be verified. Read `global-shell-architecture.md` for the complete architecture.

### Global header
- [ ] Global header Code Snippet is active and persistent.
- [ ] Header uses `wp_body_open` hook (not hardcoded in page HTML).
- [ ] Header renders on ALL pages (home, shop, product, cart, checkout, blog, contact, policies).
- [ ] Header displays logo correctly (desktop and mobile).
- [ ] Header displays primary navigation menu (via `wp_nav_menu`, not hardcoded links).
- [ ] Header navigation links point to correct pages (no 404s).
- [ ] Header cart icon shows correct cart count.
- [ ] Header is NOT duplicated in any Elementor HTML page widget.
- [ ] Header mobile layout is correct (hamburger menu, responsive).
- [ ] Header does not overlap page content.

### Global footer
- [ ] Global footer Code Snippet is active and persistent.
- [ ] Footer uses `wp_footer` hook (not hardcoded in page HTML).
- [ ] Footer renders on ALL pages.
- [ ] Footer displays footer menu (via `wp_nav_menu`, not hardcoded links).
- [ ] Footer menu links point to correct policy/support pages (no 404s).
- [ ] Footer displays contact info correctly.
- [ ] Footer displays payment badges/icons if applicable.
- [ ] Footer displays copyright with current year.
- [ ] Footer is NOT duplicated in any Elementor HTML page widget.
- [ ] Footer mobile layout is correct (stacked, responsive).

### Global CSS
- [ ] Global CSS is in Appearance 鈫?Customize 鈫?Additional CSS (not in page HTML widgets).
- [ ] CSS variables (design tokens) are defined and used consistently.
- [ ] Header styles are in global CSS (not in page HTML).
- [ ] Footer styles are in global CSS (not in page HTML).
- [ ] Shared component styles (buttons, forms, cards) are in global CSS.
- [ ] Responsive breakpoints are defined in global CSS.
- [ ] No duplicate CSS rules between global CSS and page-scoped CSS.
- [ ] Global CSS is minified or will be minified by cache plugin.

### Global JS
- [ ] Global JS Code Snippet is active and persistent.
- [ ] Global JS uses `wp_footer` hook.
- [ ] Mobile menu toggle works on all pages.
- [ ] Cart counter updates when products are added.
- [ ] Smooth scroll works for anchor links.
- [ ] Cookie consent/banner works if applicable.
- [ ] Analytics tracking fires correctly.
- [ ] No JavaScript errors in browser console on any page.
- [ ] Global JS is NOT duplicated in any Elementor HTML page widget.

### Page HTML isolation
- [ ] No page HTML widget contains `<header>` tags.
- [ ] No page HTML widget contains `<footer>` tags.
- [ ] No page HTML widget contains navigation menu HTML.
- [ ] No page HTML widget contains global CSS (design tokens, header/footer styles, shared components).
- [ ] No page HTML widget contains global JS (mobile menu toggle, cart counter, analytics).
- [ ] Each page HTML widget uses scoped CSS class names (e.g., `.home-page .hero`).
- [ ] Each page HTML widget wraps JS in IIFE `(function() { ... })()`.

## SiteGround hosting checks (if applicable)

If the site is hosted on SiteGround, verify the following. Read `siteground-bypass-guide.md` for the complete guide.

### SG Optimizer configuration
- [ ] SG Optimizer plugin is active.
- [ ] Dynamic Cache is enabled.
- [ ] Memcached is enabled.
- [ ] HTTPS Enforce is enabled.
- [ ] Gzip Compression is enabled.
- [ ] Browser Caching is enabled.
- [ ] CSS Minify is enabled.
- [ ] JS Minify is enabled.
- [ ] Defer Render-blocking JS is enabled.
- [ ] Combine CSS Files is DISABLED (breaks Elementor).
- [ ] Combine JavaScript Files is DISABLED (breaks Elementor).
- [ ] PHP version is 8.1 or higher.
- [ ] PHP Memory Limit is 512MB or higher.
- [ ] Max Execution Time is 300 seconds or higher.

### WAF and security
- [ ] WAF is set to Standard mode (not High, which can block legitimate API calls).
- [ ] No IP addresses are blocked that need access.
- [ ] No CAPTCHA challenges appeared during the build process (or were resolved manually).
- [ ] Application passwords work for REST API access (not blocked by WAF).

### Cache behavior
- [ ] SG Optimizer cache is purged after all content changes.
- [ ] Front-end pages show updated content after cache purge.
- [ ] Cache purge does not break Elementor editor.
- [ ] No stale cached versions visible to visitors.

### Performance on SiteGround
- [ ] Server response time (TTFB) is under 800ms.
- [ ] Dynamic Cache hit rate is acceptable.
- [ ] No PHP errors in error log related to SG Optimizer.
- [ ] Site loads correctly with SG Optimizer fully enabled.

## Indexing package

Prepare:

- Sitemap URL.
- Priority URL list.
- URLs not to submit: Cart, Checkout, My Account, internal search, test pages.
- Google Search Console manual submission steps unless authenticated automation is available.
- Bing Webmaster manual submission steps unless authenticated automation is available.
- robots.txt verified.
- Sitemap submitted to Google Search Console.
- Sitemap submitted to Bing Webmaster Tools.
- Rich Results report checked in Search Console.

## Final report

Include:

- What was changed.
- What was verified (with specific URLs checked).
- What remains blocked or needs user/business setup.
- Interruption/resume status: whether the task was resumed, last verified checkpoint, recovery checks run, mismatches found, and credentials revoked.
- Persistent snippets to keep.
- One-time/scanner snippets disabled.
- Files generated.
- WebP conversion status (all images converted).
- Performance metrics (PageSpeed scores, Core Web Vitals).
- SEO metadata status (titles, descriptions, schema).
- Link verification results (all links tested, no 404s).
- Mobile verification results (all pages tested on mobile).
- Image verification results (all images load, all have ALT text).
- Code quality report (no stacked code, per-page loading verified).
- Global shell verification results:
  - Global header snippet active and rendering on all pages.
  - Global footer snippet active and rendering on all pages.
  - Global CSS in Additional CSS with design tokens.
  - Global JS snippet active with all interactions working.
  - No header/footer/global CSS/JS duplicated in page HTML widgets.
- SiteGround verification results (if applicable):
  - SG Optimizer configuration (Dynamic Cache, Memcached, HTTPS, Gzip, etc.).
  - WAF mode (Standard).
  - Combine CSS/JS disabled (Elementor compatibility).
  - Cache purge behavior verified.
  - No CAPTCHA/IP block issues during build.
- Article generation report (if articles were generated):
  - Number of articles generated, reviewed, and published.
  - Number of articles scheduled with publish dates.
  - Article topic list with primary keywords.
  - Publishing schedule (frequency, days, time, timezone).
  - Article QA results (SEO metadata, images, links, schema verified).
  - Draft review status (all articles reviewed by user before publishing).
  - Next batch recommendation date (when to generate more articles).
- Post-build actions status:
  - Search engine index submission status (Google, Bing).
  - Analytics setup status (GA4, Search Console, Rank Math Analytics).
  - Social media auto-sharing setup status.
  - Scheduled publishing plan status.
