# Interruption Resume Protocol

AI coding agents can stop unexpectedly because of server errors, model context limits, browser crashes, REST timeouts, network failures, or user pauses. This project must be safe to resume.

## Core Rule

Resume from the last verified checkpoint, not from the last attempted action.

Never repeat destructive work unless a read-only recovery check proves it is necessary.

## Required Resume Ledger

Each agent run should keep or reconstruct a ledger with:

- Website task status and skill task status.
- Current phase and last verified phase gate.
- Created/updated WordPress IDs: pages, posts, products, media, menus, snippets, templates.
- Active snippets, snippet lifecycle, rollback notes, and related pages.
- WooCommerce page bindings and core settings.
- Product CSV source row count, import/update count, failed rows, gallery/body image verification.
- Article IDs, statuses, schedule dates, focus keywords, featured images, and internal links.
- QA checks passed and pending.
- Temporary credentials or sessions created and whether they were revoked.
- Next safe action.

## Resume Steps

1. Read the latest ledger and final/progress notes.
2. Run a read-only live-state check before any write:
   - pages
   - WooCommerce bindings
   - snippets
   - product/media counts
   - article statuses
   - menus
   - Rank Math sitemap
   - cart/product/checkout availability
3. Compare live state to the ledger.
4. Revoke or rotate temporary credentials created before the interruption.
5. Continue from the smallest safe unfinished step.
6. Update the ledger before the next risky operation.

## Do Not Repeat Automatically

- Old-site cleanup
- Product deletion
- Product CSV import
- Media import
- Article publishing or scheduling
- Page deletion
- Snippet replacement
- Launch/indexing submission

## If the Ledger Is Missing

Create a minimal recovery report from live read-only inspection. Continue in repair/recovery mode only after identifying protected data and launch blockers.
