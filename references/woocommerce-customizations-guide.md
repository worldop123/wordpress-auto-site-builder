# WooCommerce Customizations Guide

Practical, production-ready WooCommerce customizations implemented via Code Snippets. Every snippet is REAL, WORKING code. Read `wordpress-plugins-themes-guide.md` for option keys and `code-snippets-implementation-guide.md` for Code Snippets basics.

## Section 1: Product Page Customizations

### 1.1 Custom Product Page Layout (Trust Badges Under Price)

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add trust badges under product price on single product page
add_action('woocommerce_single_product_summary', function() {
    echo '<div class="product-trust-badges" style="display:flex;gap:16px;margin:15px 0;padding:12px 0;border-top:1px solid #eee;border-bottom:1px solid #eee;">';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">🚚 <span>Free Shipping over $100</span></div>';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">🔄 <span>30-Day Returns</span></div>';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">🔒 <span>Secure Checkout</span></div>';
    echo '</div>';
}, 11);
```

### 1.2 Product Stock Counter (Urgency)

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Display stock urgency message on single product page
add_action('woocommerce_single_product_summary', function() {
    global $product;
    
    if (!$product->managing_stock()) return;
    
    $stock = $product->get_stock_quantity();
    
    if ($stock > 0 && $stock <= 10) {
        $color = $stock <= 3 ? '#e25555' : '#ed8936';
        echo '<div class="stock-urgency" style="margin:10px 0;padding:10px 14px;background:' . $color . '15;border:1px solid ' . $color . '30;border-radius:8px;display:flex;align-items:center;gap:8px;">';
        echo '<span style="font-size:18px;">⚡</span>';
        echo '<span style="font-size:14px;color:' . $color . ';font-weight:600;">Only ' . $stock . ' left in stock — order soon!</span>';
        echo '</div>';
    }
}, 15);
```

### 1.3 Estimated Delivery Date

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Show estimated delivery date on product page
add_action('woocommerce_single_product_summary', function() {
    global $product;
    
    $min_days = 3;
    $max_days = 5;
    
    $est_start = date('M j', strtotime("+$min_days days"));
    $est_end = date('M j', strtotime("+$max_days days"));
    
    echo '<div class="estimated-delivery" style="margin:10px 0;padding:10px 14px;background:#f0f7ff;border-radius:8px;display:flex;align-items:center;gap:8px;">';
    echo '<span style="font-size:18px;">📦</span>';
    echo '<span style="font-size:14px;color:#3182ce;">Estimated delivery: <strong>' . $est_start . ' - ' . $est_end . '</strong></span>';
    echo '</div>';
}, 16);
```

### 1.4 Product Countdown Timer (Sale Price)

**Type:** PHP + JS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Show countdown timer for products on sale
add_action('woocommerce_single_product_summary', function() {
    global $product;
    
    if (!$product->is_on_sale()) return;
    
    $sale_end = '';
    if ($product->get_date_on_sale_to()) {
        $sale_end = $product->get_date_on_sale_to()->getTimestamp();
    }
    
    if (!$sale_end || $sale_end < time()) return;
    
    echo '<div id="sale-countdown" data-end="' . $sale_end . '" style="margin:15px 0;padding:16px;background:linear-gradient(135deg, #667eea15, #764ba215);border-radius:12px;text-align:center;">';
    echo '<div style="font-size:13px;font-weight:600;color:#667eea;margin-bottom:8px;text-transform:uppercase;letter-spacing:0.5px;">⚡ Sale Ends In</div>';
    echo '<div id="countdown-timer" style="font-size:28px;font-weight:700;color:#1a1a2e;font-variant-numeric:tabular-nums;">--:--:--:--</div>';
    echo '<div style="display:flex;justify-content:center;gap:12px;font-size:11px;color:#999;margin-top:4px;">';
    echo '<span>Days</span><span>Hours</span><span>Mins</span><span>Secs</span>';
    echo '</div></div>';
    
    // JS countdown
    add_action('wp_footer', function() use ($sale_end) {
        ?>
        <script>
        (function() {
            var endTimestamp = <?php echo $sale_end; ?>;
            var timerEl = document.getElementById('countdown-timer');
            if (!timerEl) return;
            
            function updateCountdown() {
                var now = Math.floor(Date.now() / 1000);
                var remaining = endTimestamp - now;
                
                if (remaining <= 0) {
                    timerEl.textContent = '00:00:00:00';
                    return;
                }
                
                var days = Math.floor(remaining / 86400);
                var hours = Math.floor((remaining % 86400) / 3600);
                var mins = Math.floor((remaining % 3600) / 60);
                var secs = remaining % 60;
                
                timerEl.textContent = 
                    String(days).padStart(2, '0') + ':' +
                    String(hours).padStart(2, '0') + ':' +
                    String(mins).padStart(2, '0') + ':' +
                    String(secs).padStart(2, '0');
            }
            
            updateCountdown();
            setInterval(updateCountdown, 1000);
        })();
        </script>
        <?php
    }, 20);
}, 12);
```

### 1.5 Product Variation Swatches (Color/Size Buttons)

**Type:** PHP + CSS + JS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Convert variation dropdowns to color/size buttons
add_action('woocommerce_variable_add_to_cart', function() {
    add_filter('woocommerce_dropdown_variation_attribute_options_html', function($html, $args) {
        $options = $args['options'];
        $product = $args['product'];
        $attribute = $args['attribute'];
        $name = $args['name'] ? $args['name'] : wc_variation_attribute_name($attribute);
        $id = $args['id'] ? $args['id'] : sanitize_title($attribute);
        $class = $args['class'];
        
        // Check if this is a color attribute
        $is_color = (stripos($attribute, 'color') !== false || stripos($attribute, 'colour') !== false);
        
        $html = '<div class="variation-swatches" data-attribute="' . esc_attr($name) . '">';
        $html .= '<div class="swatch-label" style="font-size:14px;font-weight:600;margin-bottom:8px;color:#333;">' . wc_attribute_label($attribute) . ': <span class="selected-value" style="color:#667eea;"></span></div>';
        $html .= '<div class="swatch-options" style="display:flex;flex-wrap:wrap;gap:8px;">';
        
        // Get selected value
        $selected = isset($_REQUEST[$name]) ? wc_clean(wp_unslash($_REQUEST[$name])) : $product->get_variation_default_attribute($attribute);
        
        foreach ($options as $option) {
            $is_selected = sanitize_title($option) === sanitize_title($selected);
            $option_class = 'swatch-option' . ($is_selected ? ' selected' : '');
            
            if ($is_color) {
                // Color swatch
                $color_map = array(
                    'red' => '#e25555', 'blue' => '#3182ce', 'green' => '#38a169',
                    'black' => '#1a202c', 'white' => '#f7fafc', 'yellow' => '#ecc94b',
                    'purple' => '#805ad5', 'pink' => '#ed64a6', 'orange' => '#ed8936',
                    'gray' => '#718096', 'grey' => '#718096', 'brown' => '#8B4513',
                );
                $bg_color = isset($color_map[strtolower($option)]) ? $color_map[strtolower($option)] : '#ccc';
                
                $html .= '<button type="button" class="' . $option_class . '" data-value="' . esc_attr($option) . '" style="width:36px;height:36px;border-radius:50%;border:2px solid ' . ($is_selected ? '#667eea' : '#ddd') . ';background:' . $bg_color . ';cursor:pointer;padding:0;transition:all 0.2s;position:relative;" title="' . esc_attr($option) . '">';
                if ($is_selected) {
                    $html .= '<span style="position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#fff;font-size:16px;">✓</span>';
                }
                $html .= '</button>';
            } else {
                // Size/text swatch
                $html .= '<button type="button" class="' . $option_class . '" data-value="' . esc_attr($option) . '" style="min-width:44px;height:44px;padding:0 12px;border:2px solid ' . ($is_selected ? '#667eea' : '#ddd') . ';border-radius:8px;background:' . ($is_selected ? '#667eea' : '#fff') . ';color:' . ($is_selected ? '#fff' : '#333') . ';cursor:pointer;font-size:14px;font-weight:600;transition:all 0.2s;">' . esc_html($option) . '</button>';
            }
        }
        
        $html .= '</div>';
        
        // Hidden select for WooCommerce compatibility
        $html .= '<select id="' . esc_attr($id) . '" class="' . esc_attr($class) . '" name="' . esc_attr($name) . '" data-attribute_name="' . esc_attr($name) . '" data-show_option_none="' . (isset($args['show_option_none']) ? 'yes' : 'no') . '" style="display:none;">';
        if ($args['show_option_none']) {
            $html .= '<option value="">' . esc_html($args['show_option_none']) . '</option>';
        }
        foreach ($options as $option) {
            $html .= '<option value="' . esc_attr($option) . '" ' . selected(sanitize_title($selected), sanitize_title($option), false) . '>' . esc_html($option) . '</option>';
        }
        $html .= '</select></div>';
        
        return $html;
    }, 20, 2);
}, 5);

// JS for swatch interaction
add_action('wp_footer', function() {
    if (!is_product()) return;
    ?>
    <script>
    (function() {
        document.querySelectorAll('.variation-swatches').forEach(function(swatches) {
            var hiddenSelect = swatches.querySelector('select');
            var label = swatches.querySelector('.selected-value');
            
            swatches.querySelectorAll('.swatch-option').forEach(function(btn) {
                btn.addEventListener('click', function() {
                    var value = this.getAttribute('data-value');
                    
                    // Update visual state
                    swatches.querySelectorAll('.swatch-option').forEach(function(opt) {
                        opt.classList.remove('selected');
                        if (opt.classList.contains('swatch-color') || opt.style.borderRadius === '50%' || opt.style.width === '36px') {
                            opt.style.borderColor = '#ddd';
                            var checkmark = opt.querySelector('span');
                            if (checkmark) checkmark.remove();
                        } else {
                            opt.style.borderColor = '#ddd';
                            opt.style.background = '#fff';
                            opt.style.color = '#333';
                        }
                    });
                    
                    // Mark this as selected
                    this.classList.add('selected');
                    if (this.style.borderRadius === '50%' || this.style.width === '36px') {
                        this.style.borderColor = '#667eea';
                        var check = document.createElement('span');
                        check.style.cssText = 'position:absolute;top:50%;left:50%;transform:translate(-50%,-50%);color:#fff;font-size:16px;';
                        check.textContent = '✓';
                        this.appendChild(check);
                    } else {
                        this.style.borderColor = '#667eea';
                        this.style.background = '#667eea';
                        this.style.color = '#fff';
                    }
                    
                    // Update hidden select and trigger WooCommerce variation update
                    hiddenSelect.value = value;
                    hiddenSelect.dispatchEvent(new Event('change', {bubbles: true}));
                    
                    // Update label
                    if (label) label.textContent = value;
                });
            });
        });
    })();
    </script>
    <?php
}, 20);
```

### 1.6 Sticky Add to Cart Bar on Mobile

**Type:** PHP + CSS + JS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Sticky add-to-cart bar on mobile (appears when scrolling past main button)
add_action('woocommerce_after_single_product', function() {
    global $product;
    if (!$product) return;
    
    $product_id = $product->get_id();
    $product_name = $product->get_name();
    $price_html = $product->get_price_html();
    $is_simple = $product->is_type('simple');
    $in_stock = $product->is_in_stock();
    $add_to_cart_url = $is_simple && $in_stock ? '?add-to-cart=' . $product_id : get_permalink($product_id);
    $button_text = $is_simple && $in_stock ? 'Add to Cart' : 'View Options';
    
    echo '<div id="sticky-add-to-cart" style="position:fixed;bottom:0;left:0;right:0;z-index:999;background:#fff;box-shadow:0 -4px 20px rgba(0,0,0,0.1);padding:12px 16px;display:none;align-items:center;gap:12px;border-top:1px solid #eee;">';
    echo '<div style="flex:1;min-width:0;">';
    echo '<div style="font-size:13px;color:#666;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">' . esc_html($product_name) . '</div>';
    echo '<div style="font-size:16px;font-weight:700;color:#333;">' . $price_html . '</div>';
    echo '</div>';
    echo '<a href="' . esc_url($add_to_cart_url) . '" class="button" style="padding:12px 24px;background:#667eea;color:#fff;text-decoration:none;border-radius:8px;font-weight:600;font-size:14px;white-space:nowrap;">' . $button_text . '</a>';
    echo '</div>';
    
    // Show on mobile when scrolled past main add to cart
    ?>
    <script>
    (function() {
        var stickyBar = document.getElementById('sticky-add-to-cart');
        var addToCartForm = document.querySelector('form.cart');
        
        if (!stickyBar || !addToCartForm) return;
        
        function checkPosition() {
            var rect = addToCartForm.getBoundingClientRect();
            var isMobile = window.innerWidth <= 768;
            
            if (isMobile && rect.bottom < 0) {
                stickyBar.style.display = 'flex';
                document.body.style.paddingBottom = '70px';
            } else {
                stickyBar.style.display = 'none';
                document.body.style.paddingBottom = '';
            }
        }
        
        window.addEventListener('scroll', checkPosition);
        window.addEventListener('resize', checkPosition);
    })();
    </script>
    <?php
});
```

---

## Section 2: Cart Customizations

### 2.0 Safe Quantity +/- Controls for Product and Cart Pages

**Type:** PHP + CSS + JS | **Scope:** Front-end | **Lifecycle:** persistent / ux_polish

Use this pattern when adding +/- controls. It preserves WooCommerce's original quantity input and does NOT auto-submit the cart form, because automatic cart submission can create repeated reloads, blocked UI, or frozen browser sessions on plugin-heavy stores.

Rules:

- Keep the original `<input class="qty">`; wrap/enhance it with JS only.
- Do not move the original input into a new wrapper if inserting buttons before/after it inside `.quantity` is enough.
- Respect `min`, `max`, and `step`.
- Product page +/- changes the quantity only; the customer still clicks Add to cart.
- Cart page +/- changes the quantity and enables the native "Update cart" button. Do not auto-click it unless a separate AJAX updater has been tested on that exact site.
- Do not use a body-wide `MutationObserver` that calls the enhancer after every DOM mutation. Re-enhance only on `DOMContentLoaded`, `pageshow`, and WooCommerce cart update events such as `updated_cart_totals`.
- Do not sync unrelated header/cart DOM from the stepper click handler; keep the handler small and non-blocking.
- Test on simple products, variable products, cart desktop, and cart mobile.

```php
add_action('wp_head', function() {
    if (!is_product() && !is_cart()) return;
    ?>
    <style>
    .quantity.site-qty-stepper{display:inline-grid!important;grid-template-columns:44px minmax(58px,72px) 44px;align-items:center;border:1px solid #e6e9ee;border-radius:8px;overflow:hidden;background:#fff}
    .quantity.site-qty-stepper .qty{width:100%!important;height:44px!important;border:0!important;border-left:1px solid #e6e9ee!important;border-right:1px solid #e6e9ee!important;text-align:center!important;font-weight:700!important;box-shadow:none!important}
    .site-qty-btn{width:44px;height:44px;border:0;background:#f7fafb;font-size:20px;font-weight:800;cursor:pointer}
    .site-qty-btn:hover,.site-qty-btn:focus{background:#00a7a7;color:#fff}
    </style>
    <?php
});

add_action('wp_footer', function() {
    if (!is_product() && !is_cart()) return;
    ?>
    <script>
    (function(){
      function enhance(input){
        if (!input || input.dataset.siteStepper === '1') return;
        var parent = input.closest('.quantity');
        if (!parent || parent.classList.contains('site-qty-stepper')) return;
        input.dataset.siteStepper = '1';
        parent.classList.add('site-qty-stepper');
        var minus = document.createElement('button');
        minus.type = 'button'; minus.className = 'site-qty-btn site-qty-minus'; minus.textContent = '-';
        var plus = document.createElement('button');
        plus.type = 'button'; plus.className = 'site-qty-btn site-qty-plus'; plus.textContent = '+';
        parent.insertBefore(minus, input);
        parent.appendChild(plus);
      }
      function apply(){ document.querySelectorAll('.quantity input.qty').forEach(enhance); }
      function clamp(value, min, max){ if(!isNaN(min)) value = Math.max(value, min); if(!isNaN(max) && max > 0) value = Math.min(value, max); return value; }
      document.addEventListener('click', function(e){
        var btn = e.target.closest('.site-qty-btn'); if(!btn) return;
        var input = btn.closest('.site-qty-stepper').querySelector('input.qty');
        var step = parseFloat(input.getAttribute('step')) || 1;
        var min = parseFloat(input.getAttribute('min'));
        var max = parseFloat(input.getAttribute('max'));
        var current = parseFloat(input.value); if(isNaN(current)) current = isNaN(min) ? 0 : min;
        input.value = clamp(current + (btn.classList.contains('site-qty-plus') ? step : -step), min, max);
        input.dispatchEvent(new Event('change', {bubbles:true}));
        if (document.body.classList.contains('woocommerce-cart')) {
          var update = document.querySelector('button[name="update_cart"]');
          if (update) update.disabled = false;
        }
      });
      if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', apply); else apply();
      window.addEventListener('pageshow', apply);
      if (window.jQuery) jQuery(document.body).on('updated_cart_totals wc_fragments_refreshed', apply);
    })();
    </script>
    <?php
});
```

### 2.1 Cross-Sell Products in Cart

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Display cross-sell products below cart
add_action('woocommerce_cart_collaterals', function() {
    $cross_sells = array();
    $cart_items = WC()->cart->get_cart();
    
    foreach ($cart_items as $item) {
        $product_id = $item['product_id'];
        $cross_sells = array_merge($cross_sells, wc_get_product($product_id)->get_cross_sell_ids());
    }
    
    $cross_sells = array_unique($cross_sells);
    $cross_sells = array_diff($cross_sells, array_column($cart_items, 'product_id'));
    
    if (empty($cross_sells)) return;
    
    echo '<div class="cart-cross-sells" style="margin-top:30px;">';
    echo '<h3 style="font-size:20px;margin-bottom:20px;">You May Also Like</h3>';
    echo do_shortcode('[products columns="4" ids="' . implode(',', array_slice($cross_sells, 0, 4)) . '"]');
    echo '</div>';
}, 10);

// Remove default cross-sells (to replace with our version)
remove_action('woocommerce_cart_collaterals', 'woocommerce_cross_sell_display');
```

### 2.2 Cart Item Custom Display (Product Thumbnail + Attributes)

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Customize cart item display with product attributes
add_filter('woocommerce_cart_item_name', function($product_name, $cart_item, $cart_item_key) {
    if (!is_checkout()) {
        return $product_name;
    }
    
    // On checkout, show a more compact product name
    $product = $cart_item['data'];
    $thumbnail = $product->get_image(array(50, 50), array('style' => 'float:left;margin-right:10px;border-radius:6px;'));
    
    return $thumbnail . '<span style="display:block;font-weight:600;">' . $product->get_name() . '</span>' . wc_get_formatted_cart_item_data($cart_item);
}, 10, 3);
```

### 2.3 Empty Cart Custom Message

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Custom empty cart message
add_action('woocommerce_cart_is_empty', function() {
    echo '<div style="text-align:center;padding:60px 20px;">';
    echo '<div style="font-size:64px;margin-bottom:20px;">🛒</div>';
    echo '<h2 style="font-size:24px;color:#333;margin-bottom:10px;">Your Cart is Empty</h2>';
    echo '<p style="color:#666;margin-bottom:24px;">Looks like you haven\'t added any products yet.</p>';
    echo '<a href="' . esc_url(get_permalink(wc_get_page_id('shop'))) . '" style="display:inline-block;padding:14px 32px;background:#667eea;color:#fff;text-decoration:none;border-radius:10px;font-weight:600;font-size:15px;transition:background 0.3s;" onmouseover="this.style.background=\'#5568d3\'" onmouseout="this.style.background=\'#667eea\'">Continue Shopping</a>';
    echo '</div>';
    
    // Show some featured products to encourage shopping
    echo '<div style="max-width:1200px;margin:40px auto;padding:0 20px;">';
    echo '<h3 style="text-align:center;margin-bottom:24px;">Popular Products</h3>';
    echo do_shortcode('[products columns="4" limit="4" orderby="popularity"]');
    echo '</div>';
}, 5);

// Remove default empty cart message
remove_action('woocommerce_cart_is_empty', 'wc_empty_cart_message', 10);
```

---

## Section 3: Checkout Customizations

### 3.1 Two-Column Checkout Layout (Billing + Order Summary)

**Type:** PHP + CSS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Two-column checkout layout
add_action('woocommerce_checkout_before_customer_details', function() {
    echo '<div class="checkout-two-column" style="display:grid;grid-template-columns:1fr 1fr;gap:30px;max-width:1200px;margin:0 auto;">';
    echo '<div class="checkout-left" style="min-width:0;">';
});

add_action('woocommerce_checkout_after_customer_details', function() {
    echo '</div>'; // Close .checkout-left
    echo '<div class="checkout-right" style="min-width:0;">';
    echo '<div style="position:sticky;top:20px;">';
});

add_action('woocommerce_checkout_after_order_review', function() {
    echo '</div>'; // Close sticky wrapper
    echo '</div>'; // Close .checkout-right
    echo '</div>'; // Close .checkout-two-column
});

// CSS for responsive
add_action('wp_head', function() {
    if (!is_checkout()) return;
    echo '<style>
    @media (max-width: 768px) {
        .checkout-two-column {
            grid-template-columns: 1fr !important;
            gap: 20px !important;
        }
        .checkout-right > div {
            position: static !important;
        }
    }
    </style>';
}, 20);
```

### 3.2 Order Notes and Trust Signals in Checkout

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add trust signals above checkout form
add_action('woocommerce_before_checkout_form', function() {
    echo '<div class="checkout-trust-bar" style="display:flex;justify-content:center;gap:24px;padding:16px;background:#f8f9fa;border-radius:12px;margin-bottom:24px;flex-wrap:wrap;">';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">🔒 <span>SSL Secured</span></div>';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">🚚 <span>Fast Shipping</span></div>';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">🔄 <span>30-Day Returns</span></div>';
    echo '<div style="display:flex;align-items:center;gap:6px;font-size:13px;color:#555;">💳 <span>Secure Payment</span></div>';
    echo '</div>';
}, 5);

// Add order summary note below place order button
add_action('woocommerce_review_order_after_submit', function() {
    echo '<p style="text-align:center;font-size:12px;color:#999;margin-top:12px;">By placing your order, you agree to our <a href="/terms-and-conditions/" style="color:#667eea;">Terms of Service</a> and <a href="/privacy-policy/" style="color:#667eea;">Privacy Policy</a>.</p>';
});
```

### 3.3 Phone Field Validation

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Validate phone number format
add_action('woocommerce_checkout_process', function() {
    if (isset($_POST['billing_phone']) && !empty($_POST['billing_phone'])) {
        $phone = sanitize_text_field($_POST['billing_phone']);
        // Allow +, -, spaces, parentheses, and digits
        $cleaned = preg_replace('/[\s\-\(\)]/', '', $phone);
        if (!preg_match('/^\+?[0-9]{7,15}$/', $cleaned)) {
            wc_add_notice('Please enter a valid phone number (7-15 digits).', 'error');
        }
    }
});
```

### 3.4 Custom Thank You Page Content

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Custom thank you page with order details and next steps
add_action('woocommerce_thankyou', function($order_id) {
    if (!$order_id) return;
    
    $order = wc_get_order($order_id);
    $order_number = $order->get_order_number();
    $order_total = $order->get_formatted_order_total();
    $customer_name = $order->get_billing_first_name();
    $estimated_delivery = date('M j', strtotime('+3 days')) . ' - ' . date('M j', strtotime('+5 days'));
    
    echo '<div class="thank-you-custom" style="max-width:600px;margin:0 auto;padding:20px;">';
    
    // Success header
    echo '<div style="text-align:center;margin-bottom:30px;">';
    echo '<div style="width:64px;height:64px;background:#38a169;border-radius:50%;display:flex;align-items:center;justify-content:center;margin:0 auto 16px;font-size:32px;color:#fff;">✓</div>';
    echo '<h1 style="font-size:28px;color:#1a1a2e;margin:0 0 8px;">Thank You, ' . esc_html($customer_name) . '!</h1>';
    echo '<p style="color:#666;font-size:15px;margin:0;">Your order has been placed successfully.</p>';
    echo '</div>';
    
    // Order summary
    echo '<div style="background:#f8f9fa;border-radius:12px;padding:24px;margin-bottom:20px;">';
    echo '<div style="display:flex;justify-content:space-between;margin-bottom:12px;font-size:14px;"><span style="color:#666;">Order Number:</span><strong>#' . esc_html($order_number) . '</strong></div>';
    echo '<div style="display:flex;justify-content:space-between;margin-bottom:12px;font-size:14px;"><span style="color:#666;">Total:</span><strong>' . $order_total . '</strong></div>';
    echo '<div style="display:flex;justify-content:space-between;font-size:14px;"><span style="color:#666;">Estimated Delivery:</span><strong>' . $estimated_delivery . '</strong></div>';
    echo '</div>';
    
    // Next steps
    echo '<h3 style="font-size:16px;margin:20px 0 12px;">What happens next?</h3>';
    echo '<div style="display:flex;flex-direction:column;gap:12px;">';
    echo '<div style="display:flex;gap:12px;align-items:start;font-size:14px;color:#555;"><span style="font-size:20px;flex-shrink:0;">📧</span><span>You\'ll receive an order confirmation email shortly at <strong>' . esc_html($order->get_billing_email()) . '</strong></span></div>';
    echo '<div style="display:flex;gap:12px;align-items:start;font-size:14px;color:#555;"><span style="font-size:20px;flex-shrink:0;">📦</span><span>We\'ll send you a tracking number once your order ships</span></div>';
    echo '<div style="display:flex;gap:12px;align-items:start;font-size:14px;color:#555;"><span style="font-size:20px;flex-shrink:0;">🚚</span><span>Expect delivery between <strong>' . $estimated_delivery . '</strong></span></div>';
    echo '</div>';
    
    // Actions
    echo '<div style="display:flex;gap:12px;margin-top:30px;justify-content:center;">';
    echo '<a href="' . esc_url(get_permalink(wc_get_page_id('shop'))) . '" style="padding:12px 24px;background:#667eea;color:#fff;text-decoration:none;border-radius:8px;font-weight:600;font-size:14px;">Continue Shopping</a>';
    echo '<a href="' . esc_url(get_permalink(wc_get_page_id('myaccount'))) . '" style="padding:12px 24px;background:#fff;color:#667eea;border:2px solid #667eea;text-decoration:none;border-radius:8px;font-weight:600;font-size:14px;">View Order</a>';
    echo '</div>';
    
    echo '</div>';
    
    // Remove default WooCommerce thank you content (we replaced it)
    remove_action('woocommerce_thankyou', 'woocommerce_order_details_table', 10);
}, 5);
```

---

## Section 4: WooCommerce Email Customizations

### 4.1 Add Logo to Email Header

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Add custom logo to WooCommerce email header
add_filter('woocommerce_email_header_image', function() {
    $logo_id = get_theme_mod('custom_logo');
    if ($logo_id) {
        return wp_get_attachment_image_url($logo_id, 'full');
    }
    return '';
});
```

### 4.2 Custom Email for First-Time Customers

**Type:** PHP | **Scope:** Global | **Lifecycle:** persistent

```php
// Send welcome email to first-time customers
add_action('woocommerce_checkout_order_processed', function($order_id) {
    $order = wc_get_order($order_id);
    $customer_email = $order->get_billing_email();
    
    // Check if this is the customer's first order
    $customer_orders = wc_get_orders(array(
        'customer' => $customer_email,
        'status' => array('wc-completed', 'wc-processing'),
        'limit' => 2,
    ));
    
    if (count($customer_orders) === 1) {
        // First order — send welcome email
        $subject = 'Welcome to ' . get_bloginfo('name') . '! 🎉';
        $message = '<h2>Welcome to the family, ' . $order->get_billing_first_name() . '!</h2>';
        $message .= '<p>Thank you for your first order! We\'re thrilled to have you as a customer.</p>';
        $message .= '<p>Here\'s what you can expect:</p>';
        $message .= '<ul><li>Order confirmation email (already sent)</li>';
        $message .= '<li>Shipping notification with tracking number</li>';
        $message .= '<li>30-day return guarantee if you\'re not satisfied</li></ul>';
        $message .= '<p>Use code <strong>WELCOME10</strong> for 10% off your next order!</p>';
        $message .= '<p>Cheers,<br>The ' . get_bloginfo('name') . ' Team</p>';
        
        $headers = array('Content-Type: text/html; charset=UTF-8');
        wp_mail($customer_email, $subject, $message, $headers);
    }
});
```

---

## Section 5: WooCommerce Product Loop Customizations

### 5.1 Add "Sale" Badge with Custom Styling

**Type:** PHP + CSS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Replace default sale flash with custom styled badge
remove_action('woocommerce_before_shop_loop_item_title', 'woocommerce_show_product_loop_sale_flash', 10);

add_action('woocommerce_before_shop_loop_item_title', function() {
    global $product;
    
    if (!$product->is_on_sale()) return;
    
    $regular_price = $product->get_regular_price();
    $sale_price = $product->get_sale_price();
    
    if ($regular_price && $sale_price && $regular_price > 0) {
        $discount = round((($regular_price - $sale_price) / $regular_price) * 100);
        echo '<span class="custom-sale-badge" style="position:absolute;top:10px;left:10px;background:linear-gradient(135deg, #e25555, #c53030);color:#fff;padding:4px 12px;border-radius:6px;font-size:12px;font-weight:700;z-index:2;box-shadow:0 2px 8px rgba(229,85,85,0.4);">-' . $discount . '%</span>';
    }
}, 10);

// Add sale badge for variable products
add_filter('woocommerce_sale_flash', function($html, $post, $product) {
    if ($product->is_type('variable')) {
        $prices = $product->get_variation_prices();
        $regular = min($prices['regular_price']);
        $sale = min($prices['sale_price']);
        if ($regular > $sale) {
            $discount = round((($regular - $sale) / $regular) * 100);
            return '<span class="onsale" style="background:linear-gradient(135deg, #e25555, #c53030);">-' . $discount . '%</span>';
        }
    }
    return $html;
}, 10, 3);
```

### 5.2 Product Loop: Quick View Button

**Type:** PHP + JS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Add quick view button to product loop
add_action('woocommerce_after_shop_loop_item', function() {
    global $product;
    echo '<a href="' . esc_url($product->get_permalink()) . '" class="quick-view-btn" data-product-id="' . $product->get_id() . '" style="display:block;text-align:center;padding:8px;margin-top:8px;border:1px solid #ddd;border-radius:6px;font-size:13px;color:#667eea;text-decoration:none;transition:all 0.2s;" onmouseover="this.style.background=\'#667eea\';this.style.color=\'#fff\';" onmouseout="this.style.background=\'\';this.style.color=\'#667eea\';">Quick View</a>';
}, 15);
```

### 5.3 Infinite Scroll for Shop Archive

**Type:** PHP + JS | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Infinite scroll for WooCommerce shop
add_action('woocommerce_after_shop_loop', function() {
    global $wp_query;
    
    if ($wp_query->max_num_pages <= 1) return;
    
    echo '<div id="infinite-scroll-loading" style="text-align:center;padding:30px;display:none;">';
    echo '<div style="display:inline-block;width:32px;height:32px;border:3px solid #eee;border-top-color:#667eea;border-radius:50%;animation:spin 0.8s linear infinite;"></div>';
    echo '<style>@keyframes spin{to{transform:rotate(360deg);}}</style>';
    echo '</div>';
    
    echo '<button id="load-more-products" data-page="1" data-max="' . $wp_query->max_num_pages . '" style="display:block;margin:20px auto;padding:12px 32px;background:#667eea;color:#fff;border:none;border-radius:8px;font-weight:600;font-size:14px;cursor:pointer;transition:background 0.3s;" onmouseover="this.style.background=\'#5568d3\'" onmouseout="this.style.background=\'#667eea\'">Load More Products</button>';
    
    ?>
    <script>
    (function() {
        var button = document.getElementById('load-more-products');
        var loading = document.getElementById('infinite-scroll-loading');
        if (!button) return;
        
        var currentPage = 1;
        var maxPage = parseInt(button.dataset.max);
        var loadingState = false;
        
        button.addEventListener('click', function() {
            if (loadingState || currentPage >= maxPage) return;
            
            loadingState = true;
            button.style.display = 'none';
            loading.style.display = 'block';
            currentPage++;
            
            var url = new URL(window.location.href);
            url.searchParams.set('paged', currentPage);
            
            fetch(url.toString())
                .then(function(response) { return response.text(); })
                .then(function(html) {
                    var parser = new DOMParser();
                    var doc = parser.parseFromString(html, 'text/html');
                    var newProducts = doc.querySelectorAll('ul.products li.product');
                    var productsContainer = document.querySelector('ul.products');
                    
                    newProducts.forEach(function(product) {
                        productsContainer.appendChild(product);
                    });
                    
                    loadingState = false;
                    loading.style.display = 'none';
                    
                    if (currentPage < maxPage) {
                        button.style.display = 'block';
                    } else {
                        button.style.display = 'none';
                    }
                })
                .catch(function() {
                    loadingState = false;
                    loading.style.display = 'none';
                    button.style.display = 'block';
                });
        });
    })();
    </script>
    <?php
});
```

---

## Section 6: WooCommerce Account Page Customizations

### 6.1 Custom Account Dashboard

**Type:** PHP | **Scope:** Front-end | **Lifecycle:** persistent

```php
// Custom my-account dashboard
add_action('woocommerce_account_dashboard', function() {
    $user_id = get_current_user_id();
    $customer = new WC_Customer($user_id);
    $order_count = $customer->get_order_count();
    $total_spent = $customer->get_total_spent();
    $last_order = wc_get_customer_last_order($user_id);
    
    echo '<div class="account-dashboard" style="margin-bottom:30px;">';
    echo '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:16px;margin-bottom:24px;">';
    
    // Total orders
    echo '<div style="background:#f8f9fa;border-radius:12px;padding:20px;text-align:center;">';
    echo '<div style="font-size:28px;font-weight:700;color:#667eea;">' . $order_count . '</div>';
    echo '<div style="font-size:13px;color:#666;">Total Orders</div>';
    echo '</div>';
    
    // Total spent
    echo '<div style="background:#f8f9fa;border-radius:12px;padding:20px;text-align:center;">';
    echo '<div style="font-size:28px;font-weight:700;color:#38a169;">' . wc_price($total_spent) . '</div>';
    echo '<div style="font-size:13px;color:#666;">Total Spent</div>';
    echo '</div>';
    
    // Last order
    if ($last_order) {
        echo '<div style="background:#f8f9fa;border-radius:12px;padding:20px;text-align:center;">';
        echo '<div style="font-size:16px;font-weight:700;color:#333;">#' . $last_order->get_order_number() . '</div>';
        echo '<div style="font-size:13px;color:#666;">Last Order (' . $last_order->get_status() . ')</div>';
        echo '</div>';
    }
    
    echo '</div>';
    
    // Quick links
    echo '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;">';
    echo '<a href="/my-account/orders/" style="display:flex;align-items:center;gap:12px;padding:16px;background:#fff;border:1px solid #eee;border-radius:10px;text-decoration:none;color:#333;transition:border-color 0.2s;" onmouseover="this.style.borderColor=\'#667eea\'" onmouseout="this.style.borderColor=\'#eee\'">';
    echo '<span style="font-size:24px;">📦</span><div><div style="font-weight:600;font-size:14px;">My Orders</div><div style="font-size:12px;color:#999;">Track and manage</div></div></a>';
    
    echo '<a href="/my-account/edit-address/" style="display:flex;align-items:center;gap:12px;padding:16px;background:#fff;border:1px solid #eee;border-radius:10px;text-decoration:none;color:#333;transition:border-color 0.2s;" onmouseover="this.style.borderColor=\'#667eea\'" onmouseout="this.style.borderColor=\'#eee\'">';
    echo '<span style="font-size:24px;">📍</span><div><div style="font-weight:600;font-size:14px;">Addresses</div><div style="font-size:12px;color:#999;">Manage addresses</div></div></a>';
    
    echo '<a href="/my-account/edit-account/" style="display:flex;align-items:center;gap:12px;padding:16px;background:#fff;border:1px solid #eee;border-radius:10px;text-decoration:none;color:#333;transition:border-color 0.2s;" onmouseover="this.style.borderColor=\'#667eea\'" onmouseout="this.style.borderColor=\'#eee\'">';
    echo '<span style="font-size:24px;">👤</span><div><div style="font-weight:600;font-size:14px;">Account Details</div><div style="font-size:12px;color:#999;">Update profile</div></div></a>';
    
    echo '</div></div>';
}, 5);
```

---

## Verification Checklist

After implementing any WooCommerce customization, verify:

- [ ] Product page loads without errors
- [ ] Add to cart button works (AJAX and non-AJAX)
- [ ] Variation selection updates price and stock
- [ ] Cart page displays correctly
- [ ] Checkout flow works end-to-end
- [ ] Order confirmation email is sent
- [ ] My Account page loads correctly
- [ ] Mobile layout is not broken
- [ ] No JavaScript console errors
- [ ] No PHP warnings or errors in log
- [ ] WooCommerce status shows no conflicts
- [ ] Elementor editor still works on WooCommerce pages
- [ ] Cache purged after snippet activation
- [ ] SiteGround SG Optimizer cache purged (if applicable)
