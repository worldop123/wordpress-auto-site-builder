# Deliverables

Keep chat concise. Put long code and generated content in files.

## File naming

Use lowercase site slug and purpose:

- `<site>-site-config.json`
- `<site>-homepage-style-preview-v1.html`
- `<site>-homepage-style-preview-notes.md`
- `<site>-product-csv-originality-preview.csv`
- `<site>-product-csv-rewritten-import.csv`
- `<site>-product-csv-change-report.md`
- `<site>-rankmath-product-seo-map.csv`
- `<site>-home-html-v1.md`
- `<site>-blog-html-v1.md`
- `<site>-policy-pages-html-v1.md`
- `<site>-global-shell-snippet-v1.md`
- `<site>-product-page-ux-snippet-v1.md`
- `<site>-checkout-rules-snippet-v1.md`
- `<site>-rankmath-meta-writer-v1.md`
- `<site>-media-alt-writer-v1.md`
- `<site>-seo-qa-scanner-v1.md`
- `<site>-blog-articles-batch-01.md`
- `<site>-indexing-submit-pack-v1.md`
- `<site>-launch-report.md`

## Code file format

For each snippet markdown file:

```text
Snippet Name:
Lifecycle:
Keep Enabled:
Purpose:
Dependencies:
Rollback:

<complete code only below this line>
```

If the user explicitly wants code-only files, omit explanation and keep metadata in the filename or a separate manifest.

## Final response

Summarize:

- Whether the homepage style preview was approved or explicitly waived.
- Product CSV files generated/imported, including whether identity fields were preserved and Rank Math SEO fields were included.
- Generated files or live changes.
- Verification performed.
- Items the user must still configure, such as payment, SMTP, shipping rates, DNS, or Search Console ownership.

Do not paste long generated PHP/HTML/CSS/JS in chat unless the user explicitly asks.
