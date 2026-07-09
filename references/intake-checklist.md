# Intake Checklist

Collect only what is needed. Infer anything that can be safely observed from WordPress after login.

## Required

- Service mode selection. Always identify one of these first:
  - New site build.
  - Old-site rebuild.
  - Existing-site SEO optimization only.
  - Reference-site inspired build / clone-style adaptation.
- WordPress admin URL.
- Authentication method: username/password, temporary admin account, application password, or user-guided browser login.
- Brand name and domain.
- Site type: ecommerce, lead-gen, catalog, blog, landing, hybrid.
- Target market and language. Ask which country/region the site targets. Read `global-design-preferences.md` to understand regional design conventions, color preferences, trust signals, payment methods, and cultural habits for the target market.
- Build mode and permission boundary:
  - New build, old-site rebuild, existing-site SEO optimization, reference-site clone/adaptation, repair-only, SEO/content-only, WooCommerce UX-only, or skill/workflow update.
  - Interaction mode: `ask_user` or `autonomous`.
  - `ask_user`: collect approvals for target market, homepage style, destructive cleanup, plugin/settings changes, and publishing.
  - `autonomous`: only when explicitly authorized by the user. Record that the user waived approval gates, then let AI choose market, language, design, page layouts, article topics, menus, SEO structure, and non-destructive implementation details from the available facts.
  - What may be deleted, preserved, disabled, or rewritten.
  - Whether homepage style approval is required or explicitly waived.
  - Whether article publishing is draft-review, batch pre-approved scheduling, or no article work.
- Industry and compliance restrictions.
- Contact details: email, phone, WhatsApp, address, social links, support hours.
- Logo and brand assets, or permission to generate placeholders.
- Product or service list with names, prices, images, categories, variants/options, inventory status, shipping limits, and purchase rules.
- Product import/media details when CSV is involved:
  - Source CSV type, row count, encoding, delimiter, and whether it updates existing products.
  - Source price currency, target WooCommerce currency, exchange-rate source, conversion permission, rounding strategy, and whether original prices must be backed up.
  - Featured image column, gallery image column, inline/body image handling, and whether images are remote URLs or media-library URLs.
  - Variation parent/SKU strategy, attribute columns, stock/pricing fields, category/tag fields, and Rank Math columns.
  - Whether every gallery image and product body image must be verified after import.
- Currency, tax, shipping origin, shipping countries, shipping timing, return policy, payment methods, and minimum order rules.
- Payment method details: ask whether the site uses card, PayPal, bank transfer, cash on delivery/COD, crypto, offline contact payment, or a custom gateway. For COD, ask which countries/regions support it and whether the checkout needs a COD notice. Consider regional payment preferences from `global-design-preferences.md` (e.g., iDEAL for Netherlands, PIX for Brazil, Alipay for China, COD for SEA/Middle East/Africa).
- Design style preferences: ask the user about preferred visual tone, color preferences, and any styles to avoid. Cross-reference with `global-design-preferences.md` for the target market's conventions.
- Mobile commerce preferences:
  - Preferred mobile density: compact catalog, editorial, promotion-first, category-first, or trust-first.
  - Whether product cards should be 2-column, mixed grid, horizontal scroller, or one-column. Do not assume one-column.
  - Product-card priorities: image size, title lines, price prominence, quick add/detail button, category label, shipping badge.
  - Header behavior: sticky, compact, bottom actions, search, WhatsApp, cart count, or no floating widgets.
- SEO seed keywords, priority products/categories, competitors or style references, and prohibited claims.

## Reference-Site Clone/Adaptation Intake

Use this when the customer gives a website URL to imitate, clone, reference, or rebuild from.

- Reference URL.
- Permission basis: owned site, authorized client site, or public inspiration only.
- Target site type: ecommerce, official/company site, catalog, blog/media, service/lead-gen, SaaS, portfolio, local business, documentation, booking, community, or hybrid.
- Target build type: WordPress/WooCommerce, WordPress non-ecommerce, existing WordPress rebuild, or mixed.
- Capture scope: homepage only, selected pages, or full public site surface.
- Maximum capture depth/page count.
- Must-capture surfaces: home, navigation, footer, shop/catalog, category/listing, product/detail, blog/news, article, policies, about, contact, service, pricing, case study, FAQ, cart, checkout, account, or other.
- Whether the agent may capture and save public HTML snapshots locally for analysis. Captures must remain in a gitignored folder.
- Elements that may be inspired by: layout rhythm, menu structure, section ordering, grid density, CTA placement, filter/search patterns, footer structure.
- Elements that must not be copied: text, images, logos, reviews, product data, code, brand names, trademarks, policy copy, trackers, API keys, private endpoints.
- User brand/content/products/media that will replace reference content.
- Required transformation level: close layout inspiration, same information architecture but different visual system, or loose competitive reference.

If the user authorizes autonomous execution, infer a conservative capture scope and stop if the reference site blocks public access.

## Existing-Site SEO Optimization Intake

Use this when the customer wants SEO optimization without rebuilding the site:

- Confirm scope: pages only, products only, blogs only, categories only, or full-site SEO.
- Confirm whether page layouts must be preserved.
- Confirm whether plugin installation is allowed. Code Snippets is required for one-time writers when Rank Math Free cannot bulk import SEO metadata.
- Collect priority keywords, target market/language, priority URLs, competitor URLs, and prohibited claims.
- Ask whether existing human-written SEO metadata should be preserved unless clearly missing/weak.
- Confirm whether image ALT text, category descriptions, product long descriptions, internal links, schema, sitemap/noindex rules, and article SEO can be updated.
- In autonomous mode, infer conservative defaults: preserve layout/slugs/products/prices, optimize all indexable pages/products/posts/categories, skip overwrite of strong existing custom metadata unless clearly generic or missing.

## Policy Page Intake

For every ecommerce build, collect or infer these details before writing policy pages:

- Shipping origin, shipping countries/regions, processing time, delivery estimate, tracking availability, and delay handling.
- Payment methods, COD regions, payment timing, failed delivery handling, and whether online payment is disabled.
- Return/exchange window, unopened/opened product rules, hygiene or regulated-product limits, damaged/wrong-item evidence requirements, refund method, and support contact path.
- Privacy/cookie requirements for the target market, including GDPR/EU expectations when targeting Europe.
- Age/compliance rules for regulated products, visible warning text, and checkout/entry gate behavior.
- Business identity details available to customers: brand operator, support email, WhatsApp/phone, address if available, and support hours.

If the user omits details and authorizes autonomous completion, write conservative policies that clearly state the known facts and avoid unsupported legal claims.

## Article Publishing Preferences (Ask During Build Phase)

Article creation is part of a full SEO ecommerce build unless the user opts out. In autonomous mode, choose conservative defaults and report the generated/scheduled batch clearly.

- How many articles in the initial batch? (default: 10-20)
- How many articles per week for scheduled publishing? (default: 2-3)
- Which days of the week to publish? (default: Tuesday, Thursday)
- What time of day to publish? (default: 9:00 AM target market timezone)
- How many product images per article? (default: 4-8)
- How many product internal links per article? (default: 3-5)
- Article word count range? (default: 800-1,500 words)
- Any specific article topics the user wants covered?
- Any topics to avoid?
- Brand voice/tone for articles? (formal, casual, technical, lifestyle)
- Author name and bio for article bylines? (E-E-A-T requirement)
- Should articles be reviewed individually before publishing? (default: yes, each article as draft for review)

## Full Store Surface Intake

Collect or infer whether each surface needs a custom layout pass:

- Home, Shop/product archive, product category archive, single product, Blog index/archive, single post, Cart, Checkout, My Account, Contact, FAQ, About, Shipping, Returns, Payment, Privacy, Terms, Cookie, and Age/Compliance.
- Target-country mobile product layout: two-column, mixed density, category-first, horizontal scroller, or one-column only when justified.
- Interaction requirements for buttons, accordions, tabs, filters, mobile menu, quantity controls, add-to-cart, update cart, checkout, contact forms, and policy links.
- Any existing archive/product/single-post template that must be preserved.

## Optional

- Preferred visual tone: premium, editorial, technical, playful, minimalist, wholesale, luxury, local service, B2B, etc.
- Color dislikes and required brand colors.
- Existing pages that must not be overwritten.
- Existing snippets that must remain enabled.
- Search Console/Bing access or preference for manual indexing package.
- Blog batch size, article topics, internal-link priority, and image count per article.

## Default assumptions when omitted

- Use Hello Elementor as theme baseline.
- Use Elementor HTML blocks for custom page bodies.
- Use WooCommerce for Shop, products, Cart, Checkout, and My Account.
- Use Rank Math for SEO metadata when installed.
- Use Code Snippets for PHP/CSS/JS behavior, classified by lifecycle.
- Keep Cart, Checkout, and My Account `noindex`.
- Keep products, product categories, posts, policies, FAQ, About, and Contact indexable unless the user says otherwise.

## Structured config shape

```json
{
  "site": {
    "domain": "",
    "brand": "",
    "language": "en",
    "market": "",
    "site_type": "ecommerce",
    "industry": "",
    "adult_or_regulated": false,
    "build_mode": "new|old_rebuild|existing_seo_optimization|reference_site_clone|repair|seo_content|woocommerce_ux|skill_update|mixed",
    "interaction_mode": "ask_user|autonomous"
  },
  "access": {
    "wp_admin_url": "",
    "auth_method": "browser_login|application_password|manual_paste"
  },
  "brand_assets": {
    "logo_url": "",
    "generate_logo": true,
    "generate_site_icon": true,
    "site_icon_url": "",
    "site_icon_requirements": "separate simplified square icon, clear at 32x32/64x64, not dark or muddy",
    "style_references": [],
    "avoid_styles": []
  },
  "reference_site": {
    "url": "",
    "permission_basis": "owned|authorized|public_inspiration",
    "capture_scope": "full_public_site|selected_pages|homepage_only",
    "max_pages": 40,
    "target_site_type": "ecommerce|official|catalog|blog|service|saas|portfolio|local_business|documentation|booking|community|hybrid",
    "required_surfaces": [],
    "transformation_level": "close_layout_inspiration|same_information_architecture|loose_reference",
    "do_not_copy": ["text", "images", "logos", "reviews", "product_data", "code", "trackers", "trademarks"]
  },
  "contact": {
    "email": "",
    "phone": "",
    "whatsapp": "",
    "address": "",
    "social": {}
  },
  "commerce": {
    "currency": "",
    "shipping_origin": "",
    "shipping_countries": [],
    "shipping_time": "",
    "payment_methods": [],
    "cod_regions": [],
    "minimum_order_quantity": null
  },
  "mobile_ux": {
    "density": "target_market_default|compact|spacious|mixed",
    "product_grid": "target_market_default|two_column|mixed|horizontal|one_column",
    "floating_widgets": []
  },
  "policies": {
    "shipping_origin": "",
    "delivery_estimate": "",
    "return_window": "",
    "regulated_product_notes": "",
    "support_process": ""
  },
  "products": [],
  "product_import": {
    "csv_source": "",
    "expected_row_count": null,
    "source_currency": "",
    "target_currency": "",
    "exchange_rate": null,
    "exchange_rate_source": "",
    "price_rounding": "standard|charm_ending|market_default",
    "charm_ending": "",
    "backup_original_prices": true,
    "image_columns": [],
    "gallery_required": true,
    "body_images_required": true,
    "rank_math_columns": []
  },
  "categories": [],
  "seo": {
    "seed_keywords": [],
    "priority_urls": [],
    "competitors": [],
    "prohibited_claims": [],
    "preserve_existing_custom_meta": true,
    "optimize_scope": "full_site|pages|products|posts|categories"
  },
  "preserve": {
    "pages": [],
    "snippets": [],
    "notes": []
  }
}
```
