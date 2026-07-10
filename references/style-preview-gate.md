# Style Preview Gate

Use this before full-site buildout. The agent should be highly automated after approval, but the first homepage direction must be reviewed by the user so the whole site does not inherit the wrong style.

Read `frontend-ui-aesthetic-system.md` before generating the preview. The preview must demonstrate the future global UI system: design tokens, header/footer direction, component style, ecommerce affordances, mobile drawer behavior, and target-market visual density.

## When required

Required for:

- New site builds.
- Full redesigns.
- Industry, brand, or market changes.
- Any request where the user says the site must not look AI-generated or template-like.

Can be skipped only when:

- The user explicitly says to skip review and build directly.
- The task is a narrow repair that does not change visual direction.

## Preview content

Generate one complete homepage style preview using real inputs. Do not make a thin mockup with only a hero and one product row.

If the user supplied a product CSV or the site already has WooCommerce products, inspect that product data first and use the product knowledge ledger as preview input. The preview must reflect actual product categories, representative products, price/currency signals, product media availability, shipping/compliance constraints, and likely buyer questions.

- Brand name and logo if available.
- Real product/category names or service names.
- Real market/language/currency/shipping/compliance signals.
- Proposed header menu and footer menu.
- First viewport hero.
- Product/category sections.
- Rich merchandising modules selected from the target market and product data, such as a dynamic product-image slideshow, collection strip, category image grid, comparison block, guide hub, or support/COD ordering module.
- Trust/shipping/compliance strip.
- Payment method block, including cash on delivery if the user selected it.
- Ordering steps and checkout rule preview.
- Featured products or dynamic product container preview.
- FAQ or buyer guidance section.
- Blog/guide teaser if SEO is part of the site.
- Mobile behavior notes or a responsive HTML prototype.
- Design-token summary: palette, typography, spacing, radii, button/form/card style, icon direction, and mobile breakpoint behavior.

Minimum homepage preview structure:

- Top notice bar for shipping, payment, minimum order, or age/compliance.
- Header with logo, primary navigation, account/cart/search affordance or clear placeholders.
- Hero with concrete store facts and primary actions.
- At least 6 meaningful homepage sections after the hero.
- At least 2 sections must use real product/category/post data when those records exist, with real links and real media. Do not hardcode product names, prices, images, or URLs into static HTML; use dynamic render containers or a preview clearly marked as data-driven.
- Footer with contact, policy links, category/shop links, payment/shipping note, and compliance note.
- Responsive behavior for desktop, tablet, and mobile; mobile navigation may be represented as a compact preview if not interactive.

Do not use placeholder slogans such as "Your trusted partner", "Discover the future", "Premium quality products", or fake customer claims.

## Preview formats

Use the most practical available format:

- Local HTML file with scoped CSS for review.
- Screenshot or browser preview if a local server/browser is available.
- Markdown summary plus the generated home HTML file when UI preview is not possible.
- Draft WordPress page only if the user allowed live-site drafts.

The preview should be enough for the user to judge visual direction, homepage density, header/footer completeness, section rhythm, and mobile behavior. It is not a full finished site, but it must not feel perfunctory.

Before presenting the preview, verify that any slideshow, carousel, accordion, tab, filter, or expandable module has visible controls, works on touch and mouse, does not trap focus, and does not block product/category links.

Also verify the preview against the frontend UI aesthetic gate: header and footer feel production-worthy, spacing and typography are balanced, product cards/forms/buttons have clear states, mobile 360/390/430px layouts do not overflow, and no default Elementor or generic AI styling remains.

## Approval checkpoint

After producing the preview, ask for approval or specific edits. Do not bulk-create/import all pages yet.

Acceptable user responses:

- Approved: continue full build using this style system.
- Minor edits: revise the preview once, then continue after approval.
- New direction: generate a substantially different preview, not a small color swap.
- Skip gate: continue full automation and record that the gate was waived.

## Anti-AI design review

Before showing the preview, remove common AI-site patterns:

- Generic blue/purple gradients with floating cards.
- Repetitive three-card feature rows without real content.
- Vague adjectives replacing concrete product/service details.
- Oversized hero copy that says little.
- Decorative sections that do not help shopping, trust, navigation, or SEO.
- Fake urgency, fake reviews, fake awards, or unsupported claims.
- Identical section rhythm across Home, About, Contact, and policy pages.
- Header/footer that merely exist but look cramped, oversized, unbalanced, or disconnected from the page design.
- One-note palettes made from the same hue, default blue/purple SaaS gradients, decorative blobs, or empty glass-card effects.

Make the preview feel specific:

- Use product specs, shipping details, service limits, categories, real policies, and brand constraints.
- Let navigation and page hierarchy look like an actual store, not a pitch deck.
- Use restrained, credible copy and natural microcopy.
- Prefer real product/category images when available.
- Include enough real internal paths for the preview to show how buyers move from homepage modules into products, categories, guides, policies, and contact/support.
