# SiteGround Server Bypass and Handling Guide

## Overview

SiteGround is one of the most popular WordPress hosting providers. Many sites built with this skill run on SiteGround. SiteGround implements several security and performance layers that can interfere with automated WordPress operations. This reference defines how the agent must detect, handle, and bypass these challenges without switching to alternative methods.

## CRITICAL: No Skipping Allowed

Every step in this guide must be executed carefully and in order. The agent MUST NOT:
- Skip a step because it seems unnecessary.
- Switch to an alternative method because a step is difficult.
- Ignore a SiteGround challenge and proceed as if nothing happened.
- Assume a challenge will resolve itself.

If a SiteGround challenge is encountered, the agent must follow the handling procedure for that specific challenge type. Only after the challenge is resolved may the agent continue.

## SiteGround Security and Performance Layers

### 1. Bot Detection and CAPTCHA Challenges

SiteGround's WAF may display CAPTCHA challenges or interstitial pages when it detects automated access patterns. This is most common during:
- Rapid wp-admin login attempts.
- Multiple consecutive REST API calls.
- Repeated form submissions.
- Unusual request patterns (fast clicks, no mouse movement).

#### Detection Signs
- Browser shows a CAPTCHA page (hCaptcha, reCAPTCHA, or custom challenge).
- Page title contains "Attention Required" or "Verifying you are human".
- HTTP 403 with a challenge page body.
- Page redirects to a verification URL.
- JavaScript-based challenge that takes 3-5 seconds before redirecting.

#### Handling Procedure
1. **STOP all automation immediately.** Do not retry or refresh.
2. **Notify the user**: "SiteGround is showing a verification challenge. I need you to complete the CAPTCHA in the browser."
3. **Wait for the user to manually solve the CAPTCHA** in the browser window.
4. **After the user confirms** they solved it, wait 10 seconds for the challenge cookie to set.
5. **Resume the operation from the step that was interrupted.** Do not restart from the beginning.
6. **Slow down subsequent operations**: Add 2-3 second delays between automated actions to avoid triggering another challenge.
7. **Log the challenge occurrence** in the site build log for future reference.

#### Prevention
- Add random delays (2-5 seconds) between wp-admin actions.
- Use REST API with application passwords instead of browser automation when possible (API calls are less likely to trigger CAPTCHA).
- Avoid rapid consecutive page loads or form submissions.
- Use realistic mouse movement patterns if using browser automation.
- Limit concurrent requests to 1 at a time.

### 2. IP Blocking and Rate Limiting

SiteGround may temporarily block an IP address after too many failed login attempts or suspicious requests.

#### Detection Signs
- HTTP 403 Forbidden with SiteGround error page.
- "Access denied" or "Your IP has been blocked" message.
- Connection timeout or reset.
- wp-admin returns 403 but frontend works.

#### Handling Procedure
1. **STOP all automation immediately.**
2. **Notify the user**: "Your IP address appears to be blocked by SiteGround. This can happen due to rapid automated access."
3. **Provide unblock options to the user**:
   - Option A: Wait 15-30 minutes for the temporary block to expire.
   - Option B: Log into SiteGround Site Tools → Security → Blocked IPs → Remove the blocked IP.
   - Option C: Contact SiteGround support via live chat to request unblocking.
   - Option D: Use a VPN or different network to access the site.
4. **After the block is lifted**, resume from the interrupted step.
5. **Reduce request frequency**: Switch to REST API with application passwords to minimize browser-based requests.
6. **If using REST API and still blocked**: Add a Code Snippet to whitelist the agent's IP:
   ```php
   // Add to Code Snippets temporarily
   add_filter('siteground_security_whitelist_ip', function($ips) {
       $ips[] = 'AGENT_IP_HERE'; // Replace with actual IP
       return $ips;
   });
   ```

#### Prevention
- Use application passwords for REST API instead of browser login.
- Add 3-5 second delays between automated actions.
- Avoid more than 10 consecutive wp-admin page loads without a pause.
- Batch operations: Create multiple pages via a single REST API call instead of multiple browser navigations.
- If the agent's IP is known, ask the user to whitelist it in SiteGround Site Tools.

### 3. SiteGround Optimizer Caching (SG Optimizer)

SiteGround's built-in caching plugin (SiteGround Optimizer) can serve stale content during automated operations, making it appear that changes did not take effect.

#### Detection Signs
- Page changes are not visible on the frontend after saving in wp-admin.
- PageSpeed Insights shows old content.
- Elementor changes don't appear after Update.
- REST API returns updated data but frontend shows old content.

#### Handling Procedure
1. **After any content change** (page update, product import, snippet activation), purge the SG Optimizer cache:
   - Method A (browser): SiteGround Optimizer → Purge SG Cache.
   - Method B (REST API): Not directly available; use the snippet below.
   - Method C (Code Snippet): Add a persistent snippet that purges cache on post save:
     ```php
     add_action('save_post', function() {
         if (function_exists('sg_cachepress_purge_cache')) {
             sg_cachepress_purge_cache();
         }
     });
     ```
2. **Also purge browser cache**: Hard refresh (Ctrl+Shift+R) on the frontend.
3. **Wait 5 seconds** after purging before checking the frontend.
4. **Verify the change is visible** before proceeding to the next step.

#### SG Optimizer Settings to Configure
When setting up the site, configure SG Optimizer for compatibility:
- **Dynamic Caching**: Enable (but purge after changes).
- **File-Based Caching**: Enable for static pages.
- **Memcached**: Enable for database caching.
- **HTTPS Enforce**: Enable.
- **PHP Version**: Set to 8.1+.
- **Gzip Compression**: Enable.
- **Browser Caching**: Enable.
- **CSS Minify**: Enable (but test with Elementor).
- **JS Minify**: Enable (but test with Elementor).
- **Defer Render-Blocking JavaScript**: Enable.
- **Combine CSS/JS**: DISABLE (can break Elementor pages).
- **Remove Query Strings**: DISABLE (can break cache busting).
- **Database Optimization**: Run periodically.

#### Critical SG Optimizer Rules
- Do NOT enable "Combine CSS Files" — it breaks Elementor's optimized CSS loading.
- Do NOT enable "Remove Query Strings from Static Resources" — breaks cache busting.
- Always purge cache after making changes.
- Test Elementor pages after enabling any SG Optimizer feature.

### 4. SiteGround WAF (Web Application Firewall)

SiteGround's WAF may block requests that look suspicious, including REST API calls with certain patterns.

#### Detection Signs
- HTTP 403 on REST API calls.
- "Request blocked by firewall" message.
- REST API returns HTML error page instead of JSON.
- Specific endpoints blocked (e.g., /wp-json/wp/v2/pages).

#### Handling Procedure
1. **Check if the request was blocked by WAF**: Look for SiteGround-specific error messages in the response.
2. **Notify the user**: "SiteGround's firewall blocked an API request. I may need you to whitelist this in SiteGround."
3. **Ask the user to check SiteGround Site Tools → Security → WAF**:
   - Check if WAF is set to "Strict" — change to "Standard" if needed.
   - Check blocked requests log.
   - Add exceptions for WordPress REST API endpoints.
4. **Alternative**: Use browser-based wp-admin operations instead of REST API if WAF keeps blocking.
5. **Resume from the interrupted step** after WAF is configured.

#### WAF-Friendly Practices
- Use standard WordPress REST API endpoints (not custom paths).
- Include proper authentication headers (application passwords).
- Avoid rapid consecutive API calls (add 2-3 second delays).
- Don't send requests with unusual headers or user agents.
- Use the WordPress REST API nonce for cookie-based auth.

### 5. SiteGround PHP Limits and Timeouts

SiteGround has specific PHP limits that may cause long-running operations to fail.

#### Detection Signs
- HTTP 500 error during page save or import.
- "Maximum execution time exceeded" error.
- White screen of death during Elementor operations.
- Upload fails with size error.

#### Handling Procedure
1. **Check current PHP limits** via SiteGround Site Tools → Devs → PHP Manager:
   - `max_execution_time`: Should be 120+ (default may be 30-60).
   - `memory_limit`: Should be 512M+ (default may be 256M).
   - `upload_max_filesize`: Should be 128M+.
   - `post_max_size`: Should be 128M+.
2. **Ask the user to increase limits** if they are too low:
   - Site Tools → Devs → PHP Manager → PHP Variables → Edit.
   - Or add to `php.ini` via Site Tools.
3. **For Elementor specifically**: Ensure `WP_MEMORY_LIMIT` is at least 512M:
   ```php
   // In wp-config.php (ask user to add)
   define('WP_MEMORY_LIMIT', '512M');
   define('WP_MAX_MEMORY_LIMIT', '512M');
   ```
4. **Break large operations into smaller batches**: Import 10 products at a time instead of 100.

### 6. SiteGround Staging Environment

SiteGround offers a staging environment. If the user has staging enabled, the agent should be aware.

#### Detection Signs
- Site URL contains `.staging.` or a staging subdomain.
- SiteGround Site Tools shows a staging site.

#### Handling
- Ask the user whether to work on staging or production.
- If staging: Make all changes on staging, then push to production via SiteGround's staging push feature.
- If production: Proceed normally but be extra careful with destructive operations.
- Staging and production may have different cache states.

## SiteGround-Specific Automation Strategy

### Preferred Access Methods (in order of preference)

1. **REST API with Application Passwords** (least likely to trigger challenges):
   - Generate application password in wp-admin → Users → Profile → Application Passwords.
   - Use Basic Auth with application password for all API calls.
   - Less likely to trigger CAPTCHA or IP blocks.
   - Can batch operations.

2. **WP-CLI via SiteGround SSH** (if SSH access available):
   - SiteGround provides SSH access via Site Tools → Devs → SSH.
   - WP-CLI is pre-installed on SiteGround servers.
   - Can run bulk operations without browser overhead.
   - Fastest method for large imports.

3. **Browser automation** (most likely to trigger challenges):
   - Use when API and WP-CLI are unavailable.
   - Add delays between actions.
   - Monitor for CAPTCHA challenges.
   - Be prepared to pause for user intervention.

### Rate Limiting Strategy
- **API calls**: Maximum 5 per second, with 200ms delay between calls.
- **Browser page loads**: Maximum 1 every 3 seconds.
- **Form submissions**: Maximum 1 every 5 seconds.
- **File uploads**: Maximum 1 every 10 seconds.
- **Elementor saves**: Maximum 1 every 5 seconds (Elementor is resource-intensive).

### Error Recovery Protocol
When a SiteGround challenge or error occurs:

1. **Log the error**: Record the error type, URL, timestamp, and response.
2. **Classify the error**: CAPTCHA, IP block, WAF, cache, PHP limit, or other.
3. **Follow the specific handling procedure** for that error type.
4. **After resolution, resume from the exact step that failed.** Do not restart the entire workflow.
5. **Adjust automation speed** based on the error (slow down if challenges recur).
6. **Notify the user** of any challenges encountered and how they were resolved.

## SiteGround Site Tools Integration

### What SiteGround Site Tools Provides
- **Site → File Manager**: Browse and edit files.
- **Site → Logs**: Access and error logs.
- **Site → FTP Accounts**: FTP access.
- **Devs → PHP Manager**: PHP version and limits.
- **Devs → MySQL**: Database management.
- **Devs → SSH**: SSH access (WP-CLI available).
- **Security → Blocked IPs**: View and unblock IPs.
- **Security → WAF**: Web Application Firewall settings.
- **Speed → Caching**: SG Optimizer caching settings.
- **Speed → HTTPS Enforce**: Force HTTPS.
- **Speed → Dynamic Cache**: Dynamic caching settings.

### When to Direct the User to Site Tools
- IP blocking: Security → Blocked IPs.
- WAF configuration: Security → WAF.
- PHP limits: Devs → PHP Manager.
- Cache purge: Speed → Caching → Purge Cache.
- HTTPS enforcement: Speed → HTTPS Enforce.
- SSH access: Devs → SSH (for WP-CLI operations).
- Database access: Devs → MySQL → phpMyAdmin (for manual data cleanup).

## SiteGround Pre-Build Checklist

Before starting any build on a SiteGround-hosted site:

- [ ] Verify SiteGround hosting by checking for SG Optimizer plugin or Site Tools.
- [ ] Check if WAF is enabled and at what level (Standard or Strict).
- [ ] Check if IP is already blocked (try accessing wp-admin).
- [ ] Verify PHP version is 8.1+ in Site Tools → Devs → PHP Manager.
- [ ] Check PHP limits (max_execution_time, memory_limit, upload_max_filesize).
- [ ] Verify SSH access is available (for potential WP-CLI operations).
- [ ] Generate application password for REST API access.
- [ ] Note the SiteGround Site Tools URL for the user.
- [ ] Configure SG Optimizer settings for Elementor compatibility.
- [ ] Test a simple API call to verify WAF doesn't block it.

## Common SiteGround Issues and Quick Fixes

| Issue | Symptom | Quick Fix |
|-------|---------|-----------|
| CAPTCHA on login | Challenge page on wp-admin | Ask user to solve CAPTCHA manually |
| IP blocked | 403 on all wp-admin pages | Site Tools → Security → Blocked IPs → Remove |
| Stale cache | Changes not visible | Purge SG Cache + browser hard refresh |
| WAF blocks API | 403 on REST API | Site Tools → Security → WAF → Standard mode |
| PHP timeout | 500 on large operations | Increase max_execution_time in PHP Manager |
| Memory limit | White screen | Increase memory_limit to 512M |
| Upload too large | File upload fails | Increase upload_max_filesize |
| Combine CSS breaks | Broken Elementor styling | Disable "Combine CSS" in SG Optimizer |
| Combine JS breaks | JavaScript errors | Disable "Combine JS" in SG Optimizer |
| HTTPS redirect loop | Too many redirects | Check HTTPS Enforce and WordPress URL settings |
| wp-cron not firing | Scheduled posts not publishing | Check if SiteGround disabled wp-cron; add alternate cron |

## WP-CLI Operations on SiteGround

WP-CLI is the most reliable way to perform bulk operations on SiteGround without triggering browser-based security challenges. SiteGround pre-installs WP-CLI on all servers and provides SSH access through Site Tools.

### Establishing SSH Access
1. **Generate SSH key** in Site Tools → Devs → SSH → Generate SSH Key.
2. **Download the private key** and store it securely.
3. **Connect via SSH** using the credentials shown in Site Tools:
   ```
   ssh -i /path/to/private/key USERNAME@HOSTNAME -p 18765
   ```
4. **Navigate to the site directory** (typically `~/www/SITEDOMAIN/public_html`).
5. **Verify WP-CLI is available**: Run `wp --info` to confirm.

### Common WP-CLI Commands for Site Builds
Use these commands instead of browser automation whenever possible:

```bash
# Create a page
wp post create --post_type=page --post_title="About Us" --post_status=publish

# List all pages
wp post list --post_type=page --fields=ID,post_title,post_status

# Update a post
wp post update 123 --post_content="New content here"

# Install and activate a plugin
wp plugin install elementor --activate
wp plugin install wordpress-seo --activate

# Activate a theme
wp theme activate hello-elementor

# Import content from a WXR file
wp import /path/to/file.xml --authors=create

# Flush permalinks after structure changes
wp rewrite flush

# Update all plugins (use with caution during builds)
wp plugin update --all

# Search and replace URLs (for staging-to-production moves)
wp search-replace 'https://staging.example.com' 'https://example.com' --skip-columns=guid

# Regenerate thumbnails after image uploads
wp media regenerate --yes

# Clear all caches (if SG Optimizer CLI is available)
wp cache flush
wp sg-optimize purge-cache 2>/dev/null || wp sg purge 2>/dev/null || true
```

### WP-CLI Best Practices on SiteGround
- Always run WP-CLI from the site's `public_html` directory so it detects `wp-config.php`.
- Use `--path=/absolute/path/to/wordpress` if running from another directory.
- Avoid `--skip-themes` and `--skip-plugins` unless debugging, as it can produce misleading results.
- For large imports, increase PHP limits first (see Section 5) to avoid mid-operation timeouts.
- WP-CLI operations bypass the WAF and CAPTCHA entirely, making them ideal for bulk work.

### When WP-CLI Is Unavailable
If SSH access is not configured or the user cannot provide credentials:
1. Fall back to REST API with application passwords (Section: Automation Strategy).
2. Fall back to browser automation with careful rate limiting.
3. Document that WP-CLI was unavailable so the build log reflects the chosen method.

## SSH and SFTP File Operations

Some build tasks require direct file access that neither the REST API nor wp-admin can provide. SiteGround supports SFTP via the same SSH credentials.

### SFTP Connection Details
- **Host**: The SSH hostname from Site Tools → Devs → SSH.
- **Port**: 18765 (SiteGround's default SSH/SFTP port).
- **Username**: The SSH username from Site Tools.
- **Authentication**: SSH private key (recommended) or password.

### File Operations the Agent May Need
- Editing `wp-config.php` to add constants (memory limits, WP_DEBUG, etc.).
- Uploading a custom theme or plugin zip that is too large for the wp-admin uploader.
- Inspecting the `debug.log` file in `wp-content/` for errors.
- Editing `.htaccess` for redirect rules or security hardening.
- Removing a stuck maintenance mode file (`.maintenance`).
- Uploading a `robots.txt` or custom files to the site root.

### Safety Rules for File Editing
- Always back up a file before editing it (copy to `.bak`).
- Never edit `wp-config.php` without the user's explicit permission.
- Verify file permissions after edits: directories = 755, files = 644.
- Do not delete core WordPress files under any circumstances.
- After editing `.htaccess`, verify the site still loads to avoid 500 errors.

## SiteGround Email and SMTP Considerations

SiteGround provides email hosting alongside web hosting. WordPress sites that send transactional or notification emails rely on SiteGround's mail servers.

### Common Email Issues
- **WP Mail SMTP not configured**: WordPress default `mail()` may be unreliable on SiteGround.
- **Emails marked as spam**: SiteGround's shared IP reputation can affect deliverability.
- **Sending limits**: SiteGround enforces hourly email sending limits per mailbox.
- **SPF/DKIM/DMARC not set**: Outbound email may be rejected by major providers.

### Recommended Configuration
1. **Install WP Mail SMTP** plugin (or a comparable SMTP plugin).
2. **Use SiteGround's SMTP server**:
   - SMTP Host: `smtp.hostinger.com` is NOT correct — use the SiteGround mail server shown in Site Tools → Email → Accounts.
   - SMTP Port: 465 (SSL) or 587 (TLS).
   - Encryption: SSL or TLS.
   - Username: The full email address.
   - Password: The mailbox password set in Site Tools.
3. **Send a test email** via WP Mail SMTP's test feature to verify configuration.
4. **Configure DNS records** for SPF, DKIM, and DMARC in Site Tools → DNS Zone Editor:
   - SPF: `v=spf1 include:_spf.mail.siteground.net ~all`
   - DKIM: Enable in Site Tools → Email → Authentication.
   - DMARC: `v=DMARC1; p=quarantine; rua=mailto:admin@example.com`

### When Email Cannot Be Sent
- If SiteGround's SMTP fails, recommend a third-party SMTP provider (SMTP2GO, SendGrid, Brevo).
- Update the SMTP plugin configuration with the third-party credentials.
- Do not attempt to bypass SiteGround's sending limits — request a limit increase via support.

## SiteGround Backup and Restore

SiteGround performs automatic daily backups on most plans and keeps them for up to 30 days. The agent must understand backup handling before performing destructive operations.

### Before Any Destructive Operation
Before running any of the following, confirm a fresh backup exists:
- Bulk deletion of pages, posts, or products.
- Database cleanup or optimization scripts.
- Theme switching.
- Plugin removal in bulk.
- Search-and-replace operations on the database.
- Staging-to-production pushes.

### Creating a Manual Backup
1. **Via Site Tools**: Site Tools → Security → Backups → Create Backup.
2. **Via SSH/WP-CLI**: Export the database before destructive operations:
   ```bash
   wp db export /path/to/backup-$(date +%Y%m%d-%H%M%S).sql --add-drop-table
   ```
3. **Via Code Snippet**: Not recommended for full backups; use Site Tools or WP-CLI.

### Restoring from a Backup
1. **Via Site Tools**: Site Tools → Security → Backups → Select date → Restore.
   - This restores files and database together.
   - Restoration may take 5-15 minutes depending on site size.
2. **Via WP-CLI** (database only):
   ```bash
   wp db import /path/to/backup.sql
   ```
3. **After restoration**, purge all caches (SG Optimizer + browser) before verifying.

### Backup Limitations
- Free backup retention may be limited depending on the hosting plan.
- Manual backups via Site Tools may count toward a quota.
- Backups do not include DNS or email configuration.
- The agent must NEVER assume a backup exists — always verify first.

## SiteGround-Specific wp-config.php Configurations

The following constants are commonly needed when building on SiteGround. The agent must ask the user before modifying `wp-config.php`.

### Memory and Execution
```php
define('WP_MEMORY_LIMIT', '512M');
define('WP_MAX_MEMORY_LIMIT', '512M');
```

### Debugging (enable temporarily during builds)
```php
define('WP_DEBUG', true);
define('WP_DEBUG_LOG', true);   // Logs to wp-content/debug.log
define('WP_DEBUG_DISPLAY', false);
@ini_set('display_errors', 0);
```

### Disable WordPress cron (use SiteGround's server cron instead)
```php
define('DISABLE_WP_CRON', true);
```
Then add a real cron job in Site Tools → Devs → Cron Jobs:
```
*/5 * * * * wget -q -O - https://example.com/wp-cron.php?doing_wp_cron >/dev/null 2>&1
```

### Force SSL Admin
```php
define('FORCE_SSL_ADMIN', true);
```

### Revision Control (reduce database bloat)
```php
define('WP_POST_REVISIONS', 5);
define('AUTOSAVE_INTERVAL', 300); // seconds
```

### Important Notes
- SiteGround's staging environments use a different `wp-config.php` — changes on staging do not auto-propagate.
- Always place constants above the `/* That's all, stop editing! */` line.
- Do not duplicate constants that already exist — edit them in place.

## SiteGround Migration Considerations

If the agent is building on a site that was recently migrated to SiteGround, or if a staging-to-production migration is needed, additional care is required.

### After a Migration to SiteGround
- Verify the site URL and home URL in Settings → General.
- Run a search-and-replace if the domain changed:
  ```bash
  wp search-replace 'https://olddomain.com' 'https://newdomain.com' --skip-columns=guid
  ```
- Flush permalinks: `wp rewrite flush`.
- Regenerate thumbnails: `wp media regenerate --yes`.
- Resave Elementor settings to regenerate CSS.
- Check that the SSL certificate is active (Site Tools → SSL → HTTPS Enforce).
- Verify the `.htaccess` file is the standard WordPress one.

### Staging-to-Production Push
1. **Create or sync staging** in Site Tools → WordPress → Staging.
2. **Make all build changes on staging** first.
3. **Test thoroughly on staging** before pushing.
4. **Push to production** via Site Tools → Staging → Push to Production.
5. **After push**: Purge all caches, verify permalinks, test forms and checkout.
6. **Note**: The push overwrites production files — ensure no recent production edits will be lost.

## SiteGround Performance Optimization

Beyond caching, SiteGround offers several performance features the agent should leverage.

### PHP Version
- Always use the latest stable PHP version (8.1 or higher) in Site Tools → Devs → PHP Manager.
- Older PHP versions are slower and may be deprecated.

### HTTP/2 and HTTP/3
- SiteGround supports HTTP/2 and HTTP/3 by default.
- No action needed, but verify the SSL certificate is active for these protocols to work.

### Cloudflare CDN Integration
- SiteGround offers a free Cloudflare integration via Site Tools → Speed → Cloudflare.
- Enable it for static asset delivery.
- After enabling, purge Cloudflare cache after content changes alongside SG cache.

### Image Optimization
- Use the SiteGround Optimizer image compression or a dedicated plugin (ShortPixel, Smush).
- Always compress images before upload when possible.
- Use WebP format for modern browsers.

### Database Optimization
- Run SG Optimizer's database cleanup periodically (Site Tools → Speed → Database Optimization).
- Remove post revisions, transients, and spam comments before a launch.
- Use WP-CLI for bulk cleanup:
  ```bash
  wp post delete $(wp post list --post_type=revision --format=ids) --force
  wp transient delete --expired
  wp comment delete $(wp comment list --status=spam --format=ids) --force
  ```

## Detailed Troubleshooting Scenarios

### Scenario A: wp-admin Login Loop on SiteGround
**Symptoms**: User logs in but is immediately redirected back to the login page.

**Causes and Fixes**:
1. **Cookies blocked**: Ensure the browser accepts cookies for the domain.
2. **Site URL mismatch**: Check `siteurl` and `home` options in the database.
3. **SG Optimizer cache**: Purge SG Cache and clear browser cookies.
4. **`.htaccess` issue**: Temporarily rename `.htaccess` and test.
5. **Plugin conflict**: Disable all plugins via WP-CLI (`wp plugin deactivate --all`) and re-enable one by one.
6. **File permissions**: Ensure `wp-content` is writable (755).

### Scenario B: Elementor Changes Not Saving
**Symptoms**: User edits in Elementor, clicks Update, but changes do not persist or do not appear on the frontend.

**Causes and Fixes**:
1. **PHP memory limit**: Increase to 512M (see Section 5).
2. **SG Optimizer cache**: Purge all caches.
3. **Elementor CSS regeneration**: Regenerate CSS in Elementor → Tools → Regenerate CSS.
4. **File permissions**: Ensure `wp-content/uploads/elementor/css` is writable.
5. **WAF blocking the save request**: Switch WAF to Standard mode.
6. **Disabled WordPress cron**: Elementor relies on cron for some tasks — verify cron is running.

### Scenario C: REST API Returns 403 Only on SiteGround
**Symptoms**: REST API calls work on other hosts but fail with 403 on SiteGround.

**Causes and Fixes**:
1. **WAF in Strict mode**: Switch to Standard in Site Tools → Security → WAF.
2. **Application password incorrect**: Regenerate the application password.
3. **User-Agent blocked**: Some WAF rules block non-browser user agents — use a standard user agent.
4. **ModSecurity rules**: Check Site Tools → Security → WAF → Blocked Requests for the specific rule ID and whitelist it.
5. **Hotlink protection**: Disable if it is interfering with API asset requests.

### Scenario D: "Error Establishing a Database Connection" on SiteGround
**Symptoms**: The site displays the database connection error.

**Causes and Fixes**:
1. **Database credentials in wp-config.php**: Verify `DB_HOST` matches the SiteGround database host (usually `localhost`).
2. **Database server down**: Check SiteGround status page; wait if it is a platform issue.
3. **Corrupted database**: Repair via `wp db repair` or phpMyAdmin.
4. **Exceeded database quota**: Check Site Tools → Devs → MySQL for quota usage.
5. **User privileges**: Verify the database user has all privileges on the database.

## SiteGround-Specific Quirks and Gotchas

- **Custom php.ini location**: SiteGround uses a per-domain php.ini accessible via Site Tools, not the server-wide one.
- **WP cron disabling**: SiteGround may disable default wp-cron for performance — always check and configure server cron.
- **Email sending limits**: Typically 100-500 emails per hour depending on the plan — use an external SMTP provider for high volume.
- **Staging database prefix**: Staging sites may use a different database prefix — do not hardcode table names.
- **File editor disabled**: Some SiteGround setups disable the theme/plugin editor in wp-admin for security — use Site Tools File Manager or SSH instead.
- **Auto-updates**: SiteGround may auto-update WordPress core — verify plugin compatibility before updates.
- **SG Optimizer and WooCommerce**: Some SG Optimizer features (like Combine JS) break WooCommerce checkout — test thoroughly.
- **Two-factor authentication**: SiteGround's 2FA is on the Site Tools account, not WordPress — do not confuse the two.
- **Caching of logged-in users**: SG Optimizer can cache logged-in user pages by mistake — verify "Do Not Cache User Roles" settings.
- **Gravatar and external requests**: SiteGround may rate-limit external HTTP requests — use a Gravatar caching plugin if avatars are slow.

## Glossary of SiteGround Terms

- **Site Tools**: SiteGround's custom control panel replacing cPanel.
- **SG Optimizer**: SiteGround's performance and caching plugin.
- **WAF**: Web Application Firewall; blocks malicious requests.
- **Dynamic Cache**: SG Optimizer's page caching for dynamic content.
- **Memcached**: In-memory object caching system available on SiteGround.
- **SiteGround CDN**: SiteGround's content delivery network integration.
- **SSH (Secure Shell)**: Encrypted protocol for server command-line access.
- **WP-CLI**: WordPress Command Line Interface for managing sites without a browser.
- **Application Password**: WordPress feature for REST API authentication without the main password.
- **Staging**: A copy of the site for testing before deploying to production.
- **Gzip Compression**: Server-side compression of responses to reduce transfer size.
- **Cloudflare Integration**: SiteGround's partnership with Cloudflare for CDN and security.
- **ModSecurity**: The underlying engine for SiteGround's WAF rules.
- **PHP Manager**: Site Tools section for managing PHP version and limits.
- **Blocked IPs**: Site Tools section listing IPs blocked by the security system.

## Final Reminders for the Agent

1. **Always identify SiteGround hosting early** in the build process so these procedures are ready.
2. **Prefer REST API and WP-CLI over browser automation** to minimize security challenge triggers.
3. **Never ignore a 403, 500, or challenge page** — follow the handling procedure immediately.
4. **Always purge cache after changes** and verify the result on the frontend.
5. **Always confirm a backup exists** before destructive operations.
6. **Communicate with the user** when manual intervention (CAPTCHA, IP unblock, WAF config) is required.
7. **Log every SiteGround-specific challenge** in the build log for future builds on the same site.
8. **Slow down when challenges recur** — speed is never more important than completing the build correctly.
9. **Test Elementor pages after any SG Optimizer change** — caching features frequently break Elementor.
10. **When in doubt, ask the user** rather than guessing — SiteGround configurations vary by plan and setup.
