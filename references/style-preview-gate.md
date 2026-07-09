# Style Preview Gate

Use this before full-site buildout. The agent should be highly automated after approval, but the first homepage direction must be reviewed by the user so the whole site does not inherit the wrong style.

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

- Brand name and logo if available.
- Real product/category names or service names.
- Real market/language/currency/shipping/compliance signals.
- Proposed header menu and footer menu.
- First viewport hero.
- Product/category sections.
- Trust/shipping/compliance strip.
- Payment method block, including cash on delivery if the user selected it.
- Ordering steps and checkout rule preview.
- Featured products or dynamic product container preview.
- FAQ or buyer guidance section.
- Blog/guide teaser if SEO is part of the site.
- Mobile behavior notes or a responsive HTML prototype.

Minimum homepage preview structure:

- Top notice bar for shipping, payment, minimum order, or age/compliance.
- Header with logo, primary navigation, account/cart/search affordance or clear placeholders.
- Hero with concrete store facts and primary actions.
- At least 6 meaningful homepage sections after the hero.
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

Make the preview feel specific:

- Use product specs, shipping details, service limits, categories, real policies, and brand constraints.
- Let navigation and page hierarchy look like an actual store, not a pitch deck.
- Use restrained, credible copy and natural microcopy.
- Prefer real product/category images when available.
