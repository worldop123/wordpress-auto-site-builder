#!/usr/bin/env python3
"""Create and update a resumable WordPress build ledger."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


DEFAULT_LEDGER = {
    "schema": "wordpress-auto-site-builder-ledger-v1",
    "site": {},
    "mode": {
        "build_mode": "",
        "interaction_mode": "ask_user",
    },
    "checkpoints": {
        "current_phase": "not_started",
        "last_verified_gate": "",
        "next_safe_action": "",
    },
    "wordpress_ids": {
        "pages": {},
        "posts": {},
        "products": {},
        "media": {},
        "menus": {},
        "snippets": {},
    },
    "woocommerce": {
        "page_bindings": {},
        "currency": "",
        "payment_methods": [],
        "shipping_zones": [],
    },
    "product_imports": [],
    "articles": [],
    "qa": {
        "passed": [],
        "pending": [],
        "blockers": [],
    },
    "credentials": {
        "temporary_created": [],
        "revoked": [],
        "needs_rotation": [],
    },
    "events": [],
}

RECOVERY_CHECKS = [
    "read_latest_ledger",
    "identify_last_verified_gate",
    "check_pages_and_ids",
    "check_woocommerce_bindings",
    "check_active_snippets",
    "check_product_category_media_counts",
    "check_article_statuses",
    "check_menus_and_home_blog_settings",
    "check_rank_math_sitemap",
    "check_product_cart_checkout_availability",
    "revoke_or_rotate_temporary_credentials",
    "choose_smallest_safe_unfinished_step",
]


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def load(path: Path) -> dict[str, Any]:
    if not path.exists():
        return json.loads(json.dumps(DEFAULT_LEDGER))
    return json.loads(path.read_text(encoding="utf-8"))


def save(path: Path, ledger: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    ledger["updated_at"] = now()
    path.write_text(json.dumps(ledger, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def add_event(ledger: dict[str, Any], event_type: str, message: str, data: dict[str, Any] | None = None) -> None:
    ledger.setdefault("events", []).append(
        {
            "time": now(),
            "type": event_type,
            "message": message,
            "data": data or {},
        }
    )


def cmd_init(args: argparse.Namespace) -> int:
    path = args.ledger
    ledger = load(path)
    ledger["created_at"] = ledger.get("created_at") or now()
    ledger["site"].update(
        {
            "brand": args.brand or ledger["site"].get("brand", ""),
            "domain": args.domain or ledger["site"].get("domain", ""),
        }
    )
    if args.interaction_mode:
        ledger["mode"]["interaction_mode"] = args.interaction_mode
    if args.build_mode:
        ledger["mode"]["build_mode"] = args.build_mode
    add_event(ledger, "init", "Ledger initialized or refreshed.")
    save(path, ledger)
    print(f"Ledger ready: {path}")
    return 0


def cmd_event(args: argparse.Namespace) -> int:
    ledger = load(args.ledger)
    data = json.loads(args.data) if args.data else {}
    add_event(ledger, args.type, args.message, data)
    if args.phase:
        ledger["checkpoints"]["current_phase"] = args.phase
    if args.gate:
        ledger["checkpoints"]["last_verified_gate"] = args.gate
    if args.next:
        ledger["checkpoints"]["next_safe_action"] = args.next
    save(args.ledger, ledger)
    print("Event added.")
    return 0


def cmd_recovery(args: argparse.Namespace) -> int:
    ledger = load(args.ledger)
    report = {
        "ledger": str(args.ledger),
        "site": ledger.get("site", {}),
        "mode": ledger.get("mode", {}),
        "checkpoints": ledger.get("checkpoints", {}),
        "temporary_credentials_needing_rotation": ledger.get("credentials", {}).get("needs_rotation", []),
        "recovery_checks": [{"check": check, "status": "pending"} for check in RECOVERY_CHECKS],
        "do_not_repeat_without_evidence": [
            "old_site_cleanup",
            "product_deletion",
            "product_csv_import",
            "media_import",
            "article_publish_or_schedule",
            "page_deletion",
            "snippet_replacement",
            "launch_or_indexing_submission",
        ],
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0


def cmd_summary(args: argparse.Namespace) -> int:
    ledger = load(args.ledger)
    summary = {
        "site": ledger.get("site", {}),
        "mode": ledger.get("mode", {}),
        "checkpoints": ledger.get("checkpoints", {}),
        "counts": {
            "pages": len(ledger.get("wordpress_ids", {}).get("pages", {})),
            "posts": len(ledger.get("wordpress_ids", {}).get("posts", {})),
            "products": len(ledger.get("wordpress_ids", {}).get("products", {})),
            "media": len(ledger.get("wordpress_ids", {}).get("media", {})),
            "snippets": len(ledger.get("wordpress_ids", {}).get("snippets", {})),
            "product_imports": len(ledger.get("product_imports", [])),
            "articles": len(ledger.get("articles", [])),
            "events": len(ledger.get("events", [])),
        },
        "qa_blockers": ledger.get("qa", {}).get("blockers", []),
        "next_safe_action": ledger.get("checkpoints", {}).get("next_safe_action", ""),
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


def main() -> int:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="cmd", required=True)

    p_init = sub.add_parser("init")
    p_init.add_argument("ledger", type=Path)
    p_init.add_argument("--brand", default="")
    p_init.add_argument("--domain", default="")
    p_init.add_argument("--interaction-mode", choices=("ask_user", "autonomous"))
    p_init.add_argument("--build-mode", default="")
    p_init.set_defaults(func=cmd_init)

    p_event = sub.add_parser("event")
    p_event.add_argument("ledger", type=Path)
    p_event.add_argument("--type", default="note")
    p_event.add_argument("--message", required=True)
    p_event.add_argument("--data", default="")
    p_event.add_argument("--phase", default="")
    p_event.add_argument("--gate", default="")
    p_event.add_argument("--next", default="")
    p_event.set_defaults(func=cmd_event)

    p_recovery = sub.add_parser("recovery")
    p_recovery.add_argument("ledger", type=Path)
    p_recovery.set_defaults(func=cmd_recovery)

    p_summary = sub.add_parser("summary")
    p_summary.add_argument("ledger", type=Path)
    p_summary.set_defaults(func=cmd_summary)

    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
