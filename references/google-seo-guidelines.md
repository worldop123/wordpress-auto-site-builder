# Google SEO Official Guidelines

> A comprehensive, encyclopedia-level reference covering ALL official Google SEO knowledge, sourced from Google Search Central documentation. This reference is part of the WordPress Auto Site Builder skill and should be consulted when building, optimizing, or auditing WordPress sites for Google Search.

---

## Google Search Fundamentals

- Google is a fully automated search engine that uses crawlers to continuously browse the web.
- Most sites in Google search results are automatically found and added during crawling — manual submission is rarely required.
- Changes to a site may take anywhere from hours to months to reflect in search results; generally wait weeks before evaluating the impact of a change.
- Check if Google found your content using the `site:` search operator (e.g., `site:example.com`).
- Google finds pages primarily through links from other crawled pages.
- Submit sitemaps (not mandatory but helpful) — many CMS platforms do this automatically.
- Google Search Console is the official tool for monitoring how Google sees your site.

---

## How Google Search Works

Google Search operates in three primary stages:

1. **Crawling** — Automated crawlers (Googlebot) visit known pages and follow links to discover new pages.
2. **Indexing** — Google analyzes the text, images, and video on a page and stores the information in the Google index.
3. **Serving/Ranking** — When a user queries Google, the search engine returns the most relevant, high-quality results from the index.

Key facts:

- Googlebot crawls from a US location typically.
- Google needs access to the same resources as user browsers (CSS, JavaScript, images). Blocking these resources can prevent proper rendering.
- Check what Google sees using the Search Console **URL Inspection tool** (which shows the rendered DOM, loaded resources, and HTTP response).
- Crawling is not guaranteed for every URL discovered; Google prioritizes crawl budget based on factors like server response time, site quality, and update frequency.
- Crawling is performed by multiple Googlebot user agents (e.g., `Googlebot` for desktop, `Googlebot-Smartphone` for mobile, `Googlebot-Image`, `Googlebot-News`, `Googlebot-Video`).
- The **mobile-first indexing** approach means Google predominantly uses the mobile version of the content for indexing and ranking.
- Indexing is not guaranteed even after crawling — Google only indexes content it determines is high-quality and canonical.

---

## Site Organization

### Descriptive URLs

- URL parts can appear as breadcrumbs in search results, helping users understand the page's place within a site.
- Include useful words in URLs: `https://www.example.com/pets/cats.html`
- Avoid random identifier URLs: `https://www.example.com/2/6772756D707920636174`
- Use hyphens (`-`) rather than underscores (`_`) to separate words — Google treats hyphens as word separators.

### Directory Structure

- Group similar pages in directories to help Google understand change frequency.
- Example: `/policies/` rarely changes, `/promotions/` changes frequently.
- A logical directory structure helps Google crawl efficiently and is especially important for large ecommerce sites.
- Shallow directory structures (fewer levels) are generally preferable, but logical grouping matters more than absolute depth.

### Reducing Duplicate Content

- Duplicate content is **not** a policy violation, but it causes a poor user experience and can dilute ranking signals.
- Google selects a canonical URL for groups of duplicate content automatically.
- Use **301 redirects** or `rel="canonical"` link elements to signal your preferred version.
- Ensure each content piece is accessible via one URL when possible (e.g., avoid serving the same article on multiple URLs).
- Use the Search Console **URL parameter tool** to control crawling of URL parameters that produce duplicate content.

---

## Creating Helpful, Reliable, People-First Content

Google rewards content created primarily to benefit people, not search engines. The following self-assessment questions are taken directly from Google's guidance.

### Content Quality Self-Assessment Questions

- Does the content provide original information, reporting, research, or analysis?
- Does the content provide a substantial, complete, or comprehensive description of the topic?
- Does the content provide insightful analysis or interesting information that is beyond the obvious?
- If the content draws from other sources, does it provide substantial additional value and originality, rather than simply copying or rewriting?
- Does the title and/or page heading provide a descriptive, helpful summary of the content (for example, a title that reflects the topic or a summary of an answer)?
- Is the title and/or page heading accurate and not exaggerated or shocking?
- Is this the sort of page you'd want to bookmark, share with a friend, or recommend?
- Would you expect to see this content in or referenced by a printed magazine, encyclopedia, or book?
- Does the content have any spelling or stylistic issues?
- Is the content well-produced, or does it appear hastily produced?

### Expertise Self-Assessment Questions

- Does the content present information in a way that makes you want to trust it, such as clear sourcing, evidence of the expertise involved, background about the author or the site that publishes it?
- If someone researched the site producing the content, would they come away with the impression that it is well-trusted or widely-recognized as an authority on its topic?
- Is this content written by an expert or enthusiast who demonstrably knows the topic well?
- Is the content free from easily verifiable factual errors?

### People-First Content Indicators (YES = good)

- Does the business/site have a clear, well-defined target audience who would find the content useful if they came directly to the site?
- Does the content demonstrate first-hand expertise and a depth of knowledge (for example, expertise that comes from having actually used a product or service, or visiting a place)?
- Does the site have a clear primary purpose or focus?
- After reading the content, would someone leave feeling they've learned enough about a topic to help achieve their goal?

### Search-Engine-First Content Warning Signs (YES = bad)

- Is the content primarily created to attract search engine visits rather than to help people?
- Are you producing large amounts of content about many different topics in the hope that some of it might perform well in search results?
- Are you using extensive automation to produce content on many topics?
- Are you mainly summarizing what others have to say without adding much value?
- Did you write content just because it seemed trendy, and not because you had anything to say about the topic?
- After reading the content, would a reader feel they need to search again to get better information from other sources?
- Are you writing to a particular word count because you've heard or read that Google has a preferred word count? (No, they don't.)
- Are you changing the dates of pages to make it seem as though the content is more recent without making significant changes to the content?

---

## E-E-A-T Framework (Experience, Expertise, Authoritativeness, Trustworthiness)

- E-E-A-T is **NOT** a direct ranking factor or an automated scoring system. However, the signals that identify good E-E-A-T content are used by Google's ranking systems.
- **Trustworthiness** is the most important member of the E-E-A-T family — it is the center of the E-E-A-T concept.
- **YMYL** (Your Money or Your Life) topics require the highest E-E-A-T standards. These include topics that could affect health, financial stability, safety, or civic stability.
- The **Search Quality Rater Guidelines** outline the criteria human raters use to evaluate Google's search results; raters do not influence individual site rankings but help Google measure algorithm quality.
- YMYL categories include: news and current events, civics/government/law, finance, shopping, health and safety, people in groups, and "other" (e.g., fitness, nutrition, housing, admissions).
- For YMYL topics, the threshold for trust and authoritativeness is significantly higher than for non-YMYL topics.
- E-E-A-T applies to the **page level**, the **content creator (author) level**, and the **website level**. A site can be authoritative on one topic but not another.

### The "Who, How, Why" Framework

#### WHO (Content Creator)

- Is it obvious to visitors who created the content?
- Are bylines displayed prominently and consistently?
- Do bylines provide background information about the authors and their expertise?
- Add accurate author information with visible, descriptive bylines.
- For editorial/news content, providing author information helps establish trust.

#### HOW (How Content Was Created)

- **Product reviews:** Show the quantity of items tested, present results, explain testing methods with evidence (photos, video).
- **AI-generated content:** Disclose automation or AI use when readers would reasonably expect it.
- Provide background on how automation or AI was used in producing the content.
- Explain why automation or AI was beneficial for the content creation process.
- Using automation (including AI) whose **primary purpose** is to manipulate search rankings violates Google's spam policies.

#### WHY (Why Content Was Created)

- The primary reason for creating content should be to **benefit users**.
- Content created primarily to attract search engines will not be rewarded.
- Using AI primarily to manipulate search rankings violates spam policies — this is true regardless of the content's apparent quality.

---

## Page Experience

- Google's core ranking systems reward good page experience.
- Don't focus on just one or two aspects — aim for an **overall** good experience.
- Page experience is one of many ranking signals; great content still matters most.

### Core Web Vitals

Core Web Vitals are field-measured metrics that quantify real user experience. They are the headline components of page experience.

| Vital | Measures | Good Target | Poor |
|-------|----------|-------------|------|
| **LCP** (Largest Contentful Paint) | Loading performance | Under **2.5 seconds** | Over 4.0s |
| **INP** (Interaction to Next Paint) | Responsiveness to user input | Under **200 milliseconds** | Over 500ms |
| **CLS** (Cumulative Layout Shift) | Visual stability | Under **0.1** | Over 0.25 |

> Note: INP replaced FID (First Input Delay) as a Core Web Vital in March 2024.

### Other Page Experience Factors

- **HTTPS:** Pages served securely over TLS.
- **Mobile-friendly:** Content displays well and is usable on mobile devices.
- **No intrusive interstitials:** Avoid full-screen popups or ads that make content inaccessible, especially on mobile.
- **Well-designed pages:** Main content is easily distinguishable; navigation is clear.
- **Safe browsing:** Site is not flagged for malware or deceptive content.
- **HTTPS as a ranking signal:** HTTPS is a lightweight ranking signal; it is also a prerequisite for many browser features and for user trust.
- **Mobile-friendliness test:** Use the Search Console Mobile Usability report to identify pages with mobile usability issues.
- **Intrusive interstitial penalty:** Applies specifically to mobile search; covers popups that obscure main content on first interaction. Legitimate uses (cookie notices, age verification, login dialogs on non-indexed pages) are acceptable.

---

## Structured Data

- Structured data provides explicit clues about the meaning of a page to Google.
- It enables **rich results** that are more engaging and may increase interaction / click-through rates.
- Case studies: Rotten Tomatoes +25% CTR, Food Network +35% traffic, Nestle +82% CTR.
- Structured data describes things on the page (e.g., a product, a recipe, an event) and their properties.

### Supported Formats

| Format | Recommendation | Description |
|--------|----------------|-------------|
| **JSON-LD** | RECOMMENDED | JavaScript notation embedded in `<script>` tags; easiest to maintain and least prone to errors. |
| **Microdata** | Supported | HTML specification for nesting structured data within HTML content. |
| **RDFa** | Supported | HTML5 extension for linked data in HTML. |

### Guidelines

- Use the **schema.org** vocabulary, but follow **Google Search Central documentation** as the final authority on supported properties and features.
- Provide **all required properties** for a given rich result feature.
- It is better to provide fewer but complete properties than many incomplete ones.
- Use the **Rich Results Test** during development to validate markup.
- Monitor with the **Rich Results Status Report** (in Search Console) after deployment.
- The data must describe content that is **actually visible to users** on the page.
- Do **not** create empty pages solely to host structured data.
- Keep structured data in sync with the page content; mismatched data can trigger manual actions.
- Recommended structured data types for WordPress sites include: `Article`, `BreadcrumbList`, `FAQPage`, `HowTo`, `Product`, `Recipe`, `Review`, `LocalBusiness`, `Organization`, `WebSite`, and `VideoObject`.
- Use the **Data Highlighter** (in Search Console) as a no-code alternative for tagging data on simple sites, though server-side markup is more reliable and maintainable.
- Structured data violations (such as marking up content that isn't visible, or spammy markup) can result in a **manual action** reported in Search Console.

---

## Image SEO

- Images may be the first way users find your site (via Google Images search).
- Use **high-quality** images placed **near relevant text**.
- Add **descriptive alt text** using the `alt` attribute.
- Alt text helps search engines understand the image content and its relationship to the page.
- Most CMS platforms can easily assign alt text when uploading images.
- Provide descriptive filenames (e.g., `long-tailed-puppy.jpg` rather than `IMG0001.jpg`).
- Serve images in modern formats (WebP, AVIF) for better performance.
- Use responsive images (`srcset`) to deliver appropriately sized images.

---

## Video SEO

- Embed videos on **dedicated pages** near relevant text that describes the video.
- Write descriptive text in the video **title** and **description** fields.
- Apply title best practices to video titles (concise, accurate, descriptive).
- Provide a transcript when possible to make video content more discoverable.
- Use **VideoObject** structured data to help Google understand the video.
- Submit a **video sitemap** to help Google find and index your videos.

---

## Titles and Snippets

### Title Links

- Google generates the title link for a page primarily from the `<title>` element, but may also use other headings and content.
- **Good titles:** page-specific, concise, accurately describe the page content.
- Include the site/business name, location info (where relevant), and what the page offers.
- Avoid vague titles like "Home" or "Untitled"; avoid keyword stuffing in titles.
- Brand name placement (front vs. back) is a stylistic choice; both are fine.

### Meta Descriptions

- Snippets may come from the meta description tag, but Google may also generate snippets dynamically from page content.
- **Good meta descriptions:** short, page-specific, contain the most relevant information.
- One or two sentences summarizing the page — typically up to ~160 characters.
- Write unique descriptions for each page; duplicate descriptions across pages are not useful.
- Meta descriptions do not directly affect ranking but can significantly affect click-through rate.

---

## Link Best Practices

### Internal Links

- Internal links connect users and search engines to other parts of your site.
- Google discovers most new pages through links daily.
- Write **good anchor text** that describes the linked page — avoid generic anchors like "click here" or "read more."
- Use `<a href>` tags for crawlable links; Google can follow links that are standard HTML anchor tags.
- Do **not** use JavaScript event handlers on non-anchor elements (like `<div onclick>`) for navigation — Google may not discover these links.
- Ensure important pages are linked from multiple relevant places on your site.

### External Links

- Link to **trusted resources** to add value for your readers.
- Use `rel="nofollow"` (or similar) for links you don't want to endorse.
- For user-generated content (forums, comments), auto-add `nofollow` to user-posted links.
- Qualify outbound links with:
  - `rel="nofollow"` — for links you don't want to endorse.
  - `rel="sponsored"` — for paid placements or advertisements.
  - `rel="ugc"` — for user-generated content links.

---

## Ecommerce SEO

### Navigation Structure

- Recommended hierarchy: **Menu → Category pages → Subcategory pages → Product pages**.
- Ensure **all products are reachable** via navigation links (text links that Googlebot can follow).
- Googlebot typically **doesn't submit searches** to search boxes, so content only reachable via search is likely not discovered.
- Use **sitemaps** or **Google Merchant Center Feed** if not all pages are linkable via normal navigation.
- The **more internal links** pointing to a page, the higher its relative importance within your site.
- Avoid overly deep hierarchies; keep important products within a few clicks from the homepage.

### Product Pages

- Link to **bestsellers** from the homepage, blog posts, newsletters, and category pages.
- Include **structured data for products** (price, availability, ratings, reviews) to enable rich results.
- Use `<a href>` tags, **not** JavaScript events, for navigation between products.
- Provide original, useful product descriptions — avoid copying manufacturer descriptions verbatim.
- Allow customer reviews with `Review` structured data (where appropriate).

---

## Writing High-Quality Reviews

Google evaluates review content against a high standard. A high-quality review should:

- Evaluate the product from the **user's perspective**.
- Demonstrate **expert knowledge** of the subject matter.
- Provide **evidence** — images, audio, video, or links showing expertise and testing.
- Share **quantitative measurements** (e.g., test results, performance data).
- Explain **advantages over competitors** or previous versions.
- Include **comparison alternatives** so readers can make informed decisions.
- Discuss **pros and cons** based on original research and testing.
- Describe how products **evolved from previous versions** or iterations.
- Focus on the **most important decision factors** for the category.
- Link to **other useful resources** (including other sellers, when appropriate).
- Consider linking to **multiple sellers** so readers have a choice.

---

## Google Spam Policies (Must Avoid)

Violating these policies can result in lower rankings or complete removal from Google Search. Google's automated systems and manual actions both enforce these.

### Cloaking

- Showing **different content to search engines than to users**.
- Never insert text or keywords that are only shown to search engine user agents (e.g., based on detecting Googlebot).
- Cloaking is one of the most serious violations and can result in removal from the index.

### Doorway Pages

- Creating pages **solely to rank for specific queries** that funnel users to a single destination.
- Multiple sites/domains with minor changes to cover more query space.
- Pages that exist only to redirect users to another part of the site.

### Expired Domain Abuse

- Buying **expired domains** to host content unrelated to the domain's prior purpose, primarily to leverage the domain's existing ranking signals.

### Hacked Content

- Any content placed on a site without permission due to vulnerabilities:
  - **Code injection** (malicious scripts).
  - **Page injection** (new pages created by attackers).
  - **Content injection** (adding spammy text or links).
  - **Malicious redirects**.
- Site owners should promptly clean hacked content and request reconsideration after fixing.

### Hidden Text and Links

- **White text on white background.**
- Text **hidden behind images**.
- CSS **positioning text off-screen**.
- **Font size or opacity set to 0.**
- Hidden links via single small characters (e.g., a period linking to another page).
- **ACCEPTABLE techniques** (these are not violations): accordion content, tabbed interfaces, sliders, tooltips, screen-reader-only text, content that is visible on user interaction.

### Keyword Stuffing

- Lists of **phone numbers** without substantial added value.
- **City blocks of text** listing every city/region a business serves.
- **Repeated words or phrases** that read unnaturally (e.g., "cheap shoes cheap shoes buy cheap shoes").
- Keyword stuffing makes content read poorly and violates spam policies.

### Link Spam

- **Buying or selling links** for ranking purposes (including paid posts).
- **Excessive link exchanges** ("link to me and I'll link to you").
- **Automated link creation** (e.g., using tools to build links at scale).
- **Widget links** with optimized anchor text embedded in widgets distributed to other sites.
- **Forum signature links** and comment links placed at scale.
- Use `rel="nofollow"` or `rel="sponsored"` for any paid, advertised, or otherwise compensated links.

### Scaled Content Abuse

- Using **AI tools** to generate large volumes of pages without adding value for users.
- **Scraping feeds or search results** to generate pages automatically.
- **Combining content** from different pages without adding substantial additional value.
- Creating many pages with **meaningless content** but containing search keywords.
- The defining feature is scale + lack of value, regardless of whether automation or humans are involved.

### Scraping

- **Republishing content** without adding any original value or justification.
- **Copying content** with minor modifications (e.g., synonym replacement).
- **Embedding media** (images, video) from other sites without substantial value-add.
- Scraping is acceptable only when the republished content adds clear value (e.g., original commentary, curation, organization).

### Site Reputation Abuse

- Publishing **third-party content** primarily to leverage the hosting site's established ranking signals.
- Example: a respected education site hosting payday loan reviews to rank for financial queries.
- Third-party content on a site is fine when it is **closely related** to the site's purpose and the site exercises editorial oversight.

### Sneaky Redirects

- Showing search engines one thing, then **redirecting users to different content**.
- **Desktop users** see a normal page, while **mobile users** are redirected to spam.
- Redirecting based on user agent to serve Googlebot a different page than users.
- The only acceptable redirects are those that move users to equivalent content (e.g., HTTP→HTTPS, moved pages).

### Thin Affiliate Content

- Pages with **affiliate links** where the product descriptions and reviews are copied from the merchant without original content.
- Pages that add **no original content or value** beyond the affiliate links.
- **Good affiliate pages** provide: price comparisons, original reviews, hands-on testing, product navigation, and genuine value to users.

### User-Generated Spam

- Spam accounts on community platforms.
- Forum spam posts.
- Blog spam comments.
- Spammy user profiles.
- Site owners should moderate user-generated content and add `rel="ugc"` or `rel="nofollow"` to user-posted links.
- Use CAPTCHAs, rate limiting, and automated spam detection to reduce spam at scale.
- Regularly audit user-generated content and remove spam promptly.

### Additional Spam Considerations

- A **manual action** is a human reviewer's decision that a page or site violates spam policies; it is reported in Search Console under "Manual actions."
- Manual actions can affect a single page, a section of a site, or the entire site.
- After fixing a violation, submit a **reconsideration request** in Search Console; Google will review and lift the action if the issue is resolved.
- Some violations (especially severe ones like cloaking or hacking) can result in **complete removal** from Google's index.
- Spam that is algorithmically detected (rather than manually) is handled by Google's automated systems and may recover automatically once the spam is removed and recrawled.

---

## International SEO (Multi-regional and Multilingual)

### Multilingual vs Multi-regional

- **Multilingual:** The site offers content in **multiple languages**.
- **Multi-regional:** The site targets users in **different countries/regions**.
- Some sites are **both** multilingual and multi-regional.
- Decide on a URL structure before building the site; changing it later is disruptive.

### URL Structure Options

| Structure | Example | Pros | Cons |
|-----------|---------|------|------|
| **ccTLD** | `example.de` | Clear geo-targeting; server independent; strong signal | Expensive; more infrastructure; limited availability |
| **Subdomain** | `de.example.com` | Easy setup; can use different servers | Unclear geo-targeting; harder to maintain |
| **Subdirectory** | `example.com/de/` | Easy setup; low maintenance; consolidates signals | Single server; harder to separate by region |
| **URL params** | `example.com?loc=de` | — | **NOT RECOMMENDED**; hard to segment; error-prone |

### hreflang Implementation

- Use **hreflang annotations** to help Google link users to the correct language/regional version of a page.
- Don't **auto-redirect** based on assumed language — this can trap users and break back-button navigation.
- Add **visible hyperlinks** to other language versions so users can switch manually.
- Google ignores the `geo.position` and `distribution` meta tags — do not rely on them.
- Use **UTF-8 encoding** for localized URLs (e.g., accented characters).
- The hreflang value format is `language-Region` (e.g., `es-ES` for Spanish in Spain, `es-MX` for Spanish in Mexico).
- Always include an `x-default` hreflang entry for users whose language you don't explicitly target.
- Each page must reference **all** language versions, including itself (bidirectional links).

### Geotargeting Signals

In rough order of importance:

1. **ccTLD** (strongest signal) — e.g., `.fr` clearly targets France.
2. **hreflang statements** — explicit language/region annotations.
3. **Server location** (via IP) — less reliable with CDNs, which can mask the real server location.
4. **Other signals:**
   - Local business addresses and phone numbers.
   - Local language and currency.
   - Local backlinks from the target region.
   - Google Business Profile (for local businesses).
   - Localized content that genuinely serves the target audience.

### International SEO Best Practices Summary

- Plan the URL structure before launch — switching structures later causes indexing disruption.
- Use hreflang bidirectionally: each page must reference all localized versions including itself.
- Always include an `x-default` hreflang value for unmatched languages.
- Never rely on the `geo.position` or `distribution` meta tags — Google ignores them.
- Let users self-select their preferred language/region; avoid forced redirects based on IP or browser language.
- Keep localized content genuinely localized — direct translation is often insufficient; adapt for cultural and regional context.
- Submit separate sitemaps per language/region where practical, and use Search Console to monitor international coverage.

---

## What NOT to Focus On

Many commonly-repeated SEO "best practices" are either irrelevant or misleading. Google has explicitly clarified the following:

- **Meta keywords:** Google does **NOT** use the keywords meta tag. Do not waste time on it.
- **Keyword stuffing:** Violates spam policies and harms readability.
- **Keywords in domain/URL paths:** Almost no impact beyond appearing as breadcrumbs in search results.
- **Content length limits:** There is **no ideal word count target**. Write as much as needed to cover the topic helpfully.
- **Subdomains vs subdirectories:** This is a **business/infrastructure decision**, not a ranking decision — Google treats them similarly.
- **PageRank:** Just one of many ranking factors; obsessing over PageRank is unproductive.
- **Duplicate content "penalty":** There is **no manual action** for content accessible via multiple URLs. Google simply consolidates signals to a canonical URL.
- **Heading count and order:** There is **no ideal number** of headings. Semantic heading order helps screen readers but is not critical for Google ranking. Use headings for structure and readability.
- **E-E-A-T as a ranking factor:** E-E-A-T is **NOT** a direct, automated ranking factor. It is a conceptual framework; the signals it represents (trust, expertise, etc.) are what ranking systems use.
- **XML sitemaps priority/changefreq values:** Google largely ignores the `priority` and `changefreq` attributes in sitemaps; focus on submitting accurate, clean sitemaps with valid `<lastmod>` dates.
- **DA/PA and other third-party metrics:** Domain Authority, Page Authority, and similar proprietary metrics are not used by Google and have no direct bearing on rankings.
- **"Keyword density" targets:** There is no optimal keyword density percentage; write naturally for users.

---

## SEO Starter Guide Summary Checklist

- [ ] Check if Google has found your content (`site:` search).
- [ ] Use descriptive URLs with relevant words (hyphens, not underscores).
- [ ] Group similar pages in logically-named directories.
- [ ] Reduce duplicate content with canonical tags and 301 redirects.
- [ ] Create original, comprehensive, well-written, people-first content.
- [ ] Anticipate the search terms users might use to find your content.
- [ ] Avoid distracting ads that push main content down or make it hard to find.
- [ ] Link to relevant internal and external resources with good anchor text.
- [ ] Write unique, descriptive, page-specific `<title>` tags.
- [ ] Write page-specific meta descriptions summarizing the page.
- [ ] Add high-quality images with descriptive alt text.
- [ ] Optimize videos with descriptive titles and descriptions; use video sitemaps.
- [ ] Set up Google Search Console and verify your site.
- [ ] Add structured data (JSON-LD) for rich results where applicable.
- [ ] Ensure good Core Web Vitals (LCP < 2.5s, INP < 200ms, CLS < 0.1).
- [ ] Use HTTPS for all pages.
- [ ] Ensure mobile-friendliness (responsive design).
- [ ] Avoid intrusive interstitials, especially on mobile.
- [ ] Implement hreflang correctly for multilingual/multi-regional sites.
- [ ] Follow Google's spam policies strictly — avoid all listed violations.
- [ ] Submit an XML sitemap via Search Console.
- [ ] Monitor coverage, performance, and manual actions in Search Console.
- [ ] Build content that demonstrates genuine Experience, Expertise, Authoritativeness, and Trustworthiness (E-E-A-T).
- [ ] For YMYL topics, hold content to the highest E-E-A-T standards.
- [ ] Disclose AI/automation use where readers would reasonably expect it.
- [ ] Provide visible author bylines with expertise/background information.

---

## Sources

All content sourced from official **Google Search Central** documentation:

- SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Creating helpful, reliable, people-first content: https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- Introduction to structured data: https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data
- Core Web Vitals: https://developers.google.com/search/docs/appearance/core-web-vitals
- Page experience: https://developers.google.com/search/docs/appearance/page-experience
- Help Google understand your ecommerce site structure: https://developers.google.com/search/docs/specialty/ecommerce/help-google-understand-your-ecommerce-site-structure
- Write high quality reviews: https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews
- Spam policies: https://developers.google.com/search/docs/essentials/spam-policies
- Managing multi-regional sites: https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites

---

*This reference is intended for use within the WordPress Auto Site Builder skill. Always consult the live Google Search Central documentation for the most current guidance, as Google updates its documentation and algorithms periodically.*
