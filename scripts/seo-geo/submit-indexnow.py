"""Notify IndexNow about published GPTplusSub Pages URLs that actually changed.

Run after GitHub Pages deployment, passing only new, changed, or removed URLs.
This script validates the project's URL prefix and public key file before POST.
An accepted submission does not mean the URL was crawled or indexed.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
SITE_BASE = 'https://laoma528.github.io/GPTplusSub/'
KEY_FILE = ROOT / 'docs' / '1e153e193846b19494b7348d3d587d4e.txt'
KEY_URL = SITE_BASE + KEY_FILE.name
ENDPOINT = 'https://api.indexnow.org/indexnow'


def canonical_url(raw: str) -> str:
    parsed = urlparse(raw)
    if parsed.scheme != 'https' or parsed.netloc != 'laoma528.github.io':
        raise ValueError(f'URL is outside the Pages host: {raw}')
    if not parsed.path.startswith('/GPTplusSub/') or parsed.query or parsed.fragment:
        raise ValueError(f'URL is outside the canonical project prefix: {raw}')
    if not (raw == SITE_BASE or parsed.path.endswith('.html')):
        raise ValueError(f'Expected a canonical HTML page URL: {raw}')
    return raw


def read_key() -> str:
    key = KEY_FILE.read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'[0-9a-f]{32}', key) or KEY_FILE.stem != key:
        raise ValueError('IndexNow key file name/content mismatch')
    return key


def get_text(url: str) -> tuple[int, str]:
    with urlopen(Request(url, headers={'User-Agent': 'GPTplusSub-IndexNow/1.0'}), timeout=20) as response:
        return response.status, response.read(1024).decode('utf-8', errors='replace').strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('urls', nargs='+', help='Canonical published Pages URLs changed in this release')
    parser.add_argument('--dry-run', action='store_true', help='Validate local arguments only')
    args = parser.parse_args()

    key = read_key()
    urls = list(dict.fromkeys(canonical_url(raw) for raw in args.urls))
    for url in urls:
        relative = url[len(SITE_BASE):]
        local = ROOT / 'docs' / (relative or 'index.html')
        if not local.is_file():
            raise ValueError(f'No matching local page: {local}')

    payload = {'host': 'laoma528.github.io', 'key': key, 'keyLocation': KEY_URL, 'urlList': urls}
    if args.dry_run:
        print(json.dumps({'mode': 'dry-run', 'keyLocation': KEY_URL, 'urlList': urls}, ensure_ascii=False))
        return 0

    key_status, published_key = get_text(KEY_URL)
    if key_status != 200 or published_key != key:
        raise RuntimeError('Public IndexNow key file is not deployed or does not match')
    for url in urls:
        status, _ = get_text(url)
        if status != 200:
            raise RuntimeError(f'Published page is not HTTP 200: {url} ({status})')

    body = json.dumps(payload, separators=(',', ':')).encode('utf-8')
    request = Request(ENDPOINT, data=body, headers={'Content-Type': 'application/json; charset=utf-8'}, method='POST')
    try:
        with urlopen(request, timeout=30) as response:
            status = response.status
            detail = response.read(512).decode('utf-8', errors='replace')
    except HTTPError as error:
        detail = error.read(512).decode('utf-8', errors='replace')
        print(json.dumps({'http_status': error.code, 'detail': detail, 'urlList': urls}, ensure_ascii=False))
        return 1
    except URLError as error:
        print(json.dumps({'error': str(error.reason), 'urlList': urls}, ensure_ascii=False))
        return 1

    print(json.dumps({'http_status': status, 'detail': detail, 'urlList': urls, 'meaning': 'received; crawl/index not guaranteed'}, ensure_ascii=False))
    return 0 if status in (200, 202) else 1


if __name__ == '__main__':
    raise SystemExit(main())
