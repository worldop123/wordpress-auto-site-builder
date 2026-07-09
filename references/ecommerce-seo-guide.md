# Ecommerce SEO Guide (WooCommerce)

## Overview
Ecommerce SEO requires specialized strategies beyond general SEO. This guide covers WooCommerce-specific SEO for product pages, category pages, navigation, internal linking, and conversion optimization. Read this alongside `google-seo-guidelines.md`, `rank-math-seo-guide.md`, and `structured-data-guide.md`.

## Ecommerce Site Architecture

### URL Structure Best Practices
- Product: `/product/product-slug/` or `/shop/category/product-slug/`
- Category: `/product-category/category-slug/`
- Blog: `/blog/post-slug/` or `/guides/post-slug/`
- Pages: `/page-slug/`
- Keep URLs short, descriptive, keyword-rich
- Use hyphens, not underscores
- Avoid query parameters in product URLs

### Navigation Hierarchy
Critical for Google to find all products:
```
Homepage
  → Category Pages
    → Subcategory Pages
      → Product Pages
  → Blog/Guides
    → Individual Articles
  → Policy Pages (footer)
```

Rules:
- Every product must be reachable via navigation links
- Googlebot does NOT submit searches to search boxes
- Use `<a href>` tags for all navigation (not JavaScript click handlers)
- Link to bestsellers from homepage
- Link to products from relevant blog posts
- Include sitemap for pages not reachable via navigation

### Faceted Navigation (Filters)
- Filter URLs (color, size, price) can create duplicate content
- Use `rel="canonical"` to point filter URLs back to main category
- Consider `noindex` for filtered results that don't add SEO value
- Use URL parameters in Search Console to control crawling
- Rank Math can handle canonical for WooCommerce archives

## Product Page SEO

### Product Title Optimization
- Include primary keyword near the beginning
- Include brand name
- Include one key differentiator (size, color, material, model)
- Keep under 60 characters for search results
- Example: "Premium Cotton T-Shirt | BrandName | Navy Blue, XL"

### Product Meta Description
- 120-160 characters
- Include product type, key spec, benefit, and call to action
- Example: "Shop our premium navy blue cotton t-shirt in size XL. Soft, durable, and ethically made. Free shipping over $50. Order now from BrandName."

### Product Long Description (Body Content)
Structure for SEO depth:
1. **Introduction**: What the product is, who it's for
2. **Key Features**: Bulleted list of features with benefits
3. **Specifications**: Detailed specs (dimensions, materials, weight, etc.)
4. **Use Cases**: How and where to use the product
5. **What's Included**: Package contents
6. **Shipping & Returns**: Delivery info and return policy
7. **FAQ**: Common questions about the product
8. **Internal Links**: Links to related products, categories, guides

### Product Images
- Use high-quality images (minimum 1000x1000px for zoom)
- Provide multiple angles and lifestyle shots
- Write descriptive ALT text with product name and key attribute
- Use WebP format for performance
- Include image structured data in Product schema
- Image filename should be descriptive: `navy-blue-cotton-tshirt-xl.jpg`

### Product Schema (Critical)
- Implement Product schema with all required properties
- Include offers (price, currency, availability)
- Add brand, SKU, GTIN if available
- Include aggregateRating if you have reviews
- Test every product with Rich Results Test
- See `structured-data-guide.md` for implementation details

### Product Reviews
- Enable WooCommerce reviews
- Reviews generate fresh, unique content
- Review schema enables star ratings in search results
- Never fabricate reviews or ratings
- Respond to reviews to show active engagement
- Display review count and average rating prominently

### Product Variations SEO
- Variable products: ensure each variation has proper data
- Variation attributes (color, size) should be in URL or structured data
- Consider separate landing pages for major variations if search volume warrants
- Use WooCommerce variation swatches for UX

## Category Page SEO

### Category Description
- Write unique, keyword-rich descriptions for each category
- 150-300 words with internal links to products and subcategories
- Include buying guide content to add value
- Don't just list products — provide context and guidance

### Category Meta
- Unique SEO title and meta description per category
- Include category keyword and brand
- Example: "Men's T-Shirts | Premium Cotton Tees | BrandName"

### Category Schema
- CollectionPage or ItemList schema
- BreadcrumbList schema for navigation
- Category should link to all products in that category

### Subcategory Strategy
- Create subcategories for product types with enough depth
- Example: Men > Shirts > T-Shirts, Dress Shirts, Polo Shirts
- Each subcategory gets its own SEO-optimized page
- Avoid empty categories — redirect or noindex if no products

## Blog/Guide Content for Ecommerce SEO

### Content Strategy
- Create buying guides for product categories
- Write comparison articles between product types
- Publish how-to articles related to product use
- Create gift guides for holidays and occasions
- Write industry trend articles

### Internal Linking from Blog
- Link from blog posts to relevant product pages
- Link from blog posts to category pages
- Use descriptive anchor text (not "click here")
- Aim for 3-5 internal links per article
- Link to products mentioned in the article contextually

### Article Structure for SEO
- H1: Compelling, keyword-rich title
- Introduction with key takeaway
- H2 sections with subtopics
- Product callout boxes with images and links
- Comparison tables
- FAQ section with FAQPage schema
- Conclusion with CTA to shop

## Internal Linking Strategy

### Types of Internal Links
1. **Navigation links**: Menu, breadcrumbs, footer
2. **Contextual links**: Within content to related pages
3. **Related products**: On product pages
4. **Cross-sells and up-sells**: WooCommerce features
5. **Category links**: From products to their categories
6. **Blog-to-product links**: From articles to products

### Best Practices
- Link from high-authority pages to important product pages
- Use descriptive anchor text with relevant keywords
- Don't overlink — 3-5 contextual links per page is sufficient
- Ensure no orphan pages (pages with no internal links pointing to them)
- Use Rank Math Link Genius (Pro) to find orphan pages
- Link pillar content from multiple related articles

### Orphan Page Prevention
- Every product should be linked from its category
- Every blog post should be linked from blog index and related posts
- Every page should be in a menu, footer, or contextual link
- Use sitemap as fallback for Google discovery
- Run periodic audits with Rank Math SEO Analysis

## Technical SEO for WooCommerce

### Crawl Budget Optimization
- noindex low-value pages: search results, filters, tags
- Block cart, checkout, my-account from indexing
- Use pagination properly (rel="next" and rel="prev" are deprecated, but ensure paginated pages are crawlable)
- Limit faceted navigation URL variations
- Keep sitemap clean and updated

### Canonical Tags
- WooCommerce can generate duplicate URLs (sorting, filtering)
- Rank Math handles canonical tags automatically
- Verify canonical on category pages with filters
- Set canonical for pagination to self (each page canonical to itself)

### Pagination
- WooCommerce product archives use pagination
- Each paginated page should be self-canonical
- Ensure paginated pages are in sitemap
- Don't noindex paginated pages (prevents product discovery)

### robots.txt Configuration
```
User-agent: *
Disallow: /cart/
Disallow: /checkout/
Disallow: /my-account/
Disallow: /*?add-to-cart=
Disallow: /wp-admin/
Allow: /wp-admin/admin-ajax.php

Sitemap: https://example.com/sitemap_index.xml
```

### WooCommerce-Specific SEO Settings (Rank Math)
- Enable WooCommerce module in Rank Math
- Configure product title format: `%seo_title% %sitename%`
- Set product category title format
- Configure product schema automatically
- Set noindex for internal search results
- Enable breadcrumbs for WooCommerce

## Image SEO for Ecommerce

### Image Optimization Checklist
- [ ] All product images have descriptive ALT text
- [ ] Images are in WebP format
- [ ] Images are properly sized (not oversized)
- [ ] Responsive srcset is configured
- [ ] Lazy loading enabled for below-the-fold images
- [ ] LCP image is preloaded and eager-loaded
- [ ] Image filenames are descriptive (not IMG_1234.jpg)
- [ ] Product gallery images show multiple angles
- [ ] Lifestyle images show product in use

### Rank Math Image SEO Module
- Automatically adds missing ALT attributes
- Automatically adds missing title attributes
- Pro: Adds watermark to social share images
- Enable in Rank Math Dashboard → Image SEO

## Conversion Optimization for SEO

### Page Speed and Conversions
- 1-second delay in page load can reduce conversions by 7%
- Mobile page speed directly impacts both SEO and conversions
- See `core-web-vitals-guide.md` for optimization strategies

### Trust Signals (Improve both SEO and conversions)
- Customer reviews and ratings (fresh content + social proof)
- Trust badges (SSL, payment security, review platforms)
- Clear return and refund policy
- Free shipping threshold clearly displayed
- Contact information visible
- About page with company story
- FAQ page addressing common concerns

### Mobile UX for Conversions
- Thumb-friendly button sizes (minimum 44x44px)
- One-page or simplified checkout
- Sticky add-to-cart button on product pages
- Mobile-optimized product galleries (swipe, pinch-zoom)
- Quick view for product previews
- Mobile payment options (Apple Pay, Google Pay)

## International Ecommerce SEO

### hreflang for Multilingual Stores
- Use hreflang tags for multi-region/multi-language stores
- Format: `hreflang="en-US"`, `hreflang="en-GB"`, `hreflang="fr-FR"`
- Include self-referencing hreflang on every page
- Use x-default for fallback language version
- Rank Math PRO supports hreflang configuration
- Verify with Search Console International Targeting report

### Multi-Region Considerations
- Use country-specific domains, subdirectories, or subdomains
- Subdirectories (example.com/us/, example.com/uk/) are easiest to manage
- Localize content (currency, units, cultural references, payment methods)
- Set up Google Merchant Center for each target country
- Ensure local shipping and tax info is accurate per region
- Translate SEO metadata (titles, descriptions, alt text) — don't auto-translate blindly

### Currency and Pricing Display
- Display local currency prominently
- Use schema `priceCurrency` matching displayed currency
- Avoid geolocation-based content swapping without proper hreflang
- Consider separate product feeds per currency in Merchant Center

## Local SEO for Ecommerce

### Brick-and-Click Stores
- If you have physical stores, create location pages
- Each location page: address, hours, phone, map, driving directions
- Implement LocalBusiness schema on location pages
- Link location pages from a "Store Locator" page
- Encourage and respond to Google Business Profile reviews
- Keep NAP (Name, Address, Phone) consistent everywhere

### Local Product Inventory
- Use Google Merchant Center local inventory ads
- Implement `LocalBusiness` + `Offer` schema with availability
- Show in-store availability on product pages where applicable
- Use "Buy Online, Pick Up In-Store" messaging clearly

## Ecommerce SEO Metrics and KPIs

### Organic Search Metrics
- Organic sessions to product pages
- Organic sessions to category pages
- Organic sessions to blog/guides
- Keyword rankings for product and category terms
- Organic click-through rate (CTR) from search results
- Impressions and average position in Search Console

### Revenue and Conversion Metrics
- Organic revenue (attributed to SEO channel)
- Organic conversion rate
- Average order value from organic traffic
- Organic assisted conversions
- Revenue per organic session
- New vs. returning organic customer split

### Technical Health Metrics
- Number of indexed pages vs. submitted pages
- Crawl errors and 404s
- Core Web Vitals scores (LCP, INP, CLS)
- Mobile usability issues
- Structured data errors and warnings
- Orphan page count

### Content Metrics
- Blog traffic and engagement
- Internal link click-through rates
- Bounce rate and time on page (contextual, not standalone KPIs)
- Pages per session from organic
- Top performing product/category pages

## Common Ecommerce SEO Mistakes

### Content and Metadata Mistakes
- Duplicate product descriptions from manufacturers (use original, rewritten content)
- Thin category pages with no description
- Missing or duplicate meta titles and descriptions
- Ignoring long-tail keywords for niche products
- Keyword stuffing in product titles
- Auto-generated metadata that doesn't match content

### Technical Mistakes
- Indexable cart, checkout, and account pages
- Filtered URLs creating thousands of duplicate pages
- Pagination that blocks product discovery (noindex on paginated pages)
- Missing canonical tags on product variations
- Broken internal links to out-of-stock or removed products
- Slow product images not optimized (oversized JPEGs)
- Missing or invalid structured data on products

### Architecture Mistakes
- Products only reachable via search or deep filters
- Orphan product pages with no internal links
- Flat URL structure without categories
- Too many clicks from homepage to product (aim for 3 clicks max)
- Empty categories left indexed
- No breadcrumbs on product/category pages

### Strategy Mistakes
- Ignoring blog/content marketing for ecommerce
- No internal linking strategy from content to products
- Focusing only on head terms, ignoring long-tail
- Not updating content for seasonal trends
- No competitor analysis or gap research
- Treating SEO as one-time instead of ongoing

## Seasonal SEO Strategy

### Pre-Season Preparation
- Identify seasonal keywords 2-3 months ahead (use Google Trends)
- Create or update seasonal landing pages and gift guides
- Build internal links from blog content to seasonal products
- Update meta titles/descriptions with seasonal modifiers
- Prepare product schema with seasonal availability

### During Peak Season
- Monitor rankings and traffic daily
- Ensure stock availability is reflected in schema (avoid "out of stock" ranking loss)
- Promote bestsellers and high-margin products
- Use countdown timers for limited-time offers (with care for UX)
- Keep page speed fast despite traffic spikes

### Post-Season
- Repurpose seasonal content for evergreen use
- Update or remove out-of-season product pages
- Redirect seasonal landing pages to relevant category pages
- Analyze performance for next year's planning

## Competitor Analysis for Ecommerce SEO

### Identifying SEO Competitors
- Competitors in search results may differ from business competitors
- Use Search Console to find sites ranking for your target keywords
- Analyze both direct competitors and content competitors (blogs, review sites)

### What to Analyze
- Competitor product page structure and content depth
- Category page descriptions and organization
- Keyword gaps (keywords they rank for that you don't)
- Backlink profile and linking domains
- Internal linking patterns and anchor text usage
- Structured data implementation
- Content publishing frequency and topics

### Tools for Competitor Research
- Google Search Console (your own data + "queries" comparison)
- Semrush, Ahrefs, or SimilarWeb for competitor traffic estimates
- Rank Math SEO Analyzer for on-page comparison
- Manual review of top-ranking competitor pages

## Ecommerce SEO QA Checklist

### Product Pages
- [ ] Unique SEO title per product
- [ ] Unique meta description per product
- [ ] Focus keyword set in Rank Math
- [ ] Long description with 300+ words
- [ ] Multiple product images with ALT text
- [ ] Product schema valid (Rich Results Test)
- [ ] Price, availability, and SKU correct in schema
- [ ] Add-to-cart button works
- [ ] Variation selector works (if applicable)
- [ ] Related products displayed
- [ ] Breadcrumbs displayed
- [ ] Mobile layout tested
- [ ] Page load under 3 seconds

### Category Pages
- [ ] Unique category description (150+ words)
- [ ] Unique SEO title and meta description
- [ ] All products in category are listed
- [ ] Subcategories linked (if applicable)
- [ ] Breadcrumbs displayed
- [ ] Filters work without breaking canonical
- [ ] Pagination works
- [ ] Mobile layout tested

### Blog/Guides
- [ ] Articles have unique, keyword-rich titles
- [ ] Internal links to relevant products (3-5 per article)
- [ ] Product images with ALT text
- [ ] FAQPage schema for FAQ sections
- [ ] Article schema with author and date
- [ ] Mobile layout tested
- [ ] Social sharing buttons work

### Technical
- [ ] Sitemap includes all products, categories, and posts
- [ ] robots.txt blocks cart, checkout, my-account
- [ ] Canonical tags correct on all pages
- [ ] No broken internal links
- [ ] No 404 errors on important pages
- [ ] Core Web Vitals passing (see core-web-vitals-guide.md)
- [ ] HTTPS enabled site-wide
- [ ] Mobile-friendly test passing
- [ ] Structured data valid on sample pages

### Indexing
- [ ] Products, categories, posts are indexable
- [ ] Cart, checkout, my-account are noindex
- [ ] Search results pages are noindex
- [ ] Filter/sort URLs are canonicalized
- [ ] Sitemap submitted to Google Search Console
- [ ] Sitemap submitted to Bing Webmaster Tools
- [ ] No manual actions in Search Console
