#!/usr/bin/env python3
"""Validate a WordPress auto-site-builder config and print a build/launch plan."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ALLOWED_INTERACTION_MODES = {"ask_user", "autonomous"}
ALLOWED_BUILD_MODES = {
    "new",
    "old_rebuild",
    "existing_seo_optimization",
    "repair",
    "seo_content",
    "woocommerce_ux",
    "skill_update",
    "mixed",
}

REQUIRED_SITE = ["domain", "brand", "site_type"]
REQUIRED_ACCESS = ["wp_admin_url", "auth_method"]

FULL_STORE_SURFACES = [
    "home",
    "shop_product_archive",
    "product_category_archives",
    "single_product",
    "blog_index",
    "blog_archives",
    "single_post",
    "cart",
    "checkout",
    "my_account",
    "contact",
    "faq",
    "about",
    "shipping_policy",
    "returns_policy",
    "payment_policy",
    "privacy_policy",
    "terms",
    "cookie_policy",
    "age_or_compliance",
]

INTERACTION_QA = [
    "desktop_links",
    "mobile_links",
    "desktop_buttons",
    "mobile_buttons",
    "mobile_menu",
    "quantity_product",
    "quantity_cart",
    "add_to_cart",
    "update_cart",
    "checkout_boundary",
    "forms",
    "age_cookie_gates",
    "no_overlay_blocks_clicks",
    "no_layout_overflow_360_390_430",
]

PHASES = [
    "select_service_mode_new_old_rebuild_or_existing_seo",
    "resume_read_ledger_and_verify_live_state_if_interrupted",
    "collect_requirements",
    "inspect_environment",
    "set_foundation_baseline_rankmath_menus_bindings",
    "generate_homepage_style_preview_or_record_autonomous_mode",
    "create_and_bind_pages",
    "set_elementor_canvas_and_import_html",
    "rewrite_product_csv_originality_and_rankmath_seo",
    "verify_product_csv_gallery_body_images_and_long_descriptions",
    "create_categories_products_variations",
    "generate_global_shell",
    "generate_full_store_surface_layouts",
    "generate_home_blog_policy_contact_page_html",
    "rebuild_product_single_archive_blog_archive_layouts",
    "generate_product_page_ux",
    "generate_cart_checkout_rules",
    "generate_compliance_or_age_gate",
    "write_rankmath_metadata",
    "audit_rank_math_on_page_checks_before_writer",
    "generate_rank_math_one_time_writer_if_needed",
    "verify_rank_math_meta_and_delete_writer_snippet",
    "generate_initial_seo_article_batch",
    "write_image_alt_metadata",
    "run_storefront_and_seo_qa",
    "verify_all_buttons_forms_quantity_controls_and_no_overflow",
    "verify_articles_products_archives_rankmath_schema_sitemap",
    "pass_launch_gate",
    "prepare_indexing_package",
    "final_launch_report",
]

EXISTING_SEO_PHASES = [
    "select_service_mode_new_old_rebuild_or_existing_seo",
    "resume_read_ledger_and_verify_live_state_if_interrupted",
    "collect_existing_seo_scope_and_preservation_rules",
    "inspect_environment_read_only",
    "verify_rank_math_and_prompt_account_connection",
    "verify_code_snippets_or_install_if_authorized",
    "inventory_pages_products_posts_terms_media_rankmath_sitemap_schema",
    "detect_missing_duplicate_generic_or_weak_seo_fields",
    "generate_content_aware_rank_math_mapping",
    "audit_rank_math_on_page_checks_before_writer",
    "fix_content_gaps_without_rebuilding_layouts_if_authorized",
    "generate_rank_math_one_time_writer_if_needed",
    "run_writer_once_and_capture_written_skipped_failed_ids",
    "verify_rank_math_meta_sitemap_robots_schema_and_frontend_source",
    "disable_and_delete_one_time_writer_snippet",
    "verify_no_layout_slug_commerce_checkout_or_shipping_regressions",
    "final_existing_site_seo_report",
]


def load_config(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except FileNotFoundError:
        raise SystemExit(f"Config not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Invalid JSON: {exc}")


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def validate(config: dict[str, Any]) -> dict[str, Any]:
    site = config.get("site") or {}
    access = config.get("access") or {}
    commerce = config.get("commerce") or {}
    product_import = config.get("product_import") or {}
    seo = config.get("seo") or {}
    articles = config.get("articles") or {}
    plugins = config.get("plugins") or {}

    missing: list[str] = []
    warnings: list[str] = []
    launch_blockers: list[str] = []

    for field in REQUIRED_SITE:
        if not site.get(field):
            missing.append(f"site.{field}")
    for field in REQUIRED_ACCESS:
        if not access.get(field):
            missing.append(f"access.{field}")

    interaction_mode = site.get("interaction_mode", "ask_user")
    if interaction_mode not in ALLOWED_INTERACTION_MODES:
        missing.append("site.interaction_mode must be ask_user or autonomous")

    build_mode = site.get("build_mode", "new")
    if build_mode not in ALLOWED_BUILD_MODES:
        warnings.append(f"Unknown site.build_mode: {build_mode}")
    existing_seo_mode = build_mode == "existing_seo_optimization"

    if site.get("site_type") == "ecommerce" and not existing_seo_mode:
        if not commerce.get("currency"):
            missing.append("commerce.currency")
        if not commerce.get("payment_methods"):
            launch_blockers.append("payment_methods_not_defined")
        if not commerce.get("shipping_countries"):
            launch_blockers.append("shipping_countries_not_defined")
        if not config.get("products") and not product_import.get("csv_source"):
            missing.append("products[] or product_import.csv_source")
    elif site.get("site_type") == "ecommerce" and existing_seo_mode:
        warnings.append("Existing-site SEO mode: preserve products/prices/stock/checkout; inventory live products instead of requiring CSV.")

    if interaction_mode == "autonomous":
        warnings.append("Autonomous mode: record AI decisions and do not pause for routine approvals.")
    else:
        warnings.append("Ask-user mode: approval gates remain active.")

    if existing_seo_mode:
        optimize_scope = seo.get("optimize_scope", "full_site")
        preserve_meta = seo.get("preserve_existing_custom_meta", True)
        if optimize_scope not in {"full_site", "pages", "products", "posts", "categories"}:
            warnings.append(f"Unknown seo.optimize_scope: {optimize_scope}")
        if preserve_meta is not True:
            warnings.append("Existing-site SEO mode: overwriting existing custom SEO metadata must be explicitly authorized and recorded.")
        if not plugins.get("code_snippets_active"):
            if interaction_mode == "autonomous" or plugins.get("code_snippets_install_allowed"):
                warnings.append("Code Snippets missing/unconfirmed: install and activate automatically, then verify before one-time writers.")
            else:
                launch_blockers.append("code_snippets_install_permission_required_for_rank_math_writer")
        warnings.append("Existing-site SEO mode: do not rebuild pages/layouts or change commerce settings unless separately authorized.")

    if site.get("adult_or_regulated"):
        launch_blockers.append("regulated_product_compliance_must_be_verified")

    if not seo.get("seed_keywords") and not seo.get("competitors"):
        warnings.append("SEO seed keywords/competitors missing; agent must infer carefully or ask in ask_user mode.")

    article_count = articles.get("initial_batch_count", 10)
    if article_count is None:
        article_count = 10
    try:
        article_count_int = int(article_count)
    except (TypeError, ValueError):
        article_count_int = 0
    if not existing_seo_mode and not articles.get("opt_out") and article_count_int <= 0:
        launch_blockers.append("initial_article_batch_missing")

    if product_import.get("csv_source"):
        if product_import.get("gallery_required", True) and not product_import.get("image_columns"):
            launch_blockers.append("csv_gallery_image_columns_not_defined")
        if product_import.get("body_images_required", True) and not product_import.get("body_image_strategy"):
            warnings.append("CSV body image strategy missing; inspect descriptions for inline images before import.")

    expected_surfaces = set(FULL_STORE_SURFACES)
    configured_surfaces = set(as_list(config.get("surfaces")))
    if existing_seo_mode:
        missing_surfaces = []
    else:
        missing_surfaces = sorted(expected_surfaces - configured_surfaces) if configured_surfaces else sorted(expected_surfaces)

    return {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "site": {
            "brand": site.get("brand"),
            "domain": site.get("domain"),
            "site_type": site.get("site_type"),
            "build_mode": build_mode,
            "interaction_mode": interaction_mode,
            "language": site.get("language"),
            "market": site.get("market"),
        },
        "missing_required_fields": missing,
        "warnings": warnings,
        "launch_blockers": launch_blockers,
        "required_surfaces": FULL_STORE_SURFACES,
        "missing_or_unconfirmed_surfaces": missing_surfaces,
        "interaction_qa": INTERACTION_QA,
        "phase_checklist": EXISTING_SEO_PHASES if existing_seo_mode else PHASES,
        "service_mode_choices": [
            "new: New site build",
            "old_rebuild: Old-site rebuild preserving protected products/media",
            "existing_seo_optimization: Existing-site SEO optimization without page rebuild",
        ],
        "rank_math_first_use": "Prompt user to connect Rank Math account; record connected, user_skipped, or blocked.",
        "resume_rule": "If interrupted, read ledger, verify live state read-only, revoke temporary credentials, and continue from smallest safe unfinished step.",
    }


def print_markdown(plan: dict[str, Any]) -> None:
    site = plan["site"]
    print(f"# Site Plan: {site.get('brand') or '<missing>'}")
    print()
    print(f"- Domain: {site.get('domain') or '<missing>'}")
    print(f"- Type: {site.get('site_type') or '<missing>'}")
    print(f"- Build mode: {site.get('build_mode')}")
    print(f"- Interaction mode: {site.get('interaction_mode')}")
    print(f"- Market/language: {site.get('market') or '<missing>'} / {site.get('language') or '<missing>'}")
    print()

    print("## Service Mode Choices")
    for choice in plan["service_mode_choices"]:
        print(f"- {choice}")
    print()

    for title, key in [
        ("Missing Required Fields", "missing_required_fields"),
        ("Warnings", "warnings"),
        ("Launch Blockers", "launch_blockers"),
        ("Missing or Unconfirmed Surfaces", "missing_or_unconfirmed_surfaces"),
    ]:
        print(f"## {title}")
        items = plan[key]
        if items:
            for item in items:
                print(f"- {item}")
        else:
            print("- none")
        print()

    print("## Phase Checklist")
    for phase in plan["phase_checklist"]:
        print(f"- [ ] {phase}")
    print()

    print("## Interaction QA")
    for item in plan["interaction_qa"]:
        print(f"- [ ] {item}")
    print()

    print(f"Rank Math: {plan['rank_math_first_use']}")
    print(f"Resume: {plan['resume_rule']}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("config", type=Path, help="Path to site_config JSON")
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    args = parser.parse_args()

    plan = validate(load_config(args.config))
    if args.format == "json":
        print(json.dumps(plan, ensure_ascii=False, indent=2))
    else:
        print_markdown(plan)

    return 2 if plan["missing_required_fields"] else 0


if __name__ == "__main__":
    sys.exit(main())
