# Large CSV Media Import

Use this reference when a WooCommerce product CSV is too large for the agent/tool channel, when the agent cannot attach the file directly, or when a processed CSV must be imported through a WordPress-accessible URL.

## Hard Rule: No Encoded Chat Transfer

Do not send large product CSV content through chat, base64, screenshots, pasted text, clipboard payloads, or chunked prompt messages.

Reasons:

- CSV quoting can break when HTML descriptions contain commas, quotes, line breaks, or inline images.
- Encoding can shift between UTF-8, UTF-8 BOM, GBK, Windows-1252, or Excel variants.
- Chat/tool channels may truncate silently.
- Base64 adds size, hides parser drift, and encourages agents to decode without verifying row/column integrity.
- A broken CSV can overwrite product IDs, variation parents, images, prices, or Rank Math metadata.

If the agent cannot use a binary-safe file path, browser upload, REST media upload, or verified URL, stop and ask the user to manually upload the processed CSV and provide the media/file URL.

## Safe Transport Options

Use the first available safe option:

1. Local filesystem access: read and write the CSV directly from the user's machine.
2. Browser or agent-browser upload: log into WordPress, open Media Library, upload the processed CSV as a file, then copy its attachment URL.
3. WordPress REST media upload: upload the CSV with `/wp-json/wp/v2/media` using an application password or authenticated browser session.
4. User manual fallback: ask the user to upload the processed CSV to WordPress Media Library or a private file location and provide the URL.

Never bypass upload restrictions by renaming unsafe files or disabling security plugins unless the user explicitly approves and the change is recorded and reverted.

## Before Upload

Before uploading a processed CSV:

- Save the original CSV unchanged.
- Save the processed CSV as UTF-8 without unintended re-encoding unless WooCommerce/import testing requires UTF-8 BOM for Excel compatibility.
- Run CSV inspection with RFC/Excel parsing and `doublequote=True`.
- Record file size, SHA-256 hash, encoding, delimiter, row count, column count, product type counts, and expected image/gallery counts.
- Verify headers and row field counts match.
- Verify identity fields, variation parent links, image URLs, Rank Math fields, and price conversion rules.
- Verify brand replacement did not modify `Images` values, inline `<img src>` URLs, attachment IDs, CDN URLs, or other media/download URLs.

If any check fails, do not upload/import. Fix the CSV first.

## Upload To Media Library

When using browser automation:

1. Open WordPress admin.
2. Go to Media Library > Add New.
3. Upload the processed CSV file.
4. Open the uploaded attachment details.
5. Copy the File URL and attachment ID when visible.
6. Record uploader account, timestamp, filename, file size, URL, and attachment ID.

If WordPress blocks CSV upload for security reasons, do not blindly install random file-upload plugins. Prefer REST upload if allowed, ask the user to upload through hosting file manager/private location, or ask for explicit approval before changing allowed MIME types.

## Import From Media URL With Code Snippets

Use a controlled Code Snippets `one_time_writer` only when WooCommerce import through the UI is not practical and the site owner authorized automated import.

Importer requirements:

- Run only in wp-admin.
- Require `manage_woocommerce` or administrator capability.
- Require an explicit action parameter, nonce, and expected SHA-256 hash.
- Download the CSV URL to a temporary file with `download_url()` or WordPress HTTP API.
- Reject non-CSV MIME types unless deliberately allowed and recorded.
- Reject unexpected file size, failed hash, row count mismatch, missing headers, or parser drift.
- Support `dry_run=1` first: inspect and report counts without writing products.
- On real import, update existing products only when IDs/SKUs/Parent behavior was intentionally selected.
- Record imported, updated, skipped, failed rows, warnings, and sample product IDs/URLs.
- Do not keep the importer active after use.

Do not place the CSV contents inside the snippet. The snippet should reference a URL or temporary file path plus expected hash and counts.

## Preferred Workflow

1. Process CSV locally.
2. Inspect and create product knowledge/import ledger.
3. Upload the processed CSV as a real file.
4. Copy media URL and attachment ID.
5. Run read-only/dry-run importer or WooCommerce UI mapping preview.
6. Confirm row count, headers, product types, parent links, image columns, and price fields.
7. Run the actual import.
8. Verify sample simple products, variable products, product galleries, inline body images, prices, stock, categories, add-to-cart, cart quantity, and Rank Math metadata.
9. Localize/sideload remote product/gallery/body images into the WordPress Media Library using a suitable image import/optimization plugin or controlled media workflow, then convert or serve the localized images as WebP.
10. Verify no finished product/gallery/body image depends on unapproved hotlinked remote URLs, and verify WebP output for sampled featured, gallery, inline/body, category, article, hero, logo, and OpenGraph images.
11. Delete/disable the one-time importer snippet.
12. Delete the uploaded CSV from Media Library or restrict access after verification.
13. Record final import ledger and cleanup evidence.

## Manual Fallback Message

When the agent cannot safely operate file upload or import, say:

```text
这个 CSV 文件不能通过聊天/base64/截图/粘贴方式传输，否则可能损坏产品数据。请你把我处理好的 CSV 文件手动上传到 WordPress 媒体库或一个私密文件位置，然后把文件 URL 发给我。我会用这个 URL 做校验、dry-run 和导入，不会乱猜编码或拆分粘贴。
```

## Cleanup And Privacy

CSV imports often contain product strategy, pricing, image URLs, metadata, and private operational details.

- Do not leave public CSV files indexed or linked after import.
- Remove temporary media attachments, temp files, and one-time snippets after verification.
- Do not add CSV URLs to public pages, menus, posts, sitemap, robots, or GitHub.
- Do not log credentials, application passwords, customer data, or private file URLs in public reports.
- If a temporary file must remain for rollback, restrict it outside public uploads when possible and record when it should be deleted.
