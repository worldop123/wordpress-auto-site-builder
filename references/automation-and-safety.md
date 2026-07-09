# Automation and Safety

## Credentials

- Do not echo passwords, API secrets, application passwords, or cookies.
- Do not store credentials in generated skill files, reports, snippets, or memory.
- Prefer temporary admin accounts, application passwords, or user-guided browser login.
- If using shell commands, pass secrets through environment variables where possible.

## Live site change policy

Before broad live edits:

- Inspect existing state.
- Identify pages/snippets/products that must be preserved.
- Make backups or export snippets/pages when practical.
- Use draft or inactive snippets first when testing risky code.

## Snippet lifecycle

Classify every Code Snippets item:

- `persistent`: keep enabled long-term, for shell, product UX, checkout rules, compliance gate.
- `ux_polish`: keep enabled only if it improves UI and has a clear rollback.
- `one_time_writer`: enable once, run, verify, then disable.
- `read_only_scanner`: enable/run only for diagnostics, then disable.
- `deprecated`: do not enable; keep only for historical reference or delete after backup.

Each snippet file should include:

- Name.
- Lifecycle.
- Purpose.
- Keep enabled: yes/no.
- Rollback: which snippet to disable.
- Dependencies: WooCommerce, Rank Math, Elementor, etc.

## API vs admin UI

Use API for:

- Creating/updating posts, pages, products, categories, metadata, and media when available.
- Reading site state.

Use wp-admin/browser for:

- Elementor HTML paste operations.
- Code Snippets plugin screens.
- WooCommerce settings screens blocked by API limits.
- Sites with WAF/API restrictions.

Use manual `.md` delivery for:

- User prefers copy-paste.
- CAPTCHA/2FA blocks automation.
- Production risk is too high.

## Rollback

For every functional layer, define rollback:

- Disable the snippet.
- Clear cache.
- Save permalinks if routes changed.
- Re-test affected URL.

Avoid editing theme files directly unless the user explicitly wants a child theme approach.

## SiteGround hosting handling

Many sites built with this skill run on SiteGround. SiteGround implements security and performance layers that can interfere with automated operations. Read `siteground-bypass-guide.md` for the complete handling guide.

### Detection

Detect SiteGround hosting during environment inspection by checking for:
- SG Optimizer plugin active.
- Site Tools references in wp-admin.
- Server software headers indicating SiteGround infrastructure.
- DNS or IP lookups pointing to SiteGround ranges.

### Handling challenges

- **CAPTCHA or verification challenge**: STOP all automation immediately. Do NOT retry or refresh. Notify the user and wait for manual resolution.
- **IP blocked by WAF**: Notify the user. Provide unblock instructions: Site Tools → Security → Blocked IPs. Alternatively, wait 15-30 minutes for temporary blocks to expire.
- **WAF blocks API calls**: Ask user to set WAF to Standard mode in Site Tools → Security → WAF Configuration. Do NOT switch to alternative access methods — follow the procedure.
- **Rate limiting**: Add 2-5 second delays between automated actions. Reduce batch sizes. Use REST API with application passwords instead of browser automation where possible.
- **SG Optimizer cache not purging**: Manually purge via Site Tools → Devs → Caching, or SG Optimizer dashboard. Purge after every content change.

### SG Optimizer configuration for Elementor

When SiteGround is detected, configure SG Optimizer as follows:
- **Enable**: Dynamic Cache, Memcached, HTTPS Enforce, Gzip Compression, Browser Caching, CSS Minify, JS Minify, Defer Render-blocking JS, Combine Google Fonts, Remove Query Strings.
- **Do NOT enable**: Combine CSS Files, Combine JavaScript Files (these break Elementor).
- **Frontend Optimizations**: Enable Defer Non-essential JavaScript, Disable WordPress Emojis.
- **Environment Optimizations**: Set PHP version to 8.1+, Increase PHP Memory Limit to 512MB, Increase Max Execution Time to 300.

### Prevention strategies

- Use REST API with application passwords as the preferred access method (less likely to trigger bot detection than browser automation).
- Add delays between automated actions (2-5 seconds).
- Avoid rapid sequential requests. Batch operations with pauses.
- Do NOT use aggressive scraping or rapid page refreshes.
- If a challenge appears once, slow down all subsequent operations.
- Never retry a failed request more than 2 times before notifying the user.

### Critical rule

Do NOT switch to alternative methods when encountering SiteGround challenges. Follow the defined handling procedure in `siteground-bypass-guide.md`. If a step fails, fix the issue and retry that specific step.
