"""Check ProdClub destinations and service-click placement markers."""

from html.parser import HTMLParser
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
allowed = "https://prodclub.xyz/r/W3EF6W?src=gptsub"
# This download article needs the exact download endpoints and source citation.
download_article_urls = {
    "https://prodclub.xyz/download/codex",
    "https://prodclub.xyz/api/v1/downloads/codex-windows",
    "https://prodclub.xyz/api/v1/downloads/codex-windows?arch=arm64",
}
url_pattern = re.compile(r"(?:https?:)?//(?:www\.)?prodclub\.xyz[^\s\"'<>)]*", re.I)
public_files = [root / "README.md", *sorted((root / "docs").glob("*.html"))]
public_files += sorted((root / "docs" / "assets").glob("*.js"))
violations = []


class ServiceLinkParser(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.path = path

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attrs = dict(attrs)
        if attrs.get("href") != allowed:
            return
        if not (attrs.get("data-service-placement") or "").strip():
            line, _ = self.getpos()
            violations.append(
                f"{self.path.relative_to(root)}:{line}: "
                "service link is missing a non-empty data-service-placement"
            )


for path in public_files:
    content = path.read_text(encoding="utf-8")
    if path.parent == root / "docs" and path.suffix == ".html":
        ServiceLinkParser(path).feed(content)
    for number, line in enumerate(content.splitlines(), 1):
        for url in url_pattern.findall(line):
            if path == root / "docs" / "codex-windows.html" and url in download_article_urls:
                continue
            if url.rstrip("。，；、") != allowed:
                violations.append(f"{path.relative_to(root)}:{number}: {url}")

if violations:
    print("ProdClub destination or service-click tracking checks failed:")
    print("\n".join(violations))
    sys.exit(1)

print(f"ProdClub link check passed ({len(public_files)} public files).")
