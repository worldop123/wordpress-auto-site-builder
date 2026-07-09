# Installation

## Codex

Copy the folder to:

```text
~/.codex/skills/wordpress-auto-site-builder
```

On Windows, this is usually:

```text
C:\Users\<you>\.codex\skills\wordpress-auto-site-builder
```

Restart Codex if the skill list does not refresh.

## Claude, Cursor, Trae, OpenHands, Aider, and Other Agents

Use this repository as a local reference folder. Instruct the agent to read:

```text
SKILL.md
references/intake-checklist.md
references/phase-playbook.md
references/qa-and-launch.md
```

Then ask it to load only task-relevant references.

## WordPress Requirements

- WordPress with HTTPS
- Hello Elementor theme
- Elementor plugin
- WooCommerce for ecommerce sites
- Code Snippets plugin
- Rank Math SEO plugin

Rank Math first-use reminder: ask the user to connect the relevant Rank Math account, then record whether it was connected, skipped by user choice, or blocked.

## Secret Handling

Never store WordPress passwords, application passwords, GitHub tokens, API keys, payment credentials, private cookies, or browser session data in this repository.

## Script Smoke Test

After installation, run:

```bash
python scripts/site_plan.py docs/SITE_CONFIG_EXAMPLE.json
python scripts/inspect_product_csv.py docs/SAMPLE_PRODUCT_IMPORT.csv
python scripts/rank_math_content_audit.py docs/SAMPLE_RANK_MATH_META_MAP.json
python scripts/rank_math_meta_writer.py docs/SAMPLE_RANK_MATH_META_MAP.json --output tmp-rank-math-writer.php
python scripts/resume_ledger.py init tmp-ledger.json --brand "Smoke Test" --domain example.com
python scripts/resume_ledger.py recovery tmp-ledger.json
python scripts/secret_scan.py .
```

Delete `tmp-ledger.json` and `tmp-rank-math-writer.php` after the smoke test.
