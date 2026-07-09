#!/usr/bin/env python3
"""Run a local multi-page smoke test for reference_site_capture.py."""

from __future__ import annotations

import contextlib
import functools
import json
import shutil
import tempfile
import threading
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace

from reference_site_capture import capture


PAGES = {
    "index.html": ("Reference Home", ["shop.html", "category/disposable-vapes.html", "product/starter-kit.html", "blog.html", "blog/how-to-choose.html", "shipping-policy.html", "returns-policy.html", "privacy-policy.html", "terms.html", "about.html", "contact.html", "faq.html", "cart.html", "checkout.html", "account.html", "services.html", "pricing.html", "case-study/brand-rebuild.html", "docs/getting-started.html"]),
    "shop.html": ("Shop Catalog", ["product/starter-kit.html", "category/disposable-vapes.html"]),
    "category/disposable-vapes.html": ("Disposable Vapes Category", ["product/starter-kit.html"]),
    "product/starter-kit.html": ("Example Product Detail", ["cart.html"]),
    "blog.html": ("Blog Index", ["blog/how-to-choose.html"]),
    "blog/how-to-choose.html": ("How To Choose Article", ["shop.html"]),
    "shipping-policy.html": ("Shipping Policy", []),
    "returns-policy.html": ("Returns Policy", []),
    "privacy-policy.html": ("Privacy Policy", []),
    "terms.html": ("Terms and Conditions", []),
    "about.html": ("About Our Company", []),
    "contact.html": ("Contact Support", []),
    "faq.html": ("FAQ", []),
    "cart.html": ("Cart", ["checkout.html"]),
    "checkout.html": ("Checkout", []),
    "account.html": ("Customer Account", []),
    "services.html": ("Services", []),
    "pricing.html": ("Pricing Plans", []),
    "case-study/brand-rebuild.html": ("Case Study Brand Rebuild", []),
    "docs/getting-started.html": ("Documentation Getting Started", []),
}

EXPECTED_TYPES = {
    "home",
    "shop_or_catalog",
    "category_or_listing",
    "product",
    "blog_index_or_archive",
    "single_post_or_article",
    "policy",
    "about",
    "contact",
    "faq",
    "cart",
    "checkout",
    "account",
    "service",
    "pricing",
    "case_study",
    "documentation",
}


def write_fixture(root: Path) -> None:
    for relative, (title, links) in PAGES.items():
        path = root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        link_html = "\n".join(f'<a href="/{href}">{href}</a>' for href in links)
        path.write_text(
            f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <meta name="description" content="{title} description">
</head>
<body>
  <header><nav><a href="/">Home</a><a href="/shop.html">Shop</a><a href="/blog.html">Blog</a></nav></header>
  <main>
    <h1>{title}</h1>
    <h2>Primary Section</h2>
    <p>Fixture page for reference capture testing.</p>
    {link_html}
  </main>
  <footer><a href="/privacy-policy.html">Privacy</a><a href="/terms.html">Terms</a></footer>
</body>
</html>
""",
            encoding="utf-8",
        )


def main() -> int:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp) / "site"
        output = Path(tmp) / "captures"
        write_fixture(root)

        handler = functools.partial(SimpleHTTPRequestHandler, directory=str(root))
        server = ThreadingHTTPServer(("127.0.0.1", 0), handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        try:
            port = server.server_address[1]
            args = SimpleNamespace(
                url=f"http://127.0.0.1:{port}/",
                output=str(output),
                max_pages=40,
                max_candidates=200,
                timeout=5,
                delay=0,
                same_domain=True,
                ignore_robots=True,
            )
            manifest = capture(args)
        finally:
            server.shutdown()
            server.server_close()
            thread.join(timeout=5)

        found = set(manifest["page_type_counts"])
        missing = sorted(EXPECTED_TYPES - found)
        result = {
            "captured_count": manifest["captured_count"],
            "page_type_counts": manifest["page_type_counts"],
            "missing_expected_types": missing,
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        if missing:
            return 2
        if manifest["captured_count"] < len(PAGES):
            return 3
        shutil.rmtree(output, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
