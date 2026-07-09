# Maintainer Guide

## Design Goals

- Keep the workflow universal across AI coding tools.
- Keep the WordPress stack simple and auditable.
- Prefer real verification over optimistic summaries.
- Treat launch readiness as a strict gate.
- Keep generated code small, scoped, and reversible.

## Where to Put Rules

- `SKILL.md`: only core rules, trigger-critical behavior, dead rules, and reference routing.
- `references/intake-checklist.md`: requirement collection and site_config schema.
- `references/phase-playbook.md`: build sequence and phase gates.
- `references/qa-and-launch.md`: verification and launch criteria.
- `references/code-snippets-implementation-guide.md`: snippet security, interactivity, and implementation rules.
- `references/woocommerce-customizations-guide.md`: WooCommerce UX patterns.
- `references/product-csv-originality-seo.md`: CSV rewrite/import/media integrity.
- `docs/RESUME_PROTOCOL.md`: interruption recovery and checkpoint expectations.
- `docs/`: public GitHub usage and maintainer docs.

## Avoiding Skill Bloat

`SKILL.md` is already large. Prefer adding detailed content to a reference file or docs file, then link to it from `SKILL.md`.

Add a rule to `SKILL.md` only when it must be seen immediately after the skill triggers.

## Release Process

1. Review user-requested changes and decide whether they are workflow rules, implementation examples, or public docs.
2. Patch the smallest relevant files.
3. Run searches for contradictions.
4. Confirm resume protocol still blocks repeated destructive work after interruption.
5. Run secret scans.
6. Run helper script smoke tests.
7. Update release notes if using GitHub releases.

## Compatibility Review

Before merging a feature, ask:

- Can Codex follow it?
- Can Claude follow it from local files?
- Can Trae/Cursor/OpenHands/Aider follow it without Codex-specific APIs?
- Does it avoid assuming one browser tool or one operating system?
- Does it provide a fallback when live automation is blocked?
- Can it resume safely after server errors, browser crashes, context compaction, or network failures?

## Safety Review

Reject changes that:

- Encourage storing credentials.
- Encourage unsafe payment or checkout logic.
- Skip product/media preservation.
- Skip article generation silently.
- Allow launch before QA.
- Repeat destructive work after interruption without read-only recovery checks.
- Create large opaque code blobs.
- Depend on one client's private data.
