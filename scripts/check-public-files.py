"""Validate the exact public file set and scan staged or committed content.

The manifest is read from the snapshot being checked, never the working copy.
Git hooks and CI can use the same checks without printing credential values.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
import json
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ".public-files"
ZERO = re.compile(r"^0{40}(?:0{24})?$")
OBJECT_ID = re.compile(r"^[0-9a-fA-F]{40}(?:[0-9a-fA-F]{24})?$")
PUBLIC_ROOT_FILES = {
    ".gitattributes", ".gitignore", MANIFEST, "README.md", "CONTRIBUTING.md",
    ".githooks/pre-commit", ".githooks/pre-push",
    ".github/workflows/public-content-check.yml",
    "scripts/check-public-files.py", "scripts/check-referral-links.py",
    "scripts/seo-geo/submit-indexnow.py",
}
REQUIRED_PUBLIC_FILES = {
    MANIFEST, ".gitignore", ".gitattributes", "README.md", "docs/index.html",
    ".githooks/pre-commit", ".githooks/pre-push",
    ".github/workflows/public-content-check.yml",
    "scripts/check-public-files.py", "scripts/check-referral-links.py",
}
PRIVATE_NAMES = {
    "agents.md", "claude.md", "design-openai.md", "站点入口.md",
    "credentials", "credentials.json", "credentials.yml", "credentials.yaml",
    "cookies", "cookies.json", "cookies.txt", "storage-state.json",
    "storage_state.json", "localstorage.json", "sessionstorage.json",
}
PRIVATE_PARTS = {
    "planning", "research", ".git", ".ssh", ".aws", ".codex", ".agents",
    ".ego-browser", ".venv", "venv", "node_modules", "__pycache__",
    "playwright-report", "test-results", "browser-profile", "browser-profiles",
}
PRIVATE_SUFFIXES = {
    ".pem", ".key", ".p12", ".pfx", ".jks", ".keystore", ".sqlite",
    ".sqlite3", ".db", ".har", ".log", ".tmp", ".temp", ".bak",
    ".zip", ".7z", ".rar", ".session", ".cookie", ".cookies",
}
BINARY_SUFFIXES = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".avif", ".ico",
    ".woff", ".woff2", ".ttf", ".otf", ".pdf",
}
PRIVATE_BASENAME = re.compile(
    r"(?:^|[._-])(?:private|internal|secret|secrets|credential|credentials|"
    r"cookies?|passwords?|browser|profile|backup)(?:[._-]|$)", re.I
)


class CheckError(Exception):
    """A controlled diagnostic that cannot expose Git output or secret values."""


@dataclass(frozen=True)
class Entry:
    mode: str
    kind: str
    oid: str


def git(*arguments: str) -> bytes:
    result = subprocess.run(
        ["git", "-c", f"safe.directory={ROOT.as_posix()}", *arguments],
        cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    )
    if result.returncode:
        raise CheckError("Git snapshot could not be read; no content was printed.")
    return result.stdout


def read_blob(oid: str) -> bytes:
    if not OBJECT_ID.fullmatch(oid):
        raise CheckError("Invalid Git object identifier.")
    return git("cat-file", "blob", oid)


def staged_entries() -> dict[str, Entry]:
    entries = {}
    for record in git("ls-files", "--stage", "-z").split(b"\0"):
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, oid, stage = metadata.decode("ascii").split()
        if stage != "0":
            raise CheckError("Resolve staged merge conflicts before publication.")
        path = raw_path.decode("utf-8", "surrogateescape")
        entries[path] = Entry(mode, "commit" if mode == "160000" else "blob", oid)
    return entries


def revision_entries(revision: str) -> dict[str, Entry]:
    resolved = git("rev-parse", "--verify", "--end-of-options", revision + "^{commit}").strip()
    if not OBJECT_ID.fullmatch(resolved.decode("ascii")):
        raise CheckError("Revision does not resolve to a commit.")
    entries = {}
    for record in git("ls-tree", "-r", "-z", "--full-tree", resolved.decode("ascii")).split(b"\0"):
        if not record:
            continue
        metadata, raw_path = record.split(b"\t", 1)
        mode, kind, oid = metadata.decode("ascii").split()
        entries[raw_path.decode("utf-8", "surrogateescape")] = Entry(mode, kind, oid)
    return entries


def prohibited_path(path: str) -> bool:
    parts = PurePosixPath(path).parts
    if (
        not parts or path.startswith("/") or "\\" in path
        or any(p in {".", ".."} for p in parts)
        or PurePosixPath(path).as_posix() != path
        or any(c in path for c in "*?[]{}:")
    ):
        return True
    if any(ord(c) < 32 or ord(c) == 127 for c in path):
        return True
    lower = [part.casefold() for part in parts]
    if any(part in PRIVATE_PARTS for part in lower):
        return True
    name = lower[-1]
    if name in PRIVATE_NAMES or name == ".env" or name.startswith((".env.", ".codex-", ".ego-")):
        return True
    if PurePosixPath(name).suffix in PRIVATE_SUFFIXES or PRIVATE_BASENAME.search(name):
        return True
    return False


def eligible_public_path(path: str) -> bool:
    return path in PUBLIC_ROOT_FILES or path.startswith("docs/")


def placeholder(value: str) -> bool:
    lower = value.casefold()
    return (
        lower.startswith(("your_", "your-", "example_", "example-", "placeholder", "<", "${", "{{"))
        or lower in {"password", "username", "changeme", "redacted", "example", "token", "secret"}
        or bool(re.fullmatch(r"[xX*._-]+", value))
    )


TOKEN_PATTERNS = [
    ("private key", re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----|PuTTY-User-Key-File-\d+:")),
    ("OpenAI credential", re.compile(r"(?<![\w-])sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{20,}(?![\w-])")),
    ("GitHub credential", re.compile(r"\b(?:gh[pousr]_[A-Za-z0-9]{20,255}|github_pat_[A-Za-z0-9_]{30,255})\b")),
    ("JWT credential", re.compile(r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b")),
    ("Google OAuth credential", re.compile(r"\b(?:ya29\.[A-Za-z0-9_-]{20,}|GOCSPX-[A-Za-z0-9_-]{16,})|(?<!\w)1//[A-Za-z0-9_-]{25,}")),
    ("AWS access credential", re.compile(r"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("Slack credential", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{20,}\b")),
]
ASSIGNMENT = re.compile(
    r"(?ix)(?<![\w-])(?:[\"'])?"
    r"(?:access[_-]?token|refresh[_-]?token|api[_-]?key|openai[_-]?api[_-]?key|"
    r"github[_-]?token|aws[_-]?secret[_-]?access[_-]?key|client[_-]?secret|password|passwd|pwd|session[_-]?token|"
    r"sessionid|cf_clearance|__secure-[\w.-]*session-token)"
    r"(?:[\"'])?\s*[:=]\s*(?:[\"'])?"
    r"(?P<value>[A-Za-z0-9_./+=:~!-]{16,})"
)
URL_CREDENTIAL = re.compile(
    r"https?://(?P<user>[^\s/<>\"':@]+):(?P<value>[^\s/<>\"'@]+)@", re.I
)
AUTHORIZATION = re.compile(
    r"(?i)\bauthorization[\"']?\s*[:=]\s*[\"']?(?:Bearer|Basic)\s+(?P<value>[A-Za-z0-9._~+/-]{20,})"
)


def credential_findings(text: str) -> set[tuple[int, str]]:
    findings = set()
    for category, pattern in TOKEN_PATTERNS:
        for match in pattern.finditer(text):
            findings.add((text.count("\n", 0, match.start()) + 1, category))
    for category, pattern in [
        ("credential assignment", ASSIGNMENT),
        ("credentials in URL", URL_CREDENTIAL),
        ("authorization credential", AUTHORIZATION),
    ]:
        for match in pattern.finditer(text):
            if not placeholder(match.group("value")):
                findings.add((text.count("\n", 0, match.start()) + 1, category))
    return findings


class Checker:
    def __init__(self):
        self.violations: set[tuple[str, int, str]] = set()
        self.blobs: dict[str, bytes] = {}
        self.scanned: set[tuple[str, str]] = set()
        self.snapshots = 0

    def blob(self, oid: str) -> bytes:
        if oid not in self.blobs:
            self.blobs[oid] = read_blob(oid)
        return self.blobs[oid]

    def fail(self, path: str, category: str, line: int = 1):
        self.violations.add((path, line, category))

    def check(self, entries: dict[str, Entry]):
        self.snapshots += 1
        manifest_entry = entries.get(MANIFEST)
        allowed: set[str] = set()
        if not manifest_entry or manifest_entry.kind != "blob" or manifest_entry.mode not in {"100644", "100755"}:
            self.fail(MANIFEST, "public manifest missing or not a regular file")
        else:
            try:
                manifest = self.blob(manifest_entry.oid).decode("utf-8-sig")
            except UnicodeDecodeError:
                self.fail(MANIFEST, "public manifest must be UTF-8")
                manifest = ""
            for line_number, raw in enumerate(manifest.splitlines(), 1):
                path = raw.strip()
                if not path or path.startswith("#"):
                    continue
                if path != raw:
                    self.fail(MANIFEST, "public path must not have surrounding whitespace", line_number)
                if prohibited_path(path) or not eligible_public_path(path):
                    self.fail(MANIFEST, "manifest includes a prohibited path", line_number)
                if path in allowed:
                    self.fail(MANIFEST, "duplicate public path", line_number)
                allowed.add(path)
                if path not in entries:
                    self.fail(MANIFEST, "manifest entry missing from snapshot", line_number)
        for path in REQUIRED_PUBLIC_FILES:
            if path not in entries or path not in allowed:
                self.fail(path, "required public protection or entry file is missing")
        for path in (".githooks/pre-commit", ".githooks/pre-push"):
            if path in entries and entries[path].mode != "100755":
                self.fail(path, "Git hook must retain executable mode")
        for path, entry in entries.items():
            if prohibited_path(path):
                self.fail(path, "internal or credential path is prohibited")
            if not eligible_public_path(path) or path not in allowed:
                self.fail(path, "path is not approved for publication")
            if entry.kind != "blob" or entry.mode not in {"100644", "100755"}:
                self.fail(path, "symlinks, submodules and non-regular files are prohibited")
                continue
            cache_key = (path, entry.oid)
            if cache_key in self.scanned:
                continue
            self.scanned.add(cache_key)
            content = self.blob(entry.oid)
            if PurePosixPath(path).suffix.casefold() in BINARY_SUFFIXES:
                text = content.decode("utf-8", "replace")
            else:
                if b"\0" in content:
                    self.fail(path, "public text must not contain NUL bytes")
                try:
                    text = content.decode("utf-8-sig")
                except UnicodeDecodeError:
                    self.fail(path, "public text must use UTF-8 encoding")
                    continue
            for line, category in credential_findings(text):
                self.fail(path, category, line)

    def result(self) -> int:
        if self.violations:
            print("Public-content check failed (credential values are never printed):")
            for path, line, category in sorted(self.violations):
                print(f"{json.dumps(path, ensure_ascii=False)}:{line}: {category}")
            return 1
        print(f"Public-content check passed ({self.snapshots} snapshot(s)).")
        return 0


def incoming_commits(local_sha: str, remote_sha: str, remote_ref: str, remote: str) -> list[str]:
    arguments = ["rev-list", local_sha]
    if not ZERO.fullmatch(remote_sha):
        # An explicit base is authoritative, including in CI after refs update.
        git("cat-file", "-e", remote_sha + "^{commit}")
        arguments.append("^" + remote_sha)
    else:
        if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]*", remote):
            raise CheckError("Use a configured remote name for a new branch check.")
        tracking = "refs/remotes/" + remote + "/"
        incoming_tracking = (
            tracking + remote_ref.removeprefix("refs/heads/")
            if remote_ref.startswith("refs/heads/") else ""
        )
        for ref in git("for-each-ref", "--format=%(refname)", tracking).decode("utf-8").splitlines():
            # CI may already have fetched this newly published branch. Its own
            # tip must not hide intermediate commits from the check.
            if ref != incoming_tracking:
                arguments.append("^" + ref)
    return git(*arguments).decode("ascii").splitlines()


def pre_push(checker: Checker, remote: str):
    checked = set()
    for raw in sys.stdin:
        fields = raw.split()
        if not fields:
            continue
        if len(fields) != 4:
            raise CheckError("Invalid pre-push input.")
        _local_ref, local_sha, remote_ref, remote_sha = fields
        if not OBJECT_ID.fullmatch(local_sha) or not OBJECT_ID.fullmatch(remote_sha):
            raise CheckError("Invalid pre-push object identifier.")
        if ZERO.fullmatch(local_sha):
            continue  # Deleting a remote reference publishes no new content.
        revisions = [local_sha, *incoming_commits(local_sha, remote_sha, remote_ref, remote)]
        for revision in revisions:
            if revision not in checked:
                checker.check(revision_entries(revision))
                checked.add(revision)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--staged", action="store_true", help="Check the complete Git index")
    modes.add_argument("--revision", metavar="REV", help="Check one committed snapshot")
    modes.add_argument("--pre-push", action="store_true", help="Read Git pre-push records from stdin")
    parser.add_argument("--remote", default="origin", help="Remote name used for new-reference baselines")
    args = parser.parse_args()
    checker = Checker()
    try:
        if args.staged:
            checker.check(staged_entries())
        elif args.revision:
            checker.check(revision_entries(args.revision))
        else:
            pre_push(checker, args.remote)
        return checker.result()
    except (CheckError, OSError, ValueError) as error:
        # Never forward subprocess output or credential-containing source lines.
        print("Public-content check could not complete: " + (str(error) if isinstance(error, CheckError) else "local input or environment error."))
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
