# Old Site Rebuild Procedure

## Overview

When the user wants to rebuild an existing WordPress site (not a new build), the agent must follow this procedure to clean up old data and rebuild the site. This is a destructive operation — every step must be executed carefully and in order. No step may be skipped.

### Purpose and Scope

This procedure applies when:
- The user already has a live WordPress + WooCommerce site.
- The user wants to rebuild the site design, structure, and configuration.
- The user wants to keep their existing product catalog and media library.
- The user has explicitly confirmed they want to rebuild (not start fresh on a new domain).

This procedure does NOT apply when:
- The user is building a brand-new site on a fresh WordPress install (use the standard build workflow instead).
- The user only wants minor edits to an existing site (use targeted edits, not a full rebuild).
- The user wants to migrate to a new server or domain (use a migration tool, not this procedure).

### Guiding Principles

- **Safety first**: Backups and verification come before any deletion.
- **Preserve product data**: Products and media are the only things that must survive cleanup.
- **Clean slate for rebuild**: Everything else is cleared so the rebuild starts from a known, clean state.
- **No shortcuts**: Each step exists for a reason. Skipping causes cascading errors during rebuild.

## CRITICAL: No Skipping Allowed

This is a HARD RULE. Every step in this procedure must be executed in the exact order specified. The agent MUST NOT:
- Skip a step because it seems unnecessary.
- Combine steps to save time.
- Reorder steps for convenience.
- Skip verification after a step.
- Switch to an alternative method because a step is difficult.
- Assume a step was completed without verifying.

If any step fails, STOP, fix the issue, and retry that step before moving to the next.

### Failure Handling

If a step fails:
1. Stop immediately. Do not attempt the next step.
2. Diagnose the failure (permissions, plugin conflict, network error, etc.).
3. Fix the root cause.
4. Retry the failed step from the beginning.
5. Only proceed to the next step after the failed step succeeds and is verified.

If a step fails repeatedly and cannot be resolved:
1. Inform the user of the failure and the cause.
2. Do NOT continue cleanup with a failed step unresolved.
3. Consider restoring from the backup taken in the Pre-Cleanup Checklist.
4. Document the failure for troubleshooting.

## What Is Preserved vs What Is Cleared

### PRESERVED (Do NOT Delete)
- WooCommerce products (all product data: titles, descriptions, prices, SKUs, variations, images, attributes).
- WooCommerce product categories and tags.
- Media library images (all files in wp-content/uploads/).
- Product image associations (product-to-image mappings).
- WooCommerce product attributes and attribute terms.

### CLEARED (Delete All)
- All WordPress pages (except WooCommerce-owned: Shop, Cart, Checkout, My Account).
- All WordPress blog posts/articles.
- All WordPress menus (primary, footer, mobile).
- All WordPress categories (blog categories, not product categories).
- All WordPress tags (blog tags, not product tags).
- All Code Snippets (deactivate and delete all existing snippets).
- All Elementor data and templates.
- All widgets and widget area assignments.
- All theme customizer settings (reset to defaults).
- All WordPress custom CSS (Additional CSS).
- All transients and cache.
- All WooCommerce settings (will be reconfigured).
- All shipping zones, shipping methods, shipping classes.
- All tax rates and tax classes.
- All payment gateway configurations.
- All email/SMTP settings.
- All orders and customer data (unless user explicitly requests to keep).
- All coupons and promotions.
- All WordPress users except the current admin.
- All plugins settings (except WooCommerce product data).

## Pre-Cleanup Checklist

Before starting cleanup, the agent MUST:

1. **Confirm with the user**: "This will delete all pages, blog posts, menus, snippets, and settings on your site. Only WooCommerce products and media library images will be preserved. Are you sure you want to continue?"
2. **Wait for explicit user confirmation** ("yes", "confirm", "proceed").
3. **Export a backup**: 
   - Export all WordPress content (Tools → Export → All Content).
   - Export WooCommerce products (WooCommerce → Products → Export).
   - Note: This backup is for safety — the user can restore if something goes wrong.
4. **Document current state**:
   - List all existing pages (titles, slugs, IDs).
   - List all existing blog posts (titles, slugs, IDs).
   - List all existing menus (names, locations).
   - List all active Code Snippets (names, descriptions).
   - List WooCommerce settings (currency, shipping zones, payment methods).
   - Take screenshots of the current site for reference.
5. **Confirm backup is complete** before proceeding to cleanup.

### Backup Verification

After exporting backups, verify they are usable:
1. Open the WordPress XML export file and confirm it contains posts and pages.
2. Open the WooCommerce product CSV and confirm it contains all products with data.
3. Store backup files in a safe location (local download, cloud storage).
4. Note the date and time of the backup for reference.
5. If the backup is incomplete or corrupted, do NOT proceed with cleanup.

## Step-by-Step Cleanup Procedure

### Step 1: Deactivate All Code Snippets
**MUST complete before Step 2.**

1. Go to Snippets → All Snippets.
2. Deactivate EVERY snippet (one by one or bulk deactivate).
3. Verify: All snippets show as "Inactive".
4. Do NOT delete snippets yet — deactivate first to avoid errors from active snippets during cleanup.
5. **Verification**: Go to Snippets → All Snippets and confirm all are inactive.

### Step 2: Delete All Blog Posts
**MUST complete before Step 3.**

1. Go to Posts → All Posts.
2. Select all posts.
3. Move to Trash (Bulk Actions → Move to Trash).
4. Go to Trash.
5. Delete permanently (Bulk Actions → Delete Permanently).
6. **Verification**: Go to Posts → All Posts and confirm "No posts found".
7. Also check Posts → Categories: delete all blog categories (NOT product categories).
8. Also check Posts → Tags: delete all blog tags (NOT product tags).
9. **Verification**: Categories and Tags are empty.

### Step 3: Delete All Pages (Except WooCommerce-Owned)
**MUST complete before Step 4.**

1. Go to Pages → All Pages.
2. Identify WooCommerce-owned pages: Shop, Cart, Checkout, My Account. Note their IDs.
3. Select all pages EXCEPT Shop, Cart, Checkout, My Account.
4. Move to Trash (Bulk Actions → Move to Trash).
5. Go to Trash.
6. Delete permanently (Bulk Actions → Delete Permanently).
7. For WooCommerce-owned pages (Shop, Cart, Checkout, My Account):
   - Edit each page.
   - Remove any custom Elementor content (switch to Default template).
   - Ensure correct WooCommerce shortcodes are present:
     - Cart: `[woocommerce_cart]`
     - Checkout: `[woocommerce_checkout]`
     - My Account: `[woocommerce_my_account]`
   - Shop: Leave empty (WooCommerce handles the archive).
   - Update each page.
8. **Verification**: Go to Pages → All Pages and confirm only Shop, Cart, Checkout, My Account exist with correct shortcodes.

### Step 4: Delete All Menus
**MUST complete before Step 5.**

1. Go to Appearance → Menus.
2. For each existing menu:
   - Select the menu from the dropdown.
   - Scroll to bottom.
   - Click "Delete Menu".
   - Confirm deletion.
3. Repeat until no menus remain.
4. **Verification**: Go to Appearance → Menus and confirm no menus exist.
5. Also check Manage Locations: confirm all locations are unassigned.

### Step 5: Delete All Code Snippets
**MUST complete before Step 6.**

1. Go to Snippets → All Snippets.
2. For each snippet (already deactivated in Step 1):
   - Click "Delete" or use bulk action to delete all.
   - Confirm deletion.
3. **Verification**: Go to Snippets → All Snippets and confirm "No snippets found".

### Step 6: Clear Elementor Data
**MUST complete before Step 7.**

1. Go to Elementor → Tools.
2. Click "Regenerate CSS" (clears Elementor's cached CSS).
3. Go to Elementor → System Info.
4. Click "Regenerate Data" if available.
5. If there are Elementor templates: Go to Templates → Saved Templates and delete all.
6. Clear Elementor cache: Elementor → Tools → Clear Cache.
7. **Verification**: Check that no Elementor templates remain.

### Step 7: Clear Theme Customizer Settings
**MUST complete before Step 8.**

1. Go to Appearance → Customize.
2. Navigate to Additional CSS.
3. Delete ALL content in the Additional CSS textarea.
4. Publish/Save.
5. Check other Customizer sections:
   - Site Identity: Note logo and site title (will be reconfigured).
   - Colors: Reset to defaults if possible.
   - Typography: Reset to defaults if possible.
   - Any other custom settings: Reset or note for reconfiguration.
6. **Verification**: Go to Appearance → Customize → Additional CSS and confirm it is empty.

### Step 8: Clear Widgets
**MUST complete before Step 9.**

1. Go to Appearance → Widgets.
2. Remove all widgets from all widget areas (sidebar, footer widgets, etc.).
3. Move each widget out of its area or delete.
4. **Verification**: Go to Appearance → Widgets and confirm all areas are empty.

### Step 9: Clear WooCommerce Settings (Keep Products)
**MUST complete before Step 10.**

1. Go to WooCommerce → Settings → General:
   - Note current currency, store location (for reconfiguration).
   - Reset to defaults (or note values for reconfiguration).
2. Go to WooCommerce → Settings → Shipping:
   - Delete all shipping zones.
   - **Verification**: No shipping zones remain.
3. Go to WooCommerce → Settings → Tax:
   - Delete all tax rates.
   - **Verification**: No tax rates remain.
4. Go to WooCommerce → Settings → Payments:
   - Disable all payment methods.
   - **Verification**: All payment methods disabled.
5. Go to WooCommerce → Settings → Emails:
   - Note email settings (for reconfiguration).
   - Do not delete email templates, but note they need reconfiguration.
6. Go to WooCommerce → Coupons:
   - Delete all coupons if any exist.
   - **Verification**: No coupons remain.
7. **CRITICAL**: Do NOT touch WooCommerce → Products. Product data must remain intact.
8. **Verification**: Go to WooCommerce → Products and confirm all products are still present.

### Step 10: Clear Orders and Customers (If Applicable)
**MUST complete before Step 11.**

1. Go to WooCommerce → Orders.
2. If orders exist:
   - Ask user: "Do you want to delete all existing orders? This cannot be undone."
   - If yes: Move all orders to Trash, then delete permanently.
   - If no: Skip this step.
3. Go to Users → All Users.
4. Remove all users except the current admin account and any shop managers.
   - Ask user before deleting any users.
5. **Verification**: Confirm only admin/essential users remain.

### Step 11: Clear Cache and Transients
**MUST complete before Step 12.**

1. If using SiteGround Optimizer: Purge SG Cache.
2. If using WP Rocket or other cache plugin: Clear all cache.
3. If using a CDN (Cloudflare): Purge CDN cache.
4. Clear browser cache (hard refresh).
5. Go to Tools → Site Health → Info → Database and note database size.
6. Optionally: Use a database optimization plugin to clean transients and revisions.
7. **Verification**: Visit the site homepage and confirm it shows a blank/default state.

### Step 12: Verify Product Data Integrity
**MUST complete before proceeding to rebuild.**

1. Go to WooCommerce → Products.
2. Confirm all products are still present and published.
3. Check a sample product:
   - Title, description, short description intact.
   - Price, SKU, stock status intact.
   - Product images and gallery intact.
   - Product categories and tags intact.
   - Product attributes and variations intact.
4. Go to WooCommerce → Products → Categories.
5. Confirm all product categories are present.
6. Go to WooCommerce → Attributes.
7. Confirm all product attributes are present.
8. Go to Media → Library.
9. Confirm all media files are still present.
10. **If any product data is missing**: STOP and inform the user. Do NOT proceed to rebuild.
11. **If all product data is intact**: Proceed to rebuild.

### Step 13: Export Product CSV for Rewriting (Optional)
If the user wants to rewrite product titles/descriptions/SEO:
1. Go to WooCommerce → Products → Export.
2. Export all products as CSV.
3. Save the CSV for the rewriting process (see `product-csv-originality-seo.md`).
4. This CSV will be rewritten and re-imported after the site is rebuilt.

### CSV Export Notes

- Include all columns (ID, Type, SKU, Name, Published, Visibility, etc.).
- Export both published and draft products.
- Do NOT manually edit the CSV before the rewriting process.
- Keep the original CSV untouched — the rewriting process creates a new version.
- If the store has variations, ensure the CSV includes variation rows.

## Post-Cleanup: Ready for Rebuild

After all 13 steps are complete, the site should be in a clean state:
- No pages (except WooCommerce-owned with default shortcodes).
- No blog posts.
- No menus.
- No Code Snippets.
- No Elementor templates.
- No custom CSS.
- No widgets.
- No WooCommerce settings (to be reconfigured).
- No shipping zones, tax rates, or payment methods.
- No orders or coupons.
- Products and media library are intact.

The site is now ready for the standard build workflow starting from Phase 0 (Prerequisite Check) in `phase-playbook.md`.

## Rebuild After Cleanup

After cleanup is verified, follow the standard build workflow:

1. **Phase 0**: Prerequisite check (verify plugins, theme, SSL, PHP).
2. **Phase 1**: Requirements and site_config (ask user for design, market, language, etc.).
3. **Phase 2**: Environment inspection (confirm clean state).
4. **Phase 3**: Page creation and binding (create new pages, set WooCommerce bindings). **DEAD RULE: After cleanup, WooCommerce page bindings may be broken. The agent MUST regenerate WooCommerce pages (WooCommerce → Status → Tools → "Install pages") and rebind ALL page IDs via Code Snippets PHP. This is mandatory for old site rebuilds — see `agent-enforcement-rules.md` Section 11.4.**
5. **Phase 4**: Products (products already exist — verify, optionally rewrite via CSV).
6. **Phase 5**: Global shell (create new header/footer/CSS/JS via global architecture — see `global-shell-architecture.md`). **DEAD RULE: Global shell MUST be active and verified BEFORE any page HTML is imported — see `agent-enforcement-rules.md` Section 11.7.**
7. **Phase 6**: Page HTML (generate page-specific HTML without header/footer). **DEAD RULE: Set Elementor Canvas on EVERY custom page BEFORE pasting HTML. Use batch import for large HTML. Homepage/Blog MUST use dynamic data containers. Import one page at a time — see `agent-enforcement-rules.md` Sections 11.1, 11.3, 11.5, 11.7.**
8. Continue with standard phases (7-13).

## Troubleshooting Common Issues

### Issue: Cannot Delete All Posts at Once
- Some hosts limit bulk operations. Delete in batches of 50-100.
- If a post is stuck in Trash, use the WP-CLI command: `wp post delete $(wp post list --post_type=post --format=ids) --force`.

### Issue: Code Snippets Plugin Not Installed
- If the Code Snippets plugin is not installed, skip Steps 1 and 5.
- Document this in the cleanup log so the rebuild team knows snippets were not present.

### Issue: Elementor Data Won't Clear
- If "Regenerate CSS" fails, try deactivating and reactivating the Elementor plugin.
- If Elementor templates persist, check the database `wp_postmeta` for `_elementor_data` entries.

### Issue: WooCommerce Settings Won't Reset
- If settings cannot be reset via UI, note current values and reconfigure manually during rebuild.
- Do NOT use database queries to delete WooCommerce settings — this risks product data.

### Issue: Product Data Accidentally Deleted
- STOP immediately.
- Inform the user.
- Restore products from the WooCommerce CSV backup exported in Pre-Cleanup.
- Re-verify product data integrity (Step 12) before proceeding.

### Issue: Media Library Shows Broken Images
- Check file permissions on `wp-content/uploads/`.
- Do NOT delete media files to "fix" broken images.
- Run a media regeneration plugin if thumbnails are missing.

## Rollback Procedure

If cleanup must be reversed (rare, only if product data is at risk):

1. Stop all cleanup activity immediately.
2. Inform the user that a rollback is being attempted.
3. Restore the WordPress XML export (Tools → Import → WordPress).
4. Re-import the WooCommerce product CSV (WooCommerce → Products → Import).
5. Verify product data integrity.
6. Note: Pages, posts, menus, and settings restored from XML may need manual cleanup.
7. Rollback is a last resort — prevention through careful step execution is preferred.

## Important Notes

- **Every step must be verified before moving to the next.** Do not assume a step worked.
- **If any step fails, stop and fix it.** Do not continue with partial cleanup.
- **Product data is sacred.** If any product data is lost during cleanup, stop immediately and inform the user.
- **Media library is sacred.** Do not delete any files in wp-content/uploads/.
- **The user must confirm before cleanup begins.** Do not start cleanup without explicit user approval.
- **Back up before cleanup.** Always export content before deleting anything.
- **Do not rush.** Each step takes time. Completing thoroughly is more important than completing quickly.
