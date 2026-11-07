"""Synchronize real editorial dates from Git, without refreshing unchanged pages.

Only README.md, pages already listed in docs/sitemap.xml and that sitemap can
be written. Commit editorial changes first; styles and generated date labels do
not advance a document's date. The script never stages or commits files.
"""

from __future__ import annotations

import argparse
from datetime import datetime, timedelta, timezone
from html import escape, unescape
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://prodclub.vip"
SHANGHAI = timezone(timedelta(hours=8))
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"
README_START = "<!-- content-updated:start -->"
README_END = "<!-- content-updated:end -->"
README_DATE = re.compile(
    r"(?m)^[ \t]*<!-- content-updated:start -->.*?<!-- content-updated:end -->[ \t]*(?:\r?\n)?",
    re.S,
)
HTML_DATE = re.compile(
    r"[ \t]*<p\b(?=[^>]*\bdata-content-updated(?:[\s=>]))[^>]*>.*?</p>[ \t]*(?:\r?\n)?",
    re.I | re.S,
)
BLOCKS = {
    "address", "article", "aside", "blockquote", "br", "caption", "dd", "details",
    "div", "dl", "dt", "figcaption", "figure", "h1", "h2", "h3", "h4", "h5",
    "h6", "hr", "li", "ol", "p", "pre", "section", "summary", "table", "td",
    "th", "tr", "ul",
}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
LINK_ATTRIBUTES = {
    "a": ("href",), "img": ("src", "alt", "srcset"),
    "source": ("src", "srcset", "type"), "video": ("src", "poster"),
    "audio": ("src",), "iframe": ("src", "title"),
}


class DateError(Exception):
    pass


def git(*args: str, optional: bool = False) -> str | None:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", *args], cwd=ROOT,
        stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        if optional:
            return None
        raise DateError("Git history could not be read. No date was generated.")
    try:
        return result.stdout.decode("utf-8-sig")
    except UnicodeDecodeError as error:
        raise DateError("Published text and its history must use UTF-8.") from error


def read_text(path: Path) -> str:
    try:
        return path.read_bytes().decode("utf-8-sig")
    except (OSError, UnicodeDecodeError) as error:
        raise DateError(f"Cannot read UTF-8 document: {path.relative_to(ROOT)}") from error


def strip_html_date(text: str) -> str:
    matches = list(HTML_DATE.finditer(text))
    if len(matches) > 1:
        raise DateError("A page contains more than one generated content date.")
    return HTML_DATE.sub("", text)


def strip_readme_date(text: str) -> str:
    if text.count(README_START) != text.count(README_END) or text.count(README_START) > 1:
        raise DateError("README content date markers are incomplete or duplicated.")
    return README_DATE.sub("", text)


class EditorialHTML(HTMLParser):
    """Read editorial text and destinations, ignoring site chrome and styling."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.main_depth = 0
        self.main_count = 0
        self.skip = 0
        self.in_title = False
        self.title: list[str] = []
        self.description = ""
        self.canonical = ""
        self.text: list[str] = []
        self.links: list[tuple[str, tuple[tuple[str, str], ...]]] = []

    def handle_starttag(self, tag, attrs):
        values = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta" and (values.get("name") or "").casefold() == "description":
            self.description = values.get("content") or ""
        if tag == "link" and (values.get("rel") or "").casefold() == "canonical":
            self.canonical = values.get("href") or ""
        if tag == "main":
            self.main_count += 1
            self.main_depth += 1
            return
        if not self.main_depth:
            return
        if self.skip:
            if tag not in VOID:
                self.skip += 1
            return
        if tag in {"script", "style", "template", "nav", "header", "footer"}:
            self.skip = 1
            return
        if tag in BLOCKS:
            self.text.append("\n")
        if tag in LINK_ATTRIBUTES:
            meaningful = tuple((name, values[name] or "") for name in LINK_ATTRIBUTES[tag] if name in values)
            self.links.append((tag, meaningful))

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if not self.main_depth:
            return
        if self.skip:
            if tag not in VOID:
                self.skip -= 1
            return
        if tag == "main":
            self.main_depth -= 1
        elif tag in BLOCKS:
            self.text.append("\n")

    def handle_data(self, data):
        if self.in_title:
            self.title.append(data)
        if self.main_depth and not self.skip:
            self.text.append(data)


def editorial_fingerprint(text: str, readme: bool = False) -> str:
    if readme:
        cleaned = strip_readme_date(text).replace("\r\n", "\n")
        return "\n".join(line.rstrip() for line in cleaned.strip().splitlines())
    document = EditorialHTML()
    document.feed(strip_html_date(text))
    if document.main_count != 1 or document.main_depth or not document.title:
        raise DateError("An article must contain one complete main region and a title.")
    return json.dumps([
        " ".join("".join(document.title).split()),
        " ".join(document.description.split()),
        " ".join("".join(document.text).split()), document.links,
    ], ensure_ascii=False, separators=(",", ":"))


def modification_time(relative: str, current: str) -> datetime:
    is_readme = relative == "README.md"
    head = git("show", f"HEAD:{relative}")
    if head is None:
        raise DateError(f"No committed content exists for {relative}.")
    fingerprint = editorial_fingerprint(head, is_readme)
    if editorial_fingerprint(current, is_readme) != fingerprint:
        raise DateError(f"Commit editorial changes before updating dates: {relative}")
    log = git("log", "--follow", "--format=%H%x09%cI", "HEAD", "--", relative)
    if not log:
        raise DateError(f"No committed history exists for {relative}.")
    selected: datetime | None = None
    for record in log.splitlines():
        commit, stamp = record.split("\t", 1)
        previous = git("show", f"{commit}:{relative}", optional=True)
        if previous is None:
            # The current pathname begins here, for example after a rename.
            break
        if editorial_fingerprint(previous, is_readme) != fingerprint:
            break
        try:
            candidate = datetime.fromisoformat(stamp)
        except ValueError as error:
            raise DateError(f"Invalid committed timestamp for {relative}.") from error
        if candidate.utcoffset() is None:
            raise DateError(f"Commit timestamp has no timezone for {relative}.")
        selected = candidate.astimezone(SHANGHAI)
    if selected is None:
        raise DateError(f"Cannot establish a real content date for {relative}.")
    if selected > datetime.now(timezone.utc) + timedelta(minutes=5):
        raise DateError(f"Content history has a future timestamp: {relative}")
    return selected


def format_date(stamp: datetime) -> tuple[str, str]:
    return stamp.isoformat(timespec="seconds"), f"{stamp.year}年{stamp.month}月{stamp.day}日"


def html_with_date(text: str, stamp: datetime) -> str:
    clean = strip_html_date(text)
    closings = list(re.finditer(r"</main\s*>", clean, re.I))
    if len(closings) != 1:
        raise DateError("Cannot locate a unique article ending.")
    newline = "\r\n" if "\r\n" in text else "\n"
    iso, visible = format_date(stamp)
    block = f'  <p class="content-updated" data-content-updated>内容更新：<time datetime="{iso}">{visible}</time></p>'
    split = closings[0].start()
    return clean[:split].rstrip("\r\n") + newline + block + newline + clean[split:]


def readme_with_date(text: str, stamp: datetime) -> str:
    clean = strip_readme_date(text)
    newline = "\r\n" if "\r\n" in text else "\n"
    _iso, visible = format_date(stamp)
    return clean.rstrip("\r\n") + newline * 2 + newline.join([
        README_START, f"内容更新：{visible}", README_END,
    ]) + newline


def sitemap_pages(text: str) -> list[tuple[str, str]]:
    try:
        root = ET.fromstring(text)
    except ET.ParseError as error:
        raise DateError("The sitemap is not valid XML.") from error
    if root.tag != f"{{{SITEMAP_NS}}}urlset":
        raise DateError("Expected a standard URL sitemap.")
    pages = []
    seen = set()
    for entry in root:
        locs = entry.findall(f"{{{SITEMAP_NS}}}loc")
        if len(locs) != 1 or not locs[0].text:
            raise DateError("Each sitemap entry needs one URL.")
        url = locs[0].text.strip()
        parsed = urlsplit(url)
        path = unquote(parsed.path)
        if (
            f"{parsed.scheme}://{parsed.netloc}" != SITE or parsed.query or parsed.fragment
            or not path.startswith("/") or "\\" in path or "//" in path
            or any(part in {".", ".."} for part in path.split("/"))
            or (path != "/" and (path.endswith("/") or Path(path).suffix not in {"", ".html"}))
        ):
            raise DateError("The sitemap contains an unsupported or non-canonical URL.")
        # Cloudflare Pages serves HTML at clean URLs while files stay on disk.
        article_path = path.lstrip("/") or "index.html"
        if not article_path.endswith(".html"):
            article_path += ".html"
        relative = "docs/" + article_path
        resolved = (ROOT / relative).resolve()
        if not resolved.is_relative_to((ROOT / "docs").resolve()) or not resolved.is_file():
            raise DateError("The sitemap points outside an existing local article.")
        if url in seen or relative in {item[1] for item in pages}:
            raise DateError("The sitemap contains duplicate articles.")
        seen.add(url)
        pages.append((url, relative))
    if not pages:
        raise DateError("The sitemap has no article URLs.")
    return pages


def sitemap_with_dates(text: str, dates: dict[str, datetime]) -> str:
    entries = list(re.finditer(r"<url\b[^>]*>.*?</url>", text, re.S))
    if len(entries) != len(dates):
        raise DateError("Unsupported sitemap formatting; no files were written.")
    def replace(match):
        block = match.group(0)
        loc = re.search(r"<loc\s*>(.*?)</loc>", block, re.S)
        if not loc or unescape(loc.group(1).strip()) not in dates:
            raise DateError("Cannot match a sitemap entry to its article.")
        iso, _visible = format_date(dates[unescape(loc.group(1).strip())])
        lastmod = f"<lastmod>{escape(iso)}</lastmod>"
        existing = list(re.finditer(r"<lastmod\b[^>]*>.*?</lastmod>", block, re.S))
        if len(existing) > 1:
            raise DateError("A sitemap entry has duplicate modification dates.")
        if existing:
            return block[:existing[0].start()] + lastmod + block[existing[0].end():]
        return block[:loc.end()] + lastmod + block[loc.end():]
    return re.sub(r"<url\b[^>]*>.*?</url>", replace, text, flags=re.S)


def prepare_updates() -> tuple[dict[Path, str], dict[str, str]]:
    if git("rev-parse", "--is-shallow-repository").strip() == "true":
        raise DateError("Fetch full Git history before deriving content dates.")
    sitemap_path = ROOT / "docs/sitemap.xml"
    sitemap = read_text(sitemap_path)
    pages = sitemap_pages(sitemap)
    updates: dict[Path, str] = {}
    dates: dict[str, datetime] = {}
    report = {}
    for url, relative in pages:
        path = ROOT / relative
        current = read_text(path)
        document = EditorialHTML()
        document.feed(strip_html_date(current))
        if document.canonical != url:
            raise DateError(f"Article canonical does not match sitemap: {relative}")
        stamp = modification_time(relative, current)
        candidate = html_with_date(current, stamp)
        if candidate != current:
            updates[path] = candidate
        dates[url] = stamp
        report[relative] = format_date(stamp)[0]
    readme_path = ROOT / "README.md"
    readme = read_text(readme_path)
    stamp = modification_time("README.md", readme)
    candidate = readme_with_date(readme, stamp)
    if candidate != readme:
        updates[readme_path] = candidate
    report["README.md"] = format_date(stamp)[0]
    candidate = sitemap_with_dates(sitemap, dates)
    if candidate != sitemap:
        updates[sitemap_path] = candidate
    return updates, report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true", help="Report drift without writing")
    mode.add_argument("--write", action="store_true", help="Synchronize generated labels and sitemap")
    parser.add_argument("--json", action="store_true", help="Print dates and changed paths as JSON")
    args = parser.parse_args()
    try:
        updates, dates = prepare_updates()
        if args.write:
            for path, content in updates.items():
                path.write_bytes(content.encode("utf-8"))
        changed = [path.relative_to(ROOT).as_posix() for path in updates]
        if args.json:
            print(json.dumps({"mode": "write" if args.write else "check", "changed": changed, "content_dates": dates}, ensure_ascii=True))
        else:
            print(f"Content date {'sync' if args.write else 'check'}: {len(dates)} documents, {len(updates)} file(s) {'updated' if args.write else 'need synchronization'}.")
        return 0 if args.write or not updates else 1
    except (DateError, OSError, ValueError) as error:
        print(f"Content dates not updated: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
