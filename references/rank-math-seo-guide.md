# Rank Math SEO Complete Configuration Guide

## Overview
Rank Math is a revolutionary WordPress SEO plugin known for its user-friendly interface and extensive feature set. It simplifies search engine optimization to improve online visibility. This guide covers installation, configuration, all modules, and advanced features.

## Rank Math vs Yoast SEO Comparison (18 Dimensions)

| Feature | Rank Math (Free & Pro) | Yoast SEO (Free & Premium) |
|---------|----------------------|---------------------------|
| Basic TDK optimization | Free: Full support, Pro: Full support | Free: Full support, Premium: Full support |
| UI/UX | Gutenberg/Elementor integration, floating sidebar panel | Traditional bottom meta box, clunky integration |
| Focus keywords | Free: 5 keywords, Pro: Unlimited | Free: 1 keyword, Premium: 5 keywords |
| Content scoring | Free: 100-point system, Pro: Per-keyword scoring | Free: Traffic light + readability, Premium: Synonyms |
| LSI/Related keywords | Free: Google suggestions built-in, Pro: Deep tracking | Free: No, Premium: No |
| Redirects (301/302) & 404 | Free: Built-in 404 monitor + redirector, Pro: Regex + export | Free: No, Premium: Built-in redirect manager |
| Internal linking suggestions | Free: Basic suggestions, Pro: Orphan page finder | Free: No, Premium: Orphan + suggestions |
| Schema structured data | Free: 15+ built-in schemas, Pro: Custom generator + stacked | Free: Basic article/org only, Premium: Limited |
| Image SEO automation | Free: Auto-fill missing Alt/Title, Pro: Auto watermark | Free: No, Premium: No |
| Breadcrumbs | Free/Pro: One-click enable + shortcode | Free/Premium: Requires theme modification |
| WooCommerce SEO | Free: Basic e-commerce schema, Pro: Advanced (GTIN) | Free: No, Paid: Separate plugin ($79/yr) |
| Local SEO | Free: Single location, Pro: Multi-location + KML | Free: No, Paid: Separate plugin ($79/yr) |
| News & Video sitemaps | Pro: One-click generation | Paid: Separate plugins ($79/yr each) |
| Analytics integration | Free: GSC data in backend, Pro: 12-month ranking | Free: Need to leave backend, Premium: Same |
| Performance | Free: ~40KB modular, Pro: Fast with all features | Free: Several MB, Premium: Often heavy |
| Support | Free: Active community, Pro: 24/7 tickets | Free: Forum, Premium: Email (24hr) |
| License limit | Free: Unlimited sites, Pro: UNLIMITED personal sites | Free: Unlimited, Premium: Per site ($99 each) |
| Pricing | Free: Forever, Pro: ~$69/yr | Free: Forever, Premium: $99/yr+ |

## Installation

### Free Version
1. WordPress Admin → Plugins → Add New
2. Search "Rank Math"
3. Click Install, then Activate
4. Or download from: https://wordpress.org/plugins/seo-by-rank-math/

### Pro Version
1. Login to Rank Math account at https://rankmath.com/
2. Download Rank Math Pro plugin file
3. WordPress Admin → Plugins → Add New → Upload Plugin
4. Upload the Pro .zip file
5. Activate and connect your Rank Math account
6. Official site: https://rankmath.com/

## Setup Wizard Configuration

### Step 1: Choose Configuration Mode
- **Simple**: Basic setup for beginners
- **Advanced** (RECOMMENDED): Full control over all settings
- **Custom**: Pick specific features

### Step 2: Import Data from Other SEO Plugins
- Rank Math detects if Yoast SEO, SEOPress, or other SEO plugins were previously installed
- Import configuration to seamlessly migrate

### Step 3: Site Information
- Select site category
- Enter site name and other details

### Step 4: Connect Rank Math Account
- On first use for a site, explicitly tell the user to connect the relevant Rank Math account.
- Connection is needed for account-based features such as Google Services/Analytics integration, PRO licensing, and some Rank Math services.
- If the user chooses to skip connection, record `user_skipped` and continue with local SEO settings. Do not pretend Analytics/account features are configured.
- If login, license, CAPTCHA, or permission blocks connection, record `blocked` and continue only with features that do not require the account.

### Step 5: Sitemap Configuration
- Enable XML sitemap
- Include/exclude images, post types, taxonomies
- Configure Google News sitemap and Video sitemap if needed

### Step 6: Optimization Settings
- Auto nofollow external links
- Open external links in new tab
- Other link optimization options

## Dashboard - Enable Advanced Mode

FIRST ACTION after setup: Go to Rank Math → Dashboard and enable **Advanced Mode** (not Simple Mode) to access all modules.

### Module Management Principle
**Only enable modules you actually use. Disable unused modules.** Some modules (like Analytics) can cause database bloat.

## Complete Module Reference

### 404 Monitor
- Tracks 404 errors and logs them
- Use to fix redirect errors
- **Recommendation**: Disable after fixing to prevent database bloat
- Lifecycle: `read_only_scanner` — disable after use

### ACF (Advanced Custom Fields)
- Enables Rank Math content analysis for ACF fields
- Enable if using ACF plugin
- Lifecycle: `persistent` if ACF is used

### AMP
- For Accelerated Mobile Pages support
- Enable only if using AMP plugin
- Lifecycle: `persistent` if AMP is used

### Analytics
- View Search Console, Analytics, and AdSense data directly in Rank Math
- **WARNING**: Can cause database bloat
- **Recommendation**: Consider using Search Console directly instead
- Pro version: 12-month independent keyword ranking monitoring
- Lifecycle: optional `persistent`

### bbPress
- Meta tag control for bbPress discussion boards
- Enable only if using bbPress
- Lifecycle: `persistent` if bbPress used

### BuddyPress
- Meta tag control for BuddyPress discussion boards
- Enable only if using BuddyPress
- Lifecycle: `persistent` if BuddyPress used

### Image SEO
- Automatically adds alt text to images missing it
- Saves significant time for large product catalogs
- Pro: Automatically adds logo watermark to social share images
- Lifecycle: `one_time_writer` or `persistent` for ongoing

### Link Genius (New in 2026.3.4)
- Advanced internal linking tool
- Analyzes posts, tracks link data, provides detailed reports
- Pro feature
- Lifecycle: `persistent`

### Instant Indexing
- Notifies Bing when pages are added, updated, or deleted
- Speeds up indexing for new content
- Lifecycle: `persistent`

### Link Counter
- Counts internal/external links in posts for on-page SEO
- Can cause database bloat
- Lifecycle: optional, `read_only_scanner`

### Local SEO & Knowledge Graph
- Extends Rank Math settings for local SEO
- Tells Google about your business
- Creates local (KML) sitemap
- Free: Single location support
- Pro: Multi-location management, KML map customization
- Lifecycle: `persistent` for local businesses

### News Sitemap
- Creates Google News sitemap
- Enable ONLY if publishing content for Google News
- Lifecycle: `persistent` if applicable

### Redirections
- Create 301/302 redirects within Rank Math
- Note: Server-level redirects (htaccess/nginx) are faster
- Free: Built-in redirector with 404 monitoring
- Pro: Regex matching and dead link export
- Lifecycle: `persistent`

### Schema (Structured Data)
- Add schema markup to pages/posts for higher CTR
- Free: 15+ built-in schema types (Article, Product, Review, FAQ, etc.)
- Pro: Powerful custom schema generator + stacked schemas
- Lifecycle: `persistent`

### Role Manager
- Restrict user capabilities based on assigned roles
- Control who can edit SEO settings
- Lifecycle: `persistent`

### SEO Analysis
- Analyzes entire website and provides SEO recommendations
- Different from on-page content analysis
- Lifecycle: `read_only_scanner` — run periodically

### Sitemap
- Creates XML sitemap (supports hreflang tags)
- Submit to Google Search Console
- Lifecycle: `persistent`

### Video Sitemap
- Creates video-specific sitemap
- Enable if site has many videos
- Lifecycle: `persistent` if applicable

### Google Web Stories
- Optimize Web Stories in Rank Math
- Enable if using Google Web Stories plugin
- Lifecycle: `persistent` if applicable

### WooCommerce
- Activates WooCommerce SEO options in Rank Math settings
- Metadata + product schema optimization
- Free: Basic e-commerce schema
- Pro: Advanced e-commerce (GTIN, global identifiers)
- Lifecycle: `persistent` for ecommerce sites

## General Settings (Link, Image, Breadcrumbs)

### Links Settings
- Strip category base: Remove `/category/` from URLs
- Redirect attachment URLs to parent: Prevent thin content
- Open external links in new tab: `target="_blank"` with `rel="noopener"`
- Add nofollow to external links: Control link equity
- Redirect orphaned attachments

### Images Settings
- Add missing ALT attributes automatically
- Add missing title attributes automatically

### Breadcrumbs Settings
- Enable breadcrumbs
- Use shortcode `[rank_math_breadcrumb]` to insert anywhere
- Configure separator character, show/hide homepage label
- Configure breadcrumb prefix and taxonomy labels

### Webmaster Tools Verification
- Google Search Console verification
- Bing Webmaster Tools verification
- Baidu Webmaster Tools verification
- Yandex Webmaster Tools verification
- Pinterest verification
- Site Kit by Google integration

### Edit .htaccess and robots.txt
- Edit .htaccess directly from Rank Math
- Edit robots.txt directly from Rank Math
- View and test robots.txt rules

## Titles & Meta Settings

### Global Meta
- Variable-based template system using variables like `%sitename%`, `%sitedesc%`, `%page_title%`, `%seo_title%`, `%seo_description%`, `%focus_keyword%`, `%currentdate%`, `%currentmonth%`, `%currentyear%`
- Separate title and description templates for each post type

### Post Type Settings (Posts, Pages, Products)
- Title format: e.g., `%seo_title% %sitename%`
- Description format: e.g., `%seo_description%`
- Custom robots meta: index/noindex, follow/nofollow
- Show/hide snippet editor, social preview, keyword analysis

### Taxonomy Settings (Categories, Tags, Product Categories)
- Title and description templates
- Custom robots meta per taxonomy

### Global Robots Meta
- Default robots settings for all post types
- noindex for: Cart, Checkout, My Account, internal search results, 404 pages, date archives, author archives (if single-author blog)

### Local SEO Settings
- Business type selection
- Business name, address, phone, URL
- Logo upload
- Opening hours
- Maps integration
- Knowledge Graph type (Organization or Person)

### Social Meta
- OpenGraph settings (Facebook)
- Twitter Card settings
- Social profile URLs (Facebook, Twitter, Instagram, LinkedIn, etc.)
- Default social share image

## XML Sitemap Configuration

### General Settings
- Enable XML sitemap
- Include images in sitemap
- Sitemap compression

### Post Type Sitemaps
- Enable/disable sitemaps for posts, pages, products, custom post types
- Set priority and frequency per post type

### Taxonomy Sitemaps
- Enable/disable sitemaps for categories, tags, product categories
- Set priority and frequency

### Sitemap Exclusions
- Exclude specific posts/pages by ID
- Exclude specific taxonomies
- Exclude specific URLs

### Sitemap Submission
- Submit sitemap_index.xml to Google Search Console
- Submit sitemap_index.xml to Bing Webmaster Tools
- Rank Math auto-notifies search engines of updates

## Schema Templates Configuration

### Built-in Schema Types (Free)
- Article
- Product (WooCommerce)
- Review
- FAQ
- HowTo
- Recipe
- Software Application
- Video Object
- Person
- Book
- Movie
- Course
- Event
- Dataset
- Podcast
- MusicRecording

### Custom Schema (Pro)
- Drag-and-drop schema builder
- Stack multiple schemas on one page
- Custom property mapping
- Schema validation

### Schema Setup Steps
1. Go to Rank Math → Schema Templates
2. Select schema type for each post type
3. Configure default properties
4. Test with Google Rich Results Test
5. Monitor with Search Console Rich Results report

## Instant Indexing Module

### Bing IndexNow Integration
- Automatically pings Bing when content changes
- API key required (auto-generated by Rank Math)
- Supports page creation, update, and deletion notifications
- Speeds up Bing indexing significantly

### Google Indexing API
- Not officially supported for general content (Google reserves for job postings and live streams)
- Rank Math can integrate if API access is available

## SEO Analyzer Tool

### Site-Wide SEO Audit
- Analyzes entire website for SEO issues
- Checks: meta tags, headings, images, links, performance, mobile, security
- Provides actionable recommendations with priority levels
- Can re-run after fixes to verify

### Page-Level SEO Analysis
- 100-point scoring system in post editor
- Checks focus keyword usage in: title, meta description, URL, first paragraph, headings, image alt text, content
- Content length analysis
- Internal/external link counting
- Readability analysis
- Keyword density check

## On-Page SEO: Achieving 100/100 Score

### Basic SEO Tests (Must Pass)
- Focus keyword in SEO title
- Focus keyword in meta description
- Focus keyword in URL/permalink
- Focus keyword in first 10% of content
- Focus keyword in at least one heading
- Focus keyword in image alt attribute
- Content length ≥ 600 words (recommended)
- Focus keyword density 0.5%-2.5%

### Additional Tests
- Internal links: at least 1
- External links: at least 1
- Title length: 40-60 characters
- Meta description length: 120-160 characters
- Content has table/structured data (bonus)
- Video embedded (bonus)

### Common Score Deductions
- Focus keyword not in first paragraph
- Too many focus keyword repetitions (keyword stuffing)
- Title too short or too long
- Meta description too short or too long
- No internal links
- No external links
- Content too short

### Important Note on 100/100
- 100/100 is NOT required for good SEO
- It's a guidance tool, not a guarantee of rankings
- Content quality and user value matter more than perfect scores
- Don't stuff keywords just to improve the score

## Content AI Feature (Pro)

### Overview
- AI-powered content creation within WordPress
- 40+ high-conversion templates and tools
- Requires Content AI subscription/credits

### Features
- Content generation based on focus keyword
- SEO-optimized content suggestions
- Topic research and ideation
- Question suggestions from "People Also Ask"
- Link suggestions
- Tone and style customization

### Usage
- Accessible from post editor sidebar
- Consumes credits per generation
- Not mandatory for good SEO — manual content creation is fine

## Status & Tools

### Database Tools
- Rebuild Rank Math database tables
- Clean unused data

### Import/Export
- Import settings from Yoast SEO, SEOPress, All in One SEO
- Export Rank Math settings for backup or migration
- Import/export individual module settings

### Role Manager
- Assign SEO editing capabilities to specific user roles
- Control who can: edit meta, edit robots, edit redirections, edit schema

## Rank Math PRO Features Summary
- Unlimited focus keywords
- Advanced schema generator with custom fields
- Schema stacking (multiple schemas per page)
- 12-month keyword rank tracking
- Advanced WooCommerce SEO (GTIN, brand, MPN)
- Multi-location Local SEO
- Google News Sitemap
- Video Sitemap
- Image SEO with auto-watermark
- Link Genius internal linking tool
- Content AI integration
- Unlimited personal site licenses
- 24/7 priority support
- Price: ~$69/year (vs Yoast Premium $99/year per site)

## Recommended Module Configuration for Ecommerce Sites

### Always Enable
- Sitemap (persistent)
- Schema (persistent)
- WooCommerce (persistent)
- Image SEO (persistent)
- Breadcrumbs (persistent)
- Local SEO & Knowledge Graph (persistent, if local business)
- Redirections (persistent)
- Instant Indexing (persistent)

### Enable as Needed
- Analytics (monitor for database bloat)
- Link Genius (Pro, for internal linking)
- Video Sitemap (if site has videos)
- ACF (if using Advanced Custom Fields)
- Role Manager (for multi-author sites)

### Disable After Use
- 404 Monitor (enable periodically for audits)
- SEO Analysis (run periodically)
- Link Counter (causes database bloat)

## Rank Math for WooCommerce Product SEO

### Product-Specific Settings
- Product title format: `%seo_title% %sitename%`
- Product meta description template
- Product schema (Product type with offers)
- GTIN/MPN/Brand fields (Pro)
- Product category SEO settings
- Product tag SEO settings

### Product CSV SEO Mapping
When importing products via CSV with Rank Math SEO fields:
- `rank_math_title` or `rank_math_seo_title`: SEO title
- `rank_math_description` or `rank_math_seo_description`: Meta description
- `rank_math_focus_keyword`: Focus keyword
- `rank_math_robots`: Robots directives (index,follow)
- `rank_math_canonical_url`: Canonical URL
- `rank_math_facebook_title`: OpenGraph title
- `rank_math_facebook_description`: OpenGraph description
- `rank_math_twitter_title`: Twitter card title
- `rank_math_twitter_description`: Twitter card description

### Product SEO Best Practices
- Unique SEO title per product with primary keyword near front
- Meta description with product type, key spec, shipping detail, brand
- One primary focus keyword per product (not comma-separated list)
- Robots: index/follow for published products
- Product schema with price, availability, reviews
- Internal link from category pages and blog posts to products

## Integration with WordPress Auto Site Builder

### Rank Math Baseline Setup (Phase 3)
1. Enable Advanced Mode in Dashboard
2. Configure General Settings (links, images, breadcrumbs)
3. Set Titles & Meta templates for all post types
4. Configure global robots meta (noindex for Cart, Checkout, My Account)
5. Enable and configure XML Sitemap
6. Set up Schema templates (Product for WooCommerce, Article for blog)
7. Configure Local SEO if applicable
8. Connect Webmaster Tools verification
9. Configure social meta (OpenGraph, Twitter Cards)
10. Enable WooCommerce module for ecommerce

### Content-Aware One-Time Writer Pattern

Rank Math Free supports JSON settings import, but full bulk CSV import of per-page/per-product SEO metadata is a Pro-oriented workflow. For free-version builds, use Code Snippets as a safer one-time writer.

Before writing metadata:

1. Create a content inventory from live WordPress content and build artifacts.
2. Inspect each page, product, post, and taxonomy before generating SEO fields.
3. Use the build ledger/resume ledger/product CSV report/article plan as a knowledge base, but verify against live content.
4. Produce an SEO mapping with:
   - `id`
   - `object_type`: `post`, `page`, `product`, `term`
   - `seo_title`
   - `seo_description`
   - `focus_keyword`
   - `robots`: usually `index,follow` for content and products; `noindex,follow` for cart/checkout/account/internal pages
   - `schema_type`: Product, Article, FAQPage, WebPage, CollectionPage, etc. where relevant
   - `source_evidence`: short note about which content facts were used

Recommended Rank Math post meta keys:

- `_rank_math_title`
- `_rank_math_description`
- `_rank_math_focus_keyword`
- `_rank_math_robots`

Recommended term meta keys:

- `rank_math_title`
- `rank_math_description`
- `rank_math_focus_keyword`
- `rank_math_robots`

Writer lifecycle:

1. Create a Code Snippets PHP snippet named like `one_time_writer / Rank Math SEO Meta Writer`.
2. Write only mapped IDs. Do not scan and overwrite unrelated content.
3. Skip manually customized meta unless the user approved overwrite or autonomous mode recorded the decision.
4. Record written, skipped, and failed IDs.
5. Verify admin fields and front-end source meta tags.
6. Verify sitemap/noindex behavior.
7. Disable and delete the snippet after successful verification.
8. If interrupted or partially failed, resume only missing/failed IDs from the writer ledger.

### Required On-Page SEO Checks

When writing pages, products, posts, and category descriptions, build the content and metadata so these Rank Math checks pass naturally:

#### Basic SEO

- Focus keyword appears in the SEO title.
- Focus keyword appears in the SEO meta description.
- Focus keyword appears near the beginning of visible content.
- Focus keyword appears in the main content.
- Content is not thin. Use enough product/page/article detail to satisfy search intent.

#### Additional SEO

- Focus keyword appears in at least one H2/H3/H4 subheading.
- At least one real image has ALT text containing the focus keyword.
- Keyword density is above zero and natural. Do not stuff keywords.
- Internal links point to real product/page/post URLs.
- Focus keyword is unique unless a deliberate topic cluster is documented.
- Content AI can be used when available, but it is optional and must not replace human-quality review.

#### Title Readability

- Focus keyword appears at the beginning of the SEO title when it reads naturally.

#### Content Readability

- Use short paragraphs.
- Use rich media such as real product images, page images, videos, or diagrams when available.

Before using the one-time writer, run a content-aware audit. If an item fails because the content itself is missing the focus keyword, subheading, image ALT, or rich media, fix the page/product/post content first, then write Rank Math metadata.

### Read-Only Scanner Pattern
For SEO QA:
1. Create a Code Snippet that scans all products/posts
2. Check for missing SEO titles, descriptions, focus keywords
3. Check for duplicate meta descriptions
4. Check robots directives
5. Output report
6. Disable after running

## Common Rank Math Issues and Solutions

### Sitemap Not Generating
- Check for conflicting sitemap plugins (disable other SEO plugins' sitemaps)
- Flush permalinks: Settings → Permalinks → Save Changes
- Check for server-side caching issues

### Schema Not Showing in Rich Results Test
- Verify schema module is enabled
- Check schema template assignment for post type
- Ensure required properties are filled
- Test with Google Rich Results Test

### Analytics Database Bloat
- Disable Analytics module if not needed
- Use Search Console directly instead
- Clean database using Status & Tools

### Score Stuck Below 100
- Check focus keyword placement
- Verify content length
- Add internal and external links
- Check title and description length
- Remember: 100/100 is NOT required for good rankings

## Sources
- https://rankmath.com/kb/rank-math-seo-plugin/
- https://www.pythonthree.com/rank-math-seo-plugin-tutorial/
- https://rankmath.com/kb/wordpress-seo/
- Rank Math official documentation and knowledge base
