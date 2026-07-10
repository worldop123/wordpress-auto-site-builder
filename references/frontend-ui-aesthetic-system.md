# Frontend UI Aesthetic System

Use this reference before homepage previews, global shell work, and production Elementor HTML. The goal is to make AI-built WordPress pages look like intentional ecommerce interfaces instead of generic generated blocks.

## Open-Source Pattern Library Mindset

Use open-source UI ecosystems as quality references for discipline, not as copied code or copied assets:

- shadcn/ui and Radix UI: accessible component states, clear focus rings, predictable menus, dialogs, tabs, accordions, and drawers.
- Tailwind UI and Headless UI: spacing discipline, responsive composition, disclosure patterns, and clean interaction states.
- Lucide-style icons: simple line icons for actions, trust badges, contact methods, cart/search/account affordances, and payment/support blocks.
- Shopify-grade ecommerce patterns: strong collection navigation, product-card hierarchy, checkout-safe mobile layout, visible shipping/payment/support facts.
- Linear/Stripe-level polish: restrained surfaces, precise typography, fewer decorative effects, strong alignment, and purposeful motion.

Do not paste proprietary templates, copyrighted HTML/CSS, brand assets, screenshots, icons, or images. Rebuild the pattern with the customer's brand, target market, product facts, media, language, and WooCommerce data.

## Design Tokens First

Before writing header/footer CSS or page HTML, define and record a small design system in the build ledger:

- Brand palette: primary, secondary, accent, surface, muted surface, border, text, muted text, success/error/warning. Avoid one-note palettes and default blue/purple gradients unless the brand truly requires them.
- Typography: heading family/fallback, body family/fallback, base size, line height, heading scale, paragraph width, button label style. Do not scale font size with viewport width.
- Spacing: container max width, mobile/desktop gutters, section padding, grid gaps, card padding, toolbar height.
- Shape: button radius, card radius, input radius, image radius. Cards and buttons should usually use 4-8px radius unless the existing brand system justifies more.
- Elevation: border-first by default; use subtle shadows only where they clarify hierarchy.
- Components: buttons, icon buttons, product cards, collection chips, forms, accordions, tabs, notices, trust strips, badges, mobile drawer, footer columns.

Global tokens, header/footer CSS, shared buttons, forms, product cards, icon buttons, and responsive breakpoints belong in Appearance -> Customize -> Additional CSS. Page HTML may add only page-specific scoped layout styles.

## Header Quality Gate

The global header must look designed before page HTML begins:

- Logo has stable height, clear spacing, correct background variant, and does not appear as a pasted rectangle.
- Primary navigation uses real WordPress menu items via `wp_nav_menu()`, has hover/focus/active states, and does not wrap awkwardly on common desktop widths.
- Ecommerce affordances are visible and conventional: cart, search when useful, account if enabled, and category/shop access.
- Mobile header uses a tested drawer or disclosure menu with 44px touch targets, visible close control, focus-safe behavior, and no overlap with cart/checkout controls.
- Header height, sticky behavior, border/shadow, and content offset are verified on home, shop, product, cart, checkout, blog, and policy pages.
- Do not use a giant logo, centered nav, crowded pill buttons, or decorative header effects unless the target market and brand call for them.

## Footer Quality Gate

The footer is a store navigation and trust surface, not a leftover block:

- Include brand/contact, shop/category links, policy links, payment/shipping facts, support path, compliance/age note when needed, and copyright.
- Use responsive columns on desktop and grouped sections/accordion-like stacks on mobile if the footer is long.
- Make footer links tappable, readable, and aligned. Do not bury policy/contact links in tiny text.
- Match logo and icon variants to the footer background.
- Keep decorative imagery minimal. Prefer useful trust/payment/support icons and text.

## Page HTML Aesthetic Rules

Every custom Elementor HTML page must inherit the global design system and then vary page-specific layout:

- Start with a concrete information hierarchy: what the visitor should see, compare, trust, and click.
- Use real product/category/post data through dynamic containers when data exists.
- Build section rhythm: hero, merchandising, category navigation, trust/payment/shipping, guide/FAQ/support, and internal links should not all be identical cards.
- Use stable dimensions for grids, cards, image ratios, buttons, counters, and tab controls so content does not shift on hover or when dynamic data loads.
- Use real images that help inspect products or understand the store. Convert/localize images to WebP before final use.
- Prefer useful icons, swatches, badges, comparison rows, and tables over vague feature cards.
- Keep copy specific to the product, target market, shipping/payment facts, and compliance limits.
- Avoid generic hero-only pages, empty glass cards, floating gradient blobs, one-color palette variants, fake reviews, fake awards, fake urgency, and stock-like decorative imagery.

## Ecommerce Component Standards

- Product cards: stable image aspect ratio, product title clamp, visible price/currency, clear category/attribute signal where useful, tap-safe CTA, and no title/price/button overlap at 360px.
- Collection/category modules: make browsing obvious with category names, representative real images, product counts when available, and real archive links.
- Forms: labels remain visible, inputs are large enough on mobile, validation states are clear, and checkout fields are not restyled in a way that breaks WooCommerce.
- Buttons: primary, secondary, text, and icon button styles are consistent. Each has hover, focus, disabled, and active states.
- Tables/comparisons: use horizontal scroll or stacked rows on mobile rather than squeezing text.
- Notices/trust strips: shipping time, COD/payment, returns, age/compliance, and support facts must be truthful and target-market appropriate.

## Target-Market Fit

The aesthetic system must follow the target country/language and site strategy:

- Western/Central Europe: restrained, factual, clear privacy/returns/COD or payment facts, moderate density, precise typography.
- North America/Oceania: more spacious, image-led commerce, strong trust/review areas only when real, obvious purchase paths.
- East Asia: denser specs, comparison, visual product cues, and compact but legible mobile modules.
- Southeast Asia/Middle East/Latin America/Africa: mobile-first navigation, COD/local payment/support visibility, WhatsApp/contact prominence when real.
- RTL markets: verify direction, typography, drawer side, icons, and alignment.

Autonomous mode may choose the aesthetic direction from the available site facts, but it must record the reason and still pass the visual QA gates.

## Visual QA Gate

Before showing a preview, importing page HTML, or reporting completion, verify:

- Desktop and mobile screenshots show a coherent header, footer, spacing rhythm, and typography scale.
- Viewports 360px, 390px, 430px, tablet, and desktop have no horizontal scroll, clipped buttons, text overlap, or blocked taps.
- Header/mobile drawer/footer/product cards/forms have hover/focus/active states and obvious affordances.
- Page sections are not repetitive clones; each section has a buyer, trust, navigation, SEO, education, or support purpose.
- No placeholder text, placeholder image, fake social proof, empty `#` link, broken icon, broken image, or default Elementor styling remains.
- Browser console has no interaction errors from menu, accordion, tab, slider, filter, cart, or form scripts.
- The build ledger records `frontend_ui_system_defined`, `tokens_defined`, `header_aesthetic_pass`, `footer_aesthetic_pass`, `page_aesthetic_pass`, and screenshot or viewport evidence.
