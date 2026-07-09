# WordPress Settings Implementation Guide

Practical guide for configuring WordPress, WooCommerce, Elementor, and Rank Math settings via multiple methods. Every configuration includes the method, exact code/commands, and verification steps. Read `wordpress-plugins-themes-guide.md` for the complete option key reference.

## Configuration Methods Overview

| Method | When to Use | Risk Level |
|---|---|---|
| WordPress REST API | Remote automated configuration, batch updates | Low (API validates input) |
| Code Snippets PHP (`update_option`) | One-time setup, programmatic configuration | Medium (no validation) |
| wp-config.php constants | Server-level settings, security keys | High (can break site) |
| .htaccess rules | Server redirects, caching, security | High (can break site) |
| wp-admin UI | Manual configuration, visual verification | Lowest |

---

## Section 1: WordPress Core Settings via REST API

### 1.1 Read All WordPress Settings

```bash
# Read WordPress settings via REST API
curl -X GET \
  "https://example.com/wp-json/wp/v2/settings" \
  -H "Authorization: Basic $(echo -n 'admin:xxxx xxxx xxxx xxxx xxxx' | base64)" \
  -H "Content-Type: application/json"
```

**Response includes:** `title`, `description`, `timezone`, `date_format`, `time_format`, `default_category`, `default_post_format`, `posts_per_page`, `show_on_front`, `page_on_front`, `page_for_posts`, `use_smilies`, `default_ping_status`, `default_comment_status`.

### 1.2 Update WordPress Settings via REST API

```bash
# Update site title, description, and reading settings
curl -X POST \
  "https://example.com/wp-json/wp/v2/settings" \
  -H "Authorization: Basic $(echo -n 'admin:xxxx xxxx xxxx xxxx xxxx' | base64)" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "My Store",
    "description": "Premium products for modern living",
    "timezone": "America/New_York",
    "date_format": "F j, Y",
    "time_format": "g:i a",
    "posts_per_page": 12,
    "show_on_front": "page",
    "page_on_front": 5,
    "page_for_posts": 12,
    "default_ping_status": "closed",
    "default_comment_status": "closed"
  }'
```

**Verification:** Visit Settings → General and Settings → Reading in wp-admin. Confirm all values match.

### 1.3 Set Permalink Structure via REST API

The REST API settings endpoint does NOT expose permalink structure directly. Use Code Snippets PHP instead:

```php
// One-time snippet: set permalink to /%postname%/
add_action('init', function() {
    global $wp_rewrite;
    $wp_rewrite->set_permalink_structure('/%postname%/');
    $wp_rewrite->flush_rules();
    update_option('permalink_structure', '/%postname%/');
});
```

**Verification:** Visit Settings → Permalinks. Check "Post name" is selected. Visit any blog post URL — should load without 404.

---

## Section 2: WooCommerce Settings via REST API

### 2.1 Read WooCommerce Settings Groups

```bash
# List all WooCommerce settings groups
curl -X GET \
  "https://example.com/wp-json/wc/v3/settings" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json"
```

**Returns:** Array of group objects with `id`, `label`, `description`, `parent_id`, `sub_groups`.

### 2.2 Read General Settings

```bash
# Read WooCommerce general settings
curl -X GET \
  "https://example.com/wp-json/wc/v3/settings/general" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json"
```

### 2.3 Update General Settings via REST API

```bash
# Update WooCommerce general settings
curl -X POST \
  "https://example.com/wp-json/wc/v3/settings/general" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "id": "woocommerce_currency",
      "value": "USD"
    },
    {
      "id": "woocommerce_currency_pos",
      "value": "left"
    },
    {
      "id": "woocommerce_price_thousand_sep",
      "value": ","
    },
    {
      "id": "woocommerce_price_decimal_sep",
      "value": "."
    },
    {
      "id": "woocommerce_price_num_decimals",
      "value": "2"
    },
    {
      "id": "woocommerce_default_country",
      "value": "US"
    },
    {
      "id": "woocommerce_calc_taxes",
      "value": "no"
    },
    {
      "id": "woocommerce_enable_coupons",
      "value": "yes"
    }
  ]'
```

### 2.4 Update Products Settings

```bash
# Update WooCommerce products settings
curl -X POST \
  "https://example.com/wp-json/wc/v3/settings/products" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "id": "woocommerce_shop_page_display",
      "value": ""
    },
    {
      "id": "woocommerce_default_catalog_orderby",
      "value": "menu_order"
    },
    {
      "id": "woocommerce_catalog_columns",
      "value": 4
    },
    {
      "id": "woocommerce_catalog_rows",
      "value": 4
    },
    {
      "id": "woocommerce_cart_redirect_after_add",
      "value": "no"
    },
    {
      "id": "woocommerce_enable_ajax_add_to_cart",
      "value": "yes"
    }
  ]'
```

### 2.5 Update Accounts & Privacy Settings

```bash
# Update WooCommerce accounts & privacy settings
curl -X POST \
  "https://example.com/wp-json/wc/v3/settings/account" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "id": "woocommerce_enable_guest_checkout",
      "value": "yes"
    },
    {
      "id": "woocommerce_enable_checkout_login_reminder",
      "value": "yes"
    },
    {
      "id": "woocommerce_enable_signup_and_login_from_checkout",
      "value": "yes"
    },
    {
      "id": "woocommerce_enable_myaccount_registration",
      "value": "no"
    },
    {
      "id": "woocommerce_registration_generate_username",
      "value": "yes"
    },
    {
      "id": "woocommerce_registration_generate_password",
      "value": "yes"
    }
  ]'
```

### 2.6 Configure WooCommerce Settings via Code Snippets PHP

For bulk configuration without REST API keys:

```php
// One-time snippet: configure all WooCommerce settings at once
add_action('init', function() {
    // General
    update_option('woocommerce_currency', 'USD');
    update_option('woocommerce_currency_pos', 'left');
    update_option('woocommerce_price_thousand_sep', ',');
    update_option('woocommerce_price_decimal_sep', '.');
    update_option('woocommerce_price_num_decimals', 2);
    update_option('woocommerce_default_country', 'US');
    update_option('woocommerce_calc_taxes', 'no');
    update_option('woocommerce_enable_coupons', 'yes');
    
    // Products
    update_option('woocommerce_shop_page_display', '');
    update_option('woocommerce_default_catalog_orderby', 'menu_order');
    update_option('woocommerce_catalog_columns', 4);
    update_option('woocommerce_catalog_rows', 4);
    update_option('woocommerce_cart_redirect_after_add', 'no');
    update_option('woocommerce_enable_ajax_add_to_cart', 'yes');
    update_option('woocommerce_manage_stock', 'yes');
    update_option('woocommerce_hide_out_of_stock_items', 'no');
    
    // Product images
    update_option('woocommerce_thumbnail_cropping', '1:1');
    update_option('woocommerce_thumbnail_cropping_custom_width', 600);
    update_option('woocommerce_thumbnail_cropping_custom_height', 600);
    
    // Accounts & Privacy
    update_option('woocommerce_enable_guest_checkout', 'yes');
    update_option('woocommerce_enable_checkout_login_reminder', 'yes');
    update_option('woocommerce_enable_signup_and_login_from_checkout', 'yes');
    update_option('woocommerce_enable_myaccount_registration', 'no');
    update_option('woocommerce_registration_generate_username', 'yes');
    update_option('woocommerce_registration_generate_password', 'yes');
    
    // Email
    update_option('woocommerce_email_from_name', get_bloginfo('name'));
    update_option('woocommerce_email_from', get_option('admin_email'));
    update_option('woocommerce_email_base_color', '#667eea');
    update_option('woocommerce_email_background_color', '#f7f7f7');
    update_option('woocommerce_email_body_background_color', '#ffffff');
    update_option('woocommerce_email_text_color', '#3c3c3c');
    
    // Bind pages
    $shop = get_page_by_path('shop');
    $cart = get_page_by_path('cart');
    $checkout = get_page_by_path('checkout');
    $account = get_page_by_path('my-account');
    $terms = get_page_by_path('terms-and-conditions');
    
    if ($shop) update_option('woocommerce_shop_page_id', $shop->ID);
    if ($cart) update_option('woocommerce_cart_page_id', $cart->ID);
    if ($checkout) update_option('woocommerce_checkout_page_id', $checkout->ID);
    if ($account) update_option('woocommerce_myaccount_page_id', $account->ID);
    if ($terms) update_option('woocommerce_terms_page_id', $terms->ID);
    
    // Set endpoints
    update_option('woocommerce_checkout_pay_endpoint', 'order-pay');
    update_option('woocommerce_checkout_order_received_endpoint', 'order-received');
    update_option('woocommerce_myaccount_orders_endpoint', 'orders');
    update_option('woocommerce_myaccount_view_order_endpoint', 'view-order');
    update_option('woocommerce_myaccount_edit_account_endpoint', 'edit-account');
    update_option('woocommerce_myaccount_edit_address_endpoint', 'edit-address');
    update_option('woocommerce_myaccount_payment_methods_endpoint', 'payment-methods');
    update_option('woocommerce_myaccount_lost_password_endpoint', 'lost-password');
    update_option('woocommerce_myaccount_logout_endpoint', 'customer-logout');
    
    // Flush rewrite rules for endpoints
    flush_rewrite_rules();
});
```

**Verification:** Visit WooCommerce → Settings. Check each tab. Visit /cart/, /checkout/, /my-account/ — all should load correctly.

---

## Section 3: WooCommerce Shipping Zone Configuration

### 3.1 Create Shipping Zone via REST API

```bash
# Create a shipping zone (e.g., "United States")
curl -X POST \
  "https://example.com/wp-json/wc/v3/shipping/zones" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "United States",
    "order": 1
  }'
```

### 3.2 Add Location to Shipping Zone

```bash
# Add US to the shipping zone (replace ZONE_ID with actual ID)
curl -X POST \
  "https://example.com/wp-json/wc/v3/shipping/zones/ZONE_ID/locations" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '[
    {
      "code": "US",
      "type": "country"
    }
  ]'
```

### 3.3 Add Shipping Methods to Zone

```bash
# Add Flat Rate shipping method
curl -X POST \
  "https://example.com/wp-json/wc/v3/shipping/zones/ZONE_ID/methods" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "method_id": "flat_rate",
    "settings": {
      "title": "Standard Shipping",
      "cost": "9.99",
      "tax_status": "taxable"
    }
  }'

# Add Free Shipping method
curl -X POST \
  "https://example.com/wp-json/wc/v3/shipping/zones/ZONE_ID/methods" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "method_id": "free_shipping",
    "settings": {
      "title": "Free Shipping",
      "requires": "min_amount",
      "min_amount": "100"
    }
  }'

# Add Local Pickup method
curl -X POST \
  "https://example.com/wp-json/wc/v3/shipping/zones/ZONE_ID/methods" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "method_id": "local_pickup",
    "settings": {
      "title": "Local Pickup",
      "cost": "0"
    }
  }'
```

### 3.4 Configure Shipping Zones via Code Snippets PHP

```php
// One-time snippet: create shipping zones programmatically
add_action('init', function() {
    // Check if WooCommerce is active
    if (!class_exists('WooCommerce')) return;
    
    // Create "United States" zone
    $zone = new WC_Shipping_Zone();
    $zone->set_zone_name('United States');
    $zone->set_zone_order(1);
    $zone->add_location('US', 'country');
    $zone->save();
    
    // Add Flat Rate
    $zone->add_shipping_method('flat_rate');
    $flat_rate_instance_id = $zone->get_shipping_methods();
    $flat_rate = end($flat_rate_instance_id);
    $flat_rate->instance_settings['title'] = 'Standard Shipping';
    $flat_rate->instance_settings['cost'] = '9.99';
    $flat_rate->save();
    
    // Add Free Shipping (minimum $100)
    $zone->add_shipping_method('free_shipping');
    $methods = $zone->get_shipping_methods();
    $free_shipping = end($methods);
    $free_shipping->instance_settings['title'] = 'Free Shipping';
    $free_shipping->instance_settings['requires'] = 'min_amount';
    $free_shipping->instance_settings['min_amount'] = '100';
    $free_shipping->save();
    
    // Add Local Pickup
    $zone->add_shipping_method('local_pickup');
    $methods = $zone->get_shipping_methods();
    $local_pickup = end($methods);
    $local_pickup->instance_settings['title'] = 'Local Pickup';
    $local_pickup->instance_settings['cost'] = '0';
    $local_pickup->save();
});
```

**Verification:** Visit WooCommerce → Settings → Shipping. Verify zone exists with correct locations and methods.

---

## Section 4: WooCommerce Payment Gateway Configuration

### 4.1 Read Payment Gateways via REST API

```bash
# List all payment gateways
curl -X GET \
  "https://example.com/wp-json/wc/v3/payment_gateways" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json"
```

### 4.2 Enable and Configure Payment Gateways

```bash
# Enable Direct Bank Transfer
curl -X POST \
  "https://example.com/wp-json/wc/v3/payment_gateways/bacs" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": true,
    "title": "Bank Transfer",
    "description": "Make your payment directly into our bank account.",
    "settings": {
      "title": "Bank Transfer",
      "description": "Make your payment directly into our bank account."
    }
  }'

# Enable Cash on Delivery
curl -X POST \
  "https://example.com/wp-json/wc/v3/payment_gateways/cod" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": true,
    "title": "Cash on Delivery",
    "description": "Pay with cash upon delivery."
  }'

# Enable Stripe (requires API keys)
curl -X POST \
  "https://example.com/wp-json/wc/v3/payment_gateways/stripe" \
  -u "consumer_key:consumer_secret" \
  -H "Content-Type: application/json" \
  -d '{
    "enabled": true,
    "title": "Credit Card (Stripe)",
    "description": "Pay securely with your credit card.",
    "settings": {
      "title": "Credit Card",
      "testmode": false,
      "publishable_key": "pk_live_XXXXX",
      "secret_key": "sk_live_XXXXX"
    }
  }'
```

### 4.3 Configure Bank Transfer Account Details

```php
// One-time snippet: configure BACS account details
add_action('init', function() {
    $account_details = array(
        array(
            'account_name'     => 'My Store LLC',
            'account_number'   => '1234567890',
            'sort_code'        => '12-34-56',
            'bank_name'        => 'First National Bank',
            'iban'             => 'US12 3456 7890 1234 5678 90',
            'bic'              => 'FNBAUS12',
        ),
    );
    
    $bacs_settings = get_option('woocommerce_bacs_settings', array());
    $bacs_settings['account_details'] = $account_details;
    $bacs_settings['enabled'] = 'yes';
    $bacs_settings['title'] = 'Bank Transfer';
    $bacs_settings['description'] = 'Make your payment directly into our bank account. Please use your Order ID as the payment reference.';
    $bacs_settings['instructions'] = 'Make your payment directly into our bank account. Please use your Order ID as the payment reference.';
    
    update_option('woocommerce_bacs_settings', $bacs_settings);
});
```

**Verification:** Add a product to cart, go to checkout, verify payment methods appear with correct titles and descriptions.

---

## Section 5: Elementor Configuration

### 5.1 Configure Elementor Settings via Code Snippets

```php
// One-time snippet: configure Elementor settings
add_action('init', function() {
    // Enable Elementor for pages and posts
    update_option('elementor_cpt_supports', array('page', 'post', 'product'));
    
    // Disable default color schemes (use theme colors)
    update_option('elementor_disable_color_schemes', 'yes');
    
    // Disable default typography schemes (use theme fonts)
    update_option('elementor_disable_typography_schemes', 'yes');
    
    // Set CSS print method to external
    update_option('elementor_css_print_method', 'external');
    
    // Enable Google Fonts
    update_option('elementor_google_fonts', 'yes');
    
    // Container width
    update_option('elementor_container_width', array('unit' => 'px', 'size' => 1200));
    
    // Widget spacing
    update_option('elementor_space_between_widgets', array('unit' => 'px', 'size' => 20));
    
    // Enable Flexbox Container experiment
    update_option('elementor_experiment-flexbox_container', 'active');
    
    // Enable optimized CSS loading
    update_option('elementor_experiment-e_optimized_css_loading', 'active');
    
    // Enable optimized JS loading
    update_option('elementor_experiment-e_optimized_js_loading', 'active');
    
    // Enable lazy load background images
    update_option('elementor_experiment-e_lazyload', 'active');
    
    // Enable inline font icons (SVG)
    update_option('elementor_experiment-e_font_icon_svg', 'active');
    
    // Enable optimized DOM
    update_option('elementor_experiment-e_dom_optimization', 'active');
    
    // Enable improved image loading
    update_option('elementor_experiment-e_image_loading_optimization', 'active');
    
    // Flush Elementor CSS
    if (class_exists('\Elementor\Plugin')) {
        \Elementor\Plugin::$instance->files_manager->clear_cache();
    }
});
```

**Verification:** Visit Elementor → Settings. Check all options match. Visit a page with Elementor — check no console errors.

### 5.2 Set Elementor Canvas for Specific Pages (DEAD RULE — MANDATORY)

**This is a DEAD RULE. Every custom page MUST have Elementor Canvas set.** See `elementor-html-automation.md` "DEAD RULE: Elementor Canvas Is Mandatory" for the complete enforcement procedure. This Code Snippets PHP snippet provides a programmatic way to set Canvas, but the agent MUST still verify in the Elementor UI and on the front-end.

```php
// One-time snippet: set Elementor Canvas for ALL custom pages (DEAD RULE)
add_action('init', function() {
    // Include ALL custom pages — add more slugs as needed
    $canvas_pages = array('home', 'about', 'contact', 'faq', 'blog', 'shipping-policy', 'return-policy', 'privacy-policy', 'terms-of-service', 'cookie-policy', 'payment-policy', 'age-verification', 'wholesale');
    
    foreach ($canvas_pages as $slug) {
        $page = get_page_by_path($slug);
        if ($page) {
            update_post_meta($page->ID, '_wp_page_template', 'elementor_canvas');
            update_post_meta($page->ID, '_elementor_template_type', 'wp-page');
            update_post_meta($page->ID, '_elementor_edit_mode', 'builder');
        }
    }
});
```

**Verification:** Edit each page in Elementor. Check Page Settings → Page Layout shows "Elementor Canvas". Reload each page on the front-end — verify NO theme header/footer/menu appears. If theme chrome still appears, Canvas was not set correctly. See `elementor-html-automation.md` "Canvas Verification Gate" for the complete verification procedure.

**Do NOT set Canvas on WooCommerce-owned pages**: Shop, Cart, Checkout, My Account, product archives, single product pages.

### 5.3 Configure Elementor Site Settings via Code Snippets

```php
// One-time snippet: configure Elementor global colors and fonts
add_action('init', function() {
    // Global Colors
    $colors = array(
        'primary'    => '#667eea',
        'secondary'  => '#764ba2',
        'text'       => '#2d3748',
        'accent'     => '#ed8936',
        'custom_1'   => '#2d3748',
        'custom_2'   => '#718096',
        'custom_3'   => '#e2e8f0',
        'custom_4'   => '#edf2f7',
    );
    update_option('elementor_scheme_color', $colors);
    update_option('elementor_scheme_color-picker', array_merge(array_values($colors), array('#ffffff', '#000000')));
    
    // Global Fonts
    $typography = array(
        'primary' => array(
            'font_family' => 'Inter',
            'font_weight' => '600',
        ),
        'secondary' => array(
            'font_family' => 'Inter',
            'font_weight' => '400',
        ),
        'text' => array(
            'font_family' => 'Inter',
            'font_weight' => '400',
        ),
        'accent' => array(
            'font_family' => 'Inter',
            'font_weight' => '700',
        ),
    );
    update_option('elementor_scheme_typography', $typography);
    
    // Flush Elementor cache
    if (class_exists('\Elementor\Plugin')) {
        \Elementor\Plugin::$instance->files_manager->clear_cache();
    }
});
```

---

## Section 6: Rank Math SEO Configuration

### 6.1 Configure Rank Math via Code Snippets

```php
// One-time snippet: configure Rank Math SEO settings
add_action('init', function() {
    if (!class_exists('RankMath')) return;
    
    $settings = RankMath\Helper::get_settings('all');
    
    // General settings
    update_option('rank-math-options-general', array_merge($settings->general, array(
        'breadcrumbs'                => 'on',
        'attachment_redirect_urls'   => 'on',
        'attachment_redirect_default' => home_url('/'),
        'strip_category_base'        => 'on',
        'nofollow_external_links'    => 'on',
        'new_window_external_links'  => 'on',
        'nofollow_image_links'       => '',
        'new_window_image_links'     => '',
        'image_seo_add_alt'          => 'on',
        'image_seo_add_title'        => '',
    )));
    
    // Titles & Meta
    update_option('rank-math-options-titles', array(
        // Homepage
        'homepage_title'       => '%sitename% %page% %sep% %sitedesc%',
        'homepage_description' => '%sitedesc%',
        'homepage_custom_robots' => 'on',
        'homepage_robots'      => array('index'),
        
        // Posts
        'pt_post_title'        => '%title% %sep% %sitename%',
        'pt_post_description'  => '%excerpt%',
        'pt_post_custom_robots' => 'on',
        'pt_post_robots'       => array('index', 'follow'),
        
        // Pages
        'pt_page_title'        => '%title% %sep% %sitename%',
        'pt_page_description'  => '%excerpt%',
        'pt_page_custom_robots' => 'on',
        'pt_page_robots'       => array('index', 'follow'),
        
        // Products
        'pt_product_title'        => '%title% %sep% %sitename%',
        'pt_product_description'  => '%excerpt%',
        'pt_product_custom_robots' => 'on',
        'pt_product_robots'       => array('index', 'follow'),
        
        // Product categories
        'tax_product_cat_title'        => '%term% %sep% %sitename%',
        'tax_product_cat_description'  => '%term_description%',
        'tax_product_cat_custom_robots' => 'on',
        'tax_product_cat_robots'       => array('index', 'follow'),
        
        // Blog post archives
        'author_archive_title'   => 'Articles by %author% %sep% %sitename%',
        'author_archive_robots'  => array('noindex'),
        'date_archive_title'     => '%date% %sep% %sitename%',
        'date_archive_robots'    => array('noindex'),
        'search_archive_title'   => '%search_query% %sep% %sitename%',
        'search_archive_robots'  => array('noindex'),
        
        // Cart, Checkout, My Account
        'pt_product_robots' => array('index', 'follow'),
    ));
    
    // Sitemap
    update_option('rank-math-options-sitemap', array(
        'items_per_page'     => 200,
        'include_images'     => 'on',
        'include_featured_image' => 'on',
        'exclude_post_types' => array(),
        'exclude_taxonomies' => array(),
    ));
    
    // Schema
    update_option('rank-math-options-titles', array_merge(get_option('rank-math-options-titles', array()), array(
        'product_default_rich_snippet' => 'product',
        'product_snippet_brand'       => '%seo_title%',
        'product_snippet_sku'         => '%sku%',
        'product_snippet_price'       => '%price%',
        'product_snippet_availability' => '%availability%',
    )));
    
    // Flush Rank Math cache
    delete_transient('rank_math_redirections_cached');
});
```

**Verification:** Visit Rank Math → General Settings, Titles & Meta, Sitemap Settings, Schema. Verify all settings match.

### 6.2 Set Noindex for WooCommerce Pages

```php
// One-time snippet: set noindex for cart, checkout, my account
add_action('template_redirect', function() {
    if (function_exists('is_woocommerce')) {
        if (is_cart() || is_checkout() || is_account_page()) {
            add_filter('rank_math/frontend/robots', function($robots) {
                $robots['index'] = false;
                return $robots;
            });
        }
    }
});
```

---

## Section 7: WordPress Menu Creation via REST API

### 7.1 Create Menu via REST API

```bash
# Create a navigation menu
curl -X POST \
  "https://example.com/wp-json/wp/v2/menus" \
  -H "Authorization: Basic $(echo -n 'admin:xxxx xxxx xxxx xxxx xxxx' | base64)" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Primary Menu",
    "slug": "primary",
    "location": "menu-1"
  }'
```

### 7.2 Add Menu Items via REST API

```bash
# Add a page menu item (replace MENU_ID with actual ID)
curl -X POST \
  "https://example.com/wp-json/wp/v2/menu-items" \
  -H "Authorization: Basic $(echo -n 'admin:xxxx xxxx xxxx xxxx xxxx' | base64)" \
  -H "Content-Type: application/json" \
  -d '{
    "menus": MENU_ID,
    "title": "Home",
    "url": "/",
    "status": "publish",
    "object": "page",
    "object_id": 5,
    "menus_order": 1
  }'

# Add a custom link menu item
curl -X POST \
  "https://example.com/wp-json/wp/v2/menu-items" \
  -H "Authorization: Basic $(echo -n 'admin:xxxx xxxx xxxx xxxx xxxx' | base64)" \
  -H "Content-Type: application/json" \
  -d '{
    "menus": MENU_ID,
    "title": "Shop",
    "url": "/shop/",
    "status": "publish",
    "object": "page",
    "object_id": 10,
    "menus_order": 2
  }'
```

### 7.3 Create Menus via Code Snippets PHP

```php
// One-time snippet: create and populate WordPress menus
add_action('init', function() {
    // Get menu locations
    $locations = get_registered_nav_menus();
    
    // Create Primary Menu
    $primary_menu_name = 'Primary Menu';
    $primary_menu = wp_get_nav_menu_object($primary_menu_name);
    
    if (!$primary_menu) {
        $primary_menu_id = wp_create_nav_menu($primary_menu_name);
    } else {
        $primary_menu_id = $primary_menu->term_id;
    }
    
    // Clear existing items
    $existing_items = wp_get_nav_menu_items($primary_menu_id);
    if ($existing_items) {
        foreach ($existing_items as $item) {
            wp_delete_post($item->ID, true);
        }
    }
    
    // Define menu items
    $menu_items = array(
        'home'      => array('title' => 'Home', 'url' => home_url('/')),
        'shop'      => array('title' => 'Shop', 'url' => get_permalink(wc_get_page_id('shop'))),
        'blog'      => array('title' => 'Blog', 'url' => get_permalink(get_option('page_for_posts'))),
        'about'     => array('title' => 'About', 'url' => home_url('/about/')),
        'faq'       => array('title' => 'FAQ', 'url' => home_url('/faq/')),
        'contact'   => array('title' => 'Contact', 'url' => home_url('/contact/')),
    );
    
    $order = 1;
    foreach ($menu_items as $slug => $item) {
        // Find the page
        $page = get_page_by_path($slug);
        $object_id = $page ? $page->ID : 0;
        
        wp_update_nav_menu_item($primary_menu_id, 0, array(
            'menu-item-title'     => $item['title'],
            'menu-item-url'       => $item['url'],
            'menu-item-status'    => 'publish',
            'menu-item-object'    => $object_id ? 'page' : 'custom',
            'menu-item-object-id' => $object_id,
            'menu-item-type'      => $object_id ? 'post_type' : 'custom',
            'menu-item-position'  => $order,
        ));
        $order++;
    }
    
    // Assign to menu location
    $locations = get_theme_mod('nav_menu_locations');
    $locations['menu-1'] = $primary_menu_id;
    set_theme_mod('nav_menu_locations', $locations);
    
    // Create Footer Menu
    $footer_menu_name = 'Footer Menu';
    $footer_menu = wp_get_nav_menu_object($footer_menu_name);
    
    if (!$footer_menu) {
        $footer_menu_id = wp_create_nav_menu($footer_menu_name);
    } else {
        $footer_menu_id = $footer_menu->term_id;
    }
    
    // Clear existing items
    $existing_items = wp_get_nav_menu_items($footer_menu_id);
    if ($existing_items) {
        foreach ($existing_items as $item) {
            wp_delete_post($item->ID, true);
        }
    }
    
    // Footer menu items
    $footer_items = array(
        'shipping-policy'  => 'Shipping Policy',
        'return-policy'    => 'Return Policy',
        'payment-policy'   => 'Payment Policy',
        'privacy-policy'   => 'Privacy Policy',
        'terms-and-conditions' => 'Terms of Service',
        'cookie-policy'    => 'Cookie Policy',
        'faq'              => 'FAQ',
        'contact'          => 'Contact',
    );
    
    $order = 1;
    foreach ($footer_items as $slug => $title) {
        $page = get_page_by_path($slug);
        $url = $page ? get_permalink($page->ID) : home_url('/' . $slug . '/');
        $object_id = $page ? $page->ID : 0;
        
        wp_update_nav_menu_item($footer_menu_id, 0, array(
            'menu-item-title'     => $title,
            'menu-item-url'       => $url,
            'menu-item-status'    => 'publish',
            'menu-item-object'    => $object_id ? 'page' : 'custom',
            'menu-item-object-id' => $object_id,
            'menu-item-type'      => $object_id ? 'post_type' : 'custom',
            'menu-item-position'  => $order,
        ));
        $order++;
    }
    
    // Assign footer menu to location
    $locations['menu-2'] = $footer_menu_id;
    set_theme_mod('nav_menu_locations', $locations);
});
```

**Verification:** Visit Appearance → Menus. Check both menus exist with correct items. Visit front-end — verify header menu and footer menu render correctly with working links.

---

## Section 8: wp-config.php Configuration

### 8.1 Essential wp-config.php Additions

Add these to `wp-config.php` (before `/* That's all, stop editing! */`):

```php
// Increase PHP memory limit
define('WP_MEMORY_LIMIT', '512M');
define('WP_MAX_MEMORY_LIMIT', '512M');

// Disable post revisions (or limit them)
define('WP_POST_REVISIONS', 5);

// Disable trash auto-empty (or set days)
define('EMPTY_TRASH_DAYS', 30);

// Auto-save interval (seconds)
define('AUTOSAVE_INTERVAL', 300);

// Disable file editing in admin
define('DISALLOW_FILE_EDIT', true);

// Force SSL for admin and login
define('FORCE_SSL_ADMIN', true);

// Set WordPress debug to log only
define('WP_DEBUG', false);
define('WP_DEBUG_LOG', true);
define('WP_DEBUG_DISPLAY', false);

// Disable WordPress cron (use server cron instead)
// define('DISABLE_WP_CRON', true);

// Limit revisions for WooCommerce
define('WC()->api_request_url', false); // Prevents some API-based cron
```

### 8.2 Database Repair Mode (Emergency)

```php
// Add temporarily to wp-config.php, visit /wp-admin/maint/repair.php, then REMOVE
define('WP_ALLOW_REPAIR', true);
```

---

## Section 9: .htaccess Configuration

### 9.1 Security Headers

```apache
# Add to .htaccess (Apache only)
<IfModule mod_headers.c>
    # Security headers
    Header set X-Content-Type-Options "nosniff"
    Header set X-Frame-Options "SAMEORIGIN"
    Header set X-XSS-Protection "1; mode=block"
    Header set Referrer-Policy "strict-origin-when-cross-origin"
    Header set Permissions-Policy "geolocation=(), microphone=(), camera=()"
    
    # HSTS (only if site is fully HTTPS)
    Header set Strict-Transport-Security "max-age=31536000; includeSubDomains" env=HTTPS
</IfModule>
```

### 9.2 Gzip Compression

```apache
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE text/html text/plain text/css text/javascript
    AddOutputFilterByType DEFLATE application/javascript application/x-javascript
    AddOutputFilterByType DEFLATE application/json application/xml application/rss+xml
    AddOutputFilterByType DEFLATE image/svg+xml font/woff font/woff2 application/font-woff
</IfModule>
```

### 9.3 Browser Caching

```apache
<IfModule mod_expires.c>
    ExpiresActive On
    ExpiresByType image/jpeg "access plus 1 year"
    ExpiresByType image/png "access plus 1 year"
    ExpiresByType image/webp "access plus 1 year"
    ExpiresByType image/svg+xml "access plus 1 year"
    ExpiresByType text/css "access plus 1 month"
    ExpiresByType application/javascript "access plus 1 month"
    ExpiresByType text/javascript "access plus 1 month"
    ExpiresByType font/woff "access plus 1 year"
    ExpiresByType font/woff2 "access plus 1 year"
    ExpiresByType application/pdf "access plus 1 month"
</IfModule>
```

### 9.4 Protect Sensitive Files

```apache
# Protect wp-config.php
<Files wp-config.php>
    Order Allow,Deny
    Deny from all
</Files>

# Protect .htaccess itself
<Files .htaccess>
    Order Allow,Deny
    Deny from all
</Files>

# Protect xmlrpc.php (if not needed)
<Files xmlrpc.php>
    Order Allow,Deny
    Deny from all
</Files>

# Block PHP execution in uploads
<Files *.php>
    Order Allow,Deny
    Deny from all
</Files>
# Place this in wp-content/uploads/.htaccess
```

---

## Verification Checklist for All Settings

After configuring any settings via the methods in this guide, verify:

- [ ] No PHP errors in error log after configuration change
- [ ] Front-end pages load correctly (no white screen, no 500 error)
- [ ] WordPress admin accessible without errors
- [ ] WooCommerce pages (Shop, Cart, Checkout, My Account) all work
- [ ] Checkout flow works up to payment boundary
- [ ] Permalinks work correctly (no 404 on posts/pages)
- [ ] Menu links navigate to correct pages
- [ ] Elementor editor opens without errors
- [ ] Rank Math dashboard shows configured settings
- [ ] Sitemap accessible at `/sitemap_index.xml`
- [ ] robots.txt blocks cart/checkout/my-account
- [ ] Email sending works (test order email)
- [ ] Cache purged after all configuration changes
- [ ] SiteGround SG Optimizer cache purged (if applicable)
- [ ] Mobile layout not broken
- [ ] No console errors in browser
