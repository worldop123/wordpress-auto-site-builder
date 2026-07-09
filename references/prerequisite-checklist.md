# Prerequisite Checklist - Mandatory Pre-Build Verification

## Overview
Before ANY site building work begins, the agent MUST verify that all required plugins, themes, and configurations are properly installed and activated. This is a HARD GATE — no build work proceeds until all prerequisites are met. The agent must inform the user of any missing items and provide installation instructions.

## Startup Sequence (Mandatory)

When the skill is activated, the agent MUST perform these steps in order:

### Step 1: Announce Prerequisite Check
Tell the user:
"I need to verify that your WordPress site has all required plugins and themes before we begin building. Let me check your site's current state."

### Step 2: WordPress Access Verification
- Verify WordPress admin URL is accessible
- Verify login credentials work (or guide user through browser login)
- If access fails, STOP and ask user for correct credentials

### Step 3: Theme Check - Hello Elementor
**Required**: Hello Elementor theme must be installed and activated.

Check method:
- Go to Appearance → Themes
- Look for "Hello Elementor" in active themes
- If not active: Install and activate Hello Elementor

Installation instructions for user:
1. WordPress Admin → Appearance → Themes → Add New
2. Search "Hello Elementor"
3. Click Install, then Activate
4. Or download from: https://wordpress.org/themes/hello-elementor/

If user has a different theme and wants to keep it:
- Ask user to confirm they want to use a different theme
- Verify the theme is compatible with Elementor
- Document the theme choice in site_config
- Do NOT proceed without user confirmation

### Step 4: Rank Math SEO Plugin Check
**Required**: Rank Math SEO plugin must be installed and activated.

Check method:
- Go to Plugins → Installed Plugins
- Look for "Rank Math" or "Rank Math SEO"
- Verify it is activated (not just installed)

If not installed:
1. Tell user: "Rank Math SEO is required for this build. Please install it:"
2. WordPress Admin → Plugins → Add New
3. Search "Rank Math" or "Rank Math SEO"
4. Click Install, then Activate
5. Direct link: https://wordpress.org/plugins/seo-by-rank-math/
6. Official site: https://rankmath.com/

If user has Pro version:
1. Download Rank Math Pro from https://rankmath.com/ (login required)
2. WordPress Admin → Plugins → Add New → Upload Plugin
3. Upload the Pro .zip file
4. Activate and connect Rank Math account

After installation:
- Run Rank Math Setup Wizard (Advanced mode recommended)
- On first use for a site, tell the user to connect the relevant Rank Math account in the setup wizard or Rank Math account settings.
- Record the Rank Math account state as `connected`, `user_skipped`, or `blocked`. If the user skips connection, continue with local SEO setup but note unavailable account-based features such as Analytics, PRO modules, or account services.
- Configure basic settings
- See `rank-math-seo-guide.md` for detailed configuration

### Step 5: Elementor Plugin Check
**Required**: Elementor (free) must be installed and activated.

Check method:
- Go to Plugins → Installed Plugins
- Look for "Elementor"
- Verify it is activated

If not installed:
1. WordPress Admin → Plugins → Add New
2. Search "Elementor"
3. Click Install, then Activate
4. Direct link: https://wordpress.org/plugins/elementor/

Optional but recommended: Elementor Pro
- Adds: Theme Builder, Popup Builder, WooCommerce Builder, Form widget
- If user has Elementor Pro, verify it is also activated
- Elementor Pro is NOT required for basic builds using HTML widgets

### Step 6: WooCommerce Plugin Check (for ecommerce sites)
**Required for ecommerce**: WooCommerce must be installed and activated.

Check method:
- Go to Plugins → Installed Plugins
- Look for "WooCommerce"
- Verify it is activated
- Check if WooCommerce setup wizard has been completed

If not installed:
1. WordPress Admin → Plugins → Add New
2. Search "WooCommerce"
3. Click Install, then Activate
4. Direct link: https://wordpress.org/plugins/woocommerce/
5. Complete WooCommerce setup wizard (currency, store location, etc.)

WooCommerce setup checklist:
- [ ] Store currency set
- [ ] Store address configured
- [ ] Shipping zones configured (or marked as launch blocker)
- [ ] Payment methods configured (or marked as launch blocker)
- [ ] WooCommerce pages created (Shop, Cart, Checkout, My Account)

### Step 7: Code Snippets Plugin Check
**Required**: Code Snippets plugin must be installed and activated.

Check method:
- Go to Plugins → Installed Plugins
- Look for "Code Snippets"
- Verify it is activated

If not installed:
1. WordPress Admin → Plugins → Add New
2. Search "Code Snippets"
3. Click Install, then Activate
4. Direct link: https://wordpress.org/plugins/code-snippets/

### Step 8: Cache Plugin Check
**Recommended**: A caching plugin should be installed for performance.

Mode-specific Code Snippets rule:
- For `new` and `old_rebuild` site builds, Code Snippets is a required foundation dependency for global shell, WooCommerce bindings, UX snippets, and one-time writers.
- For `existing_seo_optimization`, do not change the theme or rebuild pages. Code Snippets is still required for Rank Math Free one-time metadata writers and SEO repair snippets.
- If Code Snippets is missing and `interaction_mode` is `autonomous`, or explicit plugin-install permission is recorded, install and activate Code Snippets automatically, then record plugin version and installer account.
- If Code Snippets is missing in `ask_user` mode without permission, pause and ask for approval or provide manual installation steps. Do not write Rank Math bulk metadata before this is resolved.

Recommended options:
- WP Rocket (premium, best features)
- LiteSpeed Cache (free, excellent if on LiteSpeed server)
- W3 Total Cache (free, comprehensive)
- WP Super Cache (free, simple)

If no cache plugin:
- Warn user that site performance will be suboptimal
- Recommend installing a cache plugin
- Proceed with build but note as launch blocker

### Step 9: SSL/HTTPS Verification
**Required**: Site must be accessible via HTTPS.

Check method:
- Visit site URL with https:// prefix
- Verify SSL certificate is valid (no browser warnings)
- Check WordPress Settings → General → Site URL uses https://

If no SSL:
- Tell user: "Your site does not have SSL/HTTPS. This is critical for SEO and security."
- Recommend installing SSL certificate (Let's Encrypt is free)
- Most hosts offer free SSL via cPanel or control panel
- Mark as launch blocker

### Step 10: PHP Version Check
**Required**: PHP 8.0 or higher (8.1+ recommended).

Check method:
- Go to Tools → Site Health → Info → Server
- Check PHP version
- Alternatively: check via hosting control panel

If PHP < 8.0:
- Warn user: "Your PHP version is outdated. PHP 8.0+ is required for performance and security."
- Recommend upgrading via hosting control panel
- Mark as warning (build can proceed but performance will suffer)

## Prerequisite Summary Checklist

Print this checklist for the user before proceeding:

```
=== PREREQUISITE CHECK ===
[ ] WordPress accessible and login works
[ ] Hello Elementor theme activated
[ ] Rank Math SEO plugin installed and activated
[ ] Rank Math account connection prompted on first use; result recorded (`connected`, `user_skipped`, or `blocked`)
[ ] Elementor plugin installed and activated
[ ] WooCommerce installed and activated (ecommerce only)
[ ] WooCommerce setup wizard completed (ecommerce only)
[ ] Code Snippets plugin installed and activated
[ ] Cache plugin installed (recommended)
[ ] SSL/HTTPS enabled
[ ] PHP 8.0+ (8.1+ recommended)
=== END PREREQUISITE CHECK ===
```

## Handling Missing Prerequisites

### If Rank Math is missing
- STOP the build
- Tell user: "Rank Math SEO is required for this build. Please install it from Plugins → Add New, search 'Rank Math', or visit https://rankmath.com/"
- Provide step-by-step installation instructions
- Wait for user confirmation before proceeding
- Do NOT proceed with a different SEO plugin unless user explicitly requests it

### If Hello Elementor is not active
- STOP the build
- Tell user: "Hello Elementor theme is required. Please activate it from Appearance → Themes"
- If user wants a different theme, ask for explicit confirmation
- Verify alternative theme is Elementor-compatible
- Document the theme choice

### If WooCommerce is missing (for ecommerce builds)
- STOP the build
- Tell user: "WooCommerce is required for ecommerce sites. Please install it from Plugins → Add New, search 'WooCommerce'"
- Wait for WooCommerce setup wizard completion

### If Elementor is missing
- STOP the build
- Tell user: "Elementor is required for page building. Please install it from Plugins → Add New, search 'Elementor'"
- Wait for user confirmation

### If Code Snippets is missing
- STOP the build
- Tell user: "Code Snippets is required for functional implementation. Please install it from Plugins → Add New, search 'Code Snippets'"

Mode-specific Code Snippets missing handling:
- In `autonomous` mode or with explicit plugin-install permission, install and activate Code Snippets, then verify it appears in Plugins and its admin menu is available.
- In `ask_user` mode without permission, keep the task paused until the user installs it or approves automatic installation.
- For existing-site SEO optimization, do not substitute another snippet/plugin mechanism unless the user explicitly approves a different implementation.

## Existing-Site SEO Optimization Prerequisite Variant

When `site.build_mode` is `existing_seo_optimization`, verify the site as-is before any write action:

- [ ] Service mode recorded as `existing_seo_optimization`.
- [ ] Current theme, page builder, menus, slugs, products, prices, stock, checkout, payment, and shipping will be preserved.
- [ ] Rank Math installed and active; first-use account connection prompt/result recorded.
- [ ] Code Snippets installed/activated, or automatic install authorization recorded.
- [ ] Read-only SEO inventory can access pages, products, posts, categories/tags, media, current Rank Math meta, robots/noindex, sitemap, schema, and internal links.
- [ ] Strong existing human-written SEO metadata preservation rule recorded unless user authorized overwrite.

Hello Elementor, Elementor, and WooCommerce are observed in this mode but must not be forced or replaced if the existing site uses a different working stack. Only require WooCommerce for ecommerce SEO scopes that include products/categories.

## Post-Prerequisite Configuration

After all prerequisites are met, configure baseline settings before page creation:

1. **Permalinks**: Set to `/%postname%/` (Settings → Permalinks)
2. **Reading Settings**: Set homepage and posts page
3. **WooCommerce**: Bind Shop, Cart, Checkout, My Account pages
4. **Rank Math**: Enable Advanced Mode, configure baseline settings
5. **Elementor**: Enable Flexbox Containers, optimize settings
6. **Menus**: Create primary and footer menu placeholders

See `site-baseline-and-menus.md` for detailed baseline configuration instructions.

## User Communication Protocol

When prerequisites are missing, the agent must:
1. Clearly state what is missing
2. Provide exact installation steps
3. Provide direct download links
4. Wait for user to complete installation
5. Re-verify after user says it's done
6. Only proceed when ALL prerequisites pass

The agent must NOT:
- Skip prerequisite checks
- Proceed with missing required plugins
- Install plugins without user permission
- Assume plugins are installed without verifying
- Use alternative plugins without user approval

## Interaction Example

Agent: "I need to verify your site has all required plugins before we begin. Let me check."

[After checking...]

Agent: "Prerequisite check results:
✅ WordPress accessible
✅ Hello Elementor theme active
❌ Rank Math SEO - NOT installed
✅ Elementor - active
✅ WooCommerce - active
✅ Code Snippets - active
✅ SSL/HTTPS - enabled
✅ PHP 8.1

Rank Math SEO is required for this build. Please install it:
1. Go to Plugins → Add New
2. Search 'Rank Math'
3. Click Install, then Activate
4. Or download from https://rankmath.com/

Once installed, let me know and I'll continue the setup."

[Wait for user response before proceeding]
