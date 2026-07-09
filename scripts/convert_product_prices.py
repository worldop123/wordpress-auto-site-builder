#!/usr/bin/env python3
"""Convert WooCommerce CSV product prices between currencies.

Use an explicit exchange rate or a rates JSON file. The script does not fetch
live rates by itself so the build ledger can record the chosen source clearly.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Any


PRICE_COLUMNS = ("Regular price", "Sale price")
BACKUP_PREFIX = "Meta: _source_"
NUMERIC_RE = re.compile(r"[-+]?\d+(?:[.,]\d+)?")


def parse_price(value: str) -> Decimal | None:
    if value is None:
        return None
    text = str(value).strip()
    if not text:
        return None
    match = NUMERIC_RE.search(text.replace(" ", ""))
    if not match:
        return None
    normalized = match.group(0).replace(",", ".")
    try:
        return Decimal(normalized)
    except InvalidOperation:
        return None


def format_price(value: Decimal, decimals: int) -> str:
    quant = Decimal("1") if decimals == 0 else Decimal("1").scaleb(-decimals)
    return str(value.quantize(quant, rounding=ROUND_HALF_UP))


def charm_round(value: Decimal, decimals: int, ending: str | None) -> Decimal:
    if not ending:
        return value
    if decimals <= 0:
        return value.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    ending_decimal = Decimal(ending)
    whole = value.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    candidate = whole - Decimal("1") + ending_decimal
    if candidate <= 0:
        return value
    return candidate


def load_rate(args: argparse.Namespace) -> Decimal:
    if args.rate:
        return Decimal(str(args.rate))
    if not args.rates_json:
        raise SystemExit("Provide --rate or --rates-json")
    data = json.loads(Path(args.rates_json).read_text(encoding="utf-8-sig"))
    key = f"{args.source_currency.upper()}_{args.target_currency.upper()}"
    if key in data:
        return Decimal(str(data[key]))
    nested = data.get(args.source_currency.upper()) or data.get(args.source_currency.lower()) or {}
    if args.target_currency.upper() in nested:
        return Decimal(str(nested[args.target_currency.upper()]))
    if args.target_currency.lower() in nested:
        return Decimal(str(nested[args.target_currency.lower()]))
    raise SystemExit(f"Rate not found for {args.source_currency}->{args.target_currency}")


def convert_csv(args: argparse.Namespace) -> dict[str, Any]:
    if args.decimals < 0:
        raise SystemExit("--decimals must be 0 or greater")

    source = Path(args.input)
    output = Path(args.output)
    rate = load_rate(args)
    source_currency = args.source_currency.upper()
    target_currency = args.target_currency.upper()

    with source.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f, dialect=csv.excel)
        headers = reader.fieldnames or []
        rows = [dict(row) for row in reader]

    missing_price_columns = [col for col in PRICE_COLUMNS if col not in headers]
    working_headers = list(headers)
    backup_columns: list[str] = []
    for price_col in PRICE_COLUMNS:
        base = f"{BACKUP_PREFIX}{price_col.lower().replace(' ', '_')}"
        backup_columns.extend([base, f"{base}_currency", f"{base}_fx_rate"])
    for col in backup_columns:
        if col not in working_headers:
            working_headers.append(col)

    converted_cells = 0
    skipped_cells = 0
    changed_rows = 0
    samples: list[dict[str, Any]] = []

    for index, row in enumerate(rows, start=1):
        row_changed = False
        for col in PRICE_COLUMNS:
            if col not in headers:
                continue
            original = row.get(col, "")
            parsed = parse_price(original)
            if parsed is None:
                if original:
                    skipped_cells += 1
                continue
            converted = parsed * rate
            converted = charm_round(converted, args.decimals, args.charm_ending)
            formatted = format_price(converted, args.decimals)
            base = f"{BACKUP_PREFIX}{col.lower().replace(' ', '_')}"
            row[base] = str(original)
            row[f"{base}_currency"] = source_currency
            row[f"{base}_fx_rate"] = str(rate)
            row[col] = formatted
            converted_cells += 1
            row_changed = True
            if len(samples) < args.sample_limit:
                samples.append(
                    {
                        "row": index,
                        "id": row.get("ID") or row.get("id"),
                        "sku": row.get("SKU") or row.get("sku"),
                        "column": col,
                        "source": str(original),
                        "converted": formatted,
                    }
                )
        if row_changed:
            changed_rows += 1

    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=working_headers, dialect=csv.excel, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    report = {
        "input": str(source),
        "output": str(output),
        "source_currency": source_currency,
        "target_currency": target_currency,
        "rate": str(rate),
        "rate_source": args.rate_source,
        "rate_timestamp": args.rate_timestamp,
        "decimals": args.decimals,
        "charm_ending": args.charm_ending,
        "row_count": len(rows),
        "changed_rows": changed_rows,
        "converted_cells": converted_cells,
        "skipped_cells": skipped_cells,
        "missing_price_columns": missing_price_columns,
        "backup_columns_added": backup_columns,
        "samples": samples,
        "notes": [
            "Verify target WooCommerce currency setting before import.",
            "Keep original source CSV unchanged.",
            "Record exchange-rate source and timestamp in the import ledger.",
        ],
    }
    return report


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("input", help="Input WooCommerce product CSV")
    parser.add_argument("--output", required=True, help="Converted output CSV")
    parser.add_argument("--source-currency", required=True, help="ISO 4217 source currency, e.g. USD")
    parser.add_argument("--target-currency", required=True, help="ISO 4217 target currency, e.g. CZK")
    parser.add_argument("--rate", help="Explicit source->target exchange rate")
    parser.add_argument("--rates-json", help="JSON file with rates, e.g. {'USD_CZK': 22.5}")
    parser.add_argument("--rate-source", default="user_provided_or_runtime_checked", help="Rate source label and timestamp")
    parser.add_argument("--rate-timestamp", default=datetime.now(timezone.utc).isoformat(), help="Exchange-rate retrieval timestamp")
    parser.add_argument("--decimals", type=int, default=2)
    parser.add_argument("--charm-ending", help="Optional price ending such as 0.99, applied after conversion")
    parser.add_argument("--sample-limit", type=int, default=10)
    args = parser.parse_args()

    report = convert_csv(args)
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if report["missing_price_columns"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
