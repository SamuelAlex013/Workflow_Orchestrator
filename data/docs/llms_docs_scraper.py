from __future__ import annotations

import argparse
import re
import sys
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


THIS_DIR = Path(__file__).resolve().parent
DEFAULT_LLMS_URL = "https://docs.zapier.com/llms.txt"
DEFAULT_OUTPUT = THIS_DIR / "zapier_official_docs.md"
DEFAULT_LLMS_SNAPSHOT = THIS_DIR / "zapier_llms.txt"


LINK_RE = re.compile(r"\[[^\]]+\]\((https?://[^)]+)\)")
HEADING_RE = re.compile(r"^#{1,6}\s+.+$", re.MULTILINE)
FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)


@dataclass
class ScrapeStats:
    total_links_seen: int = 0
    links_after_filter: int = 0
    pages_fetched: int = 0
    pages_failed: int = 0
    pages_skipped: int = 0


def build_session() -> requests.Session:
    retry = Retry(
        total=4,
        connect=4,
        read=4,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=("GET",),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry)

    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update(
        {
            "User-Agent": "Workflow-Orchestrator-Docs-Scraper/1.0",
            "Accept": "text/plain, text/markdown, */*",
        }
    )
    return session


def fetch_text(session: requests.Session, url: str, timeout: int) -> str:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.text


def parse_links(llms_text: str, base_url: str) -> list[str]:
    links: list[str] = []

    for match in LINK_RE.finditer(llms_text):
        raw = match.group(1).strip()
        normalized = urljoin(base_url, raw)
        normalized = urldefrag(normalized).url
        links.append(normalized)

    # Fallback: include plain URLs if present (some llms.txt files are inconsistent)
    for raw_url in re.findall(r"https?://[^\s)]+", llms_text):
        normalized = urldefrag(raw_url.strip()).url
        if normalized not in links:
            links.append(normalized)

    # Preserve order while de-duplicating
    deduped = list(dict.fromkeys(links))
    return deduped


def is_probably_docs_markdown_url(url: str, *, allow_non_markdown: bool) -> bool:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return False

    if parsed.netloc != "docs.zapier.com":
        return False

    path = parsed.path.lower()
    if allow_non_markdown:
        return True

    return path.endswith(".md") or path.endswith("/")


def clean_page_markdown(text: str) -> str:
    cleaned = text.replace("\r\n", "\n").replace("\r", "\n").lstrip("\ufeff")
    cleaned = FRONTMATTER_RE.sub("", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned).strip()
    return cleaned


def ensure_has_heading(content: str, fallback_title: str, source_url: str) -> str:
    if HEADING_RE.search(content):
        return content

    safe_title = fallback_title.strip() or source_url
    return f"# {safe_title}\n\n{content}".strip()


def extract_title_from_url(url: str) -> str:
    path = urlparse(url).path.rstrip("/")
    name = path.split("/")[-1] if path else "document"
    name = re.sub(r"\.md$", "", name, flags=re.IGNORECASE)
    name = name.replace("-", " ").replace("_", " ").strip()
    return name.title() if name else "Document"


def build_output_document(llms_url: str, llms_text: str, pages: Iterable[str]) -> str:
    # Keep header simple, matching the style of the n8n doc file.
    title = "Zapier Docs"
    first_h1 = re.search(r"^#\s+(.+)$", llms_text, flags=re.MULTILINE)
    if first_h1:
        title = f"{first_h1.group(1).strip()} Docs"

    header = (
        f"# {title}\n\n"
        f"> Consolidated documentation scraped from {llms_url}.\n"
    )

    body = "\n\n".join(pages).strip()
    return f"{header}\n\n{body}\n"


def scrape_llms_docs(
    llms_url: str,
    output_path: Path,
    llms_snapshot_path: Path | None,
    *,
    timeout: int,
    delay_seconds: float,
    max_links: int | None,
    allow_non_markdown: bool,
) -> ScrapeStats:
    stats = ScrapeStats()
    session = build_session()

    print(f"📥 Downloading llms.txt from: {llms_url}")
    llms_text = fetch_text(session, llms_url, timeout)

    if llms_snapshot_path is not None:
        llms_snapshot_path.parent.mkdir(parents=True, exist_ok=True)
        llms_snapshot_path.write_text(llms_text, encoding="utf-8")
        print(f"💾 Saved llms.txt snapshot: {llms_snapshot_path}")

    links = parse_links(llms_text, llms_url)
    stats.total_links_seen = len(links)

    filtered_links = [
        link
        for link in links
        if is_probably_docs_markdown_url(link, allow_non_markdown=allow_non_markdown)
    ]

    if max_links is not None:
        filtered_links = filtered_links[:max_links]

    stats.links_after_filter = len(filtered_links)
    print(f"🔗 Links discovered: {stats.total_links_seen}")
    print(f"✅ Links selected: {stats.links_after_filter}")

    pages: list[str] = []
    for idx, link in enumerate(filtered_links, start=1):
        print(f"[{idx}/{len(filtered_links)}] Fetching {link}")
        try:
            raw_text = fetch_text(session, link, timeout)
            cleaned = clean_page_markdown(raw_text)

            if not cleaned:
                stats.pages_skipped += 1
                print("   ↳ Skipped (empty content)")
            else:
                fallback_title = extract_title_from_url(link)
                page_text = ensure_has_heading(cleaned, fallback_title, link)
                pages.append(page_text)
                stats.pages_fetched += 1
        except Exception as exc:
            stats.pages_failed += 1
            print(f"   ↳ Failed: {exc}")

        if delay_seconds > 0:
            time.sleep(delay_seconds)

    if not pages:
        raise RuntimeError("No pages were fetched. Check URL filters or network access.")

    final_markdown = build_output_document(llms_url, llms_text, pages)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(final_markdown, encoding="utf-8")

    print(f"\n📄 Output saved: {output_path}")
    print(f"✅ Pages fetched: {stats.pages_fetched}")
    print(f"⚠️  Pages failed: {stats.pages_failed}")
    print(f"⏭️  Pages skipped: {stats.pages_skipped}")

    return stats


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Scrape docs listed in an llms.txt file and save a single consolidated markdown file."
        )
    )
    parser.add_argument(
        "--llms-url",
        default=DEFAULT_LLMS_URL,
        help="URL to llms.txt (default: Zapier docs llms.txt)",
    )
    parser.add_argument(
        "--output",
        default=str(DEFAULT_OUTPUT),
        help="Output markdown file path",
    )
    parser.add_argument(
        "--save-llms-snapshot",
        default=str(DEFAULT_LLMS_SNAPSHOT),
        help="Path to save raw llms.txt (use empty string to disable)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=30,
        help="Request timeout in seconds",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=0.1,
        help="Delay between page requests in seconds",
    )
    parser.add_argument(
        "--max-links",
        type=int,
        default=None,
        help="Optional cap for number of links (useful for testing)",
    )
    parser.add_argument(
        "--allow-non-markdown",
        action="store_true",
        help="Also fetch non-.md docs.zapier.com links",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    snapshot = Path(args.save_llms_snapshot) if args.save_llms_snapshot else None

    try:
        scrape_llms_docs(
            llms_url=args.llms_url,
            output_path=Path(args.output),
            llms_snapshot_path=snapshot,
            timeout=args.timeout,
            delay_seconds=args.delay,
            max_links=args.max_links,
            allow_non_markdown=args.allow_non_markdown,
        )
        return 0
    except Exception as exc:
        print(f"\n❌ Scrape failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
