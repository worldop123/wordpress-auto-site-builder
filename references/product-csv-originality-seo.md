# Product CSV Originality and Rank Math SEO

Use this when the user provides an official WordPress/WooCommerce product export CSV and wants product names/titles, short descriptions, product body/long descriptions, editable image text, and product SEO data rewritten before re-import.

## Goal

Produce a re-import-ready CSV that keeps WooCommerce product identity and commerce data intact while making customer-facing product copy original, useful, compliant, and aligned with Rank Math product SEO.

The rewrite must be intelligent content transformation, not simple translation, synonym swapping, or preserving the source CSV title/description/body pattern. Treat the source CSV as raw product facts and evidence, then create differentiated product names, short descriptions, long descriptions, SEO fields, and image text for the target market.

## First inspect the CSV

If the CSV is too large for the current agent/tool channel, do not move it through chat, base64, screenshots, pasted text, or chunked prompt messages. Use `large-csv-media-import.md`: process the file through local filesystem access, browser/agent-browser media upload, REST media upload, or ask the user to manually upload the processed CSV and provide a file URL. Never guess encoding or reconstruct CSV content from partial text.

Before editing, identify:

- Encoding and delimiter.
- Parser quality. WooCommerce official exports often contain HTML fields with doubled quotes (`""`). Prefer Python `csv.excel`/RFC-style parsing with `doublequote=True` before trusting `csv.Sniffer`; Sniffer can mis-detect `doublequote=False` and silently shift `Images`, `Position`, `Parent`, or `Meta:` columns.
- Header names exactly as exported.
- Product row types: simple, variable, variation, grouped, external.
- Identity fields: `ID`, `Type`, `SKU`, `Name`, `Published`, `Is featured?`, `Visibility in catalog`, `Short description`, `Description`, `Categories`, `Tags`, `Images`, `Parent`, attributes, prices, stock, shipping, tax.
- Price currency context: source currency of `Regular price` and `Sale price`, target WooCommerce currency, exchange-rate source, timestamp, rounding rule, and whether original prices need backup columns.
- Media fields: featured image URL/ID, gallery image list, inline/body images inside `Description`, image ALT/title/caption columns, remote image URLs, attachment IDs, and any CDN/proxy URLs.
- Rank Math fields, often exported as `Meta:` columns or plugin-specific columns. Detect columns containing `rank_math`, `seo`, `focus`, `robots`, `title`, or `description`.
- Custom metadata columns. Every `Meta: ...` column must be classified by exact meta key before editing.

If unsure about field meaning, preserve it unchanged and report it.

## Product knowledge before page and SEO generation

The CSV inspection must happen before creating homepage HTML, custom page HTML, category copy, product page enhancement copy, blog/article plans, image ALT text, or Rank Math metadata. Product data is the source material for the site's content strategy.

Create a product knowledge ledger with:

- Product counts by type: simple, variable, variation, grouped, external.
- Category, tag, attribute, flavor/color/size/spec, and parent/variation structure.
- Representative product names, SKUs, slugs, price range, sale-price patterns, stock/catalog visibility, shipping/compliance notes, and targetable differentiators.
- Description quality: missing short descriptions, thin long descriptions, duplicate wording, body/detail image usage, FAQ/spec opportunities, and prohibited claims.
- Media coverage: featured image availability, gallery counts, inline body images, image ALT/title/caption fields, remote URLs, and WebP/conversion needs.
- SEO state: existing Rank Math title, description, focus keyword, robots/canonical fields, duplicate/missing values, and keyword cannibalization risks.
- Content outputs unlocked by this knowledge: homepage product/category sections, shop/category introductions, product-page trust/FAQ blocks, policy wording, article topics, internal-link plan, schema evidence, and image ALT themes.

Do not generate generic page sections such as "featured products", "premium quality", or "best sellers" without mapping them to real products/categories or dynamic WooCommerce queries. If product facts are missing or the CSV parser report shows blockers, fix inspection first.

### WooCommerce official CSV sanity checks

For official WooCommerce exports, run these checks before any rewrite/import:

- Header count equals row field count for every row.
- `Images` values are real image URLs or attachment references, not `0`, blank because of parser drift, or HTML from another column.
- Gallery counts are extracted from comma-separated `Images` URLs; the first URL is the featured image and following URLs are gallery images.
- `Position` is numeric for normal exports.
- Parent products have empty `Parent`; variation rows have `Parent` pointing to an existing parent SKU/slug/ID.
- `Parent` must never contain HTML, long description text, image URLs, or a value longer than a normal slug/SKU. Treat that as a blocker.
- `Description` and `Short description` preserve valid HTML quoting.
- No row has extra unnamed fields from broken quoting.
- Parser report records row count, column count, product type counts, image refs, max gallery count, duplicate SKUs, unresolved parents, and meta-column policies.

### Custom metadata policy

Classify exported `Meta:` columns by exact key:

- Editable Rank Math SEO fields: `Meta: rank_math_title`, `Meta: rank_math_description`, `Meta: rank_math_focus_keyword`.
- Protected Rank Math runtime fields: `Meta: rank_math_internal_links_processed`, `Meta: rank_math_analytic_object_id`.
- Editable only for migration/cleanup: `Meta: _yoast_wpseo_title`, `Meta: _yoast_wpseo_metadesc`, `Meta: _yoast_wpseo_focuskw`.
- Review manually: unknown `Meta:` keys, plugin runtime IDs, serialized data, analytics object IDs, counters, cache flags, and private integration fields.

Never bulk-edit unknown custom metadata just because it contains the words `title`, `description`, or `keyword`. Use the exact meta key and plugin context.

## Fields usually safe to rewrite

Rewrite only when present and relevant:

- Product title/name.
- Short description.
- Long description/body/content.
- Tags when the user wants SEO cleanup.
- SEO title.
- SEO description.
- Focus keyword.
- Product image ALT/title/caption columns if present and clearly mapped.

## Fields to preserve unless explicitly instructed

Do not change these casually:

- `ID`
- `Type`
- `SKU`
- `Slug`
- `Parent`
- variation attributes and attribute values
- prices
- stock
- weight/dimensions
- categories
- image URLs
- download URLs
- tax/shipping class
- published status
- catalog visibility
- menu order

Changing these can break imports, variations, existing URLs, inventory, or internal links.

## Currency conversion for imported prices

When the product source data uses a different currency than the target small-language/localized site, convert product prices before import.

Rules:

- Detect source currency and target WooCommerce currency before touching price columns.
- Use ISO 4217 codes such as `USD`, `EUR`, `CZK`, `PLN`, `HUF`, `RON`, `BGN`, `SEK`, `DKK`, `NOK`, `CHF`, `GBP`.
- Do not hardcode exchange rates in this skill. Use a user-provided rate or a live rate checked at build time from a documented source.
- Record exchange-rate source, retrieval timestamp, source currency, target currency, rate, decimal precision, and rounding strategy in the import ledger.
- Convert `Regular price` and `Sale price`; preserve sale/regular relationships and never make sale price greater than regular price.
- Preserve original source prices in backup meta columns or a separate report, for example `Meta: _source_regular_price`, `Meta: _source_regular_price_currency`, and `Meta: _source_regular_price_fx_rate`.
- Do not convert non-price numbers such as stock, dimensions, puff counts, nicotine strength, SKU, GTIN, or attributes.
- After import, verify WooCommerce currency setting, product price display, cart totals, checkout totals, Product schema `priceCurrency`, and sample variable products.

Suggested helper:

```bash
python scripts/convert_product_prices.py products.csv --output products-converted.csv --source-currency USD --target-currency CZK --rate 22.50 --rate-source "ECB/manual check" --rate-timestamp "2026-07-09T12:00:00Z"
```

Use `--charm-ending 0.99` only when the target market uses psychological pricing and the user/market strategy allows it.

## Originality rewrite rules

- Rewrite product copy from the product's actual facts, not generic adjectives.
- Do not only translate the original product name, short description, or long description. Translation can be a starting point only; the final copy must be newly planned for the target market, buyer intent, SEO opportunity, and category context.
- Do not preserve the same source CSV content with minor synonym changes. If the source has repetitive manufacturer text, thin descriptions, duplicated bodies, or formulaic names, rebuild the copy architecture.
- Preserve factual specs, sizes, flavors, colors, compatibility, package contents, materials, shipping notes, and usage limits.
- Vary title patterns across products; do not make every title the same formula.
- Rewrite product names/titles with useful differentiation: product type, key attribute, model/series, material/flavor/color/size, compatibility, pack count, or primary use case when those facts are available.
- Keep titles natural and searchable, not stuffed.
- Avoid adding unsupported superlatives such as "best", "premium", "official", "certified", or "guaranteed" unless the source proves them.
- Keep short descriptions concise and purchase-oriented. Each short description should surface the most relevant differentiator, not repeat the title in sentence form.
- Rewrite long descriptions as structured buying content. Depending on available facts, use sections such as overview, key specs, buyer use cases, compatibility/fit, flavor/material notes, package contents, care/use instructions, shipping/returns note, compliance note, and FAQ.
- Preserve inline/body images, existing valid HTML, tables, lists, and media references unless they are broken or explicitly being replaced. Rewrite surrounding text without dropping product detail images.
- Vary body structure across categories where useful. A size/fit product, flavor product, accessory, replacement part, bundle, and regulated product should not all use the same section rhythm.
- Make product copy internally linkable: identify likely category anchors, comparison angles, FAQ topics, and article ideas in the change report when the CSV facts support them.
- Align SEO fields with the rewritten copy, not the old source title. SEO titles, meta descriptions, and focus keywords must reflect the new product name/category and a real differentiator.
- For regulated products, avoid health, safety, cessation, medical, guaranteed result, or illegal-use claims.
- Do not invent specs, certifications, stock status, shipping times, reviews, awards, guarantees, compatibility, material, country of origin, or performance claims.

### Product rewrite planning checklist

Before rewriting the full CSV, create a short rewrite plan:

- Naming strategy by category: which product facts belong in names, which facts belong in descriptions, and which words should be avoided.
- Description strategy by product group: expected short-description angle, long-description section pattern, FAQ/spec use, and compliance limits.
- SEO strategy: primary keyword pattern, category keyword boundaries, cannibalization risks, and Rank Math field format.
- Uniqueness strategy: how similar SKUs, variations, bundles, colors, flavors, or sizes will stay distinct without fabricated claims.
- Evidence limits: facts that are missing and therefore must not be invented.

For catalogs larger than a few products, rewrite and review a 3-5 product sample first unless the user explicitly authorized autonomous full processing. The sample should include different product types or categories where possible.

## Rank Math product SEO mapping

When columns exist, fill them with product-specific values:

- SEO title: include primary product keyword near the front, brand, and one concrete differentiator. Keep it readable.
- Meta description: one sentence or two short clauses with product type, key spec/category, buying/shipping detail, and brand. Avoid hype.
- Focus keyword: one main keyword, not a long comma list, unless the site convention explicitly supports multiple keywords.
- Robots: products should generally be index/follow unless hidden, draft, duplicate, out-of-scope, or intentionally noindex.

If Rank Math fields are not present in the CSV:

- Add a separate SEO mapping CSV or one-time writer plan instead of guessing import column names.
- Include product ID/SKU/slug as join keys.

## Import-safe workflow

1. Save the original CSV unchanged.
2. Create a working copy.
3. Inspect headers and row counts.
4. Identify safe editable columns.
5. Rewrite one sample product first if the catalog is large or the style is uncertain.
6. Produce the full rewritten CSV after style confirmation or when the user requested direct processing. Ensure the full pass rewrites product names/titles, short descriptions, long descriptions/body content, editable image text, and Rank Math fields where present; do not leave original source copy in customer-facing fields unless the field is already excellent and the change report explains why it was preserved.
7. Validate:
   - Same row count as source unless intentionally filtered.
   - Same identity fields.
   - Same SKU/Parent relationships.
   - Same featured image and gallery image references unless intentionally replaced.
   - Inline/body image URLs in long descriptions still exist and are importable.
   - No broken CSV quoting.
   - Required columns still present.
   - HTML in descriptions is valid enough for WordPress import.
   - Converted prices match the target currency and original prices are backed up when currency conversion was used.
8. Provide a change report with edited columns, preserved columns, SEO fields, media fields, and import notes.
9. For large CSV imports, upload the final CSV as a real file, record media URL/attachment ID/file size/SHA-256, run a dry-run or mapping preview, and delete or restrict the uploaded CSV after successful verification.

## Media and body-content integrity

Before importing:

- Count gallery images per product from the CSV `Images`/gallery column and record expected counts.
- Extract inline `<img>` URLs from product long descriptions and verify they are reachable or already in the media library.
- Preserve image order when it matters for product galleries.
- Do not remove body/detail images during originality rewriting.
- If remote image URLs are used, confirm WordPress can sideload them or pre-upload them and replace with media-library URLs.

After importing:

- Compare expected vs actual featured image and gallery count for sampled products.
- Open single product pages and verify main image, thumbnails, gallery switching, long description, body/detail images, and image ALT text.
- Check at least one simple product, one variable product, one product with multiple gallery images, and one product with inline body images.
- Record failed image URLs, missing attachment IDs, mismatched gallery counts, and products requiring re-import.

## Import and verification

If importing into WordPress:

- Prefer a small test import or staging site when possible.
- Use WooCommerce product importer mapping screen carefully.
- Confirm "update existing products" behavior if IDs/SKUs match existing products.
- For large CSV files, import from a verified media URL or temporary server file using the workflow in `large-csv-media-import.md`; do not paste CSV content into Code Snippets or admin text fields.
- After import, verify product title, short description, long description, inline/body images, Rank Math meta, product URL, featured image, image gallery, variation form, price, stock, category, add-to-cart, cart quantity, and sitemap inclusion.

## Import ledger

Every CSV import deliverable must include:

- Source file name, encoding, delimiter, original row count, output row count.
- Source currency, target currency, exchange rate, rate source/timestamp, rounding rule, converted price columns, and original-price backup columns when conversion was used.
- Product/variation counts by type.
- Preserved identity fields and rewritten fields.
- Rewrite strategy summary: naming patterns used, short-description angles, long-description structures, SEO keyword patterns, sample before/after notes, and any source copy intentionally preserved.
- Uniqueness checks: duplicate or near-duplicate titles, repeated short-description formulas, repeated meta descriptions, and products whose long descriptions still need manual product facts.
- Expected featured/gallery/body image counts and actual sampled results.
- Import warnings, failed rows, failed image URLs, and remediation steps.
- Large-file transport details when used: media attachment ID, CSV URL, file size, SHA-256 hash, dry-run result, importer snippet ID, cleanup status, and manual-upload fallback if automation was not safe.
- Sample verification URLs for product, category/archive, cart, and sitemap.

## Deliverables

- Rewritten CSV ready for WooCommerce import.
- Optional sample preview CSV for first 3-5 products.
- SEO mapping CSV if Rank Math fields cannot safely be imported directly.
- Change report documenting preserved fields and modified fields.
