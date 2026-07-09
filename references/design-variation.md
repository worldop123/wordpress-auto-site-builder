# Design Variation and Anti-AI Rules

Every build must feel custom and human-made. Before generating HTML/CSS, choose a design seed and document it briefly in the internal plan. For new builds, first produce a homepage style preview and wait for approval using `style-preview-gate.md`.

## Vary these dimensions

- Hero composition: centered editorial, asymmetric product showcase, compact commerce dashboard, magazine grid, category-first, trust-first, seasonal campaign, or service-led.
- Section order: product-first, problem/solution, category navigation, shipping/trust, blog education, FAQ, brand story.
- Card treatment: border-only, soft shadow, image-led, split rows, table-like specs, carousel-like strips, dense catalog, editorial tiles.
- Typography scale: restrained commerce, luxury spacious, technical specs, friendly DTC, wholesale practical.
- Palette: derive from brand/logo/product photos; avoid reusing the previous site's dominant colors.
- Buttons and icons: consistent but not identical across projects.
- Blog article layouts: alternate guide, comparison, checklist, buyer FAQ, shipping explainer, product spotlight, category overview, and troubleshooting formats.

## Non-negotiables

- Mobile must be polished, not an afterthought.
- Text must fit within containers.
- Buttons must be tap-friendly.
- Avoid decorative clutter that hurts shopping.
- Do not use a landing-page style when the site needs an operational storefront.
- Include real product/category signals early in the first viewport.
- Preserve WooCommerce templates for transactional pages.
- Avoid designs that look like an AI-generated SaaS landing page unless the business actually is SaaS.
- Avoid generic gradients, empty glass cards, vague icons, and repetitive "feature card" layouts.
- Avoid copy that sounds generated: "elevate your experience", "seamless solutions", "unleash potential", "discover the future", "premium quality", "cutting-edge", and similar filler.
- Avoid fake social proof, fake awards, fake testimonials, fake scarcity, and unsupported brand claims.
- Use concrete store facts: product types, specs, delivery areas, minimum order, warranty/return terms, customer support path, category names, and compliance notices.
- Make page sections earn their place. Each section should help buying, trust, navigation, SEO, or support.

## Target-Market Layout Rules

The visual system must be selected from the target country/language, not copied from the previous build.

- Western and Central Europe: moderate density, precise copy, restrained palette, clear grids, visible GDPR/privacy/cookie/return information. Mobile product sections should usually support 2-column cards at 390px when titles can be clamped safely.
- North America and Oceania: more spacious commerce, larger product imagery, review/trust signals, clear add-to-cart paths, and generous white space.
- East Asia: denser information, stronger product/spec tables, more visual signals, and smaller but still legible mobile modules.
- Southeast Asia, Middle East, Latin America, and Africa: mobile-first, COD or local payment trust, WhatsApp/support visibility, faster scanning, and low-friction category/product access.
- Arabic/Middle East builds must evaluate RTL layout, Arabic typography, and culturally appropriate trust imagery.
- Do not choose one-column mobile product cards as the default. Use one column only when product names/images cannot fit professionally at 360px, or when the target market/style deliberately calls for editorial single-card browsing.
- Mixed layouts are encouraged: category chips, compact 2-column product cards, one full-width featured product, horizontal comparison strips, and FAQ/document sections can coexist.

## Page-Type Variation Within One Brand System

All pages should share tokens, button shape, spacing rhythm, and typography, but their layout must match intent:

- Home: market-specific commerce overview with early product/category signals.
- Shop/category/product: WooCommerce templates plus reversible UX snippets; do not rebuild as static Elementor pages.
- About: brand/operator trust, support path, shipping region, and regulated-product stance.
- FAQ: accordion or question groups with concise answers and FAQ schema when appropriate.
- Contact: email/WhatsApp/support process, expected response, order-information checklist.
- Policy pages: document-style layouts with summaries, steps, tables, and support callouts. No shallow single-paragraph filler.
- Blog: alternate article layouts by topic type; guides, comparisons, shipping explainers, buyer FAQs, and product spotlights should not all look identical.

## Mobile Overflow Gate

Before delivery, test at 360px, 390px, and 430px widths:

- No horizontal scroll.
- Product card titles clamp without covering price or buttons.
- Buttons remain at least 44px tall.
- Floating WhatsApp/cart/search widgets do not overlap checkout, add-to-cart, or update-cart controls.
- Header, menu, quantity steppers, and checkout fields remain tappable.
- If any layout overflows, revise CSS and re-test before final reporting.

## Human-feeling copy

Write like a competent site owner, not a marketing generator:

- Prefer short, specific sentences.
- Use real nouns from the product/service catalog.
- Mention limitations plainly where needed.
- Keep policy and checkout copy practical.
- Let product descriptions carry SEO depth; keep homepage copy crisp.
- Vary paragraph lengths and section rhythm.

Before delivery, scan headings/buttons. If they could fit any unrelated store, rewrite them with brand/category/product specifics.

## Elementor HTML block pattern

Use scoped class names and a wrapper:

```html
<main class="brand-home site-scope-v1">
  <section class="hero">...</section>
  <section class="featured-products">
    <div class="product-grid" data-site-render="home-products"></div>
  </section>
  <section class="latest-guides">
    <div class="post-grid" data-site-render="home-posts"></div>
  </section>
</main>
```

Do not include global reset CSS that can damage WooCommerce admin, Elementor canvas, checkout, or plugin UI.
