# Reference Site Capture and Clone-Style Adaptation

Use this when the user gives a reference website URL and asks to clone, imitate, copy, replicate, rebuild, or use it as a design/layout reference.

The goal is to understand page structure and interaction patterns, then build a transformed WordPress site with the user's own brand, content, products, language, compliance, and SEO. This is not permission to publish copied third-party HTML, copy, images, logos, product data, reviews, or trademarks.

## Permission and Boundary

Before capture, record:

- Reference URL.
- Whether the user owns the site, has permission, or is using it as public design inspiration.
- Target site type: ecommerce, official/company site, catalog, blog/media, service/lead-gen, SaaS, portfolio, local business, documentation, booking, community, or hybrid.
- Whether the target build is WordPress/WooCommerce, non-ecommerce WordPress, or mixed.
- Allowed depth and page limit.
- Whether checkout/cart/account pages may be inspected only when publicly accessible.

Do not bypass login walls, paywalls, checkout payment steps, CAPTCHAs, WAF blocks, geoblocking, anti-bot controls, or robots restrictions. Do not capture private user/account/order data.

## Capture Scope

Capture the HTML snapshots for relevant public pages and save them to a gitignored folder such as `.reference-captures/<domain>/<timestamp>/`.

Required page-type coverage when available:

- Home page.
- Header/navigation/menu/search surfaces.
- Footer and support link surfaces.
- Shop/catalog/listing page.
- Product/category/filter/search pages for ecommerce.
- Product/detail pages for ecommerce.
- Cart, checkout, account, wishlist, comparison, or tracking pages only if public and safe to inspect.
- Blog/news index.
- Blog/category/tag archives.
- Single post/article pages.
- About/company/brand story pages.
- Contact/support/location pages.
- Policy/legal pages: shipping, returns, refund, payment, privacy, terms, cookies, age/compliance.
- Non-ecommerce surfaces: services, pricing, case studies, portfolio, booking, documentation, FAQ, resources, careers, team, testimonials, landing pages, partner pages.

The agent should not stop at the homepage. The value of this workflow comes from mapping the whole site surface.

## What to Extract

For each captured page, record:

- URL, HTTP status, content type, final URL after redirects.
- Page type classification.
- Title, meta description, H1/H2 outline.
- Main sections in order.
- Header/menu/footer structure.
- CTA labels and positions.
- Grid/list/card density.
- Filters/sort/search/pagination patterns.
- Forms and required fields.
- Product/detail information structure when relevant.
- Trust blocks, payment badges, shipping notes, compliance notices.
- Responsive hints from CSS class names and layout structure.
- Internal links and likely sitemap coverage.
- Scripts/features that need WordPress/Code Snippets equivalents.

Save the raw HTML snapshot for internal analysis only. Also create a manifest JSON summarizing the above.

## WordPress Mapping

Map reference surfaces into WordPress deliverables:

- Static/custom pages -> Elementor HTML widgets with transformed layout and original user content.
- Header/footer -> global shell with Code Snippets and WordPress menus.
- Ecommerce listings -> WooCommerce shop/product category archives, not static copied grids.
- Product details -> WooCommerce single product templates and reversible UX snippets.
- Cart/checkout/account -> WooCommerce-owned pages, not static cloned checkout HTML.
- Blog/news -> WordPress posts, categories, tags, archives, and single post templates.
- Forms -> WordPress form plugin, REST endpoint, or safe Code Snippets implementation.
- Dynamic lists -> WordPress queries, WooCommerce queries, or shortcodes.
- Policies -> original policy copy based on user facts and target-market compliance.

If the reference site is not WordPress, translate the layout patterns into WordPress-native architecture. Do not try to recreate its framework or script stack wholesale.

## Transformation Rules

Allowed:

- Section rhythm and information architecture inspiration.
- Similar page-type coverage.
- Comparable grid density or navigation depth.
- Rebuilt components using the user's brand system.
- New copy, images, icons, products, policies, and SEO metadata.

Not allowed:

- Publishing copied HTML/CSS/JS as-is.
- Reusing reference text, product descriptions, reviews, logos, photography, icons, trademarks, policy text, or schema data.
- Copying competitor checkout flows in a way that breaks WooCommerce security or compliance.
- Keeping third-party tracking, pixels, forms, API keys, or private endpoints.
- Claiming affiliation with the reference brand.

The final site should feel inspired by the reference, but be legally, visually, and operationally distinct.

## Analysis Report

Before building, produce a report:

- Reference URL and capture timestamp.
- Captured URL count and skipped URL count.
- Page-type coverage matrix.
- Key layout patterns worth adapting.
- WordPress/WooCommerce mapping plan.
- Global header/footer/menu observations.
- SEO/content opportunities.
- Assets/text/brand elements that must not be copied.
- Risks: blocked pages, missing checkout access, heavy scripts, anti-bot, mobile overflow, inaccessible UI, compliance gaps.

## QA After Adaptation

Verify:

- All copied-looking text/assets were replaced.
- Header/footer/menu use WordPress data and user brand assets.
- WooCommerce pages remain functional and secure.
- Buttons, filters, tabs, menus, quantity controls, forms, cart, and checkout are clickable and do not freeze.
- Mobile layouts at 360px, 390px, and 430px do not overflow.
- SEO metadata is original and based on the user's content.
- No third-party tokens, trackers, private endpoints, or competitor URLs remain in generated code.

## Suggested Tool

Use:

```bash
python scripts/reference_site_capture.py https://example.com --max-pages 40
```

The output folder is gitignored. Keep the manifest and HTML snapshots local unless the user owns the reference site and explicitly asks to preserve them in a private project.
