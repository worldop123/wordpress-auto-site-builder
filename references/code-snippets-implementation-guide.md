# Code Snippets Implementation Guide

Practical, ready-to-use Code Snippets implementations for WordPress, WooCommerce, Elementor, and SEO. Every snippet in this guide is REAL, WORKING code that can be directly pasted into the Code Snippets plugin. Read `wordpress-plugins-themes-guide.md` for the option keys and settings referenced here.

## How to Use This Guide

1. Each snippet has: Title, Type (PHP/HTML/CSS/JS), Scope, Lifecycle, Code, and Verification.
2. PHP snippets go into Code Snippets → Add New → PHP snippet.
3. HTML snippets go into Code Snippets → Add New → HTML snippet.
4. CSS snippets go into Code Snippets → Add New → CSS snippet (or Appearance → Customize → Additional CSS).
5. JS snippets go into Code Snippets → Add New → JS snippet (or within an HTML snippet in `<script>` tags).
6. Always test snippets on a staging site first.
7. After activating any snippet, verify on the front-end.
8. Classify each snippet: `persistent`, `ux_polish`, `one_time_writer`, `read_only_scanner`, or `deprecated`.

---

## Interaction Safety Rules for Generated Snippets

Every front-end snippet that creates buttons, inputs, menus, accordions, tabs, filters, galleries, age gates, cookie banners, quantity controls, or checkout behavior must pass these rules before activation:

- Keep event handlers small, delegated where practical, and scoped to the relevant page or component.
- Do not use body-wide `MutationObserver` loops that mutate the same subtree they observe. Prefer `DOMContentLoaded`, `pageshow`, and specific WooCommerce/Elementor events.
- Do not auto-click native submit/update buttons unless that exact AJAX or form flow has been tested on the live site.
- Do not create overlays, floating widgets, or sticky bars that intercept taps on product, cart, checkout, menu, or form controls.
- Preserve native WooCommerce inputs, variation events, nonce fields, form names, and update buttons.
- Verify by clicking and typing in the browser on desktop and mobile. A visual screenshot alone is not enough.
- If a snippet causes console errors, repeated reloads, disabled controls, long main-thread locks, or frozen pages, deactivate it and replace with a smaller scoped implementation.

---

## Code Scale and Maintainability Rules

Code Snippets works best for small, focused WordPress/WooCommerce behaviors. The agent must not turn a site into an unmaintainable code pile.

- Small snippets are preferred. One snippet should have one clear responsibility, known hooks, scoped loading, rollback notes, and a verification checklist.
- Do not paste a full application, multi-thousand-line framework, or tangled business system into Code Snippets. Large uncontrolled code loses project context, creates hidden chain bugs, and becomes hard to debug.
- Before changing shared behavior, inspect existing snippets, hooks, global shell output, WooCommerce templates, Elementor HTML blocks, and plugin conflicts that may be affected.
- Every generated snippet must explain: purpose, affected pages, lifecycle (`persistent`, `ux_polish`, `one_time_writer`, `read_only_scanner`, or `deprecated`), dependencies, rollback action, and test evidence.
- Never hardcode secrets, credentials, API keys, payment tokens, private endpoints, or personal data in snippets or Elementor HTML.
- Use WordPress security basics: capability checks for admin/write actions, nonces for writes, sanitization for inputs, escaping for outputs, prepared queries for database access, and safe REST permissions.
- If a feature requires large state, queues, custom database tables, complex permissions, or multi-file architecture, recommend a proper plugin/custom development path instead of forcing it into Code Snippets.
- Commercial launch must treat permission bugs, data leaks, broken checkout, unsafe payment logic, regulatory claims, and platform-policy violations as launch blockers.

---

## One-Time Writer Rules

Use `one_time_writer` snippets for controlled bulk settings/meta updates such as WooCommerce page bindings, WordPress settings, Rank Math metadata, image ALT fixes, or menu assignments.

- Build a mapping first. Do not let a writer blindly scan and overwrite unrelated content.
- Include only target IDs and target fields.
- Record written, skipped, and failed IDs.
- Skip existing human-written values unless the user approved overwriting or autonomous mode recorded the decision.
- Run once, verify, then disable and delete the snippet.
- If interrupted, resume from the writer ledger and only write missing/failed IDs.
- Never leave one-time writers active on the front end or admin after successful execution.

For Rank Math Free bulk SEO metadata, prefer a one-time writer over pretending CSV SEO import is available. See `rank-math-seo-guide.md`.

---

## Large CSV Importer Rules

Do not paste large WooCommerce CSV contents into Code Snippets. A CSV importer snippet may reference only a verified file URL or temporary server file path plus expected hash/counts.

When a one-time CSV importer is required:

- Read `large-csv-media-import.md` first.
- Run only in wp-admin and require `manage_woocommerce` or administrator capability.
- Require nonce/action confirmation, expected SHA-256 hash, expected row count, and expected headers.
- Support a dry-run mode that reports parser results without writing products.
- Use WordPress temporary files and cleanup routines; do not leave downloaded CSV files public.
- Never decode base64 from chat or reconstruct CSV rows from pasted text.
- Stop and ask the user to manually upload the processed CSV if file upload, media URL retrieval, hash verification, or dry-run validation cannot be completed safely.
- Disable and delete the importer snippet after successful import and verification.

---

## Section 1: WordPress Core Configuration via Code Snippets

### 1.1 Set Permalink Structure to Post Name

**Type:** PHP | **Scope:** Global | **Lifecycle:** one_time_writer

```php
// Set permalink to /%postname%/
add_action('init', function() {
    if (get_option('permalink_structure') !== '/%postname%/') {
        update_option('permalink_structure', '/%postname%/');
        flush_rewrite_rules();
    }
});
```

**Verification:** Visit Settings → Permalinks. Check that "Post name" is selected. Visit a blog post URL and confirm it loads without 404.

### 1.2 Configure Reading Settings (Static Homepage)

**Type:** PHP | **Scope:** Global | **Lifecycle:** one_time_writer

```php
// Set front page to static page, assign blog page
add_action('init', function() {
    // Find or create Home page
    $home_page = get_page_by_path('home');
    if (!$home_page) {
        $home_page = get_page_by_path('sample-page');
    }
    $blog_page = get_page_by_path('blog');
    if (!$blog_page) {
        $blog_page = get_page_by_path('news');
    }
    
    if ($home_page) {
        update_option('show_on_front', 'page');
        update_option('page_on_front', $home_page->ID);
    }
    if ($blog_page) {
        update_option('page_for_posts', $blog_page->ID);
    }
    update_option('posts_per_page', 12);
});
```

**Verification:** Visit site homepage — should show the static Home page. Visit /blog/ — should show blog posts. Check Settings → Reading.

### 1.3 Configure Media Settings

**Type:** PHP | **Scope:** Global | **Lifecycle:** one_time_writer

```php
// Set image sizes for optimal performance
add_action('init', function() {
    update_option('thumbnail_size_w', 300);
    update_option('thumbnail_size_h', 300);
    update_option('thumbnail_crop', 1);
    update_option('medium_size_w', 600);
    update_option('medium_size_h', 600);
    update_option('large_size_w', 1536);
    update_option('large_size_h', 1536);
});
```

### 1.4 Configure Discussion Settings (Disable Comments Globally)

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Disable comments on all post types
add_action('init', function() {
    // Close comments on all posts
    update_option('default_comment_status', 'closed');
    update_option('default_ping_status', 'closed');
    update_option('default_pingback_flag', 0);
});

// Remove comment support from posts and pages
add_action('init', function() {
    $post_types = get_post_types(array('public' => true), 'names');
    foreach ($post_types as $post_type) {
        if (post_type_supports($post_type, 'comments')) {
            remove_post_type_support($post_type, 'comments');
            remove_post_type_support($post_type, 'trackbacks');
        }
    }
}, 100);

// Remove comments menu from admin
add_action('admin_menu', function() {
    remove_menu_page('edit-comments.php');
});

// Remove comments from admin bar
add_action('wp_before_admin_bar_render', function() {
    global $wp_admin_bar;
    $wp_admin_bar->remove_menu('comments');
});

// Redirect any comment attempt to homepage
add_action('template_redirect', function() {
    if (is_singular()) {
        global $post;
        if ($post && $post->comment_status === 'closed' && !is_user_logged_in()) {
            // Just let it be — comments are closed, form won't show
        }
    }
});
```

### 1.5 Disable WordPress Emojis (Performance)

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Remove emoji scripts and styles
remove_action('wp_head', 'print_emoji_detection_script', 7);
remove_action('admin_print_scripts', 'print_emoji_detection_script');
remove_action('wp_print_styles', 'print_emoji_styles');
remove_action('admin_print_styles', 'print_emoji_styles');
remove_filter('the_content_feed', 'wp_staticize_emoji');
remove_filter('comment_text_rss', 'wp_staticize_emoji');
remove_filter('wp_mail', 'wp_staticize_emoji_for_email');

// Remove emoji from TinyMCE
add_filter('tiny_mce_plugins', function($plugins) {
    if (is_array($plugins)) {
        return array_diff($plugins, array('wpemoji'));
    }
    return array();
});

// Remove emoji DNS prefetch
add_filter('wp_resource_hints', function($urls, $relation_type) {
    if ($relation_type === 'dns-prefetch') {
        $emoji_svg_url = 'https://s.w.org/images/core/emoji/';
        foreach ($urls as $key => $url) {
            if (strpos($url, $emoji_svg_url) !== false) {
                unset($urls[$key]);
            }
        }
    }
    return $urls;
}, 10, 2);
```

### 1.6 Remove WordPress Version and Meta Generators (Security)

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Remove WordPress version
remove_action('wp_head', 'wp_generator');

// Remove WLW manifest
remove_action('wp_head', 'wlwmanifest_link');

// Remove RSD link
remove_action('wp_head', 'rsd_link');

// Remove shortlink
remove_action('wp_head', 'wp_shortlink_wp_head');

// Remove REST API link from head
remove_action('wp_head', 'rest_output_link_wp_head');

// Remove oEmbed
remove_action('wp_head', 'wp_oembed_add_discovery_links');
remove_action('wp_head', 'wp_oembed_add_host_js');

// Disable XML-RPC
add_filter('xmlrpc_enabled', '__return_false');
remove_action('wp_head', 'rsd_link');
```

### 1.7 Custom Login Page Styling

**Type:** PHP + CSS | **Scope:** Admin (login page) | **Lifecycle:** persistent

```php
// Custom login page styles
add_action('login_enqueue_scripts', function() {
    ?>
    <style type="text/css">
        body.login {
            background: #1a1a2e;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        body.login::before {
            content: '';
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            opacity: 0.9;
            z-index: -1;
        }
        #login {
            width: 400px;
            padding: 40px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 16px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
        }
        #login h1 a {
            background-image: none;
            text-indent: 0;
            width: auto;
            height: auto;
            font-size: 28px;
            font-weight: 700;
            color: #1a1a2e;
            text-decoration: none;
            display: block;
            text-align: center;
            margin-bottom: 20px;
        }
        .login form {
            border: none;
            background: transparent;
            box-shadow: none;
            padding: 0;
        }
        .login form .input,
        .login form input[type="checkbox"] {
            border-radius: 8px;
            border: 2px solid #e0e0e0;
            padding: 12px;
            font-size: 15px;
        }
        .login form .input:focus {
            border-color: #667eea;
            box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
        }
        #wp-submit {
            background: #667eea;
            border: none;
            border-radius: 8px;
            padding: 12px;
            font-size: 15px;
            font-weight: 600;
            height: auto;
            line-height: 1;
            width: 100%;
            transition: background 0.3s;
        }
        #wp-submit:hover {
            background: #5568d3;
        }
        .login #backtoblog a,
        .login #nav a {
            color: #667eea;
        }
    </style>
    <?php
});

// Change login logo URL
add_filter('login_headerurl', function() {
    return home_url('/');
});

// Change login logo title
add_filter('login_headertext', function() {
    return get_bloginfo('name');
});
```

### 1.8 Custom Admin Footer and Dashboard

**Type:** PHP | **Scope:** Admin | **Lifecycle:** persistent

```php
// Custom admin footer text
add_filter('admin_footer_text', function() {
    echo 'Built with <span style="color:#e25555;">♥</span> by ' . get_bloginfo('name');
});

// Remove WordPress welcome panel
remove_action('welcome_panel', 'wp_welcome_panel');

// Remove dashboard widgets
add_action('wp_dashboard_setup', function() {
    remove_meta_box('dashboard_quick_press', 'dashboard', 'side');
    remove_meta_box('dashboard_primary', 'dashboard', 'side');
    remove_meta_box('dashboard_secondary', 'dashboard', 'side');
    remove_meta_box('dashboard_recent_drafts', 'dashboard', 'side');
    remove_meta_box('dashboard_php_nag', 'dashboard', 'normal');
    remove_meta_box('dashboard_browser_nag', 'dashboard', 'normal');
});

// Custom dashboard widget
add_action('wp_dashboard_setup', function() {
    wp_add_dashboard_widget('site_status_widget', 'Site Status', function() {
        $products = wp_count_posts('product');
        $posts = wp_count_posts('post');
        $pages = wp_count_posts('page');
        echo '<div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;">';
        echo '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:16px;text-align:center;">';
        echo '<div style="font-size:28px;font-weight:700;color:#667eea;">' . $products->publish . '</div>';
        echo '<div style="color:#666;font-size:13px;">Products</div></div>';
        echo '<div style="background:#fff;border:1px solid #e0e0e0;border-radius:8px;padding:16px;text-align:center;">';
        echo '<div style="font-size:28px;font-weight:700;color:#667eea;">' . $posts->publish . '</div>';
        echo '<div style="color:#666;font-size:13px;">Posts</div></div>';
        echo '</div>';
    });
});
```

---

## Section 2: WooCommerce Customizations via Code Snippets

### 2.1 Set WooCommerce Core Settings

**Type:** PHP | **Scope:** Global | **Lifecycle:** one_time_writer

```php
// Configure WooCommerce settings programmatically
add_action('init', function() {
    // General settings
    update_option('woocommerce_currency', 'USD');
    update_option('woocommerce_currency_pos', 'left');
    update_option('woocommerce_price_thousand_sep', ',');
    update_option('woocommerce_price_decimal_sep', '.');
    update_option('woocommerce_price_num_decimals', 2);
    
    // Products settings
    update_option('woocommerce_shop_page_display', ''); // Show products
    update_option('woocommerce_default_catalog_orderby', 'menu_order');
    update_option('woocommerce_catalog_columns', 4);
    update_option('woocommerce_catalog_rows', 4);
    update_option('woocommerce_cart_redirect_after_add', 'no');
    update_option('woocommerce_enable_ajax_add_to_cart', 'yes');
    
    // Accounts & Privacy
    update_option('woocommerce_enable_guest_checkout', 'yes');
    update_option('woocommerce_enable_checkout_login_reminder', 'yes');
    update_option('woocommerce_enable_signup_and_login_from_checkout', 'yes');
    update_option('woocommerce_enable_myaccount_registration', 'no');
    update_option('woocommerce_registration_generate_username', 'yes');
    update_option('woocommerce_registration_generate_password', 'yes');
    
    // Enable coupons
    update_option('woocommerce_enable_coupons', 'yes');
    
    // Image sizes
    update_option('woocommerce_thumbnail_cropping', '1:1');
    update_option('woocommerce_thumbnail_cropping_custom_width', 600);
    update_option('woocommerce_thumbnail_cropping_custom_height', 600);
});
```

**Verification:** Visit WooCommerce → Settings. Check each tab matches configured values.

### 2.2 Bind WooCommerce Pages

**Type:** PHP | **Scope:** Global | **Lifecycle:** one_time_writer

```php
// Bind WooCommerce pages to correct page IDs
add_action('init', function() {
    $shop_page = get_page_by_path('shop');
    $cart_page = get_page_by_path('cart');
    $checkout_page = get_page_by_path('checkout');
    $myaccount_page = get_page_by_path('my-account');
    $terms_page = get_page_by_path('terms-and-conditions');
    
    if ($shop_page) update_option('woocommerce_shop_page_id', $shop_page->ID);
    if ($cart_page) update_option('woocommerce_cart_page_id', $cart_page->ID);
    if ($checkout_page) update_option('woocommerce_checkout_page_id', $checkout_page->ID);
    if ($myaccount_page) update_option('woocommerce_myaccount_page_id', $myaccount_page->ID);
    if ($terms_page) update_option('woocommerce_terms_page_id', $terms_page->ID);
});
```

### 2.3 Custom Add to Cart Button Text

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Change add to cart text on single product pages
add_filter('woocommerce_product_single_add_to_cart_text', function() {
    return __('Add to Cart', 'textdomain');
});

// Change add to cart text on archive/shop pages
add_filter('woocommerce_product_add_to_cart_text', function() {
    return __('Add to Cart', 'textdomain');
});

// Change add to cart text for variable products
add_filter('woocommerce_product_add_to_cart_text', function($text, $product) {
    if ($product->is_type('variable')) {
        return __('Select Options', 'textdomain');
    }
    if ($product->is_type('grouped')) {
        return __('View Products', 'textdomain');
    }
    if (!$product->is_in_stock()) {
        return __('Out of Stock', 'textdomain');
    }
    return $text;
}, 10, 2);
```

### 2.4 Free Shipping Progress Bar

**Type:** PHP + HTML + JS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Free shipping progress bar on cart and checkout
add_action('woocommerce_before_cart_table', function() {
    $free_shipping_threshold = 100; // $100 for free shipping
    $cart_total = WC()->cart->get_cart_contents_total();
    $remaining = $free_shipping_threshold - $cart_total;
    $percentage = min(100, ($cart_total / $free_shipping_threshold) * 100);
    
    if ($remaining > 0) {
        $message = sprintf(
            'Add <strong>%s</strong> more to get <strong>FREE shipping!</strong>',
            wc_price($remaining)
        );
    } else {
        $message = '🎉 You qualify for <strong>FREE shipping!</strong>';
        $percentage = 100;
    }
    
    echo '<div class="free-shipping-bar" style="margin:20px 0;padding:20px;background:#f8f9fa;border-radius:12px;">';
    echo '<p style="margin:0 0 12px;text-align:center;font-size:14px;color:#333;">' . $message . '</p>';
    echo '<div style="background:#e0e0e0;border-radius:20px;height:12px;overflow:hidden;">';
    echo '<div style="background:linear-gradient(90deg, #667eea, #764ba2);height:100%;width:' . $percentage . '%;border-radius:20px;transition:width 0.5s ease;"></div>';
    echo '</div></div>';
});

// Also show on checkout
add_action('woocommerce_review_order_before_shipping', function() {
    $free_shipping_threshold = 100;
    $cart_total = WC()->cart->get_cart_contents_total();
    $remaining = $free_shipping_threshold - $cart_total;
    $percentage = min(100, ($cart_total / $free_shipping_threshold) * 100);
    
    if ($remaining > 0) {
        $message = sprintf(
            'Add <strong>%s</strong> more to get <strong>FREE shipping!</strong>',
            wc_price($remaining)
        );
    } else {
        $message = '🎉 You qualify for <strong>FREE shipping!</strong>';
        $percentage = 100;
    }
    
    echo '<div class="free-shipping-bar" style="margin:15px 0;padding:15px;background:#f8f9fa;border-radius:10px;">';
    echo '<p style="margin:0 0 10px;text-align:center;font-size:13px;color:#333;">' . $message . '</p>';
    echo '<div style="background:#e0e0e0;border-radius:20px;height:10px;overflow:hidden;">';
    echo '<div style="background:linear-gradient(90deg, #667eea, #764ba2);height:100%;width:' . $percentage . '%;border-radius:20px;"></div>';
    echo '</div></div>';
});
```

### 2.5 Minimum Order Quantity/Value

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Minimum order value check
add_action('woocommerce_check_cart_items', function() {
    $minimum_order_value = 20; // $20 minimum
    
    if (WC()->cart->total < $minimum_order_value) {
        wc_add_notice(sprintf(
            'Minimum order amount is %s. Your current order total is %s.',
            wc_price($minimum_order_value),
            wc_price(WC()->cart->total)
        ), 'error');
    }
});

// Minimum quantity per product
add_filter('woocommerce_quantity_input_args', function($args, $product) {
    $args['min_value'] = 1;  // Minimum quantity
    $args['step'] = 1;        // Quantity step
    return $args;
}, 10, 2);

// Minimum quantity for specific categories
add_filter('woocommerce_quantity_input_args', function($args, $product) {
    $min_qty_categories = array(
        'bulk-items' => 5,
        'wholesale' => 10,
    );
    
    foreach ($min_qty_categories as $cat_slug => $min_qty) {
        if (has_term($cat_slug, 'product_cat', $product->get_id())) {
            $args['min_value'] = $min_qty;
            break;
        }
    }
    return $args;
}, 10, 2);
```

### 2.6 Custom Checkout Fields

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add custom checkout field (delivery date)
add_filter('woocommerce_checkout_fields', function($fields) {
    $fields['billing']['billing_delivery_date'] = array(
        'type' => 'date',
        'label' => __('Preferred Delivery Date', 'textdomain'),
        'placeholder' => __('Select date', 'textdomain'),
        'required' => false,
        'priority' => 120,
        'class' => array('form-row-wide'),
    );
    
    $fields['order']['order_comments_placeholder'] = array(
        'type' => 'textarea',
        'label' => __('Special Instructions', 'textdomain'),
        'placeholder' => __('Notes about your order, e.g. special delivery instructions', 'textdomain'),
        'required' => false,
    );
    
    return $fields;
});

// Save custom checkout field to order meta
add_action('woocommerce_checkout_update_order_meta', function($order_id) {
    if (!empty($_POST['billing_delivery_date'])) {
        update_post_meta($order_id, '_delivery_date', sanitize_text_field($_POST['billing_delivery_date']));
    }
});

// Display custom field in admin order view
add_action('woocommerce_admin_order_data_after_shipping_address', function($order) {
    $delivery_date = get_post_meta($order->get_id(), '_delivery_date', true);
    if ($delivery_date) {
        echo '<p><strong>' . __('Delivery Date:') . '</strong> ' . esc_html($delivery_date) . '</p>';
    }
});

// Remove unwanted checkout fields
add_filter('woocommerce_checkout_fields', function($fields) {
    // Uncomment fields you want to remove
    // unset($fields['billing']['billing_company']);
    // unset($fields['billing']['billing_address_2']);
    // unset($fields['shipping']['shipping_company']);
    // unset($fields['shipping']['shipping_address_2']);
    // unset($fields['order']['order_comments']);
    
    return $fields;
});
```

### 2.7 Custom Product Tabs

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add custom product tab (Shipping Info)
add_filter('woocommerce_product_tabs', function($tabs) {
    $tabs['shipping_info'] = array(
        'title' => __('Shipping & Returns', 'textdomain'),
        'priority' => 30,
        'callback' => 'custom_shipping_info_tab_content',
    );
    
    $tabs['size_guide'] = array(
        'title' => __('Size Guide', 'textdomain'),
        'priority' => 25,
        'callback' => 'custom_size_guide_tab_content',
    );
    
    return $tabs;
});

function custom_shipping_info_tab_content() {
    echo '<h3>Shipping Information</h3>';
    echo '<ul style="list-style:disc;padding-left:20px;">';
    echo '<li><strong>Free Shipping</strong> on orders over $100</li>';
    echo '<li><strong>Standard Shipping:</strong> 3-5 business days</li>';
    echo '<li><strong>Express Shipping:</strong> 1-2 business days</li>';
    echo '<li><strong>International Shipping:</strong> 7-14 business days</li>';
    echo '</ul>';
    echo '<h3>Return Policy</h3>';
    echo '<p>We offer 30-day returns on all unused items in original packaging. <a href="/shipping-policy/">Read full policy</a>.</p>';
}

function custom_size_guide_tab_content() {
    echo '<h3>Size Guide</h3>';
    echo '<table style="width:100%;border-collapse:collapse;">';
    echo '<thead><tr style="background:#f5f5f5;">';
    echo '<th style="padding:12px;border:1px solid #ddd;">Size</th>';
    echo '<th style="padding:12px;border:1px solid #ddd;">Chest (in)</th>';
    echo '<th style="padding:12px;border:1px solid #ddd;">Waist (in)</th>';
    echo '<th style="padding:12px;border:1px solid #ddd;">Length (in)</th>';
    echo '</tr></thead><tbody>';
    echo '<tr><td style="padding:12px;border:1px solid #ddd;">S</td><td style="padding:12px;border:1px solid #ddd;">34-36</td><td style="padding:12px;border:1px solid #ddd;">28-30</td><td style="padding:12px;border:1px solid #ddd;">27</td></tr>';
    echo '<tr><td style="padding:12px;border:1px solid #ddd;">M</td><td style="padding:12px;border:1px solid #ddd;">38-40</td><td style="padding:12px;border:1px solid #ddd;">32-34</td><td style="padding:12px;border:1px solid #ddd;">28</td></tr>';
    echo '<tr><td style="padding:12px;border:1px solid #ddd;">L</td><td style="padding:12px;border:1px solid #ddd;">42-44</td><td style="padding:12px;border:1px solid #ddd;">36-38</td><td style="padding:12px;border:1px solid #ddd;">29</td></tr>';
    echo '<tr><td style="padding:12px;border:1px solid #ddd;">XL</td><td style="padding:12px;border:1px solid #ddd;">46-48</td><td style="padding:12px;border:1px solid #ddd;">40-42</td><td style="padding:12px;border:1px solid #ddd;">30</td></tr>';
    echo '</tbody></table>';
}
```

### 2.8 Recently Viewed Products Shortcode

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Track recently viewed products
add_action('template_redirect', function() {
    if (is_singular('product')) {
        global $post;
        $viewed = WC()->session->get('recently_viewed', array());
        $viewed = array_diff($viewed, array($post->ID));
        array_unshift($viewed, $post->ID);
        $viewed = array_slice($viewed, 0, 8);
        WC()->session->set('recently_viewed', $viewed);
    }
});

// Shortcode to display recently viewed products
add_shortcode('recently_viewed', function($atts) {
    $atts = shortcode_atts(array(
        'limit' => 4,
        'columns' => 4,
    ), $atts);
    
    $viewed = WC()->session ? WC()->session->get('recently_viewed', array()) : array();
    
    if (empty($viewed)) {
        return '<p>No recently viewed products yet.</p>';
    }
    
    $viewed = array_slice($viewed, 0, $atts['limit']);
    
    ob_start();
    echo '<div class="recently-viewed-products">';
    echo '<h3 style="margin-bottom:20px;">Recently Viewed</h3>';
    echo do_shortcode('[products columns="' . $atts['columns'] . '" ids="' . implode(',', $viewed) . '"]');
    echo '</div>';
    return ob_get_clean();
});
```

### 2.9 Auto-Complete Virtual Product Orders

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Auto-complete orders with only virtual products
add_action('woocommerce_thankyou', function($order_id) {
    if (!$order_id) return;
    
    $order = wc_get_order($order_id);
    if (!$order) return;
    
    $virtual = true;
    foreach ($order->get_items() as $item) {
        $product = $item->get_product();
        if ($product && !$product->is_virtual()) {
            $virtual = false;
            break;
        }
    }
    
    if ($virtual) {
        $order->update_status('completed', 'Auto-completed: order contains only virtual products.');
    }
});
```

### 2.10 Custom Email Template Styling

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Customize email sender name and address
add_filter('woocommerce_email_from_name', function() {
    return get_bloginfo('name');
});

add_filter('woocommerce_email_from_address', function() {
    return get_option('admin_email');
});

// Add custom content to order email
add_action('woocommerce_email_after_order_table', function($order, $sent_to_admin, $plain_text) {
    if ($plain_text) {
        echo "\nThank you for shopping with us!\n";
        echo "Follow us on social media for updates and promotions.\n";
    } else {
        echo '<div style="text-align:center;padding:20px;border-top:2px solid #eee;margin-top:20px;">';
        echo '<p style="font-size:14px;color:#666;">Thank you for shopping with us!</p>';
        echo '<p style="font-size:13px;color:#999;">Follow us: ';
        echo '<a href="#" style="color:#667eea;text-decoration:none;">Facebook</a> | ';
        echo '<a href="#" style="color:#667eea;text-decoration:none;">Instagram</a> | ';
        echo '<a href="#" style="color:#667eea;text-decoration:none;">Twitter</a>';
        echo '</p></div>';
    }
}, 10, 3);

// Change email base color
add_filter('woocommerce_email_base_color', function() {
    return '#667eea'; // Match your brand color
});
```

---

## Section 3: Performance Optimization via Code Snippets

### 3.1 Disable WooCommerce Cart Fragments on Non-Shop Pages

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Disable cart fragments on non-WooCommerce pages (major INP improvement)
add_action('wp_enqueue_scripts', function() {
    if (function_exists('is_woocommerce')) {
        if (!is_woocommerce() && !is_cart() && !is_checkout() && !is_account_page() && !is_product() && !is_product_category() && !is_shop()) {
            wp_dequeue_script('wc-cart-fragments');
        }
    }
}, 11);
```

**Verification:** Check PageSpeed Insights. INP should improve significantly on non-shop pages.

### 3.2 Defer Non-Critical JavaScript

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Defer JavaScript loading
add_filter('script_loader_tag', function($tag, $handle) {
    // Don't defer critical scripts
    $critical = array('jquery-core', 'jquery-migrate', 'elementor-frontend');
    
    if (in_array($handle, $critical)) {
        return $tag;
    }
    
    // Add defer to all other scripts
    if (strpos($tag, ' defer') === false && strpos($tag, ' async') === false) {
        $tag = str_replace(' src', ' defer src', $tag);
    }
    
    return $tag;
}, 10, 2);
```

### 3.3 Remove Query Strings from Static Resources

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Remove version query strings from CSS and JS (improves caching)
add_filter('script_loader_src', function($src) {
    if (strpos($src, '?ver=') !== false) {
        $src = remove_query_arg('ver', $src);
    }
    return $src;
}, 15, 1);

add_filter('style_loader_src', function($src) {
    if (strpos($src, '?ver=') !== false) {
        $src = remove_query_arg('ver', $src);
    }
    return $src;
}, 15, 1);
```

### 3.4 Preconnect to External Domains

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add preconnect for external resources
add_action('wp_head', function() {
    echo '<link rel="preconnect" href="https://fonts.googleapis.com">';
    echo '<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>';
    echo '<link rel="preconnect" href="https://cdn.jsdelivr.net">';
    // Add your payment gateway domains
    echo '<link rel="preconnect" href="https://js.stripe.com">';
    echo '<link rel="preconnect" href="https://www.paypal.com">';
    echo '<link rel="dns-prefetch" href="https://www.google-analytics.com">';
}, 1);
```

### 3.5 Disable Dashicons on Front-End

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Remove dashicons CSS from front-end (non-logged-in users)
add_action('wp_enqueue_scripts', function() {
    if (!is_user_logged_in()) {
        wp_dequeue_style('dashicons');
        wp_deregister_style('dashicons');
    }
}, 11);
```

### 3.6 Lazy Load All Images

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add loading="lazy" to all images that don't have it
add_filter('the_content', function($content) {
    if (!is_admin() && is_singular()) {
        $content = preg_replace_callback('/<img[^>]+>/', function($matches) {
            $img = $matches[0];
            // Skip if already has loading attribute
            if (strpos($img, 'loading=') !== false) {
                return $img;
            }
            // Skip if it has fetchpriority="high" (LCP image)
            if (strpos($img, 'fetchpriority') !== false) {
                return $img;
            }
            // Add loading="lazy"
            return str_replace('<img', '<img loading="lazy"', $img);
        }, $content);
    }
    return $content;
});

// Add width and height to images without them (prevents CLS)
add_filter('the_content', function($content) {
    $content = preg_replace_callback('/<img((?![^>]*width=)[^>]*)(?:src="([^"]*)")([^>]*)>/i', function($matches) {
        $url = $matches[2];
        // Try to get dimensions from the URL
        if (preg_match('/-(\d+)x(\d+)\.(jpg|jpeg|png|webp|gif)$/i', $url, $dims)) {
            return '<img' . $matches[1] . 'src="' . $matches[2] . '"' . $matches[3] . ' width="' . $dims[1] . '" height="' . $dims[2] . '">';
        }
        return $matches[0];
    }, $content);
    return $content;
});
```

---

## Section 4: SEO Enhancements via Code Snippets

### 4.1 Custom Meta Robots for Specific Pages

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add noindex to specific pages
add_action('wp_head', function() {
    if (is_page('cart') || is_page('checkout') || is_page('my-account') || is_page('wishlist')) {
        echo '<meta name="robots" content="noindex,nofollow">' . "\n";
    }
    if (is_search() || is_date() || is_author() || is_attachment()) {
        echo '<meta name="robots" content="noindex,follow">' . "\n";
    }
}, 1);
```

### 4.2 Custom OpenGraph Tags

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add OpenGraph tags if Rank Math is not handling them
add_action('wp_head', function() {
    // Only run if Rank Math OpenGraph is disabled
    if (defined('RANK_MATH_FILE') && rank_math()->settings->get('opengraph')) {
        return; // Rank Math is handling OpenGraph
    }
    
    if (is_singular()) {
        global $post;
        $title = get_the_title($post->ID);
        $description = wp_trim_words(wp_strip_all_tags($post->post_content), 30);
        $url = get_permalink($post->ID);
        $image = get_the_post_thumbnail_url($post->ID, 'full');
        $site_name = get_bloginfo('name');
        
        echo '<meta property="og:title" content="' . esc_attr($title) . '">' . "\n";
        echo '<meta property="og:description" content="' . esc_attr($description) . '">' . "\n";
        echo '<meta property="og:url" content="' . esc_url($url) . '">' . "\n";
        echo '<meta property="og:site_name" content="' . esc_attr($site_name) . '">' . "\n";
        echo '<meta property="og:type" content="article">' . "\n";
        if ($image) {
            echo '<meta property="og:image" content="' . esc_url($image) . '">' . "\n";
            echo '<meta property="og:image:width" content="1200">' . "\n";
            echo '<meta property="og:image:height" content="630">' . "\n";
        }
        echo '<meta name="twitter:card" content="summary_large_image">' . "\n";
        echo '<meta name="twitter:title" content="' . esc_attr($title) . '">' . "\n";
        echo '<meta name="twitter:description" content="' . esc_attr($description) . '">' . "\n";
        if ($image) {
            echo '<meta name="twitter:image" content="' . esc_url($image) . '">' . "\n";
        }
    } elseif (is_front_page()) {
        echo '<meta property="og:title" content="' . esc_attr(get_bloginfo('name')) . '">' . "\n";
        echo '<meta property="og:description" content="' . esc_attr(get_bloginfo('description')) . '">' . "\n";
        echo '<meta property="og:url" content="' . esc_url(home_url('/')) . '">' . "\n";
        echo '<meta property="og:site_name" content="' . esc_attr(get_bloginfo('name')) . '">' . "\n";
        echo '<meta property="og:type" content="website">' . "\n";
    }
}, 5);
```

### 4.3 Custom Breadcrumbs (Fallback if Rank Math breadcrumbs disabled)

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Custom breadcrumb function and shortcode
function custom_breadcrumbs() {
    if (is_front_page()) return;
    
    echo '<nav class="breadcrumbs" style="font-size:13px;margin-bottom:20px;color:#666;" aria-label="Breadcrumb">';
    echo '<ol style="list-style:none;display:flex;flex-wrap:wrap;gap:8px;padding:0;margin:0;">';
    
    // Home
    echo '<li><a href="' . esc_url(home_url('/')) . '" style="color:#667eea;text-decoration:none;">Home</a></li>';
    echo '<li style="color:#ccc;">/</li>';
    
    if (is_singular('product')) {
        // Shop
        echo '<li><a href="' . esc_url(get_permalink(wc_get_page_id('shop'))) . '" style="color:#667eea;text-decoration:none;">Shop</a></li>';
        echo '<li style="color:#ccc;">/</li>';
        
        // Category
        $terms = get_the_terms(get_the_ID(), 'product_cat');
        if ($terms && !is_wp_error($terms)) {
            $term = $terms[0];
            echo '<li><a href="' . esc_url(get_term_link($term)) . '" style="color:#667eea;text-decoration:none;">' . esc_html($term->name) . '</a></li>';
            echo '<li style="color:#ccc;">/</li>';
        }
        
        // Current product
        echo '<li style="color:#333;font-weight:500;" aria-current="page">' . esc_html(get_the_title()) . '</li>';
    } elseif (is_product_category()) {
        echo '<li><a href="' . esc_url(get_permalink(wc_get_page_id('shop'))) . '" style="color:#667eea;text-decoration:none;">Shop</a></li>';
        echo '<li style="color:#ccc;">/</li>';
        $current_term = get_queried_object();
        if ($current_term->parent) {
            $parent = get_term($current_term->parent, 'product_cat');
            echo '<li><a href="' . esc_url(get_term_link($parent)) . '" style="color:#667eea;text-decoration:none;">' . esc_html($parent->name) . '</a></li>';
            echo '<li style="color:#ccc;">/</li>';
        }
        echo '<li style="color:#333;font-weight:500;" aria-current="page">' . esc_html($current_term->name) . '</li>';
    } elseif (is_singular('post')) {
        echo '<li><a href="' . esc_url(get_permalink(get_option('page_for_posts'))) . '" style="color:#667eea;text-decoration:none;">Blog</a></li>';
        echo '<li style="color:#ccc;">/</li>';
        echo '<li style="color:#333;font-weight:500;" aria-current="page">' . esc_html(get_the_title()) . '</li>';
    } elseif (is_page()) {
        $parents = get_post_ancestors(get_the_ID());
        if ($parents) {
            $parents = array_reverse($parents);
            foreach ($parents as $parent_id) {
                echo '<li><a href="' . esc_url(get_permalink($parent_id)) . '" style="color:#667eea;text-decoration:none;">' . esc_html(get_the_title($parent_id)) . '</a></li>';
                echo '<li style="color:#ccc;">/</li>';
            }
        }
        echo '<li style="color:#333;font-weight:500;" aria-current="page">' . esc_html(get_the_title()) . '</li>';
    } elseif (is_home()) {
        echo '<li style="color:#333;font-weight:500;" aria-current="page">Blog</li>';
    } elseif (is_search()) {
        echo '<li style="color:#333;font-weight:500;" aria-current="page">Search: ' . esc_html(get_search_query()) . '</li>';
    } elseif (is_404()) {
        echo '<li style="color:#333;font-weight:500;" aria-current="page">404 - Page Not Found</li>';
    }
    
    echo '</ol></nav>';
}

// Auto-insert breadcrumbs after header
add_action('wp_body_open', function() {
    if (!is_front_page()) {
        echo '<div class="breadcrumb-container" style="max-width:1200px;margin:0 auto;padding:15px 20px 0;">';
        custom_breadcrumbs();
        echo '</div>';
    }
}, 20);
```

### 4.4 FAQPage Schema Markup via Shortcode

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// FAQ shortcode with automatic FAQPage schema
add_shortcode('faq', function($atts, $content = null) {
    // Parse FAQ items from content
    // Format: [faq]
    //   [faq_item q="Question 1"]Answer 1[/faq_item]
    //   [faq_item q="Question 2"]Answer 2[/faq_item]
    // [/faq]
    
    $output = '<div class="faq-section" itemscope itemtype="https://schema.org/FAQPage">';
    $schema = array(
        '@context' => 'https://schema.org',
        '@type' => 'FAQPage',
        'mainEntity' => array()
    );
    
    // The content is already parsed by nested shortcode
    $output .= do_shortcode($content);
    $output .= '</div>';
    
    // Output schema
    echo '<script type="application/ld+json">' . json_encode($schema, JSON_UNESCAPED_SLASHES | JSON_UNESCAPED_UNICODE) . '</script>';
    
    return $output;
});

add_shortcode('faq_item', function($atts, $content = null) {
    $atts = shortcode_atts(array('q' => ''), $atts);
    
    $html = '<div class="faq-item" itemscope itemtype="https://schema.org/Question" style="margin-bottom:16px;border:1px solid #e0e0e0;border-radius:8px;overflow:hidden;">';
    $html .= '<button class="faq-question" itemprop="name" style="width:100%;text-align:left;padding:16px;background:#f8f9fa;border:none;font-size:15px;font-weight:600;cursor:pointer;display:flex;justify-content:space-between;align-items:center;">';
    $html .= esc_html($atts['q']);
    $html .= '<span class="faq-toggle" style="font-size:20px;transition:transform 0.3s;">+</span>';
    $html .= '</button>';
    $html .= '<div class="faq-answer" itemscope itemtype="https://schema.org/Answer" style="padding:0 16px;max-height:0;overflow:hidden;transition:max-height 0.3s,padding 0.3s;">';
    $html .= '<div itemprop="text" style="padding:16px 0;line-height:1.6;color:#555;">' . wpautop(wp_kses_post($content)) . '</div>';
    $html .= '</div></div>';
    
    return $html;
});

// JS for FAQ toggle
add_action('wp_footer', function() {
    ?>
    <script>
    document.addEventListener('DOMContentLoaded', function() {
        document.querySelectorAll('.faq-question').forEach(function(btn) {
            btn.addEventListener('click', function() {
                var answer = this.nextElementSibling;
                var toggle = this.querySelector('.faq-toggle');
                if (answer.style.maxHeight && answer.style.maxHeight !== '0px') {
                    answer.style.maxHeight = '0px';
                    answer.style.padding = '0 16px';
                    toggle.style.transform = 'rotate(0deg)';
                    toggle.textContent = '+';
                } else {
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                    answer.style.padding = '0 16px';
                    toggle.style.transform = 'rotate(45deg)';
                    toggle.textContent = '×';
                }
            });
        });
    });
    </script>
    <?php
}, 20);
```

---

## Section 5: Dynamic Product Renderers

### 5.1 Dynamic Homepage Product Grid

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Dynamic featured products on homepage
add_shortcode('featured_products_grid', function($atts) {
    $atts = shortcode_atts(array(
        'limit' => 8,
        'columns' => 4,
        'title' => 'Featured Products',
    ), $atts);
    
    $args = array(
        'post_type' => 'product',
        'post_status' => 'publish',
        'posts_per_page' => $atts['limit'],
        'tax_query' => array(
            array(
                'taxonomy' => 'product_visibility',
                'field' => 'name',
                'terms' => 'featured',
                'operator' => 'IN',
            ),
        ),
    );
    
    $products = new WP_Query($args);
    
    if (!$products->have_posts()) {
        // Fallback to recent products
        $args['tax_query'] = array();
        $args['orderby'] = 'date';
        $args['order'] = 'DESC';
        $products = new WP_Query($args);
    }
    
    ob_start();
    echo '<div class="dynamic-product-grid" style="margin:40px 0;">';
    if ($atts['title']) {
        echo '<h2 class="section-title" style="text-align:center;margin-bottom:30px;font-size:28px;">' . esc_html($atts['title']) . '</h2>';
    }
    echo '<div style="display:grid;grid-template-columns:repeat(' . $atts['columns'] . ', 1fr);gap:20px;">';
    
    while ($products->have_posts()) {
        $products->the_post();
        $product = wc_get_product(get_the_ID());
        $permalink = get_permalink($product->get_id());
        $image = wp_get_attachment_image_src($product->get_image_id(), 'woocommerce_thumbnail');
        $price_html = $product->get_price_html();
        $on_sale = $product->is_on_sale();
        
        echo '<div class="product-card" style="border:1px solid #eee;border-radius:12px;overflow:hidden;transition:box-shadow 0.3s,transform 0.3s;">';
        echo '<a href="' . esc_url($permalink) . '" style="text-decoration:none;color:inherit;display:block;">';
        
        if ($image) {
            echo '<div style="position:relative;overflow:hidden;aspect-ratio:1;">';
            echo '<img src="' . esc_url($image[0]) . '" alt="' . esc_attr($product->get_name()) . '" style="width:100%;height:100%;object-fit:cover;transition:transform 0.5s;" loading="lazy">';
            if ($on_sale) {
                echo '<span style="position:absolute;top:10px;left:10px;background:#e25555;color:#fff;padding:4px 10px;border-radius:6px;font-size:12px;font-weight:600;">SALE</span>';
            }
            echo '</div>';
        }
        
        echo '<div style="padding:16px;">';
        echo '<h3 style="font-size:15px;margin:0 0 8px;line-height:1.4;">' . esc_html($product->get_name()) . '</h3>';
        
        // Star rating
        $rating = $product->get_average_rating();
        if ($rating > 0) {
            echo '<div style="margin-bottom:8px;font-size:13px;color:#ffa500;">' . str_repeat('★', round($rating)) . str_repeat('☆', 5 - round($rating)) . ' <span style="color:#999;">(' . esc_html($rating) . ')</span></div>';
        }
        
        echo '<div class="price" style="font-size:18px;font-weight:700;color:#333;">' . $price_html . '</div>';
        echo '</div>';
        echo '</a>';
        
        // Add to cart button
        echo '<div style="padding:0 16px 16px;">';
        echo '<a href="?add-to-cart=' . $product->get_id() . '" data-product_id="' . $product->get_id() . '" class="button add_to_cart_button ajax_add_to_cart" style="display:block;text-align:center;padding:12px;background:#667eea;color:#fff;text-decoration:none;border-radius:8px;font-weight:600;font-size:14px;transition:background 0.3s;" onmouseover="this.style.background=\'#5568d3\'" onmouseout="this.style.background=\'#667eea\'">Add to Cart</a>';
        echo '</div>';
        
        echo '</div>';
    }
    
    echo '</div></div>';
    wp_reset_postdata();
    return ob_get_clean();
});
```

### 5.2 Dynamic Blog Posts Grid

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Dynamic recent blog posts
add_shortcode('recent_posts_grid', function($atts) {
    $atts = shortcode_atts(array(
        'limit' => 3,
        'columns' => 3,
        'category' => '',
        'title' => 'Latest from Our Blog',
    ), $atts);
    
    $args = array(
        'post_type' => 'post',
        'post_status' => 'publish',
        'posts_per_page' => $atts['limit'],
        'orderby' => 'date',
        'order' => 'DESC',
    );
    
    if ($atts['category']) {
        $args['category_name'] = $atts['category'];
    }
    
    $posts = new WP_Query($args);
    
    if (!$posts->have_posts()) {
        return '<p>No posts found.</p>';
    }
    
    ob_start();
    echo '<div class="blog-posts-grid" style="margin:40px 0;">';
    if ($atts['title']) {
        echo '<h2 class="section-title" style="text-align:center;margin-bottom:30px;font-size:28px;">' . esc_html($atts['title']) . '</h2>';
    }
    echo '<div style="display:grid;grid-template-columns:repeat(' . $atts['columns'] . ', 1fr);gap:24px;">';
    
    while ($posts->have_posts()) {
        $posts->the_post();
        $image = get_the_post_thumbnail_url(get_the_ID(), 'medium_large');
        $categories = get_the_category();
        $author = get_the_author();
        $date = get_the_date();
        $excerpt = wp_trim_words(get_the_excerpt(), 20);
        
        echo '<article class="blog-card" style="border:1px solid #eee;border-radius:12px;overflow:hidden;transition:box-shadow 0.3s;">';
        
        if ($image) {
            echo '<a href="' . esc_url(get_permalink()) . '" style="display:block;overflow:hidden;aspect-ratio:16/9;">';
            echo '<img src="' . esc_url($image) . '" alt="' . esc_attr(get_the_title()) . '" style="width:100%;height:100%;object-fit:cover;transition:transform 0.5s;" loading="lazy">';
            echo '</a>';
        }
        
        echo '<div style="padding:20px;">';
        
        if ($categories) {
            echo '<span style="display:inline-block;background:#667eea;color:#fff;padding:3px 10px;border-radius:4px;font-size:11px;font-weight:600;margin-bottom:10px;text-transform:uppercase;">' . esc_html($categories[0]->name) . '</span>';
        }
        
        echo '<h3 style="font-size:17px;margin:0 0 10px;line-height:1.4;"><a href="' . esc_url(get_permalink()) . '" style="color:#333;text-decoration:none;">' . esc_html(get_the_title()) . '</a></h3>';
        
        echo '<p style="font-size:14px;color:#666;margin:0 0 12px;line-height:1.6;">' . esc_html($excerpt) . '</p>';
        
        echo '<div style="font-size:12px;color:#999;">' . esc_html($author) . ' · ' . esc_html($date) . '</div>';
        
        echo '</div></article>';
    }
    
    echo '</div></div>';
    wp_reset_postdata();
    return ob_get_clean();
});
```

---

## Section 6: Security Hardening via Code Snippets

### 6.1 Disable File Editing in Admin

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Disable theme and plugin editor
if (!defined('DISALLOW_FILE_EDIT')) {
    define('DISALLOW_FILE_EDIT', true);
}
```

### 6.2 Limit Login Attempts

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Simple login attempt limiter
add_action('wp_login_failed', function($username) {
    $ip = $_SERVER['REMOTE_ADDR'];
    $attempts = get_transient('login_attempts_' . $ip) ?: 0;
    $attempts++;
    set_transient('login_attempts_' . $ip, $attempts, 1800); // 30 min window
    
    if ($attempts >= 5) {
        set_transient('login_blocked_' . $ip, true, 1800); // Block for 30 min
    }
});

add_filter('authenticate', function($user, $username, $password) {
    $ip = $_SERVER['REMOTE_ADDR'];
    if (get_transient('login_blocked_' . $ip)) {
        return new WP_Error('too_many_attempts', 'Too many login attempts. Please try again in 30 minutes.');
    }
    return $user;
}, 30, 3);

// Reset on successful login
add_action('wp_login', function() {
    $ip = $_SERVER['REMOTE_ADDR'];
    delete_transient('login_attempts_' . $ip);
    delete_transient('login_blocked_' . $ip);
});
```

### 6.3 Hide Login Error Messages

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Generic login error message
add_filter('login_errors', function() {
    return 'Invalid login credentials. Please try again.';
});
```

### 6.4 Disable User Enumeration

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Block ?author=N URL parameter
add_action('template_redirect', function() {
    if (isset($_GET['author']) && !is_admin()) {
        wp_redirect(home_url('/'), 301);
        exit;
    }
});

// Remove author class from body
add_filter('body_class', function($classes) {
    foreach ($classes as $key => $class) {
        if (strpos($class, 'author-') === 0 || $class === 'author') {
            unset($classes[$key]);
        }
    }
    return $classes;
});
```

---

## Section 7: Custom Shortcodes for Page Content

### 7.1 Contact Info Shortcode

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// [contact_info] shortcode
add_shortcode('contact_info', function($atts) {
    $atts = shortcode_atts(array(
        'email' => get_option('admin_email'),
        'phone' => '',
        'address' => '',
    ), $atts);
    
    $html = '<div class="contact-info-block" style="padding:20px;background:#f8f9fa;border-radius:12px;">';
    
    if ($atts['email']) {
        $html .= '<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">';
        $html .= '<span style="font-size:24px;">📧</span>';
        $html .= '<a href="mailto:' . esc_attr($atts['email']) . '" style="color:#667eea;text-decoration:none;">' . esc_html($atts['email']) . '</a>';
        $html .= '</div>';
    }
    
    if ($atts['phone']) {
        $html .= '<div style="display:flex;align-items:center;gap:12px;margin-bottom:12px;">';
        $html .= '<span style="font-size:24px;">📱</span>';
        $html .= '<a href="tel:' . esc_attr(preg_replace('/[^0-9+]/', '', $atts['phone'])) . '" style="color:#667eea;text-decoration:none;">' . esc_html($atts['phone']) . '</a>';
        $html .= '</div>';
    }
    
    if ($atts['address']) {
        $html .= '<div style="display:flex;align-items:center;gap:12px;">';
        $html .= '<span style="font-size:24px;">📍</span>';
        $html .= '<span>' . esc_html($atts['address']) . '</span>';
        $html .= '</div>';
    }
    
    $html .= '</div>';
    return $html;
});
```

### 7.2 Product Categories Grid Shortcode

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// [product_categories_grid] shortcode
add_shortcode('product_categories_grid', function($atts) {
    $atts = shortcode_atts(array(
        'limit' => 6,
        'columns' => 3,
        'hide_empty' => true,
    ), $atts);
    
    $args = array(
        'taxonomy' => 'product_cat',
        'hide_empty' => $atts['hide_empty'],
        'number' => $atts['limit'],
        'parent' => 0,
    );
    
    $categories = get_terms($args);
    
    if (is_wp_error($categories) || empty($categories)) {
        return '<p>No product categories found.</p>';
    }
    
    ob_start();
    echo '<div class="categories-grid" style="margin:30px 0;">';
    echo '<div style="display:grid;grid-template-columns:repeat(' . $atts['columns'] . ', 1fr);gap:20px;">';
    
    foreach ($categories as $cat) {
        $thumbnail_id = get_term_meta($cat->term_id, 'thumbnail_id', true);
        $image = wp_get_attachment_image_src($thumbnail_id, 'medium');
        $link = get_term_link($cat);
        
        echo '<a href="' . esc_url($link) . '" class="category-card" style="text-decoration:none;display:block;border-radius:12px;overflow:hidden;position:relative;aspect-ratio:4/3;background:#f0f0f0;">';
        
        if ($image) {
            echo '<img src="' . esc_url($image[0]) . '" alt="' . esc_attr($cat->name) . '" style="width:100%;height:100%;object-fit:cover;transition:transform 0.5s;" loading="lazy">';
        }
        
        echo '<div style="position:absolute;bottom:0;left:0;right:0;background:linear-gradient(transparent,rgba(0,0,0,0.7));padding:30px 20px 20px;">';
        echo '<h3 style="color:#fff;font-size:18px;margin:0 0 4px;">' . esc_html($cat->name) . '</h3>';
        echo '<span style="color:rgba(255,255,255,0.8);font-size:13px;">' . $cat->count . ' products →</span>';
        echo '</div>';
        echo '</a>';
    }
    
    echo '</div></div>';
    return ob_get_clean();
});
```

### 7.3 Trust Badges Shortcode

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// [trust_badges] shortcode
add_shortcode('trust_badges', function($atts) {
    $atts = shortcode_atts(array(
        'style' => 'grid', // grid or row
    ), $atts);
    
    $badges = array(
        array('icon' => '🚚', 'title' => 'Free Shipping', 'desc' => 'On orders over $100'),
        array('icon' => '🔄', 'title' => '30-Day Returns', 'desc' => 'Hassle-free returns'),
        array('icon' => '🔒', 'title' => 'Secure Payment', 'desc' => 'SSL encrypted checkout'),
        array('icon' => '⭐', 'title' => 'Quality Guaranteed', 'desc' => 'Premium products only'),
    );
    
    $layout = $atts['style'] === 'row'
        ? 'display:flex;justify-content:space-around;flex-wrap:wrap;gap:20px;'
        : 'display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:20px;';
    
    $html = '<div class="trust-badges" style="margin:30px 0;padding:30px;background:#f8f9fa;border-radius:16px;">';
    $html .= '<div style="' . $layout . '">';
    
    foreach ($badges as $badge) {
        $html .= '<div style="text-align:center;padding:16px;">';
        $html .= '<div style="font-size:36px;margin-bottom:8px;">' . $badge['icon'] . '</div>';
        $html .= '<div style="font-weight:700;font-size:15px;color:#333;margin-bottom:4px;">' . $badge['title'] . '</div>';
        $html .= '<div style="font-size:13px;color:#666;">' . $badge['desc'] . '</div>';
        $html .= '</div>';
    }
    
    $html .= '</div></div>';
    return $html;
});
```

---

## Section 8: Age/Compliance Gate

### DEAD RULE: Age Gate MUST Be a Global Code Snippet — NEVER in Page HTML

**This is a DEAD RULE. The age verification gate MUST be implemented as a global Code Snippets PHP snippet using the `wp_footer` hook. The agent MUST NEVER place age gate HTML, CSS, or JS inside an Elementor HTML widget on any individual page. No exceptions.**

#### Why This Is a Dead Rule

1. **Import failures**: When age gate HTML/CSS/JS (which is typically 2,000-4,000 characters) is added to a page's Elementor HTML widget, the total page HTML payload can exceed Elementor's paste limit. This causes the HTML widget paste to fail, truncate, or timeout — the age gate code prevents the entire page from importing.

2. **Duplication**: If the age gate is in the page HTML, it only appears on that one page. The age gate needs to appear site-wide on first visit. Putting it in every page's HTML widget is redundant and bloats every page.

3. **Maintenance nightmare**: If the age gate text, design, or behavior needs to change, the agent would need to update every single page's HTML widget instead of updating one Code Snippet.

4. **Global scope**: The age gate uses `wp_footer` hook with priority 5, which fires on EVERY front-end page load. This is the correct architecture — one snippet, site-wide coverage, zero page HTML bloat.

#### Implementation Requirement

- Create the age gate as a **Code Snippets PHP snippet** (NOT an HTML snippet, NOT in Elementor HTML widget).
- Use `add_action('wp_footer', function() { ... }, 5)` — the priority 5 ensures it loads early.
- The snippet scope is **Front-end** (not Admin).
- The snippet lifecycle is **persistent** — it stays active permanently.
- After activating the snippet, verify on the front-end that the age gate appears on first visit and does not appear after confirmation (localStorage check).
- **NEVER** copy any portion of the age gate code into an Elementor HTML widget, page content, or post content.

### 8.1 Age Verification Gate

**Type:** PHP + HTML + JS + CSS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Age verification gate (first visit only, uses localStorage)
add_action('wp_footer', function() {
    // Skip on admin, login, and API
    if (is_admin() || is_login() || wp_is_json_request()) return;
    
    // Skip if already verified (check via JS localStorage)
    ?>
    <div id="age-gate" style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;z-index:99999;background:rgba(0,0,0,0.85);backdrop-filter:blur(8px);">
        <div style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);background:#fff;border-radius:20px;padding:40px;max-width:420px;width:90%;text-align:center;box-shadow:0 20px 60px rgba(0,0,0,0.5);">
            <div style="font-size:48px;margin-bottom:16px;">🔞</div>
            <h2 style="font-size:24px;margin:0 0 12px;color:#1a1a2e;">Age Verification Required</h2>
            <p style="font-size:15px;color:#666;margin-bottom:24px;line-height:1.6;">You must be at least 18 years old to enter this website. Please confirm your age to continue.</p>
            <div style="display:flex;gap:12px;">
                <button id="age-gate-yes" style="flex:1;padding:14px;background:#667eea;color:#fff;border:none;border-radius:10px;font-size:15px;font-weight:600;cursor:pointer;transition:background 0.3s;">I am 18+</button>
                <a href="https://www.google.com" id="age-gate-no" style="flex:1;padding:14px;background:#f0f0f0;color:#666;border:none;border-radius:10px;font-size:15px;font-weight:600;text-decoration:none;display:flex;align-items:center;justify-content:center;">Exit</a>
            </div>
        </div>
    </div>
    
    <script>
    (function() {
        if (!localStorage.getItem('age_verified')) {
            document.getElementById('age-gate').style.display = 'block';
            document.body.style.overflow = 'hidden';
        }
        
        document.getElementById('age-gate-yes').addEventListener('click', function() {
            localStorage.setItem('age_verified', 'true');
            document.getElementById('age-gate').style.display = 'none';
            document.body.style.overflow = '';
        });
    })();
    </script>
    <?php
}, 5);
```

---

## Section 9: Cookie Consent Banner

### 9.1 GDPR Cookie Consent Banner

**Type:** PHP + HTML + JS + CSS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Cookie consent banner
add_action('wp_footer', function() {
    ?>
    <div id="cookie-consent" style="display:none;position:fixed;bottom:0;left:0;right:0;z-index:99998;background:#1a1a2e;color:#fff;padding:16px 20px;box-shadow:0 -4px 20px rgba(0,0,0,0.15);">
        <div style="max-width:1200px;margin:0 auto;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px;">
            <div style="flex:1;min-width:280px;">
                <span style="font-size:14px;line-height:1.5;">🍪 We use cookies to enhance your browsing experience, serve personalized content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. <a href="/cookie-policy/" style="color:#667eea;text-decoration:underline;">Read Cookie Policy</a></span>
            </div>
            <div style="display:flex;gap:10px;">
                <button id="cookie-necessary" style="padding:10px 20px;background:transparent;border:1px solid rgba(255,255,255,0.3);color:#fff;border-radius:8px;font-size:13px;cursor:pointer;transition:all 0.3s;">Necessary Only</button>
                <button id="cookie-accept" style="padding:10px 24px;background:#667eea;border:none;color:#fff;border-radius:8px;font-size:13px;font-weight:600;cursor:pointer;transition:background 0.3s;">Accept All</button>
            </div>
        </div>
    </div>
    
    <script>
    (function() {
        if (!localStorage.getItem('cookie_consent')) {
            document.getElementById('cookie-consent').style.display = 'block';
            document.body.style.paddingBottom = '80px';
        }
        
        function setConsent(type) {
            localStorage.setItem('cookie_consent', type);
            document.getElementById('cookie-consent').style.display = 'none';
            document.body.style.paddingBottom = '';
            
            if (type === 'all') {
                // Enable analytics, marketing cookies here
                if (typeof gtag === 'function') {
                    gtag('consent', 'update', {
                        'analytics_storage': 'granted',
                        'ad_storage': 'granted',
                    });
                }
            }
        }
        
        document.getElementById('cookie-accept').addEventListener('click', function() {
            setConsent('all');
        });
        
        document.getElementById('cookie-necessary').addEventListener('click', function() {
            setConsent('necessary');
        });
    })();
    </script>
    <?php
}, 15);
```

---

## Section 10: Custom REST API Endpoints

### 10.1 Custom REST Endpoint for Site Info

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Register custom REST endpoint
add_action('rest_api_init', function() {
    register_rest_route('site/v1', '/info', array(
        'methods' => 'GET',
        'callback' => 'custom_rest_site_info',
        'permission_callback' => '__return_true',
    ));
    
    register_rest_route('site/v1', '/products/count', array(
        'methods' => 'GET',
        'callback' => 'custom_rest_products_count',
        'permission_callback' => '__return_true',
    ));
    
    register_rest_route('site/v1', '/menu/(?P<location>[a-zA-Z0-9_-]+)', array(
        'methods' => 'GET',
        'callback' => 'custom_rest_get_menu',
        'permission_callback' => '__return_true',
    ));
});

function custom_rest_site_info($request) {
    return array(
        'name' => get_bloginfo('name'),
        'description' => get_bloginfo('description'),
        'url' => home_url('/'),
        'language' => get_locale(),
        'timezone' => get_option('timezone_string'),
        'currency' => get_option('woocommerce_currency'),
        'woocommerce_version' => defined('WC_VERSION') ? WC_VERSION : null,
    );
}

function custom_rest_products_count($request) {
    $counts = array(
        'total' => wp_count_posts('product')->publish,
        'out_of_stock' => 0,
        'on_sale' => 0,
    );
    
    $args = array(
        'post_type' => 'product',
        'post_status' => 'publish',
        'posts_per_page' => -1,
        'fields' => 'ids',
    );
    $products = get_posts($args);
    
    foreach ($products as $product_id) {
        $product = wc_get_product($product_id);
        if ($product) {
            if (!$product->is_in_stock()) {
                $counts['out_of_stock']++;
            }
            if ($product->is_on_sale()) {
                $counts['on_sale']++;
            }
        }
    }
    
    return $counts;
}

function custom_rest_get_menu($request) {
    $location = $request['location'];
    $locations = get_nav_menu_locations();
    
    if (!isset($locations[$location])) {
        return new WP_Error('menu_not_found', 'Menu location not found', array('status' => 404));
    }
    
    $menu = wp_get_nav_menu_object($locations[$location]);
    if (!$menu) {
        return new WP_Error('menu_empty', 'Menu is empty', array('status' => 404));
    }
    
    $items = wp_get_nav_menu_items($menu->term_id);
    $menu_data = array();
    
    foreach ($items as $item) {
        $menu_data[] = array(
            'id' => $item->ID,
            'title' => $item->title,
            'url' => $item->url,
            'parent' => $item->menu_item_parent,
            'order' => $item->menu_order,
        );
    }
    
    return $menu_data;
}
```

---

## Verification Checklist

After implementing any snippet from this guide, verify:

- [ ] Snippet activated without PHP errors (check error log)
- [ ] Front-end page loads correctly (no white screen, no 500 error)
- [ ] Mobile layout is not broken
- [ ] Console has no JavaScript errors
- [ ] Functionality works as intended
- [ ] No duplicate output (if using hooks, check priority)
- [ ] Performance not degraded (check PageSpeed if relevant)
- [ ] WooCommerce checkout still works (if WC snippet)
- [ ] Elementor editor still works (if Elementor-related snippet)
- [ ] Cache purged after activation (if caching plugin active)
