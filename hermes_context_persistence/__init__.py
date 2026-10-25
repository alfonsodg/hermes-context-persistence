"""Hermes plugin: re-inject AGENTS.md context after compaction."""

import os
from pathlib import Path


def post_compaction(context: dict) -> str:
    """Re-inject AGENTS.md content after compaction."""
    workspace = context.get("workspace", os.getcwd())
    agents_path = Path(workspace) / "AGENTS.md"
    if agents_path.is_file():
        content = agents_path.read_text(encoding="utf-8")
        excerpt = content[:4000]
        return f"## Re-injected AGENTS.md (context persistence)\n{excerpt}"
    return ""


def register(plugin_api):
    """Register the post_compaction hook with Hermes."""
    plugin_api.register_hook("post_compaction", post_compaction)
