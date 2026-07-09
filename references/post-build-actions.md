# Post-Build Actions Guide

## Overview

After the website build is complete and QA passes, the agent MUST present a post-build actions checklist to the user. These actions are critical for long-term SEO success, content continuity, and site growth. The agent must NOT skip this step or assume the user knows what to do next.

Read this reference after completing Phase 21 (Prepare sitemap/indexing package) of the standard workflow. Also read `scheduled-article-publishing.md` for article generation details.

## Post-Build Action Presentation

When presenting post-build actions to the user, use this format:

```
Your website build is complete and has passed QA. Here are the recommended next steps to ensure long-term SEO success:

1. [Scheduled Article Publishing Plan] - Set up ongoing content publishing
2. [Search Engine Index Submission] - Submit your site to Google and Bing
3. [Analytics and Monitoring Setup] - Track your site's performance
4. [Social Media Auto-Sharing] - Automatically share new content on social media

Would you like me to help with any of these? I can walk you through each step.
```

Wait for the user to choose which actions to proceed with. Do NOT start any action without user confirmation.

## Action 1: Scheduled Article Publishing Plan

### What to Tell the User
"Your site has [N] articles published and [M] articles scheduled. To maintain SEO momentum, you should have a continuous publishing plan. I can help you:

1. Generate the next batch of articles (10-20 articles)
2. Set up a publishing schedule (e.g., 2-3 articles per week)
3. Plan article topics based on your products and market

Would you like me to generate more articles now?"

### Information to Collect from User
- How many articles per week? (default: 2-3)
- What days to publish? (default: Tuesday, Thursday)
- What time to publish? (default: 9:00 AM target market timezone)
- How many articles in the next batch? (default: 10-20)
- Any specific topics they want covered?
- Any topics to avoid?

### What to Do After User Confirms
1. Read `scheduled-article-publishing.md` for the full workflow.
2. Generate article topic list and present to user for approval.
3. Generate articles as drafts.
4. Send draft links to user for review.
5. After approval, schedule publish dates.
6. Ensure continuous publishing for at least 3-6 months.

### Content Calendar Tracking
Maintain a content calendar in the site config:
```json
{
  "content_calendar": {
    "published": [{"title": "...", "url": "...", "date": "2025-01-15"}],
    "scheduled": [{"title": "...", "url": "...", "date": "2025-01-22"}],
    "planned": [{"title": "...", "keyword": "...", "type": "guide"}],
    "schedule": {"frequency": "3x_week", "days": ["Tuesday", "Thursday", "Saturday"], "time": "09:00", "timezone": "America/New_York"}
  }
}
```

### Reminder Schedule
- When the current batch has 2 weeks of articles remaining, remind the user to generate the next batch.
- Track which topics have been covered to suggest new angles.
- Suggest seasonal content 4-6 weeks before major holidays/events in the target market.

## Action 2: Search Engine Index Submission

### What to Tell the User
"Your sitemap is ready at [sitemap URL]. To get your site indexed by Google and Bing, you need to:

1. Submit your sitemap to Google Search Console
2. Submit your sitemap to Bing Webmaster Tools
3. Request indexing for your most important pages

Would you like me to guide you through this process?"

### Google Search Console Setup
1. **Verify ownership**: 
   - If Rank Math Webmaster Tools verification is already set up, ownership is verified.
   - Otherwise, guide user through verification methods (HTML tag, DNS, Google Analytics).
2. **Submit sitemap**:
   - Go to Google Search Console → Sitemaps
   - Enter `sitemap_index.xml` and click Submit.
3. **Request indexing for key pages**:
   - Use URL Inspection tool for: Homepage, Shop, top 5 product pages, top 3 blog posts.
   - Click "Request Indexing" for each.
4. **Monitor**:
   - Check Coverage report in 1-2 weeks.
   - Check Performance report in 2-4 weeks for impressions and clicks.

### Bing Webmaster Tools Setup
1. **Add site**: Go to Bing Webmaster Tools → Add Site.
2. **Verify ownership**: Use the same HTML tag or DNS method as Google.
3. **Submit sitemap**: Enter sitemap URL.
4. **Submit URLs**: Use URL Submission API or Bulk URL Submission for key pages.
5. **Enable IndexNow**: If Rank Math Instant Indexing module is enabled, Bing is auto-notified of new content.

### Indexing Checklist
- [ ] Google Search Console ownership verified
- [ ] Google Search Console sitemap submitted
- [ ] Google Search Console key pages requested for indexing
- [ ] Bing Webmaster Tools ownership verified
- [ ] Bing Webmaster Tools sitemap submitted
- [ ] Bing Webmaster Tools key pages submitted
- [ ] IndexNow enabled (via Rank Math Instant Indexing)
- [ ] robots.txt accessible at `/robots.txt`
- [ ] sitemap accessible at `/sitemap_index.xml`
- [ ] No noindex on important pages

### Ongoing Indexing
- Submit new articles to Google Search Console after publishing.
- Submit new products to Google Search Console.
- Monitor Search Console for indexing errors.
- Fix any coverage issues reported by Search Console.

## Action 3: Analytics and Monitoring Setup

### What to Tell the User
"To track your site's performance and SEO progress, you should set up analytics and monitoring:

1. Google Analytics 4 (GA4) for traffic and user behavior
2. Google Search Console for search performance
3. Rank Math Analytics integration
4. Rank Math SEO Analysis (periodic site audits)

Would you like me to help configure any of these?"

### Google Analytics 4 Setup
1. **Create GA4 property**: Go to analytics.google.com → Admin → Create Property.
2. **Set up data stream**: Add Web stream with site URL.
3. **Install tracking**: 
   - Option A: Use Google Site Kit plugin (recommended for beginners).
   - Option B: Use Rank Math Analytics module.
   - Option C: Manual GA4 tag in header.
4. **Configure enhanced measurement**: Enable page views, scrolls, outbound clicks, site search, video engagement, file downloads.
5. **Set up conversions**: Track purchase (WooCommerce), contact form submission, newsletter signup.
6. **Link to Search Console**: GA4 → Admin → Property Settings → Search Console Links.

### Google Search Console Monitoring
Key reports to monitor weekly:
1. **Performance**: Impressions, clicks, CTR, average position.
2. **Coverage**: Indexed pages, errors, excluded pages.
3. **Core Web Vitals**: LCP, INP, CLS status.
4. **Mobile Usability**: Mobile-friendly issues.
5. **Rich Results**: Schema markup validity.
6. **Sitemaps**: Sitemap submission status and errors.

### Rank Math Analytics Configuration
1. Enable Analytics module in Rank Math Dashboard.
2. Connect Google Search Console account.
3. Connect Google Analytics account (optional).
4. View keyword rankings in Rank Math → Analytics.
5. Monitor 12-month keyword ranking history (Pro).

### Periodic SEO Audits
- Run Rank Math SEO Analysis every month.
- Fix high-priority issues identified by the audit.
- Monitor PageSpeed Insights scores quarterly.
- Review and update underperforming content every 3 months.

### Monitoring Checklist
- [ ] GA4 property created and tracking installed
- [ ] GA4 linked to Google Search Console
- [ ] Rank Math Analytics connected to Search Console
- [ ] WooCommerce conversion tracking set up
- [ ] Search Console monitored weekly
- [ ] Rank Math SEO Analysis run monthly
- [ ] PageSpeed Insights checked quarterly
- [ ] Core Web Vitals monitored in Search Console
- [ ] Content performance reviewed every 3 months

### Alert Configuration
Set up alerts for:
- Server downtime or 500 errors.
- SSL certificate expiration.
- Core Web Vitals regression.
- Search Console manual actions.
- Significant traffic drops.
- Broken links (404 errors).

## Action 4: Social Media Auto-Sharing

### What to Tell the User
"To drive traffic from social media, you can automatically share new blog articles and products on your social media profiles:

1. Set up auto-sharing for new blog posts
2. Configure social media profiles in Rank Math
3. Set up OpenGraph and Twitter Card meta tags (already configured)

Would you like me to help set up social media auto-sharing?"

### Social Media Profile Setup
1. **Rank Math Social Meta**:
   - Go to Rank Math → General Settings → Social.
   - Add Facebook profile URL.
   - Add Twitter profile URL.
   - Add Instagram, LinkedIn, Pinterest, YouTube URLs.
   - Set default social share image.

2. **OpenGraph Configuration** (already done during build):
   - Verify Facebook OpenGraph tags are present on all pages.
   - Test with Facebook Sharing Debugger: https://developers.facebook.com/tools/debug/
   - Ensure each article has a unique social share image.

3. **Twitter Card Configuration** (already done during build):
   - Verify Twitter Card tags are present.
   - Test with Twitter Card Validator.
   - Use `summary_large_image` card type for articles.

### Auto-Sharing Plugins
Recommend one of these plugins for auto-sharing:
1. **Revive Old Posts** (free/paid): Auto-shares new and old blog posts to Facebook, Twitter, LinkedIn.
2. **Blog2Social** (free/paid): Auto-posts to Facebook, Twitter, LinkedIn, Instagram, Pinterest.
3. **Jetpack Publicize** (free): Auto-shares to Facebook, Twitter, LinkedIn, Tumblr.
4. **Social Snap** (paid): Advanced social sharing and auto-posting.

### Auto-Sharing Configuration
1. Install chosen auto-sharing plugin.
2. Connect social media accounts (Facebook Page, Twitter, LinkedIn).
3. Configure auto-share settings:
   - Share new posts immediately on publish.
   - Share scheduled posts at their publish time.
   - Add custom message template with post title and link.
   - Add hashtags based on post tags.
   - Schedule resharing of old posts (Revive Old Posts feature).
4. Test with a sample post.

### Social Media Checklist
- [ ] Rank Math social profiles configured
- [ ] OpenGraph tags verified (Facebook Sharing Debugger)
- [ ] Twitter Card tags verified (Twitter Card Validator)
- [ ] Auto-sharing plugin installed and configured
- [ ] Social media accounts connected
- [ ] Auto-share tested with sample post
- [ ] Hashtag strategy defined
- [ ] Social share buttons on blog posts (floating or inline)
- [ ] Social share buttons on product pages

### Pinterest-Specific Setup (for visual products)
- Enable Rich Pins for Pinterest.
- Verify site on Pinterest.
- Add Pin It buttons on product images.
- Create Pinterest boards aligned with product categories.
- Auto-pin new product images and blog images.

## Post-Build Action Summary Checklist

Present this final checklist to the user:

```
=== POST-BUILD ACTIONS CHECKLIST ===

CONTENT:
[ ] Initial article batch generated and reviewed
[ ] Articles scheduled for continuous publishing (3-6 months)
[ ] Content calendar maintained
[ ] Next article batch planned

INDEXING:
[ ] Google Search Console verified and sitemap submitted
[ ] Bing Webmaster Tools verified and sitemap submitted
[ ] Key pages requested for indexing
[ ] IndexNow enabled via Rank Math

ANALYTICS:
[ ] Google Analytics 4 installed and configured
[ ] Search Console linked to GA4
[ ] Rank Math Analytics connected
[ ] WooCommerce conversion tracking set up
[ ] Monitoring routine established (weekly Search Console check)

SOCIAL MEDIA:
[ ] Social profiles configured in Rank Math
[ ] OpenGraph and Twitter Card tags verified
[ ] Auto-sharing plugin installed and configured
[ ] Social share buttons on blog and product pages

ONGOING:
[ ] Monthly Rank Math SEO Analysis audit
[ ] Quarterly PageSpeed Insights check
[ ] Quarterly content performance review
[ ] Content refresh for underperforming articles
=== END POST-BUILD ACTIONS ===
```

## Important Notes

- Do NOT start any post-build action without explicit user confirmation.
- Walk the user through each step they choose.
- Provide direct links to tools (Search Console, GA4, etc.).
- Offer to help with technical configuration where possible.
- Remind the user of upcoming content schedule gaps.
- Check in periodically on indexing status and analytics data.
- Suggest content refreshes for articles older than 6 months.
- Alert the user to any Search Console errors or manual actions.
