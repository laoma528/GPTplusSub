"""Notify IndexNow about published ProdClub URLs that actually changed.

Deploy the public verification file first. Pass only changed canonical URLs,
or use --sitemap for the initial site submission. An HTTP 200 or 202 response
acknowledges receipt; it does not prove crawling or indexing.

Protocol: https://www.indexnow.org/documentation
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[2]
SITE_BASE = 'https://prodclub.vip/'
HOST = 'prodclub.vip'
KEY_FILE = ROOT / 'docs' / '70cc308f06195be856cf5971bf54d45b.txt'
KEY_URL = SITE_BASE + KEY_FILE.name
ENDPOINT = 'https://api.indexnow.org/indexnow'
SITEMAP = ROOT / 'docs' / 'sitemap.xml'
SITEMAP_NS = {'s': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
USER_AGENT = 'ProdClub-IndexNow/1.0'
CLEAN_PATH = re.compile(r'/(?:[a-z0-9]+(?:-[a-z0-9]+)*(?:/[a-z0-9]+(?:-[a-z0-9]+)*)*)?')


def validate_url_shape(raw: str) -> str:
    parsed = urlsplit(raw)
    if (
        any(ord(char) <= 32 or ord(char) == 127 for char in raw)
        or parsed.scheme != 'https' or parsed.netloc != HOST
        or parsed.query or parsed.fragment or not CLEAN_PATH.fullmatch(parsed.path)
        or raw != SITE_BASE.rstrip('/') + parsed.path
    ):
        raise ValueError(f'Not a canonical ProdClub URL: {raw}')
    return raw


def sitemap_pages() -> dict[str, Path]:
    tree = ET.parse(SITEMAP)
    if tree.getroot().tag != '{' + SITEMAP_NS['s'] + '}urlset':
        raise ValueError('Expected a standard URL sitemap')
    pages = {}
    for entry in tree.getroot():
        locations = entry.findall('s:loc', SITEMAP_NS)
        if len(locations) != 1 or not locations[0].text:
            raise ValueError('Each sitemap entry must contain one URL')
        url = validate_url_shape(locations[0].text.strip())
        path = urlsplit(url).path
        relative = 'index.html' if path == '/' else path.lstrip('/') + '.html'
        local = (ROOT / 'docs' / relative).resolve()
        if not local.is_relative_to((ROOT / 'docs').resolve()) or not local.is_file():
            raise ValueError(f'No matching local HTML file for {url}')
        if url in pages:
            raise ValueError('Duplicate sitemap URL')
        pages[url] = local
    if not pages or len(pages) > 10_000:
        raise ValueError('The sitemap must contain 1 to 10,000 canonical pages')
    return pages


def canonical_url(raw: str, pages: dict[str, Path] | None = None) -> str:
    url = validate_url_shape(raw)
    if url not in (sitemap_pages() if pages is None else pages):
        raise ValueError(f'URL is not in the published sitemap: {raw}')
    return url


def read_key() -> str:
    # This is a public ownership-verification key, not an account credential.
    key = KEY_FILE.read_text(encoding='utf-8').strip()
    if not re.fullmatch(r'[0-9a-f]{32}', key) or KEY_FILE.stem != key:
        raise ValueError('IndexNow verification file name/content mismatch')
    return key


def get_text(url: str) -> tuple[int, str]:
    with urlopen(Request(url, headers={'User-Agent': USER_AGENT}), timeout=20) as response:
        if response.geturl() != url:
            raise ValueError(f'Published URL redirects instead of serving directly: {url}')
        return response.status, response.read(1024).decode('utf-8', errors='replace').strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('urls', nargs='*', help='New or changed canonical URLs from sitemap.xml')
    parser.add_argument('--sitemap', action='store_true', help='Submit every sitemap URL for initial setup')
    parser.add_argument('--dry-run', action='store_true', help='Validate local inputs without network requests')
    args = parser.parse_args()

    if args.sitemap == bool(args.urls):
        parser.error('Provide canonical URLs or --sitemap, but not both')
    urls = []
    try:
        key = read_key()
        pages = sitemap_pages()
        urls = list(pages) if args.sitemap else list(dict.fromkeys(canonical_url(raw, pages) for raw in args.urls))
        if args.dry_run:
            print(json.dumps({'mode': 'dry-run', 'host': HOST, 'keyLocation': KEY_URL, 'urlList': urls}, ensure_ascii=False))
            return 0

        key_status, published_key = get_text(KEY_URL)
        if key_status != 200 or published_key != key:
            raise ValueError('Public IndexNow verification file is not deployed or does not match')
        for url in urls:
            status, _ = get_text(url)
            if status != 200:
                raise ValueError(f'Published page is not HTTP 200: {url} ({status})')

        payload = {'host': HOST, 'key': key, 'keyLocation': KEY_URL, 'urlList': urls}
        request = Request(ENDPOINT, data=json.dumps(payload, separators=(',', ':')).encode('utf-8'),
                          headers={'Content-Type': 'application/json; charset=utf-8', 'User-Agent': USER_AGENT},
                          method='POST')
        with urlopen(request, timeout=30) as response:
            status = response.status
            detail = response.read(512).decode('utf-8', errors='replace')
    except HTTPError as error:
        detail = error.read(512).decode('utf-8', errors='replace')
        print(json.dumps({'http_status': error.code, 'detail': detail, 'urlList': urls}, ensure_ascii=False))
        return 1
    except (URLError, OSError, ValueError, ET.ParseError) as error:
        print(json.dumps({'error': str(error), 'urlList': urls}, ensure_ascii=False))
        return 1

    meaning = 'received; key validation pending; crawl/index not guaranteed' if status == 202 else 'received; crawl/index not guaranteed'
    print(json.dumps({'http_status': status, 'detail': detail, 'urlList': urls,
                      'meaning': meaning if status in (200, 202) else 'not accepted'}, ensure_ascii=False))
    return 0 if status in (200, 202) else 1


if __name__ == '__main__':
    raise SystemExit(main())
