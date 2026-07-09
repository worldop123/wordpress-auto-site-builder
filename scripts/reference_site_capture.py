#!/usr/bin/env python3
"""Capture public reference-site HTML snapshots for layout analysis.

The output is for local analysis only. Do not commit captured third-party HTML.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import time
from collections import deque
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any
from urllib import error, parse, request, robotparser


USER_AGENT = "wordpress-auto-site-builder-reference-capture/0.1 (+https://github.com/worldop123/wordpress-auto-site-builder)"
HTML_RE = re.compile(r"text/html|application/xhtml\+xml", re.I)


class LinkAndMetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: list[str] = []
        self.title_parts: list[str] = []
        self.meta_description = ""
        self.h1: list[str] = []
        self.h2: list[str] = []
        self._tag_stack: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        attrs_dict = {key.lower(): value or "" for key, value in attrs}
        if tag == "a" and attrs_dict.get("href"):
            self.links.append(attrs_dict["href"])
        elif tag == "link" and attrs_dict.get("href"):
            rel = attrs_dict.get("rel", "")
            if "canonical" in rel or "alternate" in rel:
                self.links.append(attrs_dict["href"])
        elif tag == "meta":
            name = (attrs_dict.get("name") or attrs_dict.get("property") or "").lower()
            if name in {"description", "og:description"} and not self.meta_description:
                self.meta_description = attrs_dict.get("content", "")
        self._tag_stack.append(tag)

    def handle_endtag(self, tag: str) -> None:
        for index in range(len(self._tag_stack) - 1, -1, -1):
            if self._tag_stack[index] == tag:
                del self._tag_stack[index:]
                break

    def handle_data(self, data: str) -> None:
        text = " ".join(data.split())
        if not text:
            return
        current = self._tag_stack[-1] if self._tag_stack else ""
        if current == "title":
            self.title_parts.append(text)
        elif current == "h1":
            self.h1.append(text)
        elif current == "h2":
            self.h2.append(text)


def normalize_url(base: str, href: str) -> str | None:
    if not href:
        return None
    href = html.unescape(href.strip())
    if href.startswith(("mailto:", "tel:", "sms:", "javascript:", "#")):
        return None
    absolute = parse.urljoin(base, href)
    parts = parse.urlsplit(absolute)
    if parts.scheme not in {"http", "https"}:
        return None
    cleaned = parts._replace(fragment="")
    return parse.urlunsplit(cleaned)


def classify_url(url: str, title: str = "") -> str:
    path = parse.urlsplit(url).path.lower().strip("/")
    text = f"{path} {title.lower()}"
    if not path:
        return "home"
    checks = [
        ("checkout", ["checkout", "kasse", "caisse", "pago", "pokladna"]),
        ("cart", ["cart", "basket", "bag", "warenkorb", "kosik"]),
        ("account", ["account", "login", "register", "my-account", "customer"]),
        ("product", ["product/", "products/", "produkt/", "item/"]),
        ("shop_or_catalog", ["shop", "store", "catalog", "collections", "category", "collections/", "collections"]),
        ("blog_index_or_archive", ["blog", "news", "journal", "magazine", "guides", "articles"]),
        ("policy", ["privacy", "terms", "shipping", "returns", "refund", "cookie", "payment", "legal", "policy"]),
        ("contact", ["contact", "support", "help", "service"]),
        ("about", ["about", "company", "brand", "story"]),
        ("pricing", ["pricing", "plans"]),
        ("case_study", ["case-study", "case-studies", "portfolio", "work"]),
        ("documentation", ["docs", "documentation", "manual", "help-center"]),
        ("faq", ["faq", "questions"]),
    ]
    for page_type, needles in checks:
        if any(needle in text for needle in needles):
            return page_type
    return "other"


def safe_name(url: str) -> str:
    parts = parse.urlsplit(url)
    slug = (parts.netloc + parts.path).strip("/").replace("/", "_")
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", slug)[:80].strip("-") or "home"
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()[:10]
    return f"{slug}-{digest}.html"


def fetch(url: str, timeout: float) -> tuple[int, str, bytes, str]:
    req = request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "text/html,application/xhtml+xml"})
    with request.urlopen(req, timeout=timeout) as response:
        status = getattr(response, "status", 200)
        content_type = response.headers.get("Content-Type", "")
        final_url = response.geturl()
        body = response.read()
    return status, content_type, body, final_url


def decode_body(body: bytes, content_type: str) -> str:
    match = re.search(r"charset=([\w.-]+)", content_type, re.I)
    encodings = [match.group(1)] if match else []
    encodings.extend(["utf-8", "latin-1"])
    for encoding in encodings:
        try:
            return body.decode(encoding)
        except (LookupError, UnicodeDecodeError):
            continue
    return body.decode("utf-8", errors="replace")


def same_domain(url: str, root_netloc: str) -> bool:
    return parse.urlsplit(url).netloc.lower().lstrip("www.") == root_netloc.lower().lstrip("www.")


def robots_for(root_url: str) -> robotparser.RobotFileParser:
    parts = parse.urlsplit(root_url)
    robots_url = parse.urlunsplit((parts.scheme, parts.netloc, "/robots.txt", "", ""))
    rp = robotparser.RobotFileParser()
    rp.set_url(robots_url)
    try:
        rp.read()
    except Exception:
        pass
    return rp


def capture(args: argparse.Namespace) -> dict[str, Any]:
    start_url = args.url
    root_netloc = parse.urlsplit(start_url).netloc
    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_root = Path(args.output) / root_netloc.replace(":", "_") / timestamp
    pages_dir = out_root / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    rp = robots_for(start_url)
    queue: deque[str] = deque([start_url])
    seen: set[str] = set()
    captured: list[dict[str, Any]] = []
    skipped: list[dict[str, str]] = []

    while queue and len(captured) < args.max_pages:
        url = queue.popleft()
        if url in seen:
            continue
        seen.add(url)

        if args.same_domain and not same_domain(url, root_netloc):
            skipped.append({"url": url, "reason": "external_domain"})
            continue
        if not args.ignore_robots and not rp.can_fetch(USER_AGENT, url):
            skipped.append({"url": url, "reason": "robots_disallow"})
            continue

        try:
            status, content_type, body, final_url = fetch(url, args.timeout)
        except error.HTTPError as exc:
            skipped.append({"url": url, "reason": f"http_{exc.code}"})
            continue
        except Exception as exc:
            skipped.append({"url": url, "reason": type(exc).__name__})
            continue

        if not HTML_RE.search(content_type):
            skipped.append({"url": url, "reason": f"non_html:{content_type[:60]}"})
            continue

        html_text = decode_body(body, content_type)
        parser = LinkAndMetaParser()
        parser.feed(html_text)
        title = " ".join(parser.title_parts).strip()
        page_type = classify_url(final_url, title)
        file_name = safe_name(final_url)
        file_path = pages_dir / file_name
        file_path.write_text(html_text, encoding="utf-8")

        links = []
        for href in parser.links:
            normalized = normalize_url(final_url, href)
            if not normalized:
                continue
            links.append(normalized)
            if normalized not in seen and len(seen) + len(queue) < args.max_candidates:
                if not args.same_domain or same_domain(normalized, root_netloc):
                    queue.append(normalized)

        captured.append(
            {
                "url": url,
                "final_url": final_url,
                "status": status,
                "content_type": content_type,
                "page_type": page_type,
                "title": title,
                "meta_description": parser.meta_description,
                "h1": parser.h1[:5],
                "h2": parser.h2[:12],
                "html_file": str(file_path.relative_to(out_root)),
                "internal_link_count": sum(1 for link in links if same_domain(link, root_netloc)),
                "external_link_count": sum(1 for link in links if not same_domain(link, root_netloc)),
            }
        )

        if args.delay:
            time.sleep(args.delay)

    page_type_counts: dict[str, int] = {}
    for page in captured:
        page_type_counts[page["page_type"]] = page_type_counts.get(page["page_type"], 0) + 1

    manifest = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "start_url": start_url,
        "output_root": str(out_root),
        "user_agent": USER_AGENT,
        "robots_respected": not args.ignore_robots,
        "captured_count": len(captured),
        "skipped_count": len(skipped),
        "page_type_counts": page_type_counts,
        "pages": captured,
        "skipped": skipped[:200],
        "notes": [
            "Captured HTML is for local analysis only.",
            "Do not commit third-party HTML snapshots.",
            "Use snapshots to transform layout patterns into original WordPress/WooCommerce pages.",
        ],
    }
    (out_root / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    return manifest


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="Reference site URL to capture")
    parser.add_argument("--output", default=".reference-captures", help="Gitignored capture output directory")
    parser.add_argument("--max-pages", type=int, default=30)
    parser.add_argument("--max-candidates", type=int, default=500)
    parser.add_argument("--timeout", type=float, default=15)
    parser.add_argument("--delay", type=float, default=0.25)
    parser.add_argument("--allow-external", action="store_true", help="Allow crawling external domains; default is same-domain only")
    parser.add_argument("--ignore-robots", action="store_true", help="Only use for owned/authorized sites")
    args = parser.parse_args()
    args.same_domain = not args.allow_external

    manifest = capture(args)
    print(json.dumps({k: manifest[k] for k in ("output_root", "captured_count", "skipped_count", "page_type_counts")}, ensure_ascii=False, indent=2))
    return 0 if manifest["captured_count"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
