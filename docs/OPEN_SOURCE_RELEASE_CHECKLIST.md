# Open Source Release Checklist

Use this before publishing the skill to GitHub.

## Repository Hygiene

- [ ] No WordPress passwords.
- [ ] No WordPress application passwords.
- [ ] No GitHub tokens.
- [ ] No API keys or payment secrets.
- [ ] No browser cookies, sessions, or storage-state files.
- [ ] No customer data, order exports, or private product supplier sheets.
- [ ] No client-specific claims that should not be public.
- [ ] `.uploads/`, exports, backups, and local screenshots are excluded.

## Documentation

- [ ] `README.md` explains purpose, stack, modes, and quick start.
- [ ] `INSTALL.md` explains installation for Codex and generic AI tools.
- [ ] `CONTRIBUTING.md` explains PR rules.
- [ ] `SECURITY.md` explains vulnerability and secret policy.
- [ ] `LICENSE` is present.
- [ ] `docs/AI_TOOL_COMPATIBILITY.md` explains multi-agent usage.
- [ ] `docs/RESUME_PROTOCOL.md` explains interruption recovery.
- [ ] `TRAE_CN_USAGE.md` is readable and generic.

## Skill Integrity

- [ ] `SKILL.md` frontmatter has valid `name` and `description`.
- [ ] The description mentions major triggers and supported workflow.
- [ ] References are linked from `SKILL.md`.
- [ ] No reference contradicts autonomous/ask-user mode.
- [ ] No reference contradicts the interruption resume protocol.
- [ ] No reference allows launch before articles, products, pages, SEO, and QA are complete.
- [ ] No snippet guide recommends unsafe global DOM loops or unverified auto-submit.
- [ ] Rank Math Free workflow uses content-aware audit plus Code Snippets one-time writer, not unavailable CSV SEO import.

## WordPress Build Rules

- [ ] Fixed stack is documented: Hello Elementor, Elementor, WooCommerce, Code Snippets, Rank Math.
- [ ] Full store surface is required: home, custom pages, products, product archives, blog archives, single posts, cart, checkout, account, policies.
- [ ] CSV import integrity covers featured images, galleries, body images, long descriptions, variations, attributes, and Rank Math fields.
- [ ] Official WooCommerce CSV parsing prefers double-quote-safe Excel/RFC parsing and validates `Images`, `Parent`, `Position`, and `Meta:` columns before rewriting.
- [ ] Custom metadata policy distinguishes editable Rank Math/Yoast SEO fields from protected runtime, analytics, serialized, or unknown meta fields.
- [ ] Logo generation also requires a separate verified site icon/favicon configured in WordPress Site Identity.
- [ ] Initial SEO article batch is required unless the user opts out.
- [ ] Buttons, links, forms, quantity controls, menus, filters, and checkout must be interaction-tested.
- [ ] Resume ledger requirements cover WordPress IDs, snippets, product imports, articles, QA checks, and temporary credentials.
- [ ] Rank Math generated writer PHP files are temporary artifacts and are not committed.

## Validation

- [ ] Run a secret scan.
- [ ] Run helper script smoke tests.
- [ ] Check Markdown links where practical.
- [ ] Review docs from the perspective of a new AI agent with no prior context.
