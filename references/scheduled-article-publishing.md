# Scheduled Article Publishing and SEO Content Guide

## Overview

This reference defines how the WordPress auto site builder generates, schedules, and publishes SEO-optimized blog articles. Articles are generated based on the site's products, target market, language, and SEO keywords. Each article must pass through a draft-review-then-publish workflow before going live.

Read this reference when:
- Generating blog articles during site build (Phase 17 of the standard workflow)
- Setting up scheduled publishing for ongoing content
- Creating article content that ranks on Google
- Configuring Rank Math SEO metadata for articles

Also read `google-seo-guidelines.md` for E-E-A-T and content quality requirements, `rank-math-seo-guide.md` for Rank Math article configuration, and `ecommerce-seo-guide.md` for blog-to-product linking strategy.

## CRITICAL: Draft-Review-Then-Publish Workflow

Every article MUST go through this workflow before publishing. No article is published without explicit user approval.

### Step 1: Generate Article as Draft
- Create the article in WordPress with status `draft`.
- Set all Rank Math SEO metadata (title, description, focus keyword, schema).
- Add all product images (as featured image and inline content images).
- Add all product internal links.
- Set the article category and tags.
- Set a future scheduled publish date (if part of a scheduled batch).

### Step 2: Send Draft Link to User
- Provide the user with the draft preview URL: `https://site.com/wp-admin/post.php?post={ID}&action=edit`
- Also provide the frontend preview URL if the theme supports draft preview.
- Clearly tell the user: "Article [title] is ready for review. Please review it at [URL] and let me know if you approve publishing or need changes."

### Step 3: Wait for User Approval
- Do NOT publish the article until the user explicitly says "approve", "publish", "ok", or similar.
- If the user requests changes, make the changes and re-send the draft link.
- If the user does not respond, the article remains as a draft (it will NOT auto-publish even if a scheduled date is set, until the user approves).

### Step 4: Publish After Approval
- Once approved, set the article to `publish` status or `future` status (if scheduled).
- If scheduled, WordPress will automatically publish it at the scheduled date/time.
- Verify the article is live by checking the frontend URL.
- Confirm to the user that the article has been published.

### Exception: Batch Pre-Approval
If the user explicitly says "pre-approve all articles in this batch" or "auto-publish without review", the agent may skip the per-article review step. But this must be an explicit user instruction, not an assumption.

## Article Generation Strategy

### Context Awareness
Before generating any article, the agent MUST understand:
1. **Site products**: What products does the site sell? What categories? What are the key product features? If a CSV was provided, use the product knowledge ledger before choosing article topics, links, images, FAQs, or focus keywords.
2. **Target market**: Which country/region is the site targeting? Read `global-design-preferences.md` for cultural and language conventions.
3. **Language**: What language should articles be in? Match the site's primary language.
4. **SEO keywords**: What are the seed keywords? What products/categories are priority?
5. **Brand voice**: What is the brand's tone? (Formal, casual, technical, lifestyle, etc.)
6. **Prohibited claims**: What claims are off-limits? (Medical, health, guaranteed results, etc.)
7. **Competitor references**: Did the user provide competitor sites or style references?

### Article Topic Generation
Articles topics should be diverse but always related to the site's products and content. Never generate random unrelated topics.

#### Topic Categories
1. **Buying Guides**: "How to Choose [Product Type] for [Use Case]"
2. **Comparison Articles**: "[Product A] vs [Product B]: Which Is Better?"
3. **How-To Guides**: "How to Use [Product] for [Specific Purpose]"
4. **List Articles**: "Top 10 [Product Category] for [Season/Occasion/Use Case]"
5. **Product Deep Dives**: "Why [Product Feature] Matters in [Product Category]"
6. **Industry Trends**: "[Industry] Trends to Watch in [Year]"
7. **Seasonal Content**: "Best [Products] for [Holiday/Season]"
8. **Problem-Solving**: "Common [Problem] and How [Product Category] Solves It"
9. **Gift Guides**: "Gift Guide: Best [Products] for [Recipient Type]"
10. **FAQ Articles**: "Everything You Need to Know About [Product Category]"
11. **Maintenance/Care**: "How to Care for and Maintain Your [Product]"
12. **Behind the Scenes**: "How [Brand] Makes [Product]"

#### Topic Selection Rules
- Never repeat the same topic angle across articles in the same batch.
- Vary the article type (guide, comparison, list, how-to, trend).
- Ensure topics are relevant to the site's actual products.
- Avoid topics that require claims the site cannot support.
- Consider seasonal relevance based on the target market.
- Consider search volume potential (use seed keywords as starting point).
- Each article should target a different primary keyword to avoid cannibalization.

### Article Content Structure (SEO-Optimized)

#### Recommended Defaults (User-Modifiable)
- **Word count**: 800-1,500 words (varies by topic complexity; quality over quantity)
- **Product images**: 4-8 real product images per article (user-configurable)
- **Product internal links**: 3-5 prominent internal links to product pages (user-configurable)
- **External links**: 1-2 authoritative outbound links (with rel="nofollow" if untrusted)
- **Headings**: H1 title + 3-5 H2 subheadings + optional H3s
- **FAQ section**: 3-5 Q&A pairs with FAQPage schema
- **Reading time**: Display estimated reading time

#### Article Structure Template
```
[Featured Image: Real product image, optimized, WebP format]

H1: [Compelling, keyword-rich title, 50-60 characters]

[Introduction paragraph: 2-3 sentences, includes primary keyword, states what the article covers and who it's for]

[Key takeaway box or summary]

H2: [Section 1 - Main topic introduction]
[2-3 paragraphs with context and value]

H2: [Section 2 - Key features/benefits]
[Content with product image]
[Product internal link - prominent, styled callout]

H2: [Section 3 - Comparison or deep dive]
[Content with comparison table or detailed analysis]
[Product image]

H2: [Section 4 - How to choose/use]
[Practical advice with bullet points]
[Product internal link]

H2: [Section 5 - Common questions]
[FAQ section with 3-5 Q&A pairs]
[FAQPage schema markup]

H2: Conclusion
[Summary + CTA to shop related products]
[Final product internal link]

[Author bio box with E-E-A-T signals]
[Related articles section]
```

### Product Image Requirements

#### Featured Image (Thumbnail)
- Must be a real product image from the site's WooCommerce product gallery.
- Optimized to WebP format.
- Size: 1200x630px (optimal for social sharing and search results).
- Descriptive ALT text including product name and key attribute.
- Filename: descriptive, e.g., `premium-cotton-tshirt-navy-blue.webp`.

#### Inline Content Images (4-8 per article)
- All images must be real product images from the site's media library.
- All images must be in WebP format.
- Each image must have descriptive ALT text.
- Each image should have width and height attributes (prevents CLS).
- Images should be placed near relevant text content.
- Mix of product shots, lifestyle images, and detail close-ups.
- Image filenames should be descriptive (not IMG_1234.webp).
- Lazy load below-the-fold images.

#### Image Sourcing
- Use images from the site's WooCommerce product galleries.
- If a product has multiple images, select the most relevant for the article context.
- Never use stock photos that don't represent actual products.
- Never use placeholder images.
- All images must be accessible (no 404s).

### Product Internal Link Requirements

#### Link Placement
- 3-5 internal links to product pages (user-configurable).
- Links must be prominent and visually distinct (not hidden in text).
- Use descriptive anchor text with relevant keywords (not "click here").
- Place links contextually within relevant content sections.
- Consider using styled callout boxes for product links.

#### Link Style Examples
- Inline link: `<a href="/product/product-slug/" class="article-product-link">Premium Cotton T-Shirt in Navy Blue</a>`
- Callout box: A styled box with product image, name, price, and "View Product" button.
- Comparison table link: Product name in a comparison table that links to the product page.

#### Link Verification
- Every internal link must point to a real, published product page.
- No 404s on any article link.
- Verify links work on both desktop and mobile.
- Links should open in the same tab (not new tab) for internal navigation.

### Article Interlinking
- Link to other relevant blog articles (2-3 per article).
- Use a "Related Articles" section at the bottom.
- Prevent orphan articles — every article should have at least 2 internal links from other articles or pages.
- Build topic clusters: pillar article → supporting articles → product pages.

## Rank Math SEO Metadata for Articles

### Required SEO Fields (Per Article)
1. **SEO Title**: 50-60 characters, includes primary keyword near the beginning, includes brand name.
   - Format: `[Primary Keyword] - [Secondary Info] | [Brand Name]`
   - Example: "How to Choose a Cotton T-Shirt: Complete Guide | BrandName"

2. **Meta Description**: 120-160 characters, includes primary keyword, summarizes article value, includes a call to action.
   - Example: "Learn how to choose the perfect cotton t-shirt with our complete guide. Compare fabrics, fits, and care tips. Shop premium tees at BrandName today."

3. **Focus Keyword**: One primary keyword per article (Rank Math free: up to 5, but use 1 primary + 2-3 secondary).
   - Must be unique across articles (no keyword cannibalization).
   - Must appear in: title, meta description, URL slug, first paragraph, at least one H2, image ALT text.

4. **URL Slug**: Short, descriptive, keyword-rich.
   - Example: `/blog/how-to-choose-cotton-tshirt`
   - Use hyphens, not underscores.
   - Keep under 60 characters.

5. **Article Schema**: Set to `Article` type in Rank Math Schema.
   - Include: headline, image, datePublished, dateModified, author, publisher.

6. **FAQPage Schema**: If article has FAQ section, enable FAQPage schema.
   - Each Q&A must be visible on the page.
   - Use Rank Math FAQ block or manual JSON-LD.

7. **BreadcrumbList Schema**: Auto-generated by Rank Math breadcrumbs.

8. **OpenGraph**: Title, description, and image for Facebook sharing.
9. **Twitter Card**: Title, description, and image for Twitter sharing.
10. **Robots Meta**: `index, follow` for all published articles.

### Rank Math Score Target
- Aim for 80+/100 on Rank Math analysis (100/100 is NOT required).
- Content quality and user value matter more than perfect scores.
- Do NOT stuff keywords to improve scores.

## Scheduled Publishing Configuration

### WordPress Built-in Scheduling
WordPress supports scheduling posts for future publication:
- Set post status to `future` with a specific date/time.
- WordPress cron (wp-cron) automatically publishes the post at the scheduled time.
- No external scheduler needed.

### Scheduling Strategy for Initial Batch
When generating articles during site build:

1. **Ask the user for scheduling preferences**:
   - How many articles per week? (default: 2-3)
   - What days of the week? (default: Tuesday, Thursday)
   - What time of day? (default: 9:00 AM in target market timezone)
   - How many articles in the initial batch? (default: 10-20)

2. **Calculate publish schedule**:
   - First article: publish immediately (after user review) or schedule for the next publishing day.
   - Subsequent articles: schedule at the configured frequency.
   - Ensure continuous publishing: daily, weekly, monthly coverage for at least 3-6 months.

3. **Example schedule** (3 articles/week, 20 articles):
   - Article 1: Tuesday, Week 1, 9:00 AM
   - Article 2: Thursday, Week 1, 9:00 AM
   - Article 3: Saturday, Week 1, 9:00 AM
   - Article 4: Tuesday, Week 2, 9:00 AM
   - ... and so on for 6-7 weeks

4. **All articles are created as drafts first**. Only after user review and approval are they set to `future` status with the scheduled date.

### Timezone Considerations
- Use the target market's timezone, NOT the server timezone.
- Configure WordPress timezone in Settings → General → Timezone to match the target market.
- Example: If targeting US East Coast, set timezone to "America/New_York".
- Example: If targeting Germany, set timezone to "Europe/Berlin".

### Continuous Publishing Plan
After the initial batch is scheduled:
- Inform the user when the initial batch will run out.
- Suggest generating the next batch before the current one ends.
- Track which topics have been covered to avoid repetition.
- Maintain a content calendar in the site config.

## Article Content Quality Standards (Google E-E-A-T)

### Experience
- Include first-hand product knowledge (features, use cases, comparisons).
- Reference actual product specifications from the WooCommerce store.
- Include practical advice based on product characteristics.

### Expertise
- Write with depth about the product category.
- Demonstrate knowledge of materials, features, and use cases.
- Include technical specifications where relevant.

### Authoritativeness
- Add author bylines with bio links.
- Link to authoritative external sources for claims.
- Reference the brand's expertise in the product category.

### Trustworthiness
- No exaggerated or unsupported claims.
- No fake reviews or testimonials.
- Disclose any affiliate relationships.
- Include accurate product information (prices, availability).

### Content Quality Checklist
- [ ] Original content (not scraped or rewritten from other sites)
- [ ] Substantial, comprehensive coverage of the topic
- [ ] Clear structure with headings and paragraphs
- [ ] No spelling or grammar errors
- [ ] No keyword stuffing
- [ ] No AI-generated bulk content without human value-add
- [ ] Includes first-hand product knowledge
- [ ] Provides actionable advice
- [ ] Answers the user's search intent
- [ ] Includes relevant product images
- [ ] Includes relevant internal links
- [ ] Mobile-readable formatting

## Article Generation Workflow (Step by Step)

### Phase 1: Planning
1. Review site_config: products, categories, target market, language, SEO keywords.
2. Generate a list of 10-20 article topics (diverse types, all product-relevant).
3. Assign a unique primary keyword to each article.
4. Create a content calendar with scheduled publish dates.
5. Present the plan to the user for approval.

### Phase 2: Generation (Per Article)
1. Write the article content following the structure template.
2. Select 4-8 real product images from the media library.
3. Add 3-5 product internal links with descriptive anchor text.
4. Write Rank Math SEO title, meta description, focus keyword.
5. Set article category and tags.
6. Add FAQ section with FAQPage schema.
7. Add author byline.
8. Set featured image (real product image, WebP).
9. Create the article as `draft` in WordPress.

### Phase 3: Review
1. Send draft link to user.
2. Wait for user feedback.
3. Make revisions if requested.
4. Re-send if revised.

### Phase 4: Scheduling and Publishing
1. After user approval, set the scheduled publish date.
2. Change status from `draft` to `future` (for scheduled) or `publish` (for immediate).
3. Verify the article appears in the sitemap.
4. Verify the article URL works (for published articles).
5. Confirm to the user.

### Phase 5: Post-Publishing
1. Submit the article URL to Google Search Console (URL Inspection).
2. Submit to Bing Webmaster Tools (URL Submission).
3. Share on social media (if configured).
4. Monitor performance in Search Console after 1-2 weeks.
5. Update internal links from other articles to the new article.

## Article Category and Tag Strategy

### Categories
- Create 3-5 blog categories aligned with product categories.
- Example: "Buying Guides", "Product Care", "Industry Trends", "How-To", "Comparisons".
- Each article is assigned to ONE primary category.
- Categories should be broad enough for multiple articles.

### Tags
- Use specific tags for article topics (not categories).
- Example: "cotton-tshirt", "summer-fashion", "gift-guide".
- 3-5 tags per article.
- Tags help with internal linking and topic clustering.
- Don't create too many tags — reuse existing ones.

## Author Profiles (E-E-A-T)

### Author Setup
- Create WordPress user accounts for article authors.
- Add author bio with expertise credentials.
- Link to author pages with background information.
- Add author social profiles (sameAs schema).
- Use Rank Math Person schema for author pages.

### Guest Authors
- If using guest authors, verify their credentials.
- Add bylines with author background.
- Don't fabricate author expertise.

## Article Performance Monitoring

### Metrics to Track
- Organic impressions (Google Search Console)
- Organic clicks (Google Search Console)
- Average position (Google Search Console)
- Click-through rate (Search Console)
- Time on page (Google Analytics)
- Bounce rate (Google Analytics)
- Internal link clicks (Google Analytics)

### Content Refresh Strategy
- Review article performance every 3 months.
- Update content with new information, products, or images.
- Update the `dateModified` field in Article schema.
- Don't change the publish date without significant content changes.
- Remove or redirect underperforming articles.

## Common Article SEO Mistakes to Avoid

- Keyword cannibalization (multiple articles targeting the same keyword)
- Thin content (under 300 words with no value)
- Duplicate content across articles
- Missing ALT text on images
- Missing internal links to products
- Missing Rank Math SEO metadata
- No author byline (E-E-A-T issue)
- No FAQ schema (missed rich results opportunity)
- No featured image (poor social sharing)
- Using stock images instead of real product images
- Links to 404 pages or unpublished products
- Publishing without user review
- Scheduling articles without timezone consideration
- Not submitting new articles to Search Console

## FAQPage Schema JSON-LD Example

When an article includes an FAQ section, the FAQPage schema must be added so Google can display rich results in search. Rank Math can generate this automatically via its FAQ block, but the agent may also inject the JSON-LD manually via a Code Snippet or the post meta.

### Manual JSON-LD Template
```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How should a cotton t-shirt fit?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A cotton t-shirt should fit snugly across the shoulders without restricting movement. The sleeve seam should sit at the edge of your shoulder, and the hem should fall just below the belt line."
      }
    },
    {
      "@type": "Question",
      "name": "Can I machine wash a premium cotton t-shirt?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Machine wash in cold water on a gentle cycle, and tumble dry on low or hang to dry to preserve the fabric and color."
      }
    }
  ]
}
```

### Rules for FAQ Schema
- Every question in the JSON-LD MUST be visibly rendered on the page with the matching answer text.
- Do not include questions that are not shown to the user.
- Keep answers concise (50-100 words is ideal for rich results).
- Do not use FAQ schema for promotional content only; answers must be genuinely informative.
- Re-validate the schema in Google's Rich Results Test after publishing.

## Article Schema JSON-LD Example

### Manual Article Schema Template
```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "How to Choose a Cotton T-Shirt: Complete Guide",
  "image": [
    "https://site.com/wp-content/uploads/2026/01/premium-cotton-tshirt-navy-blue.webp"
  ],
  "datePublished": "2026-01-14T09:00:00-05:00",
  "dateModified": "2026-01-14T09:00:00-05:00",
  "author": {
    "@type": "Person",
    "name": "Jane Doe",
    "url": "https://site.com/author/jane-doe/"
  },
  "publisher": {
    "@type": "Organization",
    "name": "BrandName",
    "logo": {
      "@type": "ImageObject",
      "url": "https://site.com/wp-content/uploads/logo.png"
    }
  }
}
```

### Rules for Article Schema
- `datePublished` must reflect the original publish date and must not change on minor edits.
- `dateModified` must be updated whenever the article content is meaningfully revised.
- The `headline` should match (or be very close to) the on-page H1 and the SEO title.
- The `image` must be a real, accessible image URL (use the featured image at minimum).
- The author must be a real WordPress user with a complete bio page.

## Sample Article Outline (Full Example)

Below is a complete, concrete outline the agent can use as a model when generating a real article. It demonstrates the structure, image placement, internal links, and FAQ schema integration described above.

### Article Metadata
- **Primary keyword**: how to choose a cotton t-shirt
- **Secondary keywords**: premium cotton tee, t-shirt fabric guide, t-shirt fit guide
- **SEO title**: How to Choose a Cotton T-Shirt: Complete Guide | BrandName
- **Meta description**: Learn how to choose the perfect cotton t-shirt with our complete guide. Compare fabrics, fits, and care tips. Shop premium tees at BrandName today.
- **URL slug**: `/blog/how-to-choose-cotton-tshirt`
- **Category**: Buying Guides
- **Tags**: cotton-tshirt, fit-guide, fabric-guide
- **Word count target**: ~1,200 words

### Outline
1. **H1**: How to Choose a Cotton T-Shirt: The Complete Guide
   - Intro paragraph (primary keyword in first 100 words, states audience and value).
   - Key takeaway box: "Match fabric weight to climate, choose a fit for your body type, and check seam quality."
2. **H2**: Why Cotton T-Shirt Quality Matters
   - 2 paragraphs on fabric quality and longevity.
   - Inline product image (lifestyle shot).
3. **H2**: Cotton Fabric Types Explained
   - Comparison table: combed cotton, ringspun cotton, organic cotton, pima cotton.
   - Product image (fabric close-up).
   - Internal link callout: Premium Cotton T-Shirt.
4. **H2**: How to Pick the Right T-Shirt Fit
   - Bullet list: slim fit, regular fit, relaxed fit.
   - Product image (model wearing product).
   - Internal link callout: Relaxed Fit Cotton Tee.
5. **H2**: Common T-Shirt Buying Mistakes
   - 4-5 bullet points with practical advice.
6. **H2**: Frequently Asked Questions
   - 4 Q&A pairs (each also rendered visibly for FAQ schema).
7. **H2**: Conclusion
   - Summary + CTA.
   - Final internal link callout: Shop All Cotton T-Shirts.
8. **Author bio box** with E-E-A-T signals.

## Content Calendar Template

A content calendar keeps article generation organized and prevents topic repetition. Store it in the site config or a shared sheet.

### Calendar Fields
- **Article ID**: Unique identifier (e.g., ART-001).
- **Title**: Working title.
- **Type**: Buying guide, comparison, how-to, list, deep dive, trend, seasonal, problem-solving, gift guide, FAQ, maintenance, behind-the-scenes.
- **Primary keyword**: The focus keyword.
- **Category**: Blog category.
- **Status**: planned, drafting, draft-ready, in-review, approved, scheduled, published.
- **Draft URL**: wp-admin draft link once created.
- **Scheduled date**: Target publish date/time in target-market timezone.
- **Author**: Assigned author.
- **Linked products**: Product slugs the article links to.
- **Notes**: Any special instructions.

### Example Calendar Row
```
ART-001 | How to Choose a Cotton T-Shirt | Buying guide | how to choose a cotton t-shirt | Buying Guides | scheduled | https://site.com/wp-admin/post.php?post=123&action=edit | 2026-01-14 09:00 America/New_York | Jane Doe | cotton-tshirt-navy, cotton-tshirt-white | First article in pillar cluster
```

## Multilingual Article Considerations

When the site targets multiple languages or regions:

- Generate a separate article per language; do not auto-translate with low-quality machine translation without human review.
- Use WPML or Polylang to link translated articles as translations of each other.
- Set the `hreflang` tags correctly so Google serves the right language version.
- Adapt examples, currency, units, and seasonal references to the target locale.
- Match the brand voice per language (formal German vs. casual English, for example).
- Re-verify Rank Math metadata for each language version (titles and descriptions should be localized, not translated literally).
- Re-select product images if the locale has different product variants.
- Confirm internal links point to the same-language product pages.

## WordPress REST API for Article Creation

The agent can create draft articles programmatically via the WordPress REST API. This is useful for batch generation.

### Endpoint
- `POST /wp-json/wp/v2/posts`

### Required Fields
- `title`: The article title (H1).
- `content`: The full HTML body (with images, links, headings).
- `status`: Set to `draft` initially.
- `categories`: Array of category IDs.
- `tags`: Array of tag IDs.
- `featured_media`: The media ID of the featured image.
- `slug`: The URL slug.
- `date`: The scheduled date (only applied once status changes to `future`).
- `author`: The author user ID.

### Rank Math Meta (via REST or post meta)
- `rank_math_title`: SEO title.
- `rank_math_description`: Meta description.
- `rank_math_focus_keyword`: Focus keyword.
- `rank_math_robots`: Robots directives (e.g., `index, follow`).
- `rank_math_schema_article`: Article schema JSON.
- `rank_math_schema_faq`: FAQPage schema JSON.

### Workflow Notes
- Always create the article as `draft` first, regardless of the intended publish date.
- Only switch to `future` (scheduled) or `publish` after the user approves.
- After creation, fetch the post ID and build the draft preview URL for the user.
- Verify the featured image and inline images are correctly attached (no broken images).

## Image Optimization Best Practices

Beyond the basic image requirements above, follow these optimization rules:

### Format and Compression
- Convert all product images to WebP before uploading (or use a plugin that serves WebP).
- Keep file sizes under 200 KB for content images and under 300 KB for the featured image where possible.
- Use lossy compression for photographs; lossless for images with sharp edges or text.

### Dimensions and Aspect Ratios
- Featured image: 1200x630px (social/OG optimal).
- Inline content images: max width 1200px, variable height, but always specify width/height attributes.
- Use responsive `srcset` where the theme supports it.

### ALT Text Rules
- Describe the image accurately; do not stuff keywords.
- Include the product name and a key attribute (color, material, feature).
- Example: "Premium cotton t-shirt in navy blue, front view on wooden hanger."
- Never leave ALT text empty for product images.

### Filename Rules
- Use lowercase, hyphenated, descriptive filenames.
- Example: `premium-cotton-tshirt-navy-blue-front.webp`.
- Never upload files named like `IMG_1234.jpg` or `screenshot.png`.

### Performance
- Lazy-load all below-the-fold images.
- Preload the featured image (above the fold) for fast LCP.
- Serve images from the same domain (avoid third-party CDNs unless configured).

## Internal Linking Strategy Deep Dive

Internal links distribute ranking power and help users discover products. Treat them as a first-class SEO asset.

### Anchor Text Guidelines
- Use descriptive, keyword-relevant anchor text.
- Vary anchor text across articles that link to the same product.
- Avoid generic anchors like "click here" or "read more".
- Keep anchor text natural within the sentence.

### Link Placement Hierarchy
1. **Contextual inline links**: Within relevant paragraphs (highest value).
2. **Callout boxes**: Styled boxes with product image + name + price + button.
3. **Comparison tables**: Product name cells linking to product pages.
4. **Related articles section**: Links to other blog posts at the bottom.
5. **Author bio / CTA**: Final link near the conclusion.

### Topic Clusters
- **Pillar article**: A comprehensive guide covering a broad topic (e.g., "The Ultimate Cotton T-Shirt Guide").
- **Supporting articles**: Narrower articles that link up to the pillar (e.g., "Cotton Fabric Types Explained").
- **Product pages**: Supporting articles link down to relevant product pages.
- Every supporting article should link to the pillar and to at least one product page.
- The pillar should link to all supporting articles.

### Orphan Prevention
- No article should have zero incoming internal links.
- After publishing a new article, add at least one link to it from an existing article or the pillar.
- Run a quarterly internal link audit to find and fix orphaned articles.

## Pillar Content and Topic Clusters

### Building a Cluster
1. Identify a broad topic aligned with a product category (the pillar).
2. Write one comprehensive pillar article (2,000+ words).
3. Generate 5-10 supporting articles, each targeting a sub-topic and a unique keyword.
4. Interlink: pillar → supporting, supporting → pillar, supporting → product pages.
5. Add a hub section on the pillar page listing all supporting articles.

### Cluster Example (Cotton T-Shirts)
- **Pillar**: The Ultimate Cotton T-Shirt Guide
- **Supporting**:
  - How to Choose a Cotton T-Shirt (buying guide)
  - Combed vs. Ringspun Cotton: What's the Difference? (comparison)
  - How to Care for Your Cotton T-Shirt (maintenance)
  - Top 10 Cotton Tees for Summer (list)
  - Why Fabric Weight Matters in T-Shirts (deep dive)
- **Products**: Each supporting article links to 2-3 relevant product pages.

## Troubleshooting Common Issues

### Article Won't Publish at Scheduled Time
- Verify WordPress timezone matches the target market.
- Verify wp-cron is not disabled; if disabled, set up a real cron job.
- Confirm the post status is `future`, not `draft`.
- Confirm the scheduled date is in the future, not in the past.

### Rank Math SEO Score Is Low
- Check that the focus keyword appears in title, meta description, URL, first paragraph, an H2, and an image ALT.
- Check content length meets the 800-word minimum.
- Ensure there is at least one internal link and one external link.
- Do NOT stuff keywords to chase a perfect score; aim for 80+.

### Images Not Displaying
- Verify the image URL returns 200 (no 404).
- Verify the image was uploaded to the media library (not hotlinked).
- Verify the image is WebP and the server serves the correct MIME type.
- Check that lazy-load scripts are not hiding above-the-fold images.

### FAQ Rich Results Not Appearing
- Re-run the Rich Results Test on the published URL.
- Confirm every question in the JSON-LD is visible on the page.
- Confirm answers are not empty.
- Confirm the page is indexed in Google Search Console.

### Internal Links Returning 404
- Confirm the target product is published (not draft/trash).
- Confirm the slug in the link matches the product's current slug.
- If a product slug changed, update all article links pointing to it.
- Add a redirect plugin to catch any stale links.

## Glossary

- **Pillar article**: A comprehensive, long-form article that serves as the hub of a topic cluster.
- **Topic cluster**: A group of interlinked articles around a central topic, plus their product pages.
- **Focus keyword**: The primary keyword targeted by an article in Rank Math.
- **Keyword cannibalization**: When two or more articles compete for the same keyword in search.
- **Orphan article**: An article with no incoming internal links from other pages.
- **Featured image**: The representative image shown in listings, social shares, and at the top of the article.
- **FAQPage schema**: Structured data that enables FAQ rich results in Google search.
- **Article schema**: Structured data describing a news/article-type page for search engines.
- **wp-cron**: WordPress's built-in task scheduler used to publish scheduled posts.
- **`future` status**: The WordPress post status for a post scheduled to publish at a future date/time.
- **`draft` status**: The WordPress post status for an unpublished post under review.
- **hreflang**: An HTML attribute that tells Google the language and region of a page, used for multilingual sites.
- **E-E-A-T**: Google's quality framework: Experience, Expertise, Authoritativeness, Trustworthiness.
- **Callout box**: A visually styled block in an article that highlights a product link with image, name, price, and button.
- **WebP**: A modern image format that provides superior compression for web images.
