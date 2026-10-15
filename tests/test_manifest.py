"""Manifest integrity — every declared pi extension must exist in the package.

Pi resolves each pi.extensions entry with existsSync and *silently skips* it
when the file is missing (pi-coding-agent dist/core/extensions/loader.js,
resolveExtensionEntries). A stale path therefore disables an extension with no
error anywhere. That is exactly what shipped in 1.4.1: pi-subagents 0.78.0
stopped publishing index.ts, the manifest kept pointing at it, and the
subagent tool vanished while skills and prompts kept loading.

Run:  uv run --with pytest pytest -q tests/
"""

import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _pi_manifest():
    pkg = json.loads((REPO / "package.json").read_text())
    return pkg.get("pi", {})


def test_manifest_declares_extensions():
    """Guards the existence test below from passing vacuously on an empty list."""
    assert _pi_manifest().get("extensions"), "pi.extensions must not be empty"


def test_every_declared_extension_exists_on_disk():
    """Each pi.extensions entry must resolve to a real file, or Pi skips it."""
    extensions = _pi_manifest().get("extensions", [])
    missing = [e for e in extensions if not (REPO / e).is_file()]
    assert not missing, (
        "pi.extensions entries that Pi silently skips (existsSync miss): "
        f"{missing}. Point them at files that actually ship in the package."
    )
