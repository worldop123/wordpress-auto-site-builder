# Contributing

Contributions are welcome if they keep the workflow portable, safe, and maintainable.

## Principles

- Keep the skill useful across AI coding tools.
- Prefer small, scoped, auditable rules over giant prompt blocks.
- Keep live-site safety first: backups, protected data, rollback notes, and QA evidence.
- Preserve the fixed stack unless a new architecture is explicitly documented.
- Do not add secrets, credentials, private site data, or client content.

## Before Opening a Pull Request

- Run a secret scan locally.
- Check that no rule contradicts the launch gate.
- Check that no snippet encourages global mutation loops, automatic cart submits, unsafe permissions, or hardcoded secrets.
- Keep reference files directly discoverable from `SKILL.md`.
- Update docs when adding behavior that users or maintainers need to know.

## Pull Request Checklist

- [ ] No secrets or private data.
- [ ] No client-specific credentials, URLs, orders, or customer information.
- [ ] Changes are compatible with Codex, Claude, Trae, Cursor, OpenHands, and Aider where possible.
- [ ] New snippet guidance includes lifecycle, scope, rollback, and verification.
- [ ] Button/interactivity rules still require real click/input testing.
- [ ] Launch mode remains blocked until pages, products, articles, SEO, and full QA pass.
