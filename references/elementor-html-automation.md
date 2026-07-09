# Elementor HTML Automation

Use this reference when the agent must create pages, open Elementor, set the page layout to Elementor Canvas, add an HTML widget, paste generated HTML, and update the page.

## DEAD RULE: Elementor Canvas Is Mandatory (No Exceptions)

**This is a DEAD RULE. The agent MUST NOT skip, delay, or forget this step. No exceptions. No excuses.**

Every custom page created with Elementor MUST have its Page Layout set to `Elementor Canvas` BEFORE pasting any HTML into the HTML widget. If the agent pastes HTML without first setting Canvas, the page is broken and must be fixed immediately.

### Why This Is a Dead Rule

Hello Elementor theme loads its default header, footer, and menu on EVERY page by default. The function `hello_elementor_display_header_footer()` returns `true` by default, and the theme enqueues `header-footer.css` on every page. The ONLY way to remove these default elements is to set the page layout to `Elementor Canvas`.

If Canvas is NOT set:
1. **Hello Elementor's default header appears** — duplicates the global header from Code Snippets.
2. **Hello Elementor's default footer appears** — duplicates the global footer from Code Snippets.
3. **Hello Elementor's default menu appears** — duplicates the global navigation.
4. **The page layout is broken** — theme CSS conflicts with page-specific CSS.
5. **The global shell architecture is broken** — two headers, two footers, two menus.

### Enforcement Procedure

1. **Create the page** (or open existing page).
2. **Open Elementor editor** for that page.
3. **Set Page Layout to Elementor Canvas** — this step MUST be completed BEFORE adding any HTML widget. See the "Set Page Layout to Elementor Canvas" section below for exact UI steps.
4. **Click Update/Save** to persist the Canvas setting.
5. **Verify Canvas is set** — reload the front-end page URL. If the theme's default header/footer/menu still appears, Canvas was NOT set correctly. Fix before proceeding.
6. **ONLY THEN** add the HTML widget and paste page content.
7. **Record in page ledger**: `"canvas_set": true` — only after verification passes.

### Pages That MUST Use Elementor Canvas

Use Elementor Canvas for ALL custom visual pages:

- Home.
- Blog landing page if it is a designed page with dynamic post container.
- Contact.
- About.
- FAQ.
- Policy pages when custom visual layout is desired.
- Age/compliance information page.
- Landing pages.

### Pages That MUST NOT Use Elementor Canvas

Do NOT use Elementor Canvas for WooCommerce-owned transactional pages (these use WooCommerce shortcodes and templates):

- Shop.
- Product category archives.
- Single product pages unless a reversible product UX snippet is being used instead.
- Cart.
- Checkout.
- My Account.

## DEAD RULE: Batch Import for Large HTML

**This is a DEAD RULE. When HTML payload is too large to paste in one operation, the agent MUST split it into batches. No exceptions.**

### When to Batch Import

- If the HTML payload exceeds approximately **30,000 characters** (including CSS and JS), use batch import.
- If the Elementor HTML widget paste operation fails, times out, or truncates the content, switch to batch import immediately.
- If the browser becomes unresponsive during paste, switch to batch import.

### Batch Import Procedure

1. **Split the HTML into logical sections** at natural boundaries (between `</section>` and `<section>`, or between `</div>` closing a major block and the next `<div>` opening a new block).
2. **NEVER split inside an open tag** — each batch must start and end with complete, valid HTML tags. Never split in the middle of `<div class="...">`, never split inside a `<style>` block, never split inside a `<script>` block.
3. **Batch 1 (First batch)**: Opening HTML structure + first section(s) + scoped CSS in a `<style>` block. Paste into the HTML widget. Click Update. Verify the first section renders correctly on the front-end.
4. **Batch 2-N (Subsequent batches)**: Append the next section(s) to the SAME HTML widget. Position the cursor at the end of the existing content. Paste the next batch. Click Update. Verify the new section renders correctly.
5. **Final Batch**: Last section(s) + closing HTML structure + scoped JS in a `<script>` block. Paste. Click Update. Verify the complete page renders correctly.
6. **After each batch**: Click Update in Elementor. Open the front-end URL. Verify the page is not broken — no unclosed tags, no missing sections, no CSS conflicts.
7. **Continuity check**: After all batches are imported, view the complete page source. Verify there are no duplicate opening tags, no orphaned closing tags, and the HTML structure is valid.

### Batch Import Rules

- **Use ONE HTML widget per page.** All batches go into the SAME HTML widget. Do NOT create multiple HTML widgets for batch imports.
- **Append, never replace.** When adding batch 2+, position the cursor at the END of existing content and append. Never select-all-and-replace with a partial batch.
- **Verify after EVERY batch.** Do not paste all batches blindly and verify at the end. After each batch, click Update and check the front-end.
- **If a batch fails to paste**: Stop. Do not retry with a smaller batch without understanding why it failed. Check for memory limits, WAF blocking, or session timeout.
- **Never split CSS or JS across batches.** The `<style>` block stays in the first batch. The `<script>` block stays in the final batch. If CSS/JS is too large, split the CSS into multiple `<style>` blocks (one per section) and the JS into multiple `<script>` blocks (one per section), but never break a single `<style>` or `<script>` tag across batches.

## Principle

Do not restart the whole page if one Elementor step fails. Maintain a page ledger:

```json
{
  "home": {
    "post_id": 0,
    "url": "",
    "edit_url": "",
    "elementor_url": "",
    "created": false,
    "canvas_set": false,
    "html_widget_inserted": false,
    "html_updated": false,
    "frontend_verified": false
  }
}
```

Resume from the first false step. Do not delete pages or regenerate stable HTML unless the user asked for a redesign.

## CRITICAL: No Header/Footer in Page HTML

Page HTML widgets must contain ONLY page-specific content. The global shell handles header, footer, menu, global CSS, and global JS. Read `global-shell-architecture.md` for the complete architecture.

- **Do NOT include `<header>` tags or header HTML** in the Elementor HTML widget. The global header is injected via `wp_body_open` hook in a Code Snippets PHP snippet.
- **Do NOT include `<footer>` tags or footer HTML** in the Elementor HTML widget. The global footer is injected via `wp_footer` hook in a Code Snippets PHP snippet.
- **Do NOT include navigation menu HTML** in the Elementor HTML widget. The global header renders the WordPress primary menu automatically.
- **Do NOT include global CSS** (design tokens, shared component styles, responsive breakpoints) in the Elementor HTML widget. Global CSS is added via Appearance → Customize → Additional CSS.
- **Do NOT include global JS** (mobile menu toggle, cart counter, smooth scroll, analytics, cookie consent) in the Elementor HTML widget. Global JS is added via Code Snippets HTML/JS snippet on `wp_footer` hook.
- **DO include**: Page-unique HTML structure, scoped CSS (using page-specific class names like `.home-page .hero`), and scoped JS (wrapped in IIFE `(function() { ... })()`).

### Why this matters

Embedding header/footer in every page HTML widget is:
1. **Redundant** — the same code is duplicated across all pages.
2. **Error-prone** — a header change requires updating every page individually.
3. **Performance-impacting** — duplicate HTML/CSS/JS increases page weight.
4. **Maintenance-heavy** — adding a menu item or changing the footer requires touching every page.

The global shell architecture solves this by injecting shared elements once, globally, via WordPress hooks.

## Create page first

Prefer API or wp-admin page creation:

- Title and slug.
- Status: draft while building, publish after verification unless the user requests immediate publish.
- Template/layout meta can be attempted through API if known, but always verify in Elementor UI.

Common Elementor canvas meta keys may include `_wp_page_template` or Elementor page settings, but UI verification is more reliable across versions.

## Open Elementor

Use whichever works:

- From Pages list: open page row action `Edit with Elementor`.
- Direct URL pattern: `/wp-admin/post.php?post=<ID>&action=elementor`.
- From classic edit screen: click `Edit with Elementor`.

Wait for the Elementor editor to finish loading. Avoid relying only on network idle; wait for visible Elementor panel/editor selectors or text.

## Set Page Layout to Elementor Canvas (MANDATORY — Execute Before Adding HTML Widget)

**This step is MANDATORY. Do NOT proceed to "Add one HTML widget" until Canvas is set, saved, and verified. Skipping this step is a DEAD RULE violation.**

Elementor UI changes often. Try these paths in order, verifying after each:

1. Newer Elementor top bar:
   - Open top bar page/settings control.
   - Look for `Page Settings`, `页面设置`, settings icon, or page title dropdown.
   - Find `Page Layout`.
   - Select `Elementor Canvas`.
   - Update.

2. Older Elementor left panel:
   - Click the bottom-left gear icon.
   - Find `Page Layout`.
   - Select `Elementor Canvas`.
   - Update.

3. WordPress edit screen fallback:
   - Open normal page edit screen.
   - Set template/page layout to Elementor Canvas if the theme/editor exposes it.
   - Update.
   - Reopen Elementor and verify.

Recognition hints:

- Labels may be English or Chinese: `Page Settings`, `页面设置`, `Page Layout`, `页面布局`, `Elementor Canvas`.
- If the top bar has replaced the old bottom-left gear, inspect the top-left/top-center toolbar and page title area first.

### Canvas Verification Gate (MANDATORY — Must Pass Before Proceeding)

After selecting Elementor Canvas and clicking Update/Save:

1. Open the front-end page URL in a new browser tab.
2. Check: Does the Hello Elementor default header appear at the top? (logo on left, menu items)
3. Check: Does the Hello Elementor default footer appear at the bottom? (copyright text, footer menu)
4. Check: Does the page appear as a blank canvas with no theme chrome?
5. **If header/footer/menu still appears**: Canvas was NOT set correctly. Go back to Elementor, re-set Canvas, Update again, and re-verify.
6. **If the page is a blank canvas (no theme header/footer)**: Canvas is set correctly. Record `"canvas_set": true` in the page ledger and proceed to add the HTML widget.
7. **NEVER proceed to HTML widget insertion until this verification passes.**

## Add one HTML widget and import HTML

For each custom page:

1. **Verify Canvas is set** — check the page ledger: `"canvas_set": true`. If false, go back to "Set Page Layout to Elementor Canvas" and complete it first.
2. Ensure the canvas is blank or contains only prior generated content for the same page.
3. Add an `HTML` widget. In Chinese UI this may appear as `HTML`.
4. Drag/click it into the main canvas.
5. Paste the full generated HTML/CSS/JS payload for that page.
   - **If the payload is large (>30,000 characters) or paste fails/truncates**: Follow the "DEAD RULE: Batch Import for Large HTML" procedure above. Split into batches, append to the SAME HTML widget, verify after each batch.
6. Update.
7. Open the front-end URL and verify:
   - The new HTML appears.
   - Scoped CSS applies.
   - No duplicate header/footer — header and footer come from the global shell only.
   - Dynamic containers are present.
   - Mobile layout is usable.
   - No HTML structure errors from batch import (if batched): check for unclosed tags, orphaned closing tags, or missing sections.

If a page already has a generated HTML widget:

- Prefer selecting and replacing the widget content.
- Avoid stacking duplicate HTML widgets unless the page intentionally has multiple independent sections.
- When replacing large content, use the batch import procedure if the new content exceeds 30,000 characters.

## Failure handling

- If Elementor fails to load because of mixed content, plugin errors, or memory limits, do not keep clicking randomly. Record the failure and use API/manual `.md` fallback.
- If the HTML widget paste is truncated or fails: **Do NOT retry the same large paste.** Switch to the batch import procedure (see "DEAD RULE: Batch Import for Large HTML"). Split the HTML into smaller batches and import sequentially, verifying after each batch.
- If a batch import produces broken HTML (unclosed tags, missing sections): Undo the last batch paste, identify the split point error, re-split at a valid tag boundary, and re-paste.
- If Update fails, check session expiry, permissions, WAF, or autosave conflict.
- If the page front end does not change, clear cache and verify that the correct page ID/URL was edited.
- If Canvas was not set before pasting HTML: Set Canvas now, Update, reload front-end to verify theme chrome is gone, then verify the page HTML still renders correctly.

## Verification

A page is done only when:

- Page exists with the correct slug.
- Page Layout is Elementor Canvas when required.
- Exactly the intended HTML content is present (page-specific content only — no header, footer, or global CSS/JS).
- Update succeeded.
- Front-end URL renders the expected design.
- Header and footer appear from the global shell (not from the page HTML widget).
- No duplicate header/footer in the page.
