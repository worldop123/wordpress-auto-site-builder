# Product CSV Originality and Rank Math SEO

Use this when the user provides an official WordPress/WooCommerce product export CSV and wants product titles, short descriptions, product body/long descriptions, and product SEO data rewritten before re-import.

## Goal

Produce a re-import-ready CSV that keeps WooCommerce product identity and commerce data intact while making customer-facing product copy original, useful, compliant, and aligned with Rank Math product SEO.

## First inspect the CSV

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
- Preserve factual specs, sizes, flavors, colors, compatibility, package contents, materials, shipping notes, and usage limits.
- Vary title patterns across products; do not make every title the same formula.
- Keep titles natural and searchable, not stuffed.
- Keep short descriptions concise and purchase-oriented.
- Use long descriptions for structured SEO depth: intro, key specs, use cases, what's included, shipping/returns note, FAQ if appropriate.
- For regulated products, avoid health, safety, cessation, medical, guaranteed result, or illegal-use claims.
- Do not invent specs, certifications, stock status, shipping times, reviews, awards, or guarantees.

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
6. Produce the full rewritten CSV after style confirmation or when the user requested direct processing.
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
- After import, verify product title, short description, long description, inline/body images, Rank Math meta, product URL, featured image, image gallery, variation form, price, stock, category, add-to-cart, cart quantity, and sitemap inclusion.

## Import ledger

Every CSV import deliverable must include:

- Source file name, encoding, delimiter, original row count, output row count.
- Source currency, target currency, exchange rate, rate source/timestamp, rounding rule, converted price columns, and original-price backup columns when conversion was used.
- Product/variation counts by type.
- Preserved identity fields and rewritten fields.
- Expected featured/gallery/body image counts and actual sampled results.
- Import warnings, failed rows, failed image URLs, and remediation steps.
- Sample verification URLs for product, category/archive, cart, and sitemap.

## Deliverables

- Rewritten CSV ready for WooCommerce import.
- Optional sample preview CSV for first 3-5 products.
- SEO mapping CSV if Rank Math fields cannot safely be imported directly.
- Change report documenting preserved fields and modified fields.
