#!/usr/bin/env python3
"""Inspect a WooCommerce product CSV for rewrite/import/media integrity."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


PROTECTED_HINTS = {
    "id",
    "type",
    "sku",
    "slug",
    "parent",
    "regular price",
    "sale price",
    "stock",
    "stock status",
    "images",
    "categories",
    "attribute",
    "tax",
    "shipping",
    "weight",
    "length",
    "width",
    "height",
}

EDITABLE_HINTS = {
    "name",
    "short description",
    "description",
    "tags",
    "rank_math",
    "seo",
    "focus",
    "meta description",
    "seo title",
    "image alt",
    "alt text",
}

IMAGE_HEADER_HINTS = {"images", "image", "gallery", "thumbnail", "featured image"}
DESCRIPTION_HEADER_HINTS = {"description", "short description", "content", "body"}
RANK_MATH_HINTS = {"rank_math", "rank math", "focus keyword", "seo title", "seo description"}
KNOWN_META_POLICIES = {
    "rank_math_title": "editable_rank_math_seo",
    "rank_math_description": "editable_rank_math_seo",
    "rank_math_focus_keyword": "editable_rank_math_seo",
    "rank_math_internal_links_processed": "protect_runtime_meta",
    "rank_math_analytic_object_id": "protect_runtime_meta",
    "_yoast_wpseo_title": "editable_yoast_migration",
    "_yoast_wpseo_metadesc": "editable_yoast_migration",
    "_yoast_wpseo_focuskw": "editable_yoast_migration",
}

IMG_RE = re.compile(r"<img\b[^>]*\bsrc=[\"']([^\"']+)[\"']", re.I)
URL_RE = re.compile(r"https?://[^\s,;|\"')<>]+", re.I)


def classify(header: str) -> str:
    h = header.strip().lower()
    key = meta_key(header)
    if key:
        policy = KNOWN_META_POLICIES.get(key, "review_custom_meta")
        if policy.startswith("protect"):
            return "protect"
        if policy.startswith("editable"):
            return "editable"
        return "review"
    if any(token in h for token in PROTECTED_HINTS):
        return "protect"
    if any(token in h for token in EDITABLE_HINTS):
        return "editable"
    return "review"


def read_with_dialect(path: Path, dialect: csv.Dialect) -> tuple[list[str], list[dict[str, str]], dict[str, Any]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, dialect=dialect)
        headers = reader.fieldnames or []
        rows = [dict(row) for row in reader]
    quality = {
        "rows": len(rows),
        "headers": len(headers),
        "image_values": sum(1 for row in rows if (row.get("Images") or "").startswith(("http://", "https://"))),
        "position_numeric": sum(1 for row in rows if (row.get("Position") or "").strip().isdigit()),
        "extra_field_rows": sum(1 for row in rows if row.get(None)),
    }
    return headers, rows, quality


def sniff(path: Path) -> tuple[csv.Dialect, list[str], list[dict[str, str]], dict[str, Any]]:
    sample = path.read_text(encoding="utf-8-sig", errors="replace")[:16384]
    candidates: list[tuple[str, csv.Dialect]] = [("excel", csv.excel)]
    try:
        candidates.append(("sniffer", csv.Sniffer().sniff(sample)))
    except csv.Error:
        pass

    best_name = ""
    best_dialect = csv.excel
    best_headers: list[str] = []
    best_rows: list[dict[str, str]] = []
    best_quality: dict[str, Any] = {}
    best_score = -1

    for name, dialect in candidates:
        headers, rows, quality = read_with_dialect(path, dialect)
        score = (
            quality["headers"] * 10
            + quality["image_values"] * 5
            + quality["position_numeric"] * 3
            - quality["extra_field_rows"] * 20
        )
        if score > best_score:
            best_name = name
            best_dialect = dialect
            best_headers = headers
            best_rows = rows
            best_quality = quality
            best_score = score

    best_quality["parser"] = best_name
    best_quality["doublequote"] = getattr(best_dialect, "doublequote", None)
    return best_dialect, best_headers, best_rows, best_quality


def split_image_list(value: str) -> list[str]:
    if not value:
        return []
    urls = URL_RE.findall(value)
    if urls:
        return urls
    parts = re.split(r"\s*[,|]\s*", value.strip())
    return [part for part in parts if part]


def detect_columns(headers: list[str]) -> dict[str, list[str]]:
    groups = {
        "image_columns": [],
        "description_columns": [],
        "rank_math_columns": [],
        "identity_columns": [],
        "variation_columns": [],
    }
    for header in headers:
        h = header.lower().strip()
        if any(token in h for token in IMAGE_HEADER_HINTS):
            groups["image_columns"].append(header)
        if not h.startswith("meta:") and any(token in h for token in DESCRIPTION_HEADER_HINTS):
            groups["description_columns"].append(header)
        if any(token in h for token in RANK_MATH_HINTS):
            groups["rank_math_columns"].append(header)
        if h in {"id", "sku", "slug", "type", "parent"}:
            groups["identity_columns"].append(header)
        if "attribute" in h or h in {"type", "parent"}:
            groups["variation_columns"].append(header)
    return groups


def meta_key(header: str) -> str:
    if not header.lower().startswith("meta:"):
        return ""
    return header.split(":", 1)[1].strip()


def detect_meta_columns(headers: list[str]) -> list[dict[str, str]]:
    columns: list[dict[str, str]] = []
    for header in headers:
        key = meta_key(header)
        if not key:
            continue
        policy = KNOWN_META_POLICIES.get(key, "review_custom_meta")
        if key.startswith("rank_math"):
            source = "rank_math"
        elif key.startswith("_yoast"):
            source = "yoast"
        else:
            source = "custom"
        columns.append({"column": header, "meta_key": key, "source": source, "policy": policy})
    return columns


def row_type(row: dict[str, str]) -> str:
    for key in ("Type", "type"):
        value = (row.get(key) or "").strip().lower()
        if value:
            return value
    return "unknown"


def inspect(path: Path, sample_limit: int) -> dict[str, Any]:
    dialect, headers, rows, parser_quality = sniff(path)
    groups = detect_columns(headers)
    meta_columns = detect_meta_columns(headers)
    type_counts = Counter(row_type(row) for row in rows)

    image_stats = {
        "rows_with_images": 0,
        "total_image_refs": 0,
        "max_images_on_row": 0,
        "rows_with_inline_body_images": 0,
        "total_inline_body_images": 0,
    }
    row_samples: list[dict[str, Any]] = []
    blockers: list[str] = []
    warnings: list[str] = []

    sku_seen: Counter[str] = Counter()
    parent_values: Counter[str] = Counter()
    product_keys: set[str] = set()
    malformed_parent_rows: list[dict[str, Any]] = []

    for row in rows:
        if row_type(row) != "variation":
            for key in ("SKU", "sku", "Slug", "slug"):
                value = (row.get(key) or "").strip()
                if value:
                    product_keys.add(value)

    for index, row in enumerate(rows, start=1):
        sku = (row.get("SKU") or row.get("sku") or "").strip()
        if sku:
            sku_seen[sku] += 1
        parent = (row.get("Parent") or row.get("parent") or "").strip()
        if parent:
            parent_values[parent] += 1
            if "<" in parent or len(parent) > 180:
                malformed_parent_rows.append({"row": index, "id": row.get("ID"), "parent": parent[:180]})

        image_refs: list[str] = []
        for col in groups["image_columns"]:
            image_refs.extend(split_image_list(row.get(col, "") or ""))
        inline_images: list[str] = []
        for col in groups["description_columns"]:
            inline_images.extend(IMG_RE.findall(row.get(col, "") or ""))

        if image_refs:
            image_stats["rows_with_images"] += 1
        if inline_images:
            image_stats["rows_with_inline_body_images"] += 1
        image_stats["total_image_refs"] += len(image_refs)
        image_stats["total_inline_body_images"] += len(inline_images)
        image_stats["max_images_on_row"] = max(image_stats["max_images_on_row"], len(image_refs))

        if len(row_samples) < sample_limit:
            row_samples.append(
                {
                    "row": index,
                    "id": row.get("ID") or row.get("id"),
                    "sku": sku,
                    "type": row_type(row),
                    "name": row.get("Name") or row.get("name"),
                    "image_ref_count": len(image_refs),
                    "inline_body_image_count": len(inline_images),
                    "has_short_description": bool((row.get("Short description") or "").strip()),
                    "has_long_description": bool((row.get("Description") or "").strip()),
                    "parent": parent,
                }
            )

    duplicate_skus = sorted([sku for sku, count in sku_seen.items() if count > 1])
    unresolved_parents = sorted([value for value in parent_values if value not in product_keys])
    if rows and not groups["image_columns"]:
        blockers.append("no_image_or_gallery_column_detected")
    if rows and image_stats["rows_with_images"] == 0:
        blockers.append("no_product_image_refs_found")
    if "variable" in type_counts and "variation" not in type_counts:
        warnings.append("variable_products_without_variation_rows_detected")
    if "variation" in type_counts and not parent_values:
        blockers.append("variation_rows_without_parent_values")
    if malformed_parent_rows:
        blockers.append("malformed_parent_values_detected")
    if unresolved_parents:
        blockers.append("variation_parent_values_do_not_match_parent_sku_or_slug")
    if duplicate_skus:
        warnings.append("duplicate_skus_detected")
    if not groups["rank_math_columns"]:
        warnings.append("no_rank_math_columns_detected_use_mapping_or_writer")
    if image_stats["rows_with_inline_body_images"] > 0:
        warnings.append("inline_body_images_detected_verify_import_and_media_library")
    if parser_quality.get("parser") != "excel":
        warnings.append("csv_sniffer_parser_selected_verify_woocommerce_doublequote_fields")

    return {
        "file": str(path),
        "delimiter": dialect.delimiter,
        "parser_quality": parser_quality,
        "row_count": len(rows),
        "column_count": len(headers),
        "type_counts": dict(type_counts),
        "columns": [{"name": h, "classification": classify(h)} for h in headers],
        "detected_columns": groups,
        "meta_columns": meta_columns,
        "image_stats": image_stats,
        "duplicate_skus": duplicate_skus[:50],
        "parent_reference_count": sum(parent_values.values()),
        "unresolved_parent_values": unresolved_parents[:50],
        "malformed_parent_rows": malformed_parent_rows[:20],
        "sample_rows": row_samples,
        "import_blockers": blockers,
        "warnings": warnings,
        "required_after_import_checks": [
            "row_count_matches_expected",
            "featured_images_visible",
            "gallery_thumbnail_count_matches_csv",
            "inline_body_images_render",
            "long_descriptions_render",
            "variation_forms_work",
            "add_to_cart_works",
            "cart_quantity_works",
            "rank_math_meta_present",
            "product_sitemap_includes_products",
        ],
    }


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("--sample-limit", type=int, default=5)
    args = parser.parse_args()

    report = inspect(args.csv_path, args.sample_limit)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if report["import_blockers"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
