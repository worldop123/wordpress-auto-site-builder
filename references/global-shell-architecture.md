# Global Shell Architecture: Header, Footer, CSS, and JS

## Overview

This reference defines how to implement global header, footer, CSS, and JS so that they are injected once globally, rather than being repeated in every Elementor HTML page. This eliminates the tedious process of adding header/footer/menu code to every page import.

## CRITICAL: Architecture Principle

The old approach embedded header, footer, and navigation HTML in every Elementor HTML widget. This is:
- **Tedious**: Every page import requires the same header/footer code.
- **Error-prone**: Header/footer changes require updating every page.
- **Bloated**: Duplicate HTML/CSS/JS on every page increases page weight.
- **Unmaintainable**: Menu changes require editing all pages.

The new approach uses **global injection**:
- **Global Header**: Injected via Code Snippets PHP hook `wp_body_open`.
- **Global Footer**: Injected via Code Snippets PHP hook `wp_footer`.
- **Global CSS**: Added via WordPress Appearance → Customize → Additional CSS.
- **Global JS**: Added via Code Snippets HTML/JS snippet with `wp_footer` hook.
- **Page-specific content**: Only page-unique HTML/CSS/JS in Elementor HTML widgets.

This means each Elementor HTML page contains ONLY the page body content — no header, no footer, no menu, no global CSS, no global JS. The global shell handles all shared elements.

Before implementing the global shell, read `frontend-ui-aesthetic-system.md`. The global shell is also the visual baseline for the whole site: design tokens, shared component styles, header quality, footer quality, mobile drawer behavior, and ecommerce affordances must be defined and verified before page HTML begins.

## DEAD RULE: Global Shell Must Be Created BEFORE Page HTML

**This is a DEAD RULE. The global shell (header, footer, footer menu, global CSS, global JS, and shared menu behavior) MUST be created, activated, and verified on the front-end BEFORE any production page HTML is generated, pasted, imported, or updated in Elementor.** See `agent-enforcement-rules.md` Section 11.7 for the complete step-by-step import order.

Import order (MANDATORY — no reordering):
1. **Frontend UI system** — define design tokens, shared component styles, icon approach, mobile drawer behavior, and header/footer layout rules from `frontend-ui-aesthetic-system.md`.
2. **Global header** (Code Snippets PHP, `wp_body_open` hook, priority 5) — verify on front-end for structure, interaction, and visual polish.
3. **Global footer** (Code Snippets PHP, `wp_footer` hook, priority 10) — verify on front-end for structure, trust content, and visual polish.
4. **Global CSS** (Appearance → Customize → Additional CSS) — design tokens, header/footer styles, shared components, and responsive breakpoints; verify it loads on all pages.
5. **Global JS** (Code Snippets HTML/JS, `wp_footer` hook) — verify mobile menu, cart counter, smooth scroll, cookie/compliance interactions as needed.
6. **Dynamic renderers** (Code Snippets PHP/JS where needed) — prepare data containers for real products/posts before page HTML depends on them.
7. **ONLY THEN** generate/import page HTML into Elementor (one page at a time, Canvas set and verified first).

**Why**: If page HTML is generated or imported before the global shell is active, agents tend to duplicate header/footer/menu/CSS/JS inside every page and later fight conflicts. The global shell must be in place first so the agent can confirm page HTML contains only page-specific content.

The build ledger must record the global shell gate before page HTML begins: `frontend_ui_system_defined`, `tokens_defined`, snippet names/IDs, hooks, menu sources, Additional CSS status, global JS status, tested URLs, desktop/mobile header result, footer result, `header_aesthetic_pass`, `footer_aesthetic_pass`, and no-duplicate evidence.

## Global Header Implementation

### Method: Code Snippets PHP Hook

Create a persistent Code Snippet with the following structure:

```php
// Snippet Name: Global Site Header
// Type: persistent
// Hook: wp_body_open (fires right after <body> tag)

add_action('wp_body_open', 'site_global_header', 5);

function site_global_header() {
    // Only render on front-end, not admin
    if (is_admin()) return;

    // Get menu items from WordPress
    $primary_menu = wp_nav_menu([
        'theme_location' => 'menu-1', // Hello Elementor primary location
        'menu_class' => 'site-header-nav',
        'container' => 'nav',
        'container_class' => 'site-header-nav-container',
        'echo' => false,
        'fallback_cb' => false,
    ]);

    // Get site info
    $site_name = get_bloginfo('name');
    $site_url = home_url('/');
    $shop_url = home_url('/shop/');
    $cart_url = wc_get_cart_url(); // WooCommerce cart URL

    // Output the header HTML
    ?>
    <header class="site-global-header" id="site-header">
        <div class="site-header-inner">
            <div class="site-header-logo">
                <a href="<?php echo esc_url($site_url); ?>">
                    <?php
                    $logo_id = get_theme_mod('custom_logo');
                    if ($logo_id) {
                        echo wp_get_attachment_image($logo_id, 'full', false, ['class' => 'site-logo-img']);
                    } else {
                        echo esc_html($site_name);
                    }
                    ?>
                </a>
            </div>

            <button class="site-header-toggle" aria-label="Toggle menu" aria-expanded="false">
                <span></span><span></span><span></span>
            </button>

            <div class="site-header-nav-wrapper">
                <?php echo $primary_menu; ?>
            </div>

            <div class="site-header-actions">
                <a href="<?php echo esc_url($cart_url); ?>" class="site-header-cart" aria-label="Cart">
                    <svg><!-- cart icon --></svg>
                    <span class="cart-count"><?php echo WC()->cart->get_cart_contents_count(); ?></span>
                </a>
            </div>
        </div>
    </header>

    <div class="site-mobile-menu" id="site-mobile-menu" aria-hidden="true">
        <?php echo $primary_menu; ?>
    </div>
    <?php
}
```

### Header CSS (in Appearance → Customize → Additional CSS)

All header styling goes in the Additional CSS section, NOT in the snippet or page HTML:

The header must pass the header quality gate in `frontend-ui-aesthetic-system.md`: stable logo sizing, balanced spacing, hover/focus/active states, cart/search/account affordances when useful, tested mobile drawer, and no awkward wrapping or overlap.

```css
/* === GLOBAL HEADER === */
.site-global-header {
    position: sticky;
    top: 0;
    z-index: 1000;
    background: var(--site-bg-header, #ffffff);
    border-bottom: 1px solid var(--site-border, #e0e0e0);
    width: 100%;
}

.site-header-inner {
    max-width: 1400px;
    margin: 0 auto;
    padding: 0 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    height: 72px;
}

.site-header-logo img {
    max-height: 48px;
    width: auto;
}

.site-header-nav-container ul {
    display: flex;
    list-style: none;
    gap: 32px;
    margin: 0;
    padding: 0;
}

.site-header-nav-container a {
    text-decoration: none;
    color: var(--site-text-nav, #333333);
    font-weight: 500;
    font-size: 15px;
    transition: color 0.2s;
}

.site-header-nav-container a:hover {
    color: var(--site-accent, #0066cc);
}

/* Mobile menu toggle */
.site-header-toggle {
    display: none;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
}

.site-header-toggle span {
    display: block;
    width: 24px;
    height: 2px;
    background: var(--site-text-nav, #333333);
    margin: 4px 0;
    transition: 0.3s;
}

/* Mobile menu */
.site-mobile-menu {
    display: none;
    position: fixed;
    top: 0;
    right: -100%;
    width: 80%;
    max-width: 320px;
    height: 100vh;
    background: var(--site-bg-header, #ffffff);
    z-index: 1001;
    padding: 80px 24px 24px;
    transition: right 0.3s ease;
    overflow-y: auto;
}

.site-mobile-menu.active {
    right: 0;
}

.site-mobile-menu ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.site-mobile-menu li {
    margin-bottom: 16px;
}

.site-mobile-menu a {
    display: block;
    padding: 12px 0;
    font-size: 18px;
    color: var(--site-text-nav, #333333);
    text-decoration: none;
}

/* Responsive */
@media (max-width: 768px) {
    .site-header-nav-wrapper {
        display: none;
    }
    .site-header-toggle {
        display: block;
    }
}
```

### Header JS (in Code Snippets HTML/JS snippet)

Create a separate Code Snippet (HTML/JS type) for the header interaction JavaScript:

```javascript
// Snippet Name: Global Header JS
// Type: persistent
// Hook: wp_footer

add_action('wp_footer', function() {
    if (is_admin()) return;
    ?>
    <script>
    (function() {
        // Mobile menu toggle
        var toggle = document.querySelector('.site-header-toggle');
        var menu = document.getElementById('site-mobile-menu');

        if (toggle && menu) {
            toggle.addEventListener('click', function() {
                menu.classList.toggle('active');
                toggle.classList.toggle('active');
                var expanded = toggle.getAttribute('aria-expanded') === 'true';
                toggle.setAttribute('aria-expanded', !expanded);
            });

            // Close menu when clicking a link
            menu.querySelectorAll('a').forEach(function(link) {
                link.addEventListener('click', function() {
                    menu.classList.remove('active');
                    toggle.classList.remove('active');
                    toggle.setAttribute('aria-expanded', 'false');
                });
            });

            // Close menu when clicking outside
            document.addEventListener('click', function(e) {
                if (!menu.contains(e.target) && !toggle.contains(e.target)) {
                    menu.classList.remove('active');
                    toggle.classList.remove('active');
                    toggle.setAttribute('aria-expanded', 'false');
                }
            });
        }
    })();
    </script>
    <?php
});
```

## Global Footer Implementation

### Method: Code Snippets PHP Hook

Create a persistent Code Snippet:

```php
// Snippet Name: Global Site Footer
// Type: persistent
// Hook: wp_footer

add_action('wp_footer', 'site_global_footer', 5);

function site_global_footer() {
    if (is_admin()) return;

    $footer_menu = wp_nav_menu([
        'theme_location' => 'footer', // Footer menu location
        'menu_class' => 'site-footer-nav',
        'container' => 'nav',
        'container_class' => 'site-footer-nav-container',
        'echo' => false,
        'fallback_cb' => false,
    ]);

    $site_name = get_bloginfo('name');
    $year = date('Y');

    ?>
    <footer class="site-global-footer" id="site-footer">
        <div class="site-footer-inner">
            <div class="site-footer-grid">
                <div class="site-footer-col site-footer-about">
                    <h4><?php echo esc_html($site_name); ?></h4>
                    <p><?php echo esc_html(get_bloginfo('description')); ?></p>
                </div>

                <div class="site-footer-col site-footer-links">
                    <h4>Quick Links</h4>
                    <?php echo $footer_menu; ?>
                </div>

                <div class="site-footer-col site-footer-contact">
                    <h4>Contact</h4>
                    <p>Email: <?php echo esc_html(get_option('admin_email')); ?></p>
                </div>

                <div class="site-footer-col site-footer-social">
                    <h4>Follow Us</h4>
                    <!-- Social links from site_config -->
                </div>
            </div>

            <div class="site-footer-bottom">
                <p>&copy; <?php echo $year; ?> <?php echo esc_html($site_name); ?>. All rights reserved.</p>
            </div>
        </div>
    </footer>
    <?php
}
```

### Footer CSS (in Additional CSS)

All footer styling goes in Additional CSS alongside header styling, using the same CSS variables.

The footer must pass the footer quality gate in `frontend-ui-aesthetic-system.md`: brand/contact block, shop/category links, policy links, payment/shipping/support facts, compliance note when needed, responsive columns or grouped mobile sections, readable logo variant, and tappable links.

## Global CSS Strategy

### Where to Put Global CSS

**Location**: WordPress Admin → Appearance → Customize → Additional CSS

This is the single source of truth for all global styles:
- CSS variables (brand colors, fonts, spacing).
- Global reset/normalize (minimal, don't conflict with WooCommerce).
- Header styles.
- Footer styles.
- Mobile responsive breakpoints.
- Shared component styles (buttons, forms, cards).

### CSS Variables (Design Tokens)

Define all design tokens as CSS variables in Additional CSS:

Use `frontend-ui-aesthetic-system.md` before choosing token values. Tokens must reflect the brand, target market, product media, and approved preview; do not leave generic blue/purple defaults unless they are explicitly appropriate.

```css
:root {
    /* Brand Colors */
    --site-primary: #0066cc;
    --site-secondary: #1a1a2e;
    --site-accent: #ff6b35;
    --site-bg-main: #ffffff;
    --site-bg-alt: #f8f9fa;
    --site-bg-header: #ffffff;
    --site-bg-footer: #1a1a2e;

    /* Text Colors */
    --site-text-main: #333333;
    --site-text-light: #666666;
    --site-text-white: #ffffff;
    --site-text-nav: #333333;

    /* Borders */
    --site-border: #e0e0e0;

    /* Spacing */
    --site-spacing-xs: 4px;
    --site-spacing-sm: 8px;
    --site-spacing-md: 16px;
    --site-spacing-lg: 24px;
    --site-spacing-xl: 48px;
    --site-spacing-2xl: 80px;

    /* Typography */
    --site-font-heading: 'Inter', sans-serif;
    --site-font-body: 'Inter', sans-serif;
    --site-font-size-base: 16px;
    --site-line-height: 1.6;

    /* Container */
    --site-container-max: 1400px;
    --site-container-padding: 24px;

    /* Transitions */
    --site-transition: 0.3s ease;

    /* Shadows */
    --site-shadow-sm: 0 1px 3px rgba(0,0,0,0.1);
    --site-shadow-md: 0 4px 12px rgba(0,0,0,0.1);
    --site-shadow-lg: 0 8px 24px rgba(0,0,0,0.15);
}
```

### What Goes in Additional CSS vs Page HTML

| CSS Type | Location | Example |
|----------|----------|---------|
| CSS variables | Additional CSS | `--site-primary: #0066cc` |
| Global reset | Additional CSS | `* { box-sizing: border-box }` |
| Header styles | Additional CSS | `.site-global-header { ... }` |
| Footer styles | Additional CSS | `.site-global-footer { ... }` |
| Button styles | Additional CSS | `.site-btn { ... }` |
| Form styles | Additional CSS | `.site-form { ... }` |
| Responsive breakpoints | Additional CSS | `@media (max-width: 768px)` |
| Page hero section | Page HTML `<style>` | `.home-hero { ... }` |
| Page product grid | Page HTML `<style>` | `.home-products { ... }` |
| Page-specific layout | Page HTML `<style>` | `.contact-map { ... }` |

### Rule: Page HTML CSS Must Be Scoped
Page-specific CSS in Elementor HTML widgets must use scoped class names:
```css
/* Good: scoped */
.home-page .hero-section { ... }
.about-page .team-grid { ... }

/* Bad: global (conflicts with other pages) */
.hero-section { ... }
.team-grid { ... }
```

## Global JS Strategy

### Where to Put Global JS

**Location**: Code Snippets → Add New → HTML/JS snippet (or PHP snippet that outputs JS via wp_footer)

Global JS includes:
- Header mobile menu toggle.
- Footer interactions.
- Cart counter update (AJAX).
- Smooth scroll.
- Lazy load polyfills.
- Analytics tracking (GA4, Facebook Pixel).
- Cookie consent banner.
- Age/compliance gate.

### What Goes in Global JS vs Page HTML

| JS Type | Location | Example |
|---------|----------|---------|
| Mobile menu toggle | Global JS (Code Snippets) | Header hamburger menu |
| Cart counter | Global JS (Code Snippets) | WooCommerce AJAX cart |
| Analytics | Global JS (Code Snippets) | GA4, Facebook Pixel |
| Cookie consent | Global JS (Code Snippets) | GDPR banner |
| Page slider | Page HTML `<script>` | Homepage hero slider |
| Page form validation | Page HTML `<script>` | Contact form validation |
| Page accordion | Page HTML `<script>` | FAQ accordion |

### Rule: Page HTML JS Must Be Scoped
Page-specific JS in Elementor HTML widgets must be scoped and use IIFE:
```javascript
// Good: scoped IIFE
(function() {
    var slider = document.querySelector('.home-hero-slider');
    if (!slider) return;
    // slider logic
})();

// Bad: global (conflicts with other pages)
var slider = document.querySelector('.home-hero-slider');
```

## What Each Elementor HTML Page Contains

With the global shell architecture, each Elementor HTML page contains ONLY:

1. **Page-specific HTML**: The unique content for that page (hero, product grid, form, etc.).
2. **Page-specific CSS**: Scoped styles for page elements only.
3. **Page-specific JS**: Scoped JavaScript for page interactions only.
4. **Dynamic containers**: `data-site-render` attributes for dynamic content injection.

### What Each Page Does NOT Contain:
- No header HTML (injected by global shell).
- No footer HTML (injected by global shell).
- No navigation menu HTML (injected by global shell).
- No global CSS variables (in Additional CSS).
- No global JS (in Code Snippets).
- No repeated header/footer styling.

### Example: Homepage HTML Widget Content
```html
<!-- Homepage-specific content only -->
<main class="home-page">
    <style>
        /* Only homepage-specific styles, scoped */
        .home-page .hero { ... }
        .home-page .featured-products { ... }
    </style>

    <section class="hero">
        <h1>Welcome to [Brand]</h1>
        <p>Tagline here</p>
        <a href="/shop/" class="site-btn">Shop Now</a>
    </section>

    <section class="featured-products">
        <h2>Featured Products</h2>
        <div data-site-render="home-products"></div>
    </section>

    <script>
        // Only homepage-specific JS, scoped IIFE
        (function() {
            // Homepage slider or interactions
        })();
    </script>
</main>
```

## Dynamic Content Renderer

The global shell also includes a dynamic content renderer that fills `data-site-render` containers:

```php
// Snippet Name: Dynamic Content Renderer
// Type: persistent
// Hook: wp_footer (after page HTML is rendered)

add_action('wp_footer', 'site_dynamic_renderer', 10);

function site_dynamic_renderer() {
    if (is_admin()) return;
    ?>
    <script>
    // Dynamic content renderer runs after page load
    (function() {
        // Find all data-site-render containers
        document.querySelectorAll('[data-site-render]').forEach(function(container) {
            var type = container.getAttribute('data-site-render');
            // Fetch content via REST API and inject
            // e.g., home-products, home-posts, blog-posts
        });
    })();
    </script>
    <?php
}
```

Alternatively, render content server-side via PHP:

```php
// Server-side dynamic rendering (preferred for SEO)
add_action('wp_body_open', 'site_render_dynamic_content', 20);

function site_render_dynamic_content() {
    if (is_front_page()) {
        // Output products directly into the page
        add_filter('the_content', function($content) {
            if (has_block('html') || is_page()) {
                $products_html = site_get_featured_products_html(8);
                $content = str_replace(
                    '<div data-site-render="home-products"></div>',
                    $products_html,
                    $content
                );
            }
            return $content;
        });
    }
}
```

## Snippet Inventory for Global Shell

| Snippet Name | Type | Hook | Purpose |
|--------------|------|------|---------|
| Global Site Header | persistent | wp_body_open | Render header HTML with menu, logo, cart |
| Global Site Footer | persistent | wp_footer | Render footer HTML with links, contact |
| Global Header JS | persistent | wp_footer | Header JS (mobile menu, cart counter) |
| Global Footer JS | persistent | wp_footer | Footer JS (smooth scroll, analytics) |
| Dynamic Content Renderer | persistent | wp_footer | Fill data-site-render containers |
| Compliance Gate | persistent | wp_body_open | Age/compliance verification (if needed) |
| Cache Purge on Save | persistent | save_post | Auto-purge SG cache after content changes |
| WooCommerce Cart Fragments Fix | persistent | wp_enqueue_scripts | Disable cart fragments on non-shop pages |

## Migration from Old Approach

When rebuilding an old site that used the old approach (header/footer in every page):

1. **Extract** the header HTML/CSS/JS from existing pages.
2. **Create** the global header snippet (Code Snippets).
3. **Create** the global footer snippet (Code Snippets).
4. **Move** global CSS to Additional CSS.
5. **Move** global JS to Code Snippets.
6. **Update** each page HTML to remove header/footer/global CSS/global JS.
7. **Keep** only page-specific content in each Elementor HTML widget.
8. **Test** that header/footer appear correctly on all pages.
9. **Test** mobile menu works.
10. **Verify** no duplicate header/footer on any page.

## Verification Checklist

- [ ] `frontend-ui-aesthetic-system.md` was read before implementation.
- [ ] Frontend UI system was recorded in the build ledger (`frontend_ui_system_defined`, `tokens_defined`).
- [ ] Global header appears on all front-end pages.
- [ ] Global footer appears on all front-end pages.
- [ ] Mobile menu toggle works on all pages.
- [ ] Primary menu links work and navigate correctly.
- [ ] Footer menu links work and navigate correctly.
- [ ] Cart counter updates when items are added.
- [ ] No duplicate header/footer on any page.
- [ ] No duplicate global CSS on any page.
- [ ] No duplicate global JS on any page.
- [ ] CSS variables defined in Additional CSS.
- [ ] Page-specific CSS is scoped to page class.
- [ ] Page-specific JS uses IIFE.
- [ ] Dynamic content containers are filled.
- [ ] Header/footer do not appear in Elementor editor.
- [ ] Header/footer do not appear in wp-admin.
- [ ] All pages load correctly on mobile.
- [ ] All pages load correctly on desktop.
- [ ] No 404s on any header/footer assets (logo, icons).
- [ ] Header and footer pass aesthetic QA: balanced spacing, stable logo size, readable typography, useful ecommerce affordances, target-market trust cues, hover/focus/active states, and no cramped or oversized elements.
