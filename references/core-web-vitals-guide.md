# Core Web Vitals Optimization Guide

## What Are Core Web Vitals

Core Web Vitals are a set of metrics that measure real-world user experience for loading performance, interactivity, and visual stability. Google's core ranking systems reward pages that provide good page experience, and Core Web Vitals are a key component.

Read this reference before performance optimization work and before final QA. Also read `google-seo-guidelines.md` for the broader page experience context.

## The Three Core Web Vitals

### LCP (Largest Contentful Paint)
- **Measures**: Loading performance
- **Good**: Under 2.5 seconds
- **Needs improvement**: 2.5 - 4.0 seconds
- **Poor**: Over 4.0 seconds
- **What triggers LCP**: The largest image, video, or text block visible in the viewport

### INP (Interaction to Next Paint)
- **Measures**: Responsiveness to user input
- **Good**: Under 200 milliseconds
- **Needs improvement**: 200 - 500 milliseconds
- **Poor**: Over 500 milliseconds
- **Replaced**: FID (First Input Delay) in March 2024
- **What it captures**: All interactions during page lifecycle, not just the first

### CLS (Cumulative Layout Shift)
- **Measures**: Visual stability
- **Good**: Under 0.1
- **Needs improvement**: 0.1 - 0.25
- **Poor**: Over 0.25
- **What causes shifts**: Images without dimensions, ads/embeds without reserved space, dynamically injected content, web fonts causing FOIT/FOUT

## LCP Optimization Strategies

### Image Optimization
- Use modern formats: WebP, AVIF (50-70% smaller than JPEG/PNG)
- Serve responsive images with `srcset` and `sizes` attributes
- Preload the LCP image: `<link rel="preload" as="image" href="hero.webp">`
- Set `fetchpriority="high"` on the LCP image
- Use `loading="eager"` for above-the-fold images (NOT lazy loading)
- Use `loading="lazy"` for below-the-fold images only

### Server Response Time (TTFB)
- Target: under 800ms
- Use PHP opcache and object cache (Redis/Memcached)
- Use a CDN with edge caching
- Optimize database queries
- Use page caching (WP Rocket, LiteSpeed Cache, W3 Total Cache)

### Render-Blocking Resources
- Minimize CSS: inline critical CSS, defer non-critical CSS
- Defer JavaScript: use `defer` for non-critical scripts
- Remove unused CSS and JavaScript
- Minify HTML, CSS, and JavaScript

### WordPress-Specific LCP Optimization
- Optimize the Hero section: use a single optimized WebP image
- Avoid large sliders/carousels as the first visible element
- Use Hello Elementor theme (lightweight, minimal overhead)
- Disable unnecessary Elementor widgets and features
- Use Elementor's performance settings: flexbox containers, optimized DOM, optimized CSS loading
- Limit the number of fonts loaded (1-2 font families max)

## INP Optimization Strategies

### JavaScript Execution
- Minimize main thread blocking
- Break long tasks into smaller chunks
- Use `requestIdleCallback()` for non-critical work
- Use `requestAnimationFrame()` for visual updates
- Defer or async non-critical JavaScript

### Third-Party Scripts
- Audit and remove unnecessary third-party scripts
- Delay third-party scripts (analytics, chat widgets, tracking pixels)
- Use `defer` or `async` for third-party scripts
- Consider server-side analytics as alternative

### WordPress-Specific INP Optimization
- Minimize plugin count (each plugin adds JS/CSS)
- Disable WooCommerce cart fragments AJAX on non-shop pages (common INP killer)
- Defer WooCommerce JavaScript on non-commerce pages
- Use Code Snippets to selectively load scripts only where needed
- Remove emoji scripts and embed scripts if not needed:
  ```php
  remove_action('wp_head', 'wp_emoji');
  remove_action('wp_head', 'wp_emoji');
  ```
- Limit Elementor animations and effects

### WooCommerce INP Fixes
- Disable cart fragments on non-WooCommerce pages:
  ```php
  add_action('wp_enqueue_scripts', function() {
      if (!is_woocommerce() && !is_cart() && !is_checkout()) {
          wp_dequeue_script('wc-cart-fragments');
      }
  }, 11);
  ```
- Optimize product gallery: reduce number of zoom images
- Disable AJAX cart on product pages if not needed

## CLS Optimization Strategies

### Images and Videos
- Always specify `width` and `height` attributes on images and videos
- Use CSS `aspect-ratio` for responsive media containers
- Reserve space for responsive images:
  ```css
  .product-image {
    aspect-ratio: 4 / 3;
    width: 100%;
  }
  ```

### Ads and Embeds
- Reserve space for ad slots with min-height
- Reserve space for embeds (YouTube, social) before they load
- Use `loading="lazy"` for below-the-fold embeds

### Web Fonts
- Use `font-display: swap` or `font-display: optional` in @font-face
- Preload critical fonts: `<link rel="preload" as="font" crossorigin>`
- Use system fonts as fallback to minimize shift
- Avoid FOUT (Flash of Unstyled Text) by using font-display strategies

### Dynamically Injected Content
- Reserve space for dynamically loaded content
- Avoid injecting banners/notifications above existing content
- Use CSS transforms for animations instead of changing layout properties

### WordPress-Specific CLS Fixes
- Always set image dimensions in Media Library
- Configure Elementor to set image dimensions
- Use CSS aspect-ratio for Elementor image widgets
- Reserve space for WordPress embeds
- Set explicit dimensions on WooCommerce product gallery images

## Measurement Tools

### Google Tools
- **PageSpeed Insights**: https://pagespeed.web.dev/ — tests both Lab and Field data
- **Search Console Core Web Vitals Report**: shows field data for your site
- **Chrome DevTools Performance tab**: detailed performance profiling
- **Lighthouse**: built into Chrome DevTools, audits performance
- **Web Vitals Chrome Extension**: real-time Core Web Vitals measurement

### Field Data vs Lab Data
- **Field Data**: Real user data from Chrome UX Report (CrUX) — what actual users experience
- **Lab Data**: Simulated data from Lighthouse — controlled environment testing
- Google uses Field Data for ranking signals
- Use Lab Data for debugging and optimization
- A page can have good Lab data but poor Field data (or vice versa)

### Key Metrics to Track
- LCP (Largest Contentful Paint)
- INP (Interaction to Next Paint)
- CLS (Cumulative Layout Shift)
- FCP (First Contentful Paint) — supplementary
- TTFB (Time to First Byte) — supplementary
- TBT (Total Blocking Time) — Lab only, correlates with INP

## WordPress Performance Stack

### Hosting Layer
- Use PHP 8.1+ (significant performance improvement over 7.x)
- Use HTTP/2 or HTTP/3
- Enable Gzip or Brotli compression
- Enable OPcache
- Use Redis or Memcached for object caching

### Caching Plugin Configuration
Recommended settings for ecommerce:
- Page caching: enabled (exclude cart, checkout, my-account pages)
- Object caching: enabled (Redis/Memcached)
- Browser caching: enabled (static assets with long expiry)
- Gzip compression: enabled
- Minify HTML/CSS/JS: enabled (test thoroughly)
- Lazy load images: enabled
- Lazy load iframes: enabled
- Database optimization: periodic

### CDN Configuration
- Serve all static assets via CDN
- Configure proper cache headers
- Enable image optimization/resize at CDN edge
- Consider Cloudflare (free tier sufficient for many sites)

### Image Optimization Pipeline
1. Upload optimized source images (WebP preferred)
2. Use Smush, ShortPixel, or Imagify for automatic optimization
3. Enable WebP conversion
4. Configure responsive image sizes
5. Set up lazy loading for below-the-fold images
6. Preload LCP image

## Elementor Performance Optimization

### Elementor Settings
- Enable Flexbox Containers (reduces DOM nesting)
- Enable Optimized DOM Output
- Enable Optimized CSS Loading
- Enable Optimized Google Fonts Loading
- Enable Lazy Load background images
- Disable unused widgets in Elementor Settings

### Elementor Best Practices
- Use Containers instead of old Sections/Columns
- Minimize nested containers (max 3 levels deep)
- Use custom CSS sparingly (prefer Elementor built-in controls)
- Avoid excessive animations and motion effects
- Limit the number of widgets per page
- Use template parts for repeated sections (header, footer)

## Hello Elementor Theme Performance

### Why Hello Elementor is Recommended
- Extremely lightweight (< 20KB CSS, minimal JS)
- No jQuery dependency
- Minimal default styling (Elementor controls the design)
- Fast initial page load
- Compatible with all major caching and optimization plugins

### Hello Elementor Optimization
- Disable emoji scripts
- Disable WordPress embed scripts if not needed
- Remove unnecessary meta tags
- Use child theme for custom functions (not parent theme edits)

## Core Web Vitals QA Checklist

Before claiming the build is complete, verify:

### LCP
- [ ] LCP element identified (usually hero image or largest text)
- [ ] LCP image is preloaded with `fetchpriority="high"`
- [ ] LCP image is in WebP format
- [ ] LCP image is properly sized (not oversized)
- [ ] Server response time (TTFB) under 800ms
- [ ] No render-blocking CSS/JS above the fold
- [ ] Page caching enabled
- [ ] CDN configured for static assets

### INP
- [ ] WooCommerce cart fragments disabled on non-shop pages
- [ ] Third-party scripts deferred or delayed
- [ ] Unnecessary plugins removed
- [ ] JavaScript minified and deferred
- [ ] No long-running JavaScript on page load
- [ ] Elementor animations minimized

### CLS
- [ ] All images have `width` and `height` attributes
- [ ] All images use `aspect-ratio` in CSS for responsive layouts
- [ ] Web fonts use `font-display: swap` or `optional`
- [ ] Ad slots have reserved space (min-height)
- [ ] No dynamically injected content above the fold
- [ ] Embeds have reserved space

### General Performance
- [ ] PageSpeed Insights score: 90+ on mobile
- [ ] PageSpeed Insights score: 95+ on desktop
- [ ] Search Console Core Web Vitals report: no poor URLs
- [ ] PHP version 8.1+
- [ ] OPcache enabled
- [ ] Object cache (Redis/Memcached) enabled
- [ ] Gzip/Brotli compression enabled
- [ ] Images optimized (WebP format)
- [ ] CSS/JS minified
- [ ] CDN active

## Common WordPress Performance Issues

### WooCommerce Cart Fragments
- **Problem**: `wc-cart-fragments.js` loads on every page, causes high INP
- **Solution**: Disable on non-woocommerce pages using Code Snippet
- **Verification**: Check PageSpeed Insights INP score improvement

### Excessive Plugin JavaScript
- **Problem**: Each plugin adds its own JS/CSS, bloating page weight
- **Solution**: Audit plugins, remove unnecessary ones, use Code Snippets for selective loading
- **Verification**: Compare before/after PageSpeed scores

### Unoptimized Images
- **Problem**: Large JPEG/PNG images slow LCP and increase page weight
- **Solution**: Convert to WebP, use responsive srcset, enable lazy loading
- **Verification**: Check image sizes in Network tab, verify WebP serving

### Render-Blocking Resources
- **Problem**: CSS/JS in `<head>` blocks rendering
- **Solution**: Inline critical CSS, defer non-critical JS, use async/defer attributes
- **Verification**: Check PageSpeed Insights "Eliminate render-blocking resources"

### Database Bloat
- **Problem**: Post revisions, transients, and plugin data bloat the database
- **Solution**: Use WP-Optimize or similar, limit post revisions, clean transients
- **Verification**: Check database size before/after optimization
