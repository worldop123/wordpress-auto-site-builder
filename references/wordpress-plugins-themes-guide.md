# WordPress Plugins, Themes, and Settings Guide

Comprehensive official reference for WordPress core settings, plugin configurations, theme structure, and hook system. Use this as the authoritative source when configuring any WordPress site built with this skill.

## WordPress Core Settings

All settings are stored in the `wp_options` table and accessed via `get_option()` / `update_option()`. Managed under wp-admin → Settings.

### General Settings (`Settings → General`)

| Field | Option Key | Default | Notes |
|---|---|---|---|
| Site Title | `blogname` | — | Displayed by themes, browser titlebar |
| Tagline | `blogdescription` | empty | Short phrase |
| WordPress Address (URL) | `siteurl` | — | Configurable via `WP_SITEURL` in wp-config.php |
| Site Address (URL) | `home` | — | Configurable via `WP_HOME` in wp-config.php |
| Administration Email | `new_admin_email` | — | Receives moderation, registration, fatal error notices |
| Membership — Anyone can register | `users_can_register` | 0 | Checkbox |
| New User Default Role | `default_role` | `subscriber` | Choices: Administrator, Editor, Author, Contributor, Subscriber |
| Site Language | `WPLANG` | `en_US` | Dashboard language |
| Timezone | `timezone_string` / `gmt_offset` | UTC+0 | Select a city or Etc/GMT offset |
| Date Format | `date_format` | `F j, Y` | PHP date format |
| Time Format | `time_format` | `g:i a` | PHP time format |
| Week Starts On | `start_of_week` | 1 (Monday) | Sunday = 0 |

### Reading Settings (`Settings → Reading`)

| Field | Option Key | Default | Notes |
|---|---|---|---|
| Front page displays | `show_on_front` | `posts` | `posts` (latest posts) or `page` (static page) |
| Front page ID | `page_on_front` | 0 | Page ID when `show_on_front = page` |
| Posts page ID | `page_for_posts` | 0 | Blog page ID; cannot equal `page_on_front` |
| Posts per page | `posts_per_page` | 10 | Blog pages show at most |
| RSS items | `posts_per_rss` | 10 | Syndication feeds |
| RSS excerpt | `rss_use_excerpt` | 0 | 0 = Full text, 1 = Excerpt |
| Search Engine Visibility | `blog_public` | 1 | 0 outputs `<meta name='robots' content='noindex,nofollow'>` and stops ping services |

### Permalinks Settings (`Settings → Permalinks`)

| Option | Structure | Example |
|---|---|---|
| Plain (default) | (empty) | `/?p=123` |
| Day and name | `/%year%/%monthnum%/%day%/%postname%/` | `/2008/03/31/sample-post/` |
| Month and name | `/%year%/%monthnum%/%postname%/` | `/2008/03/sample-post/` |
| Numeric | `/archives/%post_id%` | `/archives/123` |
| Post name (recommended) | `/%postname%/` | `/sample-post` |

Structure tags: `%year%`, `%monthnum%`, `%day%`, `%hour%`, `%minute%`, `%second%`, `%post_id%`, `%postname%`, `%category%`, `%author%`.

Optional: Category base (`category_base`), Tag base (`tag_base`). Visiting the Permalinks screen triggers a rewrite rules flush.

### Media Settings (`Settings → Media`)

| Size | Width | Height | Crop |
|---|---|---|---|
| Thumbnail | 150px | 150px | Hard crop (1) |
| Medium | 300px | 300px | Proportional |
| Large | 1024px | 1024px | Proportional |

Organize uploads into month/year folders: `uploads_use_yearmonth_folders` = 1 (default). Upload path: `wp-content/uploads`.

### Discussion Settings (`Settings → Discussion`)

Key options:
- `default_comment_status` — Allow comments on new articles (default: open)
- `require_name_email` — Comment author must fill out name and email
- `comment_registration` — Users must be registered to comment
- `close_comments_for_old_posts` / `close_comments_days_old` — Auto-close after X days
- `thread_comments` / `thread_comments_depth` — Threaded comments (max 10 levels)
- `comment_moderation` — Admin must always approve
- `comment_whitelist` — Author must have a previously approved comment
- `show_avatars` / `avatar_rating` / `avatar_default` — Avatar display

### Privacy Settings (`Settings → Privacy`)

- Select a Privacy Policy page (stored in `wp_page_for_privacy` option)
- `get_privacy_policy_url()`, `the_privacy_policy_link()` — Developer functions

## WordPress Database Structure

12 default core tables (prefix configurable via `$table_prefix` in wp-config.php, default `wp_`):

| Table | Purpose | Key Relationships |
|---|---|---|
| `wp_posts` | All content (posts, pages, attachments, revisions, custom post types) | `post_author` → `wp_users.ID`; `post_parent` → self |
| `wp_postmeta` | Post metadata (custom fields) | `post_id` → `wp_posts.ID` (one-to-many) |
| `wp_terms` | Terms (categories, tags) | `term_id` |
| `wp_term_taxonomy` | Taxonomy classification | `term_id` → `wp_terms.term_id` |
| `wp_term_relationships` | Links posts to terms | `object_id` → `wp_posts.ID`; `term_taxonomy_id` → `wp_term_taxonomy` |
| `wp_termmeta` | Term metadata (WP 4.4+) | `term_id` → `wp_terms.term_id` |
| `wp_options` | Site settings, plugin/theme config | `option_name`, `option_value`, `autoload` |
| `wp_users` | User accounts | `ID` |
| `wp_usermeta` | User metadata & capabilities | `user_id` → `wp_users.ID`; stores `{$prefix}capabilities` |
| `wp_comments` | Comments & trackbacks | `comment_post_ID` → `wp_posts.ID`; `comment_parent` → self |
| `wp_commentmeta` | Comment metadata | `comment_id` → `wp_comments.comment_ID` |
| `wp_links` | Blogroll links (legacy) | `link_id` |

The `$wpdb` object exposes table references: `$wpdb->posts`, `$wpdb->postmeta`, `$wpdb->terms`, `$wpdb->options`, etc. Key methods: `get_var()`, `get_row()`, `get_col()`, `get_results()`, `insert()`, `update()`, `delete()`, `prepare()` (SQL injection protection with `%s`, `%d`, `%f`).

## WordPress REST API

Base URL: `https://example.com/wp-json/`. Uses JSON exclusively.

### Key Endpoints

| Resource | Route |
|---|---|
| Posts | `/wp/v2/posts` |
| Pages | `/wp/v2/pages` |
| Media | `/wp/v2/media` |
| Categories | `/wp/v2/categories` |
| Tags | `/wp/v2/tags` |
| Users | `/wp/v2/users` |
| Comments | `/wp/v2/comments` |
| Settings | `/wp/v2/settings` |
| Themes | `/wp/v2/themes` |
| Plugins | `/wp/v2/plugins` |
| Nav Menus | `/wp/v2/menus` |
| Nav Menu Items | `/wp/v2/menu-items` |
| Menu Locations | `/wp/v2/menu-locations` |
| Application Passwords | `/wp/v2/users/<id>/application-passwords` |

### CRUD Operations

| Operation | Method | Endpoint |
|---|---|---|
| List | `GET` | `/wp/v2/posts` |
| Retrieve | `GET` | `/wp/v2/posts/<id>` |
| Create | `POST` | `/wp/v2/posts` (JSON body) |
| Update | `POST`/`PUT`/`PATCH` | `/wp/v2/posts/<id>` (JSON body) |
| Delete | `DELETE` | `/wp/v2/posts/<id>` (`?force=true` to bypass trash) |

### Authentication Methods

1. **Application Passwords** (built-in since WP 5.6) — Generated from wp-admin → Users → Edit User. Uses HTTP Basic Auth over HTTPS. Preferred for remote/external applications.
   ```
   curl --user "USERNAME:APP_PASSWORD" https://HOSTNAME/wp-json/wp/v2/users?context=edit
   ```
2. **Cookie Authentication** (built-in) — Used when logged into wp-admin. Requires nonces (`_wpnonce` parameter or `X-WP-Nonce` header, action: `wp_rest`).
3. **OAuth 1.0a / JWT** — Via third-party plugins for remote auth.

### Common Parameters

`_fields` (limit response fields), `_embed` (embed linked resources), `context` (`view`, `embed`, `edit`), `page`, `per_page` (max 100), `offset`, `search`, `order`, `orderby`, `include`, `exclude`. Response headers: `X-WP-Total` (total items), `X-WP-TotalPages`.

## WordPress Hook System

### Actions vs Filters

- **Action** — Runs at a specific point; callback performs a task and returns nothing. Registered with `add_action()`, fired with `do_action()`.
- **Filter** — Modifies data; callback accepts a value, modifies it, and MUST return it. Registered with `add_filter()`, applied with `apply_filters()`.

### Registration

```php
add_action( string $hook_name, callable $callback, int $priority = 10, int $accepted_args = 1 );
add_filter( string $hook_name, callable $callback, int $priority = 10, int $accepted_args = 1 );
```

- `$priority` — Lower numbers run earlier (default 10).
- `$accepted_args` — Number of arguments the callback accepts (default 1).

### Common Core Hooks

| Hook | Type | When it fires |
|---|---|---|
| `init` | Action | After WordPress fully loads; register post types, taxonomies |
| `wp_head` | Action | Inside `<head>`; output styles, meta tags |
| `wp_footer` | Action | Before `</body>`; scripts, analytics |
| `wp_body_open` | Action (WP 5.2+) | Immediately after `<body>` opens |
| `wp_enqueue_scripts` | Action | Front-end script/style enqueue |
| `template_redirect` | Action | Before template loading; redirects |
| `template_include` | Filter | Override template path |
| `save_post` | Action | After a post is saved (passes `$post_id`, `$post`) |
| `the_content` | Filter | Filters post content before display |
| `body_class` | Filter | Filters CSS classes on `<body>` |
| `pre_get_posts` | Action | Before main query runs |
| `after_setup_theme` | Action | Theme setup; `add_theme_support()` |
| `widgets_init` | Action | Register sidebars/widgets |
| `admin_menu` | Action | Register admin menu pages |
| `rest_api_init` | Action | Register custom REST routes |

### Common WooCommerce Hooks

| Hook | Type | Purpose |
|---|---|---|
| `woocommerce_before_main_content` | Action | Before shop content |
| `woocommerce_after_main_content` | Action | After shop content |
| `woocommerce_before_shop_loop` | Action | Before product loop |
| `woocommerce_after_shop_loop` | Action | After product loop |
| `woocommerce_before_single_product` | Action | Before single product |
| `woocommerce_single_product_summary` | Action | Single product summary area |
| `woocommerce_before_add_to_cart_button` | Action | Before add-to-cart |
| `woocommerce_after_add_to_cart_button` | Action | After add-to-cart |
| `woocommerce_cart_contents` | Action | Inside cart table |
| `woocommerce_payment_complete` | Action | After payment completes |
| `woocommerce_product_get_price` | Filter | Filter product price |
| `woocommerce_get_price_html` | Filter | Filter price HTML output |

## WordPress Template Hierarchy

WordPress searches down the hierarchy and uses the **first matching file** found; falls back to `index.php`.

### By Page Type

**Front Page:**
1. `front-page.php` → 2. `home.php` → 3. `page.php` → 4. `index.php`

**Single Post:**
1. `single-{post_type}-{slug}.php` → 2. `single-{post_type}.php` → 3. `single.php` → 4. `singular.php` → 5. `index.php`

**Single Page:**
1. Custom page template → 2. `page-{slug}.php` → 3. `page-{id}.php` → 4. `page.php` → 5. `singular.php` → 6. `index.php`

**Category:**
1. `category-{slug}.php` → 2. `category-{id}.php` → 3. `category.php` → 4. `archive.php` → 5. `index.php`

**Tag:**
1. `tag-{slug}.php` → 2. `tag-{id}.php` → 3. `tag.php` → 4. `archive.php` → 5. `index.php`

**Custom Taxonomy:**
1. `taxonomy-{taxonomy}-{term}.php` → 2. `taxonomy-{taxonomy}.php` → 3. `taxonomy.php` → 4. `archive.php` → 5. `index.php`

**Custom Post Type Archive:**
1. `archive-{post_type}.php` → 2. `archive.php` → 3. `index.php`

**Author:** `author-{nicename}.php` → `author-{id}.php` → `author.php` → `archive.php` → `index.php`

**Date:** `date.php` → `archive.php` → `index.php`

**Search:** `search.php` → `index.php`

**404:** `404.php` → `index.php`

## WordPress User Roles and Capabilities

| Role | Slug | Key Capabilities |
|---|---|---|
| Super Admin | `administrator` (multisite) | All capabilities + multisite management |
| Administrator | `administrator` | `manage_options`, `edit_theme_options`, `activate_plugins`, `switch_themes`, `upload_files`, `manage_categories`, `moderate_comments`, full content management |
| Editor | `editor` | Publish/manage own + others' posts/pages, `manage_categories`, `moderate_comments`, `upload_files` |
| Author | `author` | `edit_posts`, `publish_posts`, `edit_published_posts`, `delete_posts`, `delete_published_posts`, `upload_files` |
| Contributor | `contributor` | `edit_posts`, `delete_posts` (cannot publish) |
| Subscriber | `subscriber` | `read` only |

**WooCommerce roles:**
- `customer` — `read` only; can edit own account, view orders
- `shop_manager` — Editor capabilities + `manage_woocommerce`, `view_woocommerce_reports`

## WooCommerce Settings

Settings stored in `wp_options` (keyed `woocommerce_*`), accessible via REST API: `GET /wp-json/wc/v3/settings/{group_id}`.

### General Tab

| Field | Option Key | Default |
|---|---|---|
| Store address | `woocommerce_store_address` | — |
| Store city | `woocommerce_store_city` | — |
| Store postcode | `woocommerce_store_postcode` | — |
| Default country | `woocommerce_default_country` | `""` (format `"US"` or `"US:CA"`) |
| Selling locations | `woocommerce_allowed_countries` | `all` (`all`, `specific`, `all_except`) |
| Ship to countries | `woocommerce_ship_to_countries` | `""` (default = billing/shipping) |
| Default customer address | `woocommerce_default_customer_address` | `geolocation` |
| Enable tax calculation | `woocommerce_calc_taxes` | `no` |
| Enable coupons | `woocommerce_enable_coupons` | `yes` |
| Currency | `woocommerce_currency` | `USD` (ISO 4217) |
| Currency position | `woocommerce_currency_pos` | `left` (`left`, `right`, `left_space`, `right_space`) |
| Thousand separator | `woocommerce_price_thousand_sep` | `,` |
| Decimal separator | `woocommerce_price_decimal_sep` | `.` |
| Number of decimals | `woocommerce_price_num_decimals` | `2` |

### Products Tab

| Field | Option Key | Default |
|---|---|---|
| Shop page display | `woocommerce_shop_page_display` | `""` (products; `subcategories`, `both`) |
| Default sorting | `woocommerce_default_catalog_orderby` | `menu_order` |
| Category display | `woocommerce_category_display` | `""` (products) |
| Redirect to cart after add | `woocommerce_cart_redirect_after_add` | `no` |
| Enable AJAX add to cart | `woocommerce_enable_ajax_add_to_cart` | `no` |
| Catalog columns | `woocommerce_catalog_columns` | `4` |
| Catalog rows | `woocommerce_catalog_rows` | `4` |
| Manage stock | `woocommerce_manage_stock` | `yes` |
| Hide out of stock items | `woocommerce_hide_out_of_stock_items` | `no` |

**Product image sizes:**
- `woocommerce_thumbnail` — 300×300, crop true (catalog)
- `woocommerce_single` — 600×600, crop false (single product)
- `woocommerce_gallery_thumbnail` — 100×100, crop true (gallery thumbs)

### Shipping Tab

- Shipping zones managed via `WC_Shipping_Zone` data objects
- Core methods: `flat_rate`, `free_shipping`, `local_pickup`
- Shipping classes: `product_shipping_class` taxonomy
- `woocommerce_shipping_cost_requires_address` — default `no`
- `woocommerce_enable_shipping_debug` — default `no`

### Payments Tab

Payment gateways stored as `woocommerce_<gateway_id>_settings`. Core gateways:
- `bacs` — Direct bank transfer
- `cheque` — Check payments
- `cod` — Cash on delivery
- `ppcp-gateway` — PayPal Payments
- `stripe` — Stripe

Common gateway fields: `enabled` (yes/no), `title`, `description`, `instructions`.

REST API: `GET/POST /wp-json/wc/v3/payment_gateways` and `/payment_gateways/{id}`.

### Accounts & Privacy Tab

| Field | Option Key | Default |
|---|---|---|
| Guest checkout | `woocommerce_enable_guest_checkout` | `no` |
| Login reminder on checkout | `woocommerce_enable_checkout_login_reminder` | `no` |
| Signup/login from checkout | `woocommerce_enable_signup_and_login_from_checkout` | `yes` |
| My Account registration | `woocommerce_enable_myaccount_registration` | `no` |
| Auto-generate username | `woocommerce_registration_generate_username` | `yes` |
| Auto-generate password | `woocommerce_registration_generate_password` | `yes` |

### Emails Tab

Sender: `woocommerce_mail_from_name` (site title), `woocommerce_mail_from` (admin email).
Template: `woocommerce_email_base_color` (#7f54b3), `woocommerce_email_background_color` (#f7f7f7), `woocommerce_email_text_color` (#3c3c3c).

Core email notifications:
`new_order`, `cancelled_order`, `failed_order`, `order_on_hold`, `processing_order`, `completed_order`, `refunded_order`, `customer_invoice`, `customer_note`, `customer_reset_password`, `customer_new_account`, `low_stock`, `no_stock`.

### Advanced Tab

Page bindings: `woocommerce_shop_page_id`, `woocommerce_cart_page_id`, `woocommerce_checkout_page_id`, `woocommerce_myaccount_page_id`, `woocommerce_terms_page_id`.

Endpoints:
- Checkout: `woocommerce_checkout_pay_endpoint` (`order-pay`), `woocommerce_checkout_order_received_endpoint` (`order-received`)
- Account: `woocommerce_myaccount_orders_endpoint` (`orders`), `woocommerce_myaccount_view_order_endpoint` (`view-order`), `woocommerce_myaccount_edit_account_endpoint` (`edit-account`), `woocommerce_myaccount_edit_address_endpoint` (`edit-address`), `woocommerce_myaccount_payment_methods_endpoint` (`payment-methods`), `woocommerce_myaccount_lost_password_endpoint` (`lost-password`), `woocommerce_myaccount_logout_endpoint` (`customer-logout`)

### WooCommerce REST API

Base URL: `/wp-json/wc/v3/`. Authentication: Consumer Key / Consumer Secret (HTTP Basic Auth over HTTPS, or OAuth 1.0a for HTTP).

Key endpoints: `/products`, `/products/{id}/variations`, `/products/categories`, `/products/tags`, `/products/attributes`, `/orders`, `/orders/{id}/notes`, `/orders/{id}/refunds`, `/customers`, `/coupons`, `/shipping/zones`, `/taxes`, `/payment_gateways`, `/settings`, `/reports`, `/system_status`.

### WooCommerce Shortcodes

| Shortcode | Purpose |
|---|---|
| `[woocommerce_cart]` | Cart page |
| `[woocommerce_checkout]` | Checkout page |
| `[woocommerce_my_account]` | My Account page |
| `[woocommerce_order_tracking]` | Order tracking form |
| `[products]` | Products by parameters (replaces legacy shortcodes) |
| `[product_page]` | Full single product page (id, sku) |
| `[product_category]` | Products in a category |
| `[product_categories]` | Product categories list |
| `[add_to_cart]` | Add-to-cart button (id, style, sku) |
| `[add_to_cart_url]` | Add-to-cart URL (id, sku) |

`[products]` parameters: `limit`, `columns` (default 3), `orderby` (date, id, menu_order, popularity, rand, rating, title), `order` (ASC/DESC), `category`, `cat_operator` (IN/NOT IN/AND), `ids`, `skus`, `visibility`, `class`, `attribute`, `terms`, `terms_operator`, `tag`, `paginate`, `per_page`, `on_sale`, `best_selling`, `top_rated`.

## Elementor Settings

Managed under wp-admin → Elementor → Settings and Elementor Editor → Site Settings.

### Elementor Settings (wp-admin → Elementor → Settings)

**General:**
- Post Types (`elementor_cpt_supports`) — Where Elementor is usable
- Disable Default Colors (`elementor_disable_color_schemes`)
- Disable Default Fonts (`elementor_disable_typography_schemes`)

**Advanced:**
- CSS Print Method (`elementor_css_print_method`) — `external` (recommended) or `internal`
- Google Fonts — Load / Disable
- Load Font Awesome 4 Support — Yes/No (loads v4 shim)
- Enable Unfiltered File Uploads — SVG/JSON uploads
- Switch Editor Loader Method — Server config conflict resolver

**Performance:**
- Optimized Image Loading — `fetchpriority="high"` on LCP, `loading="lazy"` on below-fold
- Optimized Gutenberg Loading — Ignores unused Gutenberg blocks

### Elementor Experiments (Feature Flags)

Key experiments to enable:
- **Flexbox Container** — Active (modern layout, replaces Sections/Columns)
- **Inline Font Icons** — Active (SVG icons, no icon fonts)
- **Lazy Load Background Images** — Active
- **Optimized DOM** — Active (reduced wrapper markup)
- **Optimized CSS Loading** — Active (external CSS)
- **Optimized JS Loading** — Active
- **Additional Custom Breakpoints** — Configure as needed (default: Desktop, Tablet, Mobile)

### Elementor Site Settings (Editor → Site Settings)

**Design System:**
- Global Colors — Primary, Secondary, Text, Accent + custom
- Global Fonts — Primary, Secondary, Text, Accent + custom

**Theme Style:**
- Background, Headings (H1–H6), Buttons, Images, Form Fields
- Header/Footer customization

**Settings:**
- Site Identity — Site Name, Description, Logo, Favicon
- Background — Site background + mobile
- Layout — Content width, widget spacing, page layout
- Lightbox — Enable, colors, dimensions
- Custom CSS (Pro) — Global custom CSS

### Elementor Page Settings (per-document)

Stored in `_elementor_page_settings` post meta:
- **Page Layout** — `default` (theme), `elementor_canvas` (blank, no header/footer), `elementor_full_width` (full width with theme header/footer)
- **Hide Title** — Show/hide page title
- **Hide Header / Hide Footer** — Via Theme Builder conditions
- **Custom CSS** (Pro) — Per-page CSS

### Elementor Data Structure

Page data saved as serialized JSON in `wp_postmeta`:
- `_elementor_data` — Page content (array of elements)
- `_elementor_page_settings` — Document settings
- `_elementor_version` — Elementor version
- `_elementor_template_type` — Template type
- `_elementor_edit_mode` — Edit mode

Element types: Container Element (Flexbox), Widget Element, Section/Column (legacy), Repeaters, Responsive Data (per-breakpoint), Global Styles.

### Elementor Widget Types

**Basic (free):** Heading, Image, Text Editor, Video, Button, Divider, Spacer, Google Maps, Icon, Image Box, Icon Box, Star Rating, Image Carousel, Icon List, Counter, Progress, Tabs, Accordion, Toggle, Social Icons, Alert, SoundCloud, Shortcode, HTML, Menu Anchor, Sidebar.

**Pro:** Posts, Portfolio, Gallery, Form, Slides, Carousel, Testimonial, Price Table, Flip Box, Call to Action, Media Carousel, Price List, Animated Headline, Hotspots, Login, Search, Nav Menu, Lottie, Code Highlight, Table.

**WooCommerce:** Products, Product Categories, Add to Cart, Product Title, Product Price, Product Images, Product Add to Cart, Product Meta, Product Additional Information, Product Tabs, Upsells, Related Products, Product Short Description, Product Rating, Product Stock, Breadcrumbs.

## Code Snippets Plugin

### Snippet Types

- **PHP snippets** — Executed via WordPress hooks; replaces `functions.php` customizations
- **HTML snippets** — Output via auto-generated shortcodes or auto-insert positions
- **CSS snippets** — Applied to front-end stylesheet
- **JavaScript snippets** (Pro) — Front-end script execution

### Snippet Fields

- **Title** — Human-readable name
- **Code** — Snippet body
- **Description** — Optional notes
- **Tags** — Keywords for organization
- **Scope** — Global, Admin, Front-end, Single-site, Network
- **Priority** — Execution priority (default 10, lower runs first)
- **Active/Inactive** — Toggle without deleting
- **Conditions** (Pro) — Reusable conditional rules with AND/OR operators

### PHP Snippet Hooks

Common hooks for Code Snippets PHP:
- `wp_head`, `wp_footer`, `wp_body_open` — Front-end output injection
- `init`, `wp_loaded`, `admin_init`, `admin_menu` — Initialization
- `wp_enqueue_scripts`, `admin_enqueue_scripts` — Asset registration
- `the_content`, `woocommerce_before_main_content`, `woocommerce_after_main_content` — Content injection
- `template_redirect`, `template_include` — Template control

### HTML/CSS/JS Auto-Insert Positions

- **HTML auto-insert:** After header, Before footer, After content, Before content, Custom (shortcode or hook)
- **CSS scope:** Global, specific page, specific post type, or via conditions
- **JS scope:** Global or conditionally scoped

### Snippet Conditions (Pro)

- Reusable conditional rules saved as separate entities
- AND/OR operators for combining rules
- Targets: specific pages/posts, post types, user roles, taxonomies, devices, schedules

## Hello Elementor Theme

### Overview

Lightweight, minimalist theme built specifically for Elementor. Version 3.4.9. Requires WP 6.0+, PHP 7.4+. Free, GPL v3. No jQuery on frontend (vanilla JS since v3.0.0).

### Theme Support Features

| Feature | Arguments |
|---|---|
| `post-thumbnails` | (no args) |
| `automatic-feed-links` | (no args) |
| `title-tag` | (no args) |
| `html5` | `['search-form','comment-form','comment-list','gallery','caption','script','style','navigation-widgets']` |
| `custom-logo` | `['height'=>100,'width'=>350,'flex-height'=>true,'flex-width'=>true]` |
| `align-wide` | (no args) |
| `responsive-embeds` | (no args) |
| `editor-styles` | + `add_editor_style('assets/css/editor-styles.css')` |
| `woocommerce` | (conditional) |
| `wc-product-gallery-zoom` | WooCommerce gallery zoom |
| `wc-product-gallery-lightbox` | WooCommerce gallery lightbox |
| `wc-product-gallery-slider` | WooCommerce gallery slider |

Also: `add_post_type_support('page', 'excerpt')` — pages get excerpts.

### Menu Locations

| Location ID | Label |
|---|---|
| `menu-1` | Header |
| `menu-2` | Footer |

IMPORTANT: Hello Elementor uses `menu-1` (Header) and `menu-2` (Footer), NOT "primary". The Footer menu only appears when Elementor is active.

### Widget Areas

Hello Elementor does NOT register any sidebars/widget areas. Add via child theme `functions.php` using `register_sidebar()` on `widgets_init` hook if needed.

### Enqueued Assets

| Handle | File |
|---|---|
| `hello-elementor` | `assets/css/reset.css` |
| `hello-elementor-theme-style` | `assets/css/theme.css` |
| `hello-elementor-header-footer` | `assets/css/header-footer.css` (only when header/footer display enabled) |
| `hello-elementor-frontend` | `js/hello-frontend.min.js` (only when header/footer display enabled) |

### Elementor Integration

`hello_elementor_register_elementor_locations()` hooked to `elementor/theme/register_locations` registers all core Elementor Theme Builder locations (header, footer, single, archive).

When a page uses Elementor Canvas template, `hello_elementor_display_header_footer()` returns false, and the theme's header/footer markup + CSS are not loaded.

### Customizer Options

Minimal native Customizer:
- **Site Identity** — Logo, site title, tagline, favicon
- **Menus** — Header (`menu-1`) and Footer (`menu-2`) locations
- **Homepage Settings** — Standard WP front page display
- **Header & Footer** styling (v3.2.0+)
- **Additional CSS** — Standard WordPress textarea

No native color or typography Customizer panels. Global colors/fonts managed via Elementor Site Settings.

### Theme Settings Page (Admin)

- Disable description meta tag
- Disable skip link
- Disable page title
- Unregister Hello `style.css`
- Unregister Hello `theme.css`
- Disable cross-site header & footer (v3.0.0+)

### Customization Methods (Priority Order)

1. **Elementor Site Settings** — Global colors, fonts, site identity, header/footer, buttons, layout (recommended)
2. **Additional CSS** — Customizer textarea
3. **Code Snippets / child theme functions.php** — PHP via Code Snippets plugin or child theme
4. **Filter hooks** — `hello_elementor_add_theme_support`, `hello_elementor_register_menus`, `hello_elementor_enqueue_style`, `hello_elementor_header_footer`, etc.

### Hello Elementor Child Theme

- Child `style.css` must include `Template: hello-elementor`
- Child `functions.php` loads BEFORE parent (augments, does not override)
- Template files override by filename
- Use `get_template_directory_uri()` for parent assets, `get_stylesheet_directory_uri()` for child assets

## WordPress Theme Structure

### Standard Theme Files

**Required:**
- `style.css` — Theme header + styles
- `index.php` — Main fallback template
- `screenshot.png` — 1200×900 recommended

**Core structural:**
- `functions.php` — Theme functions
- `header.php`, `footer.php`, `sidebar.php`

**Templates (by hierarchy):**
- `front-page.php`, `home.php`
- `single.php`, `page.php`, `singular.php`, `privacy-policy.php`
- `archive.php`, `category.php`, `tag.php`, `taxonomy.php`, `author.php`, `date.php`
- `search.php`, `404.php`
- `attachment.php`, `image.php`
- `comments.php`

### style.css Header

```css
/*
Theme Name: My Theme
Theme URI: https://example.com
Author: Author Name
Author URI: https://example.com
Description: Theme description
Version: 1.0.0
Requires at least: 6.0
Tested up to: 6.5
Requires PHP: 7.4
License: GNU General Public License v2 or later
License URI: http://www.gnu.org/licenses/gpl-2.0.html
Text Domain: my-theme
Tags: tag1, tag2
*/
```

### functions.php Best Practices

- Hook setup to `after_setup_theme`
- Namespace functions
- Use `add_theme_support()` for features
- Use `register_nav_menus()` for menu locations
- Use `register_sidebar()` on `widgets_init` for widget areas
- Use `wp_enqueue_script()` / `wp_enqueue_style()` on `wp_enqueue_scripts`
- Set `$content_width` if needed

### Child Theme Creation

1. Create `wp-content/themes/{child-slug}/`
2. Create `style.css` with `Template: parent-folder-name`
3. Enqueue parent + child styles in child `functions.php`
4. Override parent templates by adding same-named files

## Common Security Plugins

### Wordfence Security

- WAF (endpoint firewall, real-time rules)
- Malware scanner (file integrity, malware signatures)
- Login security (2FA, CAPTCHA, brute force protection)
- Live traffic monitoring
- IP/user-agent/country blocking (Premium)

### Sucuri Security

- Security activity auditing
- File integrity monitoring
- Remote malware scanning (SiteCheck)
- Blocklist monitoring
- Security hardening (remove WP version, block PHP in uploads)
- Firewall (Premium WAF)

### iThemes Security / Kadence Security

- Two-factor authentication
- Password requirements/enforcement
- Brute force protection (local + network)
- File change detection
- Site scanner
- Database backups
- Security site templates (Ecommerce, Network, Non-Profit, etc.)

### All-In-One Security (AIOS)

- Login lockdown (limit failed attempts)
- 2FA (Google/Microsoft/Authy)
- File permission scanner
- Firewall (.htaccess rules, PHP firewall, 6G rules)
- Audit log
- Security score system

## Common Performance/Caching Plugins

### WP Rocket (Premium)

- Page caching + cache preloading (sitemap-based)
- GZIP compression
- Minify CSS/JS, combine CSS/JS
- Load JS deferred, delay JS execution
- LazyLoad (images, iframes, videos)
- WebP cache variant
- Critical path CSS
- Database optimization
- CDN integration
- eCommerce optimization (excludes sensitive pages)

### W3 Total Cache

- Page cache (disk/memcached/Redis)
- Minify (HTML/CSS/JS)
- Database cache, object cache
- Browser cache (ETag, cache-control)
- CDN support
- Lazy load, WebP/AVIF conversion
- Fragment cache (Pro)

### WP Super Cache

- Static HTML generation
- 3 serving methods: Expert (mod_rewrite), Simple (PHP), WP-Cache
- CDN support (OSSDL CDN off-linker)
- Cache preloading
- Garbage collection
- Requires `define('WP_CACHE', true)` in wp-config.php

### LiteSpeed Cache

- Server-level caching (LiteSpeed/OpenLiteSpeed servers)
- Object cache (Memcached/Redis)
- Image optimization + WebP/AVIF
- Minify CSS/JS/HTML, combine, critical CSS
- Lazy load, defer/delay JS
- QUIC.cloud CDN
- WooCommerce/bbPress support
- ESI (Edge Side Includes)

### SG Optimizer (SiteGround)

- Dynamic Caching (SiteGround-exclusive)
- File-based Caching
- Memcached (SiteGround-exclusive)
- HTTPS Enforce, GZIP, Browser Caching
- CSS/JS Minify, Defer JS
- WebP conversion, Image Compression
- Lazy Load
- IMPORTANT: Do NOT enable Combine CSS/JS (breaks Elementor)
- Remove Query Strings, Disable Emojis
- DNS Pre-fetch, Web Fonts Optimization

## Image Optimization Plugins

### Smush

- Lossless & lossy compression
- WebP & AVIF conversion (Pro)
- Lazy Load (images, iframes, videos)
- Auto-resize (Pro)
- Image CDN (Pro)
- Directory Smush (optimize non-Media Library images)
- Free limit: images over 5MB skipped

### ShortPixel

- Lossy, Glossy, Lossless compression
- WebP & AVIF conversion
- PDF optimization
- HEIC support
- Background/bulk optimization, WP-CLI
- AI features: Upscale, Background Removal, ALT text generation
- CDN integration
- Free: 100 credits/month

### Imagify

- Smart Compression (auto-balanced), Lossless
- WebP & AVIF (free plan)
- Auto-resize oversized images (max 2560px)
- Bulk optimization (async)
- Original backup + restore
- Optimizes JPG, PNG, WebP, PDF, GIF
- Free: 20MB/month (~200 images)

### EWWW Image Optimizer

- Free: unlimited local optimization
- Lossless JPG/PNG/GIF/SVG, WebP
- Lazy Load with auto-scaling (prevents CLS)
- Bulk optimize (Media Library + theme + custom folders)
- Premium: 5× compression, PDF, AVIF, CDN, watermarking
- WP-CLI support
- Works on Windows/Linux/MacOS/FreeBSD
