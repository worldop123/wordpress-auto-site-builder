# WordPress and Elementor Structure Reference

## Purpose
This reference MUST be read BEFORE creating any page HTML code. The agent must first understand which pages exist, their slugs, and their URLs, so that all internal links, menu items, buttons, and navigation in generated HTML point to valid, correct page paths. Every link in generated code must correspond to a real WordPress page that has been created or verified to exist.

## WordPress Page Types and Standard Slugs

### Core WordPress Pages
| Page Type | Default Slug | URL Path | Who Creates It |
|-----------|-------------|----------|----------------|
| Home/Front Page | (root) | `/` | Set in Settings → Reading |
| Blog/Posts Page | blog | `/blog/` | Set in Settings → Reading |
| Search Results | (auto) | `/?s=keyword` | WordPress core |
| 404 Page | (auto) | (auto) | Theme template |
| Date Archive | (auto) | `/2025/01/` | WordPress core |
| Author Archive | (auto) | `/author/name/` | WordPress core |
| Tag Archive | (auto) | `/tag/name/` | WordPress core |
| Category Archive | (auto) | `/category/name/` | WordPress core |

### WooCommerce Standard Pages
| Page | Default Slug | URL Path | Shortcode | Notes |
|------|-------------|----------|-----------|-------|
| Shop | shop | `/shop/` | (auto) | WooCommerce product archive |
| Cart | cart | `/cart/` | `[woocommerce_cart]` | WooCommerce owned |
| Checkout | checkout | `/checkout/` | `[woocommerce_checkout]` | WooCommerce owned |
| My Account | my-account | `/my-account/` | `[woocommerce_my_account]` | WooCommerce owned |
| Order Received | order-received | `/checkout/order-received/` | (auto) | Thank you page |
| Terms and Conditions | (custom) | (custom) | (link in checkout) | Referenced by checkout |

### Standard Custom Pages (Created by this skill)
| Page | Recommended Slug | URL Path | Template |
|------|-----------------|----------|----------|
| About Us | about-us | `/about-us/` | Elementor Canvas |
| Contact Us | contact-us | `/contact-us/` | Elementor Canvas |
| FAQ | faq | `/faq/` | Elementor Canvas |
| Shipping Policy | shipping-policy | `/shipping-policy/` | Elementor Canvas or default |
| Return Policy | return-policy | `/return-policy/` | Elementor Canvas or default |
| Privacy Policy | privacy-policy | `/privacy-policy/` | Elementor Canvas or default |
| Terms of Service | terms-of-service | `/terms-of-service/` | Elementor Canvas or default |
| Cookie Policy | cookie-policy | `/cookie-policy/` | Elementor Canvas or default |
| Payment Policy | payment-policy | `/payment-policy/` | Elementor Canvas or default |
| Age Verification | age-verification | `/age-verification/` | Elementor Canvas or default |
| Wholesale | wholesale | `/wholesale/` | Elementor Canvas |

## WordPress Template Hierarchy

### Template Loading Order (most specific to most general)
1. Custom template file assigned to page
2. `page-{slug}.php`
3. `page-{id}.php`
4. `page.php`
5. `singular.php`
6. `index.php`

### Page Templates Available with Hello Elementor
- **Default Template**: Full width with header and footer from theme
- **Elementor Canvas**: Blank canvas, no header/footer (USE THIS for custom HTML pages)
- **Elementor Full Width**: Full width with theme header/footer
- **Theme Builder Header/Footer**: If using Elementor Pro Theme Builder

### Which Pages Use Which Template
- **Elementor Canvas**: Home, About, Contact, FAQ, Policy pages, Landing pages
- **Default/Theme Template**: Shop, Cart, Checkout, My Account (WooCommerce owned)
- **Default Template**: Blog index (if using default blog page)

## WordPress Menu Structure

### Standard Menu Locations (Hello Elementor)
Hello Elementor registers these menu locations:
- `menu-1`: Primary navigation (header)
- No separate mobile menu location by default (handled by responsive CSS)

### If Using Custom Global Shell
The global shell snippet can register custom menu locations:
```php
register_nav_menus([
    'primary' => __('Primary Menu', 'textdomain'),
    'footer' => __('Footer Menu', 'textdomain'),
    'mobile' => __('Mobile Menu', 'textdomain'),
]);
```

### Menu Item Types
- **Page**: Links to a WordPress page by ID
- **Custom Link**: Links to any URL (internal or external)
- **Category**: Links to a WordPress category archive
- **Product Category**: Links to a WooCommerce product category
- **Post**: Links to a specific post

### Menu Creation via Code (for automation)
```php
// Check if menu exists, create if not
$menu_name = 'Primary Menu';
$menu_exists = wp_get_nav_menu_object($menu_name);

if (!$menu_exists) {
    $menu_id = wp_create_nav_menu($menu_name);

    // Add menu items
    wp_update_nav_menu_item($menu_id, 0, [
        'menu-item-title' => 'Home',
        'menu-item-url' => home_url('/'),
        'menu-item-status' => 'publish',
    ]);

    wp_update_nav_menu_item($menu_id, 0, [
        'menu-item-title' => 'Shop',
        'menu-item-url' => home_url('/shop/'),
        'menu-item-status' => 'publish',
    ]);

    // Assign to location
    $locations = get_theme_mod('nav_menu_locations');
    $locations['menu-1'] = $menu_id;
    set_theme_mod('nav_menu_locations', $locations);
}
```

## WordPress Permalink Structure

### Recommended Settings
- Set to `/%postname%/` (Post name) for clean URLs
- Go to Settings → Permalinks → select "Post name" → Save Changes
- MUST save permalinks after creating new pages or changing URL structure
- WooCommerce product categories use `/product-category/category-slug/`
- WooCommerce products use `/product/product-slug/` by default

### Permalink Configuration for WooCommerce
- Product permalink base: `/product/` (default) or custom
- Category base: `/product-category/` (default) or custom
- Tag base: `/product-tag/` (default) or custom
- Configure in: WooCommerce → Settings → Products → Advanced

## WordPress Shortcodes Reference

### WooCommerce Shortcodes
| Shortcode | Purpose | Usage |
|-----------|---------|-------|
| `[woocommerce_cart]` | Display cart page | Cart page only |
| `[woocommerce_checkout]` | Display checkout | Checkout page only |
| `[woocommerce_my_account]` | Display account | My Account page only |
| `[woocommerce_shop]` | Display shop | Usually auto |
| `[products]` | Display products grid | Any page |
| `[product_page id="99"]` | Single product | Any page |
| `[product_category category="slug"]` | Products by category | Any page |
| `[sale_products]` | Products on sale | Any page |
| `[best_selling_products]` | Best sellers | Any page |
| `[recent_products]` | Recent products | Any page |
| `[featured_products]` | Featured products | Any page |
| `[add_to_cart id="99"]` | Add to cart button | Any page |
| `[woocommerce_order_tracking]` | Order tracking | Any page |

### Rank Math Shortcodes
| Shortcode | Purpose | Usage |
|-----------|---------|-------|
| `[rank_math_breadcrumb]` | Display breadcrumbs | Any page |
| `[rank_math_seo_analyzer]` | SEO analysis tool | Admin pages |

### WordPress Core Shortcodes
| Shortcode | Purpose | Usage |
|-----------|---------|-------|
| `[gallery]` | Image gallery | Posts/pages |
| `[caption]` | Image caption | Posts/pages |
| `[embed]` | Embed URL | Posts/pages |
| `[audio]` | Audio player | Posts/pages |
| `[video]` | Video player | Posts/pages |

## Elementor Structure and Settings

### Elementor Editor Interface
- **Panel (left sidebar)**: Contains widgets and elements
- **Canvas (main area)**: Where you build the page
- **Navigator (bottom)**: Element tree structure
- **Settings (gear icon)**: Page settings, layout settings

### Elementor Container System (Recommended)
Modern Elementor uses Flexbox Containers instead of old Sections/Columns:

#### Container Types
- **Box**: Single container, content flows in one direction
- **Flex**: Flexible container with row or column direction
- **Grid**: CSS Grid container (newer Elementor versions)

#### Container Hierarchy
```
Container (Row, Horizontal)
  └── Container (Column, Vertical)
      └── Widget (Heading, Image, Button, etc.)
      └── Widget
  └── Container (Column, Vertical)
      └── Widget
```

#### Container Settings
- Direction: Row (horizontal) or Column (vertical)
- Align Items: Start, Center, End, Stretch
- Justify Content: Start, Center, End, Space Between, Space Around, Space Evenly
- Gap: Space between items
- Wrap: Wrap or No Wrap
- Width: Boxed (max-width) or Full Width

### Elementor Widget Categories
#### Basic Widgets
- **Heading**: Text headings (H1-H6)
- **Image**: Single image with link, caption
- **Text Editor**: Rich text content
- **Video**: Self-hosted or external video
- **Button**: CTA buttons with styling
- **Divider**: Visual separator
- **Spacer**: Vertical space
- **Google Maps**: Embed maps
- **Icon**: Single icon
- **Icon Box**: Icon with title and description

#### General Widgets
- **HTML**: Raw HTML/CSS/JS code (CRITICAL for this skill)
- **Shortcode**: Execute WordPress shortcodes
- **Menu Anchor**: Create scroll-to anchors
- **Sidebar**: Display widget areas
- **Image Box**: Image with title and description
- **Image Carousel**: Sliding images
- **Icons**: Multiple icons in a row
- **Progress Bar**: Animated progress
- **Tabs**: Tabbed content
- **Accordion**: Collapsible content
- **Toggle**: Toggle content
- **Social Icons**: Social media links
- **Star Rating**: Rating display
- **Alert**: Notification boxes
- **SoundCloud**: Audio embed
- **Counter**: Animated numbers
- **Progress**: Progress indicator

#### Pro Widgets (Elementor Pro required)
- **Theme Builder**: Header, Footer, Single Post, Archive templates
- **Popup Builder**: Create popups
- **WooCommerce Builder**: Product pages, archives
- **Form**: Contact forms
- **Nav Menu**: Advanced menu widget
- **Slides**: Advanced slider
- **Portfolio**: Project showcase
- **Gallery**: Advanced gallery
- **Price List**: Menu/price list
- **Price Table**: Pricing comparison
- **Flip Box**: Interactive flip cards
- **Call to Action**: CTA boxes
- **Testimonial Carousel**: Customer reviews

### Elementor Page Settings

#### Page Layout Options
1. **Default Page**: Theme header and footer
2. **Elementor Canvas**: No header, no footer (BLANK canvas)
3. **Elementor Full Width**: Full width, theme header/footer

**IMPORTANT**: Use Elementor Canvas for custom HTML pages. Do NOT use Canvas for WooCommerce pages (Shop, Cart, Checkout, My Account).

#### Page Settings (Gear Icon → Page Settings)
- **Page Title**: Show/hide page title
- **Page Layout**: Default / Canvas / Full Width
- **Hide Header**: Yes/No (Canvas hides by default)
- **Hide Footer**: Yes/No (Canvas hides by default)

### Elementor Global Settings (Site Settings)
Access via hamburger menu (top-left) → Site Settings

#### Global Colors
- Primary: Main brand color
- Secondary: Accent color
- Text: Body text color
- Accent: Link/accent color
- Custom colors: Up to 10 additional

#### Global Typography
- Primary: Heading font
- Secondary: Body font
- Text: Paragraph text
- Accent: Special text
- Custom fonts: Up to 10 additional

#### Site Settings Sections
- **Global Colors**: Brand color palette
- **Global Typography**: Font families and sizes
- **Theme Style**: Theme-level overrides
- **Site Identity**: Logo, site title, favicon
- **Background**: Global background
- **Layout**: Container width, content width
- **Lightbox**: Image lightbox settings
- **Custom CSS**: Global custom CSS (Pro)

### Elementor Performance Settings
Access via Elementor → Settings

#### Performance Optimizations (ENABLE ALL)
- **Flexbox Containers**: Use modern container system (reduces DOM nesting)
- **Optimized DOM Output**: Remove unnecessary wrapper elements
- **Optimized CSS Loading**: Only load CSS for used widgets
- **Optimized Google Fonts Loading**: Load fonts efficiently
- **Lazy Load Background Images**: Defer offscreen background images
- **Font Display Swap**: Use `font-display: swap` for web fonts

#### Advanced Settings
- **CSS Print Method**: Internal CSS or External CSS file
- **Dynamic Lightbox**: Enable/disable
- **Image Sizes**: Configure custom image sizes
- **Unfiltered File Uploads**: Enable for SVG uploads (use with caution)

### Elementor HTML Widget (Critical for this skill)

The HTML widget is the primary method for adding custom page code:

#### How to Use
1. Drag "HTML" widget from the panel to the canvas
2. Paste complete HTML/CSS/JS code into the content area
3. Click Update to save

#### Best Practices
- Use scoped CSS class names (e.g., `.brand-home .hero`)
- Wrap all content in a main container: `<main class="site-scope-v1">...</main>`
- Include all CSS inline within `<style>` tags inside the HTML widget
- Include JavaScript within `<script>` tags inside the HTML widget
- Use `data-site-render` attributes for dynamic content containers
- Do NOT include global CSS resets that affect WooCommerce or admin

#### Dynamic Content Containers
Use data attributes to mark where WordPress should inject dynamic content:
```html
<div data-site-render="home-products"></div>
<div data-site-render="home-posts"></div>
<div data-site-render="blog-posts"></div>
```
The global shell snippet queries these containers and fills them with real product/post data.

### Elementor Responsive Design

#### Breakpoints (Elementor defaults)
- **Desktop**: Default (1025px and above)
- **Tablet**: 768px - 1024px (portrait tablets)
- **Mobile**: Up to 767px (phones)

#### Responsive Controls
Each widget/element has responsive controls:
- Edit the element
- Switch between Desktop, Tablet, Mobile icons at the bottom of the panel
- Adjust settings per device
- Hide elements on specific devices (Advanced → Responsive → Hide on Desktop/Tablet/Mobile)

#### Responsive Best Practices
- Test ALL pages on mobile viewport
- Use container-based layouts (flexbox) for natural responsiveness
- Set mobile-specific font sizes (smaller than desktop)
- Ensure buttons are at least 44x44px on mobile
- Check image aspect ratios on mobile
- Test navigation on mobile (hamburger menu)
- Verify forms are usable on mobile

## Page Creation Workflow (CRITICAL)

The agent MUST follow this order:

### Phase 1: Create All Pages First (Before Writing HTML)
1. Create all WordPress pages with correct slugs (as draft)
2. Note each page's URL: `home_url('/page-slug/')`
3. Verify WooCommerce page bindings (Shop, Cart, Checkout, My Account)
4. Note WooCommerce URLs: `/shop/`, `/cart/`, `/checkout/`, `/my-account/`
5. Note product category URLs: `/product-category/category-slug/`
6. Note blog post URLs: `/blog/post-slug/`

### Phase 2: Build Page URL Map
Create a URL map for use in all generated HTML:
```json
{
  "home": "/",
  "shop": "/shop/",
  "blog": "/blog/",
  "cart": "/cart/",
  "checkout": "/checkout/",
  "my_account": "/my-account/",
  "about": "/about-us/",
  "contact": "/contact-us/",
  "faq": "/faq/",
  "shipping_policy": "/shipping-policy/",
  "return_policy": "/return-policy/",
  "privacy_policy": "/privacy-policy/",
  "terms": "/terms-of-service/",
  "cookie_policy": "/cookie-policy/",
  "payment_policy": "/payment-policy/",
  "product_categories": {
    "category1": "/product-category/category1/",
    "category2": "/product-category/category2/"
  }
}
```

### Phase 3: Generate HTML with Correct Links
When generating page HTML, use the URL map for ALL links:
- Menu items must point to correct page URLs
- Footer links must point to correct policy page URLs
- Category links must point to correct WooCommerce category URLs
- Product links must point to correct product URLs
- Blog links must point to correct post URLs
- All CTAs must point to real, existing pages

### Phase 4: Verify All Links
After HTML is inserted, verify:
- Every link in the HTML points to a real page (not 404)
- Every menu item navigates to the correct page
- Every button navigates to the correct destination
- Every image URL loads (not 404)
- Every category link works
- Every product link works
- Test on BOTH desktop and mobile

## Common WordPress/Elementor Issues

### Page Shows 404 After Creation
- Save permalinks: Settings → Permalinks → Save Changes
- Check page status (Published, not Draft)
- Check page slug matches URL
- Clear cache

### Elementor Canvas Not Working
- Verify Elementor is activated
- Check for conflicting plugins (other page builders)
- Increase PHP memory limit (`WP_MEMORY_LIMIT`, `128M` minimum)
- Check for theme conflicts

### HTML Widget Content Not Showing
- Clear cache (page cache and Elementor cache)
- Verify the page uses Elementor Canvas template
- Check for JavaScript errors in browser console
- Verify HTML is not truncated (Elementor has limits on very large HTML blocks)

### Menu Not Showing
- Verify menu is assigned to a location (Appearance → Menus → Manage Locations)
- If using global shell, verify shell renders `wp_nav_menu()`
- Check menu has items

### WooCommerce Pages Missing
- Go to WooCommerce → Settings → Advanced
- Verify Shop, Cart, Checkout, My Account page assignments
- If pages are missing, recreate with correct shortcodes:
  - Cart: `[woocommerce_cart]`
  - Checkout: `[woocommerce_checkout]`
  - My Account: `[woocommerce_my_account]`

## Elementor Version Differences

### New Elementor UI (Top Bar)
- Page settings moved to top bar
- Click page title or settings icon for Page Layout
- Navigator accessible from top bar
- Device preview icons in top bar

### Old Elementor UI (Bottom-Left Gear)
- Page settings under bottom-left gear icon
- Navigator at bottom
- Device preview at bottom

### Both Versions
- HTML widget works the same way
- Container system available in both
- Page Layout setting location is the main difference

## Elementor and WooCommerce Integration

### Product Pages
- Single product pages: WooCommerce handles these (NOT Elementor Canvas)
- Use Code Snippets to customize product page behavior
- Elementor Pro WooCommerce Builder can customize product templates (optional)

### Shop/Archive Pages
- WooCommerce handles product archives (NOT Elementor Canvas)
- Use Code Snippets or WooCommerce hooks to customize
- Elementor Pro can customize archive templates (optional)

### Cart/Checkout Pages
- WooCommerce owns these pages (NOT Elementor Canvas)
- Use WooCommerce blocks (newer versions) or shortcodes
- Customize via Code Snippets and WooCommerce hooks
