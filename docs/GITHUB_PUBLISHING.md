# GitHub Publishing Guide

Use this guide when preparing a public GitHub release.

## Pre-Publish

1. Run the helper script smoke tests from `INSTALL.md`.
2. Run `python scripts/secret_scan.py .`.
3. Review `docs/OPEN_SOURCE_RELEASE_CHECKLIST.md`.
4. Confirm no live customer credentials, screenshots with private data, exports, backups, writer PHP files, or browser sessions are committed.
5. Confirm English and Chinese docs are updated together where applicable.

## Repository Settings

Recommended:

- Visibility: public only after the secret scan passes.
- Default branch: `main`.
- Issues: enabled.
- Discussions: optional.
- Wiki: optional; prefer docs in the repository.
- Vulnerability reporting: enabled when available.
- Branch protection: require CI before merging once contributors are active.

## First Release

Suggested tag:

```bash
git tag v0.1.0
git push origin v0.1.0
```

Suggested release notes:

- Universal AI-agent WordPress/WooCommerce SEO workflow.
- New site build, old-site rebuild, and existing-site SEO optimization modes.
- Rank Math Free one-time writer workflow.
- WooCommerce official CSV inspection helpers.
- Chinese and English open-source documentation.

## After Publish

- Check the GitHub repository page renders Markdown correctly.
- Check Community Standards status.
- Check Actions CI status.
- Open a test issue from the template.
- Keep tokens and customer materials out of future commits.
