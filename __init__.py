"""Hermes plugin: re-inject AGENTS.md context before each LLM call."""

import os
from pathlib import Path


def _read_agents(workspace: str) -> str:
    agents_path = Path(workspace) / "AGENTS.md"
    if agents_path.is_file():
        content = agents_path.read_text(encoding="utf-8")
        return content[:4000]
    return ""


def pre_llm_call(**kwargs) -> str:
    """Re-inject AGENTS.md context before each LLM call."""
    workspace = kwargs.get("workspace", os.getcwd())
    excerpt = _read_agents(workspace)
    if excerpt:
        return f"## Re-injected AGENTS.md (context persistence)\n{excerpt}"
    return ""


def register(ctx):
    """Register the pre_llm_call hook with Hermes."""
    ctx.register_hook("pre_llm_call", pre_llm_call)
