"""Fail if a public page links to ProdClub outside the credited entry point."""

from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
allowed = "https://prodclub.xyz/r/W3EF6W?src=GPTsub"
url_pattern = re.compile(r"(?:https?:)?//(?:www\.)?prodclub\.xyz[^\s\"'<>)]*", re.I)
public_files = [root / "README.md", *sorted((root / "docs").glob("*.html"))]
public_files += sorted((root / "docs" / "assets").glob("*.js"))
violations = []

for path in public_files:
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        for url in url_pattern.findall(line):
            if url.rstrip("。，；、") != allowed:
                violations.append(f"{path.relative_to(root)}:{number}: {url}")

if violations:
    print("Non-referral ProdClub URLs are forbidden in public content:")
    print("\n".join(violations))
    sys.exit(1)

print(f"ProdClub link check passed ({len(public_files)} public files).")
