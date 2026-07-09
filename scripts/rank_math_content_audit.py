#!/usr/bin/env python3
"""Audit content and Rank Math metadata against common on-page SEO checks."""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


WORD_RE = re.compile(r"\b[\w'-]+\b", re.UNICODE)


class ContentParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.text_parts: list[str] = []
        self.heading_parts: list[str] = []
        self.image_alts: list[str] = []
        self.links: list[str] = []
        self.media_count = 0
        self._heading_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {k.lower(): v or "" for k, v in attrs}
        tag = tag.lower()
        if tag in {"h2", "h3", "h4"}:
            self._heading_depth += 1
        if tag == "img":
            self.media_count += 1
            self.image_alts.append(attrs_dict.get("alt", ""))
        if tag in {"video", "iframe", "picture"}:
            self.media_count += 1
        if tag == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"])

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() in {"h2", "h3", "h4"} and self._heading_depth:
            self._heading_depth -= 1

    def handle_data(self, data: str) -> None:
        text = data.strip()
        if not text:
            return
        self.text_parts.append(text)
        if self._heading_depth:
            self.heading_parts.append(text)


def load_items(path: Path) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    if isinstance(data, dict):
        data = data.get("items") or data.get("mapping") or []
    if not isinstance(data, list):
        raise SystemExit("Input must be a JSON list or object with items/mapping.")
    return data


def normalize(text: Any) -> str:
    return re.sub(r"\s+", " ", str(text or "")).strip().lower()


def words(text: str) -> list[str]:
    return WORD_RE.findall(text.lower())


def keyword_count(text: str, keyword: str) -> int:
    text_norm = normalize(text)
    keyword_norm = normalize(keyword)
    if not keyword_norm:
        return 0
    return text_norm.count(keyword_norm)


def parse_content(item: dict[str, Any]) -> dict[str, Any]:
    html = str(item.get("content_html") or item.get("content") or item.get("description") or "")
    parser = ContentParser()
    parser.feed(html)
    text = normalize(" ".join(parser.text_parts) or html)
    headings = normalize(" ".join(parser.heading_parts))
    return {
        "html": html,
        "text": text,
        "headings": headings,
        "image_alts": parser.image_alts + [str(v) for v in item.get("image_alts", [])],
        "links": parser.links + [str(v) for v in item.get("internal_links", [])],
        "media_count": parser.media_count + len(item.get("media", []) or []),
    }


def audit_item(item: dict[str, Any], seen_keywords: set[str]) -> dict[str, Any]:
    focus = normalize(item.get("focus_keyword"))
    seo_title = normalize(item.get("seo_title"))
    seo_description = normalize(item.get("seo_description"))
    parsed = parse_content(item)
    content_text = parsed["text"]
    content_words = words(content_text)
    first_words = " ".join(content_words[:40])
    density = 0.0
    if content_words and focus:
        density = keyword_count(content_text, focus) / max(len(content_words), 1) * 100

    checks = {
        "focus_keyword_in_seo_title": bool(focus and focus in seo_title),
        "focus_keyword_at_beginning_of_seo_title": bool(focus and seo_title.startswith(focus)),
        "focus_keyword_in_meta_description": bool(focus and focus in seo_description),
        "focus_keyword_near_content_start": bool(focus and focus in first_words),
        "focus_keyword_in_content": bool(focus and focus in content_text),
        "focus_keyword_in_subheading": bool(focus and focus in parsed["headings"]),
        "image_alt_contains_focus_keyword": any(focus and focus in normalize(alt) for alt in parsed["image_alts"]),
        "keyword_density_nonzero": density > 0,
        "has_internal_link": any(str(link).startswith("/") or item.get("site_domain", "") in str(link) for link in parsed["links"]),
        "focus_keyword_unique": focus not in seen_keywords if focus else False,
        "short_paragraphs_present": bool(re.search(r"</p>|\\n\\n", str(item.get("content_html") or item.get("content") or ""), re.I)),
        "has_rich_media": parsed["media_count"] > 0,
        "content_not_too_thin": len(content_words) >= int(item.get("minimum_words", 300)),
    }
    if focus:
        seen_keywords.add(focus)
    failed = [name for name, ok in checks.items() if not ok]
    return {
        "id": item.get("id"),
        "object_type": item.get("object_type"),
        "focus_keyword": item.get("focus_keyword"),
        "word_count": len(content_words),
        "keyword_density_percent": round(density, 3),
        "checks": checks,
        "failed": failed,
        "pass": not failed,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("mapping", type=Path, help="JSON list with SEO metadata and content fields")
    args = parser.parse_args()

    seen_keywords: set[str] = set()
    results = [audit_item(item, seen_keywords) for item in load_items(args.mapping)]
    report = {
        "items": results,
        "summary": {
            "total": len(results),
            "passed": sum(1 for item in results if item["pass"]),
            "failed": sum(1 for item in results if not item["pass"]),
        },
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 2 if report["summary"]["failed"] else 0


if __name__ == "__main__":
    sys.exit(main())
